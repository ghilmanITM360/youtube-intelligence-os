# Addendum to NAC_PROGRESS_N16.md (N17, 2026-11-05)

`NAC_PROGRESS_N16.md` is published evidence at 16bd0cc7 and stays unchanged.

**Count correction.** It says "23 where the blind label was adopted (21 LOW tile-only rows plus 1 random row)". The right count is **22** (21 + 1), as `r13_blind/BLIND_RECONCILIATION_summary.json` records (BLIND_ADOPTED_NATIVE_CROP 21, BLIND_ADOPTED 1). The batch 1 total still sums to 69: 37 + 5 + 2 + 22 + 1 + 2.

**Method wording.** `scripts/camera_all_intervals.py`, published in N16, calls the chained measure with the inlier-spread condition a "frozen rule". Only M0 was preregistered; see `method_v3/METHOD_CHANGE_LOG_N17.md`.

**Superseded class.** The N16 reconciliation set mNLN-U0284 to CHARACTER through a weak rule. N17 records CAMERA in new ledger columns. The N16 column is kept.

**Batch 2 sheets.** The batch 2 brief names sheets `<VID>_B###.jpg`, while the files are `<VID>_D###.jpg`. The reviewer read all 11.
