# Deep-VF handoff v2 (written 2026-11-08T20:52:37Z)
- Start state: 20:32Z, lock FREE, 5h 52% / weekly 19%. Repo HEAD f4dc5d14 untouched. Nothing published. SHA256SUMS (v1) verified all OK.
- Lock: acquired as deepvf-v8 (token 55AC7C6F…), released at the end of this pass.
- Outputs (all new files):
  - DEEP_VF_ADDENDUM_v2.md (main);
  - FROZEN_RULES_v2.md + .sha256 (frozen 20:41:49Z);
  - heldout_v8_selection.json (seed 20261110);
  - heldout_v8/: RESULTS.md, measured.json, motion_labels.csv, M0_format_labels.json, colour_*.csv, 6 holds sheets and 2 non-default sheets, all viewed;
  - v2/: dev colour CSVs, exemplar sheets, motion_dev_longs.csv / motion_dev_shorts.csv, motion_toolcheck_v7.csv, title_card_durations.csv, frozen tool copies;
  - proof_v1/: timeline_v1.json (editable), proof_16x9.mp4, proof_9x16.mp4, keyframes, VERIFY.json, PROOF_RESULTS.md, attempt1/.
- New ingests: videos/zJNmUWZXj2M (b7dcbf8a…) and videos/alBQCm0QpJg (41e9cd3b…); segments_v1 only. Loudness was missing for alBQ (audio out of scope).
- Tools in ~/YIOS-local-audits/tooling/asset_library/xkcd/:
  - new: colour_classes.py, motion_classes.py, heldout_v8_eval.py, render_proof.py, verify_proof.py.
- Verdicts:
  - v7 19/23 unchanged.
  - v8 targeted 32/34 HOLDS: colour 17/18, motion 15/16. The journey arm is UNTESTED.
  - Proof: P1–P7 and the red/clip checks PASS on both layouts. P8 and P9 are PENDING_HUMAN; AV is PENDING.
- Not done:
  - human playback review;
  - HumanCraft scorecard;
  - prompt pack v2 (apply the card correction, the DARK_FIELD class and the colour conditions);
  - rules v3 (MAP_FILL, Short scroll budget);
  - journey or 2026 long (alkJ7xScBiw has no local source; owner decision).
  - No CT_SCAN_COMPLETE or AV sign-off is claimed.
- Next exact operation:
  1. The owner watches proof_v1/proof_16x9.mp4 and proof_9x16.mp4 and records P8/P9.
  2. Write FROZEN_RULES_v3 (Shorts colour/motion only, from dev and v7/v8 evidence).
  3. Seed-pick 2 fresh Shorts from the 20 unused, ingest them, and run heldout_v8_eval.py adapted to v3.
- End usage: {"five_hour": 0.67, "five_hour_reset": 1794177000, "seven_day": 0.2, "seven_day_reset": 1794747600, "overage": false, "read_utc": "2026-11-08T20:52:34.618621Z"}
