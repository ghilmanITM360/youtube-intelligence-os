# 09 — Production reconstruction intelligence: images, animation, scene graphs, continuity, editing

## Goal

Convert verified evidence into an actionable **NEW ORIGINAL** production blueprint. Reuse abstract techniques and requirements rather than reproducing someone's distinctive characters, original artwork, branded identity or scripts wholesale.

## For EVERY meaningful key visual state (not blindly every identical frame)

**Image / asset-generation brief**:
- Purpose/visual concept; subject+unique original character spec; pose/action/expression; wardrobe/surface; environment (foreground/midground/background); props; layout with normalized x/y/width/height and tolerances when observable; original style vocabulary (shape grammar, stroke, material, palette, typography); camera apparent framing/angle/depth; actual/estimated lighting; readable literal TEXT as source observation (new script uses original text); aspect ratio/resolution; continuity ID, disallowed changes/negative prompt, generation target.
- Source observed frame evidence and confidence. Unknown asset origin should never become "AI generated with exact model X".

**Image-to-video / animation brief**:
- Which objects move, which remain STATIC, first/next/last poses, anchor points, path/velocity, onset/peak/hold/exit timing, anticipation/overshoot/follow-through (conditional), masking/reveal/layer order, camera vs subject motion, background parallax, object permanence, transition in/out, audio cue relation, interpolation strategy only as recommended/proposed.
- Preservation rules: character ID, aspect ratios, lighting direction, environment props, outlines, clothing and typography; no morphing/inconsistent text, no spontaneous extra objects.

**Editor construction**:
- Track/layer map, assets, keyframe/property plan, shot boundaries, SFX/music presence only if actually verified, visual narrative intent, accessibility/caption readability, continuity to preceding/following shot, review frame/time and production QA checklist.

## Visual reconstruction vs exact recreation

From compressed video, underlying layers and curves are non-identifiable without project files. Specify what can be reproduced at the output level and what implementation is only one plausible route. "Exact recreation" must mean evidence-matched composition/output, not unverifiable source timeline or licensed asset reproduction.

## New original sample storyboard state (fabricated example for schema illustration)

`Frame V07`: creator's NEW simple geometric character with open notebook, middle-left x≈0.28, headline on right x≈0.66. Flat navy/cream, circular orange accent, white-space right third. Animation: notebook slides in 0.35s, headline appears at 0.5s, character STATIC. Suggested easing "ease-out-like" from output samples; not claimed original source parameters. No random logos/text substitutions. Proposed SFX pending listening/creative approval.

## Deliverables

- Asset library and design tokens (as **original proposals**).
- `image_prompts.md` and `image_to_video_prompts.md` cross-indexed by visual state ID.
- Storyboard with original scene graph + continuity locks + `do_not_change`.
- Shot-to-shot edit rules / sample timeline project spec.
- 3 variants only when requested or helpful, not 50 filler changes.
- 10–50 prioritized improvements *if specifically requested*, each grounded in evidence, avoiding arbitrary quantity-driven padding.
- Production test checklist: visual identity consistency, typography/captions, native-mobile legibility, exact numerical facts, motion tolerance, audio cues and clip continuity.
