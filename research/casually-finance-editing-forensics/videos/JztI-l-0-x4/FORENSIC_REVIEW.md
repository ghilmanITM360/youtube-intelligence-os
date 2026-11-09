# Forensic review — JztI-l-0-x4 "Nobody Can Agree Why America Stepped In to Save Japan."

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Nobody Can Agree Why America Stepped In to Save Japan.  .mp4` (`CFSRC-025`), SHA256 `5c2ead9d...d06dc`, H.264/AAC, 360x640, 30.0 fps, 2423 frames (decoded = ffprobe), 80.832 s. SHORT uploaded 2026-08-30, 15,125 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (banded layout with a headline to f818 only; scenes cut-delimited; every HARD/ANIMATION auto stage event seen on lean pre/active/post sheets at 360p; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words measured against ASR). Audio: whole track measured (76 % voiced, 16 pauses >=0.25 s, 10 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2422.

## Measured statistics
- 21 scenes (median 3.00 s, p10 1.80, p90 7.20, longest 9.93); 20 hard cuts (14.85/min); 56 events (41.57/min), 39 of them one-frame.
- Operations: HARD_CUT_REPLACE 20, UNRESOLVED_CHANGE 10, POP_IN 6, OVERLAY_POP 4, HIGHLIGHT_SWEEP 4, CAMERA_SCROLL_ZOOM 3, POSE_SWAP 2, STROKE_REVEAL 2, CHARACTER_LOOP_ANIMATION 1, PROP_DRIFT 1, ROTATION 1, VIDEO_CLIP_INSERT 1, LAYER_SLIDE_BEHIND 1.
- Frame-weighted: static hold 74.9 %, plausibly conventional keyframe/compositing 20.7 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 4.4 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -116 ms (p10 -257, p90 -47; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (0 isolated duplicates, 0 with a 5-frame gap).

## Findings
- **Headline for 27 s, then none.** The headline 'nobody can agree why america paid to save japan' sits in the header band from the first frame and is removed at the cut f819 (27.3 s); one-line captions continue to the end. It is a close paraphrase of the public title ('Nobody Can Agree Why America Stepped In to Save Japan.') and matches no other local title (`DIRECTLY_OBSERVED`).
- **Captions track the words.** 252 caption changes matched to ASR word onsets: median +27 ms, p10 -72, p90 +166 ms, 73.0 % within ±100 ms (`MEASURED`; ASR uncertainty ~100 ms).
- **Cutting.** 20 hard cuts in 80.8 s (14.9/min), 21 scenes (median 3.0 s, shortest 1.2 s, longest 9.9 s); 58 table rows (43/min); 74.9 % of frames are static holds, 20.7 % conventional keyframe motion and 4.4 % indeterminate (a meme clip and a periodic pose animation). Hard cuts sit a median 117 ms before the nearest ASR word onset (n = 20, range -313 to +260 ms; 12 lead by more than 100 ms, 7 within ±100 ms, 1 lags) (`MEASURED`).
- **Measured camera moves on the profile page.** The CSIS profile page enlarges 1.72x with a (-64,+11) px shift over ~61 frames (f1259-1319), linear on scale and both pans (`SUPPORTED`, margin 0.038-0.052), then zooms back out to about 0.58x over 17 frames (linear `AMBIGUOUS`); a green highlight grows from 0 to 280 px over ~42 frames (f1401-1442) and a second green highlight from 204 to 495 px over ~28 frames (f1489-1516); a yellow highlight on the article grows from 0 to 274 px over f1557-1650 (`MEASURED`).
- **A 10-fps meme clip, the third time.** The cartoon-sponge meme image appears at f1755 (58.5 s, 0.14 s before ASR 'president') and its region updates on f1758, 1761, 1764, ... 1791 (every third frame) and then on f1797, 1800, 1801, 1803 and 1804, the same cadence as the shop clips in `bF9WVzzS4ds` and `gGNVpOo7BK8` (`MEASURED`; clip identity not verified).
- **Speech bubbles land on the word.** The 'Stability!' bubble pops at f1845 (61.50 s), 40 ms before ASR 'stability' (61.54 s); the 'This is sus af' bubble pops at f1969 (65.63 s) at the start of 'there's more to this story' (ASR 'there's' 65.42 s); the colour change of the arrow from green-up to red-down is complete at f900 (30.0 s), 0.26 s after ASR 'falling' (29.74 s) (`MEASURED`).
- **Red marks.** A red squiggle connects the 'Weird request' and 'Buying lots of yen' notes over ~54 frames (f1093-1146); the red circle on the yield peak draws over ~12 frames (f2365-2376), disappears at f2385 and reappears at f2399-2400, before and during ASR '19-year high' (79.48 s) (`MEASURED` for the circle; the squiggle area is below the colour threshold and its progress is read from the sheet).
- **Persona clips and a periodic animation.** The caricature at the lectern changes pose every 14 frames (f157, 171, 185, 199, 213) and a Japan-map character tints dark red at f923 and f935; whether these are pose swaps or short loops is `UNKNOWN` (`MEASURED` periodicity, sources of the meme and photo inserts `UNKNOWN`).
- **Repeated devices.** The 'US BONDS FOR SALE' stall appears in S19 as in `bF9WVzzS4ds` and `gGNVpOo7BK8`; the Japan-map character sinks behind it over ~22 frames (f2230-2252) (`DIRECTLY_OBSERVED`).
- **Shared closing sentence.** A 15-word ASR run ('which becomes a supply problem in a market that is at a 19-year high') is identical to the closing words of `zkeA5cH9nyM`, and both end on a yield chart with a red circle on the latest peak that blinks off and on; no other run of 8 or more identical words with any analysed video (`MEASURED` with difflib on ASR words, ASR uncertified).
- **Cadence not testable.** No isolated duplicate frames in continuous motion, so a 24-to-30 fps conform cannot be tested (`MEASURED`).
- **360p limits.** 12 sub-0.8 %-area changes stay as unresolved rows, mostly bubble and caption text (`MEASURED` counts; identity not reviewed).
