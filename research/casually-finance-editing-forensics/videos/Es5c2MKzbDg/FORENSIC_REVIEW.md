# Forensic review — Es5c2MKzbDg "58% More Home Sellers Than Buyers... So Why Are We Still Paying More?"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`58-More-Home-SnapYT.App.mp4` (`CFSRC-001`), SHA256 `ebf2dadf...ae35d`, H.264/AAC, 360x640, 24.0 fps, 1498 frames (decoded = ffprobe), 62.464 s. SHORT uploaded 2026-10-15, 122,355 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (79 % voiced, 11 pauses >=0.25 s, 6 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1497.

## Measured statistics
- 22 scenes (median 1.73 s, p10 0.77, p90 6.76, longest 13.46); 19 hard cuts (18.25/min); 60 events (57.63/min), 37 of them one-frame.
- Operations: HARD_CUT_REPLACE 19, CAMERA_SCROLL_ZOOM 8, POP_IN 8, OVERLAY_POP 7, POSE_SWAP 4, SLIDE_IN 3, CAPTION_CHUNK_CHANGE 3, SCALE_TWEEN 3, HIGHLIGHT_SWEEP 2, CHARACTER_RISE_IN 1, STROKE_REVEAL 1, LAYER_SLIDE_BEHIND 1.
- Frame-weighted: static hold 73.6 %, plausibly conventional keyframe/compositing 26.4 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -125 ms (p10 -219, p90 -47; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = 24 fps).

## Findings
(authored findings missing)
