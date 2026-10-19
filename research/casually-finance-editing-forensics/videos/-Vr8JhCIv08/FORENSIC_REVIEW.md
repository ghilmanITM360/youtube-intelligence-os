# Forensic review — -Vr8JhCIv08 "America's Self-Reinforcing Debt Loop."

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Americas-Self-Reinforcing-Debt-SnapYT.App.mp4` (`CFSRC-011`), SHA256 `a8f81df8...1405a`, H.264/AAC, 360x640, 24.0 fps, 1491 frames (decoded = ffprobe), 62.187 s. SHORT uploaded 2026-09-19, 23,226 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_C (cut-delimited scenes authored from a 1 s full-duration overview; detected changes not individually classified are kept as UNRESOLVED_CHANGE rows; event sheets not viewed). Audio: whole track measured (77 % voiced, 13 pauses >=0.25 s, 12 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1490.

## Measured statistics
- 18 scenes (median 3.50 s, p10 1.16, p90 5.85, longest 7.96); 17 hard cuts (16.4/min); 58 events (55.96/min), 39 of them one-frame.
- Operations: UNRESOLVED_CHANGE 41, HARD_CUT_REPLACE 17.
- Frame-weighted: static hold 78.3 %, plausibly conventional keyframe/compositing 0.0 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 21.7 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -55 ms (p10 -210, p90 110; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = 24 fps).

## Findings
- **Cut-delimited structure only.** 18 scenes and 18 hard cuts were authored from a 1 s overview; 41 detected changes (22 % of frames) are UNRESOLVED_CHANGE rows, so this video contributes scene timing, asset families and narration alignment, not motion-method evidence (depth C).
- **Reused footage with `6S3PzAUFnXQ`.** The national-debt-clock banner ('$40,086,889,777,472 / $117,446 for every single person in America') opens this video and also appears in the earlier-corpus Short `6S3PzAUFnXQ` (`REFERENCE_SUPPORTED` via its state description); a pixel comparison was not run.
- **Escalating typography.** The red '$40T' grows from a caption-sized pop to a frame-filling figure behind a man and DEBT papers; 'Back then / And now' is a split with a red divider between two map characters.
- **Props for negation.** Roads, schools and research props are crossed out with red X marks to show what interest 'buys' (`DIRECTLY_OBSERVED`).
- **Closing on data.** The last scene is the FRED interest/GDP chart with a red circle on the 2025 value and the host pointing.
- **No screen recording or generated motion identified.**

## Uncertainties (DEPTH_C)
41 changes unresolved; scene boundaries from the overview; caption timing not measured; creator tools unknown; no listening; single reviewer.
