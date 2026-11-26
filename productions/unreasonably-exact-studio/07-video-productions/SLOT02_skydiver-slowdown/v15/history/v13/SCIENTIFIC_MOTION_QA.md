# V13 scientific motion QA

**Model:** unchanged from V9–V12 (`tools/model.py`). Fixed posture, m = 80 kg, CdA = 0.5 m², NASA Glenn troposphere fit, vertical fall from rest at 10 km. These are illustrative assumptions, not a prediction for a real person.

## Model checks (rerun 2026-11-25)

| Requirement (brief §12) | Result | Evidence |
|---|---|---|
| Height never increases | Pass | `tools/v13.py --check`: "no rise" |
| Downward speed starts at zero (idealised reset) | Pass | v(0) = 0. F1 reset says "starts at rest · fixed posture" |
| Speed rises at first | Pass | 44.4 m/s at 5 s, 75.0 m/s at 12 s |
| Drag = weight at the speed maximum | Pass | Peak 80.96 m/s at 20.0 s, D/W = 1.0001 |
| Drag > weight during the slowdown | Pass | `model.py` asserts D/W ≥ 0.999 after the peak. Maximum 1.035 at about 30 s; 1.014 at 150 s |
| Net force points up | Pass | Shown as violet (drag − weight) only after 43.6 s in film time (model 20 s) |
| Speed decreases but stays positive | Pass | 52.0 m/s at 150 s. Model check "v ≥ 0"; the needle never rises after 47.7 s |
| Parachute stays closed | Pass | The back pose has the pack closed in A2 and P1 |
| Model not changed for drama | Pass | `model.py` is byte-identical to V12 |

The aircraft opening is **illustrative framing**. The model's start from rest begins only at F1 (20.92 s), and the frame there says "starts at rest". No measured speeds or survival claims are added. The wrist dial shows only SLOW–FAST, with no numbers.

## Each explanation, checked as motion (proof clips in `MOTION_DESIGN_PROOFS/`)

| Beat | What the viewer sees | Check |
|---|---|---|
| **B: airflow → drag** (E1, 16.8–20.9) | (A) The body moves down past still dots: "you: down", "still air". (B) The camera catches up and holds the body; the same dots now stream up and around it: "air, relative to you", "schematic". (C) The teal drag arrow grows up from the centre of mass: "drag: the air pushes back". | Relative airflow (dots with motion trails, no arrowheads) is visually distinct from the force (solid arrow). The flow is a potential-flow sketch around an ellipse, labelled schematic: no wake and no simulation claim. |
| **C: thin vs dense** (G1 23.1 s; I1 28.6–31.4) | Two equal 150×150 boxes. Dots ∝ model density: 0.41 kg/m³ at 10 km, 1.16 kg/m³ at 600 m (about 2.8×). Then the same body at the **same speed** under each box: the drag arrow is 2.8× longer in the denser box. | Density is the only thing that changes. There is no ruler, force diagram or instrument on that screen. The note "dots are schematic, not molecules" is on screen. |
| **Speed alone** (J1, 33.7–38.7) | A fixed "same air · same posture" box. Speed ×1→×2 with the drag arrow ×1→×4 (length ∝ k²), and a dashed ghost of the ×1 arrow. | Density and posture are visibly fixed |
| **D1: gravity wins** (H1, 24.9–28.6) | The weight arrow draws on (24.95 s), then a short drag arrow (25.6 s). The speed arrow grows. | One common scale: weight = 118 units, drag = 118 × D/W |
| **D2: equal, then drag exceeds** (K1, 38.7–46.6) | Body arrows grow to equal. "balanced: still falling" (43.3–44.2 s) appears with the downward speed arrow still at full length. Bars side by side on one baseline and one scale (weight 280 units). At 43.6 s they are equal; then the drag bar passes the dashed weight line, the excess turns violet, a camera push (×2.25) goes in, and "net force: up". | The excess is the model value: about 3.2% of the bar, roughly 9 units, at model 27 s. It is magnified only by a real camera push in which both bars scale together, so it is never redrawn larger. |
| **E: down while slowing** (K2, L1, M1; 46.6–55.4) | "still moving down" (dashed arrow). An equal-time trail with one mark every 10 s on one scale: gaps grow (rust) and then shrink (teal); every mark is lower than the last. Net force up beside a downward velocity arrow. "slower" | No hovering and no rising: every trail mark is below the previous one |
| **F: instrument** (B3 9.7 s; N1/O1 55.4–59.4) | The needle on the wrist dial falls with the model speed. The dial appears only on the wrist. | The needle never rises after 47.7 s (self-check) |
| **Recap** (Q2, 66.0–70.5) | Bars again: drag 1.5% over weight at model about 148 s. Push in ×2.6, then "still moving down". | Same scale as K1 |

## Muted review (picture only)

Read from the proof strips and storyboard panels with no sound, the sequence carries:

1. A person falls from a plane; the parachute is closed.
2. Gravity pulls down.
3. Air rushes up past you, and that pushes back (drag).
4. Thin air vs denser air.
5. Faster means much more push.
6. The push grows until it equals the weight, then passes it.
7. The extra is the up net force.
8. The marks are still going down, but closer together.
9. The dial drops and the pack is still closed.

**Still leans on narration:**
- "Wait, what?": the reaction beat
- Why the trail turns from rust to teal: the colour change alone doesn't say why
- The final "model, not a prediction" caveat. The assumptions line in R1 helps.

## Known issues

- The density dots fill a box; they are not a literal sample volume.
- The airflow dots also fill the background sky in E1. That is intentional (the air is everywhere), but it is busy.
- The posture is fixed in every model scene. The arm lift (M1) is a glance at the wrist, not a posture change, and it is not presented as a cause.
