# Held-out protocol v3 (pre-registered 2026-11-04T16:59:08Z, BEFORE ingest of held-out-3; tests manual v0.4)
Videos: FYoHYq8VRt0 (2026-05), TFhrRrRdUbA (2026-06), 4ZVtHknKuvg (2026-08) — selection/selection_v3_heldout3.json. Never used for any rule; no file under videos/<id> existed when this was written.
Ranges = all 15 long measured so far (10 dev + 2 held-out-1 + 3 held-out-2; these informed v0.4), tolerance 15 % of range each side:
- Q1 events/min 17.7–30.7 → PASS 15.75–32.65
- Q2 hard cuts/min 3.33–7.62 → 2.69–8.26
- Q3 median hold 1.29–2.44 s → 1.12–2.61
- Q4 activity frame share: within dev long range ±15 % (computed by script)
- Q5 1920x1080, 24/1 fps CFR
- Q6 integrated loudness −16.1…−16.8 ±0.5 → −17.3…−15.6 LUFS (v0.4 acknowledges outliers; a miss counts as FAIL, not excused)
- Q7 last segment HOLD 235–240 f (≈10 s end card)
Qualitative (v0.4), only if a reviewer pass runs: R1 off-white default; R2 red accent + red title/end card; R3 featureless stick figures, detailed objects; R4' question card + attribution (typed/scaled/present at f0); R4'' red title card at 6–31 s; R6 hard cuts advance steps; R7 majority 1-frame activities; R10 deadpan asides; v0.4 device: continuous drawn growth allowed.
If usage forbids the reviewer pass, the qualitative part is recorded NOT_EVALUATED (not PASS).
