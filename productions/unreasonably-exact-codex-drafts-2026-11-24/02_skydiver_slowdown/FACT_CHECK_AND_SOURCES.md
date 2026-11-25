# Claim check — slot 02

Accessed 2026-11-24. No independent aerodynamicist has reviewed this draft.

| Spoken claim | Source / section | Calculation and assumptions | Uncertainty / status |
|---|---|---|---|
| Gravity pulls down and no parachute is slowing the fall | Scenario definition | Model assumes a vertical drop from rest and unchanged body configuration; no parachute is used | ASSUMPTION |
| At 10 km the air is thin; initially speed rises | [NASA standard atmosphere](https://ntrs.nasa.gov/citations/19770009539), atmosphere tables; [NASA drag equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/), density and velocity | From rest drag is initially zero in a still-air model; gravity accelerates the body. Density increases on descent through this altitude range | DIRECTLY_SOURCED and ASSUMPTION; weather varies |
| Drag increases with density and speed | NASA drag equation, equation and discussion | D = ½ρv²CdA with fixed Cd and area; drag opposes relative airflow | DIRECTLY_SOURCED, ASSUMPTION; Cd and posture vary |
| Drag exceeds weight and downward speed decreases while descent continues | Project `work/models/fall_model.py`, set B and `fall_results_V2_check.txt` | Fnet = mg − D taking down as positive. Archived set B: 10 km peak 299 km/h, ground 189 km/h. Codex reran the copied model in the draft folder: 299 km/h peak and 189 km/h ground; reproduction is not independent validation | MODEL_RESULT; EXPERT_REVIEW_NEEDED. Not every posture or trajectory guarantees slowdown |
| Posture and conditions change result | NASA drag equation, shape, orientation, density | No new calculation | DIRECTLY_SOURCED; exact real outcome UNRESOLVED |

No claim about survival. Peak speed, impact speed and time are deliberately omitted from the narration. The 1 km comparison distracts from this short's force explanation; it can be considered in a visual note only if separately labelled and reconciled with the approved Day 1 model.
