# Codex request: what V11 still needs from the artwork

V11 animates whole-pose drawings, so no rig joints are visible. The remaining character gap is **limb animation**: no arm lift, no hand activity. Closing it needs layered parts.

## P0
1. **Layered side pose**, from the same drawing as `character/side/boot_revision_reference.png`:
   - separate near arm (upper arm, forearm, hand) with sleeve-overlap art at the shoulder and elbow
   - separate head and neck
   - the rest of the body as one piece
   - pivots in JSON; no circular caps
   - boot tops closed (V11 paints these out in code: `tools/fix_boots.py`)
2. **Gloves decision.** Either bare hands everywhere (as in the side and wrist art) or grey gloves everywhere (as in three-quarter and back). Redraw the views that don't match.
3. **Wrist art, layered:**
   - sleeve + hand
   - strap (separable so it can move)
   - housing
   - face ring
   - Keep the face blank: the scale is drawn in code.
   - Supply the face centre and radii in JSON.

## P1
4. **Three-quarter view of the device on the wrist**, for an oblique glance shot.
5. **V11-style expressive close-up face**: eyes, brows, blink, open mouth. It replaces the V9 close-up used in C1.
6. **Neutral three-quarter face** (the current one is slightly smiling).

## P2
7. **Low-altitude terrain detail sheet** for the 1–4 km shots: farm tracks, hedges, small buildings in the flat style, as separate sprites.
8. **Landscape parallax layers** for the A1 horizon: far haze, fields, river/road, near clouds.

## Not needed
- **Scale, labels, needle:** drawn in code.
- **Diagrams, arrows, flow lines:** drawn in code.
- **Standalone device studies:** not used. V11 never shows the device off a wrist.

**Ready-to-send brief with reference images:** [codex_request/CODEX_V12_ART_BRIEF.md](codex_request/CODEX_V12_ART_BRIEF.md)
