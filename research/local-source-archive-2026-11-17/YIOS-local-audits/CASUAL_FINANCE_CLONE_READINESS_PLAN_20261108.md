# Casual Finance — clone-readiness plan (owner-approved order, 2026-11-08)

Status: PLAN ONLY. Nothing started. Five-hour usage was ~95% when written; start nothing until usage is at or below ~50%.
Owner standing rules still apply: one video/task at a time, text-only publish, media/frames/images stay LOCAL, no merge, no force push.

## Order
1. Finish 15 -> 20/20, verify with `count_complete.py`, publish scoped text-only checkpoint (see CASUAL_FINANCE_15_TO_20_HANDOFF_PROMPT.md).
2. **Visual asset library** (new, owner request): save a real image for every verified visual change, per video, locally.
3. CHANNEL_DNA synthesis (common vs different patterns across the 20) + **character / environment / graphics model sheets** (new, owner request).
4. **Prompt packs** per asset (character, environment, props, typography, transitions) with consistency anchors; assets generated from them and checked against the sheets.
5. Held-out test: 3-5 videos set aside, rebuild from spec + assets only, blind compare with the originals.
6. Audio capability decision (voice, music, SFX). Until then the clone is visual-only and AV stays BLOCKED.

## Step 2 — Visual asset library (local only)
Path: `~/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/asset_library/`
- `<video_id>/states/`: one full-resolution frame per verified visual state change (new scene, new character pose/expression, new environment, new graphic/text style, new transition type). Source = existing workspace `frames/` and state ledgers; do NOT bulk re-extract.
- `<video_id>/states_index.csv`: file, source PTS + frame index, state id, what changed, source SHA-256 of the MP4, SHA-256 of the image.
- `_channel/`: deduplicated across all 20 videos (perceptual hash, keep best resolution), sorted into `characters/`, `environments/`, `props/`, `graphics_ui/`, `typography/`, `transitions/`, `color_lighting/`.
- `README_FOR_NEXT_AI.md`: tells the next AI to open the images itself, not only read prompts.
- Rules: copies only (originals untouched), SHA-256 verify, no frames on GitHub. A text-only index (CSV + hashes) may be published.

## Step 3 — Model sheets (built from real frames, not imagination)
Every sheet labels each field MEASURED / OBSERVED / INFERRED / UNAVAILABLE.
- **Character model sheet:** front / side / 3-4 / back (only those actually seen; missing = UNAVAILABLE, not invented), expression set, pose set, proportions (head-to-body ratio), line weight, shading and outline rules, outfit and props, measured palette (hex from pixels).
- **Environment sheet:** master establishing shot, layout/geography, recurring props, lighting direction, palette, camera angles used, depth/layer structure.
- **Graphics/typography sheet:** fonts (identified or closest match, flagged as such), sizes, colours, text animation, lower-thirds/charts/UI elements, safe margins.
- **Style bible one-pager:** the rules that stay constant across all 20 videos, plus listed counterexamples.

## Step 4 — Prompt packs
- One prompt file per asset: locked descriptors, reference image path, seed/reference-image instruction, negative prompts, acceptance check (side-by-side with the sheet).
- Consistency anchors: same character descriptors + same reference image in every prompt, same environment master shot for every scene in that location.
- Image/video generation needs an image model tool; Claude here writes specs and checks outputs, the generator is the owner's choice.
- Originality line: the goal is the same visual SYSTEM (style, format, rhythm). Generated assets should be original characters/logos/channel branding in that style, not a 1:1 copy of the source channel's own characters, logo or name.

## Step 5 — Held-out test
Choose 3-5 of the roster videos NOT in the 20, freeze the spec first, rebuild the visuals from spec + assets only, blind-compare against originals (shot rhythm, text timing, palette, character consistency). Report the measured gap. Do not claim "indistinguishable" without this test.

## Honest limits
- Audio is half the identity and is BLOCKED.
- Unseen angles/expressions cannot be documented, only requested as new original assets.
- 20 of 35 roster videos is a sample; counterexamples must be listed.

## PROGRESS 2026-11-08 (evening) — Step 2 frame library BUILT for all four campaigns (local only)
Tools: `tooling/asset_library/{build_states.py (CF), extract_states.py (xkcd|pe|be), dedup_channel.py}`. Run with `tooling/visual-ct-scan-venv/bin/python3 -I` for dedup (needs numpy/PIL).
| Library | Videos | State frames | Unique clusters (RMS<=3.0) | PTS mismatches | Image SHA bad |
|---|---|---|---|---|---|
| CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/asset_library | 19 (gG239LrksH4 pending) | 4,667 | 3,945 (45 span >1 video) | 0 | 0 |
| xkcd-whatif/asset_library | 44 | 5,458 | 2,755 (9) | 0 | 0 |
| primitive-education/asset_library | 15 | 1,915 | 914 (7) | 0 | 0 |
| barely-evolved/asset_library | 3 | 338 | 321 (1) | 0 | 0 |
- Each has `README_FOR_NEXT_AI.md`, `library_manifest.csv`, per-video `states_index.csv`, `_channel/unique_frames*`.
- Rep frame = ledger `rep_frame` (CF) or start+min(3,frames-1) (others; legacy CF Uumnx2Fo6cE same). One frame per state, not every frame.
- xkcd/PE/BE ledgers are VISUAL_ANALYSIS_PARTIAL (audio unverified); BE labels are minimal (descriptions stay in workspace tables).
- NOT done: category sorting (characters/environments/props/graphics_ui/typography/transitions) — needs a viewing pass; Step 3 model sheets; Step 4 prompts/assets; 20/20 publish (other account: gG239LrksH4).
- Not published anywhere: images are local only. Text indexes could be published on owner go-ahead.

## PROGRESS 2026-11-08 (night) — Casual Finance viewing pass + model sheets v0.1 (local only)
- Owner supplied `HumanCraft_Video_Studio_V2_Complete_Guide.pdf` (read in full): clone motion must be built from layered editable assets + authored keyframes, NOT image-to-video; AI stills only if approved; a tested renderer is required before any "video" claim. Applied in `asset_library/_channel/HUMANCRAFT_ALIGNMENT.md`.
- Category tags (rule-based, INFERRED) for 3,945 clusters; 168 (4.3%) viewed in 7 sheets; verdicts in `CATEGORY_AUDIT.md`.
- Model sheets v0.1 for Casual Finance in `_channel/model_sheets/` (two visual layers: white-canvas stick-figure cut-outs vs full-bleed flat-colour scenes; one parameterised stick rig + modifier kit; green-map/coin anthropomorphs; red-marker highlight system; rhythm 0.67-3.3 s median state gap).
- Tools added: `tooling/asset_library/{make_sheet.py, categorize.py, model_sheet_data.py}`.
- NOT done: measured motion curves (frame-by-frame windows per entering class), verified renderer, audio, prompt packs, asset generation (needs owner-approved image model), held-out test; same viewing pass for xkcd / Primitive Education / Barely Evolved; gG239LrksH4 + 20/20 publish remain with the other account.
