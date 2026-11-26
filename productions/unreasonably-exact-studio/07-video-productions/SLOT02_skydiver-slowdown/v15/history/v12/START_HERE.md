# Skydiver slowdown · V12 (motion-design re-edit, review cut)

**Watch:**
- [SKYDIVER_SLOWDOWN_V12.mp4](SKYDIVER_SLOWDOWN_V12.mp4): clean version, no burned captions.
- [SKYDIVER_SLOWDOWN_V12_captions.mp4](SKYDIVER_SLOWDOWN_V12_captions.mp4): same film with captions.
- [SKYDIVER_SLOWDOWN_V12.srt](SKYDIVER_SLOWDOWN_V12.srt): subtitle file.

78.2 s · 1080×1920 · 24 fps · −16.4 LUFS. **Status:** private review draft, **not ready to publish** (see [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md)).

**Narration:** the owner's 78.2 s recording, used only as the provisional review narration. It is unconfirmed, and nothing was re-recorded or rewritten.

## What changed from V11

- **Text cut:** no brand label on every shot, no MODEL banner (a small tab instead), no floating "SPEED (your wrist)" inset, no headers or footers on diagrams. Captions are an optional export.
- **Opening (2.5D):** the world camera dollies toward a tiny figure under the aircraft. A near cloud crosses the lens, then the shot cuts behind the faller with a "10 km down" drop line.
- **Character performance (new rig from the Codex V12 partition):** the forearm lifts and the head turns to the wrist (8.4 s, 54.4 s). On "Wait, what?" the head snaps back up, then blinks and nods.
- **Airflow:** "air, relative to you": paths draw on around the body with travelling markers, passing behind it and, at the outer lines, in front.
- **Forces:** grown on one scale from the centre of mass. An in-scene **×30 lens** follows the tips; inside it, the drag tip rises past the weight mark as the model runs, and the net force appears.
- **Equal-time positions:** one descending trail, a mark every 10 s, one scale. Gaps grow, then shrink.
- **Density:** air-sample lenses on an altitude ruler. **Speed ×2 → drag ×4:** one body, coupled arrows.
- **Graph:** builds in place: axes, zero, rise, top speed, a fall that stays above zero. The alternative curves appear only when the narration names other conditions.
- **Audio:** V11 sound retimed. New sleeve rustles on the arm lifts; the wind dips under the lens, trail and graph.

## Deliverables

| File | What |
|---|---|
| [MOTION_DESIGN_RESEARCH.md](MOTION_DESIGN_RESEARCH.md), `research/` | HumanCraft/xkcd principles → V12 decisions; 16-repo review |
| [TOOL_AND_LIBRARY_USAGE.md](TOOL_AND_LIBRARY_USAGE.md) | What was used vs only read (no repo installed or run) |
| [TEXT_REDUCTION_AUDIT.csv](TEXT_REDUCTION_AUDIT.csv) | 39 V11 text items classified, with their V12 treatment |
| [CODEX_ASSET_INTEGRATION_MANIFEST.csv](CODEX_ASSET_INTEGRATION_MANIFEST.csv) | Every Codex V12 file: used or not, why, and its hash |
| [RIG_AND_ATTACHMENT_QA.md](RIG_AND_ATTACHMENT_QA.md) | Rig method, tests (including failures), remaining Codex requests |
| [PARALLAX_LAYER_MAP.md](PARALLAX_LAYER_MAP.md) | Layers and per-shot camera |
| [FULL_SCREEN_VISUAL_STORYBOARD.md](FULL_SCREEN_VISUAL_STORYBOARD.md) | 75 full-size panels (start / development / payoff per shot) |
| `MOTION_DESIGN_PROOFS/` | Proofs A–F: clips and 16-frame strips |
| [SCIENTIFIC_VISUAL_QA.md](SCIENTIFIC_VISUAL_QA.md) | Physics continuity, lens honesty, muted read |
| [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md) | File checks, acceptance criteria, known issues |
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Report for the owner |
| `qa/before_after/`, `qa/V11_vs_V12_overview.png` | Owner V11 screenshots next to V12 at the same moment |

**Editable sources:**
- `tools/v12_shots.py`: shots, camera curves, science graphics, lens, trail, graph.
- `tools/v12.py`: world camera, terrain and render.
- `tools/build_rig.py` and `assets/v12rig/`: character rig.
- `tools/instrument11.py`: wrist dial.
- `tools/mix_v12.py` and `audio/stems/`: audio.
- `timeline/V12_timeline.json`, `timeline/V12.edl`, `SHOT_MANIFEST.csv`: timeline.

## Rebuild (from `v12/`)

Build the rig:

```bash
../v8/.venv/bin/python tools/build_rig.py
```

Run the self-check and render the picture (about 49 s):

```bash
../v8/.venv/bin/python tools/v12.py --check --render
```

Render the transparent caption overlay:

```bash
../v8/.venv/bin/python tools/v12.py --render --out qa/caption_overlay.mov
```

Build the audio stems and both mixes:

```bash
python3 tools/mix_v12.py
```

Mux the clean version:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V12_picture.mp4 -i audio/V12_mix.wav -filter_complex "[1]volume=2dB,alimiter=limit=0.89:level=false[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 78.2 -movflags +faststart SKYDIVER_SLOWDOWN_V12.mp4
```

Burn the caption overlay into the caption version:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V12.mp4 -i qa/caption_overlay.mov -filter_complex "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -c:a copy -movflags +faststart SKYDIVER_SLOWDOWN_V12_captions.mp4
```

Regenerate the storyboard, before/after sheets and proofs:

```bash
../v8/.venv/bin/python tools/boards_v12.py
```

V1–V11 are untouched. Nothing was uploaded or published.
