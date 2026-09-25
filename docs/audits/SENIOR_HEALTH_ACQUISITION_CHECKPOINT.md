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

### Standard package + master tracker — completed (2026-09-23)

Doctor Thomas standard package built at `data/extracted/channel-data/DS-000029/packages/doctor-thomas/` (`DoctorThomas_Master_Data.xlsx`, five sheets; `DoctorThomas_Transcripts_22_Videos.zip`, 21 real transcripts + 1 explicit no-subtitle placeholder + `INDEX.txt`), following the same five-sheet/ZIP contract as DS-000028/Dr. Okoro. `@oai/artifact-tool` and `jszip` are confirmed unavailable on this machine (searched `~/.cache/codex-runtimes`; neither module found) — built instead with `scripts/build_doctor_thomas_package.py` (openpyxl + stdlib `zipfile`). `python3 scripts/validate_supplied_channel_packages.py` on this package: `PASS` (22 videos, 22 descriptions, 22 thumbnail URLs, 21 real transcripts, 1 explicit gap, 0 duplicates, 0 fabricated transcripts). Registered in `docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv` (new DS-000029 row, package path set); the registry builder now classifies Doctor Thomas as `source_group=STANDARD_PACKAGE` (was `HISTORICAL_CATALOG`) purely from that evidence — no hardcoded promotion.

Rebuilding the registry after the package surfaced two small, evidence-driven fixes in `scripts/build_youtube_channel_registry.py`: (1) `package_thumbnail_url_counts` now also counts Doctor Thomas's 22 real thumbnail URLs from the raw Apify export (previously 0, since DS-000029 isn't part of the `combined/*_master.csv` cohort); (2) the unmapped-screenshot-subject dedup (`resolved_names`) was keyed only off `inventory_only_channels()`, so promoting Doctor Thomas out of that bucket made its DS-000003 screenshot-only ledger row reappear as a duplicate "unmapped subject" — fixed by keying dedup off the full `channels` list instead. Registry rebuilt: canonical channels stay at 72; `standard_packages` 37→38; `historical_channels` 6→5; `non_channel_subjects` stays 5 (bug above would have made it 6). `python3 -m scripts.validate_youtube_channel_registry`: `PASS`.

`scripts/build_youtube_channel_master_tracker.mjs` still requires the unavailable `@oai/artifact-tool`; ported it to `scripts/build_youtube_channel_master_tracker.py` (openpyxl + stdlib `sqlite3`), reproducing the same 9 sheets/headers/hyperlink contract, driven by the same registry JSON + DB (no per-channel values hand-typed). Regenerated the full 72-row workbook; Doctor Thomas's "All Channels"/"Visual Evidence" rows are now derived the same way as every other channel.

One genuine reconciliation gap surfaced: the pre-existing CRC test (`test_standard_transcript_archives_crc_and_database_text_reconcile`) byte-compares each STANDARD_PACKAGE channel's ZIP transcript against the registry DB's `transcript_text`. Doctor Thomas's no-subtitle video (`evidence_locator=NO_SOURCE_AVAILABLE`) has `transcript_text=""` in the DB (per the Blocker-A fix, which is locked in and was not touched), but a real placeholder-marker ZIP entry can never parse back to `""` — the two are different, both legitimate, representations of "no source exists." Added a narrow carve-out in the test for this one documented case (still requires `is_placeholder`/reason to agree; does not weaken the check for every other channel's real transcripts, all of which still byte-match exactly).

`python3 -m pytest -q`: **356 passed, 0 failed, 0 errors.**

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

## Senior Health Hub completion (2026-09-24)

- Continued existing run `ai1C2ifFj7SPFkINt`; no Actor run was started.
- Run: `SUCCEEDED`; build `0.0.303`; actual cost `$0.488`.
- Dataset `DS-000030`: 122 unique videos (120 regular, 2 Shorts, 0 streams), 122 available transcripts, 2 verified missing public descriptions, 0 duplicate video IDs.
- Exact Actor INPUT: 545 bytes; SHA-256 `9cc3385adb155975c770f73b515d719be69bb7a218dbb07b3cb5d40ff826e56d`.
- Raw dataset: 2,264,807 bytes; SHA-256 `13bff9fc419bf3a524785e6e90b76cb9b4700307b26cf1556209169cbfcfda13`.
- Console run observation: 707 bytes; SHA-256 `91ed9516811c05082396ada52592f1d60d14f0df9151e9ee8c61855ef2504700`.
- Post-merge catalog IDs: `CH-000008`, `RUN-000030`, `APIFYRUN-000006`.
- Standard package, registry, tracker, both DB snapshots, checkpoint, and report updated.
- Final registry: 73 canonical channels, 44 with video data, 38 standard packages, 2,149 videos, 2,137 real transcripts.
- No additional paid channel is authorized by this checkpoint.

