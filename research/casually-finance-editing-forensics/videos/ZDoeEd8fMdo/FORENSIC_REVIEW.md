# Forensic review — ZDoeEd8fMdo "There's A Clock on AI Nobody Can Control"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`There's A Clock on AI Nobody Can Control.mp4` (`CFSRC-041`), SHA256 `b87e9283...b38e4`, H.264/AAC, 720x1280, 30.0 fps, 2455 frames (decoded = ffprobe), 81.93 s. SHORT uploaded 2026-08-20, 45,559 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (banded layout with a lower header (header 0.24-0.37, stage 0.37-0.67); scenes cut-delimited; every HARD/ANIMATION auto stage event seen on lean pre/active/post sheets; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words measured against ASR). Audio: whole track measured (76 % voiced, 14 pauses >=0.25 s, 12 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2454.

## Measured statistics
- 20 scenes (median 3.60 s, p10 1.79, p90 6.37, longest 9.20); 19 hard cuts (13.91/min); 65 events (47.6/min), 50 of them one-frame.
- Operations: HARD_CUT_REPLACE 19, UNRESOLVED_CHANGE 15, POP_IN 12, HIGHLIGHT_SWEEP 5, OVERLAY_POP 5, STROKE_REVEAL 2, MORPH_REARRANGE 1, EXPRESSION_SWAP 1, CAPTION_CHUNK_CHANGE 1, PROP_DRIFT 1, CAMERA_SCROLL_ZOOM 1, TEXT_WRITE_ON 1, POINTER_TRANSLATE 1.
- Frame-weighted: static hold 71.8 %, plausibly conventional keyframe/compositing 26.6 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 1.6 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -93 ms (p10 -185, p90 34; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 40 of 62 duplicates share one phase mod 5; 5-frame gaps 52).

## Findings
- **Banded layout with a lower header (third layout variant).** Persistent headline "the clock on ai we can't control" sits at y 0.24-0.37 of the 720x1280 frame (the Sep banded Shorts put it at 0.20-0.30), stage 0.37-0.67, small caption line below it (band-aligned: median +33 ms against ASR onsets, 75.3 % within ±100 ms, n = 235). The headline differs from the public title ("There's A Clock on AI Nobody Can Control") by two words and matches no other local title (`DIRECTLY_OBSERVED`). The Short is about AI power demand rather than rates; it is one of this channel's Aug 2026 uploads in the local inventory.
- **No full-stage cut above 20 %, 19 hard cuts at the stage level.** 19 hard cuts in 81.9 s (13.9/min, median scene 3.6 s, longest 9.2 s), 65 events (47.6/min), 50 of them one-frame; stage-change peaks are small because most scenes are a small prop or page on white.
- **Cuts lead the word.** Hard cuts sit a median 93 ms before the nearest ASR word onset (n = 19, range -607 to +127 ms, ASR uncertainty ~100 ms), in line with the sample median of about -76 ms.
- **24 fps conform measured in an Aug 720p file.** 62 isolated duplicate frames in motion, 52 of them exactly 5 frames apart and 40 of 62 sharing one phase modulo 5 (`MEASURED`): the same 24-to-30 fps conform as `xrNPr3YrWdw` and `wo71JwXSYIs`, so it is not specific to the 360p Sep uploads.
- **Highlights measured by colour track the phrase being read.** Yellow sweeps f187-262 (2.5 s, over '$25 million', ASR 7.52-8.1 s), f724-760 (1.2 s, over 'three-quarters', ASR from 24.06 s), f1020-1106 (2.9 s, ending near '2028', ASR 36.16 s), f1118-1282 (5.5 s, over 'nearly three times more turbine capacity', ASR 39.78-41.34 s) and f1974-2049 (2.5 s, over the permitting sentence); monotone fractions 0.97-1.0 (`color_yellow.json`). A red dotted line draws under the first highlight over f322-348 (26 frames, 183 px, monotone 1.0, `color_red.json`) as the narration says 'a place in line for one'.
- **One decelerating zoom, measured.** The permitting text page enlarges 1.89x about the stage centre over 56 frames (f1941-1996) with an ease-out cubic fit on scale and pan_x (SUPPORTED, margin 0.093; `camera_1941_1996.json`), while the highlight starts at f1974.
- **Typing and logo beats land on the word.** 'You are...' is typed letter by letter over f2122-2134 (70.7-71.1 s) as the sentence 'So it's not just a single waitlist' begins (ASR 70.66 s); the Netflix logo scales in over f2313-2316 (77.10-77.20 s), within 0.12 s before the ASR 'Netflix' (77.22 s) (ASR uncertainty ~100 ms; no audio listened to).
- **Speech-bubble escalation.** The tech-company scene stacks three bubbles: text changes to 'A SUPERCALIFRAGILLION DOLLARS!!!' in one frame (f1443), then 'Pls stop making up numbers' (f1475) and 'WE CAN'T!!!' (f1521) pop in; the manufacturers' logos stay constant (`DIRECTLY_OBSERVED`).
- **Reused kit.** The lone worried figure is reused inside the Short (S12, S15); the green US-map character, the blackboard figure and the bag/paper props are also in other validated Shorts (`DIRECTLY_OBSERVED` from the asset tables); the Transformers poster and the Latitude/Utility Dive pages are source material (rights status unverified).
- **No screen recording, no generated motion identified.** 15 detected changes (mostly sub-1 % caption/prop changes and the f2379-2418 turtle scene) stay as unresolved rows.
