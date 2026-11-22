# VISUAL RECONSTRUCTION — Why Japan's Economy Is Awful (rSa2aziEsAI)

_Source: SHORT · 720×1280 @ 30.0 fps · 60.5s · published 2026-08-26 · SHA256 `73641860dea2a882…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **1815** (every frame). Reviewed shots: **12**; stable states: **45**; motion rows: **44**; micro-changes below threshold (counted, not tabulated): 2.
- Shot length: median **4.1s**, mean 5.0s, p10 1.4s, p90 8.6s → **11.9 shots/min**.
- Visual-state length: median **0.77s**, mean 0.98s → **44.6 states/min** (a new composition state roughly every 1.3s incl. transitions).
- Time in transitions/animation (frames between stable states): **16s (27%)**; stable states **44s (73%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 92%; MOTION_GRAPHICS 49%; SCREEN_CAPTURE 18%; COMPOSITED_STILLS 8%. Shots made only of drawn assets + text motion: 79% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 16, POP_IN 13, TEXT_SWAP 3, HOLD 2, SWAP 2, EXIT 2, DRAW_ON 2, ZOOM_IN 1, SCROLL 1, TEXT_REVEAL 1, REPOSITION 1.
- Narration pace: **212 words/min** over the voiced span; sync of visual events vs ASR word times: DURING_WORD 30, ON_WORD_START 23, AFTER_WORD 2, BEFORE_WORD 1.
- Shot-start offset vs nearest word start: median **73 ms** (p10 0, p90 309); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 13 of 30 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| CAPTION_BURNED | OTHER | 22.6 | 10 | UNKNOWN |
| MAP_JAPAN_CHAR | CHARACTER_MAP | 20.53 | 5 | ORIGINAL_DRAWING |
| OBJ_SPEECH_BUBBLE | OBJECT | 11.33 | 4 | ORIGINAL_DRAWING |
| OBJ_BOJ_BUILDING | OBJECT | 11.2 | 3 | ORIGINAL_DRAWING |
| OBJ_YEN_NOTE | OBJECT | 10.93 | 3 | ORIGINAL_DRAWING |
| OBJ_BONDS_DOC | OBJECT | 9.93 | 3 | ORIGINAL_DRAWING |
| ICON_PERCENT | ICON | 8.73 | 3 | ORIGINAL_DRAWING |
| OBJ_YEN_BAG | OBJECT | 6.63 | 3 | ORIGINAL_DRAWING |
| TXT_HANDLETTER | TEXT_LETTERING | 5.77 | 4 | MOTION_GRAPHICS |
| OBJ_MONSTER | OBJECT | 5.43 | 1 | ORIGINAL_DRAWING |
| CAPTION_BURNED_RED | OTHER | 4.93 | 2 | UNKNOWN |
| ICON_SHIELD | ICON | 4.5 | 1 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| first 1s (0-1s) | 1 | 1 | 0 | 300 | 0 | 1 |
| 1-3s (1-3s) | 1 | 0 | 1 | 210 | 0 | 0 |
| 3-10s (3-10s) | 2 | 1 | 2 | 180 | 1 | 0 |
| 10s-midpoint (10-30s) | 14 | 5 | 14 | 204 | 1 | 2 |
| midpoint-last5s (30-56s) | 20 | 4 | 21 | 223 | 3 | 2 |
| last 5s (56-60s) | 7 | 1 | 6 | 204 | 0 | 0 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Green Japan-shaped character (eyes, stick legs, carrying a yen money bag) on white; speech bubble 'Don't worry Japan, I'll buy it!'; stack of green 'J [S001.1 @2.3s] Caption now 'by buying its own debt.' at top; bubble from the Japan character 'Omg thank you Japan!!!' ; Japan character with glasses at lower right w

Closing frames: [S011.6 @58.6s] Two green 'Japan' bond documents appear at lower right [S011.7 @59.1s] Caption removed (silence before final line) [S011.8 @59.9s] Red X drawn through both the yen/shield cluster and the bond documents ('It can't do both')


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 8.7 | 3 | Hook: Japan solved its debt problem by buying its own debt |
| SH002 | 8.7 | 1.3 | 1 | BoJ held borrowing costs at zero |
| SH003 | 10.0 | 7.7 | 3 | The Bank of Japan buys its own bonds |
| SH004 | 17.7 | 6.4 | 5 | Those bonds pay almost nothing |
| SH005 | 24.2 | 2.0 | 2 | Investors dump the yen, chase dollar yields |
| SH006 | 26.2 | 2.1 | 2 | Currency driven off a cliff |
| SH007 | 28.2 | 7.4 | 6 | The armchair economist: 'why doesn't Japan just raise rates?' |
| SH008 | 35.6 | 1.3 | 1 | Meme: 'I can't do this right now' |
| SH009 | 36.9 | 12.2 | 10 | Commercial banks park cash at the Bank of Japan |
| SH010 | 49.1 | 3.3 | 3 | BoJ pays out trillions while collecting almost nothing |
| SH011 | 52.4 | 3.4 | 2 | 'You don't need a degree in central banking' — net interest income |
| SH012 | 55.8 | 4.7 | 7 | Payoff: defend the yen or afford the debt — can't do both |
