# Forensic review — Es5c2MKzbDg

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer). Machine QA passes (`QA.json`).

## Source
`58-More-Home-SnapYT.App.mp4` (`CFSRC-001`), SHA256 `ebf2dadf...ae35d`, H.264/AAC, 360x640, **24 fps**, 1,498 frames (decoded = ffprobe), 62.464 s. Short, uploaded 2026-10-15. Identity = title+duration match (not cryptographic). 360p limits line weight and small-motion measurement.

## Depth B means
Pass A: 63 overview frames (1 fps, full duration) and 22 cut-delimited scenes. Pass B: every frame decoded; whole-frame change segmentation (90 auto events: 18 CUT, 7 BIG_POP, 19 ANIMATION, 46 SMALL). Pass C: compact (148 px) pre/active/post sheets for all CUT, BIG_POP and ANIMATION events and for all 13 SMALL events with >=0.8 % area; 33 smaller events (caption words, thin strokes) were counted but not individually reviewed. Pass D: audio measured (79 % voiced, 11 pauses, noise floor ~20 dB below speech) plus Whisper; **not listened to**. Pass E: scenes contiguous over frames 0-1,497; every non-small auto event is attributed to an authored event. Continuous motions were not tracked numerically here (a host that stays fixed in front biases whole-frame registration), so their durations are frame counts from detection, not fitted easing.

## Findings
- **Cutting.** 19 hard cuts (18.3/min), 22 scenes, median 1.73 s but one 13.5 s evidence shot; every cut changes 20-57 % of pixels in one frame except one flagged and corrected boundary (S20 starts at f1416, not f1415).
- **Operations (60 events).** 8 scroll/zoom camera moves on screenshots, 3 slide-ins, 8 pops, 7 overlay pops, 3 scale tweens (host zoom ×2, icon growth), 2 highlight sweeps, 4 pose swaps, 1 stroke reveal, 1 layer slide behind a character, 1 character rise-in, 3 caption-chunk changes, 19 cuts.
- **Frame cadence.** Native 24 fps; no 5-frame duplicate pattern (4 isolated duplicates only). Contrast with `Qof71Ef-3EU` (24 fps conformed to 30). Author at the delivery rate of the target.
- **Caption layer.** Hand-lettered marker style whose position changes by scene; black words append progressively; large red words/numbers pop for emphasis. Word-level timing not measured for this layout (`NOT_MEASURED`).
- **Layering.** Full-bleed screenshot below, props and arrows above it, host/figures above those, captions top; figures can slide out and back in (S02) and props slide behind characters (S16).
- **Motion share.** Frame-weighted: static hold 73.6 %, motion present 26.4 % (all plausibly conventional keyframe/compositing events; no screen recording or complex character animation identified; no generated-video evidence). Counts: 60 events, 37 one-frame.
- **Narration.** Cuts lead the nearest ASR word onset by a median 125 ms (p10 -219, p90 -47); 53 % of all events fall within 100 ms of a word onset.
- **Audio.** Voiced 79 %; 11 pauses of >=0.25 s; no music/SFX distinguished from speech by measurement (`NOT_DETECTED`, not `ABSENT`).

## Uncertainties
Concurrent layers in S02 f78-f180 and S17 f1214-f1226 are only coarsely separated; 4 `POSE_SWAP` mechanisms and 3 `SCALE_TWEEN` interpolations are not resolved at 1-frame detail; creator tools unknown; no independent reviewer; no listening.
