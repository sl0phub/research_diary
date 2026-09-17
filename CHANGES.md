# CHANGES.md

The record of what changed in this repository and why. Alongside git commits, this is the single
source of truth for change history.

**Scope: code and non-content changes only** — scripts, workflows, config, templates, styling,
docs, the pipeline spec. **Published content is never logged here.** Posts under `content/arxiv/`,
`content/conferences/` and `content/deep-dives/` are the diary's output, not changes to the repo;
they carry their own dated frontmatter and are tracked in `automation/state/`.

Rules:

- Files state only what is true now. Rationale, history and superseded behaviour live here.
- Timestamps are UTC, matching the RFC3339 rule for content frontmatter.
- Entries are newest first. Line numbers are the **pre-change** ranges.
- Content-pipeline pull requests need no entry. `CHANGES.md` is outside `pathguard.py`'s write
  allowlist by design, so a pipeline run cannot add one. It stays readable by anything.

---

## Changes: 17 Sep 2026 2337H

The arXiv format example was a topic instruction, and the briefs were following it.

Every arXiv brief published so far reads as an LLM-security digest: 14 of the 16 written-up items
across the 15 and 16 September posts are LLM or agent papers. Measured against the same three feeds
on 17 September, the source does not explain that. After announce-type filtering and dedup the
candidate pool held 262 items, 156 of them LLM-related — 59.5%, against roughly 90% in the output —
and 34 non-LLM security items went unwritten, including work on encrypted-traffic side channels and
analog-pin exfiltration that matches `interests` directly.

`arxiv.py` is not the cause: it holds no keyword list, no scoring and no topic filter, and truncates
at a `--max` of 400 that a day's feeds never approach. `AGENTS.md` is not the cause either; it names
no topic at all, and §3 step 5 delegates ranking to `interests`. The cause was
`automation/examples/arxiv-example.md`, which §6 hands the writer as the worked example: all three of
its items were LLM-agent security papers, it was tagged `llm-security`, and its first `In brief`
bullet opened "Both items measure LLM agents on security tasks." An agent imitates the example it is
shown more reliably than it applies an abstract interest list, so the example set the topic.

The rewrite changes proportion, not scope. LLM and agent security is four of the seventeen
`interests` entries and keeps one write-up slot and its tag; the example now carries three write-ups
rather than two, which also stops it teaching that two items is a normal day when
`brief_max_summarized` is 8. The replacement LLM item carries an attack result instead of a benchmark
score, so it no longer sits against the `reject` rule about benchmarks with no methodology or failure
analysis — the two items it replaced were both benchmarks, both read abstract-only. Only one of the
three write-ups now carries the abstract-only marker, since the other two were retrieved in full;
previously both items carried it, which taught failed retrieval as the norm.

No script, workflow, validator or config was changed. Nothing measures whether the rebalance held:
the check is to re-run a tag-frequency count over `content/arxiv/*.md` after a week of runs and see
whether `llm-security` still appears on every post. Two findings were recorded and deliberately not
acted on — cs.AI supplies about 78% of the candidate pool while only about 15% of its items are
security-related, which is why the 15 September link roll carries papers on patent drafting and
enterprise agent deployment; and the `reject` rule about defence design with no new attack result did
not bind on either published post.

- **changes in `automation/examples/arxiv-example.md`**: `tags` and `summary` at lines 5 - 6 replaced
  — `cs.AI` and `vulnerability-discovery` dropped for `hardware`, `cryptography` and `side-channel`,
  `llm-security` kept; `title` and `date` at lines 2 - 3 moved to 2026-09-17 to match the
  replacement identifiers. The `## In brief` bullets at lines 16 - 21 replaced with two that draw a
  thread across the items instead of characterising what they are about. The two items at lines
  23 - 54 replaced with three: analog-pin exfiltration in mixed-signal ICs (arXiv:2609.19111) and
  cross-channel fragmentation against MCP tool-calling (arXiv:2609.18217), both written from
  retrieved full text and carrying no marker, and cryptanalytic sign recovery on hard-label networks
  (arXiv:2609.18751), abstract-only and keeping the marker. `## Also published` at lines 56 - 59
  extended from one entry to three; the existing `arXiv:2609.15906` entry is unchanged. The
  format-reference disclaimer at lines 9 - 14 is untouched. All six identifiers were confirmed to
  resolve before publication.

