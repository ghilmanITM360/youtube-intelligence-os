# Barely Evolved — continuation handoff after final audit (2026-11-04)

- **Owner and writer:** Claude session 1e8761b1 on Machine A. The BE lock is released at the end of this audit.
- **Branch:** research/barely-evolved-visual-forensics. The audit base is 7b3c3e7b, and the publication SHAs are recorded in `evidence/F1_PUBLICATION_RECEIPT.json` (channel_synthesis) and in each video's `evidence/F1_PUBLICATION_RECEIPT.json`.
- **Per-video sources:**
  - uPQcyookL0Y: 1416669f…
  - mNLNb-Z4T0M: e6799e8f…
  - GNaBxt_zIRA: cbe7a3af…
  - The MP4s are local-only, in `~/Downloads/videos in mp3/BarelyEvolved-MP4/`.
- **Status:** VISUAL_ANALYSIS_PARTIAL for all three videos; CT_SCAN_COMPLETE is false.
- **Next work:** see "Remaining for full completion contract" in `FINAL_THREE_VIDEO_AUDIT.md`. Listening comes first and needs a capable listener.
- **Tools:**
  - `be_final_validate.py` (validation);
  - `evaluate_rt_v2v3.py` (reconstruction evaluation);
  - `build_kit_outputs.py` (derived kit files);
  - `scripts/` (frame-grab and measurement helpers; they use `~/YIOS-local-audits/tooling/visual-ct-scan-venv`);
  - campaign tools `be_*` in `~/YIOS-local-audits/barely-evolved/`.
- **Do not:**
  - start another channel or video from this handoff;
  - re-score RT-V2-01 without pre-registering a new threshold.
