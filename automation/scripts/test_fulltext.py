#!/usr/bin/env python3
"""Offline checks for fulltext.py.

Two halves. The first needs no third-party packages and always runs: the SSRF
guard, route planning, the landing-page link resolver, the fallback chain, and
the de-hyphenation. The second parses a real arXiv HTML skeleton and is SKIPPED
when beautifulsoup4/html2text are absent -- this must not fail, because the
merge-path CI job installs nothing on purpose and would otherwise go red for a
tool it never runs.

paper_link is deliberately in the first half. It is the code that decides which
URL gets fetched out of an untrusted page, so it must be exercised on every run
rather than only where bs4 happens to be installed.

Nothing here touches the network: the fetch is stubbed, so a run is fast and
cannot be broken by arXiv being slow.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import fulltext as F  # noqa: E402

FAILURES: list[str] = []
SKIPPED: list[str] = []


def check(label: str, got, want) -> None:
    if got != want:
        FAILURES.append(f"{label}\n      got:  {got!r}\n      want: {want!r}")


def check_true(label: str, got) -> None:
    if not got:
        FAILURES.append(label)


def check_raises(label: str, fn) -> None:
    try:
        fn()
    except F.Unavailable:
        return
    FAILURES.append(label)


# --- the SSRF guard ----------------------------------------------------------
# These identifiers came out of untrusted pages, and the fetch runs next to a
# token, so the same guard linkcheck.py uses applies here.
for bad in (
    "file:///etc/passwd",
    "ftp://example.tld/x",
    "http://127.0.0.1/x",
    "http://localhost/x",
    "http://169.254.169.254/latest/meta-data/",
    "http://10.0.0.1/x",
    "http://[::1]/x",
):
    check_true(f"refuses {bad}", F._safe(bad) is not None)

check("allows a normal public https URL", F._safe("https://arxiv.org/html/2609.13353"), None)
check_true("a URL with no host is refused", F._safe("https:///x") is not None)


# --- route planning ----------------------------------------------------------
# Pure, so it is checked directly rather than inferred from which URLs got hit.
NDSS_PAGE_URL = "https://www.ndss-symposium.org/ndss-paper/a-memory-safety-analysis/"

check(
    "a bare arXiv id plans html then pdf",
    F.plan("2609.13353"),
    [("html", "https://arxiv.org/html/2609.13353"), ("pdf", "https://arxiv.org/pdf/2609.13353")],
)
check(
    "an arXiv abs URL with a version suffix plans the same routes",
    F.plan("https://arxiv.org/abs/2609.13353v2"),
    F.plan("2609.13353"),
)
check(
    "a conference URL plans one landing route, verbatim",
    F.plan(NDSS_PAGE_URL),
    [("landing", NDSS_PAGE_URL)],
)
# idstate.canonical coerces anything non-arXiv into a URL -- "not a paper" comes
# back as https://not a paper/ and file:///etc/passwd as https:///etc/passwd -- so
# plan() must test the scheme on the caller's own string, not on that form.
check_raises("prose is not a target", lambda: F.plan("not a paper"))
check_raises("a file:// URL is not a target", lambda: F.plan("file:///etc/passwd"))


# --- the landing-page link resolver ------------------------------------------
# The markup NDSS actually serves: a paper button and a slides button side by
# side, both PDFs on the same host.
NDSS_PAGE = """<!DOCTYPE html><html><body>
<article class="post-20003 ndss-paper category-ndss-2025">
  <div class="paper-data"><p>Abstract-The bootloader plays an important role.</p></div>
  <div class="paper-buttons">
    <div class="btn-group-vertical" role="group">
      <a role="button" class="btn btn-light btn-sm pdf-button" target="_blank"
         href="https://www.ndss-symposium.org/wp-content/uploads/2025-330-paper.pdf">Paper</a>
    </div>
    <div class="btn-group-vertical" role="group">
      <a role="button" class="btn btn-light btn-sm button-slides" target="_blank"
         href="https://www.ndss-symposium.org/wp-content/uploads/8C-f0330-Sihag.pdf">Slides</a>
    </div>
    <a href="https://youtu.be/QiO154VIyk8">Video</a>
  </div>