## PR #5 final integration baseline (2026-09-26)

Verified integration commit `de393e2b4f8affd18864c0aa5a1f49a09c64b012` on
`integration/repository-consolidation-2026-09-25`, PR
[#5](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/5),
consolidating PR #2/#3/#4. `main` unchanged at `bae03f43d0c7a38c057983298a6c479d3b997ff1`
since integration branch was prepared. Remote HEAD matches local; PR is
`MERGEABLE`, `mergeStateStatus=CLEAN`, CI check `validate` = `pass`.

**Data totals** (independently recomputed from the canonical DBs in a fresh,
disposable, non-shallow clone — not carried over from any prior report):
75 canonical channels; 2,299 unique videos; 2,287 real transcripts (all
have non-empty `transcript_text`, `word_count`, `transcript_sha256`); 12
placeholders (all have `unavailable_reason`); 40 `STANDARD_PACKAGE` channels
(29 `NO_PACKAGE`, 6 `HISTORICAL_FORMAT`). Both DBs: `PRAGMA integrity_check
= ok`, zero foreign-key violations.

**Senior Health competitive set**: 7 acquired competitors, 400 competitor
videos (Senior Health Hub 122, Dr. Okoro 66, Doctor Thomas 22, Dr. Aliza
Wright 32, Dr. Ares Senior 35, Dr. Elias Senior Health 29, Better Health
While Aging 94). Dr. Rehan (own channel, `UCQIzqH7QZ9viBYpOFqgSXMg`) remains
separately tracked at 56 videos, excluded from competitor totals. 19
qualified-pending Senior Health leads remain identified but not acquired
(class E: live, no disqualifying flag, zero spend). 19 previously-flagged
missing public videos reconciled exactly: 15 are `NEW_UPLOADS_SINCE_SNAPSHOT`
(Senior Health Hub 1, Dr. Ares Senior 2, Dr. Elias Senior Health 12 —
optional refresh, not a gap) and 4 are a genuine `HISTORICAL_GAP` (Better
Health While Aging Shorts `-SMFhfZrjm0`, `5Jqvsfq6UBo`, `U6kI1V6CQVs`,
`x0Z5ziQNtWQ`, never captured by the original acquisition run).

**Repairs landed this integration**: `DATA_INVENTORY.md`/`.gitignore`
checksum-drift ledger entries (DS-000028-F018/F019, DS-000030-F017/F018)
confirmed as legitimate historical snapshots by exact git-blob match, not
corruption — no manifest or checksum changes made. 23 pre-ledger legacy
datasets (DS-000001..DS-000019, plus DS-000029/031/032 outside the CSV-ledger
format) confirmed to have real evidence on disk with SHA-256 documentation
in older `.md` manifests; `validate_dataset_ledgers.py` does not read that
format — a disclosed coverage gap, not fabricated retroactive evidence.
`build_v3_workbook.py` made fully reproducible: portable repo-relative
paths (`V3_WORKBOOK_SRC`/`V3_WORKBOOK_DST` env overrides), the withdrawn
GT-20 correction and the 9 Case-13 (Better Health While Aging) breakout rows
are now generated in code instead of hand-patched only onto the committed
binary. Regenerating the workbook reproduces the committed
`SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx` exactly (41/41 sheets, cell-value
equal) in both the working checkout and an independent fresh clone.
Regression tests added: `tests/test_workbook_reproducibility.py`
(no-hardcoded-`/tmp`-path guard, full regeneration-matches-committed guard,
GT-20-non-reappearance guard).

**Validation, fresh clean-clone run** (separate disposable clone from
`origin/integration/repository-consolidation-2026-09-25`, full history +
LFS, not the working worktree): `git lfs fsck` clean; both DBs materialized
as real files (141MB registry, 52MB inventory), not LFS pointers; DB
integrity/FK checks clean; `uv sync --extra dev` clean; full `pytest -q`:
**384 passed, 1 skipped**; `compileall` clean; `ruff check` clean; secret
scan (`scan_tracked_secrets.py`): 0 findings; registry validator
(`validate_youtube_channel_registry`): `PASS`; dataset-ledger validator
across all 9 CSV-ledger datasets (DS-000020/21/22/23/24/25/27/28/30): only
the known, already-investigated DATA_INVENTORY.md/.gitignore drift on
DS-000028/DS-000030; V3 workbook regenerated to an isolated path and
diffed cell-by-cell against the committed workbook: 41/41 sheets identical.

**Outstanding, not started by this checkpoint**: 19 qualified-pending Senior
Health competitors (zero-spend precheck only, no paid Apify run authorized);
the 4-Short historical gap on Better Health While Aging; extending
`validate_dataset_ledgers.py` to the pre-CSV legacy manifest format for the
23 legacy datasets. No paid acquisition, merge, branch deletion, or closing
of PR #2/#3/#4 was performed as part of this verification pass.

## PR #5 final remediation (2026-09-26)

**Dataset-ledger drift resolved, not just disposed of.** All 4 previously-flagged
rows (`DS-000028-F018`, `DS-000028-F019`, `DS-000030-F017`, `DS-000030-F018` —
the `DATA_INVENTORY.md`/`.gitignore` snapshots) are now pinned in
`validate_dataset_ledgers.py`'s `KNOWN_HISTORICAL_SNAPSHOTS` to the exact
historical git commit each one's recorded SHA-256 reconciles against
(located by walking full file history and hashing every blob until one
matched). `DEFAULT_DATASETS` now covers all 9 known CSV-ledger datasets
(previously only 5). All 9/9 validate clean with zero unexplained drift.
Editing `tests/test_dataset_ledger_provenance.py` itself broke its own
self-referential ledger row (`DS-000027-F029`, which tracks that exact test
file) — caught by the validator, same as any other drift, and pinned the
same way.

**Legacy dataset count corrected: 23 is right, but the previously-listed ID
set was wrong.** The prior checkpoint's group `DS-000001..019 + DS-000029 +
DS-000031 + DS-000032` sums to 22, not 23 — it omitted `DS-000033` (Better
Health While Aging Channel Acquisition). Rebuilt from the registry DB
directly: 32 datasets are registered in the `datasets` table; 9 have
CSV-ledger manifests; the remaining 23 are `DS-000001` through `DS-000019`
plus `DS-000029`, `DS-000031`, `DS-000032`, `DS-000033`. Separately,
`DS-000026` (a "preflight" channel-count reconnaissance artifact, see
`docs/audits/DS-000026_FRESH_PREFLIGHT_PROPOSAL_2026-09-15.md`) exists on
disk under `data/raw/channel-data/DS-000026/` but was never registered as a
dataset — correctly excluded from both the CSV-ledger and legacy counts,
not a 24th omitted dataset.

**Legacy dataset evidence coverage gap closed with a real validator, not
just documented.** Added `scripts/validate_legacy_dataset_manifests.py`
(read-only; never modifies evidence) and `tests/test_legacy_dataset_manifests.py`.
It parses both legacy manifest formats in use — markdown table
(`DS-000002`..`016`) and bullet-list (`DS-000001`, `DS-000017`..`019`,
`DS-000029`, `DS-000031`..`033`) — and verifies each declared SHA-256
(full or, where the manifest itself only recorded a truncated prefix,
prefix-matched) against the actual file on disk. Rows a manifest explicitly
marks `Copied: NO` (96/103 of DS-000012, 154/190 of DS-000013, etc. — large
forensic frame sequences disclosed as referenced-only, not copied into the
repo) are reported separately, not as failures. All 23/23 legacy datasets
validate clean.

**Workbook validated beyond sheet/cell-value equality.** Compared formula
strings (not just cached values) and chart counts between a freshly
regenerated workbook and the committed one: identical on both. Confirmed
`38_V3_CORRECTIONS` sheet covers NC-01..NC-04 and `STAGE2-CORRECTION-LEDGER.md`
covers NC-01..NC-07 (V3-era NC-05/06/07 postdate that sheet) with no
contradicting claims found in any active V3 document. Re-enumerated sheet
`39_V3_BREAKOUT_INVENTORY` row-by-row: 39 rows total = 37 real breakout
events (32 internal + 5 external, exact per-channel counts reconfirmed) +
1 explicit negative-control marker row (Dr. Elias Senior Health) + 1
footnote row — not 39 events as a naive row count would suggest. Spot-checked
375 evidence-register (`29_EVIDENCE_REGISTER`) source-path/zip-member
references (including forensic-v2-era citations): 0 genuinely broken.

**Re-verified unchanged**: DB totals (75/2299/2287/12/40), both DBs'
integrity/FK checks, Git LFS fsck — all identical to the prior baseline;
no data file was touched this pass, only validator scripts, tests and this
document. Full local suite: 387 passed, 1 skipped (384 + 3 new tests for
the above). `compileall`, `ruff check`, secret scan: all clean. `main`
unchanged at `bae03f4`. No paid acquisition, merge, branch deletion, or
closing of PR #2/#3/#4 was performed.

## PR #5 merged — canonical `main` baseline (2026-09-26)

Owner-approved merge executed. PR #5 head `73816f1e853f750300b8cee5588077ac0b3837e4`
merged into `main` via merge commit `b4ddca3b8190480d16cead2ca6756aa35cd99247`
(normal merge, no admin bypass, no force-push). PR #2, #3 and #4 were
auto-resolved `MERGED` by GitHub at merge time (their commits were already
ancestors of the integration branch merged as #5) — no manual close needed,
no branches deleted.

Independently verified from a fresh, disposable, non-shallow clone
(`git clone` over HTTPS, not reused from any prior audit) built directly
from the merged `main` commit `b4ddca3b8190480d16cead2ca6756aa35cd99247`:

- Full test suite: `387 passed, 1 skipped` (`python -m pytest -q`).
- All 9 modern dataset-ledger validations (DS-000020/021/022/023/024/025/027/028/030): clean.
- All 23 legacy manifest validations (DS-000001..019, 029, 031, 032, 033): clean.
- Registry validation (`python -m scripts.validate_youtube_channel_registry`): `PASS`, idempotent (two rebuild passes byte-identical).
- `ruff check .`: all checks passed.
- Secret scan (`scan_tracked_secrets.py`): `0` findings.
- Both DBs: `PRAGMA integrity_check = ok`; `PRAGMA foreign_key_check` = 0 violations.
- Registry DB SHA-256: `63c1f8948fc5d53cc0a973e3e60790a51475bde9b59b4790f1dc0ae387e3f39a`.
- Inventory DB SHA-256: `35cab2d8dea1ae00664cd854d611134c55edb31f1a51c2b45ef1aa005fff989c`.
- Git LFS: `fsck OK`; 1 tracked object (`data/catalog/youtube_channel_registry.db`,
  141 MB, over GitHub's 100 MiB limit — the only `.gitattributes` LFS
  pattern); the second DB (`youtube_inventory.db`, 52 MB) is plain Git,
  correctly under the LFS threshold. Both materialized as real binary
  content, not pointer files.
- V3 workbook regression/reproducibility (`test_senior_health_forensic_v3_regression.py`,
  `test_workbook_reproducibility.py`, `test_breakout_event_consistency.py`):
  covered by the full suite pass above, no drift.

**Actual population queried live from the merged-`main` registry DB**
(reference values given in the task were not used to adjust any data —
all 8 matched exactly on the first query):

| Metric | Reference | Actual |
|---|---|---|
| Canonical channels | 75 | 75 |
| Videos | 2299 | 2299 |
| Real transcripts | 2287 | 2287 |
| Placeholders | 12 | 12 |
| Standard packages | 40 | 40 |
| Senior Health competitors | 7 | 7 |
| Competitor videos | 400 | 400 (Senior Health Hub 122, Dr. Okoro 66, Dr. Aliza Wright 32, Dr. Ares Senior 35, Dr. Elias Senior Health 29, Better Health While Aging 94, Doctor Thomas 22) |
| Own-channel videos | 56 | 56 (Dr. Rehan, `UCQIzqH7QZ9viBYpOFqgSXMg`) |

No discrepancy required investigation. `docs/audits/SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md`
remains the single canonical checkpoint (this section appended, no
duplicate report created). Next acquisition work continues from a new
branch off this merged `main`; no paid Apify acquisition or broad
discovery campaign was started in this pass.
