# Forensic review — Qof71Ef-3EU "The Cheap Money Era Is Coming to an End"

Status: `VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`The-Cheap-Money-SnapYT.App.mp4` (`CFSRC-037`), SHA256 `273fd644...e87e3`, H.264/AAC, 360x640, 30.0 fps, 2049 frames (decoded = ffprobe), 68.352 s. SHORT uploaded 2026-09-08, 375,765 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_A (banded layout: every auto stage event reviewed on pre/active/post contact sheets; caption word timing measured against ASR). Audio: whole track measured (77 % voiced, 18 pauses >=0.25 s, 10 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2048.

## Measured statistics
- 35 scenes (median 1.70 s, p10 0.37, p90 4.31, longest 5.67); 33 hard cuts (28.97/min); 63 events (55.3/min), 54 of them one-frame.
- Operations: HARD_CUT_REPLACE 32, POP_IN 14, OVERLAY_POP 4, SCREEN_RECORDING_INSERT 3, EXPRESSION_SWAP 2, CAMERA_PUSH_IN 2, HIGHLIGHT_SWEEP 2, HARD_CUT_THROUGH_BLANK_FRAME 1, POINTER_TRANSLATE 1, MASKED_REVEAL_WIPE 1, CHARACTER_LOOP_ANIMATION 1.
- Frame-weighted: static hold 83.0 %, plausibly conventional keyframe/compositing 11.4 %, screen recording 3.1 %, complex continuous animation 2.5 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -87 ms (p10 -146, p90 12; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 52 of 55 duplicates share one phase mod 5; 5-frame gaps 44).

## Findings
(authored findings missing)
