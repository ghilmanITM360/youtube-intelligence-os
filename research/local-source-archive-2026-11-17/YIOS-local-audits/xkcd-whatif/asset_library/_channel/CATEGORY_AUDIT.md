# xkcd's What If? — category sorting audit (P2, 2026-11-08, LOCAL ONLY)

## What was done
- `category_index.csv` tags all 2,755 unique clusters. Method = RULE_FROM_LEDGER_TEXT + PIXEL_FEATURES, **INFERRED** (not a per-frame human verdict). Tool: `~/YIOS-local-audits/tooling/asset_library/xkcd/categorize.py` (adapted copy; the CF keywords and peach-skin rule were removed; xkcd ledger words used instead: diagram/map/axis/inset/cutaway, question box/title card/footnote, stick/figure/crowd, named objects, scene/sky/horizon; plus off-white, dark and colour-field pixel fractions).
- `primary` counts: environments 759, characters 733, graphics_ui 463, typography 418, props 321, uncategorised 61. Tag hits (multi-tag): typography 2,139, environments 1,200, characters 1,163, props 1,123, graphics_ui 622, transitions 449.
- **Viewed: 240 of 2,755 clusters (8.7%)**, 467 member states, in 10 random 24-tile contact sheets (`review_sheets/xk_*.jpg`; tile → cluster in `*.members.csv`; `viewed_in_sheet` column in `category_index.csv`). Seeded random (20261108) within each primary category, long-form reps on 16:9 tiles (6 sheets), Shorts reps on 9:16 tiles (4 sheets). **All 44 videos** appear at least once as a tile's representative video. The other 91.3% are rule-tagged only.
- Notes written while each sheet was open: `review_sheets/VIEWING_NOTES.md`.
- One reader (this session). No reviewer subagent was used, so no second check.

## Purity verdicts (my reading, one reader)
| Sheet | Fit | Over-match / miss |
|---|---|---|
| long characters | figure present 24/24; figure-dominant ~18/24 | tiny or secondary figures in scenes still match "figure" |
| long environments | 24/24 non-white backdrops, ~15/24 real scenes/places | pixel rule (dark / non-white) pulls in colour maps (5) and dark diagrams (3) |
| long props | object-dominant ~14/24 | "board" pulls whiteboard text scenes; diagram objects; 1 landscape |
| long graphics_ui | 23/24 | reliable |
| long typography | text-dominant ~13/24, text present ~20/24 | weak "label/text" words pull labelled diagrams; 2 tiles had no visible text |
| long uncategorised | 24/24 fit an existing category | missing words: globe/equator/battery/plane/comment/number/quote |
| Shorts characters | figure present 21/24 | 3 tiles have no figure |
| Shorts environments | ~11/24 real scenes | maps (6) and diagrams (3) again |
| Shorts graphics_ui | 23/24 | reliable |
| Shorts props/typography/uncat | all fit some category | mixed bucket by design |
- Conclusion: tags are a finding aid. `graphics_ui` is reliable (~96%), `characters` is reliable for "a figure is in frame" (because nearly every xkcd frame has one), `environments` really means "background is not the off-white canvas", `typography` and `props` are about 55-60% pure. Anything used in the model sheets or prompt pack below was opened as an image first.
- `transitions` is not an image category: a single frame cannot show a transition. Transition behaviour comes from ledger event classes (P3) and measured windows (P4).

## Main visual findings from the viewing pass (OBSERVED; tile-scale, so small text can be wrong)
1. Default canvas is off-white with black hand-drawn line art; a stick figure is in almost every frame.
2. The opening "lecture frame" is one fixed layout reused across videos: figure lower-left holding a paper, empty whiteboard right, grey rounded question box top-centre with small serif "Q." text and "—Name" (seen in 4 long videos on one sheet).
3. Shorts re-use the same art: board panel in the upper half, narrator below; map panels on a black lower area with a WHITE-outline figure; wide diagrams are cropped and panned across rather than redrawn. The Shorts question card looks like a sans face with a "Q" chip, unlike the long-form serif (verify at full res in P3).
4. Background families: off-white canvas (default), black space with white line art and soft glows, grey night scenes with vignettes, flat colour fields and gradients (beige planet, dusk blue-orange, purple-pink, yellow sun disc), coloured maps (grey ocean, pale cyan shelf, cream land, green vegetation).
5. Objects are drawn with far more detail than the figures (rover, submarine cutaway, ships, Hubble, buildings). Real-world inserts (heat maps, scanned tables, Wikipedia, comment cards, quoted text) sit in thin black frames with a small serif footnote.
6. Red is the annotation colour (arrows, circles around words, strike-throughs, hatching, red results like "~6.28"), plus red glows in space scenes.

## Not done
- No per-cluster verdict for the 2,515 unviewed clusters; no second reader.
- Keywords were not re-tuned after the viewing pass (finding aid only). Sub-identities (which prop, which modifier) are not assigned.
