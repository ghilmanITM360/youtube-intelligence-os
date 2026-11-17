# VISUAL RECONSTRUCTION — The Stock Market Is Being Used as a Dumping Ground (roe3SgezmmU)

_Source: LONG_FORM · 1280×720 @ 24.0 fps · 1042.8s · published 2026-10-04 · SHA256 `e34e0e44963debee…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **25027** (every frame). Reviewed shots: **191**; stable states: **635**; motion rows: **632**; micro-changes below threshold (counted, not tabulated): 151.
- Shot length: median **4.0s**, mean 5.5s, p10 1.6s, p90 12.6s → **11.0 shots/min**.
- Visual-state length: median **0.96s**, mean 1.30s → **36.5 states/min** (a new composition state roughly every 1.6s incl. transitions).
- Time in transitions/animation (frames between stable states): **219s (21%)**; stable states **824s (79%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 58%; SCREEN_CAPTURE 48%; MOTION_GRAPHICS 47%; COMPOSITED_STILLS 21%; STOCK_FOOTAGE 2%. Shots made only of drawn assets + text motion: 34% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 225, POP_IN 144, TEXT_REVEAL 50, SCROLL 28, ZOOM_IN 23, DRAW_ON 22, HIGHLIGHT 21, REPOSITION 14, FACE_CHANGE 11, REFRAME 8, SWAP 8, TEXT_SWAP 7, EXIT 7, SLIDE_IN 6.
- Narration pace: **194 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 407, DURING_WORD 304, BEFORE_WORD 94, AFTER_WORD 15, IN_PAUSE 3.
- Shot-start offset vs nearest word start: median **17 ms** (p10 -72, p90 293); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 104 of 210 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| HOST | CHARACTER_HOST | 262.8 | 99 | ORIGINAL_DRAWING |
| TXT_HANDLETTER | TEXT_LETTERING | 102.88 | 44 | MOTION_GRAPHICS |
| POINTER | PROP | 90.29 | 26 | ORIGINAL_DRAWING |
| OBJ_MONEYBAGS | OBJECT | 74.25 | 26 | ORIGINAL_DRAWING |
| LOGO_AMAZON | LOGO | 58.96 | 12 | COMPOSITED_STILLS |
| HL_TEXT_MARKER_GREEN | ANNOTATION_OVERLAY | 51.21 | 7 | MOTION_GRAPHICS |
| OBJ_LAPTOP_CF | OBJECT | 51.16 | 9 | ORIGINAL_DRAWING |
| BLDG_TOWERS | OBJECT_BUILDING | 49.96 | 21 | ORIGINAL_DRAWING |
| HL_TEXT_MARKER | ANNOTATION_OVERLAY | 48.5 | 10 | MOTION_GRAPHICS |
| UI_YELLOW_PROGRESS | UI_OVERLAY | 48.04 | 19 | MOTION_GRAPHICS |
| CHAR_PROFESSOR | CHARACTER | 43.25 | 6 | ORIGINAL_DRAWING |
| LOGO_SPACEX | LOGO | 42.59 | 17 | COMPOSITED_STILLS |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 3 | 1 | 2 | 240 | 1 | 1 |
| 5-15s (5-15s) | 6 | 1 | 6 | 174 | 1 | 0 |
| 15-30s (15-30s) | 9 | 0 | 9 | 184 | 4 | 0 |
| 30-60s (30-60s) | 20 | 8 | 20 | 192 | 6 | 5 |
| 60s-midpoint (60-521s) | 292 | 94 | 291 | 195 | 37 | 66 |
| midpoint-last60s (521-983s) | 268 | 77 | 268 | 192 | 37 | 48 |
| last 60s (983-1043s) | 37 | 10 | 36 | 178 | 0 | 6 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Blank white canvas; host stick figure at left-centre (round peach head, black spiky hair, skeptical frown, one raised eyebrow) holding a long brown po [S001.1 @0.7s] Host now smiling, pointer touching the base of the left stacked bar; chart panel has appeared at right with stacked bar $5.2T (OpenAI $1.2T / Anthropi [S001.2 @3.1s] Host gone; chart enlarged to fill the frame; a hand-drawn red rectangle outlines the grey $4.1T bar [S001.3 @5.7s] Chart shrinks to left; red box still on grey bar; hand-lettered words 'Initial Public Offering' appear right with red initial capitals I P O; small ye

Closing frames: [S119.6 @1033.9s] Host's face switches to worried wide eyes [S119.7 @1035.4s] Diagram inverted: 'Invest a lot [money bag] and you could… Earn nothing [coins]'; host still worried [S119.8 @1036.5s] End screen: white canvas with a hand-drawn circle (subscribe placeholder), 'Subscribe for more Casual Finance', a rectangle (next-


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 13.3 | 6 | Hook: viral IPO chart introduced by host with pointer |
| SH002 | 13.3 | 17.3 | 12 | Context: dot-com + three AI giants vs thousands of companies |
| SH003 | 30.6 | 2.9 | 2 | Evidence: Anthropic/OpenAI confidential S-1 announcements |
| SH004 | 33.5 | 18.8 | 11 | Evidence: SpaceX Nasdaq debut and Anthropic IPO headlines |
| SH005 | 52.2 | 1.2 | 2 | Central question posed on chalkboard |
| SH006 | 53.5 | 1.4 | 1 | Cast of opinion-givers: Wall Street analyst, famous investors, Reddit |
| SH007 | 54.9 | 1.2 | 1 | Cast: 'famous investors' |
| SH008 | 56.0 | 1.1 | 1 | Cast: 'everyone on Reddit' |
| SH009 | 57.1 | 2.0 | 1 | Cast arguing together |
| SH010 | 59.2 | 2.2 | 1 | Transition to the better question: host reset |
| SH011 | 61.4 | 2.8 | 2 | Callback to the valuation scale (value left) |
| SH012 | 64.2 | 12.5 | 8 | Example: Amazon IPO 1997 returns |
| SH013 | 76.7 | 7.8 | 3 | Evidence: Amazon stock chart payoff with comic salesman skit |
| SH014 | 84.5 | 1.9 | 2 | Pivot: 'Now look at SpaceX' |
| SH015 | 86.4 | 4.9 | 3 | SpaceX IPO price: $135 / $1.8 trillion |
| SH016 | 91.3 | 7.1 | 7 | Comparison: Amazon x3,325 vs SpaceX |
| SH017 | 98.4 | 6.6 | 5 | Scale of $5.9 quadrillion vs world wealth (11x) |
| SH018 | 105.0 | 1.0 | 1 | Re-state: chalkboard setup then Amazon recap |
| SH019 | 106.0 | 9.8 | 6 | Difference is where they started: Amazon $429.5M |
| SH020 | 115.8 | 3.0 | 3 | Aside: SpaceX 'big boy now' |
| SH021 | 118.8 | 2.3 | 2 | 'That's the change hiding inside this chart' |
| SH022 | 121.1 | 3.7 | 3 | 'Companies used to go public to pay for their growth' |
| SH023 | 124.8 | 1.5 | 2 | 'Now they go public after they've grown' |
| SH024 | 126.3 | 5.7 | 3 | Not about one IPO: host with three logos |
| SH025 | 132.0 | 2.5 | 1 | Evidence: Bessembinder 100-year study |
| SH026 | 134.6 | 4.0 | 2 | Evidence: study abstract |
| SH027 | 138.6 | 2.2 | 2 | Typical stock lost money: laptop price chart |
| SH028 | 140.8 | 0.7 | 1 | Host at the laptop (my brokerage account) |
| SH029 | 141.5 | 4.2 | 3 | Where does the money come from? |
| SH030 | 145.7 | 3.1 | 1 | Concentration: 46 firms made half the wealth |
| SH031 | 148.8 | 4.6 | 1 | Abstract highlight: just 46 firms |
| SH032 | 153.4 | 4.5 | 3 | Evidence: Table of largest wealth creators |
| SH033 | 158.0 | 2.0 | 2 | Top five wealth creators named |
| SH034 | 160.0 | 4.4 | 6 | Top five wealth creators: logo reveal |
| SH035 | 164.4 | 5.2 | 4 | Value at time of IPO: single money bag |
| SH036 | 169.5 | 4.0 | 2 | Growth happened after IPO: SpaceX vs bags |
| SH037 | 173.5 | 4.1 | 2 | Evidence: today's largest companies by market cap |
| SH038 | 177.7 | 6.8 | 5 | The five now: grown and worth $21T |
| SH039 | 184.5 | 2.5 | 1 | Host reset before venture-capital evidence |
| SH040 | 186.9 | 9.4 | 1 | Evidence: a16z 'Private Markets Are The New High-Growth Public Markets' |
| SH041 | 196.3 | 14.5 | 7 | a16z article scroll to the key chart |
| SH042 | 210.8 | 6.2 | 3 | Joke: VC keeps the cake |
| SH043 | 217.0 | 3.0 | 3 | Vanguard report introduced |
| SH044 | 220.0 | 3.6 | 2 | Evidence: Vanguard 'Private longer, public later' report |
| SH045 | 223.6 | 4.0 | 3 | Vanguard added up every private startup worth a billion |
| SH046 | 227.7 | 3.0 | 1 | Vanguard report again |
| SH047 | 230.6 | 10.8 | 5 | Evidence: Vanguard Figure 2 — unicorns worth $8.6T |
| SH048 | 241.5 | 5.2 | 5 | Trillions of growth that never traded publicly |
| SH049 | 246.6 | 5.0 | 3 | Three things pushed companies public |
| SH050 | 251.7 | 3.2 | 4 | Timeline: 2000s, 2010s, 2020s |
| SH051 | 254.8 | 0.7 | 1 | Host reset |
| SH052 | 255.5 | 2.8 | 2 | Transition to sponsor topic: 'what quietly influences where the money goes' |
| SH053 | 258.4 | 3.5 | 2 | Loyalty/sponsor lead-in: video-player laptop |
| SH054 | 261.9 | 2.7 | 2 | Money bag with eyes |
| SH055 | 264.5 | 3.8 | 4 | Sponsor lead-in: loyalty programs change your behaviour |
| SH056 | 268.3 | 3.1 | 2 | Loyalty examples: airline and store |
| SH057 | 271.5 | 1.9 | 2 | 'It works!' |
| SH058 | 273.3 | 7.2 | 5 | Evidence: Bond Loyalty Report |
| SH059 | 280.6 | 2.5 | 1 | Sponsor reveal: chalkboard host |
| SH060 | 283.1 | 1.6 | 1 | Sponsor logo build: LT + loyalty card morph into Bilt |
| SH061 | 284.7 | 3.0 | 3 | Bilt sponsor read: what Bilt does |
| SH062 | 287.8 | 3.8 | 3 | Bilt as a character giving points |
| SH063 | 291.5 | 3.7 | 1 | Paying housing costs: stressed payer |
| SH064 | 295.2 | 2.6 | 4 | Host back: payment you already make earns points |
| SH065 | 297.8 | 5.0 | 2 | Everyday spending at 50,000+ partner businesses |
| SH066 | 302.8 | 2.2 | 1 | Host beat |
| SH067 | 305.0 | 7.0 | 10 | Redeem for stays, flights, rides, orders |
| SH068 | 312.0 | 3.0 | 2 | Host reaction |
| SH069 | 315.0 | 4.8 | 2 | Sponsor CTA: QR code |
| SH070 | 319.7 | 3.5 | 2 | Join 7M+ members, free |
| SH071 | 323.2 | 9.3 | 5 | Thank-you outro of sponsor read |
| SH072 | 332.6 | 1.5 | 1 | Sponsor link on screen |
| SH073 | 334.0 | 3.0 | 2 | Thank-you: Bilt character gives thumbs-up |
| SH074 | 337.0 | 3.1 | 3 | Back to content: companies needed real money |
| SH075 | 340.1 | 0.9 | 1 | Host beat |
| SH076 | 341.0 | 3.7 | 4 | Small business vs big business needing money |
| SH077 | 344.7 | 2.5 | 2 | Only one place to get money: the stock market |
| SH078 | 347.2 | 1.8 | 2 | 'Going public wasn't a victory lap' |
| SH079 | 349.0 | 1.4 | 2 | Big business gets tired |
| SH080 | 350.4 | 6.3 | 3 | Evidence: Amazon's 1997 prospectus (Form 424B1) |
| SH081 | 356.7 | 13.6 | 6 | The prospectus says no specific plan for proceeds |
| SH082 | 370.3 | 5.9 | 5 | Amazon was a tiny baby; one year before: 1996 |
| SH083 | 376.2 | 5.0 | 3 | 1997 → 1996 (the year before the IPO) |
| SH084 | 381.2 | 2.6 | 2 | Evidence: National Securities Markets Improvement Act of 1996 |
| SH085 | 383.8 | 8.8 | 3 | Evidence: the 100-investor limit (1940 Act page) |
| SH086 | 392.6 | 8.4 | 5 | A billion-dollar fund needs ~100 investors at $10M each |
| SH087 | 401.0 | 1.8 | 1 | Host beat |
| SH088 | 402.8 | 4.2 | 3 | Rich individuals writing massive checks |
| SH089 | 407.0 | 5.4 | 8 | Private funds were small: not enough capital to go around |
| SH090 | 412.4 | 14.0 | 8 | Evidence: 'The Deregulation of the Private Equity Market' paper |
| SH091 | 426.4 | 2.4 | 1 | Institutional capital floods the private markets |
| SH092 | 428.8 | 15.0 | 6 | Evidence: late-stage private capital growth |
| SH093 | 443.8 | 4.1 | 2 | Gag: money bag greets small briefcase |
| SH094 | 448.0 | 3.2 | 3 | Evidence: authors of the study |
| SH095 | 451.1 | 10.8 | 2 | Evidence: aggregate capital raised by late-stage startups |
| SH096 | 461.9 | 12.7 | 10 | Evidence: IPO proceeds in 2015 (Jay Ritter statistics) |
| SH097 | 474.6 | 8.6 | 3 | Companies no longer needed the stock market for capital |
| SH098 | 483.2 | 3.4 | 3 | Evidence: Public Law 104-290 again |
| SH099 | 486.6 | 2.1 | 2 | The second thing to stop working: the 500-shareholder rule |
| SH100 | 488.7 | 1.5 | 2 | Chalkboard: 'Da rule' |
| SH101 | 490.2 | 2.9 | 3 | The rule character pushes companies public |
| SH102 | 493.1 | 5.0 | 3 | Evidence: Securities Acts Amendments of 1964 (Section 12(g)) |
| SH103 | 498.1 | 3.8 | 2 | Gag: 'Section 12G … a seat on a budget airline' |
| SH104 | 501.9 | 20.0 | 6 | Evidence: Carta — Section 12(g) is 'the trigger that pushes private companies public' |
| SH105 | 521.9 | 2.4 | 3 | Startups pay with stock: employees become shareholders |
| SH106 | 524.2 | 1.5 | 3 | Startups pay people in stock (stonks) |
| SH107 | 525.7 | 2.9 | 3 | Employees paid in stock instead of cash |
| SH108 | 528.6 | 2.6 | 5 | Every employee with shares is one more shareholder |
| SH109 | 531.2 | 6.4 | 2 | Evidence: Carta 'Background' — Google and Facebook forced public |
| SH110 | 537.6 | 1.8 | 2 | Microsoft in the 1980s |
| SH111 | 539.4 | 1.4 | 3 | Evidence: 1986 Fortune story on Microsoft's IPO (via RealClearMarkets) |
| SH112 | 540.8 | 12.8 | 3 | Microsoft: 500 shareholders would force registration |
| SH113 | 553.6 | 7.9 | 4 | Jon Shirley quote: 'We decided to do it when we wanted to' |
| SH114 | 561.5 | 6.5 | 2 | Microsoft went public in 1986 |
| SH115 | 568.0 | 15.7 | 6 | Evidence: Google's 2004 S-1 — 'The deadline imposed by this requirement accelerated our de |
| SH116 | 583.8 | 3.5 | 2 | Facebook / Zuckerberg |
| SH117 | 587.3 | 12.6 | 5 | Evidence: TechCrunch 2010 — 'Facebook Will Not Go Public Anytime Soon' |
| SH118 | 599.9 | 4.8 | 5 | Facebook didn't need the money: hottest startup in the world |
| SH119 | 604.8 | 18.2 | 3 | Evidence: Facebook raises $1.5 billion (Jan 2011 press release) |
| SH120 | 623.0 | 15.3 | 5 | Facebook: worst of both worlds |
| SH121 | 638.3 | 3.2 | 2 | Facebook did go public: stock then and now |
| SH122 | 641.5 | 13.3 | 6 | Evidence: TechCrunch May 2012 — Zuckerberg hoodie / 'Our Mission Isn't To Be A Public Comp |
| SH123 | 654.8 | 9.1 | 2 | Zuckerberg's 'funny thing to say on the day you become one' |
| SH124 | 663.9 | 13.0 | 4 | Found footage: Zuckerberg podcast clip inside a drawn laptop screen |
| SH125 | 676.9 | 5.0 | 4 | Evidence: 1964 Act page 2 — the 500-holder trigger |
| SH126 | 681.9 | 6.8 | 2 | Callback: Carta Background — Google and Facebook |
| SH127 | 688.7 | 6.2 | 4 | Evidence: JOBS Act (Public Law 112-106, April 5, 2012) |
| SH128 | 694.9 | 5.1 | 3 | Gag: congress staffer proud of the acronym 'JOBS' |
| SH129 | 700.0 | 14.5 | 5 | Back to the Act: Title I and Title V |
| SH130 | 714.5 | 2.8 | 2 | Title V rewrites 12(g): 500 → 2,000 |
| SH131 | 717.2 | 9.6 | 5 | The law rewrote the rule: Microsoft, Google, Facebook stock then and now |
| SH132 | 726.8 | 9.5 | 2 | JOBS Act Title V: 2,000 holders; employees excluded |
| SH133 | 736.4 | 4.5 | 2 | Callback: Microsoft's 500 employees |
| SH134 | 740.8 | 5.7 | 2 | With rules rewritten, big business pushes back: money talks |
| SH135 | 746.5 | 3.7 | 4 | Rules character and big business |
| SH136 | 750.2 | 4.2 | 2 | Host beat: what's left |
| SH137 | 754.4 | 4.3 | 4 | Gate metaphor: the brick wall 'our business!' |
| SH138 | 758.7 | 7.7 | 7 | The payday: shares worth billions on paper |
| SH139 | 766.4 | 13.0 | 4 | Evidence: 'The Once and Future Irrelevancy of Section 12(g)' |
| SH140 | 779.5 | 7.4 | 4 | Cap before/after the JOBS Act; tender offers |
| SH141 | 786.9 | 2.6 | 2 | Tender offer = a yard sale a company runs for its own stock |
| SH142 | 789.5 | 7.9 | 7 | Employees and early investors bring shares; invited investors bring cash |
| SH143 | 797.4 | 5.7 | 3 | Stripe: the best example |
| SH144 | 803.1 | 7.0 | 5 | Evidence: Multiples — 50 most valuable private companies (Sept 2026) |
| SH145 | 810.0 | 16.7 | 6 | Stripe's tender offers: $65B (2024) → $159B (2026) |
| SH146 | 826.8 | 2.7 | 1 | Gag: no cake for us |
| SH147 | 829.4 | 7.5 | 4 | Evidence: Payments Dive — Stripe shows signs of IPO despite co-founder comments |
| SH148 | 836.9 | 5.3 | 4 | Gag: 'we should totally hang out sometime' |
| SH149 | 842.2 | 5.2 | 4 | Summary: three changes put together |
| SH150 | 847.4 | 3.9 | 3 | Three changes together: the JOBS Act page and the rewritten rules |
| SH151 | 851.3 | 1.5 | 1 | Rules character callback |
| SH152 | 852.8 | 6.4 | 6 | Tender offers let employees cash out without an IPO |
| SH153 | 859.2 | 3.4 | 3 | The new system: IPOs after growth; law no longer forcing IPOs |
| SH154 | 862.6 | 4.5 | 3 | Stripe: why would it go public? Valuation history |
| SH155 | 867.1 | 1.9 | 2 | Chalkboard: RIGHT NOW! |
| SH156 | 869.0 | 9.7 | 9 | Evidence: median time from founding to IPO (a16z) — 5 → 14 years |
| SH157 | 878.7 | 3.3 | 2 | Evidence: FXC Intelligence on Stripe's 2025 volume and valuation |
| SH158 | 882.0 | 1.0 | 1 | Chalkboard beat |
| SH159 | 883.0 | 12.0 | 8 | Evidence: fewer VC-backed IPOs — 266 in 1996 vs 49 last year (Ritter data) |
| SH160 | 895.0 | 3.3 | 3 | If companies don't need public markets, why is SpaceX going public? |
| SH161 | 898.3 | 1.0 | 2 | SpaceX went public anyway |
| SH162 | 899.3 | 3.3 | 3 | Anthropic and OpenAI lining up next |
| SH163 | 902.6 | 0.9 | 1 | Host nervous beat before research aside |
| SH164 | 903.5 | 10.6 | 1 | Aside: 'making this video meant reading a securities law from 1964, Amazon's filings, and  |
| SH165 | 914.1 | 2.7 | 2 | CTA: subscribe ask (mid-video) |
| SH166 | 916.8 | 3.7 | 2 | CTA: the channel page |
| SH167 | 920.5 | 3.5 | 3 | Why go public at all? |
| SH168 | 924.0 | 3.2 | 3 | Chalkboard: Go public because… money? |
| SH169 | 927.2 | 6.3 | 6 | Callback: a16z return-potential chart |
| SH170 | 933.5 | 12.3 | 9 | Anthropic valuation: $61.5B (Mar 2025) → $965B (May 2026) |
| SH171 | 945.8 | 4.1 | 3 | Anthropic's IPO aims at double: $2T |
| SH172 | 949.9 | 2.0 | 2 | So you're saying… |
| SH173 | 951.9 | 4.8 | 2 | Evidence: AEI — Amazon's IPO 1997 market cap $438M |
| SH174 | 956.6 | 7.7 | 8 | Callback: Amazon at IPO — asymmetric bet |
| SH175 | 964.3 | 4.5 | 4 | Worst case vs best case for early public investors |
| SH176 | 968.8 | 1.5 | 2 | Best case: never work again |
| SH177 | 970.2 | 2.0 | 2 | Loser's quip |
| SH178 | 972.2 | 2.4 | 2 | Best case: you never had to work again |
| SH179 | 974.6 | 2.9 | 4 | A chance to invest before it was priced like it had built the future |
| SH180 | 977.5 | 3.0 | 3 | Today's offers: SpaceX, Anthropic, OpenAI headlines |
| SH181 | 980.5 | 6.9 | 5 | Asymmetric bet |
| SH182 | 987.5 | 3.1 | 2 | But today that has flipped |
| SH183 | 990.5 | 4.8 | 3 | At nearly $2T, how much upside is left? |
| SH184 | 995.3 | 5.0 | 4 | 10× return = almost $2T × 10 = $17.7T |
| SH185 | 1000.4 | 2.9 | 2 | About a quarter of the entire American stock market |
| SH186 | 1003.3 | 6.2 | 3 | And for 100× — same returns as Amazon |
| SH187 | 1009.5 | 4.1 | 4 | SpaceX would need to be worth more than every public company on Earth combined |
| SH188 | 1013.6 | 3.0 | 3 | Host reset; the three giants |
| SH189 | 1016.5 | 3.3 | 2 | Closing chalkboard |
| SH190 | 1019.8 | 16.7 | 9 | Closing payoff: the same chart, a different bet |
| SH191 | 1036.5 | 6.2 | 1 | End card |

## 3. Reviewed interpretation (evidence-labelled)

**Core visual formula (OBSERVED, repeated across the whole runtime).** White full-bleed canvas → one primary "evidence object" (screenshot, document, chart, logo, headline card) → hand-drawn annotation layer (red box, highlighter, hand-lettered number, arrow) → host/character reaction pop-in → cut. States change every ~1.0 s (median) and a reviewed shot lasts ~4 s (median). 39% of runtime shows a screenshot-type asset, 25% shows the stick-figure host, 17% shows brand logos, 33% of runtime has some drawn-object layer. Only ~1% is real video (the Zuckerberg podcast clip, S077.0–S078.1, and two tiny meme clips inside speech bubbles, S083.1–S084.0).

**Recurring recipes (each with evidence IDs; reconstruction is tool-agnostic):**
1. *Document call-out* — screenshot of a primary source fills frame → highlighter wipe over the exact sentence → optional red box → host leans in with pointer. Evidence: S015.0–S015.1, S044.1–S044.6, S060.0–S061.1, S066.0–S066.1, S076.5. Build: full-bleed still, rectangle layer with multiply blend, wipe-in mask over 6–12 frames, host layer pops in on narration keyword.
2. *Number reveal build* — brand logo → hand-lettered "Worth $X" in green → second column → red down-arrow with multiplier → payoff number in outlined red. Evidence: S007.7–S007.14, S010.0–S010.6, S013.2–S013.4, S108.6–S108.14. Build: label layers appear on successive 0.4–1.0 s states; red for the surprising figure, green for the reference figure.
3. *Company-as-character* — logos get baby faces/pacifiers (young), muscular arms (grown), stick legs (acting) to dramatise life stages. Evidence: S007.9, S007.14, S021.7, S022.3, S119.3. Build: transparent PNG overlays on the logo layer; swapped as state replacements, not tweened.
4. *Callback gag* — a character with a speech bubble repeats an earlier line: "Get yo @rse into the stock market!" (S053.1, S084.2, S095.0). Joke density: ~50 gag states (speech bubbles, handwritten asides, meme tiles, 'sorry', 'tehee').
5. *Magnitude visualisation* — absurd totals are shown against a familiar object: Earth character (S011.0–S011.2, S115.2–S116.1), US-map character carrying buildings, pie chart (S113.14–S113.15), balance scale (S005.1–S005.4).
6. *Chalkboard beat* — host + pointer + green board used to pose a section's question ("Are they worth it?", "Three factors", "Da rule", "RIGHT NOW!", "PAY ATTENTION because this ain't the same!!!"): S006.0–S006.1, S027.0–S027.2, S052.0–S052.1, S098.0–S098.1, S107.0–S107.2, S118.0–S118.1. Appears at the head of each argumentative section.
7. *Found footage in a drawn frame* — real clip (podcast) inside a hand-drawn laptop bezel so third-party video still looks native (S077.0–S078.1).
8. *Sponsor integration* — 70 s Bilt read with a yellow progress bar along the bottom edge (S032.4–S036.37, ≈266–337 s), mascot-ised sponsor logo (S036.3), QR code and on-screen URL (S036.26–S036.35); returns to the main thread via a character gag (S036.38–S036.44).
9. *Open/close symmetry* — the viral valuation chart opens the video (S001.1) and returns as the final argument frame (S119.0); the closing "asymmetric bet" diagram inverts the earlier risk/reward drawings (S113.0–S113.4 → S119.5–S119.7).

**Audio observation (MEASURED, signal-level only).** Narration is the only continuous sound: gaps drop to near-digital silence, there is no sustained music bed in the body, no non-speech transients were detected (0 of 16 strong onsets fell outside speech), and the only music/ambient-like content is the final ~6.3 s end-card tail (1036.5–1042.8 s). The Zuckerberg clip (≈662–677 s) carries third-party room tone. The video therefore relies on visual change and narration pacing (194 words/min) rather than sound design for energy.

**What this video does NOT show (negative evidence).** No 3D objects; no camera moves beyond zoom/scroll on screenshots; no easing that can be separated from linear motion; no sound effects; no real talking-head.

**Counter-evidence displayed but not narrated (flag for fact-check).** The Rodrigues paper shown at S087.1 states that Section 12(g) "probably forced very few firms public" (2.94% of firms, 35 of 1,192) and calls Google/Facebook "outliers", while the narration (T0132–T0133) says the rule "forced some of the most successful companies … to go public". Both can be true (named examples vs base rate), but the base-rate nuance is only on screen.

**Possible viewer-confusion point.** Amazon column shows market value $429.5M→$2.69T beside a "x 3,325 growth" label and $1,000→$3,325,000 (S007.13–S007.14). The market-value ratio is ~6,260× while 3,325× matches the investment multiple; the difference (share-count growth) is not narrated. Marked UNVERIFIED in `FINANCE_CLAIMS.csv`.

**Production-risk note for anyone rebuilding.** The original relies on many third-party screenshots, logos and meme images; an original build should use its own captures, licensed/own-brand assets and original character art.

