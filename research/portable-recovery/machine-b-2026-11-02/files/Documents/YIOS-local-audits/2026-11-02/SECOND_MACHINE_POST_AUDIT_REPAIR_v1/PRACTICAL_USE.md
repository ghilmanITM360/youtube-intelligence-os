# Verified practical use on this machine (2026-11-02)
Run from the repo with `.venv/bin/python` (3.12.14). Always record branch+SHA. All below read-only; results in `evidence/retrieval_checks.json`.
| Workflow | Verified | Ref @ SHA |
|---|---|---|
| One channel (Nick Invests) registry query → 363 rows | yes (DB sha `39e7a28b…`) | working tree |
| One canonical video `XJ4ls6r2MCE` (NICK_185) | yes | canonical `223f4498` |
| One Machine A-only video `pFs8QGikczo` (NICK_278): canonical has partial statuses (COMPLETE + NOT_STARTED), Machine A all six COMPLETE_LIMITED_EVIDENCE | yes via `git show origin/codex/finance-machine-a-owner-directed:…` | `9c6f42fb` |
| Source/claim receipt join (NICK_278: 14 claim groups, 6 source ids, receipts keys: receipts, primary_source_receipts, calculation_receipts, limits) | yes | `9c6f42fb` |
| Performance sensitivity (723 rows; `9r-45QPLl-Y` present) | yes | canonical |
| Visual DNA (`04_PRODUCTION_DNA/VISUAL_DNA.md`, 4,235 chars) | yes | `043b85bf` |
Corrections to the v1 guide: Machine A-only videos are NOT in the canonical checkout — read them with `git show <machine-a-ref>:path` or the candidate branch. "Current completion" is the branch's `VIDEO_AUDIT_966.jsonl`, never `FINANCE_UNIVERSE.csv` (frozen 2026-10-21, 430). Run the queue test only on a scratch checkout: it rewrites two `accepted_commit` placeholders. Tests ≠ hosted CI. No guide commands were found broken.
