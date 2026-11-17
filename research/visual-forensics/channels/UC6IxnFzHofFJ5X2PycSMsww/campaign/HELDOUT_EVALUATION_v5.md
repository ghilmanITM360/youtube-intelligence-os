# Held-out evaluation v5 — FINAL (2026-11-05T17:00:03Z) — against pre-registered HELDOUT_PROTOCOL_v5.md (manual v0.6)
Protocol sha256 c24b3249… written before ingest. Measurement only so far (heldout5_quant.csv); Q2 + qualitative pending reviewers.

| Video | predicted | measured class | events/min | median hold | activity share | result |
|---|---|---|---|---|---|---|
| Z_xJ40QXu7Q billion-story building | JOURNEY | JOURNEY (events/min < 18 only) | 16.8 | 2.42 s | 0.037 | CORRECT by rule |
| IdlQsjq5vKo rifle jetpack | JOURNEY | STEPWISE | 22.5 | 1.96 s | 0.110 | WRONG |
| p2M8Y0z9Rl0 everyone jumped | STEPWISE | STEPWISE | 22.8 | 1.96 s | 0.035 | CORRECT |
Score 2/3 = "weak support" under the pre-registered threshold. **Honest reading: weaker than that.** Z_xJ is classed JOURNEY only by the events/min arm; its activity share (0.037) is far from the oTzW signature (0.291, long continuous moves). It is slow (long holds), not continuous-motion. The only video with the oTzW mechanism remains oTzW itself (n=1). IdlQ shows a raised share (0.110, 3× typical) without crossing the threshold.
Q1–Q7 (protocol-v4 ranges): 18/18 measured rows PASS (Q1, Q3, Q4, Q5, Q6, Q7 × 3); Q2 pending.
Conclusion so far: v0.6 "story structure determines rhythm" is NOT supported as a predictive rule from titles; keep it as a descriptive note (continuous-journey videos CAN fall outside the event-density range), not a production rule.

## Update 2026-11-05T16:53:04Z — reviewer on Z_xJ40QXu7Q (all 15 sheets opened, primary SHEET_04 spot-check 5 rows, 0 disagreements)
OBSERVED: Z_xJ is NOT a continuous journey. Separate static comparison scenes, Q2 = 5.86 SHOT_CUT/min (PASS), plus one recurring height diagram ('GOAL: 1,000,000,000' / FLOORS) re-scaled by 5 short blurred zoom-outs (≈0.3–0.7 s each, e.g. G0032 15 f, axis 10m→1 km). Title card 20.5–22.4 s (R4'' PASS). Its low events/min comes from long holds, not long moves.
→ Its JOURNEY "hit" was right by the threshold, wrong in substance. **Substantive score 1/3.** Verdict: v0.6 story-structure rule NOT SUPPORTED as a prediction; continuous-journey rhythm stays a single observed case (oTzW-mTQd5w). New device for the manual: short blurred scale-reveal zoom-out (0.3–0.7 s) on a persistent measurement axis.
IdlQsjq5vKo / p2M8Y0z9Rl0 reviewers not run (usage); their Q2 + qualitative = NOT_EVALUATED.

## Final 2026-11-05T17:00:03Z — all 3 reviewed (IdlQ 24/24 sheets, p2M8 17/17; primary spot-checks SHEET_14 8 rows, SHEET_06 11 rows, 0 disagreements)
Quantitative (protocol-v4 ranges): **21/21 PASS** incl. Q2 = Z_xJ 5.86, IdlQ 5.18, p2M8 7.25 cuts/min.
IdlQ (predicted JOURNEY): OBSERVED ~22 separate static scenes joined by hard cuts; flight shown as separate scenes and pose swaps; only camera move = brief scroll-up G0182 (0.35 s); longest in-frame motions ≈2 s (G0132 rifle slides out, G0142 rig rises). Its raised activity share (0.110) comes from these in-frame object moves + write-on graphs, not camera journeys. → prediction WRONG in substance too. Final substantive score 1/3 (only p2M8 STEPWISE).

| Qualitative | Z_xJ | IdlQ | p2M8 |
|---|---|---|---|
| R1 off-white default | PASS (black space scenes after 183 s) | PASS | PASS (dark globe G0168–73) |
| R2 red marks + red title/end card | PASS (red circles G0040/G0102) | PASS (red underlines on quote) | PASS (red dashed 0.5 m line, red arrows) |
| R3 stick figures, detailed objects | PASS | PASS (rifle, drum mag) | PASS (seismograph, map) |
| R4' question card + attribution | PASS | PASS — **scaled up from a speck** at G0002 ('Rob B') | PASS present at f0, persists ~20 s |
| R4'' red title card 6–31 s | PASS 20.5 s | PASS 7.9 s | PASS 20.6 s |
| R6 hard cuts advance | PASS (23) | PASS (24) | PASS (28) |
| R7 majority 1-frame | PASS | PASS 0.83 | PASS 0.88 |
| R8 label after object | — | PASS (brace then '~20g') | PASS ('JOULES' after landing) |
| R10 deadpan asides | PASS (collapse gags) | PASS | PASS ('THE REAL STORY' panel) |
Verdict: held-out-5 visual grammar and all quantitative rules PASS (21/21, 27/27). The v0.6 story-type predictive rule FAILS (1/3); v0.7 already demotes it. Across 6 held-out videos today the only out-of-range rhythm is oTzW-mTQd5w.
