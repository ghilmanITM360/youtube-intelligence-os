# RT_L1 attempt 1 - evaluation (against frozen ACCEPTANCE_RT_v1, sha c0ee184e)
Render: attempt_1/render.mp4 (sha256 in evidence/render_sha256.txt), editable source ../make_rt.py at attempt-1 time (copied as make_rt_attempt1.py), intended_timeline.csv 23 events.
Measured (RT_EVALUATION.json): 8/10 PASS. C7 FAIL: holds containing yellow 0.955 (range 0.24-0.62) - the yellow-shelled mascot is in almost every hold. C8 FAIL: stroke median 16.0 px on NATIVE_001499 (range 10-14).
Observed (primary opened SHEET_01..04 once each):
- V1 PASS: original snail-like round mascot (yellow spiral shell, yellow scarf, dot eyes, bulb nose, mitt hands); not a caveman; thick black outline, flat fills, no gradient/shadow.
- V2 PASS: single-frame swaps throughout; only multi-frame transition is the dip-to-white G0020 (f560-575).
- V3 PARTIAL->FAIL: word-by-word title build present (G0004/G0006/G0008) with reserved space, but the line is wider than the frame: "WH" is clipped at the left edge and "IST?" at the right edge (SHEET_01 slots 4-9).
- V4 PASS: red X over the hammer week (G0018, SHEET_02 slot 6).
- V5 PASS: final "5 MORE MINUTES" snooze joke held to the last frame; no end card.
- V6 FAIL: the clipped title text (same defect as V3).
Literal-picture beats present (clock = coins G0024; bed = rest G0014).
RESULT attempt 1: FAIL (C7, C8, V3, V6). Audio sync: BLOCKED (silent).
Fix request to the worker (defects only): keep the title inside 90% safe width; add mascot-free beats (objects/text alone) so yellow is in about half of holds; thin the outline to about 12 px.
