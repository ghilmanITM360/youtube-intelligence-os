# P06 Astronaut sets the reflector down (Codex B5P/B5PA/B5PR, Claude rig)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B18 window (narration_t 40.08 + 6.0 s); rig proof for the B17-B18 placement

## Expected behaviour

The astronaut, holding the reflector by its handle, gives a small lift (anticipation), lowers it to the ground while leaning from the planted boot, it touches down with a tiny settle and two small fans of dust that fly in clean arcs and drop straight back; then the glove lets go and he straightens. His glove stays exactly on the bar until release; shadows are hard and fall right.

## Files

- `P06_astronaut_sets_reflector.mp4` (540x960, 30 fps, 180 frames, h264 yuv420p)
- `P06_astronaut_sets_reflector_start.png`, `P06_astronaut_sets_reflector_middle.png`, `P06_astronaut_sets_reflector_end.png`, `P06_astronaut_sets_reflector_frame_stats.json`
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p06.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P06
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P06_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P06_astronaut_sets_reflector: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 180 of 180 expected |
| P06_astronaut_sets_reflector: frame-to-frame change | info | mean abs diff 0.634, max 3.218, min 0.239 (0-255 luma, 1/4 res); frames with ~no change: 0 of 180; max pixel luma 255; max step of mean luma 0.01 |
| grip holds while carrying: glove-to-bar error (design units) | PASS | max 0.000 |
| reflector starts lifted and lands exactly at the master pose | PASS | start height 22.7 units |
| anticipation: a small lift before lowering | PASS | lean -3.2 -> -4.0 deg |
| release comes after touch-down (cause before effect) | PASS | land 1.9 s, release 3.4 s |
| dust is ballistic (no drag): longest flight time = 2 v cos / g | PASS | 0.49 s |
| Codex layer cut re-stacks onto the B5P master (silhouette IoU >= 0.97, rule R12) | PASS | IoU 0.983 |

## Start / middle / end frames

P06_astronaut_sets_reflector

![P06_astronaut_sets_reflector start](P06_astronaut_sets_reflector_start.png)
![P06_astronaut_sets_reflector middle](P06_astronaut_sets_reflector_middle.png)
![P06_astronaut_sets_reflector end](P06_astronaut_sets_reflector_end.png)

## Defects I found by viewing frames

- (not yet reviewed)

## Corrections made

- (none yet)

## Re-test result

- (not yet re-tested)

## Scientific verification

Apollo-style suit, anonymous. Reflector proportions follow the Apollo 11 LRRR master (Codex, AS11-40-5952 reference). Dust: ballistic under lunar gravity (1.62 m/s^2) with no air drag: parabolas, no billowing cloud. Pose = illustration; the real deployment involved levelling and aiming, shown here as a set-down.

---
Status words used: `candidate`. Nothing here is `approved`.
