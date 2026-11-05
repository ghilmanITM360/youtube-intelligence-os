# RT_L1 attempt 2 - evaluation (ACCEPTANCE_RT_v1, sha c0ee184e)
Fixes for attempt 1 defects (title clipping, yellow share, stroke). Measured 9/10: C7 now 0.545 PASS, C8 12.0 px PASS; NEW FAIL C6 mean dark-ink 0.0684 < 0.071 (thinner lines and mascot-free beats reduced ink - a regression introduced by the fix).
Observed checks not re-judged on this attempt (measured FAIL already decides the attempt; sheets not opened to save reads).
RESULT attempt 2: FAIL (C6). Fix request: enlarge drawings/heavier solid black elements so held-state ink is ~8-9% without thickening the outline.
