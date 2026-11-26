# Skydiver slowdown · V11 (review cut)

**Watch:** [SKYDIVER_SLOWDOWN_V11.mp4](SKYDIVER_SLOWDOWN_V11.mp4)

- 78.2 s, 1080×1920, 24 fps
- −16.4 LUFS
- narration: the owner's 78.2 s recording, unaltered

**Status:** private review draft, **not ready to publish**. See [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md).

**Narration:** the owner has not confirmed it. The 78.2 s recording is used only as the current review-cut narration. Nothing was re-recorded or rewritten.

## What changed from V10 (owner screenshot review)

- **Character:** Codex V11 whole-pose drawings replace the V9 limb rigs, so there are no joint discs and no floating pack.
  - **Repairs:** boot caps painted out; trouser and sleeve colours unified; glance head registered onto the side pose.
- **Instrument:** always on a wrist (arm shot, wrist inset, first-person POV). It has a SLOW→FAST "↓ DOWN SPEED" face drawn in code, replacing the 4-mark clock and long strap.
  - The 0:55 sequence is rebuilt: context → glance → own forearm → push-in, needle falling → tilt to the approaching ground.
- **Terrain:** an irregular field mesh in the Codex landscape palette replaces the checkerboard. The Codex landscape study is used in the opening.
- **Airflow:** "you: moving down" first, then lines that part around the body with upward chevrons.
- **Forces (0:41, 1:08):** common scale → ring on the tips → full-frame "zoomed 30x, not the same scale" card → back to the body, still moving DOWN.
- **Equal-time positions:** a speeding-up column (gaps grow) beside a slowing-down column (gaps shrink).
- **Graph:** labels fixed.
- **Audio:** V10 design retimed. Wind drops under every card, and there are new reveal cues.

## Deliverables

| File | What |
|---|---|
| [V10_SCREENSHOT_DEFECT_AUDIT.md](V10_SCREENSHOT_DEFECT_AUDIT.md) | Each owner screenshot: cause and fix. Images in `qa/before_after/`. |
| [CODEX_REPAIR_INTEGRATION_MANIFEST.csv](CODEX_REPAIR_INTEGRATION_MANIFEST.csv) | Every Codex V11 file: used or not, shots, processing, SHA-256 |
| [CHARACTER_ANATOMY_QA.md](CHARACTER_ANATOMY_QA.md) | Pose repairs, checklist, limitations |
| [INSTRUMENT_MOTION_AND_CONTINUITY_QA.md](INSTRUMENT_MOTION_AND_CONTINUITY_QA.md) | Device, views, speedometer sequence, needle continuity |
| [SCIENTIFIC_VISUAL_QA.md](SCIENTIFIC_VISUAL_QA.md) | Physics progression A–G, zoom card, airflow research, muted read |
| [FULL_SCREEN_VISUAL_STORYBOARD.md](FULL_SCREEN_VISUAL_STORYBOARD.md), `storyboard/panels/` | 90 full-size panels |
| [SHOT_MANIFEST.csv](SHOT_MANIFEST.csv), `timeline/V11_timeline.json`, `timeline/V11.edl` | Editable timeline (source: `tools/v11_shots.py`) |
| [SOUND_DESIGN_CUE_SHEET.csv](SOUND_DESIGN_CUE_SHEET.csv), `audio/stems/` | 5 stems |
| `audio/V11_mix.wav`, `audio/V11_mix_rights_clear.wav` | Review mix, and a VO + generated-only mix |
| [CODEX_REMAINING_ASSET_REQUEST_V11.md](CODEX_REMAINING_ASSET_REQUEST_V11.md) | Art still needed (layered side pose for arm animation, gloves decision, layered wrist) |
| [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md) | 17 passes and acceptance criteria |
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Report for the owner |

## Rebuild (from `v11/`, using V8's venv plus ffmpeg)

Rebuild the repaired poses and glance layer (run from `skydiver-slowdown/`):

```bash
cd .. && v8/.venv/bin/python v11/tools/fix_boots.py && v8/.venv/bin/python v11/tools/recolour.py && cd v11
```

Check the model and continuity, then render the picture:

```bash
../v8/.venv/bin/python tools/v11.py --check --render
```

Build the stems and both mixes:

```bash
python3 tools/mix_v11.py
```

Combine picture and mix:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V11_picture.mp4 -i audio/V11_mix.wav -filter_complex "[1]volume=2dB,alimiter=limit=0.89:level=false[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 78.2 -movflags +faststart SKYDIVER_SLOWDOWN_V11.mp4
```

Regenerate the storyboard panels, shot manifest and timeline:

```bash
cd tools && ../../v8/.venv/bin/python boards_v11.py
```

V1–V10 are untouched. V11 is a separate folder with its own copies of the assets. Nothing was uploaded or published.
