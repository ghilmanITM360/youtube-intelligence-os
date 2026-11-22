# Forensic review — ffIiiPLDFdM "It Was Supposed To Get Easier to Buy a House..."

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`It-Was-Supposed-SnapYT.App.mp4` (`CFSRC-020`), SHA256 `f5039514...aae8c`, H.264/AAC, 360x640, 24.0 fps, 1449 frames (decoded = ffprobe), 60.437 s. SHORT uploaded 2026-10-16, 51,528 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (77 % voiced, 12 pauses >=0.25 s, 5 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1448.

## Measured statistics
- 13 scenes (median 3.58 s, p10 1.65, p90 8.34, longest 14.33); 12 hard cuts (11.91/min); 52 events (51.62/min), 28 of them one-frame.
- Operations: HARD_CUT_REPLACE 12, POP_IN 11, CAMERA_SCROLL_ZOOM 10, OVERLAY_POP 6, CAPTION_CHUNK_CHANGE 5, STROKE_REVEAL 3, PROP_DRIFT 3, SCALE_TWEEN 1, POSE_SWAP 1.
- Frame-weighted: static hold 57.7 %, plausibly conventional keyframe/compositing 42.3 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -68 ms (p10 -165, p90 62; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = 24 fps).

## Findings
- **Evidence anchor reused.** One document (FHFA Working Paper 24-03) is the background of four separated scenes (S08, S10, S11, S12) at different zoom/pan states, interleaved with prop/character scenes that illustrate each finding; the viewer returns to the same page as findings accumulate (`DIRECTLY_OBSERVED`).
- **Continuous screenshot motion is the dominant motion type.** 10 camera scroll/zoom events on screenshots/charts last 18-86 frames each, often with yellow/orange highlight sweeps and a host or prop popping in meanwhile; concurrent layers are not separated at 1-frame level (depth B).
- **Stroke draws.** Green rising lines, a green arrow, red falling strokes and a short red slash are drawn progressively (3 events, 4-28 frames); progress not tracked numerically here (see `7bm7XYssqlU` for a measured linear draw).
- **Scale-in of a seal.** The FHFA seal enters from the bottom-right with a scale tween over ~13 frames; logos for Fannie Mae and Freddie Mac then pop in single frames (`DIRECTLY_OBSERVED`).
- **Documents travelling.** MORTGAGE document props drift toward and away from a bank over ~15 frames each to dramatise 'handing cheap debt back' (`DIRECTLY_OBSERVED`; path and easing not tracked).
- **Red emphasis.** 7%, $6.6 trillion, 18.1%, 3%, 5.7% and "today's prices" appear as large red hand-lettered pops over black captions; every figure is a number from the narration (`DIRECTLY_OBSERVED`).
- **Tooltip.** A small tooltip appears on the rate chart in one frame at f199 (`LOW` confidence on mechanism).
- **No generated or complex character animation identified.**

## Uncertainties
Authoring is coarse: 13 scenes bundle several sub-compositions (S05, S07, S08, S12); caption word timing not measured; path and easing of document and prop drifts not tracked; creator tools unknown; no listening; single reviewer.
