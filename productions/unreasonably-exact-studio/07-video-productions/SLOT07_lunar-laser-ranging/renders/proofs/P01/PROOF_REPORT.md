# P01 Earth rotation, clouds and consistent lighting

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B05 window (narration_t 8.66 + 6.0 s); not a narration-synced shot, a rig proof

## Expected behaviour

Earth turns smoothly left-to-right (west to east) under a fixed Sun at the upper left; night lights appear only on the dark side; clouds drift slightly faster than the ground; atmosphere rim brighter on the sunlit limb; slow eased push-in, then a hold. Badge says the spin speed is illustrative.

## Files

- `P01_earth_rotation_lighting.mp4` (540x960, 30 fps, 180 frames, h264 yuv420p)
- `P01_earth_rotation_lighting_start.png`, `P01_earth_rotation_lighting_middle.png`, `P01_earth_rotation_lighting_end.png`, `P01_earth_rotation_lighting_frame_stats.json`
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p01.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P01
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P01_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P01_earth_rotation_lighting: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 180 of 180 expected |
| P01_earth_rotation_lighting: frame-to-frame change | info | mean abs diff 1.325, max 1.753, min 0.929 (0-255 luma, 1/4 res); frames with ~no change: 0 of 180; max pixel luma 255; max step of mean luma 0.17 |
| lighting constant while Earth spins (lit-side centroid drift over 7 samples) | PASS | 23.7 design units (disc radius 400) |
| Sun from the left: lit centroid is left of the disc centre (token SUN) | PASS | centroid x 467 vs centre 540 |
| no texture seam at the antimeridian (central-column step vs typical) | PASS | seam 5.12 vs typical 2.39 |
| north-pole view: no pinch/singularity at the pole (gradient at pole vs surroundings) | PASS | pole 1.53 vs ring 8.27 |
| clouds drift relative to the surface | PASS | 15.0 deg over the clip |
| star layer overscan covers the camera range (assert) | PASS | min margin 413 |

## Start / middle / end frames

P01_earth_rotation_lighting

![P01_earth_rotation_lighting start](P01_earth_rotation_lighting_start.png)
![P01_earth_rotation_lighting middle](P01_earth_rotation_lighting_middle.png)
![P01_earth_rotation_lighting end](P01_earth_rotation_lighting_end.png)

## Defects I found by viewing frames

- (not yet reviewed)

## Corrections made

- (none yet)

## Re-test result

- (not yet re-tested)

## Scientific verification

Real geography (NASA Blue Marble, public domain) and night lights (NASA Black Marble). One Sun vector for every sphere (tokens.SUN). Spin direction is west-to-east as seen from above the north pole (counter-clockwise); speed is ~3600x real and labelled ILLUSTRATIVE. Clouds are Codex artwork (Batch 1 tiles) placed by Claude with loose climatology (tropical clusters near the equator, frontal bands and cyclones at 30-55 deg, cyclones only over ocean, southern cyclones mirrored); they are not a real weather snapshot.

---
Status words used: `candidate`. Nothing here is `approved`.
