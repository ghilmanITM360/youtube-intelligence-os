# Instrument continuity QA — V10

## The device

V10 uses the Codex V10 **front circular device** (candidate layers from `assets/v10supp/instrument/front/`):
- housing
- dial
- needle without its cap
- pivot cap
- upper and lower straps (the buckle is baked into the upper strap)

All layers share a 1024×1536 canvas with the needle pivot at (512, 743). Code is in `tools/instrument10.py`.

The V9 semicircular IN-01 gauge is **retired**. It read as a car dashboard.

**Needle:**
- Angle = −120° + 240° × v / 90 m/s.
- Pointing down-left means zero, and up-right means fast.
- The dial has no numerals; Codex's dial has four unlabelled baked ticks.
- Captions say "SPEED" and "illustrative indicator, no numbers". It is not an altimeter, and nothing is relabelled.

## Wrist sequence (B2–B4, then N1)

| Shot | Brief letter | What is shown | Same wrist? | Same device? |
|---|---|---|---|---|
| B1 / B2 | A tracking, B gaze | Side view. A small device with a strap band sits on `near_forearm` just behind the cuff, in its FK frame, so it moves with the arm. The glance head looks down at it while the near arm lifts. | Right wrist (the near side in this view) | Housing and dial layers, foreshortened (scale 0.034 × 0.05) |
| B3 | C forearm detail | Codex V10 unmounted right forearm from the wearer's view. The device is centred at the measured wrist point (905, 578) and rotated 27.6° to sit across the forearm axis. The straps are masked by the sleeve alpha, so they wrap the arm and never reach into the sky. | Right | Same layers at 0.25 |
| B4 | D close-up, E needle | Face-on close-up. Only the needle moves (74 → 66 on the qualitative scale). Tag: "later in the fall". | (continues) | Same layers, 250 units |
| F1–Q2 | — | Small face-on card in the top-right corner, with the needle following the model | — | Same layers, no strap |
| N1 | E | Same close-up as B4, with the needle following the model downward | — | Same |
| M1/N1 → O1 | F return | Cut to the looking-down POV and then the over-the-back view | — | — |

**Needle continuity:**
- At the reset (F1) the needle sits at zero.
- It rises during H1–K1, and its maximum coincides with STATE 2 at 43.6 s.
- After 47.71 s it only falls; `tools/v10.py --check` asserts this.
- B4 is explicitly tagged "later in the fall", because it previews a moment after the speed peak.

**Rotation test:** visual checks of the needle at 0, 45 and 90 m/s are in `qa/instr_test.png`. The cap artefact Codex reported is not visible at film scale.

## Open issues (honest)

- **The device layers are Codex candidates, not production-approved.**
  - The buckle is baked into the strap.
  - The tick marks are baked into the dial.
  - The thresholded alpha leaves slightly hard edges.
- **No true side, oblique or three-quarter device artwork exists yet.**
  - The side-view device is the front art squashed, an approximation.
  - B3 uses the front art on a top-down forearm, which is close to face-on and acceptable.
- **The forearm is a candidate** (`flat_unmounted_candidate.png`).
  - Its style is flat and close to the V9 suit, but its sleeve colour is a little lighter.
  - The arm crops at the right edge of its canvas; the framing keeps that edge out of shot.
- **B3 and B4 last 0.9 s each.** That is tight for reading. Retiming requires the owner's narration decision.
