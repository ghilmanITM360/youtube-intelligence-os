# Character rig QA — V10

## Integration (what was done)

**Loader.** `tools/rig_renderer.py` `drawing(file, canvas_w)` loads Codex PNGs as RGBA and crops them to the **alpha** bounding box, not the RGB one. It keeps native resolution, so k = png_width / canvas_w = 4 for the 2560×1600 parts of a 640×400 canvas, and draws them at 1/k. The 4× export is applied exactly once.

This departs from the handoff's half-resize suggestion. Keeping 4× avoids upscaling blur in the 1080-px close-ups (C1, B4).

**Verification:**
- `qa/rigs_sheet.jpg` shows rest poses rendered at their canonical positions.
- Pivots and parenting come unchanged from Codex's proposed `rig.json` files, which are copied to `rigs/<view>/rig.json`. The V9 rigs are preserved in `../v9/rigs`.

**Replacement layers (renderer channels):**
- `<part>_file` swaps a drawing. It is used for `mouth` → `mouth_open.png` in C1 from 40% of the shot onward, and for `head` → the registered glance head in B2. **Only one mouth is ever drawn.**
- `blink` makes the lids replace the eyes: when lids are on, eyes are off. They are never drawn layered.
- `_attach` draws equipment in a part's own FK frame. The circular device is attached to the side rig's `near_forearm`, which is the right wrist in this view, in every side shot.

**Glance head:** a Codex V10 candidate.
- Haze below alpha 40 was removed.
- It was cropped to its opaque bounds, scaled to the side head's height (350 px at 4×) and centred on the side head (`assets/v10reg/side_head_glance.png`).
- Compared with the V9 side head in `qa/head_cmp.jpg`, the helmet, goggles and neck line up.

## Review findings

| Check | Evidence | Result |
|---|---|---|
| Joint gaps at rest and in film motion | `qa/V10_contact_1p5s.jpg`, `qa/seq_wrist.jpg`, `qa/seq_cross.jpg` | No gaps observed. In-film amplitudes are small (hands ±7°, forearms ±5°, glance +16/−26°). |
| Joint gaps at 60% of the rig limits (min, max, alternating) | `qa/rig_extremes_v10.png` | No openings in the side, three-quarter or back views |
| Visible joint caps | same | **Open (art).** Round knee, elbow and shoulder caps show as discs, most strongly in the three-quarter view. Codex flagged this too. It needs repaired artwork; animation cannot fix it. |
| Back view at extremes | same | **Open (art).** At 60% min/max the legs cross behind the pack and the boots twist. The film uses only ±2° thigh and ±4° shin flutter in A2/P1, so this is not visible in the film. |
| Identity across views | contact sheet | Same costume, palette and pack in every view. Heads are separate generations: the three-quarter head is rounder and smiling, the side head neutral. Acceptable in motion, but **not pixel-identical**. |
| Line weight and palette | contact sheet | Slight variation between views, especially the three-quarter view, which is a little warmer and heavier. Not corrected. |
| Close-up acting | C1 frames | Eyes shift (+5 px), brows lift, a 1-frame-range blink replaces the eyes, and mouth_open swaps in. No double mouth. |
| Fixed posture in the model section | F1–Q2 | Only flutter, with amplitude falling with model speed. No posture change carries the causal story. |
| Stretching | all | None. Rigid FK parts only. |

## Repair requests for Codex (artwork problems, not rig problems)

1. Side, three-quarter and back limbs: redraw elbow, knee and shoulder ends as sleeve overlaps instead of visible round caps.
2. Three-quarter head: a neutral expression matching the side and close-up identity.
3. Back view: thigh and shin parts that read correctly at ±15°.
4. A glance head generated on the side canvas with no haze, replacing the registered candidate.
