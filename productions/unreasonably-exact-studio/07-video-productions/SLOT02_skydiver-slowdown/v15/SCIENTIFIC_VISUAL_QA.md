# V15 scientific visual QA

**Model:** `tools/model.py`, unchanged since V13.
- Fixed posture: m = 80 kg, CdA = 0.50 m² (assumed).
- Air density: NASA Glenn troposphere fit.
- Starts from rest at 10 km.
- Outputs: peak 81.0 m/s at 20 s and 8,809 m, where drag/weight = 1.000. After the peak, drag/weight stays between 1.009 and 1.036 down to the ground. Speed never reverses.

Every on-screen quantity reads one model state per frame: altitude marker, density dots, arrow lengths, bar heights, needle, cloth/airflow load and graph point.

## The ten required ideas: where and how each is shown

| # | Idea | Shot (V15 film time) | How it is shown | Check |
|---|---|---|---|---|
| 1 | Gravity pulls down | B1 7.1 s, H1 35.1 s | Warm-orange solid arrow from the centre of mass, pointing down. In the model it has a constant length of 118 units (the common scale). | Weight arrow length never changes (D1 "same" re-measure) |
| 2 | At first you accelerate | H1 35.1–41.5 s | Blue dashed speed arrow grows; streaks and airflow speed up; altitude marker moves | Model speed rises 0 → 69 m/s over this stretch |
| 3 | Density rises as altitude falls | G1 32.2 s, I1 41.5 s, every tracking shot | Same-size air boxes: dot count ∝ model ρ (thin 0.41 vs denser 1.16 kg/m³ at 10 km vs 600 m). V15: air marks in every tracking shot also scale with ρ (8 + 30·ρ/1.226 marks) | Dot count from `PHYS.rho(h)` |
| 4 | Drag opposes relative motion | E1 22.3–28.0 s | You move down through still air; the camera locks on; the air streams up past you (dots with motion trails); the teal drag arrow grows up | Airflow (dots) and force (arrow) are separate marks |
| 5 | More speed → more drag (other things equal) | J1 49.4–56.3 s | Same air box, same posture; speed ×1 → ×2 and drag ×1 → ×4 (live labels); ghost of the ×1 arrow. V15: cloth flutter follows the same v² load | Drag length = 24·k² |
| 6 | Drag eventually exceeds weight | K1 56.3–66.8 s | Bars side by side on one scale from one baseline. The drag bar reaches the weight line ("equal" at the modelled peak), then passes it | Bar heights = 250 × (1, D/W) |
| 7 | Net force points up | K1 64.2 s →, K2, Q2 | V15: **×8 lens** on the bar tops. Inside, the bars are scaled 8× about the weight line, and the violet excess is the net force. A **violet net-force arrow ×8** sits on the body at the centre of mass. Both carry the ×8 badge. | Arrow length = (D/W − 1)·118·8; lens gap = (D/W − 1)·250·8 |
| 8 | Still moving down | K2 66.8 s, L1, Q2 | Blue dashed downward speed arrow next to the violet upward net-force arrow, with "still moving down" | Velocity (dashed blue) never shares a style with a force |
| 9 | Downward speed decreases | L1 68.1–74.1 s, M1, N1, Q1 | Equal-time trail: one mark every 10 s on one scale. Gaps grow, then shrink, while every mark is lower. Then the speed arrow shortens, the needle falls, and the graph falls but stays above zero ("not zero") | Self-check: needle never rises after the crossing |
| 10 | Parachute stays closed | A2 4.7 s, P1 84.8 s | Behind-view shots of the closed pack. The pack is rigid in the side-rig mesh (weight 0, tested to < 0.35 px movement at maximum load) | `tools/cloth_warp.py` self-check |

## Colour grammar (one meaning per colour)

| Quantity | V15 colour | Mark |
|---|---|---|
| Weight / gravity | warm orange `#DB7224` (V14 was rust `#9A4F2C`) | solid arrow, down |
| Drag | teal `#2F7F7A` | solid arrow, up |
| Downward velocity | blue `#2F5D8C` | **dashed** arrow, separate lane |
| Net force | violet `#7A4CC2` | double-shaft arrow and violet bar excess |
| Relative air | light blue `#5E8FB3` | dots, streamlines, flow markers (no arrowheads) |

Velocity is never drawn as a solid force arrow, and the net-force arrow is never blue.

## Magnification disclosure

The net force after the peak is 0.9–3.6 % of the weight. At true scale it would be about 4 px on screen. V15 shows it at **×8 in one place and one way**: the lens rim badge "×8" and the arrow label "net force ×8".

V14's screen-wide push onto the bars, which had no magnification label, is removed. So is V14's unused ×30 lens setting.

## Illustrative motion stays within the model

- **Fixed posture.** Limb motion is limited to knee rotation up to 2.6° × load factor and wrist rotation up to 4°. The torso, pack and head pivot are unchanged. The model's CdA is constant; the animation does not imply a posture change.
- **Cloth and airflow intensity** = drag/weight = ½ρv²·CdA/(mg). This is the model's own aerodynamic loading, so the picture reacts to density as well as speed:
  - "reset / at rest": load 0, calm
  - acceleration: rises
  - peak: about 1.0
  - after the peak: about 1.02–1.03, so it stays energetic but steady while the speed slowly falls
- **Density comparison (I1):** two figures at the same speed. The one in denser air has visibly stronger cloth motion: load 0.48 vs 1.33 (capped at 1.2 in the mesh). This is the visual version of "denser air → more drag".
- **Streamlines** are potential flow past an ellipse and are labelled "schematic". They are not a CFD result.

## Checks run

- `tools/model.py` checks pass: speed ≥ 0; after the peak D/W ≥ 0.999; ground speed < peak.
- `tools/v15.py --check` passes:
  - 2,641 frames
  - warp monotone
  - all 25 shots appear
  - model time never runs backwards
  - speed ≥ 0
  - altitude never rises
  - the needle never rises after the crossing
  - minimum altitude shown: 445 m
- `tools/cloth_warp.py` self-check passes:
  - identity at zero angle
  - pack rigid at maximum load
  - head/neck region registered (< 1 px)
  - deformation < 16 px everywhere
