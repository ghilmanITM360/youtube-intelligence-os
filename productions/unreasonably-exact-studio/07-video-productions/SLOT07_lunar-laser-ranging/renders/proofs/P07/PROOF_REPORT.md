# P07 Retroreflection (conceptual corner cube) + flat-mirror contrast

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B19-B21 (V7). Standalone clip on anim_t (not narration-bound); the same scene functions are re-timed to the anchor words inside P13.

## Expected behaviour

Clip 1: a 2-D corner-cube cross-section (two perpendicular faces, opening down toward Earth, third face as a magnified inset). Three rays at three different entry angles enter one after another (warm = outbound), bounce off both faces and leave (cool = home) ANTIPARALLEL to how they entered: parallel to the entry ray but laterally offset, never collinear. Finished rays step back so one pair is read at a time; then each pair is lit in turn with a faint pair of guide ticks across entry and exit. Clip 2 (B21 A/B): the same rays against a ghosted FLAT mirror (dashed, translucent): the mirror sends each ray away (X in the source ring), the cube returns it to its source ring (tick). Light moves at constant speed (linear), no beam is drawn into space, no number, no dimension.

## Files

- `P07_retroreflection.mp4` (540x960, 30 fps, 288 frames, h264 yuv420p)
- `P07_retroreflection_start.png`, `P07_retroreflection_middle.png`, `P07_retroreflection_end.png`, `P07_retroreflection_frame_stats.json`
- `P07_flat_mirror_contrast.mp4` (540x960, 30 fps, 270 frames, h264 yuv420p)
- `P07_flat_mirror_contrast_start.png`, `P07_flat_mirror_contrast_middle.png`, `P07_flat_mirror_contrast_end.png`, `P07_flat_mirror_contrast_frame_stats.json`
- `assert_results.json`
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p07.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P07
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P07_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P07_retroreflection: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 288 of 288 expected |
| P07_retroreflection: frame-to-frame change | info | mean abs diff 0.100, max 0.610, min 0.000 (0-255 luma, 1/4 res); frames with ~no change: 82 of 288; max pixel luma 236; max step of mean luma 0.46 |
| P07_flat_mirror_contrast: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 270 of 270 expected |
| P07_flat_mirror_contrast: frame-to-frame change | info | mean abs diff 0.061, max 0.282, min 0.000 (0-255 luma, 1/4 res); frames with ~no change: 135 of 270; max pixel luma 236; max step of mean luma 0.28 |
| exit = -entry for the 3 shown rays (assert, tol 1e-12) | PASS | dots=[-1.0, -1.0, -1.0] |
| exit = -entry for 3000 random rays (assert) | PASS | max /d_out+d_in/ = 6.66e-16 |
| exit offset from entry (not collinear) | PASS | lateral offsets [338.11, 248.22, 243.43] units |
| one ray at a time: an earlier ray is <= 0.16 bright once the next ray has started | PASS | alphas [0.15, 0.15] |
| final hold is quiet: all rays <= 0.23 bright; in the alignment stage the explained pair is lit alone (>= 0.95) | PASS | final [0.22, 0.22, 0.22] ; lit [1.0, 1.0, 1.0] |
| three distinct entry angles | PASS | [-16, -4, 20] |
| flat mirror is NOT antiparallel for tilted rays (assert) | PASS | dots=[-0.615661, -0.951057, -0.829038, -0.5] |
| contrast: mirror return misses source ring, cube return lands inside it | PASS | [{'mirror_exit_miss': 191.3, 'cube_exit_miss': 64.8, 'ring_radius': 90}, {'mirror_exit_miss': 439.0, 'cube_exit_miss': 70.0, 'ring_radius': 90}] |

## Start / middle / end frames

P07_retroreflection

![P07_retroreflection start](P07_retroreflection_start.png)
![P07_retroreflection middle](P07_retroreflection_middle.png)
![P07_retroreflection end](P07_retroreflection_end.png)

