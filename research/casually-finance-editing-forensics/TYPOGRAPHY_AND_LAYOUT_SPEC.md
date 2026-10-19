# Typography and layout spec (PRELIMINARY, n = 12 Shorts; measured on 360x640 and 720x1280 sources)

All coordinates are fractions of frame width/height (0,0 = top-left). Exact typefaces, weights and hex colours are **UNKNOWN**: the sources are low-resolution H.264 and no font file was inspected. Do not infer a font name. Re-express in your own font and palette; do not reuse pixels.

## Canvas
- Vertical 9:16 Shorts, 720x1280 originals (SnapYT copies 360x640). White (near-white, slightly cream in some 720p clips) canvas; no frame, no vignette.
- Timeline fps 24, delivered at 30 fps in the Aug 21-Sep 15 sample videos (every fifth frame repeated) and 24 fps in the Sep 25-Oct 18 sample videos (`MEASURED`).

## Layout A — banded (sample: `Qof71Ef-3EU`, `DEgQTSsSX9U`; flagged in 6 further 09-05..09-14 videos)
| Band | y range (fraction of height) | Content | Behaviour |
|---|---|---|---|
| Headline | 0.206-0.294 (two lines, ~0.04 line height) | Hand-set title text, black, casual humanist look; does not match the public title | Zero pixel change for the whole video (`MEASURED`) |
| Stage | 0.30-0.665 | Characters, props, charts, screenshots, one scene at a time | Changes by one-frame replacement or pop |
| Caption | 0.69-0.77 | 1-2 lines, ~0.028 height, black, words append | Word appears whole on the ASR onset (median +33 ms); chunk clears every 5 words (median; p10 3, p90 9; max 14) |
| Safe margin | y > 0.80 and y < 0.20 empty | — | Reserved for platform UI (inferred) |
Captions end at f1884 (62.8 s) in `Qof71Ef-3EU`: the last three sentences are uncaptioned.

## Layout B — full-bleed (sample: 8 of 10)
- No persistent headline; a title may appear for the first 4-6 s (`mT2hOLrCYSk`, `44ggG2I6JPY`).
- Screenshot/chart/photo layers fill the frame behind everything and may scroll/zoom; characters and props sit above; captions on top.
- Captions are hand-lettered marker text, black, **position changes per scene** (top-left, centre, lower third, beside an object); words append at ASR onset (timing not measured in this layout).
- Emphasis words/numbers are separate layers, 3-6x the caption size, in **red** (warnings, negatives, key figures), **green** (growth, '3%', 'right to wait') or black (neutral numbers); they pop in one frame above the caption.

## Text behaviours observed
- **Append-by-word captions** (214 events in one video, all whole-word pops). **Clear-and-restart** when the chunk ends.
- **Write-on / reveal**: only 2 events (`TEXT_WRITE_ON`), red notes beside an equals sign.
- **Large number pops** (22 emphasis assets in 8 videos): '58%', '$429,000', '18.1%', '+1.8%', '-3.2B', '$ PER SHARE'.
- **Text on objects**: tiny handwritten labels on timelines ('Principal returned at maturity', 'Interest payments', year ticks) and on bond tags ('30 yrs', '5 yrs'); legible only at full resolution, small at 360p.
- **Source text** is raster (screenshot) and often too small to read on a phone; the video enlarges the supporting fragment (push-in, scroll) and highlights it (yellow/orange/green/blue marker).

## Reading-time facts (MEASURED)
Scene holds: median 1.7-4.1 s per video; shortest ~0.17 s (single-frame scenes), longest 14.3 s (`ffIiiPLDFdM`, a source page). Caption chunk of 5 words at ~3-4 words/s ≈ 1.3-1.7 s.

## Mobile readability notes (ART_DIRECTION_INFERENCE)
Caption height ~0.028 of frame height is ~36 px on a 1280-px frame; legible only because the caption is black on white. Anything smaller than ~0.02 (tiny labels, filing text) is decoration, not reading material.
