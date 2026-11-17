# VISUAL RECONSTRUCTION — Somebody Is Quietly Repricing America (PxgCsLSf-w4)

_Source: SHORT · 720×1280 @ 24.0 fps · 64.9s · published 2026-10-05 · SHA256 `0ea5882ac58dbd23…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **1557** (every frame). Reviewed shots: **7**; stable states: **53**; motion rows: **52**; micro-changes below threshold (counted, not tabulated): 18.
- Shot length: median **8.8s**, mean 9.3s, p10 5.1s, p90 14.0s → **6.5 shots/min**.
- Visual-state length: median **0.46s**, mean 0.81s → **49.0 states/min** (a new composition state roughly every 1.2s incl. transitions).
- Time in transitions/animation (frames between stable states): **22s (34%)**; stable states **43s (66%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 100%; SCREEN_CAPTURE 85%; MOTION_GRAPHICS 15%. Shots made only of drawn assets + text motion: 15% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 18, POP_IN 11, TEXT_SWAP 9, DRAW_ON 3, TEXT_REVEAL 3, SWAP 2, ZOOM_IN 2, FACE_CHANGE 2, EXIT 1, SCALE_UP 1.
- Narration pace: **191 words/min** over the voiced span; sync of visual events vs ASR word times: DURING_WORD 31, ON_WORD_START 23, AFTER_WORD 3, BEFORE_WORD 2.
- Shot-start offset vs nearest word start: median **25 ms** (p10 -7, p90 319); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 9 of 39 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| CAPTION_CHUNK | OTHER | 32.38 | 6 | UNKNOWN |
| HOST | CHARACTER_HOST | 17.54 | 4 | ORIGINAL_DRAWING |
| MAP_USA_CHAR | CHARACTER_MAP | 14.5 | 3 | ORIGINAL_DRAWING |
| POINTER | PROP | 13.88 | 2 | ORIGINAL_DRAWING |
| SS_TREASURY_AUCTION_DOC | SCREENSHOT | 8.04 | 2 | SCREEN_CAPTURE |
| OBJ_MONEYBAGS | OBJECT | 6.92 | 2 | ORIGINAL_DRAWING |
| ICON_QUESTION | ICON | 6.25 | 1 | ORIGINAL_DRAWING |
| ICON_ARROW_RED | ICON | 6.25 | 1 | ORIGINAL_DRAWING |
| TXT_RED_BIG | TEXT_LETTERING | 5.12 | 4 | MOTION_GRAPHICS |
| HL_RED_CIRCLE | ANNOTATION_OVERLAY | 3.79 | 1 | MOTION_GRAPHICS |
| SS_HEADLINE_REUTERS_40T | SCREENSHOT | 3.46 | 1 | SCREEN_CAPTURE |
| TXT_30YEARS | TEXT_LETTERING | 3.13 | 1 | MOTION_GRAPHICS |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| first 1s (0-1s) | 2 | 1 | 1 | 300 | 0 | 1 |
| 1-3s (1-3s) | 0 | 0 | 1 | 150 | 0 | 0 |
| 3-10s (3-10s) | 4 | 0 | 4 | 171 | 0 | 0 |
| 10s-midpoint (10-32s) | 20 | 2 | 20 | 190 | 5 | 1 |
| midpoint-last5s (32-60s) | 21 | 4 | 21 | 195 | 2 | 1 |
| last 5s (60-65s) | 6 | 0 | 5 | 180 | 1 | 0 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] White canvas with centred hand-lettered '30 years' and small caption 'is long' below [S001.1 @1.0s] Caption 'is long enough that'

Closing frames: [S010.4 @61.6s] Caption '...the first country in history to cross' [S010.5 @63.2s] Pile of 'DEBT' documents with red outlined '$40T' placed between map and card; caption removed [S011.0 @64.8s] Blank white end frame (no end card or CTA); video ends


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 10.0 | 6 | Hook: 30 years is long enough that no election survives it |
| SH002 | 10.0 | 8.8 | 3 | It's the closest thing to an honest opinion on a country |
| SH003 | 18.8 | 18.4 | 20 | Definition: Treasury yield |
| SH004 | 37.1 | 7.0 | 6 | But we need to back up first: 30-year yield 5.33% |
| SH005 | 44.1 | 11.0 | 9 | The Treasury auction: $22B of 30-year debt at 5.3% |
| SH006 | 55.1 | 3.7 | 2 | Most expensive 30-year sale since 2001 |
| SH007 | 58.8 | 6.0 | 7 | $40 trillion national debt |
