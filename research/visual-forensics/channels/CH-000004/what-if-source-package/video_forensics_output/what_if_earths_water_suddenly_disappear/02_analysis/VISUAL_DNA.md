# Visual DNA — what_if_earths_water_suddenly_disappear

Global, evidence-supported production characteristics. Scene-specific detail lives in `TIMELINE.csv`; this file states only what recurs across the whole video.

## CHARACTER DNA
All human figures are minimal black-outline stick figures (circle head, single-line limbs, no facial features beyond occasional simple marks) — the recognizable "xkcd what if?" house style, consistent with the illustration family used elsewhere in this project. The host (C01) is the only character who recurs across non-adjacent shots (S01, S13, S15); every other character is scene-local.

## ENVIRONMENT DNA
Nine distinct backdrop environments (E01–E09), each confined to its own shot(s), reflecting a genuinely multi-scene explainer rather than a single locked set. All backgrounds are flat line-art with sparse color fill (white/gray/black, plus red used only for warning/danger/branding moments — title card, credits, heat gradient, engulfment rays).

## OBJECT DNA
Small watercraft (sailboat/kayak) and ship/fleet icon marks recur at multiple scales across the beach and depth-scale shots (O02, O05) — the same simple silhouette redrawn larger or smaller depending on the diagram's zoom level. Creature silhouettes (fish/whale/dolphin, O07) are the only object explicitly reused across non-adjacent shots (the S10 jar-diagram sequence and the S16/S17 aquarium epilogue), functioning as a visual callback.

## COLOR PALETTE
Overwhelmingly black-line-on-white/gray, matching this project's other xkcd-style sources. Red is reserved for exactly four purposes: the title card (S02), the runaway-heat gradient (S14), the sun-engulfment rays (S15), and the credits card (S18) — i.e., red consistently marks "branding" or "danger/heat" moments, never ordinary narrative content.

## LIGHTING
Flat, shadowless line-art throughout; no lighting model beyond solid-fill vs. outline. The only "lighting" event is the red gradient wash in S14/S15, which is a color/heat metaphor rather than a literal light source change.

## CAMERA / FRAMING
No physical camera; all "shots" are discrete diagram compositions cut against each other. Every shot uses a single locked framing internally (no pans, no handheld motion) — the only zoom-like event is the S09 zoom-out from the dual-panel depth comparison to the full Mariana Trench profile (A14), which is a diagram-scale transform, not a camera move. 17 of 18 shot boundaries are corroborated by measured `ffmpeg scdet` score spikes (see `00_source/SOURCE_MANIFEST.md`); the 18th is simply the video's natural end.

## COMPOSITION
Two recurring composition templates: (1) the "host" template — a stick figure beside a blackboard occupying the left third of frame, content drawn inside the blackboard on the right two-thirds (S01, S13, S15); (2) the "cross-section" template — a horizontal reference line (sea level or ground level) with a labeled vertical/depth scale, used for every water-level and geological diagram (S04–S09, S14).

## TYPOGRAPHY
Three recurring text systems (T01–T03, see `ASSET_MANIFEST.csv`): a bold Q-card/question style, a bold aside/exclamation caption style (VACUUM, GASP!, WHEEZE!, WORSE? FOR WHO?, Hi!), and a small measurement/chemistry label style (depth numbers, timer values, chemical formulas). All appear to be a single consistent sans-serif family at different weights/sizes rather than distinct fonts.

## GRAPHICS
14 distinct overlay graphics (G01–G14), the largest graphic inventory in this project to date, reflecting the video's greater topical range (drainage physics, marine biology, atmospheric chemistry, geology, astronomy). The "measurement overlay system" (G04: timers, scale bars, depth axes, brackets) is the single most-reused graphic, spanning 6 shots (S05–S10).

## ILLUSTRATION / 3D STYLE
Pure 2D hand-drawn-style vector line art; no 3D, no photographic elements, no camera-realistic lighting or texture anywhere in the video.

## DEPTH
No true depth-of-field or parallax; apparent "depth" in the cross-section diagrams (S04–S09) is communicated entirely through a vertical depth-scale axis and relative object size, not through actual foreground/background blur or layering.

## MOTION LANGUAGE
Motion in this video is dominated by STATE_REPLACEMENT (content swaps: graphics appearing/clearing, fills changing) and SEQUENTIAL continuous changes (fire spreading, gradient intensifying, objects descending) — see `MOTION_EVENTS.csv`. Only two motion events are genuine physical translations of a character/object through space (A03 sailboat capsize, A20 figure+dog+boat departure); everything else is either a value/label change, a fill/color change, or a fade.

## TRANSITION LANGUAGE
Nearly all 18 shot boundaries are hard CUTs. Two exceptions are evidenced by measured near-silence audio gaps and gray full-frame intermediate frames: the S06→S07 boundary (fades to solid gray before the deep-ocean panel appears, corroborated by a measured 58.7–58.9s audio near-silence gap) and the S07 shot's own opening (also preceded by the same fade). No wipes, slides, or other transition types were observed.

## ASSET REUSE PATTERN
Lower overall reuse than `weird_and_worrying_questions` in absolute terms (most graphics/objects/environments are single-shot, reflecting the wide topical range) but higher character/text-system reuse for the recurring "host" device, which structurally bookends and punctuates the video (S01 intro question → S13 mid-video punchline → S15 closing epilogue). The measurement-overlay system (G04) and the underwater cross-section backdrop (E04) are the two most-reused non-character assets (6 and 6 shots respectively... actually E04 spans 4 shots, G04 spans 6 — see `ASSET_MANIFEST.csv` for exact OTHER_APPEARANCES counts).
