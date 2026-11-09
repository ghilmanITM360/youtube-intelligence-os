# Forensic review — ud1ESmogrFY "America Has No Plan B"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`America Has No Plan B.mp4` (`CFSRC-005`), SHA256 `242114c8...6dc94`, H.264/AAC, 720x1280, 30.0 fps, 2603 frames (decoded = ffprobe), 86.853 s. SHORT uploaded 2026-08-19, 27,391 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (full-bleed analysis of a Short whose headline disappears at f245; scenes cut-delimited; every CUT/BIG_POP/ANIMATION auto event seen on compact pre/active/post sheets; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words counted only). Audio: whole track measured (76 % voiced, 24 pauses >=0.25 s, 19 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2602.

## Measured statistics
- 35 scenes (median 2.23 s, p10 1.17, p90 4.09, longest 5.63); 37 hard cuts (25.56/min); 152 events (105.01/min), 113 of them one-frame.
- Operations: UNRESOLVED_CHANGE 94, HARD_CUT_REPLACE 37, POP_IN 9, OVERLAY_POP 4, ROTATION 3, CAMERA_SCROLL_ZOOM 2, CHARACTER_RISE_IN 1, SCALE_TWEEN 1, OVERLAY_CLIP_LOOP 1.
- Frame-weighted: static hold 74.3 %, plausibly conventional keyframe/compositing 12.6 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 13.1 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -53 ms (p10 -156, p90 52; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 86 of 91 duplicates share one phase mod 5; 5-frame gaps 62).

## Findings
- **Headline for the first 8 s only.** The persistent headline "it's boring, but it's what bursts the bubble" is on screen until f244 (8.13 s); from the cut at f244 the Short runs with no headline and a small caption line (median +33 ms against ASR onsets, 76.9 % within ±100 ms, n = 273). The headline differs from the public title ("America Has No Plan B") and matches no local title (`DIRECTLY_OBSERVED`). None of the other banded Shorts analysed drops its headline mid-video (the full-bleed Shorts have none at all).
- **Fastest cutting in the sample after `Qof71Ef-3EU`.** 37 hard cuts in 86.8 s (25.6/min: 34 scene changes plus three black-frame flickers at f315, f319 and f322), median scene 2.2 s, shortest 0.7 s; 152 rows in the event table (105/min including 94 unresolved small changes), 113 of them one-frame. Hard cuts sit a median 53 ms before the nearest ASR word onset (n = 37, range -460 to +180 ms; 29 lead, 27 within ±100 ms; ASR uncertainty ~100 ms).
- **24 fps conform measured.** 91 isolated duplicate frames in motion, 62 exactly 5 frames apart and 86 of 91 sharing one phase modulo 5 (`MEASURED`): the same 24-to-30 fps conform as the other Aug-Sep videos.
- **Two linear pull-backs reveal the screen.** The orange 'is it gonna LAST? / BROKE' room zooms out to 0.79x with a 48 px downward shift over 94 frames (f883-976) and then to 0.57x over 42 frames (f992-1033), all linear (SUPPORTED; `camera_883_976.json`, `camera_992_1033.json`), revealing that the room is a video on a laptop screen (total scale about 0.45x) while the narration says 'every industry'.
- **Gags land on the word.** The black screen with two eye dots starts at f322 (10.73 s) on the ASR 'blackouts' (10.70 s) after a first 4-frame flash at f315-318; the 'ENERGY' title and its props pop at f219 (7.30 s) on the ASR 'energy' (7.32 s).
- **Setup before name.** The Thanos picture cuts in at f1560 (52.0 s), 3.3 s before the ASR 'Thanos' (55.36 s) and the snap line (55.86 s); the chatbot scene starts at f1052 (35.07 s), 1.6 s before 'strawberry' (36.72 s): visuals arrive at the start of the sentence, not at the keyword (`MEASURED` timing; ASR uncertainty ~100 ms).
- **Recurring props.** A roulette table or wheel (S07, S08 and S17, with the green US-map character in S07 and S17), tech-company logos (S09, S28, S32), the robot with red eyes (S02, S08, S09, S17, S20, S26, S33), the lone figure and the speech bubbles recur; the 'OR IT'S OVER' giant text and the 'Pick this, I'm out' exit gag close the Short.
- **Unresolved detail.** 94 detected changes (13.1 % of frames) stay as unresolved rows, most of them small caption, prop and particle changes in the dense sections; the sparkle particles around the logo bubble (f2349-2382) and the chip pile are classed `PLAUSIBLE_HYPOTHESIS` or LOW. No screen recording and no generated motion identified.
