# Forensic review — _3tM1d-WeUI "AI Is Now (Structurally) Trapped."

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`AI Is Now (Structurally) Trapped..mp4` (`CFSRC-004`), SHA256 `5cd6e86a...ff184`, H.264/AAC, 720x1280, 30.0 fps, 2575 frames (decoded = ffprobe), 85.924 s. SHORT uploaded 2026-08-20, 29,088 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (banded layout with a lower header (header 0.24-0.37, stage 0.37-0.67); scenes cut-delimited; every HARD/ANIMATION auto stage event seen on lean pre/active/post sheets; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words measured against ASR). Audio: whole track measured (79 % voiced, 21 pauses >=0.25 s, 13 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2574.

## Measured statistics
- 23 scenes (median 3.47 s, p10 1.41, p90 6.17, longest 8.83); 21 hard cuts (14.66/min); 62 events (43.29/min), 48 of them one-frame.
- Operations: HARD_CUT_REPLACE 21, UNRESOLVED_CHANGE 17, POP_IN 8, OVERLAY_POP 7, POINTER_TRANSLATE 3, SCALE_TWEEN 2, CAPTION_CHUNK_CHANGE 1, CAMERA_SCROLL_ZOOM 1, SLIDE_IN 1, OVERLAY_CLIP_LOOP 1.
- Frame-weighted: static hold 77.7 %, plausibly conventional keyframe/compositing 14.7 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 7.6 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -67 ms (p10 -127, p90 153; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 33 of 111 duplicates share one phase mod 5; 5-frame gaps 99).

## Findings
- **Lower-header banded layout (second example).** Same layout as `ZDoeEd8fMdo` (uploaded the same day): persistent headline "ai now faces a severe power shortage" at y 0.24-0.37 of the 720x1280 frame, stage 0.37-0.67, small caption line below it (median +40 ms against ASR onsets, 70.4 % within ±100 ms, n = 250). The headline differs from the public title ("AI Is Now (Structurally) Trapped.") and matches no local title (`DIRECTLY_OBSERVED`).
- **Cutting.** 21 hard cuts in 85.9 s (14.7/min, median scene 3.5 s, longest 8.8 s); 62 events (43.3/min), 48 of them one-frame. Hard cuts sit a median 67 ms before the nearest ASR word onset (n = 21, range -207 to +267 ms, ASR uncertainty ~100 ms), consistent with the sample median of about -76 ms.
- **24 fps conform again, with a changing phase.** 111 isolated duplicate frames in motion, 99 of them exactly 5 frames apart (`MEASURED`), but only 33 of 111 share the most common phase modulo 5: the 5-frame pattern is present throughout but its phase is not constant across the file (restarts at cuts are a `PLAUSIBLE_HYPOTHESIS`).
- **Three pointer arrows, two clean linear fits.** The red arrow above the energy-consumption bars glides from x = 0.555 to 0.690 of the frame width over 73 frames (f1214-1286), linear (SUPPORTED, margin 0.047), while the narration says 'because American electricity demand flatlined for 20 years' (`blob_1214_1286.json`); on the last chart the arrow moves 0.733 to 0.796 (x) and 0.467 to 0.501 (y) over 46 frames, linear on both axes (SUPPORTED, margins 0.029 and 0.027; `blob_2432_2478.json`); on the PJM supply chart its ease is ambiguous (`blob_2021_2066.json`).
- **Shrinking figure into giant text.** The lone figure shrinks to about half its width over ~30 frames (f954-984, ink-extent fit ease-in quad, SUPPORTED, margin 0.149, indicative only because the incoming text adds ink), then 'TRUST ME BRO' appears oversized and shrinks to fit by f996 (`extent_954_1000.json`).
- **Running gag.** The PJM logo with a microphone and '*crickets*' text is used twice (S06 f581-845 and S13 f1317-1457) for 'an event nobody watches' and 'the single most boring event'; bubbles escalate inside S06 ('I'm bout to drop a BANGER!' f601, 'READY?!' f638, 'So uh...' f742) (`DIRECTLY_OBSERVED`).
- **Photo pair timed to the words.** The snowy-tree photo cuts in at f1046 (34.87 s) on the ASR 'January' (34.90 s); the heat-wave photo cuts in at f1084 (36.13 s), 0.33 s before 'August' (36.46 s). The snowy-tree photo shows a tentative ease-in shift of about (+27,+52) px at analysis size over 39 frames (`camera_1046_1084.json`, tracking may follow image content).
- **Pops at the word.** Red '67M' pops at f246 (8.2 s) just before the ASR '67' (8.30 s); 'Max $325' appears by f1947 (64.9 s), 0.24 s before 'maximum' (65.14 s); the 'Booked and busy, sorry!' bubble pops at f2371 (79.03 s), 0.13 s before 'booked' (79.16 s), followed by six calendar icons (f2377-2386); the turbine photo pops at f2220 (74.0 s), 0.16 s after 'turbine' (73.84 s) (ASR uncertainty ~100 ms; no audio listened to).
- **Visual overlap with `ZDoeEd8fMdo`.** The money-bag scene's right-hand panel shows a turbine photo, a purple bar chart and a permitting text page, which look like the transformer chart and permitting page used in `ZDoeEd8fMdo` (same upload day) (`DIRECTLY_OBSERVED` at overview resolution; a frame-exact reuse test was not run for this pair).
- **Unresolved.** 17 detected changes stay as unresolved rows (7.6 % of frames), the largest being the opening bubble, text and red-block sequence (f1-177); no screen recording and no generated motion identified. The ASR ends mid-word ('God.').