</article></body></html>"""

check(
    "the paper PDF is resolved from the landing page",
    F.paper_link(NDSS_PAGE_URL, NDSS_PAGE),
    "https://www.ndss-symposium.org/wp-content/uploads/2025-330-paper.pdf",
)
# The honesty case. A slide deck is also a PDF on the same host, so a resolver
# that took the first .pdf would report source="pdf" for a brief written off
# someone's bullet points.
check_true(
    "the slide deck is never taken for the paper",
    "Sihag" not in F.paper_link(NDSS_PAGE_URL, NDSS_PAGE),
)
check(
    "a relative href resolves against the page",
    F.paper_link(NDSS_PAGE_URL, '<a class="pdf-button" href="/wp-content/uploads/x.pdf">Paper</a>'),
    "https://www.ndss-symposium.org/wp-content/uploads/x.pdf",
)
check(
    "a fragment is dropped",
    F.paper_link(NDSS_PAGE_URL, '<a href="/p.pdf#page=3">Paper</a>'),
    "https://www.ndss-symposium.org/p.pdf",
)
# A paper is served by the venue. Following a link off-site would let a page the
# pipeline did not choose pick the host that gets fetched.
check_raises(
    "an off-host pdf-button is refused",
    lambda: F.paper_link(NDSS_PAGE_URL, '<a class="pdf-button" href="https://evil.tld/p.pdf">Paper</a>'),
)
check_raises(
    "a javascript: href is refused",
    lambda: F.paper_link(NDSS_PAGE_URL, '<a class="pdf-button" href="javascript:void(0)">Paper</a>'),
)
check_raises("a page with no links yields nothing", lambda: F.paper_link(NDSS_PAGE_URL, "<p>hi</p>"))
# HTMLParser is lenient where a strict parser would give up, and conference
# pages are hand-maintained WordPress.
check(
    "an unclosed anchor still yields its link",
    F.paper_link(
        NDSS_PAGE_URL,
        '<a class="button-slides" href="/s.pdf">Slides<a class="pdf-button" href="/p.pdf">Paper',
    ),
    "https://www.ndss-symposium.org/p.pdf",
)


# --- the fallback chain ------------------------------------------------------
# The order is html -> pdf -> abstract, and the caller must be able to tell which
# happened: only the first two justify writing as though the paper was read.
PAPER_PDF = "https://www.ndss-symposium.org/wp-content/uploads/2025-330-paper.pdf"


def stub(html=None, pdf=None, landing=None, paper=None):
    """A fetch that answers by URL shape. `landing` is the page, `paper` its PDF."""

    def _fetch(url: str) -> bytes:
        if url == NDSS_PAGE_URL:
            body = landing
        elif url == PAPER_PDF:
            body = paper
        elif "/html/" in url:
            body = html
        else:
            body = pdf
        if body is None:
            raise F.Unavailable("HTTP 404 for " + url)
        return body

    return _fetch


real_fetch, real_html, real_pdf = F.fetch, F.html_to_text, F.pdf_to_text
try:
    F.html_to_text = lambda doc: "HTML BODY"
    F.pdf_to_text = lambda data: "PDF BODY"

    F.fetch = stub(html=b"<html/>", pdf=b"%PDF")
    r = F.retrieve("2609.13353", abstract="ABS")
    check("html wins when it is available", (r["source"], r["text"]), ("html", "HTML BODY"))
    check("the converted URL is reported", r["url"], "https://arxiv.org/html/2609.13353")

    F.fetch = stub(html=None, pdf=b"%PDF")
    r = F.retrieve("2609.13353", abstract="ABS")
    check("falls back to pdf when there is no html", (r["source"], r["text"]), ("pdf", "PDF BODY"))
    check_true("the html failure is reported", any("html:" in n for n in r["notes"]))

    # The NDSS case, end to end: a landing page is fetched, its paper link
    # resolved, and the PDF behind it converted. This is what the pipeline had no
    # route for, and why eight papers were written up from an empty string.
    F.fetch = stub(landing=NDSS_PAGE.encode(), paper=b"%PDF body")
    r = F.retrieve(NDSS_PAGE_URL)
    check("a landing page resolves to its paper PDF", (r["source"], r["text"]), ("pdf", "PDF BODY"))
    check("the resolved PDF URL is reported, not the page", r["url"], PAPER_PDF)

    # Sniffed, not guessed from the extension: a URL that is already the paper
    # must not be scanned for links, and a venue PDF may have no .pdf suffix.
    F.fetch = stub(landing=b"%PDF straight away")
    r = F.retrieve(NDSS_PAGE_URL)
    check("a URL that is already a PDF is converted directly", r["source"], "pdf")
    check("a direct PDF reports the URL it was given", r["url"], NDSS_PAGE_URL)

    F.fetch = stub(landing=b"<html><p>no paper here</p></html>")
    r = F.retrieve(NDSS_PAGE_URL)
    check("a landing page with no paper link does not succeed", r["source"], "none")
    check_true("the resolver failure is reported", any("no paper PDF link" in n for n in r["notes"]))

    # A link that answers with HTML must not be handed to pypdf and reported as
    # a read paper.
    F.fetch = stub(landing=NDSS_PAGE.encode(), paper=b"<html>not a pdf</html>")
    r = F.retrieve(NDSS_PAGE_URL)
    check("a paper link that answers with HTML is refused", r["source"], "none")

    F.fetch = stub(html=None, pdf=None)
    r = F.retrieve("2609.13353", abstract="ABS")
    check(
        "falls back to the abstract when neither renders",
        (r["source"], r["text"]),
        ("abstract", "ABS"),
    )
    check_true(
        "the abstract fallback says to mark the post",
        any("Abstract only" in n for n in r["notes"]),
    )

    # The bug this file exists for. With no abstract to fall back on -- which is
    # every conference item, because the backlog records carry no abstract -- the
    # old code returned source="abstract" with text="", and a brief was written
    # from it. "none" cannot be mistaken for a success.
    r = F.retrieve("2609.13353")
    check(
        "nothing retrieved and nothing supplied is source=none",
        (r["source"], r["chars"], r["text"]),
        ("none", 0, ""),
    )
    check_true(
        "the empty case says not to write the item up",
        any("do not write this item up" in n for n in r["notes"]),
    )
    r = F.retrieve("2609.13353", abstract="   \n  ")
    check("a whitespace-only abstract is not an abstract", r["source"], "none")

    # An empty parse is a failure, not a success with no text -- otherwise a post
    # would be written from nothing while reporting source=html.
    F.fetch = stub(html=b"<html/>", pdf=b"%PDF")
    F.html_to_text = lambda doc: "   \n  "
    r = F.retrieve("2609.13353", abstract="ABS")
    check("html that parses to whitespace falls through", r["source"], "pdf")

    # A malformed paper must cost that paper, not abort the run.
    F.html_to_text = lambda doc: (_ for _ in ()).throw(ValueError("broken"))
    r = F.retrieve("2609.13353", abstract="ABS")
    check("a parser exception is caught and recorded", r["source"], "pdf")
    check_true("the parser failure is reported", any("ValueError" in n for n in r["notes"]))

    F.html_to_text = lambda doc: "x" * 100
    F.fetch = stub(html=b"<html/>")
    r = F.retrieve("2609.13353", max_chars=40)
    check_true("max_chars truncates", r["chars"] <= 60 and r["text"].endswith("[truncated]"))
finally:
    F.fetch, F.html_to_text, F.pdf_to_text = real_fetch, real_html, real_pdf


# --- what the caller sees from the shell -------------------------------------
# A wrapper shelling out needs to tell "read the paper" from "did not", and both
# from a mistyped flag, which argparse already answers with 2.
check(
    "exit codes distinguish the four outcomes",
    [F.exit_code(s) for s in ("html", "pdf", "abstract", "none")],
    [0, 0, 1, 3],
)


# --- text tidying ------------------------------------------------------------
check("collapses runs of blank lines", F._tidy("a\n\n\n\n\nb"), "a\n\nb")
check("collapses horizontal whitespace", F._tidy("a     b"), "a b")
check("strips non-breaking spaces", F._tidy("a\xa0b"), "a b")

# Justified two-column PDFs break words at the line end. Its own function so this
# needs no PDF, and so it runs even where pypdf is not installed.
check("rejoins a word broken across a line", F.dehyphenate("evalua-\ntions"), "evaluations")
check("leaves a hyphen that is not at a line end", F.dehyphenate("side-channel"), "side-channel")
check("leaves a hyphen before a blank line", F.dehyphenate("foo-\n\nbar"), "foo-\n\nbar")
check("handles several breaks", F.dehyphenate("aaa-\nbbb ccc-\nddd"), "aaabbb cccddd")


# --- the library-backed half -------------------------------------------------
try:
    import bs4  # noqa: F401
    import html2text  # noqa: F401
except ImportError as exc:
    SKIPPED.append(f"HTML extraction checks: {exc}. Install requirements.txt to run them.")
else:
    # The shape arXiv's LaTeXML renderer actually emits: an ltx_document article,
    # class-tagged sections, and a bibliography that must not reach the output.
    PAGE = """<!DOCTYPE html><html><head><title>t</title></head><body>
    <nav class="ltx_TOC"><a href="#S1">Table of contents junk</a></nav>
    <div class="ltx_page_content">
      <article class="ltx_document">
        <h1 class="ltx_title">A Practical Attack</h1>
        <div class="ltx_authors">Ada Lovelace</div>
        <div class="ltx_abstract"><h6>Abstract</h6><p>We broke the thing.</p></div>
        <section class="ltx_section"><h2>1 Introduction</h2>
          <p class="ltx_para">The introduction body text.</p>
          <math alttext="x^2"><mi>x</mi></math>
        </section>
        <script>var tracking = 1;</script>
        <section class="ltx_bibliography"><h2>References</h2>
          <li class="ltx_bibitem">Someone. A cited work. 1999.</li>
        </section>
      </article>
    </div></body></html>"""

    text = F.html_to_text(PAGE)
    check_true("the abstract survives", "We broke the thing." in text)
    check_true("body prose survives", "The introduction body text." in text)
    check_true("the bibliography is removed", "A cited work" not in text)
    check_true("the table of contents is removed", "Table of contents junk" not in text)
    check_true("the author block is removed", "Ada Lovelace" not in text)
    check_true("scripts are removed", "tracking" not in text)

    # An abs landing page has no ltx_document article. This is the ar5iv trap:
    # ar5iv now redirects to /abs/, which is HTTP 200 with no full text, so a
    # parser that returned "" here would report success having read nothing.
    try:
        F.html_to_text("<html><body><p>Just an abstract page.</p></body></html>")
        FAILURES.append("a page with no ltx_document article must raise Unavailable")
    except F.Unavailable:
        pass

for note in SKIPPED:
    print(f"skipped: {note}")

if FAILURES:
    print(f"fulltext: FAILED ({len(FAILURES)}):\n")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
print(f"fulltext: all checks passed{f' ({len(SKIPPED)} skipped)' if SKIPPED else ''}")
