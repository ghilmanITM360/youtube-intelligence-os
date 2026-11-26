# V15 project consolidation and cleanup

## 1. Dependencies on V13 and V14

V15 started as a copy of `v14/`, which was already self-contained. That copy excluded V14's renders, its QA scratch and its old stems. Everything V15 needs is inside `v15/`:

| Needed by the build | Where it lives in V15 |
|---|---|
| Python environment | `.venv/` (its `pyvenv.cfg` points to Homebrew Python 3.14, not to v13/v14) |
| Codex art packages (V11/V12/V13), rigs, assets | `CODEX_*`, `rigs/`, `assets/` (+ `assets/codex/aircraft_side_v15.png`) |
| Narration | `HAMZA_VOICEOVER_RAW.mp3`, `HAMZA_VOICEOVER_CLEAN.wav` (SHA-256 identical to V14's copies) |
| Whisper model and transcription | `tools/whisper_models/`, `qa/asr/` |
| V13 reference timing (used by the word-matching warp) | `history/v13/narration_words.json`, `history/v13/narration16k.wav` |
| Library-review SFX clips | `audio/library_review/` (copied from `SFX Library/`; the build does not read the library folder when these exist) |
| V14 docs and tools, for reference | `history/v14/` |

A scan of `tools/`, `rigs/`, `assets/` and `audio/*.json` for `v13/`, `v14/` or `../` paths found only one stale comment, which was fixed. No symlinks point outside `v15/`.

## 2. Isolated rebuild

`v15/` was copied, without its outputs, into an empty folder in the session scratchpad. No `v13/`, `v14/` or `SFX Library/` was reachable from there. Then `zsh tools/build_v15.sh` ran from that copy, taking 3 min 04 s.

**Result:** all 8 checked files are byte-identical to the originals (`qa/isolated_rebuild.txt`):

| File | SHA-256 |
|---|---|
| SKYDIVER_SLOWDOWN_FINAL_V15.mp4 | `2cb6ece9…0346` |
| SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4 | `e74410fd…351d` |
| SKYDIVER_SLOWDOWN_FINAL_V15.srt | `847ae01d…46c5` |
| audio/V15_mix.wav | `da43f26a…fd6b` |
| audio/warp.json | `56040bb5…dfba` |
| audio/narration_v14.json | `6156a93c…c500` |
| HAMZA_VOICEOVER_RAW.mp3 | `edd24139…c82f` |
| HAMZA_VOICEOVER_CLEAN.wav | `ed4d9c3f…d2c4` |

Full hashes are in `qa/checksums_v15.txt`.

The scratch copy was deleted afterwards.

A second isolated rebuild ran on 2026-11-25 after owner approval, just before the removal. It produced the same 8 files, byte for byte. It also reproduced the 6 stems, the library-review mix and the review MP4 identically. Details are in `qa/isolated_rebuild.txt`.

## 3. Removing V13 and V14: **done 2026-11-25 18:22**

The owner approved V15 as OWNER_APPROVED_FINAL. Only then were the two folders moved, with Finder's Move to Trash.

| Folder | Size | Now |
|---|---|---|
| `skydiver-slowdown/v13/` | 1.0 GB (1,062,380 KB) | macOS Trash |
| `skydiver-slowdown/v14/` | 1.1 GB (1,172,328 KB) | macOS Trash |

**Trash was not emptied.** Nothing was permanently deleted.

**To recover:** open Trash, select `v13` or `v14`, and choose **Put Back**. The folder returns to `skydiver-slowdown/`.

**Checked after the move:**
- `skydiver-slowdown/` contains only `v15/`.
- The `tools/v15.py --check` and `cloth_warp.py` self-checks pass.
- All 8 recorded checksums match.
- The captioned MP4 decodes with 0 errors.

**Also changed:**
- The `v13-review` entry is removed from the project-root `.claude/launch.json`. Only `v15-review` remains.
- Two stale "run from v14/" comments in `tools/align_v14.py` and `tools/prepare_voice.py` now say v15/.

**Note:** `skydiver-slowdown/v15.zip` (876 MB, created 18:16) was already in Trash before this cleanup. This cleanup did not move it.
