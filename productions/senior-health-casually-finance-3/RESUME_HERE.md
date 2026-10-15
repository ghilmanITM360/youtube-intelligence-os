# Resume here

**Stage: three V2 REVIEW videos rendered (2026-10-15). NOT publication-ready.** No human listening or clinical approval has been given. Do not merge PR #34.

Draft PR: https://github.com/ghilmanITM360/youtube-intelligence-os/pull/34 · Issue #33 · Branch `production/senior-health-casually-finance-three-videos`.

## V2 refinement (current)
| Video | V2 review MP4 | Duration | Cues (min) | Audio |
|---|---|---:|---:|---|
| HIIT | `01_HIIT_AFTER_60/animation/v2/HIIT_After_60_V2_REVIEW.mp4` | 31.133 s | 20 (0.86 s) | Derived paced voice: atempo 0.90 on 0–1.30 s and 0.93 on 2.96–7.37 s, +0.12 s pause. Source hash unchanged. Plan in `animation/v2/VOICE_PACING.json`. |
| Running | `02_RUNNING_AFTER_60/animation/v2/Running_After_60_V2_REVIEW.mp4` | 31.933 s | 17 (0.98 s) | Original voice, unchanged |
| Swimming | `03_SWIMMING_AFTER_60/animation/v2/Swimming_After_60_V2_REVIEW.mp4` | 17.867 s | 9 (0.94 s) | Original voice, unchanged |

**Each `animation/v2/` folder contains:**
- the MP4 + a 540×960 mobile copy
- `CAPTIONS_V2.srt`
- `KEYFRAME_TIMELINE_V2.json`
- `AUDIO_PROVENANCE_V2.json`
- `CAPTION_VERIFICATION.md`
- `CORRECTION_LOG_V1_V2.md`
- `VISUAL_QA_V2.md`, which includes the Casually Finance references and the remaining questions
- `RENDER_QA_V2.json`
- `CONTACT_SHEET_V2.png`
- `CORRECTED_FRAMES_V1_V2.png`

**Shared files:**
- Defect register: `V2_REVIEW/DEFECT_REGISTER_V2.md`
- Wording evidence: `V2_REVIEW/CAPTION_SCORE_RESULTS.txt` (`tools/caption_score.py`)

**Rebuild, one at a time from repo root:**
```
python3 productions/senior-health-casually-finance-3/0X_…/animation/project_v2.py render
```
- **Engine:** `tools/anim_v2.py`.
- **HIIT needs `source_audio/voice_v2_paced.wav`.** It is git-ignored and must be regenerated with `tools/voice_stretch.py` from the plan in `VOICE_PACING.json`, then checked against the sha256 recorded there.
- **V1 is untouched:** `project.py`, `tools/anim.py` and the V1 MP4s still rebuild as before.

## Still blocking publication (V2)
**Listening (human):**
- **HIIT:**
  - "mortality or mobility": both models prefer "mobility" over "morbidity", so it was **not** substituted.
  - "caught" vs "got".
  - "avoided in", corrected from "awarded to".
  - Naturalness of the two stretched spans; revert with `voice=None` if they sound metallic.
- **Running:** "of the blood" (ASR heard "other") and "should" vs "would".

**Clinical:**
- **HIIT:** H4 (absolute cardiologist supervision), H5/H6 (blanket avoidance with CVD).
- **Running:** R3 (broad joint claim), R5 (3 runs a week as a maximum), R7 (VO₂ / "oxygen extraction" terminology).
- **Swimming:** S5 (the joints sentence contradicts itself as spoken, kept verbatim) and the "best exercise" ranking (attributed, no ranking graphic).

**Owner:**
- Phone review of the small supporting labels.
- Rights for the synthesised music/SFX and the supplied audio.

---
## V1 record (superseded by V2 for review, kept unchanged)
### Animation phase V1 (2026-10-15)
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
