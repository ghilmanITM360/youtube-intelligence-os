# Project MRI Audit — YouTube Intelligence OS (2026-11-11)

Companion reports in this folder: PROJECT_EXPLAINED, ARCHITECTURE_MAP, FEATURE_INVENTORY, GIT_SYNC_REPORT, BUGS_AND_TECHNICAL_DEBT, SECURITY_AND_PERFORMANCE, DEVELOPMENT_ROADMAP, TEST_AND_VALIDATION_REPORT, EXECUTIVE_SUMMARY.

## Method and limits
Observed: git state, file tree, `pyproject`/CI, code reads of the orchestrator, Apify client and pipeline demo, SQLite read-only inspection, lint/test/validator runs (all in TEST_AND_VALIDATION_REPORT). **Not** done: line-by-line review of all ~51k tracked Python lines (most lie in research/forensics scratch scripts), execution against live YouTube/Apify, dependency CVE scan, coverage measurement, review of the 2,000+ evidence images. Findings outside the files named are hypotheses.

## Identity and stack
Python 3.12 (stdlib + openpyxl + Pillow; Whisper/ffmpeg for the demo), SQLite (+FTS5), Git LFS for the 141 MB registry DB, GitHub Actions (`validate.yml`, Ubuntu, Python 3.12). 5,541 tracked files: 312 `.py`, ~1,980 JPG evidence thumbnails, 1,544 JSON, 252 CSV. Active branch: Finance/Economics research stream (draft PR #36).

## Data
| DB | Tables | Key counts | Integrity |
|---|---|---|---|
| `youtube_inventory.db` | 27 | 10 channels, 667 videos, 668 transcripts, 45,774 discovered files, 12,335 field provenance, 68 indexes | ok / 0 FK violations |
| `youtube_channel_registry.db` (LFS) | 26 | 75 channels, 2,303 videos, 2,291 FTS transcripts, 825 data layers | ok / 0 |
| `reference_knowledge.db` | 41 | 33 rules, 1,260 sections, 722 video assessments (+31 empty inventory tables) | ok / 0 |
Foreign keys and uniqueness are enforced (migrations 001–011; 009 adds classification uniqueness). Weak points: `max()+1` ID allocation (D4); committed binary DBs as the system of record.

## Key execution path (verified by reading)
`main()` in `scripts/run_youtube_intelligence.py:805` -> `build_plan` (:525) -> locate per-channel artifacts (`find_*_artifact`) -> `validate_coherence` (:425, checks video IDs exist in catalog) -> `attach_forensic_guidance` (:487) -> `write_outputs` (:717). It never calls the network or mutates the DB (module docstring; confirmed no write statements in the reviewed code).

## Bugs / security / performance
See BUGS_AND_TECHNICAL_DEBT.md (16 items, none a confirmed runtime failure at baseline) and SECURITY_AND_PERFORMANCE.md. Highest: CI gap for Finance gates (D1), undeclared `docx` dependency (D2), ledger-pinned code (D3, reproduced), privacy of tracked evidence (S5).

## Health scorecard
Method: 0–10 per dimension from observed evidence only; 5 = works but material gaps; unmeasured items are capped at 6.

| Dimension | Score | Evidence | Priority |
|---|---|---|---|
| Architecture | 7 | Clear layered pipeline, read-only orchestrator, explicit `NOT_AVAILABLE`; but binary DBs in git, `sys.path` hacks, branch sprawl | P2 |
| Code Quality | 7 | ruff/compile clean; 22 broader lint hits (dead locals), few tests-less scripts | P2 |
| Feature Completeness | 7 | V1 layers implemented; V2 absent by decision; no first-party data; Finance 558/1,612 | P1 |
| Security | 7 | 0 secret findings, header token, bound SQL, private repo; tracked private evidence, no CVE scan | P1 |
| Performance | 6 | Test suite 38–44 s; no measured hot paths (unmeasured, capped) | P3 |
| Reliability | 6 | Fail-closed design, but no retry (D5), single-writer assumptions, LFS bootstrap | P2 |
| Database Integrity | 8 | 3/3 DBs pass integrity + FK; ledger/registry validators pass | P3 |
| Test Coverage | 6 | 462 pass; ~74% of scripts referenced by tests (48/65); % coverage not measured | P2 |
| DevOps Readiness | 6 | CI green on main; missing finance gates, CVE scan, Dependabot; Python 3.14 default shell outside supported range | P0/P2 |
| Maintainability | 6 | Excellent docs/provenance, but ledger-pinned code and 5.4 GB history raise friction | P1 |

**Overall: ~6.6 / 10 — healthy V1 research tooling; ready for continued research work, not for external sharing or V2 without the P0/P1 items.**

## Unresolved questions
Whether private evidence will ever leave the private repo; who owns Finance writing after the merge commit; whether the first-party export exists; real coverage %; CVE status of pinned dependencies; correctness of semantic labels in Finance audits (needs human review).
