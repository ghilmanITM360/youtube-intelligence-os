# Forensic review — ODMyV3F_G2g "A Leaked Picture's The Only Proof We Spent Billions on Japan"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`A Leaked Picture's The Only Proof We Spent Billions on Japan.mp4` (`CFSRC-003`), SHA256 `a5711dee...ee3bb`, H.264/AAC, 720x1280, 30.0 fps, 1953 frames (decoded = ffprobe), 65.189 s. SHORT uploaded 2026-08-22, 16,022 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (78 % voiced, 12 pauses >=0.25 s, 8 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1952.

## Measured statistics
- 18 scenes (median 3.22 s, p10 1.25, p90 6.62, longest 8.30); 17 hard cuts (15.65/min); 56 events (51.54/min), 39 of them one-frame.
- Operations: HARD_CUT_REPLACE 17, POP_IN 14, OVERLAY_POP 6, UNRESOLVED_CHANGE 5, SLIDE_IN 5, CAMERA_SCROLL_ZOOM 2, CHARACTER_RISE_IN 2, POSE_SWAP 2, PROP_DRIFT 1, SCALE_TWEEN 1, OPACITY_FADE 1.
- Frame-weighted: static hold 77.1 %, plausibly conventional keyframe/compositing 22.9 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -67 ms (p10 -155, p90 8; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: too little continuous motion to test cadence (0 isolated duplicates, 0 with a 5-frame gap).

## Findings
- **Full-bleed, no headline, no caption band.** White background from the first frame; captions are not a fixed band, so caption timing is `NOT_MEASURED`. The file is 30 fps with no isolated duplicate frames in motion, so no 24-to-30 fps conform can be tested (`MEASURED`).
- **Cutting.** 17 hard cuts in 65.2 s (15.7/min), 18 scenes (median 3.2 s, shortest 0.9 s, longest 8.3 s); 56 table rows (51.5/min); 77.1 % of frames are static holds and 22.9 % conventional keyframe motion; no screen recording, no clip insert, no unresolved-method frames. Hard cuts sit a median 67 ms before the nearest ASR word onset (n = 17, range -173 to +160 ms; 7 lead by more than 100 ms, 9 within ±100 ms, 1 lags; ASR uncertainty ~100 ms) (`MEASURED`).
- **Two measured zooms on source photos.** The portrait of the Secretary enlarges 1.29x and moves up ~84 px (analysis size) over ~39 frames (f309-347; pans linear `SUPPORTED`, scale linear `AMBIGUOUS`), then the desk photo enlarges 1.85x with a (-19,+126) px shift over ~43 frames (f389-430), linear on scale and both pans (`SUPPORTED`, margin 0.038-0.041) (`MEASURED`).
- **A 145-frame black-box build, then a linear fade.** A black rectangle grows linearly from a small block to a frame-wide block over 145 frames (f1704-1848, ink area linear `SUPPORTED`, margin 0.049) while the host's face changes twice (neutral to a smile by f1788, a wider smile by f1848); it then fades into the desk photo, the mean gray of the upper stage rising 137 to 193 at a constant ~2.4 levels per frame over f1849-1873 (`MEASURED`).
- **Pops follow the spoken word.** Red '1998' appears at f763-764 (25.43 s), 50 ms before ASR '1998' (25.48 s); the 'buy milk' notepad pops at f928 (30.93 s) at ASR 'a doodle' (30.88 s); the red question mark pops at f1462 (48.73 s), 0.15 s before ASR 'buying' (48.88 s); the 'DON'T LOOK!' bubble pops at f1907 (63.57 s) at ASR 'was ever supposed' (63.58 s) (`MEASURED`; ASR uncertainty ~100 ms).
- **Counted pops carry the argument.** Fourteen one-frame pop-ins (US-map character, portrait, seal, notepad, DEBT papers, three bond papers one by one at f1284, f1291 and f1297, globe character) and six overlay pops make up most of the motion; three bond papers pop at 6-7 frame intervals (`DIRECTLY_OBSERVED`).
- **Source layer.** Portrait with flag and seal, a name-plate desk photo with a handwritten note, a Reuters article, a news card ('Joint Intervention'), a second news card ('Treasury yield tops 5.19%') and a red arch labelled 'TRUTH' are the evidence and metaphor props; the same name-plate photo is used in S04, S07 and S18 (`DIRECTLY_OBSERVED`).
- **No script reuse found.** No run of 8 or more identical ASR words with any other analysed video.
