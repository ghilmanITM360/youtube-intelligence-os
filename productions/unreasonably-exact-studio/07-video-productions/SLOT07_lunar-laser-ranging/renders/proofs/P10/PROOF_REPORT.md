# P10 Pulse accumulation (peak emerges from noise)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B27 start 61.65 ("from many laser pulses"), counter ramps through B28/B29 time, peak marker on "returns" (B29b anchor 70.59); clip narration_t 61.40-72.00

## Expected behaviour

Dark field with a time axis. Detections from successive laser pulses stack as one dot per detection in 40 time bins (dots, then bars as counts grow). The pulse counter ticks up, accelerating until 'returns' and then settling. Flat background builds everywhere, and a peak builds in one bin; the data-derived peak marker (argmax of the smoothed histogram) pops on 'returns' once it is statistically significant. 'ILLUSTRATIVE COUNTS' badge throughout.

## Files

- `P10_pulse_accumulation.mp4` (540x960, 30 fps, 345 frames, h264 yuv420p)
- `P10_pulse_accumulation_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P10_pulse_accumulation_start.png`, `P10_pulse_accumulation_middle.png`, `P10_pulse_accumulation_end.png`, `P10_pulse_accumulation_frame_stats.json`
- `cue_P10_pulse_accumulation_many_pulses_B27_start.png` (cue "many_pulses_B27_start", narration_t 63.90 s, frame 11)
- `cue_P10_pulse_accumulation_pulses_anchor.png` (cue "pulses_anchor", narration_t 64.86 s, frame 40)
- `cue_P10_pulse_accumulation_returns_peak.png` (cue "returns_peak", narration_t 73.66 s, frame 304)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p10.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P10
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P10_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P10_pulse_accumulation: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 345 of 345 expected |
| P10_pulse_accumulation: frame-to-frame change | info | mean abs diff 0.136, max 1.163, min 0.000 (0-255 luma, 1/4 res); frames with ~no change: 17 of 345; max pixel luma 240; max step of mean luma 1.08 |
| counter monotonic | PASS | final 1851 pulses |
| counter accelerates until "returns" then settles (peak rate near the anchor) | PASS | peak rate 384 pulses/s at 73.70 s; anchor 73.66 |
| peak not significant early (z < 3 at 200 pulses) | PASS | z={50: np.float64(1.2), 200: np.float64(2.8), 500: np.float64(4.3), 1000: np.float64(5.8), 1570: np.float64(8.0), 2400: np.float64(8.9)} |
| peak significant at "returns" (z >= 8 at n=1570) | PASS | z=8.0 |
| data-derived peak sits on the true time bin (+-1) | PASS | argmax bin 24, true bin 24 |
| peak was NOT already significant 1.5 s before the anchor (emerges, does not pre-exist) | PASS | z=6.1 |
| background is flat Poisson noise (variance/mean of off-peak bins) | PASS | dispersion 0.74 |
| histogram picture is a pure function of the counter (same n -> identical pixels) | PASS | md5 equal for repeat render, different for n=900 vs 1100 |
| bin counts never decrease as pulses accumulate | PASS | sampled every 125 pulses |
| tallest bar height changes smoothly (max step per frame) | PASS | max step 44.0 design units/frame |

## Start / middle / end frames

P10_pulse_accumulation

![P10_pulse_accumulation start](P10_pulse_accumulation_start.png)
![P10_pulse_accumulation middle](P10_pulse_accumulation_middle.png)
![P10_pulse_accumulation end](P10_pulse_accumulation_end.png)

## Defects I found by viewing frames

- v1: the pulse counter and the data-derived peak marker shared the same screen band (counter at y 560-610, marker at ~625), so a tall peak crowded the number.
- v1 check bug: the purity test compared n=900 and n=901, which are equal when pulse 900 happens to detect nothing.
- Open: top 25% and bottom 20% of the frame are empty; captions are off (because B28/B29 are intercut in the film); the counter shows only ~1,850 pulses while real APOLLO runs are 5,000 shots (illustrative); peak is only about 3x the background at the end, honest for the chosen rates but less dramatic than a hand-drawn peak; only stills viewed.

## Corrections made

- Plot moved down 60 units, counter moved up to y 490/545; purity test compares n=900 vs 1100; counter profile made a single in-quad ramp (rate rises until 'returns') followed by an out-quad settle so the rate is continuous at the anchor.

## Re-test result

- Re-rendered, stills at 1.5, 5.0, 8.9, 10.2 s re-viewed (dots -> bars -> peak marker). Checks PASS incl. 'peak not already significant 1.5 s before the anchor' (z 6.0 vs threshold 8.0) and peak bin equals the true bin.

## Scientific verification

The histogram is a deterministic simulation (seed 2013): per pulse Poisson(0.04) signal photons ~ N(0.62, 0.028) plus Poisson(0.25) uniform background, bins = 40. It is labelled illustrative (C08). Statistics are honest: the width of the signal never narrows artificially, the peak simply rises above Poisson noise as counts grow; the marker position is computed from the data (argmax of the 3-bin smoothed counts), not placed by hand. NOTE: in the film B28 (three dots) and B29 (atmosphere) are cut between B27 and B29b; the histogram is a pure function of the pulse count so the cut-away costs nothing. This proof shows it uninterrupted; the narration-aligned captions are therefore not drawn. Error bar shrinking (B30) and the '1 mm = 6.7 ps' figure are not in this clip.

---
Status words used: `candidate`. Nothing here is `approved`.
