#!/usr/bin/env python3
"""Retrieve the full text of a paper, from an arXiv id or from a paper URL.

An abstract is enough to rank a paper and not enough to write about one. This
fetches the body so a brief can quote numbers and mechanisms rather than
paraphrasing the abstract back.

This script exists because `view_text_website` returns a page as plain text and
cannot read a PDF. Most conference proceedings -- every NDSS paper, for one --
are published only as a PDF, so they have to come through here. It was arXiv-only
until a conference brief was written from eight NDSS landing pages it had no
route to, and shipped eight items whose entire body was the abstract-only marker.

Routes, and why:

  arXiv id, or an arXiv URL in any of its forms
  1. https://arxiv.org/html/<id>   arXiv's own LaTeXML rendering. Class-tagged
                                   (ltx_abstract, ltx_section, ltx_bibliography),
                                   so the parts worth keeping are identifiable
                                   rather than guessed at. Coverage is broad --
                                   papers back to 2007 render -- and it 404s
                                   cleanly when a paper has none.
  2. https://arxiv.org/pdf/<id>    Only when there is no HTML. Layout-recovered
                                   text: usable, but hyphenated across line
                                   breaks and column-order dependent.

  any other http(s) URL
  3. the URL itself                Sniffed: a body starting %PDF *is* the paper.
                                   Otherwise it is a landing page, and the paper
                                   PDF it links to is fetched instead. Extension
                                   and Content-Type are both unreliable; the
                                   magic bytes are what pypdf actually needs.

  and if none of that worked
  4. abstract                      Whatever the caller already had, if anything.
                                   With an abstract the post formats carry an
                                   explicit marker: "*Abstract only - full text
                                   not retrieved.*" Say so rather than implying
                                   the paper was read. With *nothing* -- the case
                                   that produced the empty NDSS brief -- the
                                   source is "none" and the item must not be
                                   written up at all.

Do NOT add ar5iv as a source. ar5iv.org and ar5iv.labs.arxiv.org now redirect to
arxiv.org/abs/<id>, which returns HTTP 200 and the abstract landing page -- so a
naive "try ar5iv first" reports success while silently yielding no full text at
all. This was measured, not assumed.

Requires beautifulsoup4, html2text and pypdf (see requirements.txt). This is an
ingestion tool; it is deliberately not imported by anything on the merge path.

Usage:
    fulltext.py 2609.13353
    fulltext.py https://arxiv.org/abs/2609.13353v2
    fulltext.py https://www.ndss-symposium.org/ndss-paper/<slug>/ --json
    fulltext.py https://example.tld/paper.pdf --max-chars 20000
"""

from __future__ import annotations

import argparse
import io
import ipaddress
import json
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

import idstate

HTML_URL = "https://arxiv.org/html/{ident}"
PDF_URL = "https://arxiv.org/pdf/{ident}"
UA = "research_diary-fulltext/1.0 (+https://github.com/<GITHUB_USERNAME>/research_diary)"
PER_HOST_DELAY = 3.0
TIMEOUT = 60
# A landing page can point at a file of any size. 40 MB is well past the largest
# paper PDF and far short of anything that would exhaust the runner.
MAX_BYTES = 40 * 1024 * 1024
MAX_REDIRECTS = 3
PDF_MAGIC = b"%PDF"
# Blocks LaTeXML marks as non-body: references, the table of contents, the author
# block, and the maths/markup that html2text would render as noise.
DROP_TAGS = ("script", "style", "math", "svg", "nav", "form", "button")
DROP_CLASSES = (
    "ltx_bibliography",
    "ltx_TOC",
    "ltx_authors",
    "ltx_page_footer",
    "ltx_page_header",
)
# Anchor text on a landing page that is never the paper itself.
NOT_THE_PAPER = re.compile(r"\A(?:slides?|video|poster|talk)\Z", re.I)

_last_hit: dict[str, float] = {}


class Unavailable(Exception):
    """No text could be retrieved by this route."""


