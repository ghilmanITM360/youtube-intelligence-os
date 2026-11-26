# V15 character animation QA

## What changed from V14

V14's side figure was one rigid drawing. Only the forearm lift (sprite sequence), the head (separate layer: nod, glance, blink) and whole-body bob/roll moved. Legs, boots, hands and clothing never moved independently.

V15 adds **mesh deformation** (`tools/cloth_warp.py`) to the side rig. A smooth displacement field on a 32 px grid bends the single continuous Codex drawing with PIL's MESH transform. Nothing is cut apart, so there are no joint discs, no seams, no openings and no detached parts.

| Component | V15 motion | Driver | Limit |
|---|---|---|---|
| Knees → shins → boots (each leg separately) | Rotation about each knee. Weight ramps 0 at the knee → 1 at the boot, so the boot moves with its shin. | Two-frequency oscillation, different per leg (0.21 / 0.27 Hz) | ±2.6° × (0.35 + 0.65·load) |
| Wrists → hands (each hand separately) | Rotation about each wrist (hand trims in the air) | 0.37 / 0.42 Hz | ±4° × (0.35 + 0.65·load). Off while the forearm-lift sprite plays. |
| Trousers, sleeves, shirt | Travelling ripple toward the tail (wind-driven fabric) | **Aerodynamic load = drag/weight** from the model (½ρv²·CdA/mg) | Amplitude 1 + 4.2·load^1.3 px; speed 2 + 5.5·load rad/s |
| Pack, harness hardware, watch, boots' soles, head/neck | No cloth motion (weight 0) | none | Tested: pack moves < 0.35 px at maximum load |
| Head | Existing layer: small nod, glance to the wrist, blinks (unchanged from V14, still on the separate head drawing) | Shot timing | ±1° nod |
| Forearm | Existing 12-frame lift sequence (V12 rig) | Shot timing | 22° then dissolve to the raised drawing |
| Body | Existing calm roll/bob | Ambient clock | ±0.8° / 1.2 units |

Every moving element is either a rotation about an anatomical pivot or a fabric ripple. All of it runs on the real film clock, so motion never stalls during stretched beats. Each oscillator mixes two incommensurate frequencies, so nothing loops visibly within a shot.

## Phase-dependent behaviour (driven by the model, not hand-keyed)

| Phase | Load (D/W) | What you see |
|---|---|---|
| Model reset, at rest (F1) | 0 | Cloth still; knees and hands at 35 % amplitude (calm, alive) |
| Acceleration (H1) | 0 → 0.9 | Ripples start and grow; airflow streamlines draw in with the load |
| Denser-air comparison (I1) | 0.48 vs 1.33 at the same speed | Figure in denser air flutters visibly more |
| Speed ×1 → ×2 (J1) | 0.25 → 1.0 | Flutter grows with speed squared, with the drag arrow |
| Peak and after (K1–M1) | ≈ 1.0–1.03 | Energetic but steady. The slow fall in speed is offset by rising density, which is physically right: drag stays about equal to weight. |
| Opening / tracking shots (B1–D1) | ≈ 0.5 (9.3 km, 60 m/s) | Moderate flutter |

## Anatomy rules

| Rule | Result | Evidence |
|---|---|---|
| No mechanical joint discs | Pass: no cut-outs; one continuous mesh | `qa/rig_v15/warp_states.png`; close-ups in `qa/frames_critical/` |
| No detached hands or boots | Pass: hands and boots are carried by the same field as their limb | Same |
| No floating pack | Pass: pack weight 0; harness is part of the same drawing | Self-check assertion |
| No double outlines | Pass: no layered duplicates; outlines bend with the fill | Close-up review |
| No joint openings | Pass: continuous field (no tearing possible with MESH quads sharing vertices) | Method |
| No unnatural stretching | Pass: max displacement < 16 px on a 1920 px canvas (< 1 % of body length) | Self-check assertion |
| No sudden pose teleportation | Pass: all oscillators are continuous in film time; shot cuts keep the established V14 cut points | Consecutive-frame strips |
| No repetitive robotic movement | Pass: two incommensurate frequencies per joint, different per joint | Method |

## Known limits (not fixed in V15)

- **Fingers** do not articulate individually. The Codex hands are single drawings, so only wrist rotation is possible without new art.
- **Facial expression** is limited to blink, glance and nod. There is no new mouth or eyebrow art.
- The **back and three-quarter views** (A2 rear reveal, P1 pack shot, opening) are still whole-pose drawings with body bob/roll only. The mesh layer is built for the side canvas.
- Equal-time trail (L1): only the newest figure is animated; the earlier marks are frozen ghosts on purpose.
