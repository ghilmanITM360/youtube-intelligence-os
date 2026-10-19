# Original character and asset creation spec (PRELIMINARY; broad technique only)

Basis: `ASSET_FAMILY_LIBRARY.csv` (10 validated Shorts: 20 families, 115 stick-figure appearances, 73 annotation overlays, 70 source-screenshot appearances, 33 financial-paper props, 31 money props, 24 country-map characters, 22 emphasis texts). Asset IDs are per-video analyst labels; "same asset" across videos means the same visual family or character as judged by the reviewer, not a verified identical file. **Design your own characters and props. Do not trace, recolour or crop the reference artwork.** Outline thickness, exact proportions, typefaces and hex colours were not measured (360p sources); calibrate your own at 1080x1920.

## 1. Style principles observed (`DIRECTLY_OBSERVED`)
Flat colour fills with thick uneven black outlines; very simple faces (dot or round eyes, one-line mouth, thin brows); thin stick limbs; props reduced to one silhouette plus one label; large amounts of white; red/green used for meaning (negative/positive); handwritten labels; photos, logos and screenshots mixed in only as evidence or jokes.

## 2. Asset families to build (reusability across topics)
| Family | What to make | Layers / rigging | Variants needed | Expected animation | Reuse |
|---|---|---|---|---|---|
| Presenter figure | 1 original character | head (3-4 expressions), torso, 2 arms (one with pointer), 2 legs | neutral, pointing, surprised, worried, smiling | pop-in, rise-in, slide-in, expression swap (visibility) | all topics |
| Supporting cast | 2-3 distinct figures (hair/clothes differ) | same rig, different head/hair | reaction faces | pop-in, bubble | all topics |
| Place/institution characters | map or building with eyes and legs | outline body, eyes (3 states), legs | eyes wide / half-lid | scale-in, eye swap, slide-in | per topic (countries for finance; organs for health) |
| Planet/system character | globe or organ with eyes | body, eyes, hands | 3 | scale 100 % / 45 % | finance, history |
| Money & finance props | bag, bill, coin, bond tag, document, check, bank, house, building | single flat layer each | 2 sizes | pop-in, drift, shrink, tear | finance only |
| Health props (original) | heart, pill, shoe, clock, cup, scale | single flat layer | 2 sizes | pop-in, rotation | senior health, medical |
| Annotation set | red X, green check, arrow (straight/curved), speech bubble, marker highlight, box | vector strokes with dash-offset | colours red, green, orange, yellow, blue | pop, stroke draw (linear), highlight width grow | all |
| Typography layers | caption layer, emphasis numbers (red/green/black), small labels | separate text layers above the stage | — | word-append, pop | all |
| Evidence cards | screenshot crop with source/date strip | raster layer + highlight layer | zoomed crops | scroll/push-in, highlight sweep | per topic (authorised sources only) |
| Effects | repeatable overlay clip (e.g. falling money bills) | alpha clip, looped | 1 loop, trimmed per use | loop | finance |

## 3. Reuse rules (measured pressure)
In the sample the same characters recur across videos (country-map character in 8 of 10, presenter in 7 of 10, Earth in 3, official figure in 3) and props recur within a video. Plan for **8-15 new props and 1-3 new characters per video** on top of the permanent kit; a new scene must still communicate a new beat, not only a recolour.

## 4. Technical specification
- Canvas 1080x1920; stage safe area y 0.20-0.80 (banded) or full frame (full-bleed); no text within 0.10 of top/bottom.
- Rig pivots: shoulder, elbow, neck; head swap by visibility. Expressions are separate head layers (avoid morphing).
- Props are single layers with transparent background, ~0.10-0.30 of frame width.
- Strokes (draw-on lines, arrows) are vector paths animated by stroke-dash offset at constant speed.
- Screenshots: crop to the supporting fragment, keep date/unit strip; push-in group scales around the fragment centre.
- Naming: `CH_*`, `PR_*`, `OV_*`, `SS_*`, `TY_*`, `FX_*` (matches the research IDs) so timelines are portable.

## 5. Rights and provenance
Competitor frames are **never** production assets. Third-party photos, logos, memes and screenshots seen in the sample (Avengers logo, meme photograph, news pages, filing pages) require their own licence or fair-use assessment; prefer original illustrations or public-domain/primary-source documents. Keep a provenance row per asset (source URL, licence, date).

## 6. Open gaps
Exact line weights, proportions and palette; whether the reference cast is one rig; production labour estimates (the playbook branch estimates 40-90 person-hours per 5-8 minute episode after a kit exists, `REFERENCE_SUPPORTED`).
