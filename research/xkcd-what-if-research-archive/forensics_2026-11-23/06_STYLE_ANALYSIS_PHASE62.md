# 06 Phase 6.2: illustrated style, measured on 125 viewed frames (continuation, 2026-11-23)

Status: **MEASURED (pixel statistics) + OBSERVED (two overlay sheets and one validation sheet viewed, one coder)**. Self-review, no independent review.
Sample: the 125 frames already coded in Phase 7 (87 long-form frames from 44 videos, 38 Short frames from 38 videos; 82 videos). They were chosen at "quantity moments" (a number or comparison on screen), **not at random**, so they over-represent diagram and label frames. Each row of `06_STYLE_MEASUREMENTS_125.csv` carries `video_id`, `t_s` and `frame_ref` (native-resolution frame re-extracted from the library MP4 into `phase62_style/frames/`). Code: `scripts/phase62_style.py`, `phase62_check.py`, `phase62_figures.py`.

## How each metric was measured
| Metric | Definition (all thresholds in the script) | Check |
|---|---|---|
| Background | most frequent colour after 16-level quantisation; share of pixels | |
| Ink | non-background pixels that are near-neutral (saturation < 0.25) and dark (luminance < 110); on dark backgrounds, light (> 150) | validation sheet: masks follow the drawn lines on light and dark frames |
| Red accent | non-background, R > 140, G and B < 110, saturation > 0.45 | |
| Other accent | any other saturated colour (saturation > 0.45) | |
| Grey fill | non-background neutral pixels of luminance >= 110 | |
| Stroke width | 2 x median distance-transform value on the ink skeleton, only skeleton points whose local radius is <= 8 px (thin strokes); frames where more than half of the ink is filled area (silhouettes) are excluded | **accuracy about +-1 to 2 px** (integer pixel grid, anti-aliasing, compression); a frame such as `FkUNHhVbQ1Q` t=92.69 gives 2 px from halo edges and is an artefact |
| Negative space | share of 48 x 48 px grid cells with no non-background pixel | |
| Density | connected ink components after 2-px dilation | outlier `_efsqO-4OoQ` t=23.41 (16,622, negative space 0) is a full-frame texture and was not inspected in detail |
| Label-sized component height | median height of ink components 10 to 90 px high (text glyphs plus small marks) | a proxy for lettering size, not OCR |
| Head and figure | filled-hole disk (head ring, 22 to 240 px) inside the top third of a tall component; figure height = component bbox | all 24 frames with candidates viewed on the overlay sheet; 1 false positive removed (the jetpack in `IdlQsjq5vKo`); includes raised arms and held objects in the bbox |

## Results (median, IQR in the CSV)
| Property | Long-form (87 frames) | Shorts (38 frames) |
|---|---|---|
| Light background (248 grey) | 61 of 87 | 27 of 38 |
| Near-black or dark background | 14 of 87 | 7 of 38 |
| Ink share of frame | 5.5% | 2.9% |
| Negative space | 0.66 | 0.77 |
| Thin-stroke width, native px (silhouette frames excluded) | **6.3** (n=63; 23 excluded) | **5.7** (n=31; 7 excluded; recount 2026-11-23, earlier text said n=30 and 8) |
| Frames with a red accent | 30 of 87 (34%) | 9 of 38 (24%) |
| Red share of frame when present | at most 2.7% (`jgafb8G7i4o` t=155.46); median 0 over all frames | at most 2.2% (`XvvXDEtMfhw` t=58.12) |
| Red stroke width | 6.3 px (n=30) | 4.5 px (n=11) |
| Frames with another saturated colour above 0.2% of the frame | 6 of 87 (max 4.4%, `r7B0MzvwDcA` t=57.08) | 1 of 38 |
| Grey fill, median share | 1.5% (up to 56%, `fs28lEq9smw` t=85.92 and `JqFSGkFPipM` t=110.62: maps and silhouettes) | 1.4% |
| Connected ink components | 34 (IQR 17 to 64) | 28 (IQR 11 to 66) |
| Label-sized component height | 36 px | 30 px |
| Frame size | 1920 x 1080 | 1080 x 1920 (same shorter side) |

Figures (stick-figure candidates, 27 after removing the false positive, 23 frames): height over head diameter **3.5** (IQR 3.2 to 3.7; long 3.5 n=19, Short 3.3 n=8); head diameter about 158 px (long) and 189 px (Short) on a 1080 px short side, i.e. the head is about **15 to 18% of the frame's short side** when a figure is the subject, and about **29% of the figure's height**. The head is an empty ring, the body is a single thin line with a line neck, arms and legs; no fill in these 23 frames.

## What the viewing added (OBSERVED, 8 validation frames + 24 figure-overlay frames, one coder)
- The palette is **achromatic by default**: dark linework on a near-white ground, or white linework on near-black, with mid-grey for maps, ground planes and bodies of water. **Red** is the one repeated accent: arrows, a strike-through, a ring or bracket, and numerals when a quantity is emphasised. A few frames add one other colour (for example a blue-grey chair), always small.
- Lettering is a single hand-lettered sans family in mostly capitals for labels (`MOON (TOO CLOSE)`, `LIMIT: 4 Gs`), with mixed-case handwriting for equations. Question cards use a grey rounded panel with a regular sans (`alBQCm0QpJg`, `GgEGcxJRDik`). OCR was not available, so typography was not measured beyond glyph height.
- Objects are line drawings with sparse hatching; silhouettes (black filled shapes such as skylines, craters, a drilling shaft) appear on dark frames. Whiteboard or chalkboard panels carry equations in several frames (`UXA-Af-JeCE`, `DDNMLh1I_jY`, `BnGqPxnQh9A`).
- Perspective is flat and side-on in all viewed frames (no vanishing-point drawing); globes and the Earth are drawn as outlines with grey continents.

## Limits
1. Sample is quantity moments, not scenes; no claim about "the typical frame".
2. Stroke width has about +-1 to 2 px error and is excluded on silhouette frames (31 of 125), so it describes line-art frames only.
3. Figure proportions come from a ring-detection heuristic checked by eye on 24 frames; expressions and poses were not coded.
4. **The video artwork was not compared with the static What If blog or book illustrations.** No book image was measured, so "same drawing grammar as the book" is UNVERIFIED either way (directive 6.2 warning).
5. Colour is a pixel statistic of compressed video; exact brand values are not claimed.
6. Not measured: line irregularity, outline hierarchy beyond thin versus filled, expression, perspective beyond the viewed frames.
