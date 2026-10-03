# research_diary

![research_diary](assets/research_diary_logo.jpg)

This site is a technical research diary. It has two types of posts:

- Daily briefs about new security and computer science publications.
- Long deep dives about one topic.

[Google Jules](https://jules.google/) does the research and writes the posts.
[Hugo](https://gohugo.io) and [PaperMod](https://github.com/adityatelange/hugo-PaperMod) make the
site. [GitHub Pages](https://docs.github.com/en/pages) publishes it.

Jules uses these sources:

- arXiv
- USENIX Security and USENIX WOOT
- IEEE S&P and Oakland SoK
- NDSS
- ACM CCS
- DEF CON and Black Hat
- [un]prompted
- Open web search. Thus, the diary can also use sources that are not in this list.

## How the pipeline operates

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

No part of this repository starts Jules. The schedule and the prompts are in the Jules console.
This repository contains these items:

- The specification that Jules reads (`AGENTS.md`).
- The tools that Jules runs (`automation/scripts/`).
- The checks that examine the output of Jules before a merge.

| Layer | Contents |
|---|---|
| Jules console | Repository connection, Initial Setup, the two daily scheduled tasks, manual deep dives |
| This repository | `AGENTS.md`, research scope, scripts, deduplication data, Hugo layout |
| GitHub Actions | Pull request validation, automatic merge, deployment |

## Local setup

1. Clone the repository.
1. Install [Hugo](https://gohugo.io/installation/) (extended).
1. Install [Go](https://go.dev/doc/install). Go is necessary because the theme is a Hugo module.
1. Fetch the theme:

   ```shell
   hugo mod get -u github.com/adityatelange/hugo-PaperMod
   ```

1. Start the local server. Then, open <http://localhost:1313/> to see the site:

   ```shell
   hugo server
   ```

1. Run the tests of the pipeline. These tests do not use third-party packages:

   ```shell
   for t in automation/scripts/test_*.py; do python3 "$t" || break; done
   ```

   NOTE: Some tests examine the HTML and PDF extraction of `fulltext.py`. If the packages are not
   installed, these tests stop and tell you that they did not run.

1. To run those tests, install the packages from `requirements.txt`. Usually, you install them in a
   virtualenv. If your system obeys PEP 668 and does not have `python3-venv`, install them into a
   directory:

   ```shell
   python3 -m pip install --target .pylibs -r requirements.txt
   PYTHONPATH=.pylibs python3 automation/scripts/test_fulltext.py
   ```

   NOTE: Git ignores the `.pylibs/` directory.

If Hugo is not installed on your computer, use Docker. The command that follows installs the same
pinned `.deb` that CI installs.

CAUTION: DO NOT USE `hugomods/hugo:exts`. ITS HUGO VERSION CHANGES AT NO SPECIFIED TIME. AT THIS
TIME, IT CONTAINS HUGO v0.154.5. HUGO ADDED `.Language.Direction` AFTER THAT VERSION.

The forked templates in `layouts/` use `.Language.Direction`. Thus, `hugomods/hugo:exts` cannot
render them. All pages fail with `can't evaluate field Direction in type *langs.Language`.

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

The values of `HUGO_VERSION` and `HUGO_SHA256` must agree with `.github/workflows/pages.yml`.
When you change one value, change the other value at the same time.

To simulate the full CI build with the production URL, refer to §7 of the configuration reference.

## Configuration

The full configuration reference is
**[`REFERENCE_caa20260903_153422.md`](REFERENCE_caa20260903_153422.md)**. It contains:

- All PaperMod parameters.
- The CSS-variable system for colour and layout.
- The parameters that you cannot change without an override of theme templates.
- The parameters that have no effect.

This table shows the file for each type of change:

| Change | File |
|---|---|
| Research topics, sources and tags | `automation/config/topics.toml` |
| Behaviour of Jules | `AGENTS.md` |
| Site title, menus, parameters | `config.toml` |
| Colours, fonts, layout geometry | `assets/css/extended/custom.css` |
| Pages and posts | `content/` |
| Files at the site root | `static/` |
| Record of each change and its cause (code, configuration, documents, but not posts) | `CHANGES.md` |

## The content pipeline

### Initial setup in the Jules console

Do these steps one time:

1. Connect `<GITHUB_USERNAME>/research_diary`. This installs the Jules GitHub App.
2. Configure the environment and make a snapshot of it. Refer to the subsequent section.
3. Do a manual run of each pipeline. Examine the output.
4. When the output is satisfactory, make the scheduled tasks.

NOTE: `fulltext.py` uses three packages. If they are not installed, Jules writes all papers from
the abstract only.

### Environment in the Jules console

Go to **Jules → Configure repo → Environment → run and snapshot.**

Python 3.12 is installed in the Jules VM. Most of the tools use only the Python standard library.
The ingestion tools use three more packages. Thus, the environment setup script is:

```shell
pip install -r requirements.txt
```

1. Run the setup script.
1. When the script finishes with no errors, **make the snapshot**.

Jules uses that snapshot for all subsequent tasks from this repository. Thus, Jules installs the
packages one time, not on each run. This is important because the arXiv brief runs each day.

Three problems in the environment do not show an error message. Obey these cautions.

CAUTION: WHEN `requirements.txt` CHANGES, RUN THE SETUP SCRIPT AGAIN AND MAKE A NEW SNAPSHOT.
A SNAPSHOT FROM BEFORE THE CHANGE KEEPS THE PREVIOUS PACKAGES.

With the previous packages, `fulltext.py` cannot import `bs4` or `pypdf`. It reports
`source: abstract` or `source: none`. The brief then contains less information than necessary.
If a conference paper has no abstract that `fulltext.py` can use as an alternative, Jules does
not write about that paper.

This problem looks the same as a content problem, not an environment problem. `AGENTS.md` tells
Jules to report an import error, not to find a workaround.

CAUTION: INITIAL SETUP MUST RUN `pip install -r requirements.txt`. IF THE SETUP SCRIPT IS EMPTY,
THE INGESTION TOOLS CANNOT OPERATE.

The ingestion tools are the only part of this repository that uses packages that are not in the
standard library.

NOTE: CI does not install these packages. This is a decision, not an error. These checks control the
merge:

- `pathguard.py`
- `validate.py`
- `postparse.py`
- `linkcheck.py`

They use only the standard library. Thus, no third-party package is between an untrusted pull
request and a write token. If the snapshot is broken, the Jules run is not satisfactory, but no
incorrect merge occurs.

### The console prompts

The prompts are only in the Jules console. The console has no version control, and git does
not keep a copy of the prompts. This section keeps a copy. Use it to make the prompts again.

**arXiv brief**: Scheduled Task, Daily:

```
Run the arXiv brief pipeline exactly as specified in AGENTS.md.
```

**Conference brief**: Scheduled Task, Daily:

```
Run the conference brief pipeline exactly as specified in AGENTS.md.
```

**Deep dive**: a usual task that you start manually. It has two modes:

```
Run the deep dive pipeline as specified in AGENTS.md. [Exploration] Topic: <your topic>
Run the deep dive pipeline as specified in AGENTS.md. [Detailed breakdown] Topic: <your topic>
Run the deep dive pipeline as specified in AGENTS.md. Topic: <your topic>
```

#### Deep dive modes

The marker selects the mode:

- `[Exploration]` gives a map of a full topic. It is wide, not deep.
- `[Detailed breakdown]` examines all parts of one mechanism. It is deep, not wide.

The two modes use the same research pipeline and the same source funnel. The mode changes what
Jules looks for and how carefully it reads. The mode does not change the quantity of sources.

The mode shows on the published post in two locations:

- As a prefix on the title.
- As the first tag of the post. Thus, each mode has its own `/tags/` archive.

Put the marker before `Topic:`. All the text after `Topic:` is the topic.

The third prompt came before the other two. It continues to operate. If the prompt has no
marker, Jules uses `[Exploration]` and tells you in its report.

The pipeline names must be the same as the headings in `AGENTS.md`. The two marker spellings
must be the same as in §5. The prompt has only one line. Thus, these words are the only words
that select the procedure and its depth.

You give only the direction of the research. Jules selects the sources to read and the sources to
keep in the post. Jules also divides the topic into parts. §5 of `AGENTS.md` gives the grounding
step, the three research steps and the source funnel.

#### Why the conference brief runs each day

The conference brief runs each day because of the backlog queue. All venue sources use
`window = "unseen"`. Each venue publishes all its papers at one time each year. Then, it
publishes nothing for many months. Thus, a daily read of the index pages finds nothing on most
days.

The queue solves this problem. Jules puts a programme into the queue one time. Then, `queue.py`
gives `brief_max_summarized` papers on each run. Thus, a conference with 200 papers becomes
approximately 25 usual briefs, not one very large post.

The queue contains more than 1,000 items. That is sufficient material for many months of daily
runs. When the queue is empty and no venue has a new programme, the daily run finds nothing. That
result is correct, and the run does not open a pull request.

`check = "weekly"` on those sources is a different value. It sets how frequently Jules reads the
**index page** of a venue again to find new items. It does not set how frequently the pipeline
runs.

#### Two pull requests on one day

The two scheduled tasks run each day. Thus, each task can open a pull request on the same day.
The two tasks write to `automation/state/seen.ndjson`. `queue.py` and `idstate.py` write one
record on each line, sorted by key. This keeps each diff small and prevents merge conflicts
between the two pull requests. This sort sequence is necessary, not optional.

#### Each batch must close

The queue gives eight papers on each run only if Jules closes each batch. The sequence of
`pending` items does not change between runs. Thus, if an item stays `pending`, the queue gives
it again in the same position on the next run. Each item that stays `pending` permanently
decreases the batch by one paper.

§4 step 7 of `AGENTS.md` tells Jules to close each item on the run that got it. Jules uses
`queue.py done` or `queue.py skip`. If an item stays `pending`, `queue.py` reports it.

#### Why each prompt has one line

Each prompt has only one line. This is a decision, not an error. All other instructions are in
`AGENTS.md` and `automation/config/topics.toml`. In those files, you can examine each change and
compare versions.

Also, you cannot edit a Jules scheduled task after you make it. You can only delete it
and make it again. Thus, a stable prompt lets you change the behaviour of Jules with a pull
request, not in the console.

### Checks on the output

Two workflows run. Only one of them can stop a merge.

`validate-content.yml` runs on each pull request that Jules opens. Its result is **advisory
only**. With `on: pull_request`, GitHub runs the workflow and the scripts from the pull request.
Thus, if a pull request changes a check, its own changed copy examines it. Thus, a green result
from this workflow does not show that the pull request is correct.

`auto-merge.yml` is **the trust boundary**. It runs with `on: workflow_run`. With this trigger,
GitHub always runs the copy from the default branch. The workflow runs the path guard from
`main` on the diff of the pull request. Then, it merges. It does not check out or run code from
the pull request.

The workflows do these checks:

1. **Path guard.** The diff can change only these paths:

   - `content/arxiv/*.md`
   - `content/conferences/*.md`
   - `content/deep-dives/*.md`
   - `automation/state/*`

   The input of the pipeline is untrusted web content. An agent with write access to the
   repository reads it. If a poisoned paper causes the agent to change a workflow,
   this check stops the merge. The guard runs from `main`. It runs before the runner writes a
   file from the pull request to the disk.

2. **Schema.** This check examines these items:

   - TOML frontmatter.
   - An RFC3339 UTC date.
   - Tags from the controlled vocabulary.
   - The necessary sections.
   - Grounding. Each item must have a source URL. One URL somewhere in the file is not
     sufficient.
   - Each citation must agree with a reference. Each reference must have a citation.
   - A conference index page must not replace the URL of a named paper.
   - Two references must not have the same URL.
   - The post must not contain placeholder identifiers.

   The locations where the deep dive research starts are also index pages. A repository is a
   location to look for sources. It is not a source to cite. Thus, `deep_dive.start_urls` and the
   venue index pages are in the same blocklist.

3. **Link check.** Each cited DOI and arXiv ID must resolve. An arXiv ID must identify the paper
   that the post names. Only `doi.org` and `arxiv.org` can stop a merge. The check reports other
   hosts but does not stop the merge for them. Some publishers, for example ACM, Black Hat and
   CISA, send HTTP 403 to a datacenter IP. Thus, a gate on those hosts can stop correct pull
   requests.

4. **Build.** Hugo must render each changed page. With `buildFuture = false`, Hugo removes a
   page with a future date and shows no error message. Thus, a build with no errors does not show
   that the page is on the site.

If the four checks find no errors, the pull request merges automatically and the deployment
starts. If a check finds an error, the pull request stays open.

The schema check and the link check are in code, not in text. Each instruction that is only in
`AGENTS.md` is advisory, because the agent obeys the specification as it is written. Thus, the
code examines the grounding of each item, not of each file.

The code does not examine the length and the source count of a deep dive. This is a decision,
not an error.
These limits stay in the text of `AGENTS.md`.

A minimum word count is easy to get with filler text, and filler text is the problem that the
minimum must prevent. Some references that the agent writes refer to no source. A
minimum reference count is a quota on those references.

Thus, the validator uses a different check. Each reference must have a citation in the text, and
each citation must resolve to a reference. As a result, the source count is a count
of claims that a reader can examine.

### Health

**No tool monitors the pipeline.** Nothing in this repository examines the pipeline. These
conditions all look the same from the repository, because no new posts occur:

- A deleted scheduled task.
- A revoked repository connection.
- An environment snapshot from before a change to `requirements.txt`.
- A week with no new publications.

If briefs stop, examine these items. The causes that occur most frequently are first:

1. Examine the scheduled tasks in the Jules console. Make sure that they are there. Find when
   each task ran the last time.
1. Examine the repository connection and the installation of the Jules GitHub App.
1. Find open pull requests from Jules that did not merge because a check found an error.
1. Run `queue.py stats`. Use these signs:
   - Many `pending` items and no new briefs: the runs fail. The queue contains items.
   - `skipped 0` and many `pending` items: Jules does not close rejected items.
   - A `stale` count that is more than zero: Jules did not close a batch. The queue gives
     those items again in the same position on each run.
1. Examine `automation/config/topics.toml`. Make sure that some papers agree with its topics.

## Deployment

Do this step one time: go to **Settings > Pages > Build and deployment**, and set **Source** to
**GitHub Actions**. The workflow cannot do this step. If you do not do it, the deploy job fails.

`.github/workflows/pages.yml` contains two jobs:

- **`build`** runs on each push and each pull request. On branches other than the default branch,
  it only builds the site. This finds template and configuration errors and deploys nothing.
- **`deploy`** publishes the built site to GitHub Pages. It runs only from the default branch.

The build runs `hugo --minify --baseURL "<the real Pages URL>/"`.

### Do not hardcode `baseURL`

The `configure-pages` action finds the URL where GitHub Pages publishes the site. It does this
during the build. It writes the URL to `steps.pages.outputs.base_url`. Then, the `--baseURL` flag
overrides `config.toml`. This one procedure operates correctly in these conditions:

- The usual project URL, `https://<user>.github.io/<repo>/`. This URL has a **subpath**. All
  assets and links must start with this subpath.
- A new name for the repository or the account.
- A custom domain that you add in **Settings** of the repository.

`config.toml` keeps `baseURL = "/"`. This value has an effect on **local builds only**. It lets
`hugo server` serve the site from the root.

CAUTION: DO NOT SET `relativeURLs = true`. IT BREAKS FEED READERS AND LINK PREVIEWS.

Hugo permits `relativeURLs = true` only for sites that you open from the file system. With this
parameter, RSS `<link>` elements and `og:url` are not absolute. §4 of the configuration reference
gives more information.

### Custom domain or user site

No configuration change is necessary. Do one of these steps:

- Set the domain in **Settings > Pages > Custom domain**. GitHub writes a `CNAME` file into the
  repository.
- Change the name of the repository to `<user>.github.io`. This gives a user site at the root.

In the two conditions, `base_url` changes automatically.

## Theme

The theme is a Hugo module, not a git submodule. The `themes/` directory is empty. This is a
decision, not an error.

The workflow runs `hugo mod get -u`. Thus, **each build uses PaperMod master as it is on the day of
the build**. The build ignores the commit in `go.mod`. New parameters come automatically. Changes in
the theme that break this site also come automatically.

To pin the theme:

1. Remove `-u` from the `Fetch theme` step of the workflow.
1. Commit one specified version in `go.mod`.

To change to a different theme:

1. Change `THEME_URL` in the `env:` block of the workflow.
1. Change `theme` in `config.toml`.
1. Run `hugo mod get -u <new theme>`.

## Claude Code

`CLAUDE.md` tells Claude to read this README, the configuration reference and `CHANGES.md`. It
also contains the hard rules of the repository:

- The path allowlist and its trust boundary.
- How to use `baseURL`.
- Grounding.
- The scope of TOML tables.
- RFC3339 dates.
- The theme version, which is always PaperMod master.
- The forked templates in `layouts/`.
- PDF retrieval.
- The merge path that uses only the standard library.

`CHANGES.md` records each change that is not content, and its cause. It does not record
published posts.

## License

MIT. Refer to [`LICENSE`](LICENSE). Copyright (c) 2014 Spencer Lyon. This repository comes from
the upstream [GitLab Pages Hugo example](https://gitlab.com/pages/hugo) and has the same license.
If that license is not correct, replace it in a commit that changes only the license.
