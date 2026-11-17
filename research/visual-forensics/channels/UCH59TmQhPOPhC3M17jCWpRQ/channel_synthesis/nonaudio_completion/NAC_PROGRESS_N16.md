# Non-audio remaining work — progress checkpoint N16 (2026-11-05)

- **Session:** 1e8761b1.
- **Lock:** `.be_writer_lock`.
- **Base:** remote 0c1eeaad (N15).
- **Scope:** this is a progress checkpoint, not a completion claim. The five-hour meter read 96% at 16:40Z.

## Done

**R05/R07 gap: 11 camera-UNCERTAIN claims.**
- All 11 are resolved, with 0 left uncertain:
  - 9 VERIFIED, 8 of them by chained ORB similarity and 1 (uPQc-U0066) by a native overlay;
  - 2 REJECTED.
- Evidence: `r13_blind/CAMERA_*_CHECK*.csv` and `DENSE_REVIEW_LEDGER_<vid>_v2.csv` (column `camera_claim_resolution_v2`).

**R05 gap: unlabelled slow camera moves.**
- A measured camera component now covers all 850 intervals (`dense/CAMERA_CHAIN_ALL_<vid>.csv`). It adds `camera_measured_v2` to ledger v2; ledger v1 is unchanged.
- This found 173 frame-wide verified camera moves that the ledger did not name.
- Validation: 9 random overlays were checked; 8 were consistent with the measurement and 1 (mNLN-U0027) was unclear.
- In NO_FRAMEWIDE_SUPPORT and UNRESOLVED intervals, camera is not established. That is a declared measurement floor.

**R13 blind review batch 1.**
- 69 intervals were named blind, then reconciled (`r13_blind/BLIND_RECONCILIATION*.csv`):
  - 37 agree, of which 31 are exact or MIXED-compatible and 6 are cuts that fall on the state boundary;
  - 5 taxonomy splits;
  - 2 where the ledger was upheld on native frames;
  - 23 where the blind label was adopted (21 LOW tile-only rows plus 1 random row), and 1 where both were partially right;
  - 2 settled as MIXED by camera measurement.
- In the random 30, the ledger stood in 28 cases and was corrected in 2.

**R13 blind review batch 2** (30 STATIC_HOLD labels that the measurement contradicts).
- Status: RUNNING when this checkpoint was cut. Its brief and index are frozen in `r13_blind/batch2/`.

**R20 transfer contract.**
- `portability/TRANSFER_MANIFEST_v2.json` lists 17 items (249,052,569 B): 3 MP4s, 13 renders (including the RT-01 render) and the requirements lock.
- It also records the dependencies:
  - system fonts with their sha256;
  - Python 3, OpenCV 5.0.0, NumPy 2.5.4, Pillow 13.0.0 and FFmpeg 9.0.1;
  - one hard-coded path.
- `scripts/stage_and_verify.sh` refuses a destination on the source device. In a same-device procedure test it passed all 17 sha256 checks and the 4 restore decodes. That test copy was deleted, and **it is not durable backup**.

## Next

1. Reconcile batch 2 (apply `blind_reconcile.py` rules R2–R4 to `batch2/BLIND_REVIEW_B2.csv`).
2. Write matrix v3, gates and the report.
3. Seal and publish, then release the lock.
