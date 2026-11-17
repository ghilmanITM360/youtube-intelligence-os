# VISUAL RECONSTRUCTION — The SpaceX IPO Nobody Can (Actually) Explain... (JsK53moCyZA)

_Source: SHORT · 720×1280 @ 30.0 fps · 43.0s · published 2026-06-01 · SHA256 `4e60a637b758c143…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **1291** (every frame). Reviewed shots: **3**; stable states: **57**; motion rows: **56**; micro-changes below threshold (counted, not tabulated): 1.
- Shot length: median **8.5s**, mean 14.3s, p10 6.0s, p90 25.0s → **4.2 shots/min**.
- Visual-state length: median **0.37s**, mean 0.53s → **79.5 states/min** (a new composition state roughly every 0.8s incl. transitions).
- Time in transitions/animation (frames between stable states): **13s (30%)**; stable states **30s (70%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 87%; MOTION_GRAPHICS 80%; SCREEN_CAPTURE 68%; COMPOSITED_STILLS 13%. Shots made only of drawn assets + text motion: 20% of runtime.
- Motion vocabulary (reviewer labels, count): TEXT_SWAP 16, CUT 10, LOOP_ANIM 8, POP_IN 5, HOLD 4, DRAW_ON 4, TEXT_REVEAL 3, SCROLL 2, POSE_CHANGE 1, ZOOM_IN 1, REPOSITION 1, SLIDE 1.
- Narration pace: **186 words/min** over the voiced span; sync of visual events vs ASR word times: DURING_WORD 32, ON_WORD_START 18, BEFORE_WORD 6, AFTER_WORD 3.
- Shot-start offset vs nearest word start: median **-40 ms** (p10 -77, p90 -7); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 3 of 24 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| CAPTION_CHUNK | OTHER | 30.1 | 3 | UNKNOWN |
| SS_SPACEX_BAR | SCREENSHOT | 8.7 | 1 | SCREEN_CAPTURE |
| CHAR_MUSK | CHARACTER | 7.97 | 1 | ORIGINAL_DRAWING |
| HOST | CHARACTER_HOST | 6.47 | 2 | ORIGINAL_DRAWING |
| TXT_HANDLETTER | TEXT_LETTERING | 6.43 | 3 | MOTION_GRAPHICS |
| SS_BIGGEST_COMPANIES_CHART | SCREENSHOT | 5.3 | 1 | SCREEN_CAPTURE |
| LOGO_NASDAQ | LOGO | 5.2 | 1 | COMPOSITED_STILLS |
| OBJ_401K_DOC | OBJECT | 4.53 | 1 | ORIGINAL_DRAWING |
| POINTER | PROP | 4.03 | 1 | ORIGINAL_DRAWING |
| OBJ_RULES_DOC | OBJECT | 4.03 | 1 | ORIGINAL_DRAWING |
| OBJ_CASH_BILLS | OBJECT | 3.77 | 1 | ORIGINAL_DRAWING |
| LOGO_SPACEX | LOGO | 2.77 | 1 | COMPOSITED_STILLS |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| first 1s (0-1s) | 3 | 1 | 2 | 240 | 0 | 1 |
| 1-3s (1-3s) | 2 | 0 | 2 | 150 | 1 | 0 |
| 3-10s (3-10s) | 15 | 0 | 16 | 163 | 2 | 0 |
| 10s-midpoint (10-22s) | 14 | 0 | 14 | 177 | 2 | 0 |
| midpoint-last5s (22-38s) | 17 | 2 | 16 | 207 | 3 | 2 |
| last 5s (38-43s) | 6 | 0 | 6 | 168 | 0 | 0 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] White canvas; small stick-figure host at left holding a pointer, smiling [S001.1 @0.1s] Burned-in caption (small black hand-lettered text, lower right) appears: 'Elon Musk' [S001.2 @0.6s] Caption chunk changes to 'is preparing' [S001.3 @1.4s] Blue horizontal bar chart 'SpaceX IPO vs. The Biggest Companies on Earth' appears at right with a red SpaceX bar and a yellow 'Largest IPO in history'

Closing frames: [S001.54 @40.0s] Caption 'brand-new rule' [S001.55 @40.8s] Tiny text 'shh… you saw nothing' above the logo; caption 'designed specifically' [S001.56 @42.0s] Logo/rules shifted left-down; caption 'to make that happen'; video ends on this frame (no end card)


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 29.1 | 44 | Hook: Elon Musk preparing the largest IPO in human history; word-chunk burned-in captions |
| SH002 | 29.1 | 8.5 | 6 | Reveal: the buyer is you (retirement accounts) |
| SH003 | 37.6 | 5.4 | 7 | The Nasdaq rule |
