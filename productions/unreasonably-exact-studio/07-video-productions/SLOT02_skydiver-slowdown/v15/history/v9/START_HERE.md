# Skydiver slowdown · V9 (review cut)

**Watch:** [SKYDIVER_SLOWDOWN_V9.mp4](SKYDIVER_SLOWDOWN_V9.mp4). It is 78.2 s, 1080×1920, 24 fps, at −16.4 LUFS, and contains the owner's 78.2 s narration plus V9 sound design.

**Status:** a private review draft, not ready to publish. Three things block publication:
1. The character art is a procedural placeholder (see the Codex request).
2. The library SFX are not licence-cleared.
3. The narration version is unconfirmed (see below).

## Narration decision needed

V9 uses the **recorded 78.2 s voiceover** (`audio/narration_preserved.m4a`, matching `v8/FINAL_SCRIPT_OWNER_APPROVED.md`). It is the only recording that exists. The shorter Slot 02 V2 text (`../../revised_scripts_v2/02_short_SCRIPT_V2.md`, 128 words) has **no recording**, so it was not used, and nothing was re-recorded. Please confirm which one you intend. If you choose Slot 02, a new recording is required, and the picture timeline will be retimed from `tools/v9.py` SHOTS and MODEL_MAP.

## Deliverables

| File | What |
|---|---|
| [V8_DEEP_AUDIT.md](V8_DEEP_AUDIT.md) | Independent shot-by-shot audit of V8 (provenance, physics, camera, sound) |
| [PHYSICS_VISUAL_CORRECTION_LEDGER.md](PHYSICS_VISUAL_CORRECTION_LEDGER.md) | The model, and how every beat is drawn |
| [FULL_SCREEN_VISUAL_STORYBOARD.md](FULL_SCREEN_VISUAL_STORYBOARD.md) + `storyboard/panels/` | 68 full-size 1080×1920 panels with START/DEVELOPMENT/PAYOFF/TRANSITION states |
| [SHOT_MANIFEST.csv](SHOT_MANIFEST.csv) · [ASSET_MANIFEST.csv](ASSET_MANIFEST.csv) | Shots, and every asset with its provenance |
| [CODEX_MISSING_ASSET_REQUEST_V9.md](CODEX_MISSING_ASSET_REQUEST_V9.md) | Illustrated assets needed from Codex, with prompts and pivots |
| [RIG_AND_MOTION_MANIFEST.md](RIG_AND_MOTION_MANIFEST.md) | Motion system |
| [SOUND_DESIGN_CUE_SHEET.csv](SOUND_DESIGN_CUE_SHEET.csv) · `audio/stems/` | Cues with rights status; stems VOICEOVER, WIND_AMB, FOLEY, TRANSITIONS, OTHER_SFX |
| `audio/V9_mix.wav` · `audio/V9_mix_rights_clear.wav` | Review mix, and a rights-clear alternative (VO + generated ambience only) |
| `timeline/V9_timeline.json` · `timeline/V9.edl` | Editable timeline (source of truth is `tools/v9.py`) |
| [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md) | 10 review passes, with what was found and fixed |
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Report for the owner |
| `research/REFERENCE_STUDY_V9.md` · `research/xkcd_sheets/` | HumanCraft V4 rules and xkcd What If observations |

## Rebuild

All commands are run from `v9/`. They use V8's venv (cairocffi, CairoSVG, Pillow) plus ffmpeg.

```bash
../v8/.venv/bin/python tools/model.py
```

```bash
../v8/.venv/bin/python tools/v9.py --check --render
```

```bash
python3 tools/mix_v9.py
```

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V9_picture.mp4 -i audio/V9_mix.wav -filter_complex "[1]volume=2dB,alimiter=limit=0.89:level=false[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 78.2 -movflags +faststart SKYDIVER_SLOWDOWN_V9.mp4
```

```bash
../v8/.venv/bin/python tools/boards_v9.py
```

V1–V7 (`~/GhilmanProjects/skydiver-slowdown/`) and V8 are untouched. Nothing was uploaded or published.