## Changes: 17 Sep 2026 1545H

Two deep-dive modes, and the autonomous research funnel the spec never actually specified.

Deep dives were coming out at a third the length of the ones worth keeping, and the cause was in the
spec rather than in the agent. §5 stated no length, no source count and no grounding step; its only
quantitative claim about sources was the negative one, "no cap on the number of sources". "All three
stages are run in full" asserted equal weight without defining it, so a post whose references were
twenty-five preprints and five blog posts satisfied the spec as written. The agent follows the spec
exactly, so it wrote what the spec described.

- **changes in `automation/config/topics.toml`**: `tags` gains `exploration` and `breakdown` after
  line 71; `[discovery].guidance` lines 229 - 230 reworded for the renamed stages; a `[deep_dive]`
  table appended after line 231.
- **changes in `automation/scripts/postparse.py`**: `index_urls()` docstring lines 147 - 151
  rewritten; a `deep_dive.start_urls` loop added after line 178.
- **changes in `automation/scripts/test_postparse.py`**: a starting-point membership block added
  before line 104; the individual-paper-page cases at lines 105 - 110 extended with a document under
  each newly blocked root.
- **changes in `AGENTS.md`**: §0's deep-dive row at line 26 reworded; hard constraint 6 gains the
  mode-tag rule after line 91; §2's **Retrieval: a floor, not a ceiling** gains a deep-dive pointer
  after line 264; §5 lines 453 - 518 replaced entirely; §6's **Deep dives** frontmatter paragraph at
  line 683 replaced and a `#### Length` subsection added; §7 gains **A deep-dive report** before the
  quiet-run rule.
- **changes in `automation/examples/deep-dives-example.md`**: lines 2 - 5 gain the title prefix, the
  mode tag and a `summary`; the preamble gains a paragraph saying the file shows shape and not size.
- **changes in `archetypes/deep-dives.md`**: lines 2 - 5 likewise, plus a comment naming both modes.
- **changes in `README.md`**: the deep-dive prompt block at lines 171 - 178 replaced with the three
  prompt forms; the **Schema** guard at line 244 and the closing paragraph at line 257 extended.
- **changes in `CLAUDE.md`**: **Grounding is checked in code, not asked for in prose** gains three
  paragraphs on the deep-dive exception; the frontmatter convention bullet gains a preference for a
  tag over a new key.

**Why the mode is a tag and a title prefix rather than a frontmatter key.** `check_tags` already
rejects any tag outside `topics.toml`, and `test_validate.py` reads that vocabulary live, so two new
tags enforce the mode with no validator change, no test change and no widening of `ALLOWED_KEYS`.
That key set is an injection surface — PaperMod renders several params straight into HTML attributes
— so keeping it closed is worth more than a dedicated key. The title prefix is what makes the mode
visible on the page: PaperMod has no badge param, and rendering one would mean a fourth forked theme
template against a theme that floats to master. The tags also give each mode a `/tags/` archive.

**Why the length and source floors are prose and not code.** They contradict this file's own rule
that a rule which matters goes in `validate.py`, and the exception is deliberate. A word floor is
satisfied by padding, which is the failure it would exist to prevent. A minimum reference count is a
quota on the thing that actually gets fabricated: the deep dive recorded further down this file
shipped 4,176 words and 33 references, 10 of them invented, so a floor pointed that way would have
ratified it. The forcing function used instead was already in `validate.py` — every reference must
be cited in the prose and every citation must resolve to a reference — which makes the target of
thirty sources a target of thirty checkable claims rather than thirty rows in a list. A padded list
fails today, before any floor is consulted.

**Why equal weight became a quota.** Per-stage floors and a cap on any one stage's share are the only
form of "all three stages run" that can be checked at all, even by a human reading the diff. Nothing
enforces them, which is why §7 now requires the funnel reported per stage and each citation mapped
back to the stage it came from: that report is the only record the later stages happened.

