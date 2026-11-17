# Master Report — how_long_could_you_drive_towards_the_sunset

## 1. Source summary
480x854 (≈9:16), 24fps constant frame rate, 3117 frames, 129.875s video / 129.980544s container. H.264 Main profile + AAC-LC stereo 44.1kHz audio (audio present, decoded successfully). SHA-256 and full technical detail: [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md).

## 2. Audio status
Audio stream present and verified; no transcript could be produced (local speech-to-text install failed in this environment — see manifest). Audio structure (2 measured near-silence gaps) derived directly from the waveform instead, and on-screen caption text is fully transcribed as the best available proxy for narration content: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 3. Observed production DNA
Fast-paced "what if" explainer mixing flat 2D vector diagram illustration (white-canvas circle/horizon diagrams, globes, maps) with painterly gradient-sky "real-world" scenes (a genuine sunset bookend and two polar establishing shots); minimal white stick figures throughout; red reserved exclusively for rejection marks and data-callout arrows; every shot uses a static, locked camera — all apparent motion is either graphic-element reveal/redraw or a small number of translating icons (car, sun, globe). Full detail: [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md).

## 4. Shot / state counts
| Metric | Count |
|---|---|
| Shots | 14 (S01-S14) |
| Visual states | 48 |
| Unique assets | 29 |
| Motion events | 34 (A01-A34) |
| Unique source images (WAY 2) | 14 numbered entries (13 generated + 1 reuse-stub) |
| Audio assets | 1 (undifferentiated full-mix track, AU01) |

## 5. Motion event summary
34 observed motions, concentrated in the long multi-beat shots: S04 alone accounts for 5 motions (flat-earth/mountain "wrong models" montage), S08 for 5 (Longyearbyen caption/data reveals), S10 for 4 (map/car/legend-icon build, including the video's longest single continuous motion at ~8.6s), and S14 for 5 (closing swirl + 4 dialogue-caption reveals). Full detail: [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv).

## 6. Audio event summary
Continuous mixed narration+music (LIKELY, unverified split) for nearly the entire runtime, with 2 measured near-silence points: a 0.11s gap at ~25.06s (mid-S04) and a 1.75s fade from ~128.23s to the end of the video. No exact spoken words are known; on-screen captions are used as the best proxy. Full detail: [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md).

## 7. WAY 1 — CapCut rebuild overview — COMPLETE
All 14 shots have a full build recipe (track stack, keyframes, text, transitions, audio sync): [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md).

## 8. WAY 2 — Image-to-video overview — COMPLETE
14 numbered image entries (13 generated prompts + 1 reuse-stub) and 34 animation prompts (all ≤500 characters) cover all 14 shots, with explicit state chaining and one deliberate reuse decision (S14 reuses S03's exact background/character plate as a visual bookend): [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md), [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md), [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md).

## 9. Important fidelity limitations
- No speech transcript exists; every `SCRIPT_OR_AUDIO_CUE` value in `TIMELINE.csv` is UNKNOWN as exact wording, though on-screen caption text is fully transcribed where present.
- Two shot boundaries (S07→S08, S13→S14) were not confirmed by the automated scene-cut detector despite a clear visual content change; they are marked LIKELY rather than OBSERVED for their exact cut frame (see `TIMELINE.csv` and `VISUAL_DNA.md`).
- Two long continuous motions (S04's ~6.4s mountain-roll, A09; S10's ~8.6s car-and-legend advance, A24) were confirmed smooth/single-direction via 1s interval sampling, not exhaustive native-frame verification; their exact internal pacing is LIKELY steady, not confirmed exact.
- This project produces analysis, specs, and prompts only — no image, video, or audio has actually been generated or rendered.

## 10. File index
- [00_source/SOURCE_MANIFEST.md](00_source/SOURCE_MANIFEST.md) · [00_source/audio/](00_source/audio/) (extracted original audio)
- [01_evidence/CONTACT_SHEET_1.jpg](01_evidence/CONTACT_SHEET_1.jpg) · [01_evidence/CONTACT_SHEET_2.jpg](01_evidence/CONTACT_SHEET_2.jpg) · [01_evidence/frames/](01_evidence/frames/) (130 source-resolution PNGs, 1 per second)
- [02_analysis/TIMELINE.csv](02_analysis/TIMELINE.csv) · [02_analysis/ASSET_MANIFEST.csv](02_analysis/ASSET_MANIFEST.csv) · [02_analysis/MOTION_EVENTS.csv](02_analysis/MOTION_EVENTS.csv) · [02_analysis/VISUAL_DNA.md](02_analysis/VISUAL_DNA.md)
- [03_capcut/CAPCUT_REBUILD.md](03_capcut/CAPCUT_REBUILD.md)
- [04_image_to_video/IMAGE_PROMPTS.md](04_image_to_video/IMAGE_PROMPTS.md) · [04_image_to_video/ANIMATION_PROMPTS.md](04_image_to_video/ANIMATION_PROMPTS.md) · [04_image_to_video/I2V_REBUILD.md](04_image_to_video/I2V_REBUILD.md)
- [05_audio/AUDIO_MAP.md](05_audio/AUDIO_MAP.md)
- [RUN_STATE.json](RUN_STATE.json) · [CONTINUATION_HANDOFF.md](CONTINUATION_HANDOFF.md) · [00_source/verify.py](00_source/verify.py) (runnable validation)
