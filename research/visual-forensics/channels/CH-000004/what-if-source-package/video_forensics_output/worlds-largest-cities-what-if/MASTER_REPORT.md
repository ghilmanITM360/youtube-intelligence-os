# Master Report — worlds-largest-cities-what-if

## 1. Source summary
9:16 vertical, 1080x1920, 24fps, 83.333s, H.264/AAC. See `00_source/SOURCE_MANIFEST.md`. No local speech-to-text tool was available — narration wording is UNKNOWN throughout (see `05_audio/AUDIO_MAP.md`).

## 2. Observed production DNA
Hand-drawn "doodle explainer" style: grayscale stick-figure/blackboard intro (S01), then one giant hand-drawn world map (E01) that the camera pans across for the remaining 79 seconds (S02), revealing 20 city pins and 2 decorative circular sticker vignettes as it goes. No 3D, no photography, no character motion, no particle/lighting effects anywhere. Full detail: `02_analysis/VISUAL_DNA.md`.

## 3. Shot / state counts
- 2 shots (S01, S02).
- 2 states in S01 (F01.0, F01.1).
- 9 held camera states in S02 (F02.0–F02.8), connected by 8 pan/push transitions + 1 slow pan.
Full timeline: `02_analysis/TIMELINE.csv`.

## 4. Asset counts
9 unique assets (T01, C01, O01, O02, E01, G02, G03, G04, G05) + 1 audio bed (AU01). G02 (city pin) is reused 20x; E01 (the map) underlies the entire second half. Full list: `02_analysis/ASSET_MANIFEST.csv`.

## 5. Motion event counts
10 camera/transition events (A01–A10) + 6 static reveal events (R01–R06). 8 of the 9 S02 transitions are fast blurred pan/push bursts; 1 (A08) is a slow unblurred pan — the one meaningful exception to the pattern. Full list: `02_analysis/MOTION_EVENTS.csv`.

## 6. WAY 1 — CapCut rebuild overview
Fully buildable natively in CapCut: S01 as two static PNG/text holds, S02 as one large map image with position/scale keyframes simulating the pan (crop-window technique), plus 20 timed text/dot overlays and 2 timed sticker overlays. One limitation: CapCut has no true layer-parenting, so the two map-anchored stickers (G04, G05) must be hand-keyframed to match the map's own pan deltas. See `03_capcut/CAPCUT_REBUILD.md`.

## 7. WAY 2 — Image-to-video overview
Only 3 unique source images are needed for the whole video (IMG01, IMG02, IMG03a/b) — reused rather than regenerated per shot. Because every observed S02 motion is a static-image camera pan (not independent generative motion), **no I2V generation is actually required for the map portion** — it is reconstructed the same way as the CapCut build, via crop/position keyframes over the still IMG02 plate in final assembly. The only optional generative pass is the single whip-zoom-blur transition (A02), and even that has an equally faithful non-generative alternative. See `04_image_to_video/IMAGE_PROMPTS.md`, `ANIMATION_PROMPTS.md`, `I2V_REBUILD.md`.

## 8. Important fidelity limitations
- Internal S01 cut point (F01.0→F01.1, ~2.0s) and every S02 burst-transition boundary are APPROXIMATE, bounded by the ~3–7s sampling interval used for frame extraction — re-verify exact frame numbers against the source before final cutting if frame-accuracy matters.
- Narration/voiceover wording is UNKNOWN (no transcription tool available) — do not add invented dialogue.
- Exact fonts, the original map-drawing tool, and the original editing software are UNKNOWN and not fabricated anywhere in this package.
- G04/G05 stickers' exact purpose (mascot gag vs. sponsor/brand beat) is UNKNOWN — only their observable appearance and map-anchored behavior are documented.

## 9. File index
- `00_source/SOURCE_MANIFEST.md` — container/stream metadata, tooling limitations.
- `01_evidence/CONTACT_SHEET.jpg`, `01_evidence/frames/*.jpg` — visual evidence.
- `02_analysis/TIMELINE.csv`, `ASSET_MANIFEST.csv`, `MOTION_EVENTS.csv`, `VISUAL_DNA.md` — canonical forensic data.
- `03_capcut/CAPCUT_REBUILD.md` — WAY 1 build recipe.
- `04_image_to_video/IMAGE_PROMPTS.md`, `ANIMATION_PROMPTS.md`, `I2V_REBUILD.md` — WAY 2 build recipe.
- `05_audio/AUDIO_MAP.md`, `audio_extract.mp3`, `silence_raw.log` — audio evidence.
- `RUN_STATE.json` — stage-completion record.
