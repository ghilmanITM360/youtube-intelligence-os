# P02 Earth-Moon cinematic parallax (opening line)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B01-B03, narration_t 0.00-7.12: rise starts after a small dip; lands on "moon." (2.80); slow push on "question." (6.17)

## Expected behaviour

Camera starts low on the sunlit Earth limb, dips slightly (anticipation), then rises and eases toward the Moon so the Moon settles exactly as the voice says "moon"; stars barely move, the Moon moves about a third as much as Earth (depth). After the landing the frame keeps drifting, then a gentle push on "question". NOT TO SCALE mark visible.

## Files

- `P02_earth_moon_parallax.mp4` (540x960, 30 fps, 214 frames, h264 yuv420p)
- `P02_earth_moon_parallax_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P02_earth_moon_parallax_start.png`, `P02_earth_moon_parallax_middle.png`, `P02_earth_moon_parallax_end.png`, `P02_earth_moon_parallax_frame_stats.json`
- `cue_P02_earth_moon_parallax_laser.png` (cue "laser", narration_t 1.96 s, frame 59)
- `cue_P02_earth_moon_parallax_moon_land.png` (cue "moon_land", narration_t 3.05 s, frame 92)
- `cue_P02_earth_moon_parallax_question.png` (cue "question", narration_t 6.17 s, frame 185)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p02.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P02
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P02_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P02_earth_moon_parallax: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 214 of 214 expected |
| P02_earth_moon_parallax: frame-to-frame change | info | mean abs diff 1.815, max 9.053, min 0.008 (0-255 luma, 1/4 res); frames with ~no change: 1 of 214; max pixel luma 255; max step of mean luma 1.71 |
| parallax plane stars moves 0.06 x the near plane (vertical, rise segment) | PASS | screen dy 46.3 units |
| parallax plane moon moves 0.35 x the near plane (vertical, rise segment) | PASS | screen dy 268.7 units |
| parallax plane earth moves 1.00 x the near plane (vertical, rise segment) | PASS | screen dy 759.7 units |
| depth order reads: far Moon moves less than near Earth | PASS | Moon 263 vs Earth 830 units |
| camera move lands on "moon." (2.80 s): Moon speed < 15 u/s within 0.25 s after | PASS | speed 0.8 s before 174 u/s, 0.25 s after 2.5 u/s |
| anticipation: camera dips before rising (first 0.55 s) | PASS | y 1180 -> 1215 |
| one Sun: both spheres lit from the upper left (lit-centroid offsets) | PASS | moon (np.float64(-6.4), np.float64(-3.9)), earth (np.float64(-4.6), np.float64(-8.2)) |
| star layer overscan covers the camera range (assert) | PASS | min margin 417 |

## Start / middle / end frames

P02_earth_moon_parallax

![P02_earth_moon_parallax start](P02_earth_moon_parallax_start.png)
![P02_earth_moon_parallax middle](P02_earth_moon_parallax_middle.png)
![P02_earth_moon_parallax end](P02_earth_moon_parallax_end.png)

## Defects I found by viewing frames

- (not yet reviewed)

## Corrections made

- (none yet)

## Re-test result

- (not yet re-tested)

## Scientific verification

Earth: NASA Blue Marble + Black Marble; Moon: LRO/LROC colour map (NASA SVS 4720), near side toward the viewer. One Sun vector lights both, so the Moon is a gibbous lit on the left, matching the terminator rule in PRODUCTION_ART_DIRECTION. Sizes and distance are a composition, not to scale (declared).

---
Status words used: `candidate`. Nothing here is `approved`.
