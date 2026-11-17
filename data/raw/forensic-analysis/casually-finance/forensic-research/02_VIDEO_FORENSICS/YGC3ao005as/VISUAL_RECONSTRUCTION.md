# VISUAL RECONSTRUCTION — We're Fighting A Battle Against the Market (YGC3ao005as)

_Source: SHORT · 720×1280 @ 24.0 fps · 63.0s · published 2026-10-07 · SHA256 `cc2cfb4f9b8426e0…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **1513** (every frame). Reviewed shots: **4**; stable states: **48**; motion rows: **47**; micro-changes below threshold (counted, not tabulated): 21.
- Shot length: median **16.2s**, mean 15.8s, p10 7.3s, p90 23.8s → **3.8 shots/min**.
- Visual-state length: median **0.46s**, mean 0.75s → **45.7 states/min** (a new composition state roughly every 1.3s incl. transitions).
- Time in transitions/animation (frames between stable states): **27s (43%)**; stable states **36s (57%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 100%; SCREEN_CAPTURE 60%; COMPOSITED_STILLS 40%. Shots made only of drawn assets + text motion: 0% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 12, POP_IN 11, TEXT_SWAP 11, SCALE_UP 2, TEXT_REVEAL 2, SLIDE 2, DRAW_ON 2, REPOSITION 2, HIGHLIGHT 2, EXIT 1.
- Narration pace: **188 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 27, DURING_WORD 17, BEFORE_WORD 7.
- Shot-start offset vs nearest word start: median **23 ms** (p10 1, p90 154); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 9 of 27 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| CAPTION_CHUNK | OTHER | 29.17 | 4 | UNKNOWN |
| HL_TEXT_MARKER_YELLOW | ANNOTATION_OVERLAY | 12.0 | 2 | MOTION_GRAPHICS |
| CHAR_BESSENT | CHARACTER | 9.37 | 1 | ORIGINAL_DRAWING |
| SS_CNBC_BUYBACK_ARTICLE | SCREENSHOT | 9.25 | 2 | SCREEN_CAPTURE |
| TXT_HANDLETTER | TEXT_LETTERING | 8.58 | 2 | MOTION_GRAPHICS |
| HOST | CHARACTER_HOST | 8.37 | 3 | ORIGINAL_DRAWING |
| OBJ_SPEECH_BUBBLE | OBJECT | 7.17 | 1 | ORIGINAL_DRAWING |
| OBJ_TREASURY_CERT | OBJECT | 6.75 | 3 | ORIGINAL_DRAWING |
| OBJ_MONEYBAGS | OBJECT | 5.75 | 1 | ORIGINAL_DRAWING |
| PHOTO_BESSENT | PHOTO | 5.42 | 2 | STOCK_FOOTAGE |
| SS_WSJ_BOND_OPED | SCREENSHOT | 4.17 | 1 | SCREEN_CAPTURE |
| ICON_DOLLAR_GREEN | ICON | 3.54 | 1 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| first 1s (0-1s) | 2 | 1 | 1 | 180 | 1 | 1 |
| 1-3s (1-3s) | 2 | 0 | 3 | 240 | 0 | 0 |
| 3-10s (3-10s) | 9 | 1 | 8 | 206 | 2 | 1 |
| 10s-midpoint (10-32s) | 17 | 1 | 18 | 184 | 1 | 1 |
| midpoint-last5s (32-58s) | 17 | 1 | 17 | 181 | 2 | 0 |
| last 5s (58-63s) | 1 | 0 | 0 | 192 | 0 | 0 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] White canvas with caption 'On' upper left [S001.1 @0.9s] CNBC article card '30-year Treasury yield tops 5.33%, new 19-year high, on inflation and spending concerns' (date PUBLISHED TUE AUG 18 2026 boxed in r [S001.2 @1.4s] US Treasury certificate and orange % coin appear lower right; caption 'the 30-year' [S001.3 @1.8s] Caption 'the 30-year touched'

Closing frames: [S004.6 @56.5s] Op-ed body text full-frame; yellow highlight over 'The long-term Treasury yield is the most important price in the world. It is al [S004.7 @56.9s] Caption 'Treasury yields act' [S004.8 @61.8s] Caption '…because it's the only one that has to be paid' ('has to be paid' in red); Treasury certificate appears at lower right


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 5.1 | 6 | Hook: Aug 18 the 30-year touched a 19-year high; Treasury steps in |
| SH002 | 5.1 | 25.4 | 23 | The very next morning: the Treasury steps in |
| SH003 | 30.5 | 20.0 | 10 | Next day: Bessent on TV — 'the market does not dictate policy' |
| SH004 | 50.6 | 12.5 | 9 | The WSJ opinion piece: 'Let the Bond Market Speak' |
