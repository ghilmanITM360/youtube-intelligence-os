# Forensic review — s3_3SFxtt14 "Japan's Economy Doesn't Work Without Us Anymore"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Japan's Economy Doesn't Work Without Us Anymore.mp4` (`CFSRC-023`), SHA256 `cc75eb40...c0b0a`, H.264/AAC, 720x1280, 30.0 fps, 1825 frames (decoded = ffprobe), 60.916 s. SHORT uploaded 2026-08-23, 24,011 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_C (cut-delimited scenes authored from a 1 s full-duration overview; detected changes not individually classified are kept as UNRESOLVED_CHANGE rows; event sheets not viewed). Audio: whole track measured (73 % voiced, 16 pauses >=0.25 s, 8 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1824.

## Measured statistics
- 19 scenes (median 2.43 s, p10 1.17, p90 6.41, longest 8.00); 18 hard cuts (17.73/min); 53 events (52.2/min), 36 of them one-frame.
- Operations: UNRESOLVED_CHANGE 31, HARD_CUT_REPLACE 18, POP_IN 1, CAMERA_SCROLL_ZOOM 1, CHARACTER_RISE_IN 1, SLIDE_IN 1.
- Frame-weighted: static hold 73.2 %, plausibly conventional keyframe/compositing 7.5 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 19.3 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -54 ms (p10 -306, p90 79; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (2 isolated duplicates, 0 with a 5-frame gap).

## Findings
- **Fastest cutting in the sample so far.** 18 hard cuts in 60.8 s but ~39 further detected change runs (19 % of frames) that are mostly animated screenshot scrolls and character moves; only the two largest spans (report scroll f976-1075, report slide-in f1686-1703) were resolved (`DIRECTLY_OBSERVED`). The rest are UNRESOLVED_CHANGE (depth C).
- **Document as a scrolling background.** The Treasury report scrolls vertically through four pages while the host pops in front (~f996) and points; the FT article is reused in three scenes (S03, S04, S17) at different highlight states, with a red 'only told them AFTER' pop and a 'never happened before' pop.
- **Institution as joke.** The Treasury seal appears five times and gets pixel sunglasses and bubbles ('It's MY money and I do what I want!', 'No comment.'); a shadow figure with red eyes and a note personifies the watch list (`DIRECTLY_OBSERVED`; meme sunglasses overlay rights unverified).
- **Country characters.** US-map and Japan-map characters carry eyes and legs; the US character is used for the first and the 'broke a 28-year rule' scenes (`DIRECTLY_OBSERVED`).
- **Closing.** Report cover held with the Japan character and a large 'Why?' (no summary card).
- **No screen recording or generated motion identified.**

## Uncertainties (DEPTH_C)
31 detected changes unresolved; event sheets not viewed; scene boundaries at 601 and 1691-1808 are authored from the 1 s overview; caption timing not measured; creator tools unknown; no listening; single reviewer.
