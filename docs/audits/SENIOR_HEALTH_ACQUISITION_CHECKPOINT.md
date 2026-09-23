# Senior Health Acquisition Checkpoint

Updated: 2026-09-22

## Registry and package completion

- Dr. Okoro full acquisition: `COMPLETE`
- Standard package: `COMPLETE` — 66 unique videos, 66 descriptions, 66 thumbnail URLs, and 66 YouTube subtitle transcripts
- Control/full-run deduplication: 67 source records resolve to 66 unique YouTube Video IDs; both immutable Actor run payloads remain preserved
- Registry foreign-key issue: `RESOLVED`
- Root cause: DS-000028 videos referenced canonical channel `UCMJxAeBJ0d1JC937de1eZ0Q`, while registry authority still represented Dr. Okoro only as an unresolved DS-000005 screenshot subject
- Builder fix: inventory-only canonical acquisitions are promoted before child rows, orphan references receive explicit validation errors, and registry DB rebuilds atomically instead of retaining stale rows
- Canonical channels: 71. Evidence review confirmed branch already contained 70 canonical channels including Dr. Ares; DS-000028 adds Dr. Okoro and reduces unresolved screenshot subjects from 7 to 6. The owner approved this evidence-backed count.
- Registry validation: `PASS`; `PRAGMA integrity_check = ok`; foreign-key violations `0`
- Inventory DB: `PRAGMA integrity_check = ok`; foreign-key violations `0`; SHA-256 `247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2`
- Registry DB: `PRAGMA integrity_check = ok`; foreign-key violations `0`; SHA-256 `3570f9bc014cb14a72c1b1571a05ec01ccfe4f362a9f36f9082463a5e342ebc2`
- New-campaign cumulative Apify spend: `$0.264`
- Remaining campaign budget: `$4.236`
- Next channel: Doctor Thomas (`UCFuGMi0idGeyXl6wYK9hg7Q`)

## Doctor Thomas zero-spend precheck

- Checked: `2026-09-22`
- Canonical channel ID: `UCFuGMi0idGeyXl6wYK9hg7Q`
- Current handle: `@DrThomasSeniorHealthTips`
- Public header: 22 videos; Videos tab contains 22 regular uploads
- Shorts: 0; no Shorts tab is exposed
- Archived streams: 0; no Live tab is exposed
- Repository overlap: `DS-000003` contains five screenshot-only items and no canonical video population
- Subtitle sample: 0 of 2 sampled regular videos exposed YouTube captions; both players reported captions unavailable
- Actor: `streamers/youtube-scraper`; live Free-plan price `$4.00 / 1,000` results (`$0.004` each)
- Live actor build: not exposed by the public page or the account's limited-permission Actor view; latest evidence-backed successful build remains `0.0.303`
- Expected maximum Actor charge for 22 results: `$0.088`
- Apify account usage: `$4.28 / $5.00`; account credit remaining `$0.72`
- Campaign budget remains `$4.236`; no Doctor Thomas spend occurred
- Paid run: `NOT_STARTED`; Codex weekly usage reached 85%, triggering the mandatory stop rule
- Acquisition caveat: existing-subtitles-only mode cannot presently guarantee transcripts for all 22 videos; AI transcription remains off

## Completed work

- Last completed channel: Dr. Okoro catalog acquisition
- Channel ID: `UCMJxAeBJ0d1JC937de1eZ0Q`
- Dataset: `DS-000028`
- Apify runs: control `4Jkn3vuO1nDp57HfT`; catalog `uLT4StERHwuiLthti`
- Apify datasets: control `wcOVfRxeT5khIdk8O`; catalog `vvBzcGKPzEfKLnMrX`
- Actor/build: `streamers/youtube-scraper` / `0.0.303`
- Catalog result: `SUCCEEDED`, 66 raw records, 66 unique videos (65 regular, 1 Short, 0 streams)
- Catalog subtitles: 66 available (64 auto-generated, 2 user-generated); 0 unavailable
- Catalog cost: `$0.264`; new-campaign cumulative cost: `$0.264 / $4.50`
- Historical control cost: `$0.004`; combined acquisition cost: `$0.268`
- Remaining approved campaign budget: `$4.236`
- Ending Apify free credit: `$4.59`
- Git HEAD before this checkpoint commit: `f9bac0039328af9c485ca40ebce3fe5893156c69`

