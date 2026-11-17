# VISUAL RECONSTRUCTION — Why The Dumbest Investors Win (it's not why you think) (o3FQcd91MIs)

_Source: LONG_FORM · 1280×720 @ 30.0 fps · 277.9s · published 2025-07-28 · SHA256 `82ab2b63ce250723…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **8338** (every frame). Reviewed shots: **47**; stable states: **76**; motion rows: **75**; micro-changes below threshold (counted, not tabulated): 5.
- Shot length: median **5.2s**, mean 5.9s, p10 2.7s, p90 10.7s → **10.1 shots/min**.
- Visual-state length: median **3.35s**, mean 3.63s → **16.4 states/min** (a new composition state roughly every 3.7s incl. transitions).
- Time in transitions/animation (frames between stable states): **2s (1%)**; stable states **276s (99%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 78%; SCREEN_CAPTURE 38%; COMPOSITED_STILLS 35%; MOTION_GRAPHICS 24%. Shots made only of drawn assets + text motion: 41% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 53, TEXT_REVEAL 7, POP_IN 5, ZOOM_IN 2, TEXT_SWAP 2, REFRAME 2, SWAP 2, CLEAR 1, DRAW_ON 1.
- Narration pace: **172 words/min** over the voiced span; sync of visual events vs ASR word times: DURING_WORD 49, ON_WORD_START 39, BEFORE_WORD 29, AFTER_WORD 4, IN_PAUSE 1.
- Shot-start offset vs nearest word start: median **27 ms** (p10 -162, p90 435); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 20 of 77 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| CHAR_DAVE | CHARACTER | 141.93 | 25 | ORIGINAL_DRAWING |
| TXT_SMALL_CAPTION | TEXT_LETTERING | 56.7 | 13 | MOTION_GRAPHICS |
| TXT_LABEL_DAVE | TEXT_LETTERING | 31.13 | 6 | MOTION_GRAPHICS |
| TXT_WHEN_MARKET | TEXT_LETTERING | 19.73 | 4 | MOTION_GRAPHICS |
| CHART_DK_CURVE | CHART | 18.87 | 3 | SCREEN_CAPTURE |
| TXT_LABEL_DAVE_OUTPERFORMER | TEXT_LETTERING | 15.63 | 2 | MOTION_GRAPHICS |
| CHAR_EVE | CHARACTER | 15.0 | 3 | ORIGINAL_DRAWING |
| IMG_BUFFETT_PHOTO | IMAGE_STILL | 14.73 | 2 | COMPOSITED_STILLS |
| TXT_LABEL_BUFFETT | TEXT_LETTERING | 14.73 | 2 | MOTION_GRAPHICS |
| LOGO_AMAZON | LOGO | 13.57 | 1 | COMPOSITED_STILLS |
| TXT_BETA_133 | TEXT_LETTERING | 13.57 | 1 | MOTION_GRAPHICS |
| SS_SHEET_BETA | SCREENSHOT | 10.83 | 1 | SCREEN_CAPTURE |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 2 | 1 | 1 | 192 | 0 | 1 |
| 5-15s (5-15s) | 4 | 3 | 4 | 174 | 1 | 0 |
| 15-30s (15-30s) | 5 | 3 | 5 | 168 | 3 | 1 |
| 30-60s (30-60s) | 9 | 5 | 9 | 182 | 3 | 4 |
| 60s-midpoint (60-139s) | 19 | 12 | 19 | 171 | 13 | 8 |
| midpoint-last60s (139-218s) | 24 | 12 | 24 | 167 | 6 | 7 |
| last 60s (218-278s) | 13 | 11 | 13 | 154 | 4 | 5 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Smiling stick figure with a round peach head and spiky black hair, arms out, with a handwritten name label and arrow above him, low on a blank canvas [S001.1 @1.4s] Dave larger, holding up a gold trophy topped by an orange ribbon banner [S001.2 @5.8s] A right-pointing arrow leads from Dave's trophy to a tiny blue toddler beside a large flame [S001.3 @8.2s] Dave small at left with hands on hips beside a hand-drawn axes chart with a rising green line and arrow

Closing frames: [S021.2 @266.4s] The orange joke-coin blob alone at centre [S021.3 @270.1s] Closing line alone on white [S021.4 @272.4s] White end card: title at top, a handwritten note with an arrow to three round social-media icons at left, Dave grinning and pressi


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 5.8 | 2 | Hook: Meet Dave |
| SH002 | 5.8 | 2.4 | 1 | Two years of trading is a toddler who just discovered fire |
| SH003 | 8.2 | 5.1 | 2 | His portfolio is up 13% year to date |
| SH004 | 13.3 | 3.1 | 1 | He just hit it big on a crypto meme coin |
| SH005 | 16.4 | 1.8 | 1 | His confidence is at an all-time high |
| SH006 | 18.2 | 7.5 | 3 | Dave's hobbies: Wolf of Wall Street, pitching biotech at the bar, and nicotine pouches |
| SH007 | 25.7 | 4.8 | 1 | He has what it takes to become a full-time trader |
| SH008 | 30.5 | 6.9 | 2 | Dave calls his broker |
| SH009 | 37.4 | 5.3 | 2 | Three months later: leveraged to the max on out-of-the-money Tesla calls |
| SH010 | 42.8 | 4.1 | 2 | His strategy and his risk management |
| SH011 | 46.9 | 4.5 | 1 | His wife's concern: where is the $13,000? |
| SH012 | 51.4 | 8.8 | 2 | Three more months and the Fed hikes: Dave's portfolio is down 67% |
| SH013 | 60.2 | 3.7 | 1 | His wife's new hobby: googling how to divorce him |
| SH014 | 63.9 | 4.8 | 1 | The question of today's video |
| SH015 | 68.7 | 4.1 | 1 | The Dunning-Kruger effect is the financial markets' version of Darwinism |
| SH016 | 72.9 | 10.8 | 1 | Dumb people think they're Warren Buffett; Dave sits on the peak |
| SH017 | 83.7 | 5.2 | 1 | Since 2020 you could have made money in almost any stock |
| SH018 | 88.9 | 7.6 | 2 | On the left side of the Dunning-Kruger curve, where Dave was, you outperformed the S&P |
| SH019 | 96.5 | 6.8 | 3 | Traditional value investors think it's about fundamentals and fair valuations |
| SH020 | 103.3 | 13.2 | 4 | The outperformers buy companies at 650x earnings, ride trends that make less sense than pi |
| SH021 | 116.5 | 4.7 | 1 | Warren Buffett once said: why buy Apple when you can buy fart coin |
| SH022 | 121.2 | 6.2 | 1 | If you zoom out even further, it gets more evident |
| SH023 | 127.4 | 7.9 | 2 | The greatest bull market in history: 17 years, 715% returns, a bender since 2009 |
| SH024 | 135.3 | 13.0 | 4 | High beta and irrational approaches outperformed: everything turns to gold |
| SH025 | 148.3 | 5.4 | 2 | Like all great benders it must end eventually |
| SH026 | 153.7 | 3.6 | 2 | But when is the end coming, and how can you prepare for it? |
| SH027 | 157.3 | 10.6 | 2 | Option one: sit on cash like Buffett (boring) |
| SH028 | 167.9 | 7.4 | 2 | Option two: go all in and blame others when the market reverses |
| SH029 | 175.3 | 4.6 | 3 | You can blame the Fed chair, the President or market makers |
| SH030 | 180.0 | 5.1 | 1 | You gotta blame someone: the market is rigged |
| SH031 | 185.1 | 3.3 | 1 | All this brings us to the answer to today's question |
| SH032 | 188.4 | 2.3 | 1 | Why do the dumbest investors win? |
| SH033 | 190.7 | 6.1 | 2 | And the answer is simple: retail investors love volatile, high-beta stocks |
| SH034 | 196.8 | 4.6 | 2 | Let's get a little more technical: what is beta? |
| SH035 | 201.4 | 4.8 | 1 | Beta is a measure of a stock's volatility compared with the market as a whole |
| SH036 | 206.2 | 13.6 | 2 | Amazon has a beta of 1.33: 33% more volatile than the market |
| SH037 | 219.9 | 10.9 | 1 | If the market rises 2% Amazon is expected to rise 2.66%; if it falls 2%, it falls 2.66% |
| SH038 | 230.7 | 1.4 | 1 | So why does this matter? |
| SH039 | 232.1 | 9.1 | 3 | When the market is up, a high-beta (retail) portfolio outperforms |
| SH040 | 241.2 | 5.6 | 1 | Dave looks to book a table at a celebrity sushi restaurant to celebrate his genius |
| SH041 | 246.8 | 5.4 | 1 | When the market is down, a high-beta portfolio feels the effects of gravity |
| SH042 | 252.2 | 2.9 | 1 | Now Dave is looking to see if a casual restaurant chain is hiring |
| SH043 | 255.2 | 5.0 | 1 | In a bull market Dave's high-beta portfolio makes him the next George Soros |
| SH044 | 260.2 | 6.2 | 1 | In a bear market he becomes the next trending post on a trading forum |
| SH045 | 266.4 | 3.7 | 1 | Next time a friend brags about a 10-bagger meme coin |
| SH046 | 270.1 | 2.2 | 1 | Everyone's a genius in a bull market |
| SH047 | 272.4 | 5.6 | 1 | End card: subscribe for more |
