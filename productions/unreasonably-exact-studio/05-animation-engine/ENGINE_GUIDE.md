# Unreasonably Exact animation engine: audit and reuse guide

**Snapshot:** `uemotion` as used in Slot 07 V3, taken on 2026-11-26 from `07-video-productions/SLOT07_lunar-laser-ranging/animation/uemotion/`. The snapshot is byte-identical to that folder, except that the `*.bak*` files were left out. **The locked film never imports this copy**, so changing it here cannot change the V3 renders.

**Verified:** `examples/engine_smoke.py` renders `examples/engine_smoke_2026-11-26.png` (Earth, Moon, stopwatch, disclosure note) from this snapshot and the library textures, in a fresh project layout under the scratchpad.

## 1. Architecture in one paragraph

- **Scenes are pure functions of time.** `scene(cv, ctx)` draws onto a supersampled `Canvas` in **design units (1080×1920)**. There is no frame-to-frame state, so any frame can be rendered alone (`render_frame`) or in parallel (`render_clip`, a fork pool streaming to ffmpeg as H.264/yuv420p). The same pure-time design lets `--still` and the rebuild check work.
- **Three named clocks** (`timeline.ClockSet`):
  - narration time (the voice recording) keys every reveal;
  - animation time, per segment;
  - model time, the physics, so a stopwatch can never drift from its pulse.
- **The cut** (`animation/roughcut.py` in the film) dispatches on narration time to each proof scene with that scene's own clocks, so every proof's asserts still hold in the film. Crossfades are rendered by drawing both scenes.

## 2. Component audit (the twelve priorities)

| Priority | Where | Reuse status | Notes |
|---|---|---|---|
| **Camera systems** | `uemotion/camera.py`: `Camera2D` (pan, zoom, rotate as a 3×3 similarity), `CamState` | **REUSABLE AS IS** | Used by every Slot 07 scene. The V3 opening is one continuous move (rest-point check) |
| **Multiplane parallax** | `camera.Layer2_5D` (per-layer factor, occlusion order, overscan check), `camera.starfield` | **REUSABLE AS IS** | Measured factors equal the configured ones: P02 (.06/.35/1.0), P13 (.08/.30/.75/1.0) |
| **Celestial rotation** | `space.sphere_rgba` / `draw_sphere` (equirectangular sampling, `lon0` spin, `cloud_lon` drift, `tilt`), `EarthMoonGeo`, `draw_earth_moon` | **REUSABLE**: needs `assets/earth/*` and `assets/moon/*` under the file names in `space.REAL_TEX` | P01: no antimeridian seam, no pole pinch. Library textures: `04-shared-assets/celestial/` |
| **Lighting and shadow** | `tokens.SUN` (one film-wide sun vector), sphere shading, terminator and night-light mask in `space.py` | Globe lighting **REUSABLE**. Character contact shadows are drawn per scene (`proofs/p06.py`) and are **FILM-SPECIFIC** | Keep one sun per film (Slot 07 rule 3) |
| **Layer compositing** | `canvas.py`: supersampling (`ss`), transform stack, `group(alpha)`, `blit_image` (warped bitmap, alpha-safe) | **REUSABLE AS IS** | `selftest.py` checks that `blit_image` leaves pixels outside the bitmap untouched |
| **Mesh deformation** | **Not in uemotion.** Slot 02 V15: `slot02_v15_reference/cloth_warp.py` (`field`, `warp`: 32 px grid, limb sigma fields, cloth ripple driven by drag/weight) and `rig_renderer.py` | **NEEDS REFACTOR** before sharing: it is bound to the V15 rigs and constants | Do not use cloth flutter in vacuum (playbook §15) |
| **Procedural graphics** | `easing.py` (named eases, no default), `photons.py` (detection markers, histogram), `optics.py` (corner cube, flat mirror, ray drawing), `camera.starfield` | **REUSABLE AS IS** | `optics.py` geometry is asserted (exit rays antiparallel) |
| **Graph animations** | `graphs.py` (`Axes`, `trace_line`, `bars`, `error_bar`), `photons.PulseHistogram` / `draw_histogram` | **REUSABLE AS IS** | Simulated data must carry the "Simulated data" note |
| **Time and distance visualization** | `stopwatch.py` (dial and readout driven only by model time), `space` ruler and scale bar, `formula.py` (tokens that move, scale and cross-fade into d = c × t / 2), `timeline.ModelClock` | **REUSABLE AS IS** | Formula tokens use the `math` face (macOS Arial Bold) |
| **Caption positioning** | `captions/captions_v2.py` (cue building, SRT, burn-in; three OFL styles A/B/C; style A = Comic Neue Bold 70 px), `uemotion/captions.py` (phrase lines inside `tokens.CAPTION_BOX`, word highlight), `captions/caption_qa_v15.py` (Slot 02 collision check) | **REUSABLE**: cue text comes from the film's word times | Shorts-UI overlap **not tested** |
| **Audio automation** | `audio/sound_design_v3.py` (music edit with a spectral seam, 29-point `AUTOMATION`, ducking, a 1–4 kHz carve, K-weighted calibration, key retuning, stems, two mixes), `audio/mix_v15.py`, `audio/audio_qa.py` (Slot 02 separation QA) | **REFERENCE IMPLEMENTATION**: the cue lists and automation rows are film data | Copy, then replace `cue_list()` and `AUTOMATION` |
| **Narration synchronization** | `uemotion/narration.py` (beat map CSV, word/phrase JSON, V1→V2 word-edge warp `NAR.v1(t)`), Slot 02 `slot02_v15_reference/align_v14.py` (whisper.cpp DTW words, voice-activity snap, per-phrase PCHIP warp), `sync_map_v15.py` | **FILM-SPECIFIC**: `narration.py` builds `NAR = Narration()` **at import**. It reads `../../narration/NARRATION_BEAT_MAP.csv`, `WORD_TIMESTAMPS.json` and `v1_historical/WORD_TIMESTAMPS.json`, and asserts the Slot 07 durations | A new film **must** replace `narration.py` (keep the `Narration` API: `beats`, `words`, `phrases`) |

