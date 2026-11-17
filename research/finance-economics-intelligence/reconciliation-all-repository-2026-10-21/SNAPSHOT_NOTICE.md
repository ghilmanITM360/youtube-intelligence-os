# FROZEN SNAPSHOT NOTICE

Everything in this directory is a point-in-time reconciliation as of 2026-10-21
(checksums in `FILE_CHECKSUMS_SHA256.json`; `README.md` and `VALIDATION.json`
state 430 deep-complete). Do not regenerate or edit it to track later audits.

`FINANCE_UNIVERSE.csv` stays authoritative for identity, URL, provenance and
inclusion decision. Its `audit_status` and `blocker` columns are NOT current.

Current completion authority (see `test_completion_projection_consistency.py`):
`VIDEO_AUDIT_966.jsonl` -> `VIDEO_COMPLETION_MATRIX.csv`,
`build_combined_workbook_data.py` (workbook/dashboard) and
`FINANCE_PROGRESS_CHECKPOINT.json`. Canonical and Machine A branches carry
different accepted counts; read the ledger on the branch you are on.
