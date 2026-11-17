# RT_P1 attempt 6 - evaluation (ACCEPTANCE_RT_v1, sha c0ee184e, criteria unchanged)
Only change from attempt 5 (make_rt_attempt_6.py diff): minute hand 0.6r -> 0.48r; asleep scene mascot x 395 -> 385, clock (870, r130) -> (905, r110). Timeline, grammar and everything else identical. Attempt 5 FAIL retained.
Measured 10/10 PASS (RT_EVALUATION.json): 1080x1920 50 fps 1000 frames, bg #FBFBFB, hold 1.25 s, single-frame 0.9231, 39 events/min, ink 0.0814, yellow 0.7143, stroke 18 px, matched 0.9286, 0 unexplained.
Observed (primary opened attempt_6 frames/sheets_v2 SHEET_01..04 once each: non-occluding layout, 100% of each tile visible; plus native crops f300, f370, f560, f849, f999):
- V1 PASS: egg mascot with yellow scarf; no beard, spotted tunic or headdress; thick outline; flat fills, no gradient/shadow.
- V2 PASS: single-frame swaps; only multi-frame transition is dip G0014 (f437-453).
- V3 PASS: WHY / ALARM / CLOCKS? on white with reserved slots (G0002, G0004, G0006).
- V4 PASS: red X over clock (G0012-13).
- V5 PASS: 5 MORE MINUTES joke held to f999; no CTA or end card.
- V6 PASS: attempt 5 defects resolved at native scale: hand tip clears "12" and "9" (f300, f370, f560); mascot hand has a visible gap from clock ear and ring ticks (f849, f999). Edge ink (4 px) 0 on all 14 hold end frames; ink bbox x 31-1070, y 135-1815. Text readable at sheet scale. Tightest remaining spot: TOO EARLY! close above mascot head without touching (G0022-23).
RESULT attempt 6: PASS of ACCEPTANCE_RT_v1 for visual grammar and rhythm: bounded animatic conformance only, first pass after 5 retained failures (attempts 1-5), guided by evaluator feedback.
NOT established: source-level drawing quality, first-pass reproducibility from the spec, full-video production approval. Narration sync BLOCKED (silent render, listening unavailable).