P07_flat_mirror_contrast

![P07_flat_mirror_contrast start](P07_flat_mirror_contrast_start.png)
![P07_flat_mirror_contrast middle](P07_flat_mirror_contrast_middle.png)
![P07_flat_mirror_contrast end](P07_flat_mirror_contrast_end.png)

## Defects I found by viewing frames

- v1 clip 1: background was the star field; for a neutral cross-section (BG_003_NEUTRAL_CUTAWAY) the stars competed with thin rays. One of three rays started at x=1138, outside the 1080 frame. All three rays stayed at full brightness and crossed each other, so no entry/exit pair could be read; the cube occupied only the upper third.
- v1 contrast clip: the mirror panel was cramped (rays only ~360 units long, deflection barely visible); the two source rings overlapped; the second mirror-deflected ray landed inside the FIRST ray's source ring, which falsely suggested a return.
- v1 numpy-2 bug: np.cross on 2-D vectors raised in the check code (found when the check ran).
- Still true after the fixes (viewed on stills): the three entry rays inevitably cross each other inside the cube; this is mitigated by dimming finished rays and lighting one pair at a time, but the final hold frame is busy. The third-face inset is small and wordless (only the magnifier glyph says it is an inset). In the contrast variant the cube rays pass very close to the apex (needed so the parallel-but-offset return stays inside the source ring), so they cross only a short stretch of the cube.
- Lead review (2026-11-26): the final hold frame of clip 1 was still cluttered (all three pairs at 55% with crossing lines).

## Corrections made

- Neutral dark gradient background; cube enlarged (face 640, apex y 560); three rays re-chosen (angles -4, -16, +20 deg) so all starts are on screen; finished rays step back to 30% when the next ray starts; after the last ray each pair is lit in turn with its own guide ticks, then everything settles at 55%.
- Contrast variant rebuilt as stacked panels (A mirror over B cube) with the same two rays, both leaning right (12 and 26 deg), source rings radius 90 and wide apart, mirror 450 units above the sources, X in the empty ring and a tick in the filled ring after both rays finish; ray end positions are tested against the rings.
- Added optics.cross2 (numpy-2 safe).
- Entry rays now play strictly one at a time: a finished ray drops to 0.15 as the next starts (was 0.30); in the alignment stage the explained pair is lit alone (others 0.15); final hold at 0.22 with only faint guide ticks; clip lengthened 9.0 -> 9.6 s so the quiet hold lasts about 0.9 s. Antiparallel asserts unchanged.

## Re-test result

- Re-rendered after the changes; stills viewed again (3.4, 5.0, 7.1, 8.6 s of clip 1; 2.4, 4.4, 8.0 s of clip 2): pairs are readable, mirror exits land outside the rings, cube exits inside. All checks PASS (see table). The moving clip itself was not watched.
- Re-rendered after the lead's note; stills at 3.4, 5.0, 6.9, 8.7 s viewed (one bright pair at a time, earlier rays recede). New checks PASS (earlier ray <= 0.16 once the next starts; final alphas <= 0.23). Antiparallel asserts (3 shown rays + 3000 random) still PASS.

## Scientific verification

Specular reflection is computed, not drawn by hand: a 90 degree corner is two mirror reflections, whose product is a 180 degree rotation about the apex, so the exit direction is exactly minus the entry direction in the plane. This is asserted for every shown ray and for 3000 random rays (max |d_out + d_in| reported in assert_results.json). The exit is offset by 2 x (distance of the entry line from the apex): the film must say 'parallel', never 'the same line' (research note in PROGRESS_LOG: B21 exit ray is parallel but OFFSET). A flat mirror is asserted NOT antiparallel for any tilted ray. 2-D cross-section only shows two of three reflections; the third face is the inset. Claim C06 picture rule (km-wide footprint inset at B20) is NOT part of this clip; it is in P13. No operational equipment design.

---
Status words used: `candidate`. Nothing here is `approved`.