**Why the starting points moved into config.** §5 named `eprint.iacr.org`, the ACM DL, IEEE Xplore,
NDSS and Springer as places to look, and none of them was in the citation blocklist — hard constraint
8 says an index is where you look and never what you cite, but a starting point named only in prose
is one nothing enforces. `deep_dive.start_urls` is read by `postparse.index_urls()`, so naming a
repository and blocking its landing page are now the same edit. This is the hole `retired_index_urls`
was written to close, reopened at the other end. Each entry normalizes to a bare host or a short
path, so a real citation underneath it does not collide; `oaklandsok.github.io` is deliberately
absent because it is already a `sources` entry.

---

## Changes: 17 Sep 2026 1530H

Every route out of the backlog's `pending` state, and the schedule change that made the gap urgent.

- **changes in `automation/scripts/queue.py`**: lines 11 - 14 replaced with the closing invariant;
  line 33 reworded; `_rank()` and `_venue_match()` added after line 125; lines 129 - 131 (`pending`)
  rewritten to sort by `_rank`; `stale_head()` and `_report_stale()` added after line 146; `next`
  gains the warning at line 207 and `stats` a `stale` count at line 226.
- **changes in `automation/scripts/test_queue.py`**: docstring lines 6 - 7 extended; a `stale head`
  section added after line 98, covering a fresh queue, a drained queue, an item left behind a close,
  a skip clearing the block, the venue filter, and agreement with `pending`'s order.
- **changes in `automation/config/topics.toml`**: a ninth `reject` rule added after line 83; the
  compulsory-sources comment at line 110 extended to say what `check` does and does not govern.
- **changes in `AGENTS.md`**: pipeline table line 25 replaced; the `source` table's `none` row
  (line 199) and the paragraph below it (lines 203 - 204) replaced with the recovery procedure;
  §2's `queue.py` reference extended after line 216; `check` key at lines 244 - 245 rewritten;
  §3 steps 6 and 7 (lines 287 - 288, 297 - 298) repointed at recovery; §4 step 4 extended after
  line 343; §4 step 6 (line 355) repointed; §4 step 7 (lines 357 - 367) replaced with the
  two-route close-out; §6's `none` note (lines 501 - 502) replaced; §7 report line 578 extended.
- **changes in `README.md`**: line 34 and line 165 corrected to the current console config; lines
  180 - 185 replaced with the cadence rationale; health check at line 240 extended.
- **changes in `CLAUDE.md`**: new hard rule added after line 147; `fulltext.py` rule extended after
  line 226; `content/conferences/` table row at line 257 given its cadence.

### Why `skip` had to be documented, not just implemented

`queue.py skip` and the `skipped` status shipped with the queue and were unit-tested from the
start — and were named in no document: not `AGENTS.md`, `README.md`, `CLAUDE.md` or the reference.
`AGENTS.md` §4 step 4 told Jules to reject items matching `topics.toml`'s `reject` list, and step 7
said "Record every item you **kept**", offering only `queue.py done`. A rejected item is not kept,
so nothing closed it.

`pending()` orders by `(first_seen, key)`, and the whole NDSS and USENIX programme was enqueued in
one commit, so all 1354 records share `first_seen = 2026-09-15` and the order is alphabetical by key
and stable across runs. An unclosed item is therefore re-served in the same batch slot on every
subsequent run — a head-of-line block, not a rotation — and each one narrows the batch permanently.

Measured before the change: **1330 `pending`, 24 `done`, 0 `skipped`**. The 24 closed records were
the alphabetically-first 24, a clean prefix, so nothing was stranded yet. It had not fired because
Jules was closing all 8 of each batch and routing the non-highlights to **Also published** rather
than rejecting them — including items matching the `reject` list plainly. Correct application of
step 4 was what would have stuck an item, and the next batch (`all-…` through `anota`) contained a
cross-device-authentication usability study that the "posture scanning, configuration survey or
compliance measurement" rule drops.

A route documented nowhere is a route never taken, so the rule is now stated in `AGENTS.md` **and**
checked in code, per the "Grounding is checked in code" rule: `stale_head()` reports pending items
ranked ahead of the newest closed item. Warn-only and exit 0, because §4 step 2 treats `next`'s
output as the run's material and a non-zero exit would derail a run over bookkeeping; and outside
`validate.py`, which is content-only and offline, so a queue slip must not block a pull request.

