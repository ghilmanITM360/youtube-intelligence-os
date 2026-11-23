# Validation (executed 2026-11-20; audio excluded by owner)
Renderer: `tools/render_original.py` (PIL + ffmpeg, h264, 1920x1080, 24 fps). Output: `~/YIOS-local-audits/CF-reproduction-tests-20261120/testC.mp4` (14.0 s, 336 frames, local only). Contact sheet: `REPRODUCTION_TESTS/testC_contact_sheet.png`. All art original (teal square-head figure with beanie, coin, bars); no source frame or asset used.

Test A, style frame (frame 240): background (247,249,246) vs reference median (255,255,255); non-background area 14.4% vs reference median 13.2% (p10-p90 4.7-37.6%); text contrast 15.6:1; margins 55-89 px at 640 px width. PASS on these measures. Not measured: typography match, line weight, human review.

Test B, animation: measured by re-running the same frame-diff method on the render. Cuts, pop-ins, text swap and pose swap: 1 frame each. Push-in: scale 1.00 to 1.20 in about 15 frames, ease-out (matches the 1.0-1.2 zoom seen in yViMyIVOHkQ E159). Slide/line: 14 frames. PASS as a self-consistency check only: it proves the renderer follows the measured rules, not that it equals the original.

Test C, independent concept ("why coffee costs more", not from any reference): 5 scenes, shots 3.0/3.2/2.8/3.5/1.5 s (reference median 2.88 s, mean 3.46 s). Entering classes chosen from the decision-rule table (props POP_IN, scene starts CUT, poses swap). Frame review by the auditor: scenes read clearly, but the art is plain. Shot lengths were chosen to match reference stats, not predicted by the engine.

Not done: human review by the owner, a second concept, audio, a vertical (Short) test, comparison against held-out reference videos by someone other than the author. Tests passed: A, B (objective, limited), C (objective, limited). Tests failed: 0. Blocked: audio.
