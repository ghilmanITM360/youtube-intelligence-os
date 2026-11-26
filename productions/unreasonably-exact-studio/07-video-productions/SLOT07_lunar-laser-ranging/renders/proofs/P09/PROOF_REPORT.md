# P09 Faint detection (sparse markers, no flash)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B26-B28, narration_t 58.30-66.20. Axis draws on at 58.55; a pulse-sent tick per row every 0.36 s; the click of row 6 lands on "photons" (61.29); the raster dims at 63.5; three markers light and hold from "few" (64.02).

## Expected behaviour

Dark field, a thin time axis. One tiny hollow tick per laser pulse appears at the left of its row; a detection (if any) shows as a small cool dot that fades in over 0.18 s with ONE thin expanding ring and then holds faintly. Most rows stay empty. In the pause before 'A few photons' the raster dims to black; three single markers (larger, soft ring) light one after another from 'few' and hold. 'ILLUSTRATIVE' marks the counts as not data.

## Files

- `P09_faint_detection.mp4` (540x960, 30 fps, 241 frames, h264 yuv420p)
- `P09_faint_detection_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P09_faint_detection_start.png`, `P09_faint_detection_middle.png`, `P09_faint_detection_end.png`, `P09_faint_detection_frame_stats.json`
- `cue_P09_faint_detection_photons_click.png` (cue "photons_click", narration_t 63.37 s, frame 88)
- `cue_P09_faint_detection_raster_dims.png` (cue "raster_dims", narration_t 65.62 s, frame 156)
- `cue_P09_faint_detection_few_three_dots.png` (cue "few_three_dots", narration_t 66.17 s, frame 172)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p09.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P09
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P09_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P09_faint_detection: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 241 of 241 expected |
| P09_faint_detection: frame-to-frame change | info | mean abs diff 0.084, max 0.832, min 0.000 (0-255 luma, 1/4 res); frames with ~no change: 102 of 241; max pixel luma 240; max step of mean luma 0.83 |
| no bright flash: max pixel luma over all frames (captions excluded) | PASS | max luma 172 of 255 (flash would be > 230) |
| no brightness pop: max frame-to-frame change of mean luma | PASS | max step 0.049 (0-255 scale) |
| sparse: lit pixels (luma>40) never exceed % of the frame | PASS | max 0.538 % |
| a detection click lands on "photons" (63.37 s) | PASS | click at 63.370 s, anchor 63.370 (word edges are +-0.12 s estimates) |
| exactly three markers hold at the end (connected blobs luma>60, area>12 px) | PASS | blobs=3 (all sizes [124, 124, 129]) |
| events: 14 rows, 6 detections, 8 of 14 rows empty | PASS | sparse by construction |

## Start / middle / end frames

P09_faint_detection

![P09_faint_detection start](P09_faint_detection_start.png)
![P09_faint_detection middle](P09_faint_detection_middle.png)
![P09_faint_detection end](P09_faint_detection_end.png)

## Defects I found by viewing frames

- v1: markers were 6 design units radius: on a 540-wide proof they read as specks and the per-row 'pulse sent' ticks were almost invisible.
- v1: after 0.8 s the three held markers lost their rings, so B28's 'each with a soft ring' was not met in the hold.
- v1 check bug: the 'exactly three markers' test counted the badge letters (42 blobs); the click time was 0.1 s late against the anchor (61.39 vs 61.29).
- Open: the upper 40% of the frame is empty early in the clip and the raster fills upward only slowly; the three final dots are placed by hand (not drawn from the simulated data); only stills were viewed.

## Corrections made

- Raster markers enlarged (x1.35, ring 52), tick marks brighter; held markers keep a faint static ring (alpha 0.3, no brightness cap exceeded); row timing shifted so the click lands on 'photons'; test masks the badge and counts blobs > 12 px.

## Re-test result

- Re-rendered; frames decoded from the MP4 at 1.5, 3.2, 4.6, 5.6, 6.4, 7.6 s viewed: sparse, no flash, dim-down before 'A few photons', three markers. Checks PASS: max luma 172 (no flash), max mean-luma step 0.05, lit area < 0.5% of the frame.

## Scientific verification

C08: LLR works in the single-photon regime; the best station sees about 1 photon per shot, most see far fewer, so 'a few photons' (three dots) is a fair illustration while sparse rows are the common case. The marker is an educational symbol (photons are not visible objects). The three dots are illustrative, not a data claim, and are labelled ILLUSTRATIVE. No number on screen.

---
Status words used: `candidate`. Nothing here is `approved`.
