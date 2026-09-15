# YouTube Channel Registry and Tracker Handoff

Date: 2026-09-14

## Scope and safety

This feature implements the approved YouTube channel registry, query catalog, validator, and Excel tracker. It did not run Apify, spend credits, start DS-000026, modify `main`, modify `ui/v1`, modify the remediation worktree, open a PR, or merge a branch. Historical `data/raw` and `data/extracted` evidence remains unchanged except for the newly authorized raw channel-target authority committed in `d8eef65`.

The generated registry database is separate from `data/catalog/youtube_inventory.db`. Both database binaries remain ignored and must never be force-added.

## Usage checkpoint

- Latest check: 66% primary / 25% weekly.
- The 85% stop threshold has not been reached.
- If primary usage reaches 90%, start nothing new and update this handoff only.

## Git state and commits

- Worktree: `/Users/ghilmanislam360/Documents/youtube-intelligence-os-channel-registry-2026-09-14`
- Branch: `feat/youtube-channel-registry-and-tracker-2026-09-14`
- Base: `b7f0abfc39dd3906616489f3eb608e0caac8fefd`
- Authority commit: `d8eef65e3d0a301a2c82e6aa78663e26cdc4d917`
- Registry implementation commit: `b9cc126` (`data: add reproducible YouTube channel query registry`)
- Tracker commit: `7c37b76` (`docs: add channel data and intelligence coverage tracker`)
- `c024d13` remains in ancestry.
- Local HEAD, upstream, and live feature-branch remote were all `7c37b769f7d3a6393b01f12ca1b1f9e5e4b04c16` before the final validation additions.
- Update (2026-09-15 continuation): the final commit (`ef2813bca6993f250c7c4cb3a88edc7b7dfc5774`, "data: finalize reproducible YouTube channel tracker") has been pushed. Local HEAD, `@{upstream}`, and `git ls-remote origin` for `feat/youtube-channel-registry-and-tracker-2026-09-14` were independently re-verified as identical (`ef2813bca6993f250c7c4cb3a88edc7b7dfc5774`), 0 ahead/0 behind, on 2026-09-15. Push is complete; this line no longer describes a pending step.

## Authoritative target controls

- Batch A: 47 rows
- Batch B: 20 rows
- Submitted rows: 67
- Exact duplicates: 4
- Normalized URL identities: 63
- Canonical target channels: 63
- Ordered payload SHA-256: `b8f72bfee5d3c8edc206dd4a28d4f31470b9f24a1305044548a1dc78ebd90296`
- Canonical identity resolution: 63 verified, 0 unresolved

Target progress:

| Group | `COMPLETE` | `COMPLETE_WITH_LIMITATIONS` | `NOT_EXTRACTED` | Total |
|---|---:|---:|---:|---:|
| Original targets | 26 | 8 | 10 | 44 |
| Later-added targets | 0 | 0 | 19 | 19 |
| All targets | 26 | 8 | 29 | 63 |

No target is classified `PARTIAL`, `UNAVAILABLE_OR_DELETED`, or identity-unresolved.

## Registry controls

Canonical channel source groups:

| Source group | Channels |
|---|---:|
| Standard packages | 35 |
| Historical catalog/intelligence format | 5 |
| Identity-only targets | 29 |
| Total | 69 |

Additional controls:

- Channels with stored video data: 40
- Stored channels outside the target list: 6
- Datasets: 25
- Unique videos: 1,904
- Real transcripts: 1,893
- Explicit transcript placeholders: 11
- Videos missing public descriptions: 14
- Screenshot-only non-channel subjects: 7
- Channel data-layer rows: 759 (`69 × 11`)
- Intelligence coverage rows: 552 (`69 × 8`)

The registry keeps identity, extraction, package, video metadata, description, transcript, thumbnail metadata, visual assets, forensic video, intelligence, and first-party analytics states independent. Raw data availability does not mean generated intelligence. Public metrics do not mean first-party YouTube Analytics.

## Visual and intelligence controls

- Full forensic visual channel: xkcd's What If? (`UC6IxnFzHofFJ5X2PycSMsww`, historical `CH-000004`). Evidence: 83 thumbnail URLs/downloaded thumbnails, 107 keyframes, 3 canonical source videos, and 107 timestamped observations.
- Downloaded thumbnail evidence without full forensic video: Dr. Aliza Wright | Advice (32 thumbnails, 7 screenshots) and Dr. Elias Senior Health (29 thumbnails).
- Title-only historical packaging: Matty Invests and Mr. Finance.
- Standard packages: 35 channels with thumbnail URLs only; no downloaded thumbnail or forensic evidence is inferred.
- Seven screenshot-only subjects remain unmapped and separate from canonical channels.

Generated intelligence rows by capability:

| Capability | Generated rows |
|---|---:|
| Topic Opportunity | 5 |
| Packaging | 5 |
| Hook | 5 |
| Script | 5 |
| Editing/Visual | 1 |
| Unified Orchestration | 5 |
| Channel Strategy | 4 |
| First-party Analytics | 0 |

