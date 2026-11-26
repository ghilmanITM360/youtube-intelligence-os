# Skydiver slowdown · V15 (final production)

> **Status: OWNER_APPROVED_FINAL** (2026-11-25). V15 is the canonical production master of *Why Can a Skydiver Slow Down Without a Parachute?*
>
> - **Publish with:** the rights-clear master. That is `SKYDIVER_SLOWDOWN_FINAL_V15.mp4`, or the `_CAPTIONS` version, both built from `audio/V15_mix.wav`. Never publish `audio/V15_mix_library_review.wav` or `qa/review/review_library_mix.mp4`: their library clips have no confirmed licence.
> - **Not uploaded:** YouTube upload waits for a separate instruction from the owner.
> - **V13 and V14:** moved to macOS Trash, which is recoverable. See [PROJECT_CLEANUP_REPORT.md](PROJECT_CLEANUP_REPORT.md).
> - **Integrity:** SHA-256 of every project file is in `qa/FINAL_MANIFEST_SHA256.txt`.

## Watch

| File | What |
|---|---|
| [SKYDIVER_SLOWDOWN_FINAL_V15.mp4](SKYDIVER_SLOWDOWN_FINAL_V15.mp4) | Clean version, no captions (publication mix, rights-clear) |
| [SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4](SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4) | Captions burned in |
| [SKYDIVER_SLOWDOWN_FINAL_V15.srt](SKYDIVER_SLOWDOWN_FINAL_V15.srt) | Subtitles (46 cues, Hamza's spoken wording) |
| `qa/review/index.html` | Review page: phone-size player, chapter jumps, low-volume and muted buttons, library-SFX comparison |

110.04 s · 1080×1920 · 24 fps · 2,641 frames · −16 LUFS · AAC 192 kbps.

**To open the review page**, run this from `unreasonably-exact/`:

```bash
python3 -m http.server 8615 --bind 127.0.0.1 --directory skydiver-slowdown/v15
```

Then open http://127.0.0.1:8615/qa/review/

## What changed from V14

See [FINAL_PRODUCTION_QA.md](FINAL_PRODUCTION_QA.md) for the full defect audit.

| Area | Change |
|---|---|
| **Audio** (owner-reported defect) | Bed about 10 dB lower. Ducking under speech is 12 dB for ambience and 9 dB for effects, plus a speech-band carve (1–4.5 kHz, −6 dB more). Voice lightly levelled. Reveal sounds cut from 11 to 5. Separation in voiced windows: median 10.5 → 20.7 dB. See [AUDIO_MIX_QA.md](AUDIO_MIX_QA.md). |
| **Captions** | Raised 126 px (box bottom at 1,626 px, so 294 px clear of the bottom edge). Wrapped as two balanced lines. The 65 s overlap is gone. "Slowing down doesn't mean you have stopped falling" is never split. An automated collision check runs on every cue. |
| **Character** | Mesh deformation on the side rig: knees, boots and wrists move independently, and the clothing ripples. The ripple strength follows the model's drag/weight. Seam-free, and the pack stays rigid. See [CHARACTER_ANIMATION_QA.md](CHARACTER_ANIMATION_QA.md). |
| **Science** | Weight is warm orange. Net force is shown at one magnification, ×8 and labelled: an in-scene lens on the bar tops plus a violet arrow on the body. The full-screen bar push-ins are gone. Air marks thin out with altitude. Airflow builds with the load that makes the drag arrow. See [SCIENTIFIC_VISUAL_QA.md](SCIENTIFIC_VISUAL_QA.md). |
| **Environment** | Farmsteads and villages along the roads. Shaded tree crowns that resolve as the ground approaches. A foreground air-mote layer in front of the faller. |

## Audio stems (`audio/stems/`)

| Stem | Contents |
|---|---|
| `VOICEOVER.wav` | Hamza's narration |
| `AMBIENCE.wav` | Wind bed and distant aircraft |
| `FOLEY.wav` | Cloth, sleeve/strap, wrist ticks, needle |
| `SCIENCE_FX.wav` | Five soft reveal accents |
| `TRANSITIONS.wav` | Camera moves |
| `LIBRARY_REVIEW.wav` | Four SFX Library clips, **review mix only**: licence unknown (see [SFX_LICENCE_MANIFEST.csv](SFX_LICENCE_MANIFEST.csv)) |

There is no music stem: the film has no music.

Mixes:
- `audio/V15_mix.wav`: the publication master, rights-clear
- `audio/V15_mix_library_review.wav`: for listening comparison only

## Other files

| File | What |
|---|---|
| [FINAL_REPORT_ROMAN_URDU.md](FINAL_REPORT_ROMAN_URDU.md) | Owner report |
| [SOUND_DESIGN_CUE_SHEET.csv](SOUND_DESIGN_CUE_SHEET.csv) | Every sound: time, picture event, level, source, rights |
| [NARRATION_VISUAL_SYNC_MAP.csv](NARRATION_VISUAL_SYNC_MAP.csv) | Each spoken line, its key word, and the frame of its visual event |
| [PROJECT_CLEANUP_REPORT.md](PROJECT_CLEANUP_REPORT.md) | V13/V14 dependency audit, isolated rebuild, removal plan |
| `timeline/V15_TIMELINE.json` | Shots, warp, captions and sound cues in film time |
| `research/V15_RESEARCH_NOTES.md` | Sources and the tool review |
| `qa/` | Caption collision CSV, audio metrics, frame strips, rig sheets, build log |
| `HAMZA_VOICEOVER_RAW.mp3` / `HAMZA_VOICEOVER_CLEAN.wav` | Original recording and production narration |
| `history/` | V8–V14 docs and tools, for reference only (not used by the build) |

## Rebuild (from `v15/`)

```bash
zsh tools/build_v15.sh
```

This runs alignment, the physics and rig checks, the picture self-check, the picture and caption renders, the mix, the muxes, the sync map and the timeline. It takes about 5 minutes on this Mac.

Add `--from-voice` to also redo the narration edit and the Whisper transcription. That needs Homebrew `ffmpeg`, `whisper-cli` and Python 3.14; everything else is inside `v15/` (`.venv/`, art, rigs, Whisper model, library-review clips).

Nothing was uploaded or published.

**Verify integrity** (from `v15/`):

```bash
shasum -a 256 -c qa/FINAL_MANIFEST_SHA256.txt | grep -v ': OK$'
```

No output means every file matches. Run it after the build, too: a rebuild rewrites logs and QA images, so those lines differ while the deliverables stay byte-identical.