## Validation

- Catalog `ingest-existing`: completed as `RUN-000026` / `APIFYRUN-000004`
- Inventory database: `PRAGMA integrity_check = ok`; `PRAGMA foreign_key_check` returned no rows
- Catalog-run rows: 66 video snapshots, 66 available transcripts, 66 thumbnail-evidence rows
- Deduplication: control video `eD2OnCE8iKM` overlapped once; canonical video identity remains unique; catalog run added 65 new video identities
- Coverage: 65 regular videos, 1 Short, 0 public archived streams; matches precheck
- Catalog raw dataset: 2,038,742 bytes; SHA-256 `1d55bcf8a429a8619bb7238cea58f0310770c01ad05e69f40f135fbaa9139dc1`
- Raw dataset: 23,770 bytes; SHA-256 `493caa1673a7d73d9659fe913c7f00a52b179bf43dfbb5e17b6966cb5101cb45`
- Transcript: 13,195 bytes; SHA-256 `a44706058e070033e3e63321ef1b1305eecbe8e70dcd27c664d961646fed8cda`
- Raw-retention verifier: `VERIFIED`
- Focused Channel-ID regression: 1 passed
- Full Apify-ingest module: 21 passed
- Console verification: run ID, target, build, input limits, result count, video identity, status, and `$0.004` cost match local evidence
- Billing detail: Console shows `$0.004`; the local cost-observation row remains non-final because charged-event API fields were unavailable and were not fabricated

## Dataset lineage decision

`DS-000028` remains the Dr. Okoro acquisition lineage. Control and catalog runs retain separate immutable raw evidence and append-only snapshots. One overlapping control video was logically deduplicated by YouTube Video ID; original control evidence remains unchanged.

## Current boundary

- Approved additional acquisition cap: `$4.50`
- New-campaign actual spend: `$0.264`; remaining: `$4.236`
- Apify subscription: Free plan; `$5.00` monthly free platform usage; no payment method configured
- Apify current-period usage after catalog run: `$0.41 / $5.00`; `$4.59` remains
- Actor price display: from `$4.00 / 1,000 videos` (`$0.004` per video)
- Actor/build: `streamers/youtube-scraper` / latest observed successful build `0.0.303`
- Catalog-run maximum cost setting: `$0.30`; actual cost `$0.264`
- Next channel: Doctor Thomas (`UCFuGMi0idGeyXl6wYK9hg7Q`), after usage capacity recovers
- Next state: `CODEX_USAGE_CHECKPOINT_90_PERCENT`

## New-campaign ledger

| Run | Channel | Content Type | Results | Max Charge | Actual Cost | Cumulative Actual |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `uLT4StERHwuiLthti` | Dr. Okoro | regular + Shorts | 66 | `$0.300` | `$0.264` | `$0.264` |

Historical control remains separately recorded at `$0.004`.

## 90% usage checkpoint

- Codex weekly usage reached 90% after successful ingestion. No further Actor run started.
- Inventory DB: integrity `ok`; foreign-key violations `0`; SHA-256 `247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2`
- Registry DB: integrity `ok`; foreign-key violations `0`; unchanged SHA-256 `e8cacdccedca566b4d9c2c5a2bcb86ed07bdf3915aff2a41d5c9a227cffc47e6`
- Registry rebuild attempted after ingestion but stopped on `sqlite3.IntegrityError: FOREIGN KEY constraint failed`; transaction left registry DB unchanged and healthy. Diagnose before rebuilding next session.
- Full standard package generation deferred: mandatory 90% checkpoint forbids starting a large packaging job.

## Zero-spend Dr. Okoro precheck

- Public channel identity reconfirmed: `UCMJxAeBJ0d1JC937de1eZ0Q`, `@drmarcusokoro`
- Public channel header: 66 videos
- Regular-video catalog: 65 items observed across the complete public Videos tab
- Shorts catalog: 1 item (`PSukpB1Io-o`)
- Archived streams: 0 publicly exposed; no Live tab is present and the `/streams` route resolves to the Videos catalog
- Existing control video: `eD2OnCE8iKM`; retain and deduplicate by YouTube Video ID if a full run is approved
- Current Actor schema exposes separate limits for regular videos, Shorts, and streams
- Subtitle mode available: existing subtitles only; language `Any`; plaintext output
- AI video analysis remains off; no paid AI transcription is authorized
- No new Actor run or charge was started during this precheck