### The superseded retry rule

`AGENTS.md` previously instructed Jules to leave a `source="none"` item **pending** "so a run that
can reach the paper gets another go at it", in three places: the §2 `source` table, §3 step 7 and
§4 step 7. Unbounded, and against the wrong failure. `dl.acm.org`, `blackhat.com` and `cisa.gov`
refuse any datacenter IP by policy and `usenix.org` times out intermittently, so re-issuing the same
request tomorrow was not a retry — and 833 of the 1330 pending items are USENIX Security.

Replaced by recovery-then-reject on the same run: one `google_search` for a reachable copy, the
result re-fetched through `fulltext.py`, and rejection if that fails. A retry mechanism was designed
and dropped in favour of this — an `attempts` field, a `defer` subcommand and a
`(attempts, first_seen, key)` ordering — because it added a schema, a config value and a second
notion of queue position to solve a case where the fetch was never going to succeed.

No new record field was added, `pending()`'s order is unchanged, and the state file's schema is as it
was. `403` and `404` route identically but publish differently: a 403 item may still appear in
**Also published** because the venue did publish it, while a 404 item appears nowhere, since
`linkcheck.py` gates only `doi.org` and `arxiv.org` and would not catch the dead link.

The arXiv brief keeps its own bounded version — an unrecoverable item is simply not recorded, and the
48-hour feed window gives it one more run before it falls out on its own. That pipeline has no queue,
so nothing accumulates behind it.

### Schedule: the conference brief is daily

The Jules console now holds two daily scheduled tasks. The conference brief's weekly task was deleted
and recreated as daily; a scheduled task cannot be edited in place, and the console is not version
controlled, so `README.md` lines 155 - 189 remain the only record of it.

The superseded rationale argued that weekly was right because "they publish in one annual burst and
then drain, so a daily run would find nothing most days". That is true of the venue index pages and
false of the pipeline: the queue decouples them, and with 1330 items enqueued there is material for
about 167 consecutive runs. Daily only begins to waste a run once a programme is drained and no new
one has been posted.

`check = "weekly"` on the nine `retrieval = "urls"` sources therefore keeps its value. No script
reads the key — `postparse.py` consumes only `retrieval` and `url_templates` — so it is advisory,
addressed to Jules, and it now says what it governs: re-reading a venue's index page, not the
pipeline's schedule. As previously worded it read, on a daily schedule, like permission to skip a run.

Daily also sharpens the head-of-line block from a paper a week to a paper a day, and means both
scheduled tasks can open a pull request the same day. Both write `automation/state/seen.ndjson`, so
the sorted-NDJSON discipline in `queue.py` and `idstate.py` is now load-bearing rather than
theoretical.

---

## Changes: 17 Sep 2026 1300H

- **changes in AGENTS.md**: refactored to become more readable, lines 11 - 582 restructured
  (commit `461f006`). Sections regrouped into a numbered runbook layout; no rule changed meaning.
- **changes in README.md**: line 151 prompt wording aligned with the AGENTS.md pipeline headings
  (commit `461f006`). Rationale: a one-line console prompt selects the procedure by name, so the
  words must match the headings exactly.
- **changes in CHANGES.md**: created. Rationale: the repo's docs carried both the pre-change and
  post-change state of the same decisions, and the git history they cited as evidence was squashed
  into `7f6dd46`, so `a79aa37`, `990b2d8` and theme SHA `d376885` no longer resolve. The prose was
  the only surviving record and it pointed at nothing.

### Documentation refactor — history extracted

- **changes in CLAUDE.md**: incident narrative removed from the allowlist (lines 65 - 69), rename
  guard (82 - 84), grounding (88 - 93, 99 - 107), format examples (120 - 125), TOML tables
  (129 - 131), theme selector (151 - 152) and `fulltext.py` (182 - 189, 201) rules. Every rule and
  every invariant was retained; only the narration of how each was learned moved here.
