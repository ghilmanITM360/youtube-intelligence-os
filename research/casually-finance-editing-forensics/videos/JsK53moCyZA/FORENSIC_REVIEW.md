# Forensic review — JsK53moCyZA "The SpaceX IPO Nobody Can (Actually) Explain..."

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`The SpaceX IPO Nobody Can (Actually) Explain... - Casual Finance (720p, h264).mp4` (`CFSRC-033`), SHA256 `4e60a637...930be`, H.264/AAC, 720x1280, 30.0 fps, 1291 frames (decoded = ffprobe), 43.13 s. SHORT uploaded 2026-06-01, 212,691 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (75 % voiced, 9 pauses >=0.25 s, 6 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1290.

## Measured statistics
- 11 scenes (median 3.93 s, p10 1.57, p90 5.50, longest 7.43); 10 hard cuts (13.91/min); 56 events (77.9/min), 47 of them one-frame.
- Operations: UNRESOLVED_CHANGE 19, HARD_CUT_REPLACE 10, POP_IN 8, CAPTION_CHUNK_CHANGE 7, OVERLAY_POP 6, POSE_SWAP 4, CHARACTER_RISE_IN 1, SCALE_TWEEN 1.
- Frame-weighted: static hold 62.7 %, plausibly conventional keyframe/compositing 37.0 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.2 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -80 ms (p10 -160, p90 56; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 13 of 17 duplicates share one phase mod 5; 5-frame gaps 10).

## Findings
- **A small centred stage, no headline, no band.** Every change of the picture happens inside rows 0.366-0.722 of the frame (about 0.36 of its height); the top 37 % and bottom 28 % stay white from the first to the last frame, and a small typed caption sits at the bottom edge of the active band. This is the oldest upload of the six Shorts (2026-06-01) and its layout differs from the full-bleed Aug-Oct Shorts, so no era-wide claim is made from one video (`MEASURED`).
- **A 24 fps timeline conformed to 30 fps.** The 17 isolated duplicate frames in motion are 5 frames apart in 10 cases and 13 of 17 share one phase modulo 5; the '401K' growth (f913-980) repeats frames at f916, 921, 926, 931, 941, 946, 966, 971, 976 and 981 (all 1 modulo 5) while it moves, i.e. 4 new pictures per 5 frames (`MEASURED`; of the two 30 fps files analysed in this session this is the one with a conform, rSa2aziEsAI shows none).
- **Cutting.** 10 hard cuts in 43.1 s (13.9/min), 11 scenes (median 3.93 s, p10 1.57, p90 5.50, longest 7.43 s); 56 table rows (78/min), 47 of them one-frame and 19 unresolved sub-0.8 %-area changes (caption words, tiny texts); 62.7 % of frames are static holds and 37.0 % conventional keyframe motion (nearly all of it the wobbling character, the chart builds and the paper growth); the file has no frame with 20 % or more of the full frame changing, so cuts here are changes of 6-31 % of the active band (`MEASURED`).
- **Hard cuts sit close to the word.** Median 80 ms before the nearest ASR word onset (n = 10, range -160 to +133 ms; 3 lead by more than 100 ms, 6 within ±100 ms, 1 lags; ASR uncertainty ~100 ms) (`MEASURED`).
- **The caption clears before the picture at 6 of 10 cuts.** At f128/f129, f351/f352, f516/f517, f912/f913 and f1009/f1010 the caption block is cleared exactly one frame (33 ms) before the new picture (403-610 px at the earlier frame, 3507-6255 px at the cut), and at f870-871/f872 two frames before; at the other 4 cuts (f645, f692, f790, f1128) the frame before has 0 changed px (`MEASURED`; the same one-frame lead was measured in 6S3PzAUFnXQ).
- **A metronomic wobble.** The character beside the first chart swaps poses exactly every 10 frames at f139, 149, 159, ... 339, 349 (22 swaps of 583-595 px, 3 per second) for the whole of S02 (`MEASURED`).
- **Charts are built in steps on the beat.** The defense-contractor row pops 0.7 s before ASR 'defense' (9.7 s), red 'more than all COMBINED!' lands at ASR 'combined.' (10.82 s = f324), the Coca-Cola row 60 ms before ASR 'Coca' (13.16 s), later logo rows at f409-487 ending at ASR 'Starbucks' (15.5 s), and the 'Top 10 LSE Companies' bar replaces them at the next cut (`MEASURED`; ASR uncertainty ~100 ms).
- **Marks land at or before the key word.** The SpaceX logo pops 90 ms before ASR 'SpaceX,' (23.16 s), the red ellipse on the loss figure 0.16 s before ASR 'billion' (24.96 s), the pointing figure 70 ms before ASR 'you.' (29.84 s) (`MEASURED`).
- **Evidence and props.** Charts or a news card carry 6 of 11 scenes (S01-S04, S06, S07); the rest are characters, a 401K paper and Nasdaq logo props (`DIRECTLY_OBSERVED`). The bubble 'Give me SPACEX stocks pls', the tiny texts 'much' and 'ahh... you now nothing' and the angel and devil figures are not in the ASR (`DIRECTLY_OBSERVED`, text read at 720p).
- **No script reuse found.** The longest run of identical ASR words with any other analysed video is 3 (difflib on `asr_words.csv`).
