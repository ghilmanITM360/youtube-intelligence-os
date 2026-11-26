# P03 Observatory-to-Moon transition (selected opening A)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B01-B04: "Imagine pointing a powerful laser at the moon. / Not to light it up. / To ask it a question. / You fire a pulse at a reflector"

## Expected behaviour

A: dome and Moon both visible from frame 0; the slit opens and the telescope rises while the camera tilts toward the Moon, landing on "moon". B: starts inside the opening slit on the telescope, pulls back to dome + Moon by "moon". C: Earth limb + Moon; push to the station pin, pull up to the Moon. All: on "Not to light it up" a floodlight cone washes the Moon, a red NO mark appears and the cone collapses; on "To ask it a question" brackets lock on the Moon; on "fire" one pulse leaves and reaches the Moon 1.28 s later, on "reflector".

## Files

- `P03_opening_A_observatory_to_moon.mp4` (540x960, 30 fps, 291 frames, h264 yuv420p)
- `P03_opening_A_observatory_to_moon_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P03_opening_A_observatory_to_moon_start.png`, `P03_opening_A_observatory_to_moon_middle.png`, `P03_opening_A_observatory_to_moon_end.png`, `P03_opening_A_observatory_to_moon_frame_stats.json`
- `cue_P03_opening_A_observatory_to_moon_moon.png` (cue "moon", narration_t 3.10 s, frame 93)
- `cue_P03_opening_A_observatory_to_moon_not_light.png` (cue "not_light", narration_t 4.56 s, frame 137)
- `cue_P03_opening_A_observatory_to_moon_question.png` (cue "question", narration_t 6.52 s, frame 196)
- `cue_P03_opening_A_observatory_to_moon_fire.png` (cue "fire", narration_t 8.32 s, frame 250)
- `cue_P03_opening_A_observatory_to_moon_arrive.png` (cue "arrive", narration_t 9.30 s, frame 279)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p03.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P03
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P03_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P03_opening_A_observatory_to_moon: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 291 of 291 expected |
| P03_opening_A_observatory_to_moon: frame-to-frame change | info | mean abs diff 0.677, max 3.943, min 0.002 (0-255 luma, 1/4 res); frames with ~no change: 16 of 291; max pixel luma 240; max step of mean luma 0.62 |
| A: at "moon." (2.80 s) the Moon AND the aperture/station are both on screen | PASS | moon (796, 329) r101, aperture (476, 1307) |
| A: frame 0 shows the subject (aperture/station on screen) | PASS | aperture at t=0 (668, 1112); Moon on screen at t=0: True |
| A: camera move lands on "moon." (Moon screen speed falls) | PASS | before 5 u/s, 0.3 s after 0 u/s |
| A: Moon readable at phone size (screen radius >= 45 units at "moon.") | PASS | r = 101 |
| A: layer overscan (assert) | PASS | min margin 23 |
| pulse travels in real time: arrival - launch = 1.28 s and lands on "reflector" (9.10) | PASS | launch 7.92, arrive 9.20 |
| no premature answer: no pulse before "fire" (7.84) | PASS | launch 7.92 |
| the wrong idea (cone) is gone before "To ask" (5.56) | PASS | cone off at 5.21 |
| telescope drive has no overshoot (lean is monotonic while slewing) | PASS | lean 38 -> 6 deg |

## Start / middle / end frames

P03_opening_A_observatory_to_moon

![P03_opening_A_observatory_to_moon start](P03_opening_A_observatory_to_moon_start.png)
![P03_opening_A_observatory_to_moon middle](P03_opening_A_observatory_to_moon_middle.png)
![P03_opening_A_observatory_to_moon end](P03_opening_A_observatory_to_moon_end.png)

## Defects I found by viewing frames

- (not yet reviewed)

## Corrections made

- (none yet)

## Re-test result

- (not yet re-tested)

## Scientific verification

No continuous beam to the Moon is drawn (the cone is the marked WRONG idea). The pulse is a symbol, drawn as a dot, moving in REAL time (1.28 s Earth-Moon, C02). Observatory = generic illustration (Codex B4M/B4L/B4L2/B4P), never captioned as Apache Point. Moon = LRO colour map; Earth = Blue Marble. C carries NOT TO SCALE.

---
Status words used: `candidate`. Nothing here is `approved`.
