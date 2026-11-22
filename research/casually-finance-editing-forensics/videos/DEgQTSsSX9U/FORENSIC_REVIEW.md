# Forensic review — DEgQTSsSX9U "For 50 Years We Had A Buyer Who Never Asked the Price... Not Anymore."

Status: `VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`For-50-Years-SnapYT.App.mp4` (`CFSRC-017`), SHA256 `ffe27019...1c726`, H.264/AAC, 360x640, 30.0 fps, 1917 frames (decoded = ffprobe), 63.936 s. SHORT uploaded 2026-09-15, 25,311 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_A (banded layout: every auto stage event reviewed on pre/active/post contact sheets; caption word timing measured against ASR). Audio: whole track measured (77 % voiced, 16 pauses >=0.25 s, 12 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1916.

## Measured statistics
- 26 scenes (median 1.87 s, p10 1.08, p90 4.75, longest 7.03); 25 hard cuts (23.46/min); 75 events (70.38/min), 56 of them one-frame.
- Operations: HARD_CUT_REPLACE 25, POP_IN 21, OVERLAY_POP 9, POSE_SWAP 5, SCALE_TWEEN 3, SLIDE_IN 3, STROKE_REVEAL 2, CAMERA_SCROLL_ZOOM 2, SHAPE_MORPH 1, TEXT_WRITE_ON 1, PROP_DRIFT 1, CHARACTER_LOOP_ANIMATION 1, OPACITY_FADE 1.
- Frame-weighted: static hold 80.3 %, plausibly conventional keyframe/compositing 15.6 %, screen recording 0.0 %, complex continuous animation 0.6 %, change of undetermined method 3.4 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -13 ms (p10 -96, p90 139; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 32 of 54 duplicates share one phase mod 5; 5-frame gaps 38).

## Findings
- **Layout (banded era).** Same system as `Qof71Ef-3EU` (Sep 8): a two-line burned-in headline ("How Pensions Secretly Saved the Bond Market") at y 0.206-0.284 for the whole video (zero change), a bounded stage and a small one-line caption band that appends words at ASR onset (median +27 ms, 78 % within +-100 ms, n = 215). The headline is not the public title (`DIRECTLY_OBSERVED`).
- **Native cadence.** 30 fps delivery of a 24 fps timeline: 38 five-frame duplicate gaps and 32 of 54 isolated duplicates on one phase (`MEASURED`), as in `Qof71Ef-3EU`.
- **Bond tear.** A BOND tag is torn in half over ~11 frames by a white wedge opening from the right (`SHAPE_MORPH`; drawn frames vs mask unknown).
- **Timeline build.** The 'interest payments' timeline is built bill by bill: red line, four one-frame bill pops (f259, f284, f307, f331), bag at maturity (f347) and a curved-arrow label (f361); later the line and bag stretch 'decades out' (f521-568).
- **Opacity fade measured.** The black '?' circle fades from black to white over f1881-1902: mean gray 66.9 -> 253 in near-equal steps (~10.7 per output frame), **linear** (`MEASURED`).
- **Shrinking props.** The pension check scales down to an icon twice (f412-432, f1186-1213) to show an unchanging obligation.
- **Pun asset reuse.** The MUNDER DIFFLIN sign (also in `Qof71Ef-3EU`, S04) returns for 'it isn't your money': a repeated parody asset across videos (`DIRECTLY_OBSERVED`).
- **Photos.** A Fed-chair photo, a market-crash photo, a sky photo with a falling tiny figure and a pension-card photo carry authority and risk beats.
- **No screen recording or generated motion identified.** The arguing-figures loop (f1235-1300) is `INDETERMINATE`.

## Uncertainties
Pose-swap versus rig for the arguing figures; progress of several slides/draws not tracked; creator tools unknown; no listening; single reviewer.
