# P11 Stopwatch sync (final reading exactly 2.56 s)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B06-B07, narration_t 10.80-18.00: stopwatch on "how" (11.42), pulse and clock start on "light" (12.81), stop on "seconds." (16.14)

## Expected behaviour

Stopwatch (analog dial + digital) fades in at 0.00 on 'how long'. On 'light' the emission ring contracts onto the launch station (anticipation) and the pulse bead leaves, the clock starts. Pulse and stopwatch both read the same model clock, played in slow motion (badge 'SLOW-MOTION xN ILLUSTRATIVE'; never real time). The bead touches the Moon ring exactly at reading 1.28, returns on the cool lane, and the stopwatch freezes on 2.56 as the bead reaches Earth on 'seconds.' (spring kick, hand and digits lock). A gentle punch-in toward the stopwatch lands with the stop. NOT TO SCALE mark visible.

## Files

- `P11_stopwatch_sync.mp4` (540x960, 30 fps, 202 frames, h264 yuv420p)
- `P11_stopwatch_sync_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P11_stopwatch_sync_start.png`, `P11_stopwatch_sync_middle.png`, `P11_stopwatch_sync_end.png`, `P11_stopwatch_sync_frame_stats.json`
- `cue_P11_stopwatch_sync_how_stopwatch_in.png` (cue "how_stopwatch_in", narration_t 12.39 s, frame 28)
- `cue_P11_stopwatch_sync_light_emit.png` (cue "light_emit", narration_t 13.69 s, frame 67)
- `cue_P11_stopwatch_sync_moon_turn_1.28.png` (cue "moon_turn_1.28", narration_t 15.28 s, frame 114)
- `cue_P11_stopwatch_sync_seconds_stop_2.56_(+0.1s).png` (cue "seconds_stop_2.56_(+0.1s)", narration_t 16.97 s, frame 165)
- `ASSERT_RESULT_final_reading.txt`
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p11.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P11
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P11_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P11_stopwatch_sync: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 202 of 202 expected |
| P11_stopwatch_sync: frame-to-frame change | info | mean abs diff 1.166, max 8.222, min 0.065 (0-255 luma, 1/4 res); frames with ~no change: 0 of 202; max pixel luma 255; max step of mean luma 6.73 |
| ASSERT: displayed final reading is exactly "2.56" and model_t == 2.56 on every frame after the stop | PASS | reading='2.56', model_t=2.56; written to ASSERT_RESULT_final_reading.txt |
| derived value consistent with claim C01 | PASS | 2*384400 km / c = 2.5644 s, rounds to 2.56 |
| pulse position vs displayed reading (pixel centroid, 40 sampled frames) | PASS | max /dy/ = 7.4 design units (reading quantised to 0.01 s = 5.3 units/step; trail biases centroid backward) |
| turn-around at the Moon at reading 1.28 | PASS | n=15.280 m=1.2800 |
| slow-motion factor is shown (badge) and finite | PASS | x1.24; beat-map note: "2.56 s inside 3.3 s of speech" |
| model clock monotonic, constant rate while running | PASS | rate 0.02667 model s per frame while running |
| star layer overscan covers the camera range (assert) | PASS | min margin 419 world units |

## Start / middle / end frames

P11_stopwatch_sync

![P11_stopwatch_sync start](P11_stopwatch_sync_start.png)
![P11_stopwatch_sync middle](P11_stopwatch_sync_middle.png)
![P11_stopwatch_sync end](P11_stopwatch_sync_end.png)

## Defects I found by viewing frames

- v1: the digital readout box sat on top of the dial numerals 1 and 2 (visible in the 2.30 s frame).
- v1: the Earth looked smeared (1024x512 procedural texture magnified ~5x) and drew attention away from the stopwatch.
- v1: the stopwatch crown touched the 'NOT TO SCALE' mark after the punch-in.
- v1 test bug: the final-reading assertion started one frame before the stop (found because the assert fired: model_t was 2.5549 on frame 160).
- Open: the slow-motion factor (1.30) differs from the design doc's ~1.8 (documented departure); the punch-in is toward the stopwatch with the whole diagram, so the Earth limb rises into the caption band; the arrival ring on Earth is small and partly hidden behind the caption scrim; only stills viewed.

## Corrections made

- Readout moved into a pill under the dial; Earth textures raised to 4096x2048 and pre-built before forking workers; stopwatch moved down 42 units; assertion range fixed (ceil).

## Re-test result

- Re-rendered: frames at 1.0, 2.5, 3.9, 5.0, 5.5, 5.6 s viewed. ASSERT final reading '2.56' and model_t == 2.56 on every frame after the stop: PASS (file ASSERT_RESULT_final_reading.txt). Pixel check: bead centroid vs displayed reading within 6.9 design units over 40 frames.

## Scientific verification

2 x 384,400 km / c = 2.5645 s (claim C01, verified, derived from the NASA mean semi-major axis); displayed value 2.56. One leg = 1.28 s (C02). The picture is a non-scale schematic (declared). The pulse is an educational symbol (no visible beam). The slow-motion badge states the time stretch; the stopwatch ends on the TRUE value. Departure from SCIENTIFIC_VISUAL_DESIGN V2 (which proposes the whole 11.4-16.1 s window, factor ~1.8): the clock here starts when the voice says 'light' (factor ~1.3), matching the beat map's 'pulse starts on light' and 'real time (2.56 s inside 3.3 s of speech)'. No speed-of-light or distance number appears.

---
Status words used: `candidate`. Nothing here is `approved`.
