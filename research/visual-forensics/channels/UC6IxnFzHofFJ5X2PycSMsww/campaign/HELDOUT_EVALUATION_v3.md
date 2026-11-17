# Held-out evaluation v3 (FINAL, 2026-11-04T20:37:06Z) — against frozen HELDOUT_PROTOCOL_v3.md (manual v0.4)
Order (file mtimes): protocol + selection written before any videos/<id> existed → ingest 17:02–17:08Z (2026-11-04) → measurement → reviewers rvH3 (FYoH 2026-11-04; TFhr, 4ZVt 2026-11-05) → primary spot-checks. No held-out output was used to write v0.4.
## Quantitative (MEASURED; campaign/heldout3_quant.csv)
| Rule | FYoHYq8VRt0 (2026-05) | TFhrRrRdUbA (2026-06) | 4ZVtHknKuvg (2026-08) |
|---|---|---|---|
| Q1 events/min (15.75–32.65) | PASS 25.3 | PASS 27.1 | PASS 29.1 |
| Q2 hard cuts/min (2.69–8.26) | PASS 4.86 | PASS 4.46 | PASS 4.57 |
| Q3 median hold (1.12–2.61 s) | PASS 1.85 | PASS 1.65 | PASS 1.17 (inside tolerance only; below raw range 1.29) |
| Q4 activity frame share | PASS 0.053 | PASS 0.107 | PASS 0.173 |
| Q5 1920x1080 24/1 | PASS | PASS | PASS |
| Q6 LUFS (−17.3…−15.6) | PASS −16.4 | PASS −16.7 | PASS −16.8 |
| Q7 last HOLD 235–240 f | PASS 239 f | PASS 239 f | PASS 239 f |
Totals: 21/21 PASS. Q2 = count of reviewer rows whose event_class contains SHOT_CUT (incl. combinations) / duration.
## Qualitative (OBSERVED; reviewer rvH3 all sheets + primary 0.6-scale spot-check of SHEET_01 each)
| Rule | FYoH | TFhr | 4ZVt |
|---|---|---|---|
| R1 white/off-white canvas default | PASS | PASS (dark starfield inside board = counterexample class) | PASS |
| R2 red accent + red title/end card | PASS | PASS (red ellipse, 'RIP', strike on SPACE; title G0022 11.8 s, end card G0158) | PASS (title G0010 8.29 s, end card G0178) — NOTE red/orange also used for fire/heat and pink magma (G0112–G0115, G0126, G0144) |
| R3 stick figures; detailed objects | PASS | PASS | PASS |
| R4' question card + attribution, any entry form | PASS (present f0) | PASS (scale-up f1–f7, '— Sean Gallagher') | PASS (present at hold f0–f47, '— Joanna Xu') |
| R4'' title card after cold-open premise | PASS 13.8 s | PASS 11.8 s | PASS 8.3 s |
| R6 steps advance mainly by hard cut | PASS ~14 | PASS 13 | PASS 14 |
| R7 majority 1-frame activities | PASS 0.89 | PASS (pop-on majority per reviewer) | PASS |
| R10 deadpan literal asides | PASS | PASS (paper 'NOT EVERYTHING IS ANTIMATTER' G0157) | PASS ('NOT AGAIN' G0008, 'WORSE? FOR WHO?' G0124, 'RIP ALL LIFE ON EARTH / THANKS JOANNA' G0120) |
Spot-check: FYoH 0 disagreements; TFhr 1 minor (G0010 pose detail, corrected via primary_corrections.csv); 4ZVt 0.
Unresolved reviewer segs: FYoH 2, TFhr 7, 4ZVt 12 (listed in each validation.json).
## Verdict
v0.4 held-out PASS on all 3 unseen long videos (21/21 quantitative, all evaluated qualitative rules). Caveats: (a) 4ZVt median hold 1.17 s is only inside the 15% tolerance — 2026 videos trend denser, so the v0.4 hold floor should be reviewed when more 2026 long videos are measured; (b) R2 should state that red/orange/pink also appear as content colour for fire/heat, not only as marks; (c) qualitative rules rely on one reviewer per video plus one primary sheet spot-check; audio not listened (ASR only) — no FULL_AV_SIGNOFF.
Process deviation recorded: 4ZVt reviewer wrote a helper script /private/tmp/claude-501/scratch/gen.py outside its review dir to emit the CSV (preserved; pipeline used only the review-dir files). Validator patched to accept the rv1→rvH3 symlink path (xk_validate_review.py).
