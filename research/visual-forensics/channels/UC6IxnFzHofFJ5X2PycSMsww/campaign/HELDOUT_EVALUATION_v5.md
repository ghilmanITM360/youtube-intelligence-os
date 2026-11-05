# Held-out evaluation v5 — INTERIM (2026-11-05T16:49:15Z) — against pre-registered HELDOUT_PROTOCOL_v5.md (manual v0.6)
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
