# Deep-VF handoff (written 2026-11-08T19:26:27Z)
- Start state: lock FREE at 19:06:35Z; 5h 34% / weekly 16%; repo HEAD f4dc5d14 untouched; remote research/xkcd-whatif-visual-forensics head 3c6145cc (checkpoint R). Nothing published this pass.
- Lock: acquired as deepvf-s (token E3C45DF5…), released at the end of this pass.
- Outputs (all local, new files only): DEEP_VF_ADDENDUM_v1.md (main), strata_map.csv, opening/ (44 frame-3 JPEGs, layout/reuse CSVs, variance_map, member_grid), motion_windows/ (15 windows), script_beats/ (segments, cue_summary, 3 beat sheets), FROZEN_RULES_v1.md + .sha256, heldout_v7_selection.json, heldout_v7/ (RESULTS.md, measured.json, 12 sheets), colour_mode_share.csv.
- New ingests: videos/U4cONnQxgvo and videos/X97DDWvxaqQ (ingest + loudness + segments_v1; no reviewed ledger). Their source SHAs match the census.
- Tools (~/YIOS-local-audits/tooling/asset_library/xkcd/):
  - new: opening_reuse.py, strata_map.py, script_beats.py, beat_sheet.py, heldout_v7_eval.py.
  - changed: motion_window.py (optional out-dir argument; falls back to ingest evidence and segments_v1 for unreviewed videos).
- Verdict: frozen v1 = 19/23 (82.6%) → DOES NOT HOLD. Failures are colour/red wording (3) and journey-format camera share (1).
- Not done: render (no authorization recorded); listening/sync/AV (BLOCKED); prompt pack v2 (corrections listed in addendum §7); visual check of hold-drift flags; no CT_SCAN_COMPLETE and no AV sign-off claimed.
- Next exact operation:
  1. Re-view colour and journey scenes in existing dev videos WH4g1ptJ-70, BO8rOs05v48, r7B0MzvwDcA, qu8nx1qUwEU, oTzW-mTQd5w and Z_xJ40QXu7Q (library state JPGs, no decode) and write FROZEN_RULES_v2 (colour/red + journey camera budget only).
  2. Seed-select a v8 set of 4 unseen Pop-6 longs + 2 fresh Shorts, ingest the Shorts, and run heldout_v7_eval.py adapted to v2.
- End usage: {"five_hour": 0.46, "five_hour_reset": 1794177000, "seven_day": 0.18, "seven_day_reset": 1794747600, "overage": false, "read_utc": "2026-11-08T19:26:24.568587Z"}
