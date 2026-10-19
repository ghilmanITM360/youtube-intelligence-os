# Forensic review — RB5zVghPor8 "78% of The Government's Money Goes to Just 5 Things"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`78-of-The-SnapYT.App.mp4` (`CFSRC-002`), SHA256 `251cc2c7...34e4b`, H.264/AAC, 360x640, 24.0 fps, 1689 frames (decoded = ffprobe), 70.421 s. SHORT uploaded 2026-10-01, 35,881 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (74 % voiced, 21 pauses >=0.25 s, 16 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1688.

## Measured statistics
- 20 scenes (median 2.29 s, p10 1.41, p90 5.32, longest 12.42); 19 hard cuts (16.19/min); 57 events (48.57/min), 38 of them one-frame.
- Operations: HARD_CUT_REPLACE 19, POP_IN 9, CAPTION_CHUNK_CHANGE 9, SCALE_TWEEN 4, SLIDE_IN 4, CAMERA_SCROLL_ZOOM 3, HIGHLIGHT_SWEEP 3, OVERLAY_POP 2, SHAPE_MORPH 2, MORPH_REARRANGE 1, ROTATION 1.
- Frame-weighted: static hold 71.8 %, plausibly conventional keyframe/compositing 24.9 %, screen recording 0.0 %, complex continuous animation 3.3 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -95 ms (p10 -131, p90 -47; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: irregular duplicates; cadence unresolved.

## Findings
- **Rotation measured.** The kitchen knife (S03) holds at 82.5 deg until f354, swings down to 22.3 deg by f362 (about -60 deg in 7 frames; step size falls from ~10 to ~2 deg/frame), then swings back to 70.3 deg by f370 (+48 deg in 8 frames; step size rises to 7-8 deg/frame). Two opposite-direction ease curves in one 16-frame gesture, not one named easing (`MEASURED`, principal-axis tracker, `orient_339_371.json`).
- **Door swings.** A brown door opens in two places (f1011-1039 with cash and a green arrow; f1446-1471 revealing the tiny map character): drawn as skewed shapes that change every frame; rig or frame-by-frame cannot be separated (`DIRECTLY_OBSERVED`; classed `MORE_COMPLEX_CONTINUOUS_ANIMATION`).
- **Chart choreography.** The bar chart is zoomed, five bars recoloured in steps, then the bars are re-stacked into a single block that carries the '78%' headline (`MORPH_REARRANGE`, f231-247), i.e. data shapes are turned into an object.
- **Quote bubbles.** Official figure plus a large bubble holding scrolling quote text with yellow highlight sweeps (S08, S13): the document is spoken by the character; scroll/highlight run 56-64 frames each.
- **Slide-ins.** Four slide-ins from the left edge (map character f285, chart strip f413, host f1483, bill document f1588) last 7-21 frames each.
- **Third-party imagery.** A meme photograph scales in with a '???' bubble (f1271-1287); rights status unverified.
- **Pops and scale tweens.** 9 pops (money bags, documents, figures), 4 scale tweens (receipt unrolling, map-character growth, meme, knife entrance); red 'not' and green 'growth' pop as coloured words.
- **Receipt.** The opening BILL receipt unrolls over ~81 frames while the caption starts on top of it.
- **No generated or screen-recorded motion identified.**

## Uncertainties
Coarse authoring (20 scenes, several with concurrent layers); caption timing not measured; exact frames of some sub-pops approximate; creator tools unknown; no listening; single reviewer.
