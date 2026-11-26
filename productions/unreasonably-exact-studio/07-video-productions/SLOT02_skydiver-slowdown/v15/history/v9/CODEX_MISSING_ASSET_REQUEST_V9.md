# Codex missing-asset request — V9

**Why this exists:** a provenance audit of V1–V8 found that **no character or equipment artwork was ever image-generated**. Every part was drawn by code (Pillow PNGs in V1–V6; Bézier SVGs from `build_rigs.py` in V7/V8). V9 still uses those procedural SVGs as **placeholders**. The owner's illustrated-asset requirement is **not yet satisfied**.

Claude does the procedural animation, airflow, forces, camera, terrain and editing. Codex supplies the complex illustrated artwork below. Request only what the V9 storyboard actually uses.

## Shared requirements for every character asset

- **Style:** original hand-drawn scientific illustration. Thin natural charcoal outline (#272822, slightly irregular), flat fills, minimal face (dot eyes behind goggles, small mouth), no gloss, no gradients. Restrained colour: suit warm paper #F2EFE5, trousers grey-green #D6D7CB / far side #ACAEA3, straps #535852, skin #F4E5CC. The closed container is the single accent, tan #BC9A77 with a paler stitched flap. Spirit: xkcd-What-If-adjacent simplicity. Do **not** copy xkcd characters or frames.
- **Identity** (must match across views): adult skydiver, rounded helmet with one broken highlight, broad goggle band, jumpsuit, chest strap and leg-strap harness, **closed** container high on the back (never a deployed canopy), no visible handles or deployment devices called out.
- **Delivery:** transparent PNG at 4× (2560×1600 for 640×400 canvases), plus layered PSD or SVG if possible. Every part file uses the **same full canvas and origin** as its view's `rigs/<view>/rig.json` (640×400), so existing pivots still work. Parts overlap 8–12 px past each joint so rotation never opens a gap.
- **Reference:** current placeholder geometry is `review/character_turnaround.jpg` in V8 and `rigs/<view>/rig.json` (pivots and paint order). Keep the same proportions and pivots unless you supply a new rig.json.

## Requests (priority order)

| Asset ID | Shot IDs | Purpose | Viewpoint | Components (separate transparent files) | Pivots / attachment | Expected path | Priority |
|---|---|---|---|---|---|---|---|
| CH-01 | B1, D1, F1–M1, Q1–Q2, R1 | Main side tracking character (model section, held posture) | Side, nose right, belly-to-earth arch | torso, pack, head (helmet+goggles), near/far upper_arm, forearm, hand, near/far thigh, shin, foot (15) | Use `rigs/side/rig.json` pivots: shoulder 380,205 / elbow 427,259 / wrist 493,244 / hip 262,226 / knee 189,253 / ankle 141,185; pack parented to torso | `v9/assets/codex/side/*.png` | **P0** |
| CH-02 | E1 | Three-quarter airflow shot | 3/4 front-left | same 15 parts | `rigs/three_quarter/rig.json` | `v9/assets/codex/three_quarter/*.png` | P1 |
| CH-03 | A2, P1 | Rear view, closed container is the subject | From above and behind | torso, pack (trapezoid flap, closure, pocket seam), head (rear dome, goggle strap), 12 limb parts | `rigs/back/rig.json` | `v9/assets/codex/back/*.png` | **P0** |
| CH-04 | C1 | Reaction close-up | Front, chest-up | torso/harness, head, eyes (pair), lids (closed pair), brows, mouth (neutral + slightly open) | `rigs/closeup/rig.json`; eyes translate ±6 px | `v9/assets/codex/closeup/*.png` | P1 |
| CH-05 | B2, N1 | Wrist instrument insert from the wearer's view | First person, right forearm entering from lower right, glove upper left | sleeve/forearm, cuff, glove (open relaxed hand), instrument strap | Dial centre sits on the wrist top; supply that point in a JSON | `v9/assets/codex/wrist/*.png` | **P0** |
| CH-06 | O1 | Looking-down POV | First person, both gloves at the bottom corners, palms down | left_glove, right_glove (cuffs crop at frame edge) | Pivots at the cuff edge | `v9/assets/codex/pov/*.png` | P2 |
| IN-01 | B2, N1, F1–M1 card | Instrument identity (illustrative, **not** an altimeter) | Front | housing (semicircle bezel), dial face with unlabelled ticks (no numerals), needle, centre pivot cap | Needle pivot is the cap centre; needle drawn pointing straight up | `v9/assets/codex/instrument/*.png` | P1 |
| AC-01 | A1 | Establishing aircraft | Side profile, small high-wing jump aircraft, open side door, flying right | aircraft body, propeller blur disc (separate) | none | `v9/assets/codex/aircraft_side.png` | **P0** |
| EN-01 | A1, R1 | Layered cloud illustrations | Side and slightly from above | 6 flat-bottomed cumulus, 3 thin wisps | none | `v9/assets/codex/clouds/*.png` | P2 |

**Not requested (done procedurally in V9, judged adequate):** terrain and farmland (perspective-projected, altitude-correct), sky and haze, cloud deck placement, airflow, force arrows, density samples, speed sketch.

## Image-generation prompts (one per asset, same style suffix)

Style suffix for all: *"original hand-drawn scientific illustration, thin slightly irregular charcoal outline, flat muted fills, no shading gradients, no gloss, minimal face, transparent background, isolated, consistent character design, educational explainer style"*

- **CH-01:** "Adult skydiver in free fall seen exactly from the side facing right, belly-to-earth arch, knees bent with heels raised, arms forward with soft elbows, rounded helmet with goggles, light jumpsuit, dark harness straps, closed tan parachute container on the back — " + suffix. Then split into the 15 listed parts on a 640×400 canvas matching rig.json pivots.
- **CH-03:** "Same skydiver seen from above and behind, arms and legs spread symmetrically, closed tan parachute container with trapezoid flap and stitched seams fully visible, helmet dome with goggle strap — " + suffix.
- **CH-05:** "First-person view of the wearer's own right forearm crossing the frame from lower right toward upper left, light jumpsuit sleeve, dark cuff, relaxed gloved hand, a round semicircular instrument strapped on top of the wrist, no numbers on it — " + suffix.
- **AC-01:** "Small high-wing single-engine jump aircraft in side profile flying right, open side door, simple windows, seen from a distance — " + suffix.
- **CH-02, CH-04, CH-06, IN-01, EN-01:** same character description and suffix, with the viewpoint from the table.

## Integration plan once delivered

1. Drop the files at the expected paths.
2. Point `rigs/<view>/rig.json` `file` entries at the PNGs. `rig_renderer.drawing()` already accepts PNG through Cairo if the loader is switched; that is a single-line change.
3. Rerun `tools/v9.py --check --render`, then `tools/boards_v9.py`.
4. Re-inspect pivots at the joint extremes.
