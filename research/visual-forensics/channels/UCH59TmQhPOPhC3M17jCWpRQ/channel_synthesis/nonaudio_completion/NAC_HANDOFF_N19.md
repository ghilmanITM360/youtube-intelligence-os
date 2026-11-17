# Barely Evolved: handoff N19 (2026-11-06)

Session 15f69c1b. Branch research/barely-evolved-visual-forensics. Base N18 `95866052a7a467566d759707b23016457bec7129`. This file supersedes `NAC_HANDOFF_N17.md` for the items below. N19's commit and readback are in `evidence/N19_PUBLICATION_RECEIPT.json` on Machine A and in `BE_OPS_LOG.txt`, because a commit cannot contain its own receipt.

## Status
`FINAL_AUDIT_MATRIX_v3.csv` statuses are unchanged: R08 and R20 PARTIAL, R09 and R21 BLOCKED, R22 FAIL. `NON_AUDIO_COMPLETE` and `CT_SCAN_COMPLETE` are not awarded.

## Camera reconciliation
Table: `method_v3/CAMERA_RECONCILIATION_N19.csv` (46 rows). Measure: `method_v3/FLAGGED_REGION_MOTION_N19.csv`, script `scripts/flagged_region_motion_n19.py`. Ledgers and `BLIND_RECONCILIATION_v3.csv` are not changed; for these rows the N19 table overrides their `final_*` columns.

- **6 R3 rows, now inspected on native frames.** The blind CHARACTER label did not hold on any of them.
  - Frame-wide zoom plus camera attribution, 4 rows: mNLN-U0189, mNLN-U0254, GNaB-U0192 (class MIXED) and GNaB-U0109 (class CAMERA).
  - Attribution unresolved, 2 rows: mNLN-U0231 and GNaB-U0239. They have a white background and no static reference, so M3 CAMERA_FRAMEWIDE is not confirmed there. Their ledger attribution CAMERA is withdrawn.
- **5 ledger rows with M3 NO_CAMERA or OBJECT_MOVE, inspected.**
  - mNLN-U0167 and mNLN-U0276: ledger class CAMERA is wrong; now CHARACTER and GRAPHIC_TEXT, NOT_CAMERA.
  - mNLN-U0222: DIGITAL_ZOOM and NOT_CAMERA hold; the scroll scales over a held room.
  - GNaB-U0055 and GNaB-U0061: NOT_CAMERA is too strong; now CAMERA_VS_SLIDE_UNRESOLVED.
- **New correction, 35 rows.** `reconcile_v3.py` wrote `final_camera_attribution` NOT_CAMERA for M3 OBJECT_MOVE, although N17 declared that label not validated (4/6 held-out). These rows now read CAMERA_NOT_ESTABLISHED. They were not re-inspected. The audit v3 table was already right: its "camera not established" counts 137, 124 and 112 include OBJECT_MOVE.

**Limits.**
- One same-vendor reader who knew the M3 and ledger values; first and last frames, plus the frame after the interval.
- One first visual reading (mNLN-U0231) was corrected after measuring.
- A camera label here means a uniform whole-frame change in flat art, not proof of how the original was edited.
- Plain-background rows can carry M3 CAMERA_FRAMEWIDE without a static reference. That population was not counted. M3 was not retuned, so the used held-out sample stays spent.
- Not adjudicated, and not required: 44 LEDGER_CAMERA_M3_OTHER rows and the unnamed frame-wide rows. They remain "camera not established" or as declared in audit v3.

## R20 dependency closure
Manifest `portability/TRANSFER_MANIFEST_v3.json`, sums `portability/TRANSFER_SHA256SUMS_v3.txt`, script `scripts/stage_and_verify_v3.sh`, results `portability/R20_VERIFY_N19.json` and `portability/RERENDER_CLOSURE_N19.json`. v2 is kept.

- **Calibration extracts:** the 4 extracts are now package items, so the package has 21 items and 260,841,354 bytes. They are byte-verified as files. Regeneration from source was not tested and is not needed.
- **Font:** `/Library/Fonts/Bradley Hand Bold.ttf` is not a missing dependency. RT-V2-S02 falls back to `Noteworthy.ttc` when it is absent, and that is how the published render was made.
- **Correction, RT-V2-S02:** `WORKER_NOTES.md` and `EVALUATION.json` name Bradley Hand. The rendered font is Noteworthy. Those files stay unchanged. A render with Bradley Hand differs (mean per-pixel difference 0.47). The test stays FAIL as published.
- **Re-render:** all 13 `render.py` files ran from scratch copies on Machine A, and 13/13 `rt.mp4` came out byte-identical. RT-V3-S01 needed its absolute output path changed in the copy.
- **Procedure test:** the script refuses a same-device destination (exit 2). With `--same-device-test`, 21/21 hashes passed and 4 restores decoded. This is not a backup.
- **Not tested:** a second Mac. Byte-identical re-rendering needs the listed fonts and runtime versions.

**Transfer: BLOCKED.** No approved off-device destination was provided. Git holds text only and is not a backup of source media or renders.

## Next
1. **Owner:** name an off-device destination. Then run `scripts/stage_and_verify_v3.sh <DEST>` and confirm the copy reads from the second Mac. That is the remaining required non-audio work.
2. **Owner:** audio R08, R09 and R21 need actual listening.

Re-verify from `final_audit/`: `/usr/bin/python3 be_final_validate_v3.py OUT.json`.
