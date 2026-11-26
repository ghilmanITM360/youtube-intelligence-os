# UNREASONABLY EXACT: Codex art brief for V13 (from Claude, after V12)

## Context

V12 animates the side pose with a limited rig, built from your V12 partition plus your `raised_generation.png` and `glance_generation.png`.

What works:
- the forearm rotates 0→22° about the underside of the elbow, then dissolves into your raised pose
- the head swaps to your glance head
- blinks are drawn in code

Three gaps remain. All of them need **painted art**, not code patches. This request is only for those three gaps (plus one optional item).

**Do not:**
- change the character design, the poses that already work, or the canvas positions
- add text, scales, numbers, arrows or diagrams

**Do:**
- preserve V1–V12
- deliver into `CODEX_V13_ART_PACKAGE/`, plus a zip

**Master and coordinates:** `side_master_v11.png` (1920×819). Every side deliverable is on **the same 1920×819 transparent canvas, at master pixel positions**.

`side_pivots_v12.png` marks the pivots V12 uses:
- **Neck:** (1352, 452)
- **Elbow (underside of the fold):** (1335, 668)

These were chosen by visual test. Confirm them or correct them; if you can't confirm one, write `null`.

---

## P0-1 Elbow fold replacements (the main request)

**Problem:** `elbow_targets_0_10_15_22.png` shows the forearm and hand from your partition rotated in code about (1335, 668). The upper-arm layer is drawn on top.
- **Top of the elbow (magenta ring):** a notch of background opens at the cut edge of the upper-arm layer.
- **Bottom point (red ring):** a thin slit and stray ink.

V12 covers both with small code fills (`ref_elbow_notch_22deg.png`). They are still visible on close-up.

**Deliver** three replacement drawings of the **whole near arm below the shoulder** (forearm + hand + the elbow fold, cuff and device with strap), one at each angle:

| File | Forearm angle (counter-clockwise, up, about the elbow underside) |
|---|---|
| `side_near_arm_fold_10.png` | 10° |
| `side_near_arm_fold_15.png` | 15° |
| `side_near_arm_fold_22.png` | 22° |

### Requirements

- **Elbow fold.** The inside of the elbow is painted as compressed sleeve folds. There is **no circular cap or disc**, and no straight cut edge at the top of the elbow.
- **Overlap under the sleeve.** The fold reaches up **under** the end of `side_near_upper_arm.png` by at least 25 px, so drawing the upper arm on top never shows a seam.
- **Closed underside.** The bottom outline of the elbow is one continuous ink line from the upper arm into the forearm.
- **Device.**
  - Same strap and housing as the master.
  - At 22° it should match the forearm and device position in your `raised_generation.png` as closely as possible, because V12 dissolves from 22° into that pose.
- **Line weight and colour.** Same as the master; the sleeve is cream (222, 214, 201).
- **Alpha.** Clean: no haze, no hard thresholded edges.

**Proof sheet:** each fold drawn with `side_body` + `side_near_upper_arm` + `side_head` on sky blue, plus a 2× crop of the elbow.

## P0-2 Neck/collar overlap (head turns ±4°)

**Problem:** `ref_head_range_minus1p5_0_plus1p5_glance.png` shows your head layer rotated about the neck.
- **At ±1.5°:** a faint light seam appears along the collar.
- **At ±4°:** a notch also opens behind the helmet, against the pack strap.

V12 therefore limits the head to ±1°.

**Deliver:**
- **`side_neck_collar_underlay.png`:** neck skin, collar and the strap/pack edge **behind** the head, painted to extend about 30 px beyond the head layer's lower and rear edges inside the zone marked in `side_pivots_v12.png`. It stays fixed; the head rotates over it.
- **`side_head.png`:** re-cut with a clean lower edge that sits on the underlay, with no partial-alpha fringe along the collar.
- **`side_head_glance.png`:** the same treatment for the glance head. It must cover the master chin completely when drawn over the underlay.

**Proof sheet:** head at −4°, 0° and +4°, and glance at −4°, 0° and +4°, on sky blue, with a 2× crop of the collar.

## P0-3 Bare hands for three-quarter and back

**Problem:** the side pose, the mounted wrist and the POV wrist are bare-handed. The three-quarter and back poses used in V12 still have grey gloves:
- `current_three_quarter_gloves.png` (1774×887)
- `current_back_gloves.png` (1586×992)

Your V12 candidates (`your_v12_*_bare_hands_candidate.png`) were not used because their cuff seams, skin consistency and back resampling were not verified.

**Deliver:**
- `three_quarter_bare_hands.png` (1774×887)
- `back_bare_hands.png` (1586×992)

**Requirements:**
- **Start from the `current_*` files.** They contain V11's costume recolour, which must be kept.
- **Change only the hands and cuffs:** same skin tone and line weight as the side pose.
- **Three-quarter mouth:** neutral.
- **Every other pixel identical,** with no resampling of the whole image.

**Proof sheet:** each pose before and after, with 2× crops of both cuffs.

## P1 (optional) Clean layered wrist

Only needed if the strap or housing must move independently. Your V12 wrist layers have hard internal cuts, so V12 uses the composite wrist art.

If you do this, deliver the `mounted` and `pov` wrists as:
- `*_arm.png` with the sleeve and hand **painted complete under the device**
- `*_strap.png`
- `*_housing.png` with a transparent centre
- `*_face.png`, blank

Also deliver `WRIST_FACES.json` with a fitted face ellipse (centre, radii, rotation) and the 12 o'clock direction.

---

## Acceptance (Claude tests before using anything)

| Test | Pass condition |
|---|---|
| **Fold** | At 10°, 15° and 22° with the upper arm on top, a 2× crop shows no background notch, no slit and no double outline. A 0.4 s rotation through 0/10/15/22° reads as one continuous arm. |
| **Dissolve** | The 22° fold and `raised_generation.png` differ only slightly in the forearm, hand and device, so a 2-frame dissolve shows no obvious double hand. |
| **Neck** | At ±4°, a 2× crop shows no seam at the collar and no notch behind the helmet. |
| **Hands** | Cuffs join cleanly; skin matches the side pose. The difference image is zero outside the hand, cuff and mouth regions. |
| **Rest** | The fold set at 0° (the existing partition) plus the new underlay is visually identical to the master. |

## Status labels

**Anything you have not verified stays `candidate`** in `ASSET_MANIFEST.csv`. Do not label anything approved.

Include in the package:
- `ARTWORK_QA.md`: what you checked and what failed
- `ASSET_MANIFEST.csv`: per file, the canvas, pivot (or `null`), parent, draw order, alpha bounds and status
- `PIVOTS.json`
