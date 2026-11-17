# Finance reconciliation matrix (live git objects, fetched 2026-11-02)
| Item | Canonical | Machine A |
|---|---|---|
| Branch | research/finance-economics-intelligence | codex/finance-machine-a-owner-directed |
| SHA | 223f44981ee174988574e86d5e23ae83ee60ee5d | 9c6f42fb33e493314cced538d5c5fa599a29e6c5 |
| Merge base | 223f4498… (= canonical head) | same |
| Commits | 0 unique | 44 unique, 0 patch-equivalent (`git cherry`) |
| Accepted (all 6 dims) | 461 | 554 (all `COMPLETE_LIMITED_EVIDENCE`; zero full-evidence) |
| Ledger rows / duplicates | 966 / 0 | 966 / 0 |
| Added IDs | — | **93**, computed from record statuses, list in JSON; first NICK_186, last NICK_278 |
| Accepted IDs lost | — | 0 |
| Existing accepted records changed | — | 0 byte-for-byte ledger changes (NICK_260 correction lives in `corrections/NICK_260/` + C17/C20 layer inside NICK_260 which is itself a Machine A addition) |
| Source-confidence changes | — | none to existing; added rows carry limited-evidence labels |
| Tooling/schema | — | adds `build_continuation_queue.py`, `build_source_readiness.py`, `machine_a_tools/*`, queue CSV/JSON, expansion K01 + 30 verified-not-registered transcript candidates, 2 test files |
| Projections | 461 | JSONL/CSV/matrix/analysis CSVs, workbook (554), checkpoint, forecast, RESUME_HERE, ownership doc all updated; 372 audit-batch files added |
| Queue/handoff | — | queue summary: 554 accepted, 185 eligible, next `pTyMmSZ2EVs` (NICK_279) |
| Concurrent/conflicting edits | none (Machine A is a strict descendant) | `FINANCE_WRITER_OWNERSHIP.md` modified on A; repair branch touches only validator, its test, a notice file and a new test → merges cleanly |

Machine A is 0 behind / 44 ahead of canonical, so no conflicts; canonical had no commits after the merge base.Full ID list: `evidence/finance_reconciliation.json`.
