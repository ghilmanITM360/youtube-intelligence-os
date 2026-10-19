# Forensic review — 7bm7XYssqlU "Home Prices Are Crashing and Spiking?"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Home-Prices-Are-SnapYT.App.mp4` (`CFSRC-018`), SHA256 `97bb1151...a866f`, H.264/AAC, 360x640, 24.0 fps, 1311 frames (decoded = ffprobe), 54.677 s. SHORT uploaded 2026-10-18, 24,660 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (72 % voiced, 18 pauses >=0.25 s, 13 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1310.

## Measured statistics
- 17 scenes (median 2.83 s, p10 1.56, p90 4.80, longest 6.29); 16 hard cuts (17.56/min); 54 events (59.26/min), 36 of them one-frame.
- Operations: HARD_CUT_REPLACE 16, POP_IN 15, OVERLAY_POP 8, STROKE_REVEAL 4, CAMERA_SCROLL_ZOOM 4, CAPTION_CHUNK_CHANGE 3, CHARACTER_RISE_IN 2, POSE_SWAP 1, PROP_DRIFT 1.
- Frame-weighted: static hold 70.1 %, plausibly conventional keyframe/compositing 29.9 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -74 ms (p10 -144, p90 96; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = 24 fps).

## Findings
- **Layout.** Full-bleed, no fixed headline or caption band (unlike `Qof71Ef-3EU`). Hand-lettered marker captions append word by word at positions that change per scene; emphasis numbers/words are large and green, black or red (`DIRECTLY_OBSERVED`).
- **Stroke draws.** The opening red falling line is drawn over f0-f29 at a constant ~72 red px/frame (tip speed ~0.027 frame widths/frame; **linear**, RMSE 0.028 vs ease-out 0.193; `MEASURED`). The Hartford price chart line draws over ~100 frames (ink 1,170 -> 3,021, includes caption growth; `MEASURED`, coarse).
- **Screenshots.** Pew and Zillow articles and the Hartford photo scroll/zoom for 16-33 frames behind the host; headline cards are replaced one by one in single frames (4 swaps).
- **Pops.** 15 `POP_IN` and 8 `OVERLAY_POP` events: props (houses, buildings, clock, bubble) and emphasis numbers appear in one frame, usually on a caption keyword; building icons pop at 570, 587, 593, 602-604 to count "no massive building wave".
- **Characters.** The host rises or pops in from the right/bottom over 2-4 frames; a profile figure, a hooded man, a curly-haired man, a top-knot builder and the green US-map character each appear in one scene; heads change per scene (a small cast, not one rig, as far as the video shows).
- **Argument build.** Two-city comparison (Austin chart then Hartford chart) held by a shared two-chart frame (S13) before the dollar-sign and builder punchline; the final scene is a 20-frame hold on "the builder".
- **No generated or screen-recorded motion identified.**

## Uncertainties
S11 f830-880 mechanism (pan vs pointer motion); whether the white patch at f176 means price cuts; caption word timing not measured for this layout; small events below 0.8 % area (caption words, thin strokes) not individually reviewed; creator tools unknown; no listening; single reviewer.
