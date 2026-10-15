# Resume here

**Stage: three V1 REVIEW previews rendered (owner review). NOT publication-ready.** No human listening or clinical approval has been given. Do not merge PR #34.

Draft PR: https://github.com/ghilmanITM360/youtube-intelligence-os/pull/34 · Issue #33 · Branch `production/senior-health-casually-finance-three-videos`.

## Animation phase (2026-10-15)
| Video | Preview | Duration | Scenes | Layer tracks | Unique assets | SFX |
|---|---|---:|---:|---:|---:|---:|
| HIIT | `01_HIIT_AFTER_60/animation/HIIT_After_60_V1_REVIEW.mp4` | 30.567 s | 8 | 37 | 14 | 11 |
| Running | `02_RUNNING_AFTER_60/animation/Running_After_60_V1_REVIEW.mp4` | 31.933 s | 8 | 45 | 14 | 13 |
| Swimming | `03_SWIMMING_AFTER_60/animation/Swimming_After_60_V1_REVIEW.mp4` | 17.867 s | 6 | 59 | 7 | 5 |

Each video's `animation/` folder contains:
- the full and mobile (540×960) MP4s
- `project.py`, the editable scene, layer and keyframe data
- `KEYFRAME_TIMELINE.json`
- `CAPTIONS_REVIEW.srt`
- `AUDIO_PROVENANCE.json`
- `CONTACT_SHEET.png`
- `VISUAL_QA_V1.md`
- `qa/RENDER_QA.json`
- `raster/`: 3× PNGs of the package's own SVGs, committed so a clone does not need Sharp

## Rebuild (from repo root, one at a time)
```
python3 productions/senior-health-casually-finance-3/01_HIIT_AFTER_60/animation/project.py render
python3 productions/senior-health-casually-finance-3/02_RUNNING_AFTER_60/animation/project.py render
python3 productions/senior-health-casually-finance-3/03_SWIMMING_AFTER_60/animation/project.py render
```
- **Needs:** Python 3 with Pillow and numpy, ffmpeg, the macOS fonts Chalkboard SE and Arial, and each package's `source_audio/original_audio.m4a`. The audio is git-ignored; take it from `delivery/*.zip` and check it against `AUDIO_TRANSFER_MANIFEST.json`.
- **Bounded checks:** `project.py test A B` renders the window from A to B seconds, and `project.py still t…` writes PNG stills.
- **Engine:** `tools/anim.py`. Set `REVIEW_MARKS = False` only after owner and clinical sign-off.

## Still blocking publication
- **HIIT:**
  - H4 (13.4–16.2 s): "expert cardiologist" supervision is stated absolutely.
  - H5 (16.2–21.3 s): "mortality or mobility", which may be "morbidity".
  - H6 (21.3–24.3 s): the ASR heard either "avoided" or "awarded".
- **Running:**
  - R3: a broad joint-problem claim, and the ASR garbled "muscular scuttle".
  - R5: a universal limit of 3 runs per week.
  - R7: the VO₂ / "oxygen extraction" terminology.
- **Swimming:** S5, the contradictory joints sentence. The "best exercise" ranking (S2/S3) is shown without ranking visuals.
- **Owner decisions:**
  - Listen to every video end to end, confirm the caption wording and the cue timing (taken from ASR word times), and review playback on a phone.
  - Decide on rights for the synthesised music and SFX, and confirm the rights to the supplied audio.

Source and reference originals are read-only. The unrelated untracked `finance-short-02-visual-calibration/`, `research/` and `productions/dr-rehan-…/`, and the stash, are preserved.
