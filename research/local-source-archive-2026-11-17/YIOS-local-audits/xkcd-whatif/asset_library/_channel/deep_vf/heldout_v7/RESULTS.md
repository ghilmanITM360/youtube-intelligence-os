# Held-out v7 results (frozen rules v1, sha in ../FROZEN_RULES_v1.sha256; LOCAL ONLY)

The rules were frozen at 2026-11-08T19:15:48Z, before any held-out table or frame was opened. Measurements are in `measured.json`. The viewed sheets are `*_holds.jpg` (one tile per automated HOLD) and `*_long_activities.jpg` (one tile per ACTIVITY longer than 6 frames). Every source SHA was re-verified and all 6 match.

| Rule | U4cONnQxgvo (Short A) | X97DDWvxaqQ (Short B) | e3uk7jU3RHo | UXA-Af-JeCE | X7sbn9LMZOg | U8F7UNK9jco |
|---|---|---|---|---|---|---|
| S1 no red title card (MEASURED) | PASS (0 frames) | PASS (0) | n/a | n/a | n/a | n/a |
| S2 1-frame share ≥0.44 (MEASURED, automated) | PASS 0.641 | PASS 0.800 | n/a | n/a | n/a | n/a |
| S3 canvas #F9F9F9±3 (MEASURED, modal bright pixel of scaled hold frames) | PASS #F7F7F7 | PASS #F7F7F7 | n/a | n/a | n/a | n/a |
| S4 dissolve 6±1 f | NOT_EVALUATED: no standalone dissolve; overlay fades ride an 8–9 f blurred camera move (window H7_S_MAPMOVE G0016) | NOT_EVALUATED: none seen | n/a | n/a | n/a | n/a |
| S5/L1 red only as marks (OBSERVED) | **FAIL**: translucent pink region fill on map (G0041–G0045) | **FAIL**: red-drawn prop objects (PART 1/PART 2 books, G0067–G0069) | PASS: circles, strike, hatch, ripple marks | PASS: labels, arrows, strike, damage lines, warning outline | PASS: scribble, X, field lines | **FAIL**: painted red/orange sunset backgrounds, yellow-filled suns, navy gradient skies (G0011–G0015, G0081–G0095, G0121–G0133) |
| S6/L2 no photographs (OBSERVED) | PASS | PASS | PASS | PASS | PASS (a typeset search-results UI inset on the board, G0007–G0011, is drawn/typeset, not a photo) | PASS (painted, not photo) |
| S7 Short-vs-parent density ±20% (MEASURED, automated both sides, ASR_UNCERTIFIED) | PASS 20.4 vs 18.4/min (+11%), 36/38 sentences matched | n/a | n/a | n/a | n/a | n/a |
| L3 camera moves ≤6% of activities (OBSERVED on >6 f tiles) | n/a | n/a | **FAIL**: about 7–9 of 75 (≈10–12%) are blurred ruler scrolls and zooms in a magnitude-ladder video | PASS (1 long activity) | PASS (≤2/63) | PASS (≤3/67) |

**Tally:**
- 19 of 23 evaluated rule×video checks pass, which is **82.6%**. That is below the 90% bar, so the verdict is **FROZEN_SET_DOES_NOT_HOLD**.
- The 4 failures fall into two categories:
  - **Colour/red usage** (3 failures). The P3 rule was worded too narrowly.
  - **Camera share in a scale-ladder/journey format** (1 failure). This matches the earlier oTzW held-out-4 failure in the quant protocol.
- Hold stillness was not visually verified. The automated `hold_drift_px60` flags give 9/76, 3/61, 2/64, 1/68, 5/40 and 6/51 holds per video, and these candidates were not viewed.

## New findings surfaced by the held-outs (each n=1 unless stated)
1. **Painted colour mode.** U8F7UNK9jco (2025-10-21, sha 38b212f4…) builds whole scenes as painted colour plates:
   - red/orange sunset gradients and yellow-filled sun discs;
   - navy night skies with a warm horizon glow;
   - the canvas measured #FDFDFD, not #F7–F9.

   This is not a one-off. Across all 44 local longs, the share of non-title frames with mean saturation >25 is a continuum (`../colour_mode_share.csv`). The top five are WH4g1ptJ-70 0.48, BO8rOs05v48 0.33, U8F7UNK9jco 0.27, r7B0MzvwDcA 0.24 and qu8nx1qUwEU 0.21.
2. **Glow gradients are common.** UXA-Af-JeCE uses half-frame black with a radial white glow as a recurring scene grammar for "the Sun's surface" (G0011–G0041, G0057–G0067). X97DDWvxaqQ uses screen-glow vignettes (G0083–G0095). A blanket "no gradients" rule is wrong.
3. **Slow process animation (new motion class).** U8F7UNK9jco G0104 (216 f) and G0106 (220 f) show a day/night terminator sweeping slowly across a map for about 9 s each. U8F7 G0008 (106 f), G0016, G0022 and G0034 show a sun disc travelling along a path over 21–106 f. This is an object/process path animation and is not in the earlier class table.
4. **Persistent scale-ladder anchor.** In e3uk7jU3RHo a numbered ruler at the left edge stays on screen for the whole explanation. It scrolls with motion blur as the magnitude label changes, which raises the camera-move share in this format.
5. **Red edit-mark device.** A red strike-through write-on followed by a corrected label appears in e3uk (RICHTER SCALE → "MOMENT MAGNITUDE" SCALE, G0015–G0021) and X97D (G0036–G0040). It was also seen in dev WH4g (GREENWICH MERIDIAN → NEW EQUATOR). Count so far: 3 videos.
6. **Map-explainer Short compound move.** U4cONnQxgvo G0016 (MEASURED window): an 8–9 f push-in and pan with motion blur. During the move, inset circles fade out and a hurricane symbol fades in, and the move lands hard (progress 0.728 → 1.000 in one frame).
