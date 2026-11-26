# Skydiver slowdown · V14: Hamza's narration

**Watch:**
- [SKYDIVER_SLOWDOWN_V14_HUMAN_VOICE.mp4](SKYDIVER_SLOWDOWN_V14_HUMAN_VOICE.mp4): clean version
- [SKYDIVER_SLOWDOWN_V14_CAPTIONS.mp4](SKYDIVER_SLOWDOWN_V14_CAPTIONS.mp4): with captions
- [SKYDIVER_SLOWDOWN_V14.srt](SKYDIVER_SLOWDOWN_V14.srt): subtitles

110.04 s · 1080×1920 · 24 fps · 2641 frames · −16.0 LUFS.

**Status:** private review cut. Nobody has watched it in a player or listened to it yet (see `FINAL_SYNC_QA.md`). V13 is unchanged.

## What V14 is

V14 is V13's picture, re-timed to Hamza's recording. The characters, the opening composition and the science scenes are V13's.

**How the re-timing works:**
- Each of Hamza's phrases is matched to the same phrase in the V13 narration.
- Every shot, camera move and reveal is placed where that phrase now falls. This is a smooth, per-phrase time map in `audio/warp.json`, not one speed factor.
- Background motion keeps running at real speed even where a beat is stretched: body bob and roll, air streaks, flow markers and the propeller.

**Changes beyond the re-timing:**
- "this is a model" brings in the model's speed-time graph inside the MODEL frame. The graph stays for "change the posture or the conditions".
- "posture: fixed" appears when Hamza says "body position stays fixed".
- The drag bar passes the weight line on "stronger".
- "starts at rest" appears on "starting from rest", not before it.
- The speed ×2 sweep starts on "the faster you fall".
- The end card has a slow push, so the last 1.3 s is not a held frame.
- **Sound is rebuilt and fully generated.** Wind, aircraft, cloth, wrist ticks, needle, whooshes and reveal tones are all made in `tools/mix_v14.py`. No library clips are used, so the mix is rights-clear.

## Deliverables

| File | What |
|---|---|
| `HAMZA_VOICEOVER_RAW.mp3` | Original recording (unchanged copy) |
| `HAMZA_VOICEOVER_CLEAN.wav` | Production narration; edit list in `audio/voice_edit.csv` |
| [HUMAN_VOICE_TRANSCRIPT.md](HUMAN_VOICE_TRANSCRIPT.md) | Verified transcript, edits, differences from the script |
| `WORD_LEVEL_TIMESTAMPS.json` | 202 words: film, clean and raw times, emphasis estimate |
| `NARRATION_VISUAL_SYNC_MAP.csv` | Brief's table: each line, its words and the frame of its visual event |
| `SOUND_DESIGN_CUE_SHEET.csv` | Every sound: time, linked picture event, level, source |
| `V14_TIMELINE.json` | Shots in V14 time, the warp, captions, sound cues |
| [FINAL_SYNC_QA.md](FINAL_SYNC_QA.md) | Checks and results |
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Owner report |
| `history/v13/` | V13 docs, timeline and tools, for reference |

## Rebuild (from `v14/`)

V14 is self-contained: `.venv/`, art, rigs, the Whisper model (`tools/whisper_models/`), and V13 references in `history/v13/`. System tools needed: Homebrew `ffmpeg`, `whisper-cli` and Python 3.14.

Edit the narration (trim the pre-roll, cap long pauses, process):

```bash
.venv/bin/python tools/prepare_voice.py
```

Make a 16 kHz copy for transcription:

```bash
ffmpeg -y -i HAMZA_VOICEOVER_CLEAN.wav -ar 16000 -ac 1 qa/asr/clean16k.wav
```

Transcribe with word timings:

```bash
whisper-cli -m tools/whisper_models/ggml-small.en.bin -f qa/asr/clean16k.wav -ml 1 -sow -ojf -of qa/asr/clean_words --dtw small.en -l en -np
```

Build word, phrase and sentence timings, the captions, the SRT and the time map:

```bash
.venv/bin/python tools/align_v14.py
```

Run the self-check and render the picture:

```bash
.venv/bin/python tools/v14.py --check --render
```

Render the caption overlay:

```bash
.venv/bin/python tools/v14.py --render --out qa/caption_overlay.mov
```

Build the stems and the mix:

```bash
.venv/bin/python tools/mix_v14.py
```

Mux the clean version:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V14_picture.mp4 -i audio/V14_mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t 110.0417 -movflags +faststart SKYDIVER_SLOWDOWN_V14_HUMAN_VOICE.mp4
```

Burn in the captions:

```bash
ffmpeg -y -i SKYDIVER_SLOWDOWN_V14_HUMAN_VOICE.mp4 -i qa/caption_overlay.mov -filter_complex "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -c:a copy -movflags +faststart SKYDIVER_SLOWDOWN_V14_CAPTIONS.mp4
```

Write the sync map and the timeline:

```bash
.venv/bin/python tools/sync_map_v14.py && .venv/bin/python tools/timeline_v14.py
```

**To pin a reveal to a word:** add it to `EVENTS` in `tools/align_v14.py`, then rerun from that step.

Nothing was uploaded or published.
