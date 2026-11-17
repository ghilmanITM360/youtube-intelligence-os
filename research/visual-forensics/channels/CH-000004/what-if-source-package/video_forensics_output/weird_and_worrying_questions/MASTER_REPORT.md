# Master Report — weird_and_worrying_questions

## 1. Source summary
1080x1920 (9:16), 24fps constant frame rate, 1139 frames, 47.458s video / 47.508s container. H.264 + AAC-LC stereo audio (present, decoded successfully). SHA-256 and full technical detail: [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md).

## 2. Audio status
Audio stream present and verified; no transcript could be produced (local speech-to-text install failed in this environment, same as other videos in this project). Unusually for this project, every question and caption line is also fully legible on-screen, so on-screen text is a near-complete proxy for spoken content: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 3. Observed production DNA
A "reading weird internet questions" comedic short in the same hand-drawn black-ink vector/sketch style used elsewhere in this project: a single recurring stick-figure narrator (C01) sits at a desk for the **entire video in one locked, uncut camera shot**, reacting via an evolving thought bubble to five named, on-screen questions (Shelby, Jeff, Tomasz, AJ, Karl) plus one unattributed spoken aside. Every "cut" detected by automated scene analysis is a large content swap within this single static frame (a bubble graphic appearing/clearing, or a second character entering/exiting), not a camera change — the entire video is modeled as one shot, S01, with 27 internal visual states. Full detail: [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md).

## 4. Shot / state counts
| Metric | Count |
|---|---|
| Shots | 1 (S01, the entire 47.458s runtime — no camera cuts observed) |
| Visual states | 27 |
| Unique assets | 19 |
| Motion events | 25 (A01–A25) |
| Unique source images (WAY 2) | 14 (6 reused across multiple states; 2 first/last-frame pairs) |
| Audio assets | 1 (undifferentiated full-mix track, AU01) |

## 5. Motion event summary
25 observed motions, almost all content swaps (new graphic appears or existing graphic clears) rather than continuous physical motion; the two genuine continuous-motion events are the thermometer's mercury drop (A03) and the crying figure's growing puddle (A23, ~3s, the longest single motion in the video). The one clear physical translation is the thrown coffee mug (A06). Full detail: [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv).

## 6. Audio event summary
Continuous narration (LIKELY, reading the on-screen questions/captions aloud) for nearly the entire runtime, with 4 measured near-silence gaps (max 0.51s) concentrated in the closing third. No exact spoken words are known, but on-screen Q-card and caption text is a reliable content proxy throughout. Full detail: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 7. WAY 1 — CapCut rebuild overview — COMPLETE
Because the video is one continuous locked shot, the single S01 build recipe sequences layer visibility/keyframes across all 27 states rather than cutting between camera shots: [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md).

## 8. WAY 2 — Image-to-video overview — COMPLETE
14 unique image entries (6 reused across multiple states, 2 first/last-frame pairs for the biggest compositional jumps — the teeth/coffee payoff and the volcano/plaque/crying transitions) and 25 animation prompts (all ≤500 characters) cover the full single-shot state chain: [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md), [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md), [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md).

## 9. Important fidelity limitations
- No speech transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is UNKNOWN as exact wording, though on-screen Q-card/caption text is fully transcribed and used as the primary content proxy (unusually complete for this project).
- Seven internal state boundaries (frames 213, 292, 507, 675, 833, 977, and a small blip at ~1134) are OBSERVED (confirmed by automated scene-cut detection); the remaining 20 internal state boundaries were determined by 1-second-interval visual sampling only, not exhaustive frame-by-frame confirmation, and are labeled LIKELY in `TIMELINE.csv` and `MOTION_EVENTS.csv`.
- This project produces analysis, specs, and prompts only — no image, video, or audio has actually been generated or rendered.

## 10. File index
- [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md) · [00_source/audio/](00_source/audio/) (extracted original audio)
- [01_evidence/CONTACT_SHEET_1.jpg](01_evidence/CONTACT_SHEET_1.jpg) · [01_evidence/frames/](01_evidence/frames/) (47 source-resolution PNGs, 1 per second) · 5 targeted zoom-grid inspection tiles
- [02_analysis/TIMELINE.csv](02_analysis/TIMELINE.csv) · [02_analysis/ASSET_MANIFEST.csv](02_analysis/ASSET_MANIFEST.csv) · [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv) · [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md)
- [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md)
- [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md) · [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md) · [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md)
- [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md)
- [RUN_STATE.json](RUN_STATE.json) · [CONTINUATION_HANDOFF.md](CONTINUATION_HANDOFF.md) · [00_source/verify.py](00_source/verify.py) (runnable validation)
