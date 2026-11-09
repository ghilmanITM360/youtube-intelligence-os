# Forensic review — f_ZCoPKLpyU "Japan's Economic Problems... Now Is America's Economic Problem"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Japan's Economic Problems... Now Is America's Economic Problem.mp4` (`CFSRC-022`), SHA256 `a7b7c2db...28eea`, H.264/AAC, 720x1280, 30.0 fps, 1848 frames (decoded = ffprobe), 61.682 s. SHORT uploaded 2026-08-31, 23,417 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (full-bleed analysis of a Short whose headline disappears at the blackboard cut; scenes cut-delimited; every CUT/BIG_POP/ANIMATION auto event seen on compact pre/active/post sheets; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words counted only). Audio: whole track measured (77 % voiced, 11 pauses >=0.25 s, 11 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1847.

## Measured statistics
- 18 scenes (median 2.95 s, p10 1.81, p90 4.91, longest 9.77); 17 hard cuts (16.54/min); 94 events (91.44/min), 72 of them one-frame.
- Operations: UNRESOLVED_CHANGE 59, HARD_CUT_REPLACE 17, POP_IN 10, OVERLAY_POP 4, PROP_DRIFT 3, CAPTION_CHUNK_CHANGE 1.
- Frame-weighted: static hold 84.3 %, plausibly conventional keyframe/compositing 11.5 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 4.2 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median 20 ms (p10 -192, p90 164; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (1 isolated duplicates, 0 with a 5-frame gap).

## Findings
- **Same hybrid layout as `ud1ESmogrFY`.** A persistent headline "why japan s**** economy is now our problem" (profanity masked in the video) at y 0.24-0.37 of the 720x1280 frame for the first 19.3 s; it is gone from the cut at f579 (19.3 s, the blackboard scene) to the end, so the Short is banded for 31 % of its length and full-bleed afterwards. The headline differs from the public title ("Japan's Economic Problems... Now Is America's Economic ...") and matches no local title (`DIRECTLY_OBSERVED`). Captions are not band-aligned here (caption-to-ASR timing `NOT_MEASURED`).
- **Cutting.** 17 hard cuts in 61.6 s (16.5/min, median scene 3.0 s, longest 9.8 s); 94 table rows (91/min) of which 59 are unresolved small changes (4.2 % of frames) and 72 are one-frame. Hard cuts sit a median 20 ms after the nearest ASR word onset (n = 17, range -253 to +193 ms; 8 lead, 10 within ±100 ms; ASR uncertainty ~100 ms), later than the sample median of about -73 ms.
- **Cadence not testable.** One isolated duplicate frame: too little continuous motion to test the 24-to-30 fps conform.
- **Number pops follow the spoken number.** Red '13T' first appears at f276 (9.2 s) between the ASR '13' (8.76 s) and 'trillion' (9.42 s) and is steady by f285; red '122.3T' pops at f350 (11.67 s) during the budget sentence ('budget' 11.06 s); the red X over the dollar note pops at f1301 (43.37 s), 0.17 s after the ASR 'feelings' (43.20 s) and is removed at the cut f1320-1321 (`MEASURED` from red-pixel counts).
- **Visual gags on the sentence.** The yen note falls off the cliff over f1556-1601 (51.9-53.4 s) as the ASR says 'off a cliff' (cliff 52.96 s); the dollar bag leaves over f1814-1827 (60.5-60.9 s) as 'selling dollars' ends (60.82 s); the bags scene cuts in at f1757 (58.57 s), 0.33 s before 'buying yen' (58.90 s) (ASR uncertainty ~100 ms).
- **Same sentence, re-composed scenes (`zkeA5cH9nyM`).** A 25-word ASR block ('because the US dollar sits on one side of nearly 90 % of all currency trades on earth, buying yen almost always means selling dollars') is identical to the closing block of `zkeA5cH9nyM` (uploaded 2026-08-28; here 2026-08-31), and the same props (currency notes popping one by one, a globe character, dollar and yen bags) illustrate it, but five sampled frames of this sequence correlate at most 0.38 with the best-matching frames of `zkeA5cH9nyM` (45x80 gray correlation): the kit is reused, the clips are re-composed (`MEASURED`; only five frames tested).
- **Chart pages are passive; stakes come from props.** The three source charts (debt-to-GDP bars, bond issuance with 13T/122.3T, yen collapse) have no measured camera move in this Short; the only moving items are DEBT papers (popped in four to five steps), a stack of yen notes (five pops), arrows (six pops) and the falling note.
- **No screen recording, no generated motion identified.** 59 detected changes stay as unresolved rows.
