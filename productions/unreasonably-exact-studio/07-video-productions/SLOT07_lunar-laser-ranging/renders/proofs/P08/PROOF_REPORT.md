# P08 Light journey (there and back, 1.28 s each way)

**Status: candidate.** Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).

Beats / timing: B08-B11, narration_t 17.20-26.40. Outbound lights on "there" (18.19), return on "and back" (18.51), arc split on "way." (20.91), leg 1 lands on "moon" (23.48), leg 2 lands at the end of "return." (25.62)

## Expected behaviour

The stopwatch (frozen 2.56 from B07) gets a bracket arc over the whole interval on 'Not'; a ghost '2.56 s' label (the wrong idea 2.5 s each way) is struck out on 'each'; on 'way.' the dial arc splits at the half into a warm 1.28 and a cool 1.28 and matching leg brackets appear beside the lanes. The dial rewinds to 0.00, the pulse leaves, climbs the warm lane while the stopwatch counts 0 -> 1.28, lands on the Moon ring on 'moon' (leg label locks with a spring pop), returns down the cool lane while the stopwatch counts 1.28 -> 2.56 and stops on 2.56 at Earth. Pulse and stopwatch share one model clock (slow motion, badge 'SLOW-MOTION x1.2 ILLUSTRATIVE').

## Files

- `P08_light_journey.mp4` (540x960, 30 fps, 260 frames, h264 yuv420p)
- `P08_light_journey_audio_preview.mp4` (same video + slice of the master voice, preview only; master untouched)
- `P08_light_journey_start.png`, `P08_light_journey_middle.png`, `P08_light_journey_end.png`, `P08_light_journey_frame_stats.json`
- `cue_P08_light_journey_there_outbound_lights.png` (cue "there_outbound_lights", narration_t 18.19 s, frame 19)
- `cue_P08_light_journey_not_arc.png` (cue "not_arc", narration_t 19.10 s, frame 46)
- `cue_P08_light_journey_way_split.png` (cue "way_split", narration_t 20.89 s, frame 100)
- `cue_P08_light_journey_launch_leg1.png` (cue "launch_leg1", narration_t 22.03 s, frame 134)
- `cue_P08_light_journey_moon_1.28.png` (cue "moon_1.28", narration_t 23.38 s, frame 175)
- `cue_P08_light_journey_launch_leg2.png` (cue "launch_leg2", narration_t 24.13 s, frame 197)
- `cue_P08_light_journey_return_2.56.png` (cue "return_2.56", narration_t 25.48 s, frame 238)
- `PROOF_REPORT.md` (this file)

Source: `animation/proofs/p08.py` + package `animation/uemotion/`.

## How to re-render

```
cd /Users/ghilmanislam360/workprojects/unreasonably-exact/lunar-laser-ranging
~/.venvs/uepipe/bin/python animation/render_proofs.py P08
```
Deterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `P08_1080/`).

## What was checked programmatically

| check | result | detail |
|---|---|---|
| P08_light_journey: container | PASS | h264, yuv420p, 540x960, r_frame_rate 30/1, decoded frames 260 of 260 expected |
| P08_light_journey: frame-to-frame change | info | mean abs diff 0.511, max 3.839, min 0.073 (0-255 luma, 1/4 res); frames with ~no change: 0 of 260; max pixel luma 255; max step of mean luma 3.15 |
| stopwatch model clock: 1.28 at the Moon, held 1.28 during the pause, 2.56 at Earth | PASS | m(moon)=1.2800 m(hold)=1.2800 m(home)=2.5600 |
| both legs play at the same slow factor (badge stays true) | PASS | x1.055 (out) vs x1.055 (return) |
| colour grammar: outbound bead warm (R>B), return bead cool (B>R) | PASS | out (246, 209, 164), return (174, 222, 250) |
| pulse reaches the Moon at model 1.28 and turns | PASS | p before 1.00000 after 1.00000 |
| split lands at the half: angle(1.28)/angle(2.56) == 0.5 | PASS | 1.28 + 1.28 = 2.56 |
| reveal times come from words/beat anchors | PASS | {'there': 18.19, 'and_back': 18.51, 'not_': 19.1, 'each_way': 20.89, 'moon': 23.38, 'ret': 25.48} |

## Start / middle / end frames

P08_light_journey

![P08_light_journey start](P08_light_journey_start.png)
![P08_light_journey middle](P08_light_journey_middle.png)
![P08_light_journey end](P08_light_journey_end.png)

## Defects I found by viewing frames

- v1: two-line captions broke as 'Not two and a half seconds each / way.' (a lone word on line 2) and the white text sat on bright cloud, low contrast.
- Found while viewing P11 (same stopwatch): the digital readout box covered the dial numerals 1 and 2. Fixed in the shared stopwatch, so it also applies here.
- Open: captions take three lines in other proofs; the 1.28 s labels are dimmed to 30% while counting and may read as disabled on a phone; the arc bracket around the dial sits close to the Moon when the dial is at top-left; the badge 'SLOW-MOTION x1.2 ILLUSTRATIVE' is wordy against the design doc's zero-sentence budget (kept because the brief asks for an illustrative-time badge); the return pulse reaches Earth at the END of 'return.' (25.62 s), not at the word start, and only the stills of this proof were viewed.

## Corrections made

- Caption renderer now balances two-line breaks and draws a dark scrim; stopwatch readout moved into its own pill under the dial; both legs forced to the same slow factor (1.2) so the badge number is true for the whole journey (asserted within 0.02).

## Re-test result

- Re-rendered, stills at 1.2, 2.9, 3.2-3.9, 5.3, 7.0, 8.4 s re-viewed: captions balanced, numerals clear, colour grammar correct. Checks PASS. The strike-through on the ghost 2.56 label was not captured in a still (it lasts ~0.3 s); its geometry is code-checked only by construction.

## Scientific verification

One leg = 384,400 km / c = 1.282 s (C02), shown as 1.28 s; whole = 2.56 s (C01). The split at the Moon is the same physical event for time and path. 'a little over a second' = 1.28 s is the MEAN (the distance varies, C03). Colour grammar warm out / cool back is checked by pixel sampling. The pulse moves at constant speed in model time (light does not ease). Non-scale schematic is declared. Honest limit: the return leg arrives at the END of 'return.' (25.62) rather than its first millisecond, because only 1.24 s separate 'and' and 'return' and the leg needs 1.28 s x slow factor; making both legs share one factor (1.2) was preferred over a faster return.

---
Status words used: `candidate`. Nothing here is `approved`.
