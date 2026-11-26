# Character anatomy QA — V11

## What changed

The owner rejected V10's assembled character: it showed circular joint discs, oval boot ends, a floating pack and an identity change in the three-quarter view.

The Codex V11 package **does not contain a layered rig**. It contains *fused whole-pose studies* (side, three-quarter, back) and a glance head, all marked "candidate; unregistered; not approved".

**V11 decision:** draw each pose **whole**, as a single layer, and stop animating limbs separately.
- A whole drawing has no joints that can open or show a disc.
- The cost is that there is **no independent limb animation** in V11 (see Limitations).

## Repairs made here (code, reproducible)

| Asset | Problem | Repair | Script |
|---|---|---|---|
| Side pose (V11-C04 `boot_revision_reference.png`) | Boot tops drawn as closed ovals (the failure Codex itself reported) | Inner cap outline repainted with the boot's own median colour inside the eroded silhouette. The boots now read as solid ankle boots. Before/after: `qa/boot_zoom.png` → `qa/boot_zoom_fix.png`. | `tools/fix_boots.py` |
| Side pose | All-cream suit; the V9 identity, and the V11 three-quarter and back poses, all have grey trousers | Cream pixels left of the harness leg strap shifted to the trouser grey. The boundary follows the strap row by row (`qa/hipseam.png`). | `tools/recolour.py` |
| Three-quarter pose (V11-C06) | Far sleeve grey, near sleeve cream | Far sleeve shifted to the cream jacket colour | `tools/recolour.py` |
| Glance head (V11-C03) | Not registered to anything | Registered on the side canvas: scale 0.39, 4° down, neck alpha feathered below the chin. Used as a replacement layer in B2/M2. Trials: `qa/glance_reg.png`. | `tools/recolour.py` |

## Checklist (brief §03)

| Check | Result | Evidence |
|---|---|---|
| Shoulder overlap | Continuous sleeve drawn in one piece in all three poses | `qa/recol.png`, `qa/tq_back.png` |
| Elbow continuity | Cloth folds, no disc | same |
| Knee continuity | Continuous trouser bends | same |
| Ankle / boot attachment | Side: cap ovals painted out. Three-quarter/back: boots enter the trouser cuffs. | `qa/boot_zoom_fix.png` |
| Wrist attachment | Side pose has the small device on the near (right) wrist. Wrist shots use the same strap colour and housing shape. | `qa/V11_contact_1p5s.png` |
| Torso–leg connection | Harness leg strap crosses the hip. Colour change sits under the strap. | `qa/hipseam.png` |
| Head attachment | Single drawing. The glance head is feathered into the neck (a faint chin overlap on the sleeve is visible at full size, not at film scale). | `qa/glance_reg.png` |
| Closed pack + harness | Pack drawn with harness straps over it in side, three-quarter and back poses. No floating gap. | `qa/before_after/0m13.png` |
| Whole motion range | The only motion is body roll ±1.2°, bob ±1.5 units and 0.6% breathing scale. These cannot open seams. | `tools/v11_shots.py: body()` |
| Identity across views | Same helmet, goggles, cream jacket, grey trousers and tan pack. **Gloves differ:** three-quarter/back have grey gloves, side/wrist are bare-handed. | open |

## Performance (brief §05)

- **Motion sources:**
  - calm whole-body roll, bob and breathing (no random limb shake)
  - camera push-ins on the gaze and wrist shots
  - environment parallax from the projected terrain and clouds
  - relative-air specks
  - flow lines in E1/I2
- **Gaze:** the head is replaced with the downward-glance drawing.
- **Model segment:** the posture stays fixed throughout (one side drawing, one pose). The B2/M2 gaze shots are outside the model frame and do not change posture inside it.
- **Motion was reviewed:**
  - `qa/motion/wrist.png` (8.2–11.2 s)
  - `qa/motion/air.png` (16.8–20.9 s)
  - `qa/motion/cross.png` (38.7–47.7 s)
  - `qa/motion/end_wrist.png` (52–59.4 s)
  - `qa/motion/recap.png` (66–70.6 s)

## Limitations (honest)

1. **No limb animation.** No arm lift on the glance, no hand activity. The brief asks for "appropriate arm and hand activity". That needs separated, registered parts with overlap art, which Codex has not delivered. This is the largest remaining character gap.
2. **The C1 reaction close-up still uses the V9 close-up face.** It has rounder goggles than the V11 heads, because no V11 expressive close-up exists. The identity is close, not exact.
3. **Gloves are inconsistent** across views (see above).
4. **All V11 character art is Codex candidate art, not approved.** The repairs above are mine and also need art-direction approval.
5. The three-quarter face is subdued but still slightly smiling.
