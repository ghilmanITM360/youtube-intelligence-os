# V12 scientific visual QA

**Model (unchanged from V9–V11, `tools/model.py`):** a fixed-posture fall from rest at 10 km through the NASA Glenn troposphere fit.
- Inputs: m = 80 kg, CdA = 0.5 m² (illustrative assumptions).
- Outputs: peak 81.0 m/s at model 20 s; D/W reaches 1.035 at about 30 s; 52 m/s at 150 s, 445 m above the ground.
- **No numbers are shown on screen except "10 km", which the narration says.**

**Self-check (`tools/v12.py --check`):**
- 25 shots are continuous.
- Model time never runs backwards.
- v ≥ 0 and altitude never rises.
- The needle never rises after 47.7 s and stays above zero once falling.
- No ground contact (minimum 445 m).
- Every 8th frame draws without error.

## Continuity checks (brief §18)

| Check | V12 |
|---|---|
| **Gravity stays downward** | The weight arrow always points down from the centre of mass, at the same length (L = 118) throughout. D1 re-measures it against a fixed tick ("same"). |
| **Modelled velocity stays downward** | The dashed blue arrow always points down. Its length follows model speed (8 + 0.75·v units, schematic scale). |
| **Parachute closed** | The pack is part of the body art and never opens (A2, P1). |
| **Common scale for weight and drag** | Both arrows start at one point. Drag length = 118 · D/W from the model, at every frame. |
| **Equal forces ≠ zero velocity** | At 43.6 s (model 20 s, D/W = 1.000) the lens shows the teal tip on the dashed weight mark while the dashed DOWN arrow stays at full length. |
| **Drag > weight ⇒ net force up** | The violet net arrow appears only when the tip passes the mark (gap > 5 lens units). Before that, a small rust "net down" arrow shows. |
| **Speed falls without upward motion** | Every trail mark in L1 is lower than the one before. The needle and graph decrease but stay positive. The "not zero" bracket is on the graph. |
| **Instrument follows the speed state** | B3: 74 → 66, a flash-forward with no model claim. N1/O1: the needle comes from the model's speed at the mapped model time. |
| **Ground keeps approaching** | The altitude ruler marker falls monotonically. O1 tilts to a nearer ground (model about 2.1 km → 970 m). |

## Magnification honesty

- **K1 / Q2 lens:** in-scene, joined to the tips by a leader line, with "×30" on the rim.
- **Inside the lens:**
  - The dashed rust line is where an arrow as long as the weight ends.
  - The teal tip sits (D/W − 1) · 118 · 30 units above it, so the *difference* is magnified 30×.
  - **The lens never shares the body-diagram scale, and the rim badge says so.**
  - The arrowhead and shaft width inside the lens are drawn at a fixed lens size; only positions are magnified.
- **The tip is driven by the model.** It rises through the mark as model time runs 17.5 → 27 s (film 42.0 → 46.6 s). The crossing is not keyframed by hand.

## Equal-time trail (replaces V11's two-column 4 s / 15 s comparison)

- **One trail, one interval, one scale:** a mark every 10 model-seconds, 0–150 s, at 0.085 units per metre for every gap.
  - Gaps from the model: 411 m (0–10 s), 780 m, 800 m, 768 m … 527 m (140–150 s).
  - Gaps grow, then shrink, on a scale the viewer can compare directly.
- **Gap bars are coloured by phase:** rust while speeding up (≤ 20 s), teal while slowing.
- **The slowdown is gentle and the picture shows it as gentle** (800 → 527 m per 10 s). It is not exaggerated.

## Other graphics

- **Airflow (E1, I2):**
  - Potential flow past an ellipse in the body frame: air arrives from below and leaves above.
  - Lines draw on, white-cored flow markers travel along them, and the body occludes the back pass.
  - Marked **"schematic"**. **No aerodynamic simulation was performed.**
- **Air samples (G1, I1):** equal-size lenses. Dot count = model density / sea-level density × 70, and drift rate follows model speed. The dots are marks, not molecules; this is stated here and not on screen (see `TEXT_REDUCTION_AUDIT.csv`).
  - The I1 lenses sit at 10 km, 5 km and 600 m on the altitude ruler. That is a preview of conditions, not the model's state at that moment, which is still about 9.4 km. The narration ("as you fall, you're entering denser air") supports this reading.
- **Speed ×2 → drag ×4 (J1):**
  - Same air, same body. The speed counter runs 1 → 2 and the drag arrow follows k² continuously.
  - Schematic lengths, labelled "same air". It is not a model state.
- **Graph (Q1, S1):**
  - Model TRACE: axes draw, the curve rises from zero with a tracking point, then "top speed", the fall, and the "not zero" bracket.
  - The alternative curves (CdA × 0.7 and × 1.6, same model) appear only in S1, when the narration says "change the posture or the conditions".

## Muted read (contact sheets and strips viewed without audio)

1. Tiny figure under an aircraft, high above farmland.
2. Behind the faller, with a closed pack, 10 km above the ground.
3. A rust arrow pulling down.
4. They check the wrist; the dial needle drops.
5. Surprise.
6. Same arrow, same length.
7. Air streams past the body.
8. MODEL, starting at rest.
9. Drag grows against weight; the air gets denser lower down.
10. Faster means much more drag.
11. Under the lens, drag overtakes weight and the net force points up.
12. The trail still goes down, but the gaps shrink.
13. The wrist needle falls.
14. The ground nears.
15. The pack is still closed.
16. The graph peaks and declines without reaching zero.
17. Model assumptions.
18. Other inputs give other curves.

**Weak points in the muted read:**
- **The J1 counters ("speed ×2", "drag ×4")** are small text and carry the idea.
- **The I1 density lenses** need the narration to read as "lower down = denser".