Other modules: `tokens.py` holds the colour and type grammar, the safe area and caption box; it is film-wide but generic. `video.py` writes the clip with proof frames, frame stats and ffprobe output.

## 3. Project layout contract (the engine assumes it)

```
<project>/
  animation/uemotion/          (copy of this snapshot)
  animation/<scenes>.py        your scenes; sys.path includes animation/
  assets/fonts/comicneue/      ComicNeue-Regular.ttf, ComicNeue-Bold.ttf, OFL.txt
  assets/earth/, assets/moon/  only if you call space.preload_real() / real textures
  narration/NARRATION_BEAT_MAP.csv, narration/WORD_TIMESTAMPS.json   (read by narration.py)
```

`tokens.py` and `space.py` find `assets/` **three folders above their own file**: `uemotion/` → `animation/` → the project. Keep the layout, or change those two lines and record the change in the pin file.

## 4. How a new project reuses the engine (copy and pin)

1. Copy `05-animation-engine/uemotion/` to `<project>/animation/uemotion/`.
2. Copy the needed assets from `04-shared-assets/` into `<project>/assets/`, renamed to the names in `space.REAL_TEX` when using real globes.
3. Write `<project>/narration/` from the new recording. Use Slot 02's `align_v14.py` method (whisper.cpp with `-ml 1 -sow --dtw`, voice-activity snap), then adapt `narration.py` (remove the V1 warp and set `MASTER_WAV` and `MASTER_DURATION`).
4. Write `<project>/LIBRARY_PIN.md`: the snapshot date (2026-11-26), the files changed and why. This follows playbook §16 rule 2.
5. Build each mechanism as a proof scene with asserts. Assemble with a `roughcut.py` like Slot 07's (17-segment `CUT` table plus a `DISCLOSURES` table).
6. Validators:
   - `validators/validate_asset.py` for every incoming PNG;
   - `validators/contact_sheet.py` and `filmstrip.py` for decoded-frame review (the ffmpeg build has no `drawtext`);
   - the film's own `tools/rebuild_check.py` pattern for reproducibility.

## 5. Changing the shared engine

- Change the snapshot here, never inside a finished film.
- After a change, rebuild one old film against it as a regression test. Slot 07 is the regression film: copy the project, swap in the new `uemotion`, and run `tools/rebuild_check.py`. The frames should still match within about 2/255.
- Record the change in `../CHANGELOG.md` with the date.

## 6. Dependencies

`requirements_uemotion.txt`: Python 3.13.15; numpy 2.5.5, pillow 13.0.0, scipy 1.18.1, opencv-python-headless 5.1.0.95, aggdraw 1.4.1; ffmpeg 9.0.1; the macOS system fonts Menlo.ttc and Arial Bold.ttf (not redistributable).

Slot 02 V15 uses its own `.venv` with Python 3.14.7, inside its folder.
