# Rebuild instructions: Slot 07 V3

Run every command from this folder: `07-video-productions/SLOT07_lunar-laser-ranging/`. Paths inside the project are relative. The project does not read anything from outside its own folder, except for the dependencies listed in §1.

## 1. External dependencies (not in the project)

| Dependency | Version (verified 2026-11-26) | How to recreate |
|---|---|---|
| Python virtual env `~/.venvs/uepipe` | Python 3.13.15 (uv-managed) | `uv venv ~/.venvs/uepipe --python 3.13 && ~/.venvs/uepipe/bin/python -m pip install -r tools/requirements_uepipe.txt` |
| Python packages | numpy 2.5.5, pillow 13.0.0, scipy 1.18.1, opencv-python-headless 5.1.0.95, aggdraw 1.4.1 | `tools/requirements_uepipe.txt` |
| ffmpeg / ffprobe on PATH | 9.0.1 (Homebrew) | `brew install ffmpeg` (the build has no `drawtext`; contact sheets use `tools/contact_sheet.py`) |
| macOS system fonts | `/System/Library/Fonts/Menlo.ttc` (numbers), `/System/Library/Fonts/Supplemental/Arial Bold.ttf` (formula maths face, caption tool labels) | ship with macOS; not redistributable, so not copied |
| Codex CLI (only to regenerate artwork) | `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex` 0.171.0-alpha.13.2 | see `../../02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md` |

The fonts (Comic Neue, OFL) and the music are inside the project: `assets/fonts/` and `audio/music/Small_Variables.mp3`. The music was copied into the project on 2026-11-26. Until then `tools/sound_design_v3.py` read it from the workspace root.

## 2. Full rebuild (about 15 minutes on this Mac)

Steps a–c **overwrite the locked V3 renders**. Run them only in a copy of the project, or after the owner explicitly asks for a re-render. To check reproducibility, use §3 instead.

```bash
P=~/.venvs/uepipe/bin/python
$P animation/selftest.py                                   # science + geometry asserts
$P animation/roughcut.py --scale 1.0                      # a. picture: renders/roughcut_v3/SLOT07_V3_clean.mp4 (~13 min)
$P animation/roughcut.py --range 75.0 78.2 --scale 1.0    #    the two V3 patches (precision beat, formula),
$P animation/roughcut.py --range 81.6 88.1 --scale 1.0    #    spliced at frames 2250/2346/2448/2643 (FINAL_PRODUCTION_QA.md)
$P tools/sound_design_v3.py                                # b. music edit, automation, SFX, stems, both mixes
bash tools/finish_v3.sh                                    # c. grade, PREMIUM (music review) + RIGHTS_CLEAR masters, captions, SRT
```

The patch splice was done by hand in the V3 session, using a frame-accurate ffmpeg concat at the frames listed above. If a fresh full render includes the patched code, as the current source does, the patches are already in it and no splice is needed.

## 3. Reproducibility check (non-destructive): run 2026-11-26

```bash
~/.venvs/uepipe/bin/python tools/rebuild_check.py "$PWD" /tmp/slot07_rebuild after
```

This renders 19 stills (0:01.5 to 1:34) from the current scene code at full resolution. It compares each one with the same frame decoded from the locked `renders/roughcut_v3/SLOT07_V3_clean.mp4` and logs every file the code opens.

**Result** (`qa/REBUILD_CHECK_2026-11-26.json`):
- **Frame match.** Mean absolute difference is 1.38–1.88 /255 on all 19 frames, which is the H.264 encoding error. The values are identical before and after the project moved to `07-video-productions/`.
- **Files read.** The code opened 80 files, all inside the project. It also read the Python environment and the two macOS fonts. No temporary directory, and no path outside the project.

## 4. Self-checks that must still pass after any change

- `animation/selftest.py`
- The proof checks in `renders/proofs/*/PROOF_REPORT.md`, re-run with `animation/render_proofs.py <ID>`
- The V3 scene checks:
  - opening: no static hold at 2–4 s;
  - G22: only the detected photon enters the telescope;
  - G37: Moon–Earth clearance ≥ 216.
