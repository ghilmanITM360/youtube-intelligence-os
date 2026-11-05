# Reviewer deviations from briefs (recorded by orchestrator)
- v3 crop reviewer read CROP_INDEX_GNaBxt_zIRA.csv (not in brief input list; it only maps sheets to interval ids/frames), wrote rows in batches of 2-3 sheets, and left a helper script ~/YIOS-local-audits/.ap.py (CSV append only; moved to session scratchpad, not evidence). Output integrity checked: 128 rows, 128 unique ids, 11 fields each.
- v2/v3 dense reviewers repaired unquoted-comma rows after writing (self-reported); final CSVs parse 288/280 rows x 9 fields.
- v1 dense reviewer labelled all 282 rows OBSERVED including changes between tiles; limitation recorded in ledger (density/limitation columns) and superseded for 99 rows by native-crop verification.
