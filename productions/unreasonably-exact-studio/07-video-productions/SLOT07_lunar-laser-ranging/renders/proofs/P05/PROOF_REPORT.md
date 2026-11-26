# P05 Apollo astronaut movement (arm rig v2: shoulder skinning, Codex layers)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B18 window (narration_t 40.08 + 5.0 s); a rig proof, not the final B18 choreography

## Expected behaviour

Astronaut stands on the lunar plate; small anticipation (near arm back, body up), then the near arm reaches forward and down while the body leans from the boots, overshoots a little and settles; the far arm follows a beat later with half the swing; then recovers. Breathing keeps the hold alive. No gaps open at the shoulders.

## Files

- `P05_astronaut_arm_rig.mp4` (540x960, 30 fps, 150 frames, h264 yuv420p)
- `P05_astronaut_arm_rig_start.png`, `P05_astronaut_arm_rig_middle.png`, `P05_astronaut_arm_rig_end.png`, `P05_astronaut_arm_rig_frame_stats.json`
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p05.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P05
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P05_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P05_astronaut_arm_rig: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 150 of 150 expected |
| P05_astronaut_arm_rig: frame-to-frame change | info | mean abs diff 1.164, max 4.603, min 0.324 (0-255 luma, 1/4 res); frames with ~no change: 0 of 150; max pixel luma 254; max step of mean luma 0.06 |
| no gap at the near shoulder over (-12, 32) deg (opaque-at-rest pixels uncovered within 70 px of the pivot) | PASS | worst 86 px of 15361 |
| no gap at the far shoulder over (-6, 18) deg (opaque-at-rest pixels uncovered within 70 px of the pivot) | PASS | worst 0 px of 15361 |
| overlapping action: far arm peaks after the near arm | PASS | near peak 1.74 s, far 1.86 s |
| anticipation: near arm swings back before the reach | PASS | min -9.0 deg |
| overshoot then settle on the reach | PASS | peak 30.0 vs settle 26.0 |

## Start / middle / end frames

P05_astronaut_arm_rig

![P05_astronaut_arm_rig start](P05_astronaut_arm_rig_start.png)
![P05_astronaut_arm_rig middle](P05_astronaut_arm_rig_middle.png)
![P05_astronaut_arm_rig end](P05_astronaut_arm_rig_end.png)

## Defects I found by viewing frames

- (not yet reviewed)

## Corrections made

- (none yet)

## Re-test result

- (not yet re-tested)

## Scientific verification

Anonymous A7L-style suit (no names, flags or patches). Motion is stylised; low lunar gravity is not simulated in this clip (it matters for walking and dust, not for an arm reach). Rig v1 has no elbow: the reach is a shoulder swing; the kneel/align pose (no photo evidence, gap G-ASTRO) will be a whole-pose replacement.

---
Status words used: `candidate`. Nothing here is `approved`.
