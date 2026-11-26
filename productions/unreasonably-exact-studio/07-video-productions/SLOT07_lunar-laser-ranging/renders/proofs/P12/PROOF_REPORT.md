# P12 Distance calculation (bar folds in half, readout on "distance")

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B33-B36, narration_t 78.80-85.40: "t" lands on "time," (79.76), c and the long bar land on "light," (81.85), the fold ends on "two." (83.13), the readout appears on "distance." (84.60)

## Expected behaviour

The stopwatch's 2.56 flies up and becomes the symbol t on 'time,'. 'c' and the multiply sign arrive on 'speed'/'light,' and the long round-trip bar (length c x t; outbound half warm, return half cool, hinge at the Moon level) grows out of Earth on 'light,'. On 'then divide by two' the hinge pulses (anticipation), the cool half folds over the warm half like a paper strip (cubic sweep that ends exactly on 'two.', small settle), 'd =' appears and '/ 2' lands on 'divide' / 'two.'. The one-way bar slides to its own lane right of the light lanes (it no longer sits on the return lane), the ruler fills, the readout '≈ 384,000 km / mean distance' appears on 'distance.' and d pops.

## Files

- `P12_distance_calculation.mp4` (540x960, 30 fps, 194 frames, h264 yuv420p)
- `P12_distance_calculation_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P12_distance_calculation_start.png`, `P12_distance_calculation_middle.png`, `P12_distance_calculation_end.png`, `P12_distance_calculation_frame_stats.json`
- `cue_P12_distance_calculation_time_t_lands.png` (cue "time_t_lands", narration_t 82.51 s, frame 27)
- `cue_P12_distance_calculation_light_bar_grows.png` (cue "light_bar_grows", narration_t 84.42 s, frame 84)
- `cue_P12_distance_calculation_then_hinge_pulse.png` (cue "then_hinge_pulse", narration_t 85.12 s, frame 105)
- `cue_P12_distance_calculation_fold_mid.png` (cue "fold_mid", narration_t 85.50 s, frame 116)
- `cue_P12_distance_calculation_two_fold_done.png` (cue "two_fold_done", narration_t 85.77 s, frame 124)
- `cue_P12_distance_calculation_distance_readout.png` (cue "distance_readout", narration_t 87.20 s, frame 167)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p12.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P12
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P12_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P12_distance_calculation: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 194 of 194 expected |
| P12_distance_calculation: frame-to-frame change | info | mean abs diff 0.469, max 3.760, min 0.067 (0-255 luma, 1/4 res); frames with ~no change: 0 of 194; max pixel luma 255; max step of mean luma 3.57 |
| bar halves: visible length 2D before the fold, D after (assert), free end lands on the Earth end | PASS | 2D=658.0 -> 329.0 ; y_end 1434.0 vs base 1434.0 ; edge-on at 90 deg: 329.0 |
| ASSERT round(d_km/1000)*1000 == 384000 with d_km = c*2.56/2/1000 (readout "≈ 384,000 km" is consistent with the displayed t) | PASS | c*2.56/2 = 383734 km -> 384,000 ; sourced mean 384,400 km -> 384,000 at 3 s.f. ; with t = 2.56444 s the formula gives 384400.0 km |
| folded bar has its own lane (>= 50 units from both light lanes and clear of the Moon disc) | PASS | bar x = 630 ; lanes at (514, 566) |
| event times equal the beat-map anchor words | PASS | t token lands on "time," 82.51; bar starts growing on "light," 84.42; fold ends exactly on "two." 85.77; readout appears on "distance." 87.20 |
| fold angle reaches pi at "two." and never exceeds it | PASS | theta(two.)=3.141593 |
| fold is anticipated (small lift before the sweep) | PASS | min theta -0.100 rad |
| readout region unchanged before "distance." (-0.20 s vs -0.10 s) and changed by the readout after (+0.25 s) | PASS | changed px before the anchor 0, after 2490 |
| readout alpha at the anchor is 0 and at +0.18 s is 1 | PASS | see render; alpha(anchor-0.01)=0.00 alpha(anchor+0.18)=1.00 |

## Start / middle / end frames

P12_distance_calculation

![P12_distance_calculation start](P12_distance_calculation_start.png)
![P12_distance_calculation middle](P12_distance_calculation_middle.png)
![P12_distance_calculation end](P12_distance_calculation_end.png)

## Defects I found by viewing frames

- v1: the flying '2.56 s' token and the 't' token overlapped at low alpha for ~0.25 s (a muddy double text), and the numeric token was small (56) compared to the 116-unit symbol.
- v1: the bar 'grew' with expo-out, so 95% of its length appeared within 0.15 s of 'light,' and read as a pop, not a build.
- v1: the 384,400 km panel overlapped the one-way bar after the slide, with the bar visible through the panel.
- v1 test bugs: fold-bar 'visible length' returned 0 at theta = pi (metric was wrong); the readout pixel test counted stars.
- Open: displayed arithmetic is rounded (see issue below); the leader line from the formula to the bar is faint; the folded bar sits on top of the return lane rather than replacing it; ruler ticks have no labels (no sourced scale numbers); 'mean distance' is two words of text on screen (design doc allows numbers/symbols only); only stills viewed.
- Lead review (2026-11-26): the folded bar sat on top of the return lane after the slide, and the rounded 384,400 km vs displayed 2.56 s arithmetic was inconsistent.
- First re-render after the lead's change: the longer text '\u2248 384,000 km' at size 56 overflowed its panel and the panel touched the bar. Fixed by text size 44 and bar lane at cx+90.

## Corrections made

- Token cross-fade shortened to the last 0.12 s before landing and the token scales 1 -> 2 in flight; bar growth now cubic in-out over 0.75 s from 'light,'; readout panel narrowed, opaque, moved right (+312); fold metric fixed (extent from Earth to the highest point); readout test now compares frames before and after the anchor.
- Readout changed to '\u2248 384,000 km' + 'mean distance' (lead decision): code asserts round(c*2.56/2/1000)*1000 == 384000 and that the sourced mean 384,400 km rounds to the same value. The folded one-way bar now slides to its own lane (x = cx+90, >= 50 units from both light lanes, clear of the Moon disc) instead of the return lane; readout panel re-centred (cx+300, half-width 182, text 44) to clear it.

## Re-test result

- Re-rendered; MP4 frames at 1.0, 2.6, 3.2, 3.9, 4.4, 5.9 s viewed: t arrives clean, bar builds, fold lands on 'two.', readout on 'distance.'. All checks PASS including 'readout region unchanged until the anchor, changed after'.
- Re-rendered; assertion and 'own lane' check PASS; end frame viewed again.

## Scientific verification

d = c t / 2 (C11, verified relationship); c = 299,792,458 m/s exactly. The fold is geometric: the free end of the return half travels y = hinge - L cos(theta) and lands on the Earth end at theta = pi (asserted), so out-and-back becomes one leg. The readout is '≈ 384,000 km' with the label 'mean distance' (owner/lead decision): 384,000 is both c*2.56/2 = 383,734 km and the sourced mean 384,400 km (C01, NASA) rounded to 3 significant figures, so the arithmetic on screen is consistent with the displayed t = 2.56 s (asserted in code).  The bar and schematic are NOT to scale (mark shown); the bar's lengths are a schematic 2D vs D, never a measured scale. Simple model (ignores atmosphere and array geometry, C11) is not stated on screen; add to the owner decision list if wanted.

---
Status words used: `candidate`. Nothing here is `approved`.
