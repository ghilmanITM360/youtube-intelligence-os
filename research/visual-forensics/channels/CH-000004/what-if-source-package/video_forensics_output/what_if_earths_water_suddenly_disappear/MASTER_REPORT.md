# Master Report — what_if_earths_water_suddenly_disappear

## 1. Source summary
1920x1080 (16:9, landscape — the first landscape video in this project's set), 24fps constant frame rate, 4411 frames, 183.792s video stream / 183.856s container. H.264 + AAC stereo audio (present, decoded successfully). SHA-256 and full technical detail: [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md).

## 2. Audio status
Audio stream present and verified; no transcript could be produced (local speech-to-text install failed in this environment, same as every other video in this project). Unlike `weird_and_worrying_questions`, on-screen text here covers only diagram labels/captions, not full narration, so most spoken content remains genuinely UNKNOWN: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 3. Observed production DNA
An "xkcd's what if?" video-series explainer in the same hand-drawn black-ink stick-figure style used elsewhere in this project, but structurally the most complex video in this project to date: a genuinely edited, 18-shot production (not a single locked shot) covering water-drainage physics, marine biology, atmospheric chemistry, geology, and astronomy. A recurring "host" (C01) bookends and punctuates the video at three points (intro question, mid-video punchline, closing epilogue). Full detail: [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md).

## 4. Shot / state counts
| Metric | Count |
|---|---|
| Shots | 18 (S01–S18; 17 of 18 boundaries corroborated by measured `ffmpeg scdet` score spikes) |
| Visual states | 47 |
| Unique assets | 41 |
| Motion events | 29 (A01–A29) |
| Unique source images (WAY 2) | 24 (reused across 47 states; only 4 images require baked text) |
| Audio assets | 1 (undifferentiated full-mix track, AU01) |

## 5. Motion event summary
29 observed motions: mostly STATE_REPLACEMENT (content swaps — graphics appearing/clearing, fill/color changes) and SEQUENTIAL continuous changes (fire spreading, gradient intensifying, objects descending). Only two motions are genuine physical translations through space: the sailboat capsize (A03) and the household figure+dog+boat departure (A20). Full detail: [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv).

## 6. Audio event summary
Continuous narration (LIKELY) through most of the runtime, with 22 measured near-silence gaps; two of these (58.7s, 154.9s) coincide almost exactly with independently-detected shot-cut timestamps, corroborating those cuts. The credits card (S18) and tail of S17 show markedly more silence, consistent with narration ending before the video does. Full detail: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 7. WAY 1 — CapCut rebuild overview — COMPLETE
18 per-shot build recipes covering media/layers/keyframes/transitions/audio sync for the full runtime: [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md).

## 8. WAY 2 — Image-to-video overview — COMPLETE
24 unique image prompts (aggressive reuse — several images cover 2-3 non-adjacent states each) and 29 animation prompts (all ≤500 characters) cover the full 18-shot state chain: [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md), [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md), [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md).

## 9. Important fidelity limitations
- No speech transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is UNKNOWN. Unlike `weird_and_worrying_questions`, on-screen text does not substitute for full narration content here — significant explanatory detail spoken by the narrator is not recoverable from visual evidence alone.
- 17 of 18 shot boundaries are OBSERVED (corroborated by `ffmpeg scdet` score spikes); all internal state boundaries within shots are LIKELY (determined by 2-second-interval visual sampling, appropriate to this video's 4x-longer runtime versus other videos in this project).
- The seaplane/jar-diagram interleave in S10 (F10.0–F10.3) could not be pinned to an exact frame boundary — no `scdet` cut was detected in that 29-second span — and is flagged APPROXIMATE in both `CAPCUT_REBUILD.md` and `I2V_REBUILD.md`.
- This project produces analysis, specs, and prompts only — no image, video, or audio has actually been generated or rendered.

## 10. File index
- [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md) · [00_source/audio/](00_source/audio/) (extracted original audio)
- [01_evidence/CONTACT_SHEET_1.jpg](01_evidence/CONTACT_SHEET_1.jpg)–[CONTACT_SHEET_4.jpg](01_evidence/CONTACT_SHEET_4.jpg) · [01_evidence/frames/](01_evidence/frames/) (92 overview PNGs, 1 per 2s) · [01_evidence/cuts/](01_evidence/cuts/) (34 before/after cut frames) · 5 targeted zoom-grid inspection tiles
- [02_analysis/TIMELINE.csv](02_analysis/TIMELINE.csv) · [02_analysis/ASSET_MANIFEST.csv](02_analysis/ASSET_MANIFEST.csv) · [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv) · [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md)
- [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md)
- [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md) · [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md) · [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md)
- [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md)
- [RUN_STATE.json](RUN_STATE.json) · [CONTINUATION_HANDOFF.md](CONTINUATION_HANDOFF.md) · [00_source/verify.py](00_source/verify.py) (runnable validation)
