# Claude Code animation handoff (for a separate production agent)

Read first: `ORIGINAL_PRODUCTION_BLUEPRINT.md`, `KEYFRAME_RECIPE_LIBRARY.md`, `SCRIPT_TO_VISUAL_DECISION_SYSTEM.md`, `ASSET_CREATION_SPEC.md`, `TYPOGRAPHY_AND_LAYOUT_SPEC.md`, `OBSERVATIONS_VS_HYPOTHESES.md`. All of them are PRELIMINARY (10 of 48 local videos, Shorts only). Do **not** copy competitor frames or artwork. Do not claim audio knowledge: nothing here was listened to.

## What to build
An original vertical explainer pipeline: script → beat sheet → asset layers → frame-based keyframes → deterministic render → verification against the measured grammar.

## Required architecture (compatible with existing in-repo work)
- A pure function `evaluate(frame)` derives every transform and visibility from absolute frame number (as in `production/senior-health-casually-finance-three-videos` and the playbook's Remotion pilot, `origin/research/casually-finance-success-playbook` `PILOT_REMOTION`). No accumulated per-frame state.
- Timeline JSON: `{"fps":24, "scenes":[{"id","start","end"}], "keyframes":[{"frame","target","property","value","ease":"linear|step|ease_out_quad"}]}`; hard cuts are `step` visibility at the scene start frame; pops are `step` visibility on frame n; strokes use dash offset; camera moves use one parent group scale/translate.
- Layout A (banded) and B (full-bleed) templates from the typography spec; caption layer generated from ASR word times (+1 frame).
- Assets as separate SVG/PNG layers named `CH_*`, `PR_*`, `OV_*`, `SS_*`, `TY_*`, `FX_*`.

## Verification (copy these scripts or call them)
`research/casually-finance-editing-forensics/scripts/`:
- `forensic_features.py <id> <research_dir> <evidence_root> --asr` (note: edit the source lookup if the clip is not in the inventory), `segment_full.py`/`segment_events.py`, `measure_motion.py` (camera/blob/extent/orient), `build_video_tables.py`.
Targets: median cut offset -150..+50 ms vs ASR word onset; caption offsets within ±100 ms; static share 60-90 %; no unintended duplicate frames; every cut changes >= 1000 of 57,600 analysis pixels on a dense scene.

## Python environment note
Use `python3 -E` (user-site numpy/PIL/torch/whisper). Do not use `-I`. ffmpeg 9 requires `-fps_mode passthrough`, not `-vsync`.

## Human gates you cannot pass
Listening, art direction, rights review of memes/logos/photos, financial/medical claim sign-off. Report them as blocked.

## Known gaps to respect
Easing evidence is thin (use linear by default); no long-form recipes; sound design is unknown; the reference channel's rig, tools and labour are unknown; the Oct-12 prior corpus and the Remotion pilot note acting/illustration gaps (`PILOT_REMOTION/QUALITY_REVIEW.md`: acting 2.5/5, illustration 3.0/5 against a 4.0 reference).

## First task suggestion
Build one 60-second original Short in a non-finance topic using recipes R01-R07 and R12-R13, then run the verification scripts and record deviations in a new `PRODUCTION_VERIFICATION.md` (separate branch from this research).
