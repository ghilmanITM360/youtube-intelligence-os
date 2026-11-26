# Skydiver slowdown · V13 (opening restored, science simplified): review cut

**Watch:**
- [SKYDIVER_SLOWDOWN_V13.mp4](SKYDIVER_SLOWDOWN_V13.mp4): clean version
- [SKYDIVER_SLOWDOWN_V13_captions.mp4](SKYDIVER_SLOWDOWN_V13_captions.mp4): with captions
- [SKYDIVER_SLOWDOWN_V13.srt](SKYDIVER_SLOWDOWN_V13.srt): subtitles

78.2 s · 1080×1920 · 24 fps · −16.4 LUFS.

**Status:** private review draft, **not ready to publish**. The narration is the owner's provisional recording.

## What changed from V12

- **Opening** (`OPENING_V10_V11_V12_V13_COMPARISON.md`): V11's composition is back. The aircraft is upper-middle with the figure below it. The camera establishes, follows, then approaches, with four parallax layers. There is no cloud wipe; the shot cuts straight to the closed pack.
- **Airflow:** you move down through still air. The camera then holds you and the air streams up past you. Only then does the drag arrow appear.
- **Density:** two equal boxes, thin vs denser air. Then the same speed under each box gives more drag in the denser air.
- **Speed:** "same air · same posture" box; speed ×2 → drag ×4.
- **Forces:** the ×30 lens is gone. The forces grow to equal ("balanced: still falling"). Bars side by side on one scale show the drag bar passing the weight line; the excess turns violet (net force up) and the camera pushes in to show it.
- **Captions:** Whisper (whisper.cpp) plus voice detection. 48 short cues, 0 overlaps (V12 had 1 overlap and a 131-character cue).
- **Sound:** the wind follows the fall, not the graphics. Cues moved to the new reveals.
- **Codex V13 art:** bare hands used on the back pose. Elbow folds and neck art rejected (tested, defects remain).

## Deliverables

| File | What |
|---|---|
| [OPENING_V10_V11_V12_V13_COMPARISON.md](OPENING_V10_V11_V12_V13_COMPARISON.md) | Version comparison and the new opening stages. Sheet: `qa/OPENING_V10_V11_V12_V13.png` |
| [SCIENTIFIC_VISUAL_RESEARCH.md](SCIENTIFIC_VISUAL_RESEARCH.md) | NASA / Physics Classroom / image reference ledger (`research/screens/`); library reassessment |
| [SCIENTIFIC_MOTION_QA.md](SCIENTIFIC_MOTION_QA.md) | Model checks, beat-by-beat motion check, muted review |
| [CODEX_V13_INTEGRATION_MANIFEST.csv](CODEX_V13_INTEGRATION_MANIFEST.csv) | Every Codex V13 file: used or not, evidence, sha256 |
| [CAPTION_SYNC_QA.md](CAPTION_SYNC_QA.md) | Alignment method and checks; per-cue table in `qa/asr/caption_alignment.csv` |
| [SOUND_DESIGN_QA.md](SOUND_DESIGN_QA.md) | Mix changes, measurements, licence status |
| [FULL_SCREEN_VISUAL_STORYBOARD.md](FULL_SCREEN_VISUAL_STORYBOARD.md) | 75 full-size panels |
| `MOTION_DESIGN_PROOFS/` | Proofs A–F (clips and strips) |
| [FINAL_VISUAL_AND_AUDIO_QA.md](FINAL_VISUAL_AND_AUDIO_QA.md) | File checks, checklist, known issues |
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Report for the owner |

**Editable sources:**
- `tools/v13_shots.py`: shots, camera curves, opening layers, airflow, density, bars
- `tools/v13.py`: renderer and captions
- `tools/build_rig.py` with `assets/v12rig/RIG.json`: rig
- `assets/v13reg/`: bare-hand poses
- `tools/mix_v13.py`: audio; stems in `audio/stems/`
- `tools/align_captions.py`: captions
- Timeline: `timeline/V13_timeline.json`, `timeline/V13.edl`, `SHOT_MANIFEST.csv`

## Rebuild (from `v13/`)

V13 is self-contained (v8–v12 were removed; see `CLEANUP_AND_CONSOLIDATION_REPORT.md`):
- `.venv/`: Python 3.14 environment (packages in `requirements.txt`)
- `audio/sfx_library_used/`: the 8 library clips the mix uses
- `CODEX_V12_ART_PACKAGE/` and `codex_request/`: rig source art for `tools/build_rig.py`
- `qa/reference/opening_frames/`: V10–V12 frames for the opening comparison
- `history/`: earlier versions' docs, manifests and prompts

System tools needed: Homebrew `ffmpeg`, `whisper-cli`, and Python 3.14.

The Whisper model `tools/whisper_models/ggml-small.en.bin` is about 466 MB.

Make a 16 kHz mono copy of the narration:

```bash
ffmpeg -y -i audio/narration_preserved.m4a -ar 16000 -ac 1 qa/asr/narration16k.wav
```

Transcribe it with word timings:

```bash
whisper-cli -m tools/whisper_models/ggml-small.en.bin -f qa/asr/narration16k.wav -ml 1 -sow -ojf -of qa/asr/narration_words --dtw small.en -l en -np
```

Build the caption cues and the SRT:

```bash
.venv/bin/python tools/align_captions.py
```

Run the self-check and render the picture:

```bash
.venv/bin/python tools/v13.py --check --render
```

Render the transparent caption overlay:

```bash
.venv/bin/python tools/v13.py --render --out qa/caption_overlay.mov
```

Build the audio stems and both mixes:

```bash
python3 tools/mix_v13.py
```

Mux the clean version:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V13_picture.mp4 -i audio/V13_mix.wav -filter_complex "[1]volume=2dB,alimiter=limit=0.89:level=false[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t 78.2 -movflags +faststart SKYDIVER_SLOWDOWN_V13.mp4
```

Burn the caption overlay into the caption version:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V13.mp4 -i qa/caption_overlay.mov -filter_complex "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -c:a copy -movflags +faststart SKYDIVER_SLOWDOWN_V13_captions.mp4
```

Regenerate the storyboard, comparisons and proofs:

```bash
.venv/bin/python tools/boards_v13.py
```

V1–V12 are untouched. Nothing was uploaded or published.
