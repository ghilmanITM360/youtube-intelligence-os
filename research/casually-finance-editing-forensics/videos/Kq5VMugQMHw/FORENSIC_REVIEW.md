# Forensic review — Kq5VMugQMHw "They Spent $73.6 Billion to Save Their Currency... It Failed."

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`They Spent $73.6 Billion to Save Their Currency... It Failed..mp4` (`CFSRC-042`), SHA256 `6b550609...a0d3f`, H.264/AAC, 720x1280, 30.0 fps, 1905 frames (decoded = ffprobe), 63.586 s. SHORT uploaded 2026-08-25, 14,368 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (75 % voiced, 20 pauses >=0.25 s, 8 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1904.

## Measured statistics
- 19 scenes (median 2.50 s, p10 1.31, p90 6.09, longest 11.17); 18 hard cuts (16.98/min); 68 events (64.17/min), 48 of them one-frame.
- Operations: HARD_CUT_REPLACE 18, POP_IN 17, UNRESOLVED_CHANGE 12, PROP_DRIFT 9, OVERLAY_POP 4, SLIDE_IN 3, CHARACTER_RISE_IN 1, CHARACTER_LOOP_ANIMATION 1, SCALE_TWEEN 1, ROTATION 1, OPACITY_FADE 1.
- Frame-weighted: static hold 61.6 %, plausibly conventional keyframe/compositing 28.7 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 9.7 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -104 ms (p10 -242, p90 119; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (2 isolated duplicates, 0 with a 5-frame gap).

## Findings
- **Full-bleed, no headline, no caption band.** White background from the first frame; captions are typed on the stage as props, so caption timing is `NOT_MEASURED`. The file is 30 fps with only two isolated duplicate frames in motion, so no 24-to-30 fps conform can be tested (`MEASURED`).
- **Cutting.** 18 hard cuts in 63.6 s (17.0/min), 19 scenes (median 2.5 s, shortest 0.8 s, longest 11.2 s); 66 table rows (62/min), 17 of which are one-frame pop-ins; 61.6 % of frames are static holds, 28.7 % conventional keyframe motion and 9.7 % indeterminate (two turning/looping character scenes). Hard cuts sit a median 104 ms before the nearest ASR word onset (n = 18, range -307 to +193 ms; 9 lead by more than 100 ms, 7 within ±100 ms, 2 lag; ASR uncertainty ~100 ms) (`MEASURED`).
- **Numbers and rates pop at the spoken number.** Red '$74B' pops at f216 (7.20 s), 20 ms before ASR '74' (7.22 s); the 'Fed Funds Target 3.50 - 3.75%' bubble pops at f688 (22.93 s), 10 ms before ASR '3.5' (22.94 s); three calendar icons pop at f460, f475 and f486 (15.33, 15.83, 16.20 s) on 'about', 'three' and 'weeks' (ASR 15.64, 15.86, 16.16 s) (`MEASURED` from red-pixel counts: +658, +638, +673 px).
- **Five bond papers pile up one by one.** Papers appear at f882, f888, f893, f899 and f905 (intervals 6, 5, 6 and 6 frames) under 'Flood the market with American bonds nobody asked for' (ASR 'flood' to 'bonds' 29.2-30.2 s), and the percent coin moves away from the dollar sign in three steps (f813-826, f852-864, f951-973) (`DIRECTLY_OBSERVED`; coin paths not tracked).
- **A red double arrow and a turning ring.** The red double arrow appears at f1183-1187 (245 red px) and lengthens to 345 px by f1235 (~2 px per frame); a ring of three red arrows (1928 red px from f1548) changes over ~115 frames while 'FX intervention feedback loop' is typed inside and a text page fades in behind it; the next scene is a red glowing card 'THE DOOM LOOP' (f1663-1688) whose red area falls from 7295 to 0 px over f1669-1688 (`MEASURED`; ring rotation versus a looped clip `UNKNOWN`).
- **Dark red 'monster' beat as a loop.** In S05 (f503-547, the frame held at mean gray 23.5) the lower right changes on every frame by ~700-1200 px for ~43 frames while 'Then reality set in' is on screen (`MEASURED`; looping character animation not resolved).
- **Slow drift as the only motion in a long scene.** In the final scene the note and 'PROBLEMS' text drift down by about 0.05 of the frame height over ~146 frames (changed-region bbox y 0.45-0.61 at f1765 to 0.50-0.66 at f1900) (`MEASURED` from the changed-region bbox).
- **A cut after a named word.** 'THE DOOM LOOP' appears at f1663 (55.43 s), 0.29 s before ASR 'doom' (55.72 s); the host and ouroboros scene cuts in at f1688 (56.27 s) at ASR 'It's' (56.22 s) (`MEASURED`).
- **Shared sentence with `f_ZCoPKLpyU`.** A 16-word ASR run ('Japan's benchmark rate now sits around 1% while America's sits between 3.5 and 3.75') is identical to the rate sentence of `f_ZCoPKLpyU`, and both show a US-map character beside the Fed building with a Fed funds bubble; the chart sequences differ (`MEASURED` with difflib on ASR words, ASR uncertified).
- **Source and prop layer.** Japan Times article, a Japan benchmark-rate chart page, a macrosynergy text page, a blue shield, calendar icons, a 'US BONDS FOR SALE' stall, an ouroboros image and a red 'PROBLEMS' title carry the points (`DIRECTLY_OBSERVED`).
- **Rate chart geometry not reported.** The camera tracker returns a near-zero net shift (0.0 px) on the benchmark-rate chart (f560-612) because the line reveals as the page moves; ease-out cubic (x) and ease-in quad (y) fits are `SUPPORTED` but not interpretable as a camera move.
