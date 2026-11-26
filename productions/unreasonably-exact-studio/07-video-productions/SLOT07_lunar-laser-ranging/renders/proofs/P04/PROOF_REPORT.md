# P04 Observatory and telescope movement (RIG_002)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: rig proof (not narration-synced); used by the opening (B01-B04) and B22

## Expected behaviour

Shutter splits open from its centre, leaves slide out; then the telescope inside rises smoothly from a low lean to near-vertical and keeps tracking slowly. No part of the tube shows outside the slit.

## Files

- `P04_observatory_rig.mp4` (540x960, 30 fps, 180 frames, h264 yuv420p)
- `P04_observatory_rig_start.png`, `P04_observatory_rig_middle.png`, `P04_observatory_rig_end.png`, `P04_observatory_rig_frame_stats.json`
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p04.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P04
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P04_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P04_observatory_rig: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 180 of 180 expected |
| P04_observatory_rig: frame-to-frame change | info | mean abs diff 0.433, max 1.409, min 0.000 (0-255 luma, 1/4 res); frames with ~no change: 22 of 180; max pixel luma 236; max step of mean luma 1.09 |
| telescope pixels outside the slit are clipped (it sits inside the dome) | PASS | raw tube alpha outside slit up to 25709 px, all masked by SLIT |
| the tube is visible through the open slit at the end | PASS | visible alpha 21599 px |
| mount drive: no overshoot (lean monotonic while slewing) | PASS | lean 40 -> 6 deg |
| shutter opens before the telescope moves (mechanical order) | PASS | open done 2.0 s, slew starts 2.2 s |
| aperture is in the slit once pointed (from 3.17 s; at low lean it is behind the shell by design) | PASS | aperture at end (510, 800) |
| overscan (assert) | PASS | min margin 232 |

## Start / middle / end frames

P04_observatory_rig

![P04_observatory_rig start](P04_observatory_rig_start.png)
![P04_observatory_rig middle](P04_observatory_rig_middle.png)
![P04_observatory_rig end](P04_observatory_rig_end.png)

## Defects I found by viewing frames

- (not yet reviewed)

## Corrections made

- (none yet)

## Re-test result

- (not yet re-tested)

## Scientific verification

Generic dome observatory (illustration, not Apache Point). Large telescopes slew smoothly and settle without overshoot; the shutter opens before the telescope points out.

---
Status words used: `candidate`. Nothing here is `approved`.
