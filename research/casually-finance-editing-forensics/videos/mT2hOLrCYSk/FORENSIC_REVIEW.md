# Forensic review — mT2hOLrCYSk "Every Tech Company Is (Basically) Guessing With This AI Stuff"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`Every Tech Company Is (Basically) Guessing With This AI Stuff.mp4` (`CFSRC-013`), SHA256 `f64f2a43...2237d`, H.264/AAC, 720x1280, 30.0 fps, 2711 frames (decoded = ffprobe), 90.452 s. SHORT uploaded 2026-08-21, 47,619 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_C (cut-delimited scenes authored from a 1.5 s full-duration overview; the three money-rain overlays inspected on a dense sheet and cross-correlated; all other detected changes kept as UNRESOLVED_CHANGE rows; event sheets not viewed). Audio: whole track measured (74 % voiced, 25 pauses >=0.25 s, 14 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-2710.

## Measured statistics
- 21 scenes (median 4.07 s, p10 1.93, p90 6.50, longest 10.10); 20 hard cuts (13.27/min); 69 events (45.77/min), 43 of them one-frame.
- Operations: UNRESOLVED_CHANGE 45, HARD_CUT_REPLACE 20, OVERLAY_CLIP_LOOP 3, CHARACTER_LOOP_ANIMATION 1.
- Frame-weighted: static hold 72.5 %, plausibly conventional keyframe/compositing 0.0 %, screen recording 0.0 %, complex continuous animation 10.7 %, change of undetermined method 16.8 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -137 ms (p10 -252, p90 104; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 111 of 114 duplicates share one phase mod 5; 5-frame gaps 84).

## Findings
- **Money-rain overlay (measured).** Three 85-115-frame scenes (f885-968, f1398-1512, f2389-2479) show dozens of overlapping banknote layers moving across the upper half every frame (lag-1 correlation 0.47) over fixed big-tech/Amazon/Meta logos. The bill layer is **pixel-identical across the three segments**: the first frame of each correlates 1.000 with the others over the unobstructed band y 0.30-0.40 (`MEASURED`, native frames 885/1398/2389). So one pre-rendered clip (or a seeded particle effect) is reused three times and trimmed to the phrase length (`DIRECTLY_OBSERVED` reuse; authoring method `UNKNOWN`). Frame-weighted these scenes are the 'complex continuous animation' share of this video (10.7 %) because the motion is dense per-frame overlay, not simple keyframes.
- **Hard cuts around the overlay.** The rain starts with a single-frame full-stage replacement and ends on another (f969, f1513, f2480); scene boundaries were set at those frames.
- **Number labels in colour.** '+2.5B' and '$ PER SHARE' in green and '-3.2B', '-2.9B' in red/black are hand-lettered figures that sit on the logo/bag (`DIRECTLY_OBSERVED`).
- **Filing pages as evidence.** Amazon and Meta 10-K pages are shown full-bleed with highlight sweeps and a peeking host (S09, S13-S15, S17).
- **Comparative close.** A red vertical divider splits Amazon | Meta, each with a chip, a calendar and three-figure icons (S19), then the blackboard host delivers 'These guys... reaching opposite conclusions'.
- **Frame-weighted caution.** 16.8 % of frames contain detected changes whose mechanism was not resolved (`INDET`); the true conventional/complex split for this video is therefore uncertain. No screen recording identified.

## Uncertainties (DEPTH_C)
45 auto-detected changes are UNRESOLVED_CHANGE; scene boundaries between S02-S06 and S09-S11 are authored from a 1.5 s overview and may be 1-3 s early/late (cut frames verified numerically only where a large change exists); caption timing not measured; creator tools unknown; no listening; single reviewer.
