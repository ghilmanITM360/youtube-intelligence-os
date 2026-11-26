# OPENING candidates A/B/C (narration 0 - 9.7 s)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B01-B04: "Imagine pointing a powerful laser at the moon. / Not to light it up. / To ask it a question. / You fire a pulse at a reflector"

## Expected behaviour

A: dome and Moon both visible from frame 0; the slit opens and the telescope rises while the camera tilts toward the Moon, landing on "moon". B: starts inside the opening slit on the telescope, pulls back to dome + Moon by "moon". C: Earth limb + Moon; push to the station pin, pull up to the Moon. All: on "Not to light it up" a floodlight cone washes the Moon, a red NO mark appears and the cone collapses; on "To ask it a question" brackets lock on the Moon; on "fire" one pulse leaves and reaches the Moon 1.28 s later, on "reflector".

## Files

- `OPEN_A_ground_cinematic.mp4` (540x960, 30 fps, 291 frames, h264 yuv420p)
- `OPEN_A_ground_cinematic_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `OPEN_A_ground_cinematic_start.png`, `OPEN_A_ground_cinematic_middle.png`, `OPEN_A_ground_cinematic_end.png`, `OPEN_A_ground_cinematic_frame_stats.json`
- `cue_OPEN_A_ground_cinematic_moon.png` (cue "moon", narration_t 3.10 s, frame 93)
- `cue_OPEN_A_ground_cinematic_not_light.png` (cue "not_light", narration_t 4.56 s, frame 137)
- `cue_OPEN_A_ground_cinematic_question.png` (cue "question", narration_t 6.52 s, frame 196)
- `cue_OPEN_A_ground_cinematic_fire.png` (cue "fire", narration_t 8.32 s, frame 250)
- `cue_OPEN_A_ground_cinematic_arrive.png` (cue "arrive", narration_t 9.30 s, frame 279)
- `OPEN_B_closeup_to_wide.mp4` (540x960, 30 fps, 291 frames, h264 yuv420p)
- `OPEN_B_closeup_to_wide_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `OPEN_B_closeup_to_wide_start.png`, `OPEN_B_closeup_to_wide_middle.png`, `OPEN_B_closeup_to_wide_end.png`, `OPEN_B_closeup_to_wide_frame_stats.json`
- `cue_OPEN_B_closeup_to_wide_moon.png` (cue "moon", narration_t 3.10 s, frame 93)
- `cue_OPEN_B_closeup_to_wide_not_light.png` (cue "not_light", narration_t 4.56 s, frame 137)
- `cue_OPEN_B_closeup_to_wide_question.png` (cue "question", narration_t 6.52 s, frame 196)
- `cue_OPEN_B_closeup_to_wide_fire.png` (cue "fire", narration_t 8.32 s, frame 250)
- `cue_OPEN_B_closeup_to_wide_arrive.png` (cue "arrive", narration_t 9.30 s, frame 279)
- `OPEN_C_earth_to_moon.mp4` (540x960, 30 fps, 291 frames, h264 yuv420p)
- `OPEN_C_earth_to_moon_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `OPEN_C_earth_to_moon_start.png`, `OPEN_C_earth_to_moon_middle.png`, `OPEN_C_earth_to_moon_end.png`, `OPEN_C_earth_to_moon_frame_stats.json`
- `cue_OPEN_C_earth_to_moon_moon.png` (cue "moon", narration_t 3.10 s, frame 93)
- `cue_OPEN_C_earth_to_moon_not_light.png` (cue "not_light", narration_t 4.56 s, frame 137)
- `cue_OPEN_C_earth_to_moon_question.png` (cue "question", narration_t 6.52 s, frame 196)
- `cue_OPEN_C_earth_to_moon_fire.png` (cue "fire", narration_t 8.32 s, frame 250)
- `cue_OPEN_C_earth_to_moon_arrive.png` (cue "arrive", narration_t 9.30 s, frame 279)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/opening.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py OPEN
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `OPEN_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| OPEN_A_ground_cinematic: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 291 of 291 expected |
| OPEN_A_ground_cinematic: frame-to-frame change | info | mean abs diff 0.664, max 3.982, min 0.001 (0-255 luma, 1/4 res); frames with ~no change: 16 of 291; max pixel luma 240; max step of mean luma 0.62 |
| OPEN_B_closeup_to_wide: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 291 of 291 expected |
| OPEN_B_closeup_to_wide: frame-to-frame change | info | mean abs diff 0.943, max 6.102, min 0.001 (0-255 luma, 1/4 res); frames with ~no change: 15 of 291; max pixel luma 240; max step of mean luma 1.20 |
| OPEN_C_earth_to_moon: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 291 of 291 expected |
| OPEN_C_earth_to_moon: frame-to-frame change | info | mean abs diff 1.110, max 7.769, min 0.051 (0-255 luma, 1/4 res); frames with ~no change: 0 of 291; max pixel luma 255; max step of mean luma 2.47 |
| A: at "moon." (2.80 s) the Moon AND the aperture/station are both on screen | PASS | moon (796, 329) r101, aperture (476, 1307) |
| A: frame 0 shows the subject (aperture/station on screen) | PASS | aperture at t=0 (668, 1112); Moon on screen at t=0: True |
| A: camera move lands on "moon." (Moon screen speed falls) | PASS | before 5 u/s, 0.3 s after 0 u/s |
| A: Moon readable at phone size (screen radius >= 45 units at "moon.") | PASS | r = 101 |
| B: at "moon." (2.80 s) the Moon AND the aperture/station are both on screen | PASS | moon (796, 329) r101, aperture (476, 1307) |
| B: frame 0 shows the subject (aperture/station on screen) | PASS | aperture at t=0 (889, 852); Moon on screen at t=0: True |
| B: camera move lands on "moon." (Moon screen speed falls) | PASS | before 179 u/s, 0.3 s after 0 u/s |
| B: Moon readable at phone size (screen radius >= 45 units at "moon.") | PASS | r = 101 |
| C: at "moon." (2.80 s) the Moon AND the aperture/station are both on screen | PASS | moon (681, 483) r153, aperture (477, 1275) |
| C: frame 0 shows the subject (aperture/station on screen) | PASS | aperture at t=0 (540, 1200); Moon on screen at t=0: True |
| C: camera move lands on "moon." (Moon screen speed falls) | PASS | before 1 u/s, 0.3 s after 0 u/s |
| C: Moon readable at phone size (screen radius >= 45 units at "moon.") | PASS | r = 153 |
| A: layer overscan (assert) | PASS | min margin 23 |
| B: layer overscan (assert) | PASS | min margin 63 |
| C: layer overscan (assert) | PASS | min margin 418 |
| pulse travels in real time: arrival - launch = 1.28 s and lands on "reflector" (9.10) | PASS | launch 7.92, arrive 9.20 |
| no premature answer: no pulse before "fire" (7.84) | PASS | launch 7.92 |
| the wrong idea (cone) is gone before "To ask" (5.56) | PASS | cone off at 5.21 |
| telescope drive has no overshoot (lean is monotonic while slewing) | PASS | lean 38 -> 6 deg |

## Start / middle / end frames

OPEN_A_ground_cinematic

![OPEN_A_ground_cinematic start](OPEN_A_ground_cinematic_start.png)
![OPEN_A_ground_cinematic middle](OPEN_A_ground_cinematic_middle.png)
![OPEN_A_ground_cinematic end](OPEN_A_ground_cinematic_end.png)

OPEN_B_closeup_to_wide

![OPEN_B_closeup_to_wide start](OPEN_B_closeup_to_wide_start.png)
![OPEN_B_closeup_to_wide middle](OPEN_B_closeup_to_wide_middle.png)
![OPEN_B_closeup_to_wide end](OPEN_B_closeup_to_wide_end.png)

OPEN_C_earth_to_moon

![OPEN_C_earth_to_moon start](OPEN_C_earth_to_moon_start.png)
![OPEN_C_earth_to_moon middle](OPEN_C_earth_to_moon_middle.png)
![OPEN_C_earth_to_moon end](OPEN_C_earth_to_moon_end.png)

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
