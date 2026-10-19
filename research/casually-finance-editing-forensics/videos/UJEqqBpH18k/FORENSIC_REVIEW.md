# Forensic review — UJEqqBpH18k "The World Is Running Out of Buyers"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`The-World-Is-SnapYT.App.mp4` (`CFSRC-039`), SHA256 `ab444fc9...f5d37`, H.264/AAC, 360x640, 30.0 fps, 2206 frames (decoded = ffprobe), 73.579 s. SHORT uploaded 2026-09-12, 37,564 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (banded layout; scenes cut-delimited; every HARD/ANIMATION auto stage event seen on lean pre/active/post sheets; operations authored for the main events, remaining detected changes kept as UNRESOLVED_CHANGE rows; caption words measured against ASR). Audio: whole track measured (76 % voiced, 14 pauses >=0.25 s, 8 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2205.

## Measured statistics
- 15 scenes (median 3.57 s, p10 1.53, p90 10.60, longest 16.03); 13 hard cuts (10.6/min); 40 events (32.62/min), 31 of them one-frame.
- Operations: HARD_CUT_REPLACE 13, POP_IN 9, UNRESOLVED_CHANGE 7, CAMERA_SCROLL_ZOOM 5, OVERLAY_POP 3, HIGHLIGHT_SWEEP 1, TEXT_WRITE_ON 1, SLIDE_IN 1.
- Frame-weighted: static hold 87.3 %, plausibly conventional keyframe/compositing 11.2 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 1.5 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -67 ms (p10 -160, p90 6; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: irregular duplicates; cadence unresolved.

## Findings
- **Banded era (fourth example).** Persistent headline 'We Have No Control Over the Bond Market' (zero change), bounded stage, caption band aligned to ASR (median +44 ms, 73 % within ±100 ms, n = 216); 30 fps file with the 24→30 repeat cadence in motion segments.
- **13 hard cuts in 73.5 s (10.6/min)**, the slowest cutting of the banded sample (Qof71Ef-3EU 29/min, DEgQTSsSX9U 23/min, NgryCruZegs 19/min): long scenes hold evidence (Fed page 593-112 = 16 s) while captions carry the pace.
- **Recycled kit again.** MUNDER DIFFLIN sign, bond tag, bill-by-bill timeline with bag, the country ensemble and the Japan-map character recur from the other banded Shorts; the timeline is rebuilt (bills at f609, f634, f658, f682, f698; ~25-frame spacing), not reused as a clip.
- **Written-on text on a diagram.** A struck-through 'thirty years' label grows over the timeline for ~38 frames (`TEXT_WRITE_ON`), the only write-on of its kind in the sample so far.
- **Evidence scene length.** The Fed committee page scrolls and zooms three times (f138-150, f157-163, f184-205) with a host pop-in at f204 and a highlight at f592.
- **No screen recording or generated motion identified.**

## Uncertainties
Scene boundaries snapped to the nearest large change; 5 scenes begin without one; creator tools unknown; caption timing measured; no listening; single reviewer.
