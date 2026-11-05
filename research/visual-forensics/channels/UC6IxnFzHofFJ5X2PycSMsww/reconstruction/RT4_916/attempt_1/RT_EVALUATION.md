# RT4_916 attempt 1 — portrait 9:16 Short, scored against frozen ACCEPTANCE_CRITERIA_RT4_916.md (sha a27f4b41…, frozen 2026-11-05T19:09:06Z, before render)
Render: attempt_1/RT4_animatic.mp4 sha256 8e63c969d843b74c658a2701fa092e462212946609ac6b8c575ab5407b023026 (local-only, not published). Worker: fresh sonnet subagent, spec-only (self-reported read list; not transcript-audited). Silent. Measured with the source pipeline (xk_measure, xk_scenedetect, xk_segment, xk_rt_eval); raw RT_EVALUATION.json, tables/.
| Check | Result |
|---|---|
| M1 format | PASS h264 yuv420p 1080x1920, 24/1, 1440 frames, 60.0 s |
| M2 events/min 17.9–28.2 | PASS 26.0 (26 activities) |
| M3 median hold 1.44–2.84 s | PASS 2.00 s |
| M4 intended events ±2 f ≥80 %, 0 unexplained | PASS 25/26 (96 %), 0 unexplained onsets |
| M5 no title/end card | PASS: first segment HOLD 30 f (blank board under SUN CLOCK banner), last segment HOLD 116 f; no full-frame card in sampled frames |
| V1 vertical composition, anchor ≥90 % | PASS on sample: stacked upper + lower panels; SUN CLOCK banner visible in 8/8 sampled frames |
| V2 no edge clipping, safe zone | PASS on sample, with note: the pebble is cut by the left edge in the f720 frame only because it is mid blurred slide-in (intended slide at f700) |
| V3 original identity | PASS on sample: pebble with dot eyes, teal banner/accents, no red/stick figure/dinosaur/'what if'; objects (tree, sun, arc) more detailed than narrator |
| V4 no collisions | PASS on sample; worker fixed a star-over-'GOOD NIGHT' collision and I saw none in f1439 |
Visual evidence: attempt_1/frames/primary_sheet_8.png (frames 5, 200, 430, 700, 720, 1000, 1200, 1439; read by orchestrator, 0.33 scale). Only 8 of 1440 frames were viewed.
Weaknesses seen: the lower panel is empty in about half of the sampled frames (canvas under-used); the one miss in M4 not investigated.
Verdict: RT4_916_PASS_PORTRAIT (attempt 1 of max 3; no failed attempts). Scope: portrait silent rhythm/format/composition only. Not tested: narration sync, audio, story quality, full-frame visual review. Does not upgrade RT3 (landscape) or vice versa.
