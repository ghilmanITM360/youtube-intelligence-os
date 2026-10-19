# Original production blueprint (PRELIMINARY; from 10 validated Casually Finance Shorts)

Purpose: produce **original** vertical explainers in Finance, Senior Health, Medical, History and other topics with comparable timing, structure and communication. This is a method, not a template to copy: use original characters, props, wording and sources. No finished video is made here. Companion files: `KEYFRAME_RECIPE_LIBRARY.md`, `ASSET_CREATION_SPEC.md`, `SCRIPT_TO_VISUAL_DECISION_SYSTEM.md`, `TYPOGRAPHY_AND_LAYOUT_SPEC.md`, `CLAUDE_CODE_ANIMATION_HANDOFF.md`. Everything below is derived from sample statistics (n = 10, depth-mixed) and from `ART_DIRECTION_INFERENCE`; none is a creator statement.

## 1. Format targets (measured in the sample)
| Parameter | Target | Sample evidence |
|---|---|---|
| Length | 55-100 s (Shorts) | 54.7-100.9 s |
| Canvas | 1080x1920 white (render at 720x1280 minimum) | 720x1280 sources |
| Timeline fps | 24 (export 24; if the platform needs 30, repeat every 5th frame) | 24 native Sep-Oct, 24→30 conformed Aug-Sep |
| Hard cuts | 12-24 per minute (scene median 1.7-4.1 s) | median 16/min |
| Visual events (incl. pops) | 40-70 per minute | median 50/min |
| Static frames | 60-90 % | 75 % |
| Words | 165-215 per minute; phrases ~3.6 words/s; pause ~0.3 s every ~4 s | measured |
| Caption | append-by-word at onset +1 frame, chunks of ~5 words | median +33 ms |
| Cut timing | 2-4 frames before the keyword onset | median -80 ms |

## 2. Production pipeline (stages and gates)
1. **Script**: one claim per sentence; write each sentence with its *visual verb* in the margin (see decision system). Gate: every number has a source and a unit.
2. **Voice**: record or synthesise; trim to ~3.5 words/s with 0.25-0.35 s pauses. Gate: human listening (this research could not do it).
3. **Beat sheet**: split the script into scenes at pauses and sentence turns (aim 1.7-4 s per scene). Gate: no scene without a new object, number or reaction.
4. **Asset list**: per scene list characters, props, annotations, screenshots (`ASSET_CREATION_SPEC.md`). Build every asset once as a separate layer; reuse variants.
5. **Layer plan and keyframes**: choose layout (banded vs full-bleed, see typography spec), assign recipes R01-R13 to scenes.
6. **Timeline data**: frame-based keyframes `{frame, target, property, value}` with linear easing by default; hard cuts = scene start frames; pops = visibility at frame n.
7. **Render** deterministic (frame function of time); export 24 fps.
8. **Verify**: run `scripts/forensic_features.py --asr` and `build_video_tables.py` on your own render: cut-to-word offsets (target median -80 ms, within ±150 ms), caption offsets (target within ±100 ms), frame duplicates (none unless intended), static-frame ratio.
9. **Human gates**: listen on a phone, read all captions, verify every number against its source, check meme/brand/photo rights.

## 3. Scene grammar (what a scene is)
A scene = one stage composition reached by a hard cut, then grown by pops/draws/camera moves until the next cut. Maximum one new idea per scene; reaction or analogy scenes are allowed to carry a single character. Three scene types appear throughout: **Evidence** (screenshot/chart + highlight + presenter pop), **Concept** (props popped sequentially), **Reaction/Analogy** (one character or meme-like beat). Typical Short: 13-35 scenes.

## 4. Topic adaptation
| Topic | Characters | Props | Evidence scenes | Notes |
|---|---|---|---|---|
| Finance | country maps, officials, presenter | money bags, bonds, documents, charts | filings, central-bank charts, news pages | Source every number; show date and unit |
| Senior health | presenter, patient figure, clinician | organs (simple), pill, shoe, heart, clock | study abstracts, guidelines | Medical claims need a clinician review; avoid diagnostic imagery without rights |
| Medical | same as above + anatomy props | molecule, scan outline (original), device | trial figures, label text | Evidence highlighting is the key device |
| History | era figures, maps | artefacts, documents, ships | archive pages (public domain), timelines | Use dated timelines as the diagram device |
Existing in-repo successor work (not evidence of the originals): `production/senior-health-casually-finance-three-videos` and `production/finance-short-0*` demonstrate SVG rigs; their documented quality gaps (acting, illustration breadth) apply to anything built from this blueprint.

## 5. Quality gates and known limits
- Do not claim parity with the reference channel: illustration and acting quality require human art direction (see playbook `PILOT_REMOTION/QUALITY_REVIEW.md`).
- Easing evidence is thin; start linear and judge by eye.
- No long-form recipes; long-form pacing is covered only by the earlier Oct-12 corpus (`REFERENCE_SUPPORTED`).
- Audio design is a human task.