The 35 standard-package channels are input-ready but have no generated per-channel Topic, Packaging, Hook, or Script artifacts. First-party Analytics is `SCHEMA_READY_NO_DATA` for all 69 channels.

## Reproducible SQLite registry

Tracked implementation:

```text
data/catalog/channel_registry/schema.sql
data/catalog/channel_registry/example_queries.sql
scripts/build_youtube_channel_registry.py
scripts/build_youtube_channel_master_tracker.mjs
scripts/validate_youtube_channel_registry.py
tests/test_youtube_channel_registry.py
tests/test_youtube_channel_master_tracker.py
docs/YOUTUBE_CHANNEL_REGISTRY.md
docs/audits/YOUTUBE_CHANNEL_REGISTRY_QUERY_RESULTS_2026-09-14.md
```

Ignored generated database:

```text
data/catalog/youtube_channel_registry.db
```

The validator passes integrity, foreign keys, required views, uniqueness, evidence links, source-group distinctions, visual controls, intelligence input/output distinctions, and idempotent double-build controls. Both builds produced identical counts, including 69 channels, 1,904 videos, 1,904 transcript rows, 25 datasets, 239 artifacts, and 552 intelligence rows. FTS5 is enabled; the standard SQL transcript-search fallback returns the same sampled results.

All 35 standard transcript ZIPs pass CRC, unique-member, member-count, parsed-text, placeholder-reason, and SHA-256 reconciliation against SQLite: 1,601 videos, 1,591 real transcripts, 10 placeholders, and 33 real transcripts above Excel's 32,767-character cell limit. The five historical channels contribute 303 videos, 302 real transcripts, one placeholder, and three additional transcripts above the Excel limit. Complete long text remains in SQLite/source ZIPs rather than being forced into Excel cells.

## Excel tracker

Workbook:

```text
data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx
```

Sheets:

1. `Dashboard`
2. `All Channels`
3. `Pending Channels`
4. `Data Coverage`
5. `Visual Evidence`
6. `Datasets`
7. `Submitted URLs`
8. `Intelligence Coverage`
9. `Definitions`

The workbook was authored with `@oai/artifact-tool`; the operation marker ran exactly once. Dashboard controls are formula-linked and evaluate to 69/63/40/35/5/29/1/3/2/7/1,904/1,893/11/14. All nine sheets were rendered and visually reviewed. The Artifact Tool renderer does not calculate `HYPERLINK`, but a disposable LibreOffice recalculation proved canonical YouTube and repository formulas resolve to their friendly link labels. No alternative library authored the delivered workbook. A clean temporary rebuild from the tracked builder was semantically identical to the repository workbook across values, formulas, styles, dimensions, frozen panes, tables, merged cells, and conditional formatting.

Workbook tests reconcile channel IDs, target groups, extraction/package states, videos, transcripts, placeholders, description gaps, dataset memberships, visual evidence, all 552 capability rows, 67 ordered submissions, duplicate references, formulas, tables, and portable links against JSON and SQLite.

## Validation evidence

- Registry plus workbook tests: 23/23 passed.
- Package-validator and package-generalization tests: 11/11 passed.
- Registry validator: PASS.
- SQLite two-run idempotence: PASS.
- All example SQL queries: PASS.
- Cross-format raw/CSV/JSON/SQLite/workbook/query-report reconciliation: PASS.
- Standard-package ZIP CRC/text/SHA reconciliation: 35/35 channels; 1,601/1,601 members.
- Downloaded-thumbnail manifests/files/checksums: 32 + 29 + 83 verified.
- Forensic artifact: 107 keyframes, 3 source videos, 107 observations, and 13/13 provenance files verified.
- Formula error scan: 0 matches.
- Credential/token scan: no high-confidence findings.
- Workbook absolute-path scan: no `/Users/` or `file://` links.
- Full bundled suite: 309 tests; 307 passed; 1 failure and 1 error.

The two full-suite problems are pre-existing isolated-worktree environment issues, not feature failures:

1. `test_no_raw_evidence_files_were_added_for_these_sources` expects ignored DS-000018 raw evidence that is absent from the linked worktree.
2. `test_output_and_all_channel_availability_are_deterministic` compares historical catalog paths containing the main worktree's absolute path with normalized feature-worktree output.

Both were previously confirmed to pass read-only in the main worktree. No evidence or dependencies were changed to hide them.

## Immutable-state evidence

- Main HEAD remains `a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8`; its eight user-owned untracked files retain their recorded SHA-256 values.
- Historical catalog SHA-256 remains `3751021da50c4f6cc7289db795bcf848e78be07066de72266298e2a4d2836ad6`.
- Remediation HEAD remains `b7f0abfc39dd3906616489f3eb608e0caac8fefd` with its pre-existing untracked files.
- `ui/v1` remains clean at `0412932a4ff77e3e3bfe33c45f4e4889e17a7b23`.
- Feature diff under `data/raw` and `data/extracted` contains only the authorized new raw target authority; no existing raw/extracted file changed.

Do not record this file's SHA-256 inside itself.

## Audit resolution addendum (2026-09-15 continuation)

