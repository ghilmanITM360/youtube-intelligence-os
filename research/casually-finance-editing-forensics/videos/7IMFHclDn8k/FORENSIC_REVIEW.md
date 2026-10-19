# Forensic review — 7IMFHclDn8k "Everyone's Future Is Riding on an AI Boom That Hasn't Showing Up"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Everyones-Future-Is-SnapYT.App.mp4` (`CFSRC-015`), SHA256 `a30e8af4...fb35b`, H.264/AAC, 360x640, 24.0 fps, 1562 frames (decoded = ffprobe), 65.131 s. SHORT uploaded 2026-09-27, 33,419 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (75 % voiced, 17 pauses >=0.25 s, 8 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1561.

## Measured statistics
- 18 scenes (median 3.00 s, p10 1.65, p90 6.48, longest 8.38); 17 hard cuts (15.66/min); 51 events (46.98/min), 31 of them one-frame.
- Operations: HARD_CUT_REPLACE 17, POP_IN 11, CAMERA_SCROLL_ZOOM 6, CAPTION_CHUNK_CHANGE 6, OVERLAY_POP 4, HIGHLIGHT_SWEEP 3, CHARACTER_RISE_IN 2, ROTATION 1, POSE_SWAP 1.
- Frame-weighted: static hold 59.7 %, plausibly conventional keyframe/compositing 40.3 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -125 ms (p10 -235, p90 -5; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = 24 fps).

## Findings
- **Evidence mix.** Five source screenshots (Davos article, GDP bar chart, Yahoo Finance quote card, Federal Reserve text page, BEA table), one of them recoloured: the argument leans on quoted and tabulated data, with the stick-figure cast as commentary (`DIRECTLY_OBSERVED`).
- **Camera on screenshots.** 6 scroll/zoom events (26-91 frames) pan or zoom the article, chart, quote and table; red box and highlights are added on top (S13-S14).
- **Recolour step.** The GDP chart's Q1/Q2 2026 bars turn green in one frame (f312) to flag the two quarters under discussion.
- **AI props.** A grey robot with red eyes rises beside the quote (f428+), a chip pops on top (f493), and a server rack with money bags pops (f772-862): objects stand in for the 'AI investment' abstraction.
- **Clock.** A wall clock beside the US-map character represents 'patience' (S10); hand rotation not tracked.
- **Growth arrow.** A green zig-zag arrow and three popping bags illustrate 'conditions as good as they have ever been'.
- **Two-possibility close.** 'Which leaves two possibilities' -> official figure with bubble ('Don't worry everyone!') -> GDP chart panning to '+1.8%' and a worried host rising from below: the second possibility ('1.8 isn't the floor, it's the ceiling') is delivered with the number as the final image (`DIRECTLY_OBSERVED`).
- **No screen recording or generated motion identified.**

## Uncertainties
Coarse authoring (18 scenes; S06, S09, S13 bundle concurrent layers); caption timing not measured; clock rotation and several slides untracked; creator tools unknown; no listening; single reviewer.
