# Master Report — what_would_a_magnitude_15_earthquake_be

## 1. Source summary
1280x720 (16:9, landscape), 24fps constant frame rate, 4447 frames, 185.29s video stream / 185.34s container. H.264 + AAC stereo audio (present, decoded successfully). SHA-256 and full technical detail: [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md).

## 2. Audio status
Audio stream present and verified; no transcript could be produced (local speech-to-text install failed in this environment, the same standing issue as every other video in this project). On-screen text here covers only headlines/captions/gag props, not full narration, so most spoken explanatory content remains genuinely UNKNOWN: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 3. Observed production DNA
An "xkcd's what if?" video-series explainer in the same hand-drawn black-ink stick-figure style used elsewhere in this project. Structurally simpler than the multi-topic water-disappearance video: one continuous idea (a vertical Moment-Magnitude scale) climbed from Magnitude 9 up to a fictional Magnitude 25 (the sun exploding), then descended from Magnitude 1 down to Magnitude -15 (an imperceptible mouse-scale vibration), bookended by an intro Q&A/comparison bit and the standard bumper/credits cards. Full detail: [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md).

## 4. Shot / state counts
| Metric | Count |
|---|---|
| Shots | 16 (S01-S16; all 16 boundaries OBSERVED via measured `ffmpeg scdet` score spikes ≥5.4) |
| Visual states | 47 |
| Unique assets | 39 |
| Motion events | 33 (A01-A33) |
| Unique source images (WAY 2) | 29 (extensive reuse; 3 first/last-frame pairs used for major transformations) |
| Audio assets | 1 (undifferentiated full-mix track, AU01) |

## 5. Motion event summary
33 observed motions: a majority are STATE_REPLACEMENT swaps between successive magnitude values (matching this video's core "flip through the scale" structure), plus several genuine continuous transformations — the NYC-skyline collapse (A03), the Earth cracking/fragmenting/exploding sequence (A10, A11, A13), the sun-to-magnetar morph (A14, A15), the magnetar's pulsing burst (A16), and small physical falls (leaf A24, cat A25/A26, feather A30, hourglass sand A31). Full detail: [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv).

## 6. Audio event summary
Continuous narration (LIKELY) through most of the runtime, with 26 measured near-silence gaps; three of these (18.9s, 125.6-126.0s, 158.2s) coincide almost exactly with independently-detected shot/state boundaries, corroborating those cuts. The final ~11 seconds (ending vignette + credits) show markedly more silence, consistent with narration ending before the video does — the same pattern observed in other videos in this project. Full detail: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 7. WAY 1 — CapCut rebuild overview — COMPLETE
16 per-shot build recipes covering media/layers/keyframes/transitions/audio sync for the full runtime: [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md).

## 8. WAY 2 — Image-to-video overview — COMPLETE
29 unique image prompts (3 as first/last-frame pairs for the video's hardest transformations) and 33 animation prompts (all ≤500 characters) cover the full 16-shot state chain: [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md), [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md), [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md).

## 9. Important fidelity limitations
- No speech transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is UNKNOWN. On-screen text covers only headlines/captions/gag props, not the narrator's actual explanation of each magnitude value.
- All 16 shot boundaries are OBSERVED (`ffmpeg scdet` score ≥5.4, corroborated visually at 1fps sampling). Internal state boundaries within shots are OBSERVED-to-LIKELY depending on how densely that region was sampled (native-frame spot checks for S01-S14's fast-changing sections; native-resolution grabs for the newspaper, ending vignette, and select magnitude cards).
- The S10-S12 region (sun → sunquake → magnetar → Magnitude-25 sun → explosion) has one APPROXIMATE shot-boundary attribution: the measured cut at 92.75s does not correspond to an obvious visual swap at 1fps sampling resolution, so F12.0's exact start content is a best-effort carry-over description rather than a confirmed new composition. Flagged in `TIMELINE.csv`, `MOTION_EVENTS.csv` (A17), and both rebuild files.
- A single-frame "MAGNITUDE 0" flicker measured at ~t7s within S01 is treated as a source-rendering artifact and is not reproduced in either rebuild pathway.
- This project produces analysis, specs, and prompts only — no image, video, or audio has actually been generated or rendered.

## 10. File index
- [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md) · [00_source/audio/](00_source/audio/) (extracted original audio)
- [01_evidence/CONTACT_SHEET_1.jpg](01_evidence/CONTACT_SHEET_1.jpg)-[CONTACT_SHEET_3.jpg](01_evidence/CONTACT_SHEET_3.jpg) · [01_evidence/frames/](01_evidence/frames/) (93 overview JPGs, 1 per 2s) · [01_evidence/dense/](01_evidence/dense/) (185 dense JPGs, 1 per 1s) · [01_evidence/DENSE_A_19-48.jpg](01_evidence/DENSE_A_19-48.jpg) through [DENSE_H_0-18.jpg](01_evidence/DENSE_H_0-18.jpg) (tiled inspection sheets) · [01_evidence/cuts/](01_evidence/cuts/) (targeted native-resolution grabs)
- [02_analysis/TIMELINE.csv](02_analysis/TIMELINE.csv) · [02_analysis/ASSET_MANIFEST.csv](02_analysis/ASSET_MANIFEST.csv) · [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv) · [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md)
- [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md)
- [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md) · [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md) · [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md)
- [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md)
- [RUN_STATE.json](RUN_STATE.json) · [CONTINUATION_HANDOFF.md](CONTINUATION_HANDOFF.md) · [00_source/verify.py](00_source/verify.py) (runnable validation)
