# research_diary

![research_diary](assets/research_diary_logo.jpg)

A technical research diary: daily briefs on newly published security and CS work, plus long-form
deep dives. Content is researched and written by [Google Jules](https://jules.google/), built with
[Hugo](https://gohugo.io) and [PaperMod](https://github.com/adityatelange/hugo-PaperMod), and
published to [GitHub Pages](https://docs.github.com/en/pages).

Sources: arXiv, USENIX Security, USENIX WOOT, IEEE S&P, NDSS, ACM CCS, Oakland SoK, DEF CON,
Black Hat and [un]prompted — plus open web search, so the diary is not limited to those.

## How it works

```
Jules web console  ──>  Jules VM reads AGENTS.md  ──>  pull request
                                                          │
                              validate-content.yml  <─────┤   advisory — runs the PR's own code
                              path guard, schema, build    │
                                                          │
                              auto-merge.yml       <──────┘   the trust boundary — runs from main
                              re-runs main's path guard,
                              linkcheck, then merges
                                     │
                                     └──>  pages.yml  ──>  GitHub Pages
```

Nothing in this repository calls Jules. The schedule and the prompts live in the Jules console; the
repository carries the specification Jules reads (`AGENTS.md`), the tooling it runs
(`automation/scripts/`), and the checks that gate its output.

| Layer | Owns |
|---|---|
| Jules console | Repo connection, Initial Setup, the two daily scheduled tasks, manual deep dives |
| This repo | `AGENTS.md`, research scope, helper scripts, dedup state, Hugo layout |
| GitHub Actions | PR validation, auto-merge, deploy |

## Quick start

1. Clone the repo.
1. Install [Hugo](https://gohugo.io/installation/) (extended) and [Go](https://go.dev/doc/install)
   — Go is needed because the theme is a Hugo module.
1. Fetch the theme:

   ```shell
   hugo mod get -u github.com/adityatelange/hugo-PaperMod
   ```

1. Preview at <http://localhost:1313/>:

   ```shell
   hugo server
   ```

1. Run the pipeline's own tests. They need no dependencies — the tests covering `fulltext.py`'s
   HTML and PDF extraction skip themselves when the packages are absent, and report that they did:

   ```shell
   for t in automation/scripts/test_*.py; do python3 "$t" || break; done
   ```

   To run those skipped checks too, install the ingestion dependencies. A virtualenv is the usual
   way; on a PEP 668 system without `python3-venv` available, install to a directory instead:

   ```shell
   python3 -m pip install --target .pylibs -r requirements.txt
   PYTHONPATH=.pylibs python3 automation/scripts/test_fulltext.py
   ```

   `.pylibs/` is gitignored.

No local Hugo install? Use Docker, pulling the same pinned `.deb` CI installs. Do **not** use
`hugomods/hugo:exts` — it floats, currently ships Hugo v0.154.5, and that predates
`.Language.Direction`, so it cannot render the forked templates in `layouts/` and fails on every
page with `can't evaluate field Direction in type *langs.Language`.

```shell
docker run --rm -p 1313:1313 -v "$PWD":/src -w /src \
  -e HUGO_VERSION=0.166.0 \
  -e HUGO_SHA256=52b06555f739b1a08e04f5c31296e9bdf166a012e9b7e3137befc889dbc24db8 \
  golang:1.23-bookworm sh -c '
    set -e
    apt-get update -qq && apt-get install -y -qq curl git
    curl -sSL -o /tmp/hugo.deb \
      "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
    echo "${HUGO_SHA256}  /tmp/hugo.deb" | sha256sum -c -
    dpkg -i /tmp/hugo.deb
    git config --global --add safe.directory /src
    hugo mod get -u github.com/adityatelange/hugo-PaperMod
    hugo server --bind 0.0.0.0'
git checkout -- go.mod go.sum   # hugo mod get rewrites these
```

`HUGO_VERSION` and `HUGO_SHA256` must match `.github/workflows/pages.yml`; bump them together.
To simulate the full CI build against the production URL instead, see §7 of the reference.

## Configuration

See **[`REFERENCE_caa20260903_153422.md`](REFERENCE_caa20260903_153422.md)** for the full
configuration reference: every PaperMod param, the CSS-variable colour and layout system, what
cannot be configured without overriding theme templates, and which settings are dead no-ops.

Short version:

| Change | Where |
|---|---|
| What gets researched (interests, sources, tags) | `automation/config/topics.toml` |
| How Jules behaves | `AGENTS.md` |
| Site title, menus, params | `config.toml` |
| Colours, fonts, layout geometry | `assets/css/extended/custom.css` |
| Pages and posts | `content/` |
| Files served at site root | `static/` |
| What changed and why (code, config, docs — not posts) | `CHANGES.md` |

## The content pipeline

### One-time setup in the Jules console

1. Connect `<GITHUB_USERNAME>/research_diary` (installs the Jules GitHub App).
2. Configure the environment and snapshot it — see below. `fulltext.py` needs three packages;
   without them every paper falls back to abstract-only.
3. Create the scheduled task — but only after a manual run has produced output you trust.

### Jules console environment

**Jules → Configure repo → Environment → run and snapshot.**

Python 3.12 is preinstalled. Most of the tooling is stdlib, but the ingestion tools need three
packages, so the environment setup script is:

```shell
pip install -r requirements.txt
```

Run it, and once it succeeds **take the snapshot**. Jules reuses that snapshot for every later task
started from this repository, so the install cost is paid once instead of on every run — which
matters here, because the arXiv brief runs daily.

Three things worth knowing, because each one fails quietly:

- **Re-run and re-snapshot whenever `requirements.txt` changes.** A stale snapshot keeps the old
  packages, and the failure looks like a content problem rather than an environment one:
  `fulltext.py` cannot import `bs4` or `pypdf`, reports `source: abstract` or `source: none`, and
  the brief is thinner than it should be — or, for a conference paper with no abstract to fall back
  on, the item is dropped entirely. `AGENTS.md` tells Jules to report an import failure rather than
  work around it.
- **Initial Setup must run `pip install -r requirements.txt`.** The ingestion tools are the one
  part of this repo that is not stdlib-only, so an empty setup script leaves them unusable.
- **CI installs none of this.** The checks that gate a merge — `pathguard.py`, `validate.py`,
  `postparse.py`, `linkcheck.py` — are deliberately stdlib-only, so no third-party package sits
  between an untrusted pull request and a write token. A broken snapshot therefore shows up as a
  failed Jules run, never as a bad merge.

### The console prompts

These live only in the Jules UI, which is not version controlled and cannot be restored from git.
They are recorded here so they can be recreated:

**arXiv brief** — Scheduled Task, Daily:

```
Run the arXiv brief pipeline exactly as specified in AGENTS.md.
```

**Conference brief** — Scheduled Task, Daily:

```
Run the conference brief pipeline exactly as specified in AGENTS.md.
```

**Deep dive** — a normal task, run by hand, in one of two modes:

```
Run the deep dive pipeline as specified in AGENTS.md. [Exploration] Topic: <your topic>
Run the deep dive pipeline as specified in AGENTS.md. [Detailed breakdown] Topic: <your topic>
Run the deep dive pipeline as specified in AGENTS.md. Topic: <your topic>
```

The marker selects the mode. `[Exploration]` maps a whole topic, breadth first; `[Detailed
breakdown]` takes one mechanism apart, depth first. Both run the same research pipeline against the
same source funnel — the mode changes what Jules looks for and how closely it reads, not how much it
looks. It reaches the published post as a prefix on the title and as the post's first tag, so the
mode is visible on the page and each mode gets its own `/tags/` archive.

The marker goes before `Topic:`, so everything after that word is the topic. The third form is the
predecessor of the other two and still works: no marker means `[Exploration]`, and Jules says so in
its report.

The pipeline names must match the headings in `AGENTS.md` exactly, and the two marker spellings must
match §5 — with a one-line prompt, those words are the only thing selecting which procedure runs and
how deep it goes.

You supply the direction of research and nothing else. Which sources are worth reading, which of
them survive into the post, and how the topic divides up are Jules' to work out: §5 specifies the
grounding step, the three research stages and the funnel it filters them through.

Daily for the conference brief because of the backlog queue, not in spite of it. Every venue
source is `window = "unseen"`: they publish in one annual burst and then go quiet, so reading the
index pages daily would find nothing most days. The queue decouples the two — a programme is
enqueued once and `queue.py` hands out `brief_max_summarized` papers per run, so a 200-paper
conference becomes a couple of dozen ordinary briefs instead of one unusable post. With over a
thousand items enqueued there is material for months of consecutive runs, and it is only once a
programme is drained and no new one has been posted that a daily run starts spending itself to
discover nothing. That is still a valid outcome: it opens no pull request.

`check = "weekly"` on those sources is a separate number — how often a venue's **index page** is
worth re-reading for newly posted items, not how often the pipeline runs.

Both tasks running daily means both can open a pull request on the same day, and both write
`automation/state/seen.ndjson`. The sorted-NDJSON discipline in `queue.py` and `idstate.py` — one
record per line, sorted by key — is what keeps those diffs to a few lines each and stops them
conflicting. It is load-bearing now rather than theoretical.

"Hands out eight papers per run" holds only while each batch is closed out. `pending` order is
stable, so an item left `pending` is handed out again in the same slot on the next run; every one
that accumulates costs the batch a paper permanently. `AGENTS.md` §4 step 7 requires each item to
leave `pending` by `queue.py done` or `queue.py skip` on the run that received it, and `queue.py`
reports it when one does not.

They are one line on purpose. Everything else lives in `AGENTS.md` and `automation/config/topics.toml`,
where it is reviewable and diffable — and because a Jules scheduled task **cannot be edited** once
created, only deleted and recreated. Keeping the prompt stable means iterating on behaviour is a
pull request, not a UI round trip.

### What guards the output

Two workflows run, and only one of them gates.

`validate-content.yml` runs on every pull request Jules opens and is **advisory**: `on:
pull_request` executes the pull request's own copy of both the workflow and the scripts, so a pull
request that edits a check is judged by its own edited copy. A green tick there means nothing on
its own.

`auto-merge.yml` is **the trust boundary**. It runs `on: workflow_run`, which always executes the
default branch's copy, re-runs `main`'s path guard against the pull request's diff, and only then
merges. It never checks out or executes anything from the pull request.

What gets checked:

1. **Path guard** — the diff may only touch `content/arxiv/*.md`, `content/conferences/*.md`,
   `content/deep-dives/*.md` and `automation/state/*`. The pipeline's input is untrusted web content
   fed to an agent with repo write access, so this is the boundary that stops a poisoned paper from
   editing a workflow. Run from `main`, before any pull request file reaches the disk.
2. **Schema** — TOML frontmatter, RFC3339 UTC date, tags from the controlled vocabulary, required
   sections, and grounding: a source URL on *each* item rather than somewhere in the file, every
   citation matched to a reference and back, no conference index page standing in for a named paper,
   no two references sharing one URL, no placeholder identifiers. The deep dive's research starting
   points count as index pages too: a repository is somewhere to look and never something to cite,
   so `deep_dive.start_urls` and the venue index pages are the same blocklist.
3. **Link check** — the DOIs and arXiv IDs cited must resolve, and an arXiv ID must be the paper the
   post says it is. Only `doi.org` and `arxiv.org` are gating; everything else is reported and not
   enforced, because publishers such as ACM, Black Hat and CISA return 403 to a datacenter IP and
   gating on them would fail good pull requests.
4. **Build** — Hugo must actually render each changed page. `buildFuture = false` means a
   future-dated page is dropped *silently*, so a green build is not by itself evidence.

Passing all four auto-merges and triggers the deploy. Failing leaves the pull request open.

The schema and link checks are deliberately in code rather than in prose: anything stated only in
`AGENTS.md` is advisory, because the agent follows the spec exactly as written. Grounding is
therefore checked per item, not once per file.

The deep dive's length and source counts are the deliberate exception, and they stay in prose. A
word-count gate is satisfied by padding, which is the failure it is meant to prevent, and a minimum
reference count is a quota on exactly the thing that gets fabricated. What carries the weight instead
is a check that already exists: every reference must be cited in the prose and every citation must
resolve to a reference, so a source count is a count of claims a reader can check, not of rows in a
list.

### Health

**There is no monitoring.** Nothing in this repo observes the pipeline, so a deleted scheduled task,
a revoked repo connection, a stale environment snapshot and a genuinely quiet week all look
identical from here: no new posts.

Check by hand, in rough order of likelihood, if briefs stop appearing:

- the scheduled tasks in the Jules console — are they still there, and when did each last run?
- the repository connection and the Jules GitHub App installation;
- any open pull request from Jules sitting unmerged because validation failed;
- `queue.py stats` — pending items with no briefs being written means runs are failing, not that
  there is nothing to cover. Two more signals there: `skipped 0` against a large `pending` count
  means rejected items are not being closed out, and a non-zero `stale` count means an earlier batch
  was left open and is being re-served in the same slot every run;
- whether `automation/config/topics.toml` has been narrowed until it matches nothing.

## Deployment

One-time repo setup: under **Settings > Pages > Build and deployment**, set **Source** to
**GitHub Actions**. The workflow cannot do this for you, and the deploy job fails without it.

`.github/workflows/pages.yml` defines two jobs:

- **`build`** — runs on every push and pull request. Off the default branch it only builds, which
  catches template and config errors without deploying anything.
- **`deploy`** — publishes the built artifact to Pages, from the default branch only.

The build runs `hugo --minify --baseURL "<the real Pages URL>/"`.

### Do not hardcode `baseURL`

The `configure-pages` action resolves the real deployed Pages URL at build time and exposes it as
`steps.pages.outputs.base_url`; the `--baseURL` flag then overrides `config.toml`. This one setup
handles all of:

- the standard project URL, `https://<user>.github.io/<repo>/` — note the **subpath**, which every
  asset and link must be prefixed with
- renaming the repo or the account
- a custom domain added later in repo settings

`config.toml` keeps `baseURL = "/"`, which affects **local builds only** and lets `hugo server`
serve from the root.

Do not set `relativeURLs = true` to try to make paths portable. Hugo restricts it to
filesystem-navigable sites, and it leaves RSS `<link>` elements and `og:url` non-absolute, which
breaks feed readers and link previews. Reference §4 covers this in detail.

### Using a custom domain or a user site

No config change needed — set the domain under **Settings > Pages > Custom domain** (GitHub writes
a `CNAME` file into the repo), or rename the repo to `<user>.github.io` for a root-level user site.
`base_url` follows either way.

## Theme

The theme is a Hugo module, not a submodule; `themes/` is intentionally empty.

The workflow runs `hugo mod get -u`, so **the theme floats to PaperMod master on every build** and
the commit pinned in `go.mod` is ignored at build time. New params arrive automatically, but so do
upstream breaking changes. To pin instead, drop `-u` from the workflow's `Fetch theme` step and
commit an exact version in `go.mod`.

To swap themes, change `THEME_URL` in the workflow's `env:` block and `theme` in `config.toml`,
then re-run `hugo mod get -u <new theme>`.

## Working with Claude Code

`CLAUDE.md` points Claude at this README, the reference document and `CHANGES.md`, and records the
repo's hard rules — the path allowlist and its trust boundary, `baseURL` handling, grounding, TOML
table scoping, RFC3339 dates, the floating theme, the forked templates in `layouts/`, PDF
retrieval, and the stdlib-only merge path.

`CHANGES.md` records what changed and why, for code and non-content changes. Published posts are
not logged there.

## License

MIT — see [`LICENSE`](LICENSE). Copyright (c) 2014 Spencer Lyon; inherited from the upstream
[GitLab Pages Hugo example](https://gitlab.com/pages/hugo) this repo derives from. Replace it
deliberately if that is no longer accurate.
