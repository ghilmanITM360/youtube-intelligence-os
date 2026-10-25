# Master Report — what_if_the_moon_were_made_of_protons

## 1. Source summary
720x1280 (9:16), 24fps constant frame rate, 2114 frames, 88.083s video / 88.143s container. H.264 Main profile + AAC-LC stereo 44.1kHz audio (audio present, decoded successfully). SHA-256 and full technical detail: [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md).

## 2. Audio status
Audio stream present and verified; no transcript could be produced (local speech-to-text install failed in this environment, same as other videos in this project — see manifest). Audio structure (7 measured near-silence gaps) derived directly from the waveform, and on-screen caption/label text is fully transcribed as the best available proxy for narration content: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 3. Observed production DNA
A fast-paced comedic physics "what if" explainer in loose hand-drawn black-ink vector/sketch style: a recurring minimalist stick-figure narrator (C01) reacts to an escalating series of self-contained whiteboard diagrams (circle-and-label scale comparisons, force arrows, energy-well graphics) on flat white or black backgrounds, culminating in a black-hole joke and a closing "growing void" gag on a starfield background. Every shot uses a static, locked camera — all motion is either a graphic element being drawn/revealed or a single icon growing/radiating in place; no camera movement, parallax, or multi-object choreography was observed anywhere. Full detail: [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md).

## 4. Shot / state counts
| Metric | Count |
|---|---|
| Shots | 9 (S01-S09) |
| Visual states | 32 |
| Unique assets | 27 |
| Motion events | 24 (A01-A24) |
| Unique source images (WAY 2) | 15 (all independently generated; no cross-shot reuse) |
| Audio assets | 1 (undifferentiated full-mix track, AU01) |

## 5. Motion event summary
24 observed motions, concentrated in the diagram-heavy first two-thirds: S03 (the orbit/force-scale comparison) accounts for 5 motions, S04 (the "moles of moles" escalation) for 3, S05 (electron-moon disintegration) for 2, S06 (universe/black-hole payoff) for 3, S08 (dark-energy joke) for 4, and S09 (closing growing-void gag) for 5, including the video's single longest continuous motion (~13s circle growth, A20). Full detail: [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv).

## 6. Audio event summary
Continuous mixed narration+music (LIKELY, unverified split) for nearly the entire runtime, with 7 measured near-silence points, several of which land close to shot boundaries (26.1s, 63.5s). No exact spoken words are known; on-screen captions/labels are used as the best proxy. Full detail: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 7. WAY 1 — CapCut rebuild overview — COMPLETE
All 9 shots have a full build recipe (track stack, keyframes, text, transitions, audio sync): [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md).

## 8. WAY 2 — Image-to-video overview — COMPLETE
15 unique image entries and 24 animation prompts (all ≤500 characters) cover all 9 shots, with explicit state chaining and two internal first/last-frame pairs (S06's zoom-to-black-hole payoff; S09's closing circle-growth payoff) used to control the video's two biggest compositional transformations: [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md), [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md), [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md).

## 9. Important fidelity limitations
- No speech transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is UNKNOWN as exact wording, though on-screen caption/label text is fully transcribed where present.
- All 8 shot boundaries are OBSERVED (confirmed by automated scene-cut detection), but all 24 internal visual-state boundaries were determined by 1-second-interval visual sampling only, not exhaustive frame-by-frame confirmation, and are labeled LIKELY for their exact IN/OUT frame in `TIMELINE.csv` and `MOTION_EVENTS.csv`.
- S09's ~13s continuous circle-growth motion (A20) will very likely need to be produced as several shorter chained I2V sub-clips rather than one generation call, given typical model duration limits — see `I2V_REBUILD.md`.
- This project produces analysis, specs, and prompts only — no image, video, or audio has actually been generated or rendered.

## 10. File index
- [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md) · [00_source/audio/](00_source/audio/) (extracted original audio)
- [01_evidence/CONTACT_SHEET_1.jpg](01_evidence/CONTACT_SHEET_1.jpg) · [01_evidence/CONTACT_SHEET_2.jpg](01_evidence/CONTACT_SHEET_2.jpg) · [01_evidence/frames/](01_evidence/frames/) (88 source-resolution PNGs, 1 per second)
- [02_analysis/TIMELINE.csv](02_analysis/TIMELINE.csv) · [02_analysis/ASSET_MANIFEST.csv](02_analysis/ASSET_MANIFEST.csv) · [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv) · [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md)
- [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md)
- [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md) · [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md) · [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md)
- [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md)
- [RUN_STATE.json](RUN_STATE.json) · [CONTINUATION_HANDOFF.md](CONTINUATION_HANDOFF.md) · [00_source/verify.py](00_source/verify.py) (runnable validation)
