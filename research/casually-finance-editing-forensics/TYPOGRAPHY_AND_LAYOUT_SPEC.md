# Typography and layout spec (PRELIMINARY, n = 38 Shorts of 48 local videos of 210 public; measured on 360x640 and 720x1280 sources; snapshot 2026-10-20 night)

All coordinates are fractions of frame width/height (0,0 = top-left). Exact typefaces, weights and hex colours are **UNKNOWN**: the sources are low-resolution H.264 and no font file was inspected. Do not infer a font name. Re-express in your own font and palette; do not reuse pixels.

## Canvas
- Vertical 9:16 Shorts, 720x1280 originals (SnapYT copies 360x640). White (near-white, slightly cream in some 720p clips) canvas; no frame, no vignette.
- Timeline fps 24, delivered at 30 fps in the 08-19..09-15 sample videos and the 2026-06-01 `JsK53moCyZA` (25 files; every fifth frame repeated in the 12 where the phase could be measured, 13 unresolved) and at 24 fps in the 09-19..10-18 sample videos (13 files, 8 native, 5 unresolved) (`MEASURED`).

## Layout A — banded (sample: 13 of 38 videos, among them `Qof71Ef-3EU`, `DEgQTSsSX9U`, `06pN9dDvVVU`, `gGNVpOo7BK8`, `JztI-l-0-x4`)
| Band | y range (fraction of height) | Content | Behaviour |
|---|---|---|---|
| Headline | 0.206-0.294 (two lines, ~0.04 line height) | Hand-set title text, black, casual humanist look; matches the public title in 0 of the 3 newest banded videos (one paraphrases it) | Zero pixel change while present (`MEASURED`); in 3 of the newer banded videos it is removed at one cut (13.5, 16.3 and 27.3 s) and never returns |
| Stage | 0.30-0.665 | Characters, props, charts, screenshots, one scene at a time | Changes by one-frame replacement or pop |
| Caption | 0.69-0.77 | 1-2 lines, ~0.028 height, black, words append | Word appears whole on the ASR onset (per-video medians +13 to +53 ms, median of medians +33 ms, 64-83 % within ±100 ms; 14 videos); the line grows phrase by phrase ('it's', 'it's the fastest', ...) and the chunk clears every 5 words (median; p10 3, p90 9; max 14) |
| Safe margin | y > 0.80 and y < 0.20 empty | — | Reserved for platform UI (inferred) |
Captions end at f1884 (62.8 s) in `Qof71Ef-3EU`: the last three sentences are uncaptioned.

## Layout B — full-bleed (sample: 24 of 38 plus the small-stage variant below; two of them, `ud1ESmogrFY` and `f_ZCoPKLpyU`, keep a headline for the first 8.1 s and 19.3 s)
- No persistent headline; a title may appear for the first 4-6 s (`mT2hOLrCYSk`, `44ggG2I6JPY`).
- Screenshot/chart/photo layers fill the frame behind everything and may scroll/zoom; characters and props sit above; captions on top.
- Captions are hand-lettered marker text, black, **position changes per scene** (top-left, centre, lower third, beside an object); words append at ASR onset (timing not measured in this layout).
- Emphasis words/numbers are separate layers, 3-6x the caption size, in **red** (warnings, negatives, key figures), **green** (growth, '3%', 'right to wait', '$101') or black (neutral numbers); they pop in one frame above the caption, at or up to 80 ms before the spoken word in 10 of 13 measured cases (`MEASURED`; the other three lead by 0.16-0.53 s).

## Layout C — small centred stage (sample: 1 of 38, `JsK53moCyZA`, 2026-06-01)
- All picture changes sit in rows 0.366-0.722 of the frame (about 0.36 of its height); the top 0.37 and the bottom 0.28 stay white from the first to the last frame; no headline. A small typed caption occupies the bottom edge of the band (y 0.69-0.72). Charts, characters and logos are small. Cuts change 6-31 % of the band (2-11 % of the full frame). `MEASURED` (row profile); no era-wide claim is made from one video.

## Text behaviours observed
- **Append-by-word captions** (214 events in one video, all whole-word pops). **Clear-and-restart** when the chunk ends.
- **Write-on / reveal**: 8 `TEXT_WRITE_ON` events in 8 videos: red notes beside an equals sign, '48 hours later...' typed in steps every ~3 frames (`bF9WVzzS4ds`), a red hand-lettered phrase written in over 5 frames (`H3PRCteue9Y`).
- **Large number pops** (92 emphasis-text appearances in 27 videos at n = 32): '58%', '$429,000', '18.1%', '+1.8%', '-3.2B', '$ PER SHARE', '$74B', '$60B', '6%', '3.8', '1998', '50', '$131,000'; newer: red '100%', '120%', '2031', '5.3%,', '$4B', '$40T', 'since 2001', green 'three full points' and 'of all time' typed inside the caption line, red 'in 19 years', yellow '30-year debt', 'COMBINED!' and 'that's a horrible deal'.
- **Text on objects**: tiny handwritten labels on timelines ('Principal returned at maturity', 'Interest payments', year ticks) and on bond tags ('30 yrs', '5 yrs'); legible only at full resolution, small at 360p.
- **Asides**: speech bubbles whose text swaps in one frame ('Pls don't leave me!' to 'I'll stay for them dollars') and tiny captions next to a prop ('his glasses were thick AF'); the wording is not in the narration (`DIRECTLY_OBSERVED`).
- **Captions on dark or photo scenes** are white lettering (`rSa2aziEsAI` red-vignette and photo scenes, outline not verified); on white scenes they are black marker text, 1-3 lines, sometimes bottom-left beside a figure.
- **Source text** is raster (screenshot) and often too small to read on a phone; the video enlarges the supporting fragment (push-in, scroll) and highlights it (yellow/orange/green/blue marker).

## Reading-time facts (MEASURED)
Scene holds: median 1.7-5.7 s per video; shortest ~0.03 s (single-frame scenes), longest 16.0 s (`UJEqqBpH18k`, a source page). Caption chunk of 5 words at ~3-4 words/s ≈ 1.3-1.7 s.

## Mobile readability notes (ART_DIRECTION_INFERENCE)
Caption height ~0.028 of frame height is ~36 px on a 1280-px frame; legible only because the caption is black on white. Anything smaller than ~0.02 (tiny labels, filing text) is decoration, not reading material.
