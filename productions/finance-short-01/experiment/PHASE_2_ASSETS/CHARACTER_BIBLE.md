# Character bible

## Remy: main character (design version remy-2)

An original shopper. Remy is the on-screen actor. The narrator is off-screen, so **Remy never lip-syncs**.

### Locked identity landmarks (geometry, not just colour)

These are ported unchanged from Phase 1 `thumbnail_sources/render.mjs` `shopper()` at offset (+159, +42) in the rig frame:

| Landmark | Rig-frame (RCS) value |
|---|---|
| Face outline | Angular warm-brown face: flat right cheek plane, squared jaw, flat chin (path `FACE` in `build/rig_remy.py`) |
| Ear | Screen-left, outer arc 204–246 x, 186–241 y |
| Eyes | Tall ink ovals rx 7.5 / ry 12.5 at **(303,207)** and **(361,206)**: 58 px spacing; white catchlight upper right |
| Nose | L-stroke `M336 212 L346 236 L329 241`. Never changes |
| Hair | Plum-black curls (`#342A39`) massed high and swept toward screen-right, fringe notch at (362,128), sideburn to (262,204) |
| Wardrobe | Teal sweater with ribbed hem, cream shirt-collar points, cream wrist cuffs, slate trousers, plum-brown shoes with cream soles |
| Skin | `#BB7557`, shade `#9A5940`, highlight `#CC8B6A`, blush `#C96A57` (happy/relieved/content only) |

**Deliberate Phase 2 refinement:** the curl contour is rounder and more evenly scalloped than the spikier Phase 1 sweep, and gains highlight strokes and a fringe shadow. Mass and position are kept, but the silhouette is **not pixel-identical** to the thumbnails. Owner sign-off is required (see `ASSET_QA.md`).

### Proportions and construction

- Rig frame `0 0 640 1060`, ground y = 1030. Total height ≈ 1000 units: about 3.8 heads, a stocky explainer build with a broad sweater torso.
- 21 parts in one rest frame with explicit pivots (`remy_rig.json`, `contact_sheets/remy_rig_pivots_sheet.png`). Joints: hip_c, neck, shoulders, elbows, wrists, hips, knees, ankles.
- Near side (screen-left) uses the base tone; far side uses the shade tone of the same design for depth.
- Faces 3/4 to screen-right. Mirror the whole character to face left. Never mirror the head alone, except as a deliberate glance.

### Pose library (19, `characters/main/poses/`)

`stand_neutral`, `point_forward`, `point_up`, `point_across`, `hold_sheet`, `hold_bill`, `hold_card_up`, `open_hands`, `shrug`, `shocked`, `think_chin`, `drop_coin`, `relieved`, `walk_a`, `walk_b`, `tick_pen`, `circle_marker`, `sit_relaxed`, `sit_notice`. Each pose lists its compatible expressions and story use in `remy_rig.json`.

### Expressions (15) and components

Presets: neutral, curious, intrigued, confused, concerned, worried_talk, shocked, alarmed, relieved, happy, content, focused, determined, skeptical, deadpan.

They're built from 6 eye kinds (open, wide, half, happy, closed, squint), 6 brow sets, 9 mouths, a fixed nose and an optional blush. Gaze shifts both eyes by ≤ 6 px. Head tilt is ±7° around the neck pivot (see `remy_gaze_tilt_sheet.png`).

### Hands (10 drawings)

relaxed, point, fist, open, palm_up, grip_back + grip_front, pen_back + pen_front, release. They're stylised four-finger mittens with distinct thumbs, joined to the wrist under a cream cuff. To hold an object, sandwich it between the *_back and *_front drawings.

### Acting notes by beat

| Beat | Remy's acting |
|---|---|
| Hook | Quizzical shrug, then concern holding the statement |
| B2 | Curious walk-in, intrigued reading |
| B3 | Decisive point at the IF |
| B4 | Skeptical think-chin, then point at "not yet charged" |
| B5 | Determined coin drops, then a relieved exhale |
| B6 | Concern, then shock (no panic) |
| B7 | Skeptical, then walks the timeline |
| B8 | Focused ticking, then concern |
| B9 | Calm open hands ("two different things") |
| B10 | Determined circling |
| B11 | Content on the sofa |
| B12 | Concerned glance at the waiting receipt |

Hold each readable pose at least 12 frames. Concern never becomes panic.

## Store associate: supporting character (assoc-1, B2 only)

**Why the associate exists:** an offer needs someone offering it. The associate gives B2 a real interaction: presenting the sofa and offering the card across the counter. They're a neutral, friendly employee, not a villain.

**Identity:**
- Round face, light olive-tan skin `#D9A27A`.
- Round ink glasses, dark top-bun hair `#2B2230`.
- Sage apron with pocket and a **blank** badge, cream rolled-sleeve shirt, slate trousers, brown shoes.

**System:** the associate uses Remy's skeleton, limb and hand system (recoloured), so motion grammar matches. The silhouette is distinct (bun, glasses, apron).

**Poses:** `assoc_stand`, `assoc_present`, `assoc_offer_sheet`. **Expressions:** content, happy, neutral. Always mirrored to face Remy.

No other supporting characters were created. The script doesn't justify more, and Phase 1 explicitly rejected villain bankers.
