# VISUAL RECONSTRUCTION — America's Debt Hasn't Broken... Yet (6S3PzAUFnXQ)

_Source: SHORT · 720×1280 @ 24.0 fps · 69.0s · published 2026-10-02 · SHA256 `6ec37847fdccb35f…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **1655** (every frame). Reviewed shots: **9**; stable states: **58**; motion rows: **57**; micro-changes below threshold (counted, not tabulated): 49.
- Shot length: median **5.9s**, mean 7.7s, p10 4.0s, p90 13.3s → **7.8 shots/min**.
- Visual-state length: median **0.52s**, mean 0.85s → **50.5 states/min** (a new composition state roughly every 1.2s incl. transitions).
- Time in transitions/animation (frames between stable states): **20s (29%)**; stable states **49s (71%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 92%; SCREEN_CAPTURE 90%; MOTION_GRAPHICS 8%. Shots made only of drawn assets + text motion: 10% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 18, TEXT_SWAP 17, POP_IN 7, TEXT_REVEAL 4, ZOOM_IN 3, SLIDE 2, DRAW_ON 2, SCROLL 1, POSE_CHANGE 1, FACE_CHANGE 1, TEXT_SWAP; 1.
- Narration pace: **200 words/min** over the voiced span; sync of visual events vs ASR word times: DURING_WORD 33, ON_WORD_START 23, BEFORE_WORD 5, AFTER_WORD 5.
- Shot-start offset vs nearest word start: median **13 ms** (p10 -72, p90 183); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 8 of 26 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| CAPTION_CHUNK | OTHER | 42.17 | 9 | UNKNOWN |
| HOST | CHARACTER_HOST | 13.54 | 6 | ORIGINAL_DRAWING |
| POINTER | PROP | 11.46 | 5 | ORIGINAL_DRAWING |
| TXT_HANDLETTER | TEXT_LETTERING | 10.75 | 3 | MOTION_GRAPHICS |
| MAP_USA_CHAR | CHARACTER_MAP | 9.46 | 5 | ORIGINAL_DRAWING |
| SS_CBO_DEBT_GDP_CHART | SCREENSHOT | 8.25 | 1 | SCREEN_CAPTURE |
| SS_FRED_GDP_CHART | SCREENSHOT | 6.5 | 1 | SCREEN_CAPTURE |
| SS_CRFB_SPIRAL | SCREENSHOT | 6.04 | 1 | SCREEN_CAPTURE |
| TXT_RED_BIG | TEXT_LETTERING | 5.0 | 2 | MOTION_GRAPHICS |
| OBJ_DEBT_DOC | OBJECT | 4.42 | 3 | ORIGINAL_DRAWING |
| SS_PRINCIPAL_INTEREST | SCREENSHOT | 3.62 | 1 | SCREEN_CAPTURE |
| CHAR_PEOPLE_ROW | CHARACTER | 3.0 | 1 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| first 1s (0-1s) | 1 | 1 | 0 | 360 | 1 | 1 |
| 1-3s (1-3s) | 2 | 0 | 2 | 240 | 2 | 0 |
| 3-10s (3-10s) | 6 | 2 | 6 | 180 | 1 | 1 |
| 10s-midpoint (10-34s) | 22 | 2 | 22 | 201 | 3 | 2 |
| midpoint-last5s (34-64s) | 24 | 4 | 25 | 189 | 4 | 2 |
| last 5s (64-69s) | 3 | 0 | 2 | 228 | 0 | 0 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] National-debt-clock banner screenshot ('WHAT IS THE NATIONAL DEBT TODAY? $40,086,889,777,472 / THAT'S $117,446 FOR EVERY SINGLE PERSON IN AMERICA') at [S001.1 @1.4s] Chart 'Average interest expense on US government debt now over $3 billion per day' (line rising steeply); caption 'the interest is this big' [S001.2 @2.7s] CBO 'The Budget Outlook — Deficits' text excerpt (deficit $1.9T in 2026; 5.8% of GDP; double the 50-year average) with caption 'and the deficit'

Closing frames: [S008.0 @66.8s] Infographic enlarged; host's worried face with hand on chin at lower left; caption 'We go from having breathing room to having' [S008.1 @67.0s] Caption 'to having someone suck' [S008.2 @67.8s] Final caption 'to having someone suck the oxygen out of the room' — video ends (no end card)


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 5.7 | 5 | Hook: if debt, interest and deficit are this big, why isn't this a crisis? |
| SH002 | 5.7 | 4.2 | 3 | America's economy grows faster than it borrows |
| SH003 | 9.9 | 9.8 | 8 | Average rate ~3.5% vs economy growing ~6.5% |
| SH004 | 19.8 | 12.5 | 12 | When the rate you pay is lower than the rate you grow, old debt shrinks |
| SH005 | 32.2 | 5.9 | 6 | Growing faster than debt isn't unlimited borrowing |
| SH006 | 38.1 | 2.8 | 5 | …which is exactly what's happening to the United States |
| SH007 | 41.0 | 16.8 | 11 | Debt/GDP ~101% now, 120% by 2036 (CBO); growth beats interest by 3 points |
| SH008 | 57.7 | 5.1 | 4 | CRFB: the date is 2031 when the two lines meet |
| SH009 | 62.8 | 6.1 | 4 | Final line: from breathing room to oxygen sucked out |
