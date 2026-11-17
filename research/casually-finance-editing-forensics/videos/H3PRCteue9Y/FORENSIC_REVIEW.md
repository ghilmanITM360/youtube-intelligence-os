# Forensic review — H3PRCteue9Y "Your Dollar's Emergency Fund Is (Mostly) Not Spent on Emergencies"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Your Dollar's Emergency Fund Is (Mostly) Not Spent on Emergencies.mp4` (`CFSRC-054`), SHA256 `3132dfa8...2fd62`, H.264/AAC, 720x1280, 30.0 fps, 1885 frames (decoded = ffprobe), 62.936 s. SHORT uploaded 2026-08-24, 10,392 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (75 % voiced, 11 pauses >=0.25 s, 8 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1884.

## Measured statistics
- 16 scenes (median 3.17 s, p10 1.70, p90 6.42, longest 13.00); 15 hard cuts (14.3/min); 57 events (54.34/min), 42 of them one-frame.
- Operations: HARD_CUT_REPLACE 15, OVERLAY_POP 10, UNRESOLVED_CHANGE 8, SLIDE_IN 7, POP_IN 5, CAPTION_CHUNK_CHANGE 3, CHARACTER_RISE_IN 3, HIGHLIGHT_SWEEP 2, OPACITY_FADE 1, CAMERA_SCROLL_ZOOM 1, SCALE_TWEEN 1, TEXT_WRITE_ON 1.
- Frame-weighted: static hold 75.6 %, plausibly conventional keyframe/compositing 23.3 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 1.1 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -27 ms (p10 -173, p90 40; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (0 isolated duplicates, 0 with a 5-frame gap).

## Findings
- **Full-bleed, no headline, no caption band.** White background from the first frame; hand-lettered captions are scene props and caption timing is `NOT_MEASURED`. The file is 30 fps with no isolated duplicate frames in motion, so no 24-to-30 fps conform can be tested (`MEASURED`).
- **Cutting.** 15 hard cuts in 62.9 s (14.3/min), 16 scenes (median 3.2 s, shortest 1.4 s, longest 13.0 s); 57 table rows (54/min); 75.9 % of frames are static holds, 23.1 % conventional keyframe motion and 1.1 % indeterminate. Hard cuts sit a median 27 ms before the nearest ASR word onset (n = 15, range -207 to +220 ms; 5 lead by more than 100 ms, 9 within ±100 ms, 1 lags; ASR uncertainty ~100 ms), the tightest cut-to-word timing of the 2026-10-20 batch (`MEASURED`).
- **Red marks land at or just before the spoken word.** The red 'David Kennedy' label pops at f78 (2.60 s), 40 ms before ASR 'David' (2.64 s); the red X over the dictionary definition pops at f870 (29.00 s) at ASR 'defined' (28.96 s); red 'may NOT be reviewed' is written in over f1783-1787 (59.43-59.57 s) and completes 50 ms before ASR 'may' (59.62 s); the red 'that cost $131,000' pops at f1287 (42.90 s), 0.16 s before ASR 'that' (43.06 s); the red arrow on the fund page pops at f315 (10.50 s), 0.18 s after ASR 'Exchange' (10.32 s) (`MEASURED` from red-pixel counts; ASR uncertainty ~100 ms).
- **Measured slow moves on source pages.** The Exchange Stabilization Fund page enlarges 1.55x with a (+86,+110) px shift over ~30 frames, linear on scale and both pans (`SUPPORTED`, margin 0.035-0.045); the statute page slides in with a (-123,+43) px shift over ~29 frames (pans ease-in-out `SUPPORTED`, margin 0.031-0.034); the Simon document slides in over 13 frames with a +101 px shift (ease-in-out `SUPPORTED`, margin 0.030-0.039) (`MEASURED`).
- **Yellow highlights and a pot.** Yellow highlights grow on the document (0 to 97 px over f139-164; 111 to 185 px over f1239-1259; 235 to 408 px over f1276-1315) and on the statute (0 to 67 px and 139 to 227 px); the pot of cash slides in over 15 frames (f255-269), rises from the bottom over ~15 frames (f592-606) and pops in one frame at f931 (`MEASURED`).
- **Bubbles carry asides.** Bubbles ('I don't need y'all!', 'Mr. President, could you sign this?', 'To stabilize, sure XDDDD', 'And what if I used some for Clash Royale?', 'Are you bloody JOKING?!?') and small captions ('his glasses were thick AF', 'it had better been a GREAT Persian carpet!') are not in the ASR (`DIRECTLY_OBSERVED`, text read at 720p).
- **Pop-in sequence of props.** Pot (f931), official (f970) and bubble (f1005) pop at 39- and 35-frame intervals; the piggy bank pops at f1631 (54.37 s), 0.39 s before ASR 'piggy' (54.76 s) (`MEASURED`).
- **No script reuse found.** No run of 8 or more identical ASR words with any other analysed video.
