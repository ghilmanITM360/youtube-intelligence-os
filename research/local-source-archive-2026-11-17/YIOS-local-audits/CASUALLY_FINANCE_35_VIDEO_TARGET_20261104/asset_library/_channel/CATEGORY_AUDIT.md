# Casual Finance — category sorting audit (2026-11-08, LOCAL ONLY)

## What was done
- `category_index.csv` tags all 3,945 unique clusters. Method = RULE_FROM_LEDGER_TEXT + PIXEL_FEATURES (INFERRED, not a per-frame human verdict).
  Rules: keywords on the ledger text of every cluster member + white/green/dark pixel fractions of the representative frame.
- `primary` counts: graphics_ui 1370, characters 833, typography 741, props 542, environments 244, uncategorised 210, transitions 5.
- A cluster can hold several things (stick man + chalkboard + text). Categories are tags, not folders; `tags` lists every rule hit.
- **Viewed:** 168 of 3,945 clusters (4.3%) were opened as images in 7 contact sheets (`review_sheets/`, `*.members.csv` list the tiles; `viewed_in_sheet` column marks them). The other 95.7% are rule-tagged only.

## Viewing-pass verdicts (my reading of each 24-tile random sheet; one reader, no second check)
| Sheet (provisional tag) | What I saw | Fit |
|---|---|---|
| characters | every tile has a character (stick figure, anthropomorphic map, costume figures, robot, detective) | 24/24 contain a character; tag is reliable |
| graphics_ui | screenshots, charts, maps, logos, documents, but also stick figure at a drawn monitor and a hand-drawn chart | about 21/24; keyword "chart/graph/map" over-matches drawn props |
| typography | text cards, chalkboard text, captions, but also speech-bubble scenes and text+map | about 15/24 text-dominant; keyword "text/word" over-matches |
| props | money bags, oil barrels, newspaper, documents, houses, bulletin board, but also 4 charts/tables | about 18/24 prop-dominant |
| environments | painted/flat-colour full-bleed scenes (casino, forest, boardroom, underwater, supermarket, gym) | 22/24 correct (2 were grey chart slides) |
| uncategorised | props 9, graphics/screens 8, characters 7 | all fit an existing category; keyword misses |
- Conclusion: use the tags to FIND candidates, never as ground truth. Anything that goes into a model sheet or prompt pack was opened as an image first.
- `transitions` is not an image category: a single frame cannot show a transition. Transition behaviour is measured from ledger entering classes instead (`model_sheets/entering_class_counts.csv`).

## Not done
- No per-cluster human verdicts for the 95.7% unviewed. A second reviewer or a second random sheet per category would raise confidence.
- Sub-categories (character identity, prop type, chart type) are not assigned; the ledger asset ids (`model_sheets/asset_roster.csv`) are the closest identity signal.
