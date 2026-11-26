# Skydiver slowdown · V10 (review cut)

**Watch:** [SKYDIVER_SLOWDOWN_V10.mp4](SKYDIVER_SLOWDOWN_V10.mp4)

| Property | Value |
|---|---|
| Duration | 78.2 s |
| Resolution | 1080×1920 |
| Frame rate | 24 fps |
| Loudness | −16.4 LUFS |
| Narration | Owner's 78.2 s recording, unaltered |

**Status:** private review draft. **It is not ready to publish.** See [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md).

## What changed from V9

- **Character art:** the Codex image-generated character, aircraft, cloud, close-up and POV-glove art replaces all procedural character art. 65 of the 73 Codex assets are used; the semicircular gauge and its 4 wrist layers are retired.
- **Instrument:** a new circular device from the Codex V10 candidates. It stays on the same right wrist through four shots: side, forearm, close-up and corner card.
- **Science beats rebuilt as single-idea compositions:**
  - large density boxes
  - a same-air comparison
  - force STATES 1 → 2 → 3 on one scale, with a 10× lens on the arrow tips
  - equal-time positions (moving DOWN / net force UP)
  - a readable speed graph
- **Overload removed:** V9's ruler and net-force inset are gone, and nothing small and unreadable is layered over the force scene.
- **Sound:** the V9 sound design is kept and retimed. A rights-clear mix is still provided.

## Narration

There is still only one recording, the 78.2 s one. No newer recording was found. The shorter Slot 02 V2 script remains unrecorded.

**The owner has not decided** which narration to use. Nothing was regenerated or rewritten. The timeline stays editable: `SHOTS` and `MODEL_MAP` live in `tools/v10_shots.py`.

## Deliverables

| File | What |
|---|---|
| [CODEX_ASSET_INTEGRATION_MANIFEST.csv](CODEX_ASSET_INTEGRATION_MANIFEST.csv) | Every Codex file: used or not, which shots, provenance, SHA-256 |
| [CHARACTER_RIG_QA.md](CHARACTER_RIG_QA.md) | Loader, registration, replacement layers, seams, open art issues |
| [INSTRUMENT_CONTINUITY_QA.md](INSTRUMENT_CONTINUITY_QA.md) | Wrist sequence and needle continuity |
| [SCIENTIFIC_ILLUSTRATION_RESEARCH.md](SCIENTIFIC_ILLUSTRATION_RESEARCH.md) | Sources actually examined and principles applied |
| [PHYSICS_VISUAL_VERIFICATION.md](PHYSICS_VISUAL_VERIFICATION.md) | Model rerun and the source of each beat's values |
| [FULL_SCREEN_VISUAL_STORYBOARD.md](FULL_SCREEN_VISUAL_STORYBOARD.md) and `storyboard/panels/` | 82 full-size panels |
| [SHOT_MANIFEST.csv](SHOT_MANIFEST.csv), `timeline/V10_timeline.json`, `timeline/V10.edl` | Editable timeline (source of truth: `tools/v10_shots.py`) |
| [SOUND_DESIGN_CUE_SHEET.csv](SOUND_DESIGN_CUE_SHEET.csv) and `audio/stems/` | 5 stems: VOICEOVER, WIND_AMB, FOLEY, TRANSITIONS, OTHER_SFX |
| `audio/V10_mix.wav` and `audio/V10_mix_rights_clear.wav` | Review mix, and a VO + generated-sound alternative |
| [CODEX_REMAINING_ASSET_REQUEST_V10.md](CODEX_REMAINING_ASSET_REQUEST_V10.md) | Artwork still needed |
| [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md) | Review passes and evidence |
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Report for the owner |

## Rebuild (from `v10/`, using V8's venv plus ffmpeg)

Check the physics model and the timeline, then render the picture:

```bash
../v8/.venv/bin/python tools/model.py
```

```bash
../v8/.venv/bin/python tools/v10.py --check --render
```

Build the stems and the two mixes:

```bash
python3 tools/mix_v10.py
```

Combine picture and mix into the final file:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V10_picture.mp4 -i audio/V10_mix.wav -filter_complex "[1]volume=2dB,alimiter=limit=0.89:level=false[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 78.2 -movflags +faststart SKYDIVER_SLOWDOWN_V10.mp4
```

Regenerate the storyboard panels, shot manifest and timeline:

```bash
cd tools && ../../v8/.venv/bin/python boards_v10.py
```

V1–V9 are untouched; V10 is a separate folder with its own copies of the assets. Nothing was uploaded or published.
