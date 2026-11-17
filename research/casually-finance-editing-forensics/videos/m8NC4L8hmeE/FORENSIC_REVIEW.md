# Forensic review — m8NC4L8hmeE "The World's Greatest Investor vs The Leader of America's Money"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`The-Worlds-Greatest-SnapYT.App.mp4` (`CFSRC-040`), SHA256 `7a9e53ba...bab15`, H.264/AAC, 360x640, 24.0 fps, 1502 frames (decoded = ffprobe), 62.635 s. SHORT uploaded 2026-09-23, 11,442 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (81 % voiced, 11 pauses >=0.25 s, 6 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1501.

## Measured statistics
- 18 scenes (median 3.25 s, p10 1.44, p90 5.33, longest 7.88); 17 hard cuts (16.28/min); 73 events (69.93/min), 52 of them one-frame.
- Operations: UNRESOLVED_CHANGE 34, HARD_CUT_REPLACE 17, SLIDE_IN 4, OVERLAY_POP 4, HIGHLIGHT_SWEEP 3, CAPTION_CHUNK_CHANGE 2, CAMERA_SCROLL_ZOOM 2, TEXT_WRITE_ON 1, SCALE_TWEEN 1, CHARACTER_RISE_IN 1, VIDEO_CLIP_INSERT 1, OPACITY_FADE 1, POP_IN 1, POINTER_TRANSLATE 1.
- Frame-weighted: static hold 64.0 %, plausibly conventional keyframe/compositing 31.6 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 4.4 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -118 ms (p10 -211, p90 -25; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: irregular duplicates; cadence unresolved.

## Findings
- **Full-bleed with typed and red captions, no band.** No headline; captions are typed on the stage (some in red: 'And Bessent didn't take it well' typed over f108-141, red area 85 to 631 px). The file is native 23.976 fps (inventory 24.0): 12 isolated duplicate frames in motion, irregular, so no 24-to-30 conform applies (`MEASURED`).
- **Cutting.** 17 hard cuts in 62.6 s (16.3/min), 18 scenes (median 3.3 s, shortest 1.0 s, longest 7.9 s); 73 table rows (70/min), of which 34 are unresolved sub-0.8 %-area changes (mostly caption and bubble words); 64.0 % of frames are static holds, 31.6 % conventional keyframe motion and 4.4 % indeterminate (the clip insert). Hard cuts sit a median 118 ms before the nearest ASR word onset (n = 17, range -243 to +32 ms; 9 lead by more than 100 ms, 8 within ±100 ms, none lag; ASR uncertainty ~100 ms) (`MEASURED`).
- **Highlights are timed to the quoted sentence.** A yellow highlight grows over the CNBC quote from f864 (36.03 s, 30 ms before ASR 'Stan's' at 36.06 s) to f1034 (43.1 s, the end of the quote at 43.06 s), reaching 3136 px, while the quote text pans left by about 185 px over f896-1004 (x pan linear `SUPPORTED`, margin 0.053; scale ease-in-out `SUPPORTED`, margin 0.048); later highlights grow over f1173-1244 (0 to 770 px) and f1315-1398 (150 to 714 px) during 'one man saying that the market price is information' and 'the price is an opinion and policy doesn't take orders from opinions' (`MEASURED`).
- **A 10-fps clip on a 24 fps timeline.** The dog clip under 'NICKNAME ALERT' updates on f1045, 1047, 1050, 1052, 1054, 1057, 1059, 1062, 1064, 1066, 1069, 1071, 1074, 1076, 1078, 1081, 1083 and 1085 (alternating 2- and 3-frame gaps, about 10 updates per second) and then holds static to the cut f1138; the heading flips between thin red and bold dark-red lettering about every 12 frames. The card appears 0.17 s before ASR 'Besant' (43.62 s) in 'Besant called him by his nickname' (`MEASURED`; clip identity `UNKNOWN`).
- **Word-level pops.** Red 'wrong' appears at f736 (30.69 s), 50 ms before ASR 'wrong' (30.74 s); the 'Who tf are you lol' bubble appears at f591 (24.65 s) at ASR 'Treasury' (24.58 s); the 'I thought you better than this' bubble appears at f714 (29.77 s), 0.3 s after 'explaining' (29.46 s) (`MEASURED`).
- **Bubbles and captions add commentary the narration does not speak.** Bubble and caption texts such as 'wtf man', 'no bro code', 'Who tf are you lol', 'I thought you better than this', 'XDDD' and 'I do what I want boo' are not in the ASR (`DIRECTLY_OBSERVED`, text read at 360p).
- **Source inserts.** A phone with a LinkedIn post, a news-headline card, a Druckenmiller photo with a LinkedIn profile card, a Yahoo Finance text box, a WSJ page, a G20 poster with a 'Greetings from Asheville' postcard, CNBC quotes and an article page serve as the evidence layer (`DIRECTLY_OBSERVED`); the slide-ins take ~9-17 frames each.
- **Final beat.** A document marked 'SUPER DUPER PLAN! CLASSIFIED' is searched by a magnifying glass moving in over ~31 frames (f1459-1489, path not measured) while the narration asks 'then what exactly is the plan?' (`DIRECTLY_OBSERVED`).
- **No script reuse found.** No run of 8 or more identical ASR words with any other analysed video.
- **360p limits.** Thin lines and small caption changes sit near the detector floor; 34 unresolved rows keep them without identifying each.
