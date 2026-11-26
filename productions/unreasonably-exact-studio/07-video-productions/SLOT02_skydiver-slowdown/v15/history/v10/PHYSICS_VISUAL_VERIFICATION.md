# Physics and visual verification — V10

## Model, rerun on 2026-11-25 (`tools/model.py`, unchanged from V9)

**Setup:** vertical fall from rest at 10 km. Fixed posture with m = 80 kg, g = 9.8 m/s², CdA = 0.50 m². These are **assumed illustrative values**, not measurements of a person.
**Equations:** NASA Glenn troposphere fit for ρ(h); D = ½ρv²·CdA; a = g − D/m. Euler integration with dt = 0.01 s.

**Units check:**
- ρ is in kg/m³ (1.226 at sea level, 0.414 at 10 km, matching standard atmosphere tables).
- D/W is dimensionless.

**Internal checks:** `model.py` asserts that v never goes negative, that D/W ≥ 0.999 after the peak, and that the speed at the ground is below the peak. All pass.

| model t | altitude | speed | D/W | ρ |
|---|---|---|---|---|
| 0 s | 10 000 m | 0 | 0 | 0.414 |
| 10 s | 9 589 m | 69.9 m/s | 0.68 | 0.435 |
| **20 s (peak)** | 8 809 m | **81.0 m/s** | **1.000** | 0.479 |
| 30 s | 8 009 m | 78.5 m/s | 1.035 (max) | 0.526 |
| 90 s | 3 842 m | 61.9 m/s | 1.021 | 0.835 |
| 158.6 s | ground | 50.9 m/s | 1.013 | 1.226 |

These numbers are **model-dependent**. None of them is spoken in the narration or shown on screen. The film shows no numerals.

## Film-to-model time map

`MODEL_MAP` in `tools/v10_shots.py` maps film time to model time and is the same as in V9. The film compresses 150 s of model time into 57 s.

| Film time | Model time | What happens |
|---|---|---|
| 20.92 s | 0 s | Reset: the model starts at rest |
| 43.6 s | 20 s | Drag equals weight (STATE 2) |
| 78.2 s | 150 s | End of film. The model's last ~9 s (near the ground) are never shown. |

The minimum altitude depicted is 445 m, and there is no impact.

## Beat-by-beat verification

| Beat | What is drawn | Source of values | Status |
|---|---|---|---|
| F1 reset | Needle at zero, no world motion, "starts at rest" | model t = 0 | ✔ |
| G1 / I1 density | Equal 132-unit boxes; dot count = round(ρ/1.226 × 150) for 10 km, 5 km, 300 m (51, 90, 147 dots) | ρ(h) from `model.py` | ✔ Schematic marks, labelled "dots are marks, not molecules". Clouds are not used as a density cue. |
| H1 STATE 1 | Weight > drag, velocity arrow grows | D/W, v from model | ✔ |
| J1 comparison | Same dot field, same body, speeds 1× and 2×; drag arrows 24 and 96 units (∝ v²) | Drag equation at fixed ρ and CdA | ✔ Labelled "SAME AIR · SAME BODY". Kept separate from the changing-density descent. |
| K1 STATE 1→2→3 | Weight fixed at 118 units; drag = 118 × D/W. STATE 2 is labelled when 0.995 ≤ D/W < 1.004, "balanced at top speed · still moving down" | model | ✔ Drag crosses weight at film 43.6 s, during "stronger than your weight" |
| K1 / Q2 lens | Tips zoomed in 10×; gap = (D/W − 1) × 118 × 10 (≈ 41 units at D/W 1.035) | model | ✔ The zoom is drawn as a lens with a leader line to the tip. No second arrow sits beside the forces. |
| L1 equal-time positions | Model altitude every 15 s from t = 30 to 150; gaps fall from about 1 150 m to about 790 m per step (≈ −31%) | model | ✔ The shrink is modest because the honest slowdown is modest; it is labelled "gaps shrink: slower". Every mark is below the previous one. |
| M1 / N1 needle | Needle = −120° + 240° × v/90 m/s, no numerals | model v | ✔ After 47.7 s the needle never rises (asserted in `--check`) |
| Q1 graph | Downward speed against time from the trace; axis labels "downward speed", "time", "zero"; tracking dot | model | ✔ Never below zero; peak and decline only |
| S1 alternatives | CdA × 0.7 and × 1.6 runs of the same model, labelled "smaller / larger drag area", and "same simple model, other inputs" | `sim_alt()` | ✔ Supported by the model. These are not claims about specific postures. |

**Assertions in `tools/v10.py --check` (pass):**
- 26 shots are contiguous.
- Model time never runs backwards.
- v ≥ 0 throughout, and altitude never rises.
- The needle is monotonic after 47.7 s.
- The minimum altitude is 445 m.

## Remaining scientific caveats (stated on screen at R1)

- Posture is fixed, and the atmosphere is a standard troposphere with no wind.
- The mass and CdA are assumed values.
- "Not a prediction for a real person."
