# VISUAL RECONSTRUCTION — To Save the Economy... We’re About to Break It (xtqbRt94TTw)

_Source: LONG_FORM · 1920×1080 @ 24.0 fps · 827.6s · published 2026-09-22 · SHA256 `030a85ad15c25a5a…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **19862** (every frame). Reviewed shots: **133**; stable states: **489**; motion rows: **487**; micro-changes below threshold (counted, not tabulated): 103.
- Shot length: median **5.3s**, mean 6.2s, p10 2.4s, p90 11.5s → **9.6 shots/min**.
- Visual-state length: median **1.00s**, mean 1.40s → **35.5 states/min** (a new composition state roughly every 1.7s incl. transitions).
- Time in transitions/animation (frames between stable states): **144s (17%)**; stable states **684s (83%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 97%; MOTION_GRAPHICS 63%; SCREEN_CAPTURE 51%; COMPOSITED_STILLS 10%. Shots made only of drawn assets + text motion: 41% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 165, POP_IN 100, BUILD 42, HIGHLIGHT 29, SCROLL 23, TEXT_REVEAL 20, ZOOM_IN 18, SWAP 17, REPOSITION 14, FACE_CHANGE 13, POSE_CHANGE 12, EXIT 12, REFRAME 5, TEXT_SWAP 4.
- Narration pace: **196 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 301, DURING_WORD 261, BEFORE_WORD 44, AFTER_WORD 13, IN_PAUSE 1.
- Shot-start offset vs nearest word start: median **40 ms** (p10 -59, p90 269); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 88 of 268 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| HOST | CHARACTER_HOST | 274.83 | 72 | ORIGINAL_DRAWING |
| POINTER | PROP | 152.75 | 33 | ORIGINAL_DRAWING |
| UI_SPONSOR_BAR | UI_OVERLAY | 61.88 | 11 | MOTION_GRAPHICS |
| HL_TEXT_YELLOW | ANNOTATION_OVERLAY | 57.5 | 12 | MOTION_GRAPHICS |
| HL_TEXT_ORANGE | ANNOTATION_OVERLAY | 47.08 | 7 | MOTION_GRAPHICS |
| MAP_USA_CHAR | CHARACTER_MAP | 45.96 | 15 | ORIGINAL_DRAWING |
| ICON_PERCENT_ORANGE | ICON | 45.34 | 15 | ORIGINAL_DRAWING |
| OBJ_LAPTOP_CF | OBJECT | 43.5 | 9 | ORIGINAL_DRAWING |
| HL_RED_BOX | ANNOTATION_OVERLAY | 39.33 | 8 | MOTION_GRAPHICS |
| OBJ_DATA_CENTER | OBJECT | 34.96 | 11 | ORIGINAL_DRAWING |
| OBJ_TREASURY_NOTE | OBJECT | 31.75 | 8 | ORIGINAL_DRAWING |
| OBJ_MONEY_BAG_BIG | OBJECT | 31.16 | 13 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 3 | 1 | 3 | 216 | 2 | 1 |
| 5-15s (5-15s) | 5 | 2 | 5 | 180 | 1 | 1 |
| 15-30s (15-30s) | 6 | 0 | 5 | 196 | 0 | 0 |
| 30-60s (30-60s) | 13 | 7 | 13 | 192 | 3 | 6 |
| 60s-midpoint (60-414s) | 206 | 51 | 205 | 189 | 45 | 33 |
| midpoint-last60s (414-768s) | 210 | 61 | 211 | 199 | 20 | 38 |
| last 60s (768-828s) | 46 | 11 | 45 | 196 | 1 | 7 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Blank white canvas (first frame) [S001.1 @2.8s] Four dark news-headline cards tilted around an orange circle with a white percent sign, above a hand-drawn Federal Reserve building character with lar [S001.2 @3.5s] Federal Reserve Board press-release page with yellow highlight over the 12-0 vote line and the quarter-point hike line; smiling host at right holding  [S002.0 @6.9s] Same statement page smaller at left, host larger at right pointing the stick toward the page

Closing frames: [S102.2 @817.0s] Tilted DEBT documents fly in around the chart's corners [S103.0 @817.8s] Final scene: the USA-map character with wary eyes at left and a single DEBT document at right [S104.0 @821.4s] White end card with a large empty circle at upper left and an empty rectangle below it (blank slots for platform end-screen elemen


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 7.8 | 4 | Hook: Fed raises rates for first time in three years; headline wall and FOMC statement |
| SH002 | 7.8 | 5.2 | 3 | Seven weeks earlier: calendars and an unruly committee |
| SH003 | 13.0 | 17.0 | 7 | July meeting: 9-3 vote against hiking, then compared with September |
| SH004 | 30.0 | 2.1 | 1 | So what changed? host with laptop |
| SH005 | 32.1 | 3.6 | 1 | Fed chair Warsh introduced: bio page |
| SH006 | 35.8 | 8.7 | 1 | Press-conference explanation: inflation not abating (American Banker) |
| SH007 | 44.4 | 0.9 | 1 | In plain English: dictionary |
| SH008 | 45.3 | 3.5 | 4 | Inflation will not go away: arrows get eyes and a voice |
| SH009 | 48.8 | 4.5 | 2 | Bond market gets validation: bond certificates |
| SH010 | 53.3 | 8.7 | 3 | Evidence: 10-year Treasury above 5%, highest since 2007 (Financial Times) |
| SH011 | 62.0 | 13.7 | 7 | Evidence: eleven tightening cycles since 1965 (Blinder journal paper) |
| SH012 | 75.7 | 6.9 | 5 | Only one cycle stopped after a single hike |
| SH013 | 82.6 | 8.4 | 6 | 1997: Greenspan hikes once and stops (Fed rate-change archive) |
| SH014 | 91.0 | 9.8 | 4 | Projections: 16 of 18 officials pencil in another hike (FOMC dot plot) |
| SH015 | 100.8 | 14.6 | 5 | Conference Board brief: more inflation coming, the Fed rarely stops after one move |
| SH016 | 115.4 | 26.6 | 10 | New York Fed paper: fourteen tightening cycles 1955-2009, ten followed by recession |
| SH017 | 142.0 | 5.5 | 4 | Three soft landings in fifty years: crisis averted |
| SH018 | 147.5 | 2.9 | 5 | It's not the number, it's where the cycle lands: the headline stack returns |
| SH019 | 150.4 | 6.5 | 2 | Where do these cycles land in the economy |
| SH020 | 157.0 | 11.5 | 9 | For most of 70 years a hike reached you through a clear door: mortgages and housing |
| SH021 | 168.5 | 2.5 | 3 | People spent less and the economy cooled off |
| SH022 | 171.0 | 1.7 | 1 | Since the Second World War: a wartime image |
| SH023 | 172.7 | 7.7 | 5 | Housing was the Fed's most direct lever, but the lever is breaking |
| SH024 | 180.4 | 8.8 | 5 | Evidence: mortgage-free homes and rate lock-in distribution |
| SH025 | 189.2 | 5.8 | 6 | With a 4% mortgage and rates near 7% you won't sell: headline stack |
| SH026 | 194.9 | 4.2 | 2 | Fed report names it: rate lock |
| SH027 | 199.2 | 7.4 | 5 | Never moving again: 4% locked versus 7% market |
| SH028 | 206.5 | 13.1 | 5 | Evidence: existing-home sales stuck near 4 million a year (NAHB, Wolf Street) |
| SH029 | 219.6 | 9.2 | 5 | If the Fed's favorite brake lever isn't working, where do the hikes land? |
| SH030 | 228.8 | 8.6 | 4 | Warsh answered it himself: Jackson Hole speech on AI capital |
| SH031 | 237.4 | 3.8 | 4 | The chairman pointing at the data centers |
| SH032 | 241.2 | 2.2 | 3 | So how much money are we talking about? |
| SH033 | 243.4 | 7.2 | 3 | Evidence: JP Morgan estimates the AI buildout at about $5 trillion through 2030 |
| SH034 | 250.6 | 10.8 | 4 | Evidence: a finance professor's paper puts the American AI buildout at about 2.8% of GDP a |
| SH035 | 261.4 | 2.2 | 2 | 2.8% of everything America produces, every year through 2032 |
| SH036 | 263.7 | 15.8 | 1 | For context: railroads 2.5%, electrification 1%, interstate highways 1.5% of the economy |
| SH037 | 279.5 | 5.2 | 3 | The tech companies at the centre: Alphabet, Amazon, Meta |
| SH038 | 284.6 | 3.5 | 2 | The reasonable assumption: they've got the money for it, right? |
| SH039 | 288.2 | 1.0 | 1 | But they're not: don't touch my money |
| SH040 | 289.1 | 9.1 | 9 | Evidence: operating cash flow covers only about a quarter of the spend (JP Morgan credit p |
| SH041 | 298.2 | 3.4 | 4 | Evidence: JP Morgan expects the rest to be borrowed: a $4.1 trillion debt story (Benzinga) |
| SH042 | 301.6 | 3.2 | 3 | Where do you go when you need four trillion dollars? Hey Bob |
| SH043 | 304.9 | 3.3 | 4 | Nancy Pelosi's trading account gag |
| SH044 | 308.2 | 5.8 | 3 | But these companies decided to look somewhere else: the bond market |
| SH045 | 313.9 | 14.6 | 7 | Evidence: five tech companies' bond issuance $35B a year, $93B in 2025, $132B by July (Van |
| SH046 | 328.5 | 10.3 | 3 | AI infrastructure spend above $830 billion: half the investment-grade market (Chatham via  |
| SH047 | 338.9 | 9.5 | 9 | Compared with the credit markets: about half the investment-grade bond market, two thirds  |
| SH048 | 348.4 | 7.6 | 3 | A handful of companies through every door in the credit market at once |
| SH049 | 356.0 | 5.7 | 1 | Vanguard: hyperscaler capex above a trillion a year for three years |
| SH050 | 361.7 | 2.4 | 1 | The buildout isn't a check somebody writes |
| SH051 | 364.1 | 4.1 | 5 | A standing appointment with the bond market every year for the rest of the decade |
| SH052 | 368.2 | 4.5 | 2 | The price of money is the entire story |
| SH053 | 372.8 | 2.8 | 2 | Sponsor segue: let's take a quick pause |
| SH054 | 375.5 | 3.3 | 3 | Sponsor: Odoo introduced (a thin yellow progress bar starts along the bottom edge) |
| SH055 | 378.8 | 5.0 | 3 | All-in-one management software: one need, one app |
| SH056 | 383.8 | 6.6 | 6 | Operations on one platform: invoices, spreadsheets, a website, the laptop |
| SH057 | 390.5 | 3.0 | 1 | All applications centralized into one database |
| SH058 | 393.5 | 6.9 | 5 | Sales linked to accounting, inventory and projects |
| SH059 | 400.4 | 2.7 | 3 | No more double manual entry of data |
| SH060 | 403.1 | 5.5 | 4 | No more jumping between tools or searching through sources |
| SH061 | 408.5 | 8.9 | 5 | Focus on what matters, not repetitive tasks: if you need it, I've got it |
| SH062 | 417.4 | 8.6 | 3 | Use any one app for free, or the whole suite under $25 a month |
| SH063 | 426.0 | 5.2 | 2 | More than 28 million users worldwide |
| SH064 | 431.2 | 13.4 | 8 | Call to action: free meeting or 15-day free trial, link below |
| SH065 | 444.6 | 5.5 | 3 | Back to how one small change in the price of money could wreak havoc |
| SH066 | 450.1 | 4.1 | 6 | How bonds work: the government rate plus a little extra, the spread |
| SH067 | 454.2 | 3.8 | 2 | The extra on top is called the spread |
| SH068 | 457.9 | 4.3 | 2 | The spread is the market's nervousness about being repaid |
| SH069 | 462.2 | 6.3 | 1 | Evidence: hyperscaler spreads widened about 30 basis points this year (JP Morgan) |
| SH070 | 468.5 | 5.5 | 2 | Fifteen times the move on some of the most profitable companies |
| SH071 | 474.0 | 5.4 | 3 | That's the best of the best in the market |
| SH072 | 479.4 | 8.7 | 6 | Go down the stack: project debt about 100 bps wider, junk about 200 wider (JP Morgan) |
| SH073 | 488.0 | 1.4 | 1 | Junk territory: the detective |
| SH074 | 489.4 | 7.5 | 4 | Near the bottom of the stack it gets ugly: CoreWeave |
| SH075 | 496.9 | 3.9 | 2 | Halfway through the lender sent it back: the $2.6 billion CoreWeave loan (Bloomberg) |
| SH076 | 500.8 | 16.5 | 7 | The conditions: paid down in full, a coverage test, a minimum cash balance |
| SH077 | 517.3 | 5.9 | 3 | Lenders want to be sure there's money when it's their turn to get paid |
| SH078 | 523.2 | 2.5 | 1 | It ended up clearing at 10.4% |
| SH079 | 525.8 | 11.5 | 7 | CoreWeave's interest bill went from $267 million to $640 million a quarter; interest ate 4 |
| SH080 | 537.2 | 2.9 | 2 | The bottom of the AI market repricing in real time |
| SH081 | 540.2 | 1.7 | 1 | While the thing is still being built |
| SH082 | 541.8 | 4.2 | 3 | The question nobody in the industry wants to say out loud |
| SH083 | 546.0 | 3.5 | 4 | At what price does this stop being worth doing? |
| SH084 | 549.6 | 20.2 | 8 | Evidence: Mercatus models a single GPU cluster at different costs of capital: breakeven ar |
| SH085 | 569.8 | 5.0 | 6 | Established companies with investment-grade balance sheets pay 6-8% on new deals |
| SH086 | 574.8 | 4.0 | 4 | Late-stage AI companies with strong revenue: 10-14% |
| SH087 | 578.8 | 5.0 | 5 | Earlier-stage venture-backed AI companies: 15-20% |
| SH088 | 583.8 | 5.3 | 3 | The top of the market clears the break even, the middle stands on the line, the bottom is  |
| SH089 | 589.1 | 2.5 | 5 | And this is a price that's now rising: the rate-hike headlines return over the map |
| SH090 | 591.6 | 4.4 | 5 | A borrowing cost isn't paid once, it's more like rent |
| SH091 | 596.0 | 2.9 | 1 | And it resets two ways |
| SH092 | 599.0 | 11.1 | 7 | Way one is fast: debt at the bottom of the market floats |
| SH093 | 610.1 | 5.6 | 6 | When the Fed raised rates last week, that loan got more expensive before the next payment  |
| SH094 | 615.7 | 4.3 | 4 | Way two is slow and structural |
| SH095 | 620.0 | 3.2 | 3 | Every loan matures, every bond comes due |
| SH096 | 623.2 | 2.8 | 2 | And when it does, almost nobody pays it off |
| SH097 | 626.0 | 5.3 | 3 | They roll it over and borrow again at whatever the market is charging that morning |
| SH098 | 631.3 | 5.8 | 4 | A company that borrowed cheaply years ago won't get the same rate at the next loan |
| SH099 | 637.0 | 5.5 | 3 | The average tightening cycle since 1983 added more than 3 percentage points (St. Louis Fed |
| SH100 | 642.5 | 4.0 | 2 | Sixteen of eighteen officials see at least one more hike this year |
| SH101 | 646.5 | 2.0 | 2 | The Conference Board sees three |
| SH102 | 648.5 | 2.0 | 1 | You can't borrow all this money at once |
| SH103 | 650.5 | 13.7 | 6 | Not a one-time borrower: like that friend who asks for money |
| SH104 | 664.2 | 8.2 | 5 | This cycle is different: in the past a hike landed on demand (mortgages, cards, cars) |
| SH105 | 672.5 | 5.8 | 4 | This time the biggest impact lands on the supply side: companies with enormous debt loads  |
| SH106 | 678.2 | 2.4 | 1 | That's the part people get wrong about a rate hike |
| SH107 | 680.6 | 3.2 | 2 | For most borrowers a hike doesn't break anything the day it lands |
| SH108 | 683.9 | 5.8 | 7 | It breaks things later, when somebody goes back for more money and it costs more |
| SH109 | 689.7 | 7.5 | 3 | Massive demand for debt and a rate cycle just getting started, running at each other like  |
| SH110 | 697.2 | 4.4 | 1 | Let the AI companies burn to the ground |
| SH111 | 701.6 | 3.8 | 3 | But the damage doesn't stay inside the industry: we're all gonna get kicked |
| SH112 | 705.4 | 18.3 | 3 | Evidence: data-centre spending grows about 0.85 points of GDP a year, twice the housing-bo |
| SH113 | 723.7 | 3.8 | 6 | So the AI build-out is going roughly twice as fast as the housing bubble |
| SH114 | 727.5 | 2.7 | 2 | And we all remember how that one ended |
| SH115 | 730.2 | 1.8 | 2 | AI isn't just growing fast |
| SH116 | 732.0 | 2.0 | 2 | It is the growth in the economy |
| SH117 | 734.0 | 6.3 | 1 | Evidence: AI capex is about a 1.5-point boost to US growth |
| SH118 | 740.3 | 8.2 | 3 | Evidence: private data-centre construction up 57% in a year (Our World in Data) |
| SH119 | 748.5 | 6.7 | 4 | Evidence: America spends more building data centres than office buildings (Census Bureau) |
| SH120 | 755.2 | 5.0 | 4 | The good news: nothing's broken yet |
| SH121 | 760.2 | 3.4 | 1 | But the absence of damage is not evidence of safety |
| SH122 | 763.6 | 5.9 | 3 | JP Morgan plotted what the big five tech companies do with every dollar of revenue |
| SH123 | 769.5 | 6.0 | 3 | Evidence: capital spending never took more than 13 cents of a revenue dollar; this year it |
| SH124 | 775.5 | 2.6 | 4 | Almost every cent the businesses bring in |
| SH125 | 778.1 | 3.2 | 1 | For the first time on the chart, free cash flow goes negative |
| SH126 | 781.3 | 7.6 | 7 | Every year more has to be financed by debt, at a rate that rises with it |
| SH127 | 789.0 | 3.7 | 1 | That's where the dots actually connect for the rate-hike decision |
| SH128 | 792.6 | 6.3 | 5 | The kind of detail traditional media leaves out |
| SH129 | 798.9 | 5.6 | 3 | If you find this interesting, hit subscribe |
| SH130 | 804.5 | 2.8 | 4 | You'll keep hearing the same story: the Fed raising rates by a quarter point (headline car |
| SH131 | 807.3 | 2.0 | 1 | But that's not the real story |
| SH132 | 809.4 | 12.0 | 15 | The real story: the largest buildout in history keeps going back to the market for more mo |
| SH133 | 821.4 | 6.2 | 1 | End card: subscribe for more (held about 6 s after the narration ends) |
