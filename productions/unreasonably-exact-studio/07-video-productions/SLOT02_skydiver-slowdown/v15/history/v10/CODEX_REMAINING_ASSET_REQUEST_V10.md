# Codex request: assets still missing after V10 integration

Below are only the items whose artwork itself is the problem. Everything else is handled in animation.

All character parts use the existing canvas, origin and pivots from `rigs/<view>/rig.json`, delivered at 4×.

## Items

### P0
1. **Production-approved front device.**
   - Use the current circular design.
   - Clean alpha, with no hard threshold edges.
   - Separate dial ticks, or confirm the ticks are baked.
   - Separate upper strap, lower strap and buckle.
   - Cap with no stem remnant.
2. **Device in side (edge-on) and oblique views.**
   - Same identity as the front device.
   - Separate housing, dial and needle where the face is visible.
   - Each view needs a needle pivot point.
   - Used for: B1/B2 side wrist, and a future oblique glance shot.
3. **Production-approved forearm (wearer view).**
   - Same sleeve colour as the side suit (#F2EFE5 family).
   - Sleeve extends past the canvas edge, with no straight crop.
   - Wrist centre and forearm axis supplied in JSON.

### P1
4. **Joint-cap repair for the side, three-quarter and back limbs.** Elbows, knees and shoulders should be drawn as sleeve overlaps, not visible discs.
5. **Neutral three-quarter head** matching the side and close-up identity.
6. **Back-view thigh and shin parts** that hold up at ±15°.
7. **Glance head generated on the side canvas**, with no haze.

### P2
8. **Flat-style looking-down terrain and horizon.**
   - Match the character's line and flat-fill style.
   - Supply as separate parallax layers: far haze, mid terrain, river/roads, near clouds.
   - The current painted candidates are more detailed than the characters.

## Not needed

- Scientific diagrams, arrows, graphs and density marks are authored in code from `tools/model.py`.
- The equal-time position ghosts reuse the side rig.
