# Forensic review — HvnVO1_YrMQ "Who Allowed This to be The Fix For the Economy?"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Who-Allowed-This-SnapYT.App.mp4` (`CFSRC-049`), SHA256 `ef5ecc81...f4740`, H.264/AAC, 360x640, 24.0 fps, 1704 frames (decoded = ffprobe), 71.061 s. SHORT uploaded 2026-09-25, 21,187 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth
DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed). Audio: whole track measured (76 % voiced, 16 pauses >=0.25 s, 10 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-1703.

## Measured statistics
- 15 scenes (median 4.00 s, p10 2.14, p90 8.77, longest 11.54); 14 hard cuts (11.82/min); 47 events (39.68/min), 35 of them one-frame.
- Operations: HARD_CUT_REPLACE 14, POP_IN 12, CAPTION_CHUNK_CHANGE 7, OVERLAY_POP 5, STROKE_REVEAL 3, SLIDE_IN 2, POSE_SWAP 2, PROP_DRIFT 1, HIGHLIGHT_SWEEP 1.
- Frame-weighted: static hold 70.9 %, plausibly conventional keyframe/compositing 29.1 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 0.0 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -55 ms (p10 -183, p90 74; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = 24 fps).

## Findings
- **Chart growth.** Three EIA charts grow left to right as areas/lines (crude stack f637-684, gas line f797-834, combined stack f919-971): progressive chart reveals that carry the narration's numbers (`DIRECTLY_OBSERVED`; progress not tracked here).
- **Counting props.** Barrels fall in one by one (3), gas cylinders pop in pairs (4), a red X cancels the barrels, then the cylinders replace them: the metaphor changes with the sentence (`DIRECTLY_OBSERVED`).
- **Long source scene.** A Bloomberg article scrolls for ~233 frames (9.7 s, the longest hold in this sample so far) with green and cyan highlights sweeping while an analyst figure with a laptop stays still.
- **Pop-culture analogies.** A basketball player dunking on a hoop (S14) carries the 'eight-foot hoop' analogy; a pixel-sunglasses overlay appears on the official (S09); a 'SUPER DUPER PLAN! CLASSIFIED' document parodies the plan. Meme/pop imagery is part of the grammar (`DIRECTLY_OBSERVED`; rights unverified).
- **Official as recurring character.** The grey-haired green-tie figure (also in `RB5zVghPor8`, `7IMFHclDn8k`) appears three times with bubbles and a sunglasses overlay.
- **Slides.** Map character and host slide in from the left edge (18 frames each).
- **No screen-recorded or generated motion identified.**

## Uncertainties
Coarse authoring; caption timing not measured; barrel and chart progress not tracked; creator tools unknown; no listening; single reviewer.