def _safe(url: str) -> str | None:
    """Reject anything that is not a plain public http(s) fetch.

    Same guard as linkcheck.py, and for the same reason: these fetches are driven
    by identifiers that came out of untrusted pages.
    """
    p = urllib.parse.urlsplit(url)
    if p.scheme not in ("http", "https"):
        return f"not an http(s) URL: {url}"
    host = p.hostname
    if not host:
        return f"no host in URL: {url}"
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return f"unresolvable host: {url}"
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            return f"resolves to a non-public address ({ip}): {url}"
    return None


class _SafeRedirect(urllib.request.HTTPRedirectHandler):
    """Re-run the SSRF guard on every hop.

    urlopen follows redirects by itself and _safe() only ever saw the first URL,
    so https://evil.tld/r -> http://169.254.169.254/ was one redirect away. That
    was always true; the landing-page route is what makes it reachable from a
    page the pipeline did not choose. arXiv's /pdf/<id> legitimately redirects,
    so the hops are checked and capped rather than refused.
    """

    max_repeats = MAX_REDIRECTS
    max_redirections = MAX_REDIRECTS

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        problem = _safe(newurl)
        if problem:
            raise Unavailable(f"refused a redirect to {problem}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _throttle(host: str) -> None:
    last = _last_hit.get(host)
    if last is not None:
        wait = PER_HOST_DELAY - (time.monotonic() - last)
        if wait > 0:
            time.sleep(wait)
    _last_hit[host] = time.monotonic()


def fetch(url: str) -> bytes:
    problem = _safe(url)
    if problem:
        raise Unavailable(problem)
    _throttle(urllib.parse.urlsplit(url).hostname or "")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    opener = urllib.request.build_opener(_SafeRedirect)
    try:
        with opener.open(req, timeout=TIMEOUT) as resp:
            return resp.read(MAX_BYTES)
    except urllib.error.HTTPError as exc:
        raise Unavailable(f"HTTP {exc.code} for {url}") from exc
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        raise Unavailable(f"{exc} for {url}") from exc


def plan(target: str) -> list[tuple[str, str]]:
    """The ordered (route, url) attempts for a target. Pure: no network, no I/O.

    `route` is "html" or "pdf" for arXiv, and "landing" for everything else --
    see _render for what a landing route does.

    idstate.canonical answers the only question asked of it here, "is this an
    arXiv paper", and its normalized form is deliberately not used as a URL: it
    coerces everything else into one, turning "not a paper" into
    https://not a paper/ and file:///etc/passwd into https:///etc/passwd. The
    scheme is therefore tested on the caller's own string, and that string is
    what gets fetched.
    """
    kind, ident = idstate.canonical(target)
    if kind == "arxiv":
        return [("html", HTML_URL.format(ident=ident)), ("pdf", PDF_URL.format(ident=ident))]
    if urllib.parse.urlsplit(target).scheme in ("http", "https"):
        return [("landing", target)]
    raise Unavailable(f"not an arXiv id or an http(s) URL: {target!r}")


class _Anchors(HTMLParser):
    """Every <a> on a page, as {"href", "classes", "text"}.

    stdlib rather than BeautifulSoup on purpose. This is the code that decides
    which URL gets fetched out of an untrusted page, so it has to run in the half
    of test_fulltext.py that is *not* skipped when bs4 is missing -- which is CI,
    where nothing is installed. Nothing is lost by it either: html_to_text hands
    bs4 "html.parser" anyway, so the underlying parser is the same one.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[dict] = []
        self._open: dict | None = None

    def _flush(self) -> None:
        if self._open is None:
            return
        self._open["text"] = " ".join("".join(self._open["text"]).split())
        self.links.append(self._open)
        self._open = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        self._flush()  # an unclosed <a>: keep it rather than losing it to the next
        a = dict(attrs)
        self._open = {
            "href": (a.get("href") or "").strip(),
            "classes": (a.get("class") or "").split(),
            "text": [],
        }

    def handle_data(self, data: str) -> None:
        if self._open is not None:
            self._open["text"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a":
            self._flush()

    def close(self) -> None:
        super().close()
        self._flush()


def _host(url: str) -> str:
    return (urllib.parse.urlsplit(url).hostname or "").lower().removeprefix("www.")


def paper_link(page_url: str, document: str) -> str:
    """The absolute URL of the paper PDF linked from a conference landing page.

    Lexical only -- no DNS and no fetching -- so it runs offline in the tests.
    _safe() still applies to whatever comes back, inside fetch().

    NDSS marks the paper <a class="... pdf-button">Paper</a> and the deck
    <a class="... button-slides">Slides</a>. Excluding the deck is not cosmetic:
    a slide deck is also a PDF, so picking one up would report source="pdf" for
    a brief written off someone's bullet points. Only the class and text rules
    are NDSS-shaped; the exclusions and the trailing ".pdf" rule are generic
    enough to carry most WordPress-backed programme pages.
    """
    parser = _Anchors()
    parser.feed(document)
    parser.close()

    ranked: list[tuple[int, str]] = []
    for link in parser.links:
        href = link["href"]
        if not href:
            continue
        scheme = urllib.parse.urlsplit(href).scheme.lower()
        if scheme and scheme not in ("http", "https"):
            continue  # javascript:, mailto:, data:
        resolved, _ = urllib.parse.urldefrag(urllib.parse.urljoin(page_url, href))
        parts = urllib.parse.urlsplit(resolved)
        if parts.scheme not in ("http", "https"):
            continue
        if _host(resolved) != _host(page_url):
            continue  # a paper is served by the venue; never follow one off-site
        path = parts.path.lower()
        text = link["text"]
        if "button-slides" in link["classes"] or NOT_THE_PAPER.match(text) or "slides" in path:
            continue
        if "pdf-button" in link["classes"]:
            ranked.append((0, resolved))
        elif text.casefold() == "paper":
            ranked.append((1, resolved))
        elif path.endswith(".pdf"):
            ranked.append((2, resolved))
    if not ranked:
        raise Unavailable(f"no paper PDF link on {page_url}")
    return min(ranked, key=lambda r: r[0])[1]


def html_to_text(document: str) -> str:
    """Body text of an arXiv LaTeXML page, references and furniture removed.

    Selecting the <article> and dropping blocks by class beats walking the tag
    tree and counting depth: one unclosed element inside a dropped region wedges
    a depth counter and silently returns almost nothing.
    """
    from bs4 import BeautifulSoup  # imported lazily so --help works without deps
    import html2text

    soup = BeautifulSoup(document, "html.parser")
    article = soup.find("article", class_=lambda c: c and "ltx_document" in c)
    if article is None:
        raise Unavailable("no <article class='ltx_document'> in the page")

    for tag in DROP_TAGS:
        for node in article.find_all(tag):
            node.decompose()
    for cls in DROP_CLASSES:
        for node in article.find_all(class_=lambda c, want=cls: c and want in c):
            node.decompose()

    converter = html2text.HTML2Text()
    converter.ignore_links = True
    converter.ignore_images = True
    converter.body_width = 0
    return _tidy(converter.handle(str(article)))


def pdf_to_text(data: bytes) -> str:
    from pypdf import PdfReader  # imported lazily so --help works without deps

    reader = PdfReader(io.BytesIO(data))
    pages = [(page.extract_text() or "") for page in reader.pages]
    return _tidy(dehyphenate("\n".join(pages)))


def dehyphenate(text: str) -> str:
    """Rejoin words a PDF broke across a line end ("evalua-\ntions").

    Left in, every such word is unsearchable and unquotable. Joining without the
    hyphen is right for a syllable break and wrong for a compound that happens to
    land on the line end ("language-model" -> "languagemodel"); the former is far
    more common in justified two-column text and neither is distinguishable
    without a dictionary. One of several reasons HTML is tried first.

    Its own function so it can be tested without constructing a PDF.
    """
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def _tidy(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _render(route: str, url: str) -> tuple[str, str, str]:
    """Fetch one route and convert it. Returns (source, url converted, text).

    The converters are named here rather than held in a lookup table built at
    import: test_fulltext.py stubs F.fetch, F.html_to_text and F.pdf_to_text, and
    a table would capture the originals and make every stubbed test pass against
    the real functions.
    """
    raw = fetch(url)
    if route == "html":
        return "html", url, html_to_text(raw.decode("utf-8", "replace"))
    if route == "pdf":
        return "pdf", url, pdf_to_text(raw)

    # "landing". One hop only: a PDF found on a page is never re-scanned for
    # links, so a page cannot walk the fetcher around a site.
    if raw[: len(PDF_MAGIC)] == PDF_MAGIC:
        return "pdf", url, pdf_to_text(raw)
    link = paper_link(url, raw.decode("utf-8", "replace"))
    body = fetch(link)
    if body[: len(PDF_MAGIC)] != PDF_MAGIC:
        raise Unavailable(f"{link} did not answer with a PDF")
    return "pdf", link, pdf_to_text(body)


def retrieve(target: str, abstract: str = "", max_chars: int = 0) -> dict:
    """Return {"id", "source", "url", "text", "chars", "notes"}.

    `source` is "html", "pdf", "abstract" or "none" -- the caller needs to know
    which, because only the first two justify writing as though the paper was
    read. "abstract" means an abstract was supplied and nothing better was
    reachable: mark the item. "none" means nothing at all came back, and the item
    must not be written up in any form -- that case used to return an empty
    string dressed as a successful abstract, and a brief was written from it.
    """
    notes: list[str] = []
    try:
        attempts = plan(target)
    except Unavailable as exc:
        notes.append(str(exc))
        attempts = []

    for route, url in attempts:
        try:
            source, final, text = _render(route, url)
        except Unavailable as exc:
            notes.append(f"{route}: {exc}")
            continue
        except ImportError as exc:
            notes.append(f"{route}: missing dependency ({exc}); see requirements.txt")
            continue
        except Exception as exc:  # noqa: BLE001 - a malformed paper must not abort the run
            notes.append(f"{route}: could not parse ({exc.__class__.__name__}: {exc})")
            continue
        if not text.strip():
            notes.append(f"{route}: parsed to empty text")
            continue
        if max_chars and len(text) > max_chars:
            text = text[:max_chars].rstrip() + "\n\n[truncated]"
        return {
            "id": target,
            "source": source,
            "url": final,
            "text": text,
            "chars": len(text),
            "notes": notes,
        }

    text = _tidy(abstract)
    if text:
        notes.append("fell back to the abstract; mark the item *Abstract only* in the post")
        return {
            "id": target,
            "source": "abstract",
            "url": "",
            "text": text,
            "chars": len(text),
            "notes": notes,
        }
    notes.append("nothing was retrieved and no abstract was supplied; do not write this item up")
    return {"id": target, "source": "none", "url": "", "text": "", "chars": 0, "notes": notes}


def exit_code(source: str) -> int:
    """0 the paper was read, 1 only an abstract, 3 nothing at all.

    3 rather than 2 because argparse already exits 2 on a usage error, and a
    caller shelling out could not otherwise tell a mistyped flag from a paper it
    is not allowed to write about.
    """
    if source in ("html", "pdf"):
        return 0
    return 1 if source == "abstract" else 3


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("target", help="arXiv id (2609.13353), or the URL of a paper or its page")
    ap.add_argument("--abstract", default="", help="fallback text if no full text is available")
    ap.add_argument("--max-chars", type=int, default=0, help="truncate the body at N characters")
    ap.add_argument("--json", action="store_true", help="emit one JSON object instead of text")
    args = ap.parse_args(argv)

    result = retrieve(args.target, args.abstract, args.max_chars)
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(
            f"# source: {result['source']}  chars: {result['chars']}"
            + (f"  url: {result['url']}" if result["url"] else ""),
            file=sys.stderr,
        )
        for note in result["notes"]:
            print(f"# note: {note}", file=sys.stderr)
        print(result["text"])
    return exit_code(result["source"])


if __name__ == "__main__":
    sys.exit(main())
