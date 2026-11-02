# SECOND_MACHINE_POST_AUDIT_REPAIR_v1 (2026-11-02)

Follow-up to `../SECOND_MACHINE_SYNC_AUDIT_v1` (kept immutable). Nothing was pushed, merged, force-pushed or scheduled. PR #36, canonical Finance (`223f4498…`), Machine A (`9c6f42fb…`) and `main` (`08e71926…`) were re-verified unchanged at the end (`git ls-remote`).
Environment: repo `.venv` Python 3.12.14, Node (test_workbook_formatting.mjs), checkout `.claude/worktrees/second-machine-audit-repair-ef17c5` (existing app-created worktree; no new clone/worktree made by this task). Stash (1 entry, 2,267 untracked items) untouched.

## Issue ledger
| # | Issue | Status | Receipt |
|---|---|---|---|
| 1 | DS28-F020 / DS30-F019 `.gitattributes` provenance failure | **FIXED** | below |
| 2 | Universe CSV "stale 430" | **FIXED (relabelled, guarded; values intentionally unchanged)** | below |
| 3 | Canonical vs Machine A Finance split | **Reconciled; candidate validated; integration NOT done** | `finance_reconciliation.md` |
| 4 | Full-suite failure (459/1/1) | **FIXED** — repair branch 462 pass/1 skip/0 fail | `evidence/full_tests_*.log` |
| 5 | 38 vs 48 Finance tests | **VERIFIED_NO_CHANGE** — Machine A adds `test_expansion_queue.py`, `test_nick260_correction.py` (+8..10); candidate = 50 with the 2 new tests here, repair on canonical = 40 | — |
| 6 | CT Checkpoint B / Video 006 evidence | **EXTERNAL_BLOCKED** | `CT_TRANSFER_REQUEST.md` |
| 7 | Hosted CI | **EXTERNAL_BLOCKED** — latest run on canonical head `223f4498` (run 41053016403) = failure, billing annotation per v1; not retried | — |
| 8 | Missing LFS payloads (6) | **VERIFIED_NO_CHANGE** — none needed by any operation here; registry DB in this checkout is real SQLite, sha `39e7a28b…` (frozen) | — |
| 9 | Guide commands | **VERIFIED_NO_CHANGE** — 6 retrievals pass, branch+SHA in `evidence/retrieval_checks.json` | `PRACTICAL_USE.md` |
| 10 | Writer ownership handback | **UNRESOLVED (owner decision)** | below |

## 1. Provenance root cause
`.gitattributes` is shared, mutable repo configuration, not raw evidence. DS-000028-F020 and DS-000030-F019 recorded the 627-byte / `1970079d…` blob that was current at packaging (commit `59cf2185`, 2026-09-22 "preserve DS-000028 raw evidence"). It was later legitimately extended (`71bb5946` 801 B, `b28f0484` 983 B, `c5c3d60e` 895 B, the last for Nick CRLF CSV whitespace rules). Current bytes `93d4461c…` (895 B). The validator's own contract (docstring + `KNOWN_HISTORICAL_SNAPSHOTS`) says mutable snapshots must be pinned to the historical Git blob; these two rows were simply never pinned. Not corruption, not a line-ending/filter effect (raw blobs compared via `git show`).
Repair (commit `cd2160f9`): pin both rows to `59cf21851b5f6e57975ab51944b7572a3edf7471` (blob sha256 == ledger hash, ancestor of HEAD). Expected hashes were NOT changed; no check removed. Regression tests: rows pinned to ingestion-time blob; tamper test in a temp git repo shows later working-tree edits pass but a wrong ledger hash still returns `HISTORICAL_BLOB_SHA_MISMATCH`.
Before/after: `validate_dataset_ledgers` 2 failing rows → 0; ledger tests 11→13 pass.

## 2. Completion count
`reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv` is a checksum-registered **frozen snapshot** (builder docstring, `FILE_CHECKSUMS_SHA256.json`, `VALIDATION.json` 430, an existing test pins 430). It is not a live projection; the workbook builder already overrides its `audit_status` from `VIDEO_AUDIT_966.jsonl`. So it was NOT regenerated (would break checksums/tests and rewrite history). Fix: added `SNAPSHOT_NOTICE.md` (the checksummed README was deliberately not edited) and `test_completion_projection_consistency.py`, which fails if JSONL, completion matrix, checkpoint JSON and workbook-builder summary disagree, or if the snapshot hash/label change. Canonical = 461 everywhere; candidate = 554 everywhere (JSONL, matrix, checkpoint, queue summary, workbook dashboard 554/412 original pending).

## 3. Finance reconciliation — see `finance_reconciliation.md` / `evidence/finance_reconciliation.json`
## 4. Candidate
Local branch `candidate/finance-integration-2026-11-02` = Machine A head `9c6f42fb` + `--no-ff` merge of the repair branch → `554a8335eaa49605a41c7edd4759c662f7fba770` (unpushed, review artifact only, no ownership transfer).
Validation: 966 unique rows/0 duplicates, 554 accepted, 0 accepted IDs lost, `validate_audit_966` + `validate_research` exit 0 (26 source fingerprints), dataset ledgers 0 issues, next queue entry `pTyMmSZ2EVs` (NICK_279), Finance pytest 50 pass, full pytest 462 pass/1 skip/0 fail, Node 2/2 pass. Note: running the queue test regenerates two `accepted_commit` placeholders (`CONTAINING_COMMIT_VERIFY_LIVE` → containing SHA) in `FINANCE_CONTINUATION_QUEUE.csv`; this is expected self-reference and was reverted.

## 5. Git changes / recovery
Local only: `repair/second-machine-post-audit-2026-11-02` (`cd2160f9f6b61da3891819b56eb2726fe0894521`, parent canonical `223f4498`), `candidate/finance-integration-2026-11-02` (`554a8335…`). Backup: `evidence/local_branches.bundle`, `evidence/repair_commit.patch`. No existing ref moved. Scripts: `scripts/` (v1 audit scripts copied from `/private/tmp/yios-sync-audit-v1/` + new reconcile/retrieval scripts).

## Handback requirements (owner decision)
Integration is a pure fast-forward of canonical to Machine A (merge base = canonical head, 0 patch-equivalent). Remaining dependency: the owner/writer publishes a Machine A release and a Machine B (or chosen) acceptance in `FINANCE_WRITER_OWNERSHIP.md`, then FF + cherry-pick `cd2160f9`. Until then PR #36 stays at 461.