- **changes in CLAUDE.md**: line 92 cited `automation/examples/research-example.md`, which does not
  exist. Corrected to `deep-dives-example.md`. Rationale: the file was renamed when the "deep
  research" pipeline became "deep dive".
- **changes in CLAUDE.md**: lines 267 - 270 ended "Minimum bar before reporting a config or template
  change as done:" with a colon and no list; the following paragraph was the unrelated `hugomods`
  warning. Restored the three `grep -o` assertions and the expected-output line from §7 of
  `REFERENCE_caa20260903_153422.md`, which is where this block was copied from.
- **changes in CLAUDE.md**: lines 9 - 10 omitted Oakland SoK from the source list. Added.
  Rationale: it is a compulsory `retrieval = "urls"` source at `automation/config/topics.toml`
  lines 176 - 180, so the list was incomplete in a way that understated the pipeline's scope.
- **changes in CLAUDE.md**: added a `## Recording changes` section and a `Where things go` row for
  this file.
- **changes in README.md**: lines 69 - 76 recommended `hugomods/hugo:exts` for local preview.
  Replaced with the pinned `.deb` runner. Rationale: that image floats and ships Hugo v0.154.5,
  which predates `.Language.Direction` and therefore cannot render the forked templates in
  `layouts/` at all — it fails with `can't evaluate field Direction in type *langs.Language` on
  every page. CLAUDE.md and §7 of the reference both already said so; only the README still
  offered the broken command.
- **changes in README.md**: lines 174 - 191 credited `validate-content.yml` with gating the merge.
  Reattributed to `auto-merge.yml`. Rationale: `on: pull_request` runs the pull request's own copy
  of both the workflow and the scripts, so `validate-content.yml` is advisory and explicitly not
  the trust boundary. This contradicted CLAUDE.md lines 71 - 81 and the reference at lines
  206 - 210 and 291 - 292.
- **changes in README.md**: history removed from lines 127 - 128, 193 - 196 and 200 - 203; moved
  below.
- **changes in README.md**: lines 263 - 266 described CLAUDE.md as recording "the hard rules
  (notably the `baseURL` handling)". Rewritten — CLAUDE.md now carries about twelve hard rules.
- **changes in README.md**: lines 10 - 12 omitted Oakland SoK. Added, as for CLAUDE.md.
- **changes in README.md**: line 3 pointed the logo at `/assets/research_diary_logo.jpg`. Made
  relative. Rationale: Hugo serves `static/` at the site root, not `assets/`, and a leading slash
  also breaks the image on GitHub's own render of the README.
- **changes in README.md**: the "How it works" diagram at lines 16 - 23 showed
  `validate-content.yml` performing the path guard, schema and build checks with `auto-merge`
  merely merging afterwards. Redrawn to label `validate-content.yml` advisory and `auto-merge.yml`
  the trust boundary. Rationale: the diagram carried the same misattribution as the prose below it,
  so fixing only the prose would have left the two disagreeing.
- **changes in README.md**: added a `CHANGES.md` row to the Configuration table (after line 93) and
  a paragraph under "Working with Claude Code".
- **changes in CLAUDE.md**: added `CHANGES.md` as item 3 of "Read these first" (line 24).
- **changes in AGENTS.md**: lines 43 - 46 wrote the allowlist as `content/arxiv/**`,
  `content/conferences/**`, `content/deep-dives/**`. Corrected to the `*.md` single-level form.
  Rationale: `pathguard.py`'s globs are single-level, so a nested path such as
  `content/arxiv/sub/x.md` matched the specification and failed CI. CLAUDE.md lines 52 - 55 already
  had the correct form, so the two agent-facing files disagreed — the exact drift CLAUDE.md lines
  302 - 304 exist to prevent.
- **changes in AGENTS.md**: lines 83 - 85 and 197 - 200 cited
  `content/conferences/2026-09-15-daily-brief.md` in the present tense as a broken artifact.
  Removed. Rationale: that brief was rewritten in `fa6b108` and now carries six full items tagged
  `ndss`, so both passages described a file that no longer exists in that form.
