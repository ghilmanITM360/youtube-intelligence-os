# DS-000027 — Dr. Ares Senior acquisition preflight

Audit date: 2026-09-20

Status: **PREFLIGHT COMPLETE — AWAITING EXPLICIT LAUNCH APPROVAL**

No Apify Actor was launched. No credits were spent.

## Dataset allocation and duplicate control

- `DS-000026` is already reserved by the committed 29-channel preflight at `docs/audits/DS-000026_FRESH_PREFLIGHT_PROPOSAL_2026-09-15.md`.
- The next safe dataset identifier is `DS-000027`.
- Repository text, manifest, raw-directory, normalized-registry, and available catalog checks found no existing Dr. Ares dataset under handle `@Dr.Ares-YT` or channel ID `UC356D-NzdnznBOftTpYoBLw`.
- No dataset record or final manifest has been created. The new directory contains preflight evidence only.

## Git audit

- Initial local branch: `main` at `a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8`, clean, 12 commits behind `origin/main`.
- Initial configured upstream and independently verified remote tip: `dcfe2927eee8c9bca11ac03cf21724c59b440b6b`.
- The clean checkout was fast-forwarded to `dcfe2927eee8c9bca11ac03cf21724c59b440b6b` before allocating a dataset ID.
- One worktree exists: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`, branch `main`; no extra branch was created.
- The initial audit found no tracked or untracked user-owned files.

## Verified channel identity

| Field | Public browser observation |
|---|---|
| Submitted URL | `https://www.youtube.com/@Dr.Ares-YT` |
| Display name | Dr. Ares Senior |
| Handle | `@Dr.Ares-YT` |
| Canonical channel ID | `UC356D-NzdnznBOftTpYoBLw` |
| Canonical URL | `https://www.youtube.com/channel/UC356D-NzdnznBOftTpYoBLw` |
| Subscribers | 52.1K (rounded public display) |
| Public videos | 35 |
| About text | Public description begins: “Welcome to the channel! I'm Ares Smith Sr. Simple, science-backed tips…” |

The canonical `<link>` and Open Graph URL both resolved to the same channel-ID URL. Identity therefore does not depend on the mutable handle alone. Separate Shorts and livestream counts were not exposed and remain `NOT_AVAILABLE`.

Raw observation: `data/raw/channel-data/DS-000027/preflight/channel_identity_evidence.json`.

## Authenticated Apify preflight

- Account/workspace displayed: `Ai Personal`.
- Plan: Free.
- Usage displayed: `$4.28 / $5.00`; calculated remaining displayed credit: `$0.72`.
- Actor: `streamers/youtube-scraper` (`h7sDV53CddomktSi5`), build `latest` proposed.
- Applicable Free-plan video event: `$4.00 / 1,000` videos written to the dataset.
- Platform usage: included.
- Paid add-ons observed: channel date range `$1.30 / 1,000`; AI description `$15 / 1,000 video minutes`; AI summary `$15 / 1,000 video minutes`; speech-to-text transcript `$48 / 1,000 started video minutes`.
- Transcript configuration proposed: `ALWAYS_SUBTITLES`, which downloads existing YouTube subtitles when present and does not request paid speech-to-text. Videos without subtitles will remain explicitly unavailable.
- Shorts, livestreams, date filter, AI description, AI summary, and speech-to-text are disabled.

## Cost and reserve

| Item | Amount |
|---|---:|
| Public videos / video-event ceiling | 35 |
| Direct video-event estimate | `$0.140` |
| Conservative planning envelope | 37 results / `$0.148` |
| Displayed remaining credit before run | `$0.720` |
| Required reserve | `$0.300` |
| Projected balance after conservative estimate | `$0.572` |
| Projected headroom above reserve | `$0.272` |

The proposal fits the documented reserve using displayed values. Actual cost must be recorded from post-run billing if authorized and launched.

## Proposed exact input

The sanitized, non-secret input is preserved at `data/raw/channel-data/DS-000027/preflight/proposed_actor_input.json`. It targets only the canonical Dr. Ares channel URL with `maxResults: 35`, existing subtitles only, and every optional paid add-on disabled.

## Evidence inventory

| Path | Disposition |
|---|---|
| `data/raw/channel-data/DS-000027/preflight/channel_identity_evidence.json` | `SUPPORTING_EVIDENCE`; local immutable public-browser observation |
| `data/raw/channel-data/DS-000027/preflight/authenticated_apify_balance_evidence.json` | `SUPPORTING_EVIDENCE`; local authenticated budget observation |
| `data/raw/channel-data/DS-000027/preflight/authenticated_apify_pricing_evidence.json` | `SUPPORTING_EVIDENCE`; local pricing observation |
| `data/raw/channel-data/DS-000027/preflight/actor_input_schema_evidence.json` | `SUPPORTING_EVIDENCE`; local schema/readme observation |
| `data/raw/channel-data/DS-000027/preflight/proposed_actor_input.json` | `HOLD`; proposed sanitized input, not submitted |
| `data/raw/channel-data/DS-000027/preflight/preflight_cost_proposal.json` | `HOLD`; authorization gate record |
| `docs/audits/DS-000027_DR_ARES_PREFLIGHT_PROPOSAL_2026-09-20.md` | `REFERENCE_ONLY`; durable, non-secret handoff proposed for Git |

Completeness assertion: 7 items discovered/created for this preflight, 7 items have exactly one explicit disposition.

## Launch gate

**STOP.** No Actor run, credit spend, dataset registration, package build, catalog mutation, commit, or push is authorized yet. The required next step is explicit user approval of the exact canonical target, proposed input, and conservative `$0.148` estimate while preserving the `$0.30` reserve.

## Preflight validation results

- `python3 scripts/validate_dataset_ledgers.py`: **PASS** — DS-000021 through DS-000025 all reported `clean`.
- Six DS-000027 preflight JSON files: **PASS** — all parsed successfully with `python3 -m json.tool`; SHA-256 digests were computed for each local raw file.
- `git diff --check`: **PASS** after removing two Markdown hard-break trailing spaces.
- Focused dataset-ledger provenance tests: **10 passed**.
- YouTube registry tests: raw-authority tests passed, but database-backed tests could not run because the git-ignored local `data/catalog/youtube_inventory.db` is a zero-byte file with no `channels` table. It was not rebuilt or staged during this preflight.
- Direct registry-validator script invocation also has a module-path requirement (`python3 -m scripts.validate_youtube_channel_registry` or `PYTHONPATH=.`); after that environment correction it would still require a populated local inventory catalog.
- Master-tracker tests could not import because `openpyxl` is unavailable in the current system Python and no repository `.venv` exists. No dependency was installed during this preflight.
- Full test suite: **not run** because the task is intentionally stopped before launch and the focused environment blockers above are unresolved.
- Tracked database binaries: **none**. The only `.db` found is the zero-byte, git-ignored local inventory database.

## File disposition at the approval gate

| File group | Necessary | Validated | Commit now | Push now | Disposition |
|---|---:|---:|---:|---:|---|
| Six files under `data/raw/channel-data/DS-000027/preflight/` | Yes | JSON parse and SHA-256 pass | No; ignored raw evidence | No | Preserve locally; never mutate |
| `docs/audits/DS-000027_DR_ARES_PREFLIGHT_PROPOSAL_2026-09-20.md` | Yes | `git diff --check` pass | No; launch workflow incomplete | No | Preserve as handoff |
| `data/catalog/youtube_inventory.db` | No preflight change | Found zero-byte/stale | No | No | Preserve untouched and ignored |

No unrelated file was modified, deleted, moved, staged, or committed. No extra branch was created.