A follow-on audit (`docs/audits/YOUTUBE_CHANNEL_REGISTRY_COMPLETION_AUDIT_2026-09-15.md`) independently re-verified this handoff's controls and flagged three items needing resolution. Findings, reproduced a second time in this continuation session:

**Intelligence coverage row count — 552 is correct.** `552 = 69 channels × 8 capabilities`, confirmed both by direct SQLite query (`SELECT COUNT(*) FROM intelligence_coverage` = 552, `SELECT COUNT(*) FROM channels` = 69, `SELECT COUNT(*) FROM intelligence_capabilities` = 8) and by this document's own §"Registry controls" above. An external audit brief expected `414 = 69 × 6`; there is no schema evidence any capability is excluded from the per-channel cross-join, so `414` is a stale figure from that brief, not from this codebase. Kept here as a historical/audit-brief value only, superseded by 552.

**Input-ready channel counts — 40 and 35 are both correct, measuring different things.** `40` = channels with `input_data_available = 1` for a capability (35 `STANDARD_PACKAGE` + 5 `HISTORICAL_FORMAT`, confirmed by SQL join on `channels.package_status`). `35` = the narrower subset additionally carrying `status = 'DATA_READY'` (standard-package only; the 5 historical-format channels carry `status = 'VALIDATED'` instead, despite also having usable input data). Both numbers are already guarded by existing tests (`tests/test_youtube_channel_registry.py:177,197,252,281`) and by `scripts/validate_youtube_channel_registry.py`'s `EXPECTED` dict (`channels_with_video_data: 40`, `standard_packages: 35`, `intelligence_coverage_rows: 552`), so no new regression test was added.

**Visual evidence terminology.** To avoid ambiguity in the "83 thumbnail URLs/downloaded thumbnails... 107 keyframes... 107 timestamped observations" wording above: the 32/29/83 "downloaded thumbnail" counts are fetched-and-hashed metadata records (`sha256`, `byte_size`, `final_url` captured per thumbnail in each channel's packaging-intelligence JSON) — the underlying JPEGs are not committed to the repository, only their metadata is. The 107 "keyframes" for CH-000004 are likewise structured JSON observations (`measured_features[].keyframe_count`, cross-checked against 203 `visual_features` entries covering 92 distinct video/timestamp pairs across 3 source videos) — no keyframe image files exist anywhere in the repository; `data/raw/keyframes/` is tracked but contains only a `.gitkeep` placeholder. This does not indicate missing work — it reflects the feature's intended design (structured forensic observations, not a committed image corpus) — but "keyframes"/"downloaded thumbnails" should be read as evidence records, not image files, when this document is cited.

**Excel `HYPERLINK()` cached-error cells — accepted with documented limitation (resolution B), not rebuilt.** Direct ZIP/XML inspection (stdlib `zipfile`, no `openpyxl` needed) reproduces the 1,090 `HYPERLINK()` formulas = 1,090 cached error-typed cells exactly, 100% resolving to valid `youtube.com`/`youtu.be`/`github.com` URLs (zero local file paths), with no `calcPr` element present (Excel's automatic-recalculation default applies). The cached error text is the standard `"HYPERLINK is not implemented. linkLocation=..., friendlyName=..."` placeholder left by a writer/recalculation engine that doesn't evaluate `HYPERLINK()`, not a broken formula. This section's own earlier claim of a disposable LibreOffice recalculation proving correct resolution was made in the original authoring environment; no `openpyxl`, LibreOffice, Numbers, or Excel exists in this or the prior audit's verification environment, so that specific claim could not be independently re-executed here. Rebuilding the workbook was not attempted (would require `openpyxl`, which is not installed and was not auto-installed per this task's safety rules — see below). No formula was replaced with a hardcoded value.

**`openpyxl` availability.** Not installed in this environment (system Python 3.9.6, Homebrew Python, or either local venv checked). Per this task's rules, it was not auto-installed. This blocks ~10 of the registry/workbook/tracker tests and the validator script's idempotence re-check from running here; the 4 raw-authority tests that don't touch the workbook (`RawChannelAuthorityTests`) run and pass without it. This is an environment/dependency-availability limitation, not a known code defect.

## Remaining release steps

Status as of the 2026-09-15 continuation: steps 1-4 below are complete (see addendum above). Retained for reference:

1. Verify the feature status and that the ignored database/evidence are not staged. — Done; `data/catalog/*.db` remains gitignored and untouched.
2. Commit only the validated documentation, reproducible workbook builder, cross-format/ZIP reconciliation tests, and this handoff. — Done at `ef2813b`.
3. Push only `feat/youtube-channel-registry-and-tracker-2026-09-14` with its own upstream. — Done; see addendum for re-verified SHAs.
4. Verify local, upstream, and live remote SHAs match. — Done.
5. Do not open a PR or merge. — Still applies; no PR was opened, no merge performed.

Remaining open item: install `openpyxl` (or equivalent) in a verification environment to independently re-run the workbook-dependent tests and validator idempotence check; this continuation could not do so per its no-auto-install rule (see addendum).