## Durable and local-only files

Tracked for commit:

- `data/manifests/DS-000028.md`
- `data/manifests/apify/4Jkn3vuO1nDp57HfT.json`
- this checkpoint

Remote-preservation set:

- `data/raw/channel-data/DS-000026/preflight/29_channel_public_counts.json`
- `data/raw/channel-data/DS-000026/preflight/29_channel_registry_export.json`
- `data/raw/competitors/DS-000028/dataset.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/evidence/actor_input.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/evidence/run_metadata_console_observation.json`
- `data/raw/competitors/DS-000028/apify/4Jkn3vuO1nDp57HfT/transcripts/eD2OnCE8iKM.txt`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/raw/dataset.json`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/evidence/actor_input.json`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/evidence/run_metadata_console_observation.json`
- `data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/transcripts/` (66 files)
- `data/manifests/apify/uLT4StERHwuiLthti.json`
- `data/catalog/youtube_inventory.db`
- `data/catalog/youtube_channel_registry.db` (Git LFS)

Correction (2026-09-22): owner policy requires remote preservation of canonical
raw evidence and valid project database snapshots. DS-000028 acquisition
evidence, existing DS-000026 preflight evidence, `youtube_inventory.db`, and
`youtube_channel_registry.db` passed integrity, secret, and size review for
remote preservation. SQLite WAL/SHM files, caches, temporary files, secrets,
and exact duplicate staging copies remain excluded.

## Doctor Thomas acquisition (2026-09-23)

| Run | Channel | Content Type | Results | Max Charge | Actual Cost | Cumulative Actual |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `WqJIbwUkgkHDHxdaI` | Doctor Thomas | regular only | 22 | `$0.120` | `$0.088` | `$0.352` |

- Channel identity verified before spend: `UCFuGMi0idGeyXl6wYK9hg7Q`, `@DrThomasSeniorHealthTips` — matched exactly, no mismatch.
- Live Apify pricing verified pre-run: Free plan, $4.00/1,000 videos ($0.004/video); expected cost 22×$0.004=$0.088, confirmed exactly on completion.
- Actor input: `maxResults=22`, `maxResultsShorts=0`, `maxResultStreams=0`, `transcriptionAndSubtitle=ALWAYS_SUBTITLES` (existing captions only), `aiVideoDescription=false`, `aiVideoSummary=false`. Platform-enforced `maxTotalChargeUsd=0.12`.
- Run result: SUCCEEDED, 152/152 requests succeeded, 0 failed, 22/22 unique videos, 0 duplicates, 0 Shorts, 0 streams.
- Transcripts: 21/22 AVAILABLE, 1/22 UNAVAILABLE (`fj4TaPrLl8U` — `NO_SUBTITLE_AVAILABLE`, non-blocking per policy).
- Dataset registered as `DS-000029` via `scripts/inventory_catalog.py ingest` (controlled path, no manual SQLite writes); ingested via `scripts/apify_youtube_ingest.py ingest-existing` → `apify_source_run_id=APIFYRUN-000005`, `channel_id=CH-000007`, `registration_run_id=RUN-000028`.
- `scripts/inventory_catalog.py verify --dataset-id DS-000029`: 24 physical files checked, 0 mismatches, `PRAGMA integrity_check: ok`, FK violations `0`, status `VERIFIED`.
- Inventory DB: integrity `ok`; foreign-key violations `0`; SHA-256 `ab9597fef7389319fcc3aad4c942e124e6969112253ac28e721ee918b09fd7b0`
- Registry DB: integrity `ok`; foreign-key violations `0`; SHA-256 `a5b24543b61ebfdd11e35b0495417fc8be7e12796771e8f5c7694039d15a0082` (rebuilt — see fix below)
- Secret scan (`scripts/scan_tracked_secrets.py`): `0` findings.

### Registry bug — fixed (2026-09-23)

`scripts/build_youtube_channel_registry.py` previously crashed with `TypeError: can only concatenate str (not "NoneType") to str` in `_historical_records` (line ~610) whenever an Apify-ingested video had no YouTube captions and no transcript archive backing it (Doctor Thomas's `fj4TaPrLl8U`: `canonical_reference=NULL` and `archive_member_path=NULL`). The function's DS-000001-era legacy fallback assumed one of those two fields was always populated. Fixed by adding an explicit branch: when both fields are `NULL`, the video is retained with `evidence_locator="NO_SOURCE_AVAILABLE"`, `is_placeholder=1`, `transcript_text=""`, and `unavailable_reason="NO_YOUTUBE_SUBTITLE"` (or `notes` if present) — no fabricated transcript text or archive path, no dropped video, no disabled FK checks. Added regression tests `HistoricalRecordsNoSubtitleTests` (both the no-subtitle-and-no-archive case and confirming the normal-transcript path is unchanged) to `tests/test_youtube_channel_registry.py`.

Canonical registry rebuilt successfully: **71 → 72 channels**. Doctor Thomas is now a canonical registry channel (`UCFuGMi0idGeyXl6wYK9hg7Q`, source_group `HISTORICAL_CATALOG` via the inventory-catalog path, exactly once, 22 videos linked, 21 real transcripts, 1 explicit gap, 0 duplicate IDs). `python3 -m scripts.validate_youtube_channel_registry`: `PASS`. Baseline control totals in `scripts/validate_youtube_channel_registry.py` (`EXPECTED`) and matching hardcoded counts in `tests/test_youtube_channel_registry.py` / `tests/test_editing_visual_intelligence.py` updated to the new evidence-backed values (72 channels, 2027 videos, 2015 real transcripts, 12 placeholders, etc.) — all derived from live query output, none hardcoded to a guessed number.

`python3 -m pytest -q`: **353 passed, 3 failed** — all 3 in `tests/test_youtube_channel_master_tracker.py` (`test_channel_submission_and_intelligence_rows_reconcile`, `test_channel_visual_and_capability_values_reconcile`, `test_raw_csv_json_sqlite_workbook_and_query_report_reconcile`), all tracing to the single remaining gap below. Registry/editing/intelligence-refresh test failures (the previous 8) are fully resolved.

### Remaining blocker — cross-channel master tracker workbook

`data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx` ("All Channels" and "Visual Evidence" sheets) needs a new 31-column row for Doctor Thomas, computed by `scripts/build_youtube_channel_master_tracker.mjs` from per-capability status logic (TOPIC_OPPORTUNITY/PACKAGING/HOOK/SCRIPT/EDITING-VISUAL as VALIDATED/PARTIAL/NOT_AVAILABLE/etc.). That script requires an unvendored `@oai/artifact-tool` module (this repo is intentionally dependency-free). The `Datasets` sheet was hand-patched with the DS-000029 row (plain values, verified against the DB) since that carries no derived logic, but the "All Channels"/"Visual Evidence" rows were **not** hand-faked — reproducing 31 columns of derived capability status by hand risked silently corrupting a checked-in artifact. Flagged as background follow-up task `task_803d60fb` rather than guessed. This is a separate, pre-existing cross-channel tracker — distinct from the per-channel Doctor Thomas standard package (which remains deferred for the same `jszip`/`artifact_tool` reason, tracked below, not by this same task).

### Durable files (this acquisition)

- `data/manifests/DS-000029.md`
- `data/manifests/apify/WqJIbwUkgkHDHxdaI.json`
- `data/raw/competitors/DS-000029/dataset.json`
- `data/raw/competitors/DS-000029/apify/WqJIbwUkgkHDHxdaI/raw/dataset.json`
- `data/raw/competitors/DS-000029/apify/WqJIbwUkgkHDHxdaI/evidence/actor_input.json`
- `data/raw/competitors/DS-000029/apify/WqJIbwUkgkHDHxdaI/evidence/run_metadata_console_observation.json`
- `data/raw/competitors/DS-000029/apify/WqJIbwUkgkHDHxdaI/transcripts/` (21 files)
- `data/catalog/youtube_inventory.db`
- this checkpoint

### Next channel

Senior Health Hub (`UCAYG0fzUyxv6OevH88qA45w`) zero-spend precheck only — do not start a paid run for it before the registry-rebuild blocker above is resolved and this acquisition's data is confirmed pushed to remote.
