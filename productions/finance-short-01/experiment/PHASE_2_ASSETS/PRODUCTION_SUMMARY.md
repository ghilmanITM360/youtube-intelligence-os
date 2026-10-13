# Production summary: Phase 2 assets

**Final status: `AUDIO_CORRECTION_REQUIRED`.** The asset package is complete and QA'd, but the supplied MP3 pronounces "APR" as "April" at 38.63–39.03 s. Animation timings can't be frozen until a corrected MP3 is supplied and re-aligned (about 10 s of compute with the included scripts).

## Inputs (located and verified)

- MP3: `~/Downloads/TTSOL-en-AU-WilliamMultilingual-20261013-154730.mp3`, SHA256 `f4a9e22d…7b33`. Copied read-only to `audio_analysis/source_audio/`, never edited.
- **Phase 1 recovery:** the experiment folder and ZIP were not in the working tree. The desktop app had stashed them as untracked files during a branch switch at 16:05 (`stash@{0}`, "epitaxy: pre-switch from research/senior-health-complete-local-sync"). Only `finance-short-experiment-01/` and `finance-short-experiment-01.zip` were restored to the working tree (`git restore --source=stash@{0}^3 --worktree`). The stash itself is untouched and still holds its other files. The ZIP and folder are byte-identical.
- Read: README, FINAL_SCRIPT, PRELIMINARY_STORYBOARD, ASSET_REQUIREMENTS, FACT_CHECK, TITLE_OPTIONS, thumbnail SVGs and render code, Visual/Motion DNA, the 27-sequence audit, asset-factory feasibility, and the mortgage-pilot quality review (read-only). No research was repeated.

## Audio results

- 52.728 s; MPEG-1 Layer III; 24 kHz mono; 48 kbps CBR.
- No clipping (peak −2.8 dBFS); −20.6 LUFS (quiet; level it in the mix).
- 0.207 s lead-in, 0.370 s tail, 20 internal pauses, nothing truncated.
- Narration matches the script word for word (140/140) except **APR → "April"**. That's a material error; evidence is in five ASR decodes plus spectrogram/formant analysis.
- 21 measured phrases map 1:1 to 21 shots.

## Beats and shots

12 approved beats → 21 shots (one per measured phrase) → 17 composed hero frames on 6 environment set-ups. Provisional cut frames are in `SCENE_ASSET_MAP.csv`; total length is 1590 frames at 30 fps.

## What was drawn (honest counts)

| Group | Count |
|---|---|
| **Authored base designs** | 84 total: 12 character parts (10 Remy + 2 associate), 23 small face components (6 eyes, 6 brows, 10 mouths, nose), 10 hand drawings, 25 prop designs, 5 environment kits, 6 diagram layouts, 3 typography templates |
| **Characters** | 1 main (Remy, rigged), 1 supporting (store associate, sharing the rig system) |
| **Derived states** | 70: 19 Remy poses + 3 associate poses, 15 + 3 expression heads, 15 prop states (statement, receipt lengths, balance levels, switch, check box, calendar, clock hand, sign), 7 far-side/assembled parts, 8 label pills |
| **Derived layer exports** | 73: 48 diagram layers, 16 environment layers, 7 sofa layers, 2 rest-placed hands |
| **Compositions** | 17 scene hero frames, built only from library instances |
| **Files** | 244 SVG sources, 196 PNG exports, 11 contact sheets, 17 layout JSONs, rig JSONs, manifests. 522 files, 18 MB |

Recolours, mirrored uses and repeated instances are not counted as new art. Far-side limbs are tone variants of the near-side designs.

## Key artifacts

| Path | What it is |
|---|---|
| `CLAUDE_HANDOFF.md` | Rebuild rules, rig maths, shot-by-shot keyframes, handoffs, captions, limits |
| `AUDIO_ALIGNMENT.json` | Measured phrases, provisional word anchors, pronunciation gate |
| `SCENE_ASSET_MAP.csv`, `ASSET_REGISTER.csv` | Shot map and asset register |
| `STYLE_GUIDE.md`, `CHARACTER_BIBLE.md`, `ASSET_QA.md` | Style, identity and QA records |
| `contact_sheets/storyboard_scenes_sheet.png` | The whole Short at a glance |

## Method and provenance

Every artwork was authored as SVG code in `build/`:
- `rig_remy.py`, `rig_associate.py`: characters
- `props.py`, `env.py`, `diagrams.py`, `typography.py`: library
- `scenes.py`: compositions

It renders with the same Sharp/librsvg runtime as Phase 1. There was no paid generation, AI image generation, stock, competitor or brand material, MP4 render or animation. Remy's identity landmarks are ported from the Phase 1 thumbnail code.

## Not done (by instruction)

No animation, no MP4, no replacement voiceover, no narration edits, no changes to the mortgage pilot, YIOS evidence or PRs #21/#25/#28. Nothing was published and no git commit was made; the folder is local and untracked.

## Next steps for the owner

1. Regenerate the MP3 with APR spelled out (`A-P-R` / `A.P.R.`).
2. Review `contact_sheets/remy_expression_sheet.png` to approve the remy-2 hair refinement.
3. Review the storyboard sheet.
4. Authorize the Claude animation phase.
