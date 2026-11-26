# UNREASONABLY EXACT — Codex art brief for V12 (from Claude, after V11)

## Context

V11 used your V11 repair package as whole-pose drawings. No rig joints are visible any more, but **the arms and hands cannot move**. The owner's brief asks for purposeful arm/hand activity (raising the wrist to look at the device). This request covers only the art needed for that, plus two consistency fixes.

**Do not:**
- change the character design
- redraw poses that already work
- add text, scales, numbers, arrows or diagrams (Claude draws those in code)

**Do:**
- preserve V1–V11 files
- deliver into a new folder `CODEX_V12_ART_PACKAGE/`, plus a zip

Reference files are in this folder:
- `side_body_v11_repaired.png`: the side pose as used in V11, after Claude's boot-cap and trouser-colour repairs. **Use this as the master.**
- `side_split_targets.png`: numbered approximate pivots.
- `ref_boot_repair.png`: how the boot tops were closed.
- `ref_wrist_sequence_v11.png`: the owner's V10 screenshot next to the V11 wrist sequence.

---

## P0-1 Layered side pose (the main request)

Split `side_body_v11_repaired.png` (1920×819) into these layers, all on **the same 1920×819 transparent canvas**, at the same pixel positions as the master:

| Layer | Contents | Pivot (see targets image) |
|---|---|---|
| `side_body.png` | Everything not listed below (torso, legs, boots, pack, harness, far arm if not split) | — |
| `side_head.png` | Helmet, goggles, face, neck down to the collar | 1 neck |
| `side_head_glance.png` | Same head looking down at the near wrist, same size and line weight | 1 neck |
| `side_near_upper_arm.png` | Near sleeve, shoulder to elbow | 2 near shoulder |
| `side_near_forearm.png` | Near forearm, cuff and **device with strap** | 3 near elbow |
| `side_near_hand.png` | Near hand | 4 near wrist |
| `side_near_forearm_raised.png` | **Replacement drawing:** forearm rotated ~35° up toward the face, device face turned toward the viewer | 3 near elbow |
| `side_near_hand_raised.png` | Hand to match the raised forearm | 4 near wrist |
| *(optional)* `side_far_forearm.png`, `side_far_hand.png` | Far arm parts | 5, 6 |

### Requirements

- **Hidden overlap art.** Each child layer extends **under** its parent at the joint as a sleeve overlap, so rotating it ±20° (forearm ±35° using the raised replacement) never opens a gap.
  - The overlap must be cloth (sleeve folds), **never a circular cap or disc**. Discs were the owner's main V10 rejection.
- **Fill behind the arm.** The body layer must contain the torso drawn **behind** the near arm, so lifting the arm reveals a jacket and harness, not a hole.
- **Boot tops stay closed**, as in the master.
- **Bare hands**, matching the side and wrist art (see P0-2).
- **Clean alpha:**
  - no haze
  - no thresholded hard edges
  - nothing touching the canvas edge except where the master does
- **`PIVOTS.json`:** `{layer: {pivot:[x,y], parent: name, draw_order: n}}` in 1920×819 pixels.
  - Unknown values = `null`. Never guess.
- **Proof sheet:** every layer assembled at rest, and at the extremes listed below, rendered on sky blue. Rest must match the master pixel for pixel, within the anti-aliasing.

| Joint | Extremes |
|---|---|
| head | ±8° |
| near upper arm | −15° / +20° |
| near forearm | −20° / +20° |
| near forearm raised | +0° / +15° |
| near hand | ±15° |

## P0-2 Gloves decision → bare hands everywhere

- The side pose, the mounted wrist and the POV wrist are bare-handed.
- The three-quarter (`character/three_quarter/pose_reference.png`) and back (`character/back/pose_reference.png`) poses have grey gloves.

**Redraw only the hands** in those two poses as bare hands in the same skin tone and line weight. Everything else stays identical.

- Deliver at the same canvas sizes (1774×887 and 1586×992), pixel-aligned to the originals.
- The three-quarter far sleeve should be cream, as in V11. You may start from Claude's recoloured `v11/assets/v11reg/tq_body.png`.
- While on the three-quarter pose: make the mouth **neutral** (currently slightly smiling).

## P0-3 Layered wrist art (same device in every view)

For `wrist/mounted_reference.png` (1774×887) and `wrist/pov_reference.png` (1774×887), deliver on the same canvases:

- `*_arm.png`: sleeve, cuff and hand.
- `*_strap.png`: the strap only, separate so it can be nudged.
- `*_housing.png`: bezel ring and crown, with a **transparent centre**.
- `*_face.png`: a **blank** off-white face disc. Claude draws the SLOW→FAST scale and needle in code; do not add marks.
- `WRIST_FACES.json`: face centre, x/y radii and the 12 o'clock direction (degrees) per composition.
  - Claude measured mounted (853,409) rx 84 ry 81 and POV (829,497) rx 76 ry 85. Please confirm or correct.

---

## P1 (if time allows)

4. **Three-quarter view of the device on a wrist** (an oblique glance shot), layered as in P0-3.
5. **V11-style expressive close-up face**, to replace the V9 close-up used at "Wait, what?". Layers:
   - head
   - eyes
   - lids (blink replacement)
   - brows
   - mouth
   - mouth_open (replacement)

   Same helmet and goggles as the V11 side head.

## P2

6. **Low-altitude terrain sprites** in the flat landscape style (1–4 km view): farm tracks, hedgerows, small farm buildings, tree clumps. Separate transparent PNGs on a top-down view.
7. **Landscape parallax layers** for the opening horizon (far haze, fields, river/road, near clouds), from `environment/landscape_reference.png`.

---

## Acceptance (Claude will test before using any of it)

- **Rest test:** the layered side pose at rest is visually identical to the master.
- **Seam test:** at every listed extreme, no gap, no disc and no double outline. Claude will render 4–10 s motion proofs.
- **Lift test:** the near arm can lift and bring the device into view without revealing empty background through the torso.
- **Identity test:** same person in side, three-quarter and back views. Same bare hands, neutral face.
- **Wrist test:** the device sits on the same wrist with the same housing in every view. The face is blank and its centre matches `WRIST_FACES.json`.

## Status labels

Label anything that fails a test or is unverified as **candidate** in `ASSET_MANIFEST.csv`. Do not label it approved.

Include in the package:
- `ARTWORK_QA.md`: what you checked and what failed
- `ASSET_MANIFEST.csv`: per file canvas, pivot, parent, draw order, alpha bounds and status
