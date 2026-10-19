# Forensic review — NgryCruZegs "Nobody Is Talking About the World's Safest Market Breaking"

Status: `VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Nobody-Is-Talking-SnapYT.App.mp4` (`CFSRC-026`), SHA256 `02f598d4...a6c0a`, H.264/AAC, 360x640, 30.0 fps, 2013 frames (decoded = ffprobe), 67.157 s. SHORT uploaded 2026-09-14, 11,041 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_A (banded layout: every auto stage event reviewed on pre/active/post contact sheets; caption word timing measured against ASR). Audio: whole track measured (76 % voiced, 15 pauses >=0.25 s, 7 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2012.

## Measured statistics
- 24 scenes (median 1.90 s, p10 0.86, p90 6.08, longest 7.90); 21 hard cuts (18.76/min); 55 events (49.14/min), 41 of them one-frame.
- Operations: HARD_CUT_REPLACE 21, UNRESOLVED_CHANGE 10, POP_IN 8, OVERLAY_POP 5, CAMERA_SCROLL_ZOOM 4, SCALE_TWEEN 3, CHARACTER_RISE_IN 2, SHAPE_MORPH 1, HIGHLIGHT_SWEEP 1.
- Frame-weighted: static hold 72.7 %, plausibly conventional keyframe/compositing 26.5 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.8 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -93 ms (p10 -167, p90 0; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 36 of 48 duplicates share one phase mod 5; 5-frame gaps 31).

## Findings
- **Third banded-era Short.** Same system as `Qof71Ef-3EU` and `DEgQTSsSX9U`: persistent two-line headline (here 'The Cheap Money Era Is Coming to an End', y 0.206-0.294, zero change), bounded stage, small caption band (caption words aligned to ASR: median +20 ms, 80 % within ±100 ms), 24 fps timeline conformed to 30 fps (36 of 48 duplicates share one phase, `MEASURED`).
- **Headline versus public title.** The burned-in headline equals the public title of `Qof71Ef-3EU` ('The Cheap Money Era Is Coming to an End'), while `Qof71Ef-3EU` itself shows 'The Great Refinancing Crisis Is Coming Due'. Possible title tests or later title edits; identity mapping (title+duration) is unaffected because the durations differ (`DIRECTLY_OBSERVED`, cause `UNKNOWN`).
- **Script and asset recycling without frame reuse.** About a third of this narration repeats `Qof71Ef-3EU` nearly verbatim ('a third of the developed world's fixed rate debt maturing by 2027... not a forecast... the supply of paper is exploding... none of what's happening is hidden'), and the same props recur (MUNDER DIFFLIN sign and paper boxes with a red X, the bond/certificate collage, the bill-by-bill maturity timeline with 'Principal returned at maturity', the country-map ensemble, the detective), **but no frame correlates >= 0.90 between the two videos** (maximum 0.84 at 45x80 resolution): the scenes are re-composed per video, not re-used as clips (`MEASURED`, `evidence/cross_video_reuse.json` and a targeted pair test). The kit is reused; the storyboard is rebuilt.
- **Satire opener.** 'BREAKING NEWS!!!' paper and a computer-man bubble ('REPTILIANS') ridicule click-driven media (f0-184), a distinct hook from the claim-first openers of other Shorts.
- **Bubble burst.** A blue bubble pops into droplets over a few frames at f312-333 as a literal 'bubble popping' (`DIRECTLY_OBSERVED`).
- **Pinboard close.** The last two scenes use a pinboard with red strings ('connect the dots') and a 'let me cook' bubble.
- **No screen-recorded or generated motion identified.**

## Uncertainties
Scene boundaries S06-S08 and S17-S19 are snapped to the nearest large change; three scenes begin without a large change (marked no_auto_cut); 20 detected changes unresolved; caption timing measured; creator tools unknown; no listening; single reviewer.
