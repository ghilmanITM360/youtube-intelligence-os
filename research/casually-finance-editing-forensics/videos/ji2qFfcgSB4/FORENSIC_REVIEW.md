# Forensic review — ji2qFfcgSB4 "Everything We Know About Debt Is Changing"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Everything-We-Know-SnapYT.App.mp4` (`CFSRC-016`), SHA256 `9eabd5fc...096b1`, H.264/AAC, 360x640, 30.0 fps, 2377 frames (decoded = ffprobe), 79.296 s. SHORT uploaded 2026-09-06, 65,485 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (banded layout; scenes cut-delimited; every HARD/ANIMATION auto stage event seen on lean pre/active/post sheets; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words measured against ASR). Audio: whole track measured (79 % voiced, 15 pauses >=0.25 s, 13 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2376.

## Measured statistics
- 14 scenes (median 5.62 s, p10 2.43, p90 9.48, longest 11.10); 13 hard cuts (9.84/min); 56 events (42.37/min), 50 of them one-frame.
- Operations: POP_IN 26, HARD_CUT_REPLACE 13, OVERLAY_POP 8, UNRESOLVED_CHANGE 3, HIGHLIGHT_SWEEP 3, CAMERA_SCROLL_ZOOM 1, OPACITY_FADE 1, POSE_SWAP 1.
- Frame-weighted: static hold 86.4 %, plausibly conventional keyframe/compositing 13.4 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.2 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -53 ms (p10 -137, p90 39; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (6 isolated duplicates, 5 with a 5-frame gap); pattern is consistent with a 24 fps timeline repeated to 30 fps but the sample is small.

## Findings
- **Banded era (fifth example).** Persistent headline 'The World's Safest Market Is Breaking' (zero change), stage 0.30-0.665, caption band aligned to ASR (median +27 ms, 79.5 % within ±100 ms, n = 224). The headline is the public title of a long-form in the same corpus (`0ll9rEtoRrs`, uploaded 2026-09-01, five days before this Short), not of this Short (`DIRECTLY_OBSERVED` from the headline text and the inventory titles; whether the Short is a cut-down of that long-form is `UNKNOWN`). The same pattern holds for `NgryCruZegs` (headline = public title of `Qof71Ef-3EU`); the other banded headlines checked (3) match no title among the 48 local videos. Denominator: 5 banded videos analysed.
- **13 hard cuts in 79.3 s (9.8/min)**, the slowest cutting of the banded sample so far (UJEqqBpH18k 10.6/min, NgryCruZegs 19, DEgQTSsSX9U 23, Qof71Ef-3EU 29): cuts are long evidence holds (spreadsheet table, text pages, PIMCO table), pace is carried by 26 single-frame pop-ins and the captions.
- **Cuts lead the word.** Hard cuts sit a median 53 ms before the nearest ASR word onset (n = 13, ASR uncertainty ~100 ms), consistent with the sample median of about -76 ms.
- **Only one camera move, measured.** The Netherlands flag slides off the left edge while the table is pushed in to 2.07x over 31 frames (f271-301). Fit: ease-out quad (decelerating), SUPPORTED, margin 0.05, all three channels agree (`camera_270_302.json`). A second decelerating push-in in the sample; most other measured moves are linear.
- **Stepwise highlight.** The yellow bar on the `S09` text page grows left to right in six steps over 74 frames (f1249-1323) with a linear overall rate (SUPPORTED); `S04` and `S11` highlights are ambiguous or aggregate-only (see `MOTION_EVENTS.csv`).
- **Numbers pop ahead of the word.** '2 TRILLION!' (f391, red) is on screen before the caption reaches 'trillion' (f410); '500B' (f2306) pops as the sentence 'more than €500 billion' completes. Bills accumulate in equal steps (f2267, f2274, f2281, f2287; counts not resolved).
- **Recycled characters.** Large US-map character, UK-map character (with teacup), a green map-shaped character (read as the Netherlands, reviewer's label) and a stick-figure host recur from the other banded Shorts; props (bags, bills, tags, notes) are rebuilt for the scenes.
- **Cadence.** Only 6 isolated duplicate frames in motion, 5 of them 5 frames apart: consistent with the 24 fps timeline repeated to 30 fps but too small a sample to claim (QA text corrected).
- **No screen recording or generated motion identified.**
