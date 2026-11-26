# Physics → visual correction ledger (V9)

## Model actually used (tools/model.py — runnable, self-checking)

- Vertical fall from rest at 10 000 m, still air, fixed posture. W = mg; D = ½·Cd·A·ρ·V²; a = (W − D)/m (NASA Glenn, *Falling object with air resistance*, *Drag equation*).
- ρ(h): NASA Glenn troposphere fit (T = 15.04 − 0.00649h; p = 101.29·((T+273.1)/288.08)^5.256; ρ = p/(0.2869·(T+273.1))), valid below 11 km.
- Assumed m = 80 kg, Cd·A = 0.50 m². These are illustrative, not a prediction for any person (NASA: Cd depends on shape and inclination and is found experimentally).
- Output: peak 81 m/s at t ≈ 20 s (h ≈ 8.8 km), where D = W. Then D/W stays between 1.01 and 1.035, and speed falls slowly to ≈ 51 m/s near the ground (t ≈ 159 s). `python tools/model.py` asserts v ≥ 0 always, D/W ≥ 1 after the peak, and end speed < peak.
- NASA does not discuss D > W explicitly. Deceleration while moving down follows from a = (W − D)/m < 0. This is stated as an inference, not a NASA quote.

## How each beat is drawn and why

| Beat | Narration | Physics (model) | V9 depiction | What we avoid | Where |
|---|---|---|---|---|---|
| A Gravity down | "gravity is still pulling you down" | W constant | Rust arrow from the centre of mass, same length in every shot (100 units = W) | Changing weight length between shots | B1, D1, H1–Q2 |
| B Drag < weight at first | "At first, gravity wins" | D/W 0 → 0.75 over model t 0.6–12 s | Teal drag arrow from CoM grows from 0, read from model D/W × 100 units | Drag drawn at fixed length | H1 |
| C Speed rises | "You keep going faster" | v 0 → 74 m/s | Needle on the fixed card, dashed velocity lane, streak speed and length ∝ v | Needle without a common scale | H1 |
| D Denser air | "entering denser air" | ρ 0.414 → 0.45 kg/m³ | Two **equal-size** samples, dot count ∝ ρ: "at 10 km" vs "air now" | Unequal areas or "visible molecules" | G1, I1 |
| E Drag grows with speed | "the faster you fall, the harder it pushes back" | D ∝ V² at constant ρ | Separate panel "SAME AIR · two speeds", equal panels; 2× speed gives 4× drag arrow | Mixing the density change into the speed comparison | J1 |
| F Drag = weight | "Eventually…" | D/W = 1.000 at model t ≈ 20 s | Drag tip reaches the dashed "weight length" tick; inset shows "balanced"; velocity still down, world still streaming | Showing a stop or hover at D = W | K1 |
| G Drag > weight | "can actually become stronger than your weight" | D/W ≤ 1.035 | Drag tip passes the tick by ~3 units on the same 100-unit scale (honest) | V8's 1.5× drag | K1, Q2 |
| H Net force up, velocity down | "still moving down… net force… up" | net = D − W ≈ 0.03 W | Violet double-shaft net arrow = (D − W), drawn **10× enlarged** in a labelled inset; velocity in its own blue dashed lane | Net arrow of invented size; same style as velocity | L1, M1, Q2 |
| I Speed decreasing, still descending | "downward speed starts to decrease" | v 78 → 69 → 62 … 51; h always falling | Needle moves only down after 47.7 s (asserted in `--check`); velocity arrow shortens but points down; ground keeps approaching; altitude marker keeps descending | Needle reversal; rising/hovering character | M1–Q2 |
| J Ground closer | "the ground gets closer" | h 3.8 → 1.5 km (model t 90–130 s) | Straight-down camera at model altitude; fields grow by projection | Impact, landing, distance readouts | O1, P1 |
| K Model caveat | "this is a model…" | — | Pull-back with "SIMPLIFIED MODEL · fixed posture · standard atmosphere" frame | Claiming a real-person outcome | R1 |
| L Other inputs | "Change the posture or the conditions" | Same model with Cd·A ×0.7 and ×1.6 | Dashed alternative speed curves | Posture change shown as the cause of the main slowdown | S1 |

## Separation rules enforced

- **Five grammars:** relative airflow = thin moving dashes, no arrowheads; drag = solid teal; weight = solid rust; velocity = dashed blue in its own lane; net force = violet double shaft. No style is reused across quantities.
- **Time:** film → model time map in `MODEL_MAP` (v9.py). Model scenes carry "MODEL · time compressed". The hook (B2) is a cinematic flash-forward tagged "later in the fall". The model reset at 20.92 s is explicit ("MODEL · starts at rest", needle 0, world motionless, wind near-silent).
- **Posture:** in model shots, joint flutter is limited to hands, feet and fabric. Amplitude scales with airspeed (0.25–0.70 of hook amplitude). The body angle is not changed.
- **No invented readouts:** no numbers on the dial or the altitude ruler. Only "10 km" and "ground" (premises of the script) appear.
- **Ground never reached:** minimum depicted altitude is 445 m (asserted).

## Remaining scientific limits

- The schematic airflow is 2-D potential flow around a stretched cylinder. It is labelled "relative airflow · schematic", not a turbulence simulation.
- The cloud deck at about 2 km and the terrain are illustrative. Haze uses a fixed 40 km visibility scale.
- The drag crossing happens early (model t ≈ 20 s, about 1.2 km below the start), while the narration places it after "entering denser air". The picture follows the model numbers: the crossing occurs during K1, model t 18 → 30 s.
