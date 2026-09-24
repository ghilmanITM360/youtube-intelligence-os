# Dataset Ledger Provenance Reconciliation — 2026-09-23

## Method

For every failing ledger row, `.gitattributes`/`.gitignore`/tracker-code rows
are mutable snapshots (not raw evidence). Per `scripts/validate_dataset_ledgers.py`,
they must be added to `KNOWN_HISTORICAL_SNAPSHOTS` pointing at the exact
historical commit whose blob content hashes to the ledger's declared
`sha256`. All commits touching each path were enumerated with
`git log --all --full-history -- <path>`, each blob hashed with
`git show <commit>:<path> | shasum -a 256`, and compared byte-for-byte
against the ledger value. No fuzzy/partial matching used.

## Evidence table

| Dataset | File ID | Path | Ledger SHA-256 | Ledger Size | Historical Match | Commit | Classification | Proposed Resolution |
|---|---|---|---|---|---|---|---|---|
| DS-000021 | F039 | `.gitattributes` | `35af574b...ccb656` | 475 | YES | `78ad5d728380873d67422d71e67f613ff28c37cf` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000022 | F035 | `.gitignore` | `af8acee8...cf4541028` | 3483 | YES | `b138af0e8e216f897e0bb9a96021a153b5967a72` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000023 | F026 | `.gitignore` | `af8acee8...cf4541028` | 3483 | YES | `b138af0e8e216f897e0bb9a96021a153b5967a72` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000023 | F027 | `.gitattributes` | `35af574b...ccb656` | 475 | YES | `78ad5d728380873d67422d71e67f613ff28c37cf` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000024 | F024 | `.gitignore` | `af8acee8...cf4541028` | 3483 | YES | `b138af0e8e216f897e0bb9a96021a153b5967a72` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000024 | F025 | `.gitattributes` | `35af574b...ccb656` | 475 | YES | `78ad5d728380873d67422d71e67f613ff28c37cf` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000025 | F023 | `.gitignore` | `af8acee8...cf4541028` | 3483 | YES | `b138af0e8e216f897e0bb9a96021a153b5967a72` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000025 | F024 | `.gitattributes` | `35af574b...ccb656` | 475 | YES | `78ad5d728380873d67422d71e67f613ff28c37cf` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000027 | F018 | `scripts/build_youtube_channel_registry.py` | `62eb4561...806c3d22e` | 65108 | YES | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000027 | F019 | `scripts/build_youtube_channel_master_tracker.mjs` | `ba591028...02d94ecd` | 30544 | YES | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000027 | F027 | `scripts/build_youtube_channel_registry.py` | `62eb4561...806c3d22e` | 65108 | YES | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000027 | F028 | `scripts/build_youtube_channel_master_tracker.mjs` | `ba591028...02d94ecd` | 30544 | YES | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000027 | F030 | `tests/test_youtube_channel_registry.py` | `0d932d83...ff887914` | 14513 | YES | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` | HISTORICAL_GIT_BLOB_MATCH | Add pin |
| DS-000027 | F031 | `docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv` | `63983c26...33b0885d` | 13908 | YES | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` (confirms prior `2511013` short-hash claim) | HISTORICAL_GIT_BLOB_MATCH | Add pin |

No `ORIGINAL_SNAPSHOT_UNRECOVERABLE`, `ACTUAL_CORRUPTION`, or
`LEDGER_GENERATION_BUG` rows found. Every failing row is a mutable
code/config snapshot whose byte-exact historical blob still exists in Git
history — the identical situation already handled by the existing
`KNOWN_HISTORICAL_SNAPSHOTS` entries for DS-000021-F034/F035/F037/F038 and
DS-000022-F032/F033/F034.

## Proposed fix

Add 14 entries to `KNOWN_HISTORICAL_SNAPSHOTS` in
`scripts/validate_dataset_ledgers.py`. No manifest CSV edits required — the
pinned-row code path (`validate_row`) only checks blob SHA-256 against the
pin, not `size_bytes`, and every SHA already matches exactly.

No mismatch is skipped, no dataset ignored, no PASS hardcoded, no checksum
or size check removed. `DEFAULT_DATASETS` unchanged; DS-000027 stays outside
the pytest-gated `DATASETS` list as before (all 6 of its rows are now clean
via the same pin mechanism, verified with an explicit
`python scripts/validate_dataset_ledgers.py DS-000027` run).

## Patch

Path: `/private/tmp/yios-ledger-provenance-fix.patch`
SHA-256: recorded below after generation
Files affected: `scripts/validate_dataset_ledgers.py` only
`git apply --check`: recorded below
