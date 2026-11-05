# RT_P1 attempt 4 - evaluation (ACCEPTANCE_RT_v1, sha c0ee184e)
Same render as attempt 3 (sha256 bee25c1d71d90418..., byte-identical). Only change: intended_timeline.csv drops the frame-0 "initial" row, because a first state is not a change and cannot have an onset. This is a timeline correction made by the evaluator after seeing the C9 failure, and attempt 3's result stays recorded as FAIL.
Measured 10/10 PASS: hold 1.25 s, single-frame 0.9231 (limit 0.923), 39 events/min, ink 0.0823, yellow 0.714, stroke 18 px, matched 13/14 = 0.929, 0 unexplained.
Observed (primary opened attempt_3 SHEET_01..04 once each; same render):
- V1 PASS: original egg-shaped mascot with yellow scarf; no caveman, beard, spots or headdress; thick outline, flat fills, no gradient/shadow.
- V2 PASS: single-frame swaps; only multi-frame transition is dip G0014.
- V3 PASS: WHY / ALARM / CLOCKS? word by word with reserved slots (G0002, G0004, G0006).
- V4 PASS: red X over the clock (G0012).
- V5 PASS: final 5 MORE MINUTES bubble held to the end; no end card.
- V6 FAIL: vertical recomposition works, but the sun ray crosses "COCK-A-DOODLE" (G0015) and "MONEY" sits against the right edge (G0019-G0023). Same standard as RT_L1 attempt 4.
RESULT attempt 4: FAIL (V6). Fix request: those two layout defects only.