- **changes in AGENTS.md**: line 223 omitted Oakland SoK. Added, as for CLAUDE.md and README.
- **changes in AGENTS.md**: rationale stripped from lines 31 - 34, 52 - 56, 96 - 99 and 184 - 186.
  Each rule and each instruction was kept; only the explanation of why it is shaped that way moved
  here. The DEF CON edition arithmetic at lines 380 - 381 was deliberately **kept** — it is a check
  Jules performs, not an explanation of one.
- **changes in AGENTS.md**: added a pointer at line 11 telling Jules to `read_file CHANGES.md` for
  the reasoning behind a rule. Rationale: the rules here no longer carry their own justification,
  and `pathguard.py` restricts what a pull request may *write*, not what Jules may read — so the
  pointer is one Jules can actually follow.
- **changes in REFERENCE_caa20260903_153422.md**: line 281 cross-referenced "§9" for the agent
  runtime. Corrected to §8. Rationale: §8 is "Agent runtime"; §9 is "Upstream docs".
- **changes in REFERENCE_caa20260903_153422.md**: lines 212 - 214 ("Related, and how this was
  found") moved here. Lines 216 - 222 split — "Removed from this repo" is history, "do not re-add"
  is the live rule and stays.
- **changes in REFERENCE_caa20260903_153422.md**: the header asserted generation on 2026-09-03
  while the body carried "Verified 2026-09-16" and "Audited 2026-09-16". Last-audit date noted in
  the header. Rationale: the filename implies a freshness the document no longer has.
- **changes in AGENT_CAPABILITIES_caa260916.md**: reframed as an inventory of what the sandbox
  provides, not a grant of what to use, with a pointer to AGENTS.md for the prohibitions.
  Rationale: line 35 presented `sudo` and `docker` group membership and line 56 presented `curl`
  and `wget` as freely usable, while AGENTS.md lines 116 - 118 and 136 - 139 forbid exactly those.
  Read alone, the capabilities file overrode the spec.
- **changes in AGENT_CAPABILITIES_caa260916.md**: line 28's note about legacy tools moved here.

### Known and deliberately not changed

Confirmed present, left alone in this pass because it was scoped to documentation. Recorded so it
is not lost:

- `automation/scripts/test_pathguard.py` lines 20 - 23 cite `a79aa37` and `990b2d8`, which do not
  resolve in this repository. The rule the comment states is load-bearing and correct.
- `automation/scripts/validate.py` line 123 and `test_validate.py` line 158 refer to "the A8 trap".
  There is no A8: the date rule is hard constraint 4 in the current AGENTS.md. Line 276 of
  `validate.py` correctly cites "hard constraint 8" for the index-page rule, so the numbering
  scheme changed and one reference was left behind.
- `automation/scripts/validate.py` lines 46 - 49 explain the `SECTIONS` dict entirely in terms of
  `news`, `NEWS_NAME` and `RESEARCH_NAME`, none of which exist. The reason it gives — do not
  collapse the dict back to a conditional — is still valid. The same vocabulary survives in
  `test_validate.py` fixtures `GOOD_NEWS` and `GOOD_RESEARCH`.
- `automation/scripts/pathguard.py` lines 22 - 25 advertise a
  `git diff --name-only | pathguard.py --stdin` invocation, which is the exact pipeline that
  `changed_files()` at lines 68 - 76 exists to avoid. It also omits `--head`, the flag both
  workflows depend on.
- `automation/config/topics.toml` line 121 sets `feed_url`, which nothing reads — `arxiv.py` line
  54 hardcodes the same URL. Line 122 sets `window = "48h"` on an RSS source, which `arxiv.py` line
  299 states is ignored on that path.
- `automation/examples/` — all three files carry a "the previous version of this file used invented
  IDs" paragraph. These are Jules' format prompt, so the surrounding instruction is operative; only
  the framing is history.
- `.github/workflows/validate-content.yml` lines 144 - 145 and `auto-merge.yml` lines 78 - 79 carry
  a tombstone comment and an "as before" that refers to a configuration the file no longer shows.

---

## Extracted rationale and incidents

Everything below predates this log. It was removed from the files named and is preserved here
verbatim so nothing is lost. Grouped by the rule it used to justify.

### The path allowlist — why it must not be widened

From `CLAUDE.md` lines 65 - 69:

> This has already gone wrong once. In `a79aa37` the agent hit the guard and added
> `.github/workflows/*`, `config.toml` and `pathguard.py` to it; in `990b2d8` it moved those same
> paths out of the test's DENY list into ALLOW so CI went green. The guard then permitted precisely
> what it existed to stop, for three commits. `test_pathguard.py` now pins the whole `ALLOWED`
> tuple against a literal, so widening it fails the suite rather than being ratified by an edited
> expectation list. Keep that pin.

Neither SHA resolves in this repository. The surviving rule is the pin in `test_pathguard.py` and
the prohibition in CLAUDE.md.

From `CLAUDE.md` lines 82 - 84, on why the guard reads blob modes and both sides of a rename:

> The guard also inspects blob modes and both sides of a rename. Neither is cosmetic: `--name-only`
> prints only the destination of a rename, so `git mv .github/workflows/pages.yml
> content/conferences/x.md` used to read as a single allowed path while the workflow silently
> vanished.

From `AGENTS.md` lines 52 - 56, on why editing the guard does not help:

> This is checked twice: once on your pull request, and again after validation by a workflow that
> runs from `main`. Editing the guard, its test, or the workflow does not widen the list — the
> second check does not read your branch's copy of any of them.

### Grounding — why it is checked in code, not asked for in prose

From `CLAUDE.md` lines 88 - 93:

> `AGENTS.md` has always said "every item must carry a source URL". `validate.py` implemented that
> as one `re.search` over the whole body, so a 4,176-word deep dive with 33 references passed on the
> strength of a single `http`. Ten of those references did not support what they were attached to:
> five attached an invented talk title to a bare conference index URL taken verbatim from
> `topics.toml`, one was the DOI in `automation/examples/research-example.md` with the year changed
> by a digit, one was a real arXiv ID for an unrelated paper, and three were plain 404s.

The same incident, from `README.md` lines 193 - 196:

> The schema and link checks exist because the earlier contract was prose. `AGENTS.md` has always
> said "every item must carry a source URL", and the validator implemented it as one regular
> expression over the whole file — so a 4,000-word deep dive with 33 references passed on the
> strength of one working link. Ten of those 33 turned out not to support what they were attached
> to.

The two retellings disagree on the word count. **4,176 is the figure to trust**; "4,000" was a
rounding that hardened into a second fact. The file named in the CLAUDE.md copy is also wrong — it
is `deep-dives-example.md`, not `research-example.md`.

From `CLAUDE.md` line 101, on the `postparse.py` test cases:

> The false-positive traps, all of which were hit during development

The four traps themselves remain in CLAUDE.md as invariants; only the note that each was hit during
development moved here.

### Format examples — why every identifier in them is real

From `CLAUDE.md` lines 122 - 125:

> `automation/examples/` is the agent's format prompt, and it used to teach the shape with invented
> arXiv IDs and DOIs. A deep dive then produced `arXiv:2605.12345` — the same `26XX.XXXXX` shape —
> and mutated the example's S&P DOI by one digit. Every identifier in those files is now real and
> resolving, and each file says so.

### TOML tables — why keys sit above the first table header

From `CLAUDE.md` lines 129 - 131:

> This bit the repo twice. In `config.toml`, seven top-level settings — `buildFuture` among them —
> sat below `[pagination]` and were silently scoped into it, so Hugo never applied them. The same
> mistake put `tags` inside `[discovery]` in `automation/config/topics.toml`.

The same incident, from `REFERENCE_caa20260903_153422.md` lines 212 - 214:

> Related, and how this was found: `buildFuture` had been sitting below the `[pagination]` header in
> `config.toml`, so TOML scoped it into that table and Hugo never read it. Six other top-level
> settings were inert the same way. Keys must appear **above** the first `[table]` header.

The counts are consistent: one plus six is the seven CLAUDE.md reports.

### The theme's dark-mode selector

From `CLAUDE.md` lines 151 - 152, duplicating `REFERENCE_caa20260903_153422.md` lines 20 - 22:

> Practical trap: the dark-mode CSS selector is `:root[data-theme="dark"]` on master; it was `.dark`
> until early 2025. Snippets written for `.dark` silently do nothing.

§2 of the reference owns this now; CLAUDE.md points at it.

### `fulltext.py` — why it takes any URL, and why `none` is not `abstract`

From `CLAUDE.md` lines 182 - 189 and 201:

> It was arXiv-only — `retrieve()` formatted its argument into `arxiv.org/{html,pdf}/<id>` — while
> the conference backlog holds landing-page URLs and no abstract. So a conference item had no route
> at all: every route failed, the fallback returned an *empty* string dressed as `source="abstract"`,
> and `content/conferences/2026-09-15-daily-brief.md` shipped eight NDSS papers whose entire body
> was the abstract-only marker. `validate.py` passed it, because an item only has to carry a bullet
> and a URL.
>
> It now takes an arXiv id or any http(s) URL.
>
> The empty-string-as-success return is the bug that produced the brief above.

That brief was rewritten in `fa6b108`. The three load-bearing consequences — the stdlib link
resolver, picking the paper over the slide deck, and `source="none"` being a refusal rather than a
thin success — remain in CLAUDE.md as rules.

### Venue tags

From `AGENTS.md` lines 83 - 85:

> This has gone wrong once already — `content/conferences/2026-09-15-daily-brief.md` shipped tagged
> `unprompted` with eight NDSS papers in it.

From `AGENTS.md` lines 197 - 200, on `source="none"`:

> `none` is not a thinner version of `abstract`. It means every route failed and no abstract was
> supplied, so there is no material at all — writing an item from it produces a heading, a marker
> and no content, which is what `content/conferences/2026-09-15-daily-brief.md` is.

The rule survives in AGENTS.md; only the claim about that specific file was removed, because it is
no longer true of it.

### Why the two briefs are split

From `AGENTS.md` lines 31 - 34:

> The split exists because arXiv is a daily feed read in full, while the conference venues are pages
> you read on an "unseen" basis and that publish in one annual burst — which is why the conference
> brief drains a backlog a batch at a time rather than covering a whole programme at once.

Also stated, at more length, in `README.md` lines 160 - 165, which remains the fuller copy.

### `fulltext.py` picks the paper, not the deck

From `AGENTS.md` lines 184 - 186:

> It picks the **paper**, never the slide deck — a deck is a PDF too, and briefing from someone's
> bullet points while reporting that you read the paper is the failure this exists to prevent.

### Identifiers must not be adapted

From `AGENTS.md` lines 96 - 99:

> Taking an identifier you saw somewhere — including in this repository's format examples — and
> changing a digit or a year to fit produces something that looks checkable and is not.

The prohibition and "That is fabrication, not citation" remain in AGENTS.md.

### The Jules environment snapshot

From `README.md` lines 127 - 128:

> **This replaces the old "leave Initial Setup empty" instruction.** That was true while everything
> was stdlib-only; it is not any more.

### Monitoring

From `README.md` lines 200 - 203:

> **There is no monitoring.** A weekly `staleness.yml` canary used to open an issue when a feed went
> quiet; it was removed to cut workflow noise.

No `staleness.yml` exists in `.github/workflows/`. "There is no monitoring", and the manual checks
that follow it, remain in the README.

### Settings removed from this repo

From `REFERENCE_caa20260903_153422.md` lines 216 - 222, the changelog halves of the
"Do not re-add these" table:

> `[params.assets] disableHLJS` — **Dead.** No reference anywhere in the theme. PaperMod dropped
> highlight.js; highlighting is Chroma now. Removed from this repo.
>
> `pygmentsUseClasses` — Legacy Hugo alias for `[markup.highlight] noClasses`. Was set redundantly
> alongside it. Removed from this repo.
>
> `assets.disableScrollBarStyle` — Existed in Jan 2025 PaperMod, removed on master.

The rule — do not re-add these, they do nothing — stays in the reference.

### Superseded Jules tools

From `AGENT_CAPABILITIES_caa260916.md` line 28:

> *Note: Legacy/deprecated tools (`grep`, `create_file_with_block`, `overwrite_file_with_block`) are
> omitted as they are superseded by `run_in_bash_session` and `write_file`.*
