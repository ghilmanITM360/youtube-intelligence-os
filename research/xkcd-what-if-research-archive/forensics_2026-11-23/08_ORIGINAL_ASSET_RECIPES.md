# 08 Original asset recipes, contracts and method choice (continuation, 2026-11-23)

Status: **DRAFT, self-reviewed, not exercised in any production.** Observations about the source channel are from stills I viewed (video ID + timestamp or review cell in `08_SCENE_BREAKDOWN_AND_METHOD_CHOICE.csv`); recommendations are **original production proposals**, kept apart from observations (the CSV has separate "observed" and "chosen_method" columns). No source artwork, script or audio is to be copied, traced or restyled.

## 1. Observed on the viewed stills (10 scenes, 10 videos; plus the 125 style frames)
- All 10 scenes are flat, side-on, 2D. No viewed frame uses vanishing-point perspective or a 3D-lit solid; some use gradients and glow (lightning, explosion) and grey-fill silhouettes. Nothing viewed requires proving 3D or parallax: **none is claimed and none is assumed**.
- Each scene = a small set of independently movable layers (figure, prop, label, divider, symbol) on an empty ground; negative space median 0.66 (long) and 0.77 (Short) (`06_STYLE_ANALYSIS_PHASE62.md`).
- Quantity is carried by a text label, a side-by-side layout or a labelled bracket far more than by to-scale drawing (`07_SCIENCE_VISUAL_PASS.md`: spoken number on screen in about half of the quantity moments).

## 2. Method selection rule (hypothesis, self-reviewed)
Choose by the scientific idea and the storytelling function, cheapest sufficient method first:
| Idea | Method | Use when | Do not use when |
|---|---|---|---|
| a number or ratio with no shape | static diagram + animated label / scale comparison | ratios, magnitudes, "X times" | the idea is a trajectory or a field |
| before / after, A versus B | split panel (2D vector) | two states, same scene | continuous change must be shown |
| a repeated crowd or ring | 2D vector with procedural instancing | many identical symbols | each member must differ |
| a path or geometric solution (sunset, orbit sketch) | 2D vector with a parametric or solved path | an exact geometric answer exists | curvature or 3D lighting changes the answer |
| a character acting | 2D character animation with a short pose set | a gag or an action loop | explaining a mechanism |
| a field or latitude dependence on a sphere | layered 2.5D or 3D globe | the picture must stay correct from several angles | a flat map conveys the same number |
| a trajectory or fluid actually computed | physics simulation (state the model and the time step) | the film claims numerical accuracy | the picture is illustrative: then mark it schematic |
Add 2.5D, 3D or parallax **only** when this table says the idea needs it; never as decoration.

## 3. Asset categories to create (original), with the contract in `08_ASSET_CONTRACT_SCHEMA.json`
1. **Character set**: one construction recipe (ring head, line body, neck, arms, legs; head about 29% of figure height in the observed sample, an observation to compare against, not a mandate), at least 6 original poses (stand, point, hold object, sit at desk, lie down, react), 3 expressions by eye and mouth marks only, stroke width parameter (reference range 4.5 to 8 px at a 1080 px short side), layers: line, fill, accessory. Names are asset IDs, not copies.
2. **Props and environments**: house, desk, chair, board, vehicle, tree, globe, map outline, skyline silhouette, each as grouped layers with pivot and attach anchors and a foreground/background split.
3. **Diagram kit**: axes, brackets, arrows, dividers, equation blocks, numeric labels, a single accent colour for emphasis (observed reference: red; choose and document your own), grey fills for ground and maps.
4. **Scientific markers**: units, ratio labels, "not to scale" notice, source-ID tag linking to the physics sheet (`07_SCIENCE_CLAIM_CHECKS.csv` pattern: claim, assumptions, recomputed value, source, verdict).
5. **Effect elements**: glow, bolt, burst, motion lines, built as separate layers so they can be removed.
Each asset needs: asset ID, layers with z order, anchors, camera-safe canvas, style parameters, science block (quantity, units, equation, assumptions, `to_scale` yes / schematic / partly), motion block (method, anchors used, procedural elements, duration at 24 fps) and a QA block (`UNREVIEWED` until someone reviews it; reviewer kind recorded).

## 4. Limits
Ten scenes only; frames are stills (motion not observed); no hidden software, rigging or simulation method is inferred; none of the contracts was tested by building an asset; physics status is carried from `07_SCIENCE_CLAIM_CHECKS.md` where a claim was checked and is otherwise NOT_VERIFIED.
