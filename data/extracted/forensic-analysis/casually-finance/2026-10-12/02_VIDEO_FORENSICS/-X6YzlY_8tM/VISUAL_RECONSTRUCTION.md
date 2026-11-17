# VISUAL RECONSTRUCTION — The SpaceX IPO... It's Worse Than You Think (-X6YzlY_8tM)

_Source: LONG_FORM · 1280×720 @ 24.0 fps · 892.1s · published 2026-05-21 · SHA256 `adff66768f5545cd…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **21410** (every frame). Reviewed shots: **230**; stable states: **572**; motion rows: **571**; micro-changes below threshold (counted, not tabulated): 84.
- Shot length: median **3.1s**, mean 3.9s, p10 1.1s, p90 7.3s → **15.5 shots/min**.
- Visual-state length: median **0.96s**, mean 1.35s → **38.5 states/min** (a new composition state roughly every 1.6s incl. transitions).
- Time in transitions/animation (frames between stable states): **120s (13%)**; stable states **773s (87%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): MOTION_GRAPHICS 100%; ORIGINAL_DRAWING 77%; SCREEN_CAPTURE 23%. Shots made only of drawn assets + text motion: 77% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 210, BUILD 119, LOOP_ANIM 69, TEXT_REVEAL 56, POSE_CHANGE 23, STRIKE 10, HIGHLIGHT 9, FACE_CHANGE 8, SWAP 8, EXIT 8, ZOOM_IN 7, STACK 7, HOLD 6, TEXT_SWAP 6.
- Narration pace: **187 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 344, DURING_WORD 311, BEFORE_WORD 97, AFTER_WORD 41, IN_PAUSE 8.
- Shot-start offset vs nearest word start: median **21 ms** (p10 -88, p90 284); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 89 of 228 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| HOST | CHARACTER_HOST | 201.13 | 76 | ORIGINAL_DRAWING |
| UI_SPONSOR | UI_OVERLAY | 86.38 | 26 | MOTION_GRAPHICS |
| LOGO_SPACEX | LOGO | 85.2 | 23 | COMPOSITED_STILLS |
| OBJ_LAPTOP | OBJECT | 51.25 | 14 | ORIGINAL_DRAWING |
| OBJ_RULES | OBJECT | 44.0 | 13 | ORIGINAL_DRAWING |
| POINTER | PROP | 42.63 | 12 | ORIGINAL_DRAWING |
| OBJ_DESK | OBJECT | 40.92 | 11 | ORIGINAL_DRAWING |
| OBJ_BOARD | OBJECT | 38.38 | 11 | ORIGINAL_DRAWING |
| LOGO_XAI | LOGO | 36.21 | 9 | COMPOSITED_STILLS |
| LOGO_STARLINK | LOGO | 36.12 | 10 | COMPOSITED_STILLS |
| OBJ_CASH | OBJECT | 35.84 | 14 | ORIGINAL_DRAWING |
| CHAR_MUSK | CHARACTER | 34.75 | 16 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 4 | 2 | 4 | 192 | 2 | 2 |
| 5-15s (5-15s) | 26 | 4 | 26 | 150 | 2 | 1 |
| 15-30s (15-30s) | 17 | 5 | 16 | 200 | 3 | 3 |
| 30-60s (30-60s) | 15 | 7 | 15 | 202 | 1 | 7 |
| 60s-midpoint (60-446s) | 232 | 92 | 232 | 178 | 31 | 57 |
| midpoint-last60s (446-832s) | 240 | 106 | 241 | 194 | 25 | 76 |
| last 60s (832-892s) | 38 | 14 | 37 | 163 | 2 | 7 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Host smiles holding pointer [S001.1 @1.4s] Host points at company capitalization ranking [S002.0 @4.3s] SpaceX red valuation bar above smiling Musk with arms shifting [S002.1 @4.7s] SpaceX red valuation bar above smiling Musk with arms shifting

Closing frames: [S106.6 @882.9s] Victory caption beside Musk [S106.7 @883.3s] Musk enlarged with caption [S106.8 @883.9s] Final subscribe card and YouTube-only icons


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 4.3 | 2 | Host smiles holding pointer |
| SH002 | 4.3 | 7.5 | 21 | SpaceX red valuation bar above smiling Musk with arms shifting |
| SH003 | 11.8 | 0.4 | 1 | Red comparison slogan added beside Musk |
| SH004 | 12.1 | 0.4 | 1 | Musk stands atop SpaceX valuation bar |
| SH005 | 12.5 | 0.8 | 1 | Musk stands atop SpaceX valuation bar |
| SH006 | 13.2 | 4.0 | 10 | Musk stands atop SpaceX valuation bar |
| SH007 | 17.2 | 4.3 | 2 | SpaceX bar compared with ten LSE companies |
| SH008 | 21.5 | 1.6 | 2 | Host smiles on white |
| SH009 | 23.1 | 3.2 | 3 | SpaceX logo |
| SH010 | 26.3 | 2.8 | 2 | Ranking chart returns |
| SH011 | 29.1 | 3.6 | 2 | Host has angel and devil Musk figures on shoulders |
| SH012 | 32.7 | 4.9 | 3 | 401k paper alone |
| SH013 | 37.6 | 5.6 | 3 | Nasdaq logo |
| SH014 | 43.2 | 4.2 | 2 | Host smiles |
| SH015 | 47.4 | 1.2 | 1 | SpaceX logo on white |
| SH016 | 48.7 | 6.4 | 1 | White SpaceX logo sparkles on black |
| SH017 | 55.1 | 1.3 | 1 | Host frowns with arm out |
| SH018 | 56.4 | 5.2 | 5 | Street interviewer with microphone and tiny crowd |
| SH019 | 61.7 | 1.2 | 2 | Two respondents alone |
| SH020 | 62.8 | 2.0 | 2 | SpaceX logo returns |
| SH021 | 64.9 | 2.6 | 3 | First business carton appears |
| SH022 | 67.5 | 2.5 | 2 | Single rocket replaces cartons |
| SH023 | 70.0 | 3.1 | 3 | SpaceX presents poster slice The Good |
| SH024 | 73.2 | 2.5 | 2 | Host smiles |
| SH025 | 75.6 | 5.2 | 5 | Ugly poster slice next to business carton |
| SH026 | 80.8 | 5.5 | 5 | Carton opens showing xAI logo with Musk |
| SH027 | 86.4 | 1.2 | 1 | Black screen |
| SH028 | 87.6 | 1.1 | 1 | Host neutral expression |
| SH029 | 88.7 | 2.2 | 3 | Open xAI carton returns |
| SH030 | 91.0 | 0.9 | 1 | Host smiles sweating with arms out |
| SH031 | 91.8 | 6.4 | 12 | xAI logo as ninja with headband and limbs |
| SH032 | 98.2 | 0.4 | 1 | Time transition phrase |
| SH033 | 98.7 | 10.3 | 3 | SpaceX and xAI logos separate |
| SH034 | 109.0 | 1.8 | 1 | Host concerned |
| SH035 | 110.8 | 4.4 | 2 | SpaceX logo alone |
| SH036 | 115.1 | 2.3 | 2 | Enlarged host shrugs |
| SH037 | 117.5 | 2.8 | 2 | xAI logo again |
| SH038 | 120.3 | 3.0 | 2 | xAI character holds phone |
| SH039 | 123.3 | 2.5 | 2 | Host concerned |
| SH040 | 125.8 | 5.3 | 4 | xAI logo alone |
| SH041 | 131.1 | 4.0 | 1 | Founding-team photograph |
| SH042 | 135.1 | 4.0 | 4 | DeepMind logo |
| SH043 | 139.1 | 2.5 | 1 | Host smiles shrugs |
| SH044 | 141.6 | 0.6 | 1 | Arrow points to year |
| SH045 | 142.2 | 2.8 | 9 | Bloomberg burn headline above flaming money bags |
| SH046 | 145.0 | 1.2 | 1 | Host frowns |
| SH047 | 146.2 | 4.0 | 1 | Faded team photo |
| SH048 | 150.2 | 2.5 | 1 | Musk alone neutral |
| SH049 | 152.7 | 4.5 | 1 | Musk beside his post about rebuilding xAI |
| SH050 | 157.1 | 1.4 | 1 | Host neutral hands on hips |
| SH051 | 158.5 | 5.3 | 3 | Enlarged neutral Musk |
| SH052 | 163.9 | 1.4 | 3 | xAI logo broken into black pieces |
| SH053 | 165.2 | 4.2 | 2 | Host smiles |
| SH054 | 169.4 | 19.4 | 4 | AI comparison chart with OpenAI revenue only |
| SH055 | 188.8 | 5.2 | 3 | Host smiles |
| SH056 | 194.1 | 4.4 | 2 | Host concerned raises hand |
| SH057 | 198.5 | 1.2 | 1 | Host smiling shrugs |
| SH058 | 199.7 | 3.1 | 10 | Burn headline returns above money bags with changing flames |
| SH059 | 202.8 | 6.4 | 4 | First business carton |
| SH060 | 209.2 | 2.5 | 1 | Host smiling arm out |
| SH061 | 211.8 | 2.8 | 1 | Bad poster slice next to business two |
| SH062 | 214.5 | 1.6 | 2 | Open carton beneath red kinda bad label |
| SH063 | 216.2 | 4.4 | 2 | Mars respondent appears alone |
| SH064 | 220.6 | 2.0 | 1 | Large smiling globe |
| SH065 | 222.5 | 8.8 | 3 | Globe smaller |
| SH066 | 231.3 | 5.2 | 1 | Reuters rocket revenue excerpt with logo and rocket |
| SH067 | 236.5 | 1.2 | 1 | Host shocked holding cheeks |
| SH068 | 237.7 | 5.4 | 2 | IPO ranking returns |
| SH069 | 243.1 | 6.0 | 2 | Rocket next to solid green revenue circle |
| SH070 | 249.1 | 3.0 | 1 | Full western poster next to business three |
| SH071 | 252.1 | 6.7 | 5 | Good poster slice remains |
| SH072 | 258.8 | 5.8 | 1 | SpaceX sparkle logo on black |
| SH073 | 264.6 | 2.0 | 1 | Starlink logo |
| SH074 | 266.5 | 3.9 | 4 | Host smiles |
| SH075 | 270.4 | 4.0 | 2 | Laughing green-tie buyer gestures |
| SH076 | 274.5 | 3.0 | 6 | Host smiles |
| SH077 | 277.4 | 3.3 | 1 | Beta timeline begins |
| SH078 | 280.8 | 0.7 | 1 | Smiling globe returns |
| SH079 | 281.5 | 6.5 | 1 | Satellite above source headline about ten thousand satellites |
| SH080 | 288.0 | 7.2 | 3 | Three satellites send red arrows toward right |
| SH081 | 295.2 | 1.9 | 1 | Host smiles shrugs |
| SH082 | 297.1 | 4.9 | 2 | Bald bespectacled man's portrait |
| SH083 | 302.0 | 5.2 | 2 | Podcast clip with translucent play triangle |
| SH084 | 307.2 | 10.5 | 1 | Guest clip with explanatory note beneath |
| SH085 | 317.7 | 18.5 | 3 | Podcast angle shifts with note retained |
| SH086 | 336.2 | 5.0 | 3 | Starlink logo alone |
| SH087 | 341.2 | 9.2 | 5 | Revenue headline beneath satellite |
| SH088 | 350.4 | 7.3 | 2 | Host points at green chalkboard question |
| SH089 | 357.8 | 7.8 | 4 | Yahoo Finance article excerpt |
| SH090 | 365.5 | 3.1 | 3 | Large green growth statistic |
| SH091 | 368.6 | 2.7 | 2 | Host smiling hands on hips |
| SH092 | 371.3 | 1.1 | 1 | Upward green arrow with Starlink logo |
| SH093 | 372.5 | 4.2 | 1 | Host sits at laptop behind desk |
| SH094 | 376.7 | 9.0 | 4 | Starlink logo above yacht |
| SH095 | 385.7 | 2.0 | 1 | Cartoon unmasking scene overlaid SpaceX and Starlink logos |
| SH096 | 387.8 | 3.5 | 1 | Money scattering at podium with Starlink face overlay |
| SH097 | 391.2 | 4.0 | 1 | Reuters rocket excerpt returns |
| SH098 | 395.2 | 0.7 | 1 | Mars drawing with SpaceX flag |
| SH099 | 395.9 | 1.7 | 1 | Host smiling arm out |
| SH100 | 397.6 | 4.0 | 13 | Repeated burn headline above money sacks with changing flames |
| SH101 | 401.6 | 5.6 | 4 | Year transition |
| SH102 | 407.2 | 1.9 | 1 | Host neutral hands on hips |
| SH103 | 409.1 | 2.2 | 1 | Party reaction meme with xAI caption |
| SH104 | 411.3 | 10.7 | 5 | Reuters loss excerpt above SpaceX Starlink and rocket |
| SH105 | 422.0 | 3.8 | 2 | Host smiles |
| SH106 | 425.8 | 4.2 | 3 | Defense comparison chart reduced to top left |
| SH107 | 430.0 | 6.7 | 2 | Host enlarged smiles hands on hips |
| SH108 | 436.7 | 1.2 | 1 | IPO rank chart returns |
| SH109 | 437.8 | 3.8 | 2 | Rocket drawing |
| SH110 | 441.6 | 5.6 | 2 | Nasdaq logo and rules scroll |
| SH111 | 447.2 | 1.7 | 1 | Host smiles |
| SH112 | 448.9 | 1.8 | 1 | Large Nasdaq logo |
| SH113 | 450.7 | 1.5 | 1 | Rule title |
| SH114 | 452.1 | 7.2 | 6 | December2025 to March2026 calendar row |
| SH115 | 459.4 | 1.2 | 1 | Host sweats with arms out |
| SH116 | 460.6 | 1.2 | 1 | Rules parchment |
| SH117 | 461.8 | 2.3 | 5 | Musk on red sloped runway |
| SH118 | 464.0 | 1.0 | 1 | Host smiles |
| SH119 | 465.1 | 2.5 | 2 | Host and blank chalkboard yellow progress strip |
| SH120 | 467.5 | 2.8 | 1 | Host holds microphone smiling |
| SH121 | 470.3 | 3.7 | 2 | Host at laptop smiles |
| SH122 | 474.0 | 4.7 | 4 | Laptop screen shows channel banner |
| SH123 | 478.7 | 1.2 | 2 | Oil barrel drawing |
| SH124 | 480.0 | 4.3 | 5 | Host neutral behind laptop |
| SH125 | 484.3 | 2.0 | 3 | Bank of England drawing |
| SH126 | 486.3 | 2.1 | 2 | Debt report agreement papers beside respondent |
| SH127 | 488.5 | 0.4 | 1 | Growth arrow completes |
| SH128 | 488.8 | 0.8 | 1 | Cluttered desk returns |
| SH129 | 489.7 | 1.5 | 2 | Bespectacled host smiles at laptop |
| SH130 | 491.1 | 2.4 | 2 | Close host writes on notepad frowning |
| SH131 | 493.5 | 0.6 | 1 | Wispr chalkboard returns |
| SH132 | 494.1 | 6.0 | 1 | Typing versus Flow speed demo on laptop |
| SH133 | 500.1 | 3.9 | 6 | Wispr wordmark has arms and legs |
| SH134 | 504.0 | 3.0 | 2 | Host at desk with small Wispr and laptop inset |
| SH135 | 507.0 | 1.5 | 1 | Host alone smiling |
| SH136 | 508.5 | 7.6 | 1 | Host laptop below assets versus oil price chart |
| SH137 | 516.0 | 1.3 | 1 | Chart enlarged with red circle on legend |
| SH138 | 517.3 | 6.2 | 1 | Host laptop beside FRED Saudi currency chart |
| SH139 | 523.6 | 1.0 | 1 | FRED chart enlarged with red arrow on peg period |
| SH140 | 524.6 | 9.5 | 1 | Host laptop beneath BIS highlights excerpt |
| SH141 | 534.1 | 10.6 | 4 | Wispr versus Default dictated text comparison |
| SH142 | 544.7 | 1.7 | 2 | Host smiling at laptop |
| SH143 | 546.4 | 8.2 | 3 | Host alone under sponsor strip |
| SH144 | 554.6 | 2.8 | 2 | Host and Wispr character |
| SH145 | 557.4 | 2.9 | 8 | Anthropomorphic SpaceX in fur cape accompanies Musk on red runway |
| SH146 | 560.3 | 5.9 | 2 | Host smiling gestures |
| SH147 | 566.2 | 3.0 | 1 | Buyer wears Nasdaq ribbon smiling |
| SH148 | 569.2 | 5.9 | 2 | Yahoo excerpt with briefcases |
| SH149 | 575.1 | 2.2 | 2 | Eager buyer wears Nasdaq ribbon |
| SH150 | 577.3 | 3.3 | 2 | Nasdaq100 logo alone |
| SH151 | 580.6 | 1.8 | 2 | Neutral buyer holds cash |
| SH152 | 582.4 | 0.8 | 1 | Host smiles |
| SH153 | 583.2 | 2.4 | 1 | Man on cash meme with Nasdaq badge |
| SH154 | 585.5 | 6.9 | 2 | Old rules parchment |
| SH155 | 592.5 | 2.2 | 2 | Host at chalkboard waiting message |
| SH156 | 594.7 | 2.8 | 1 | Curious character studies rising chart |
| SH157 | 597.5 | 8.2 | 5 | Neutral cash buyer |
| SH158 | 605.7 | 1.8 | 1 | Analyst beside growth chart again |
| SH159 | 607.5 | 5.6 | 2 | Three calendar icons |
| SH160 | 613.1 | 0.2 | 1 | Stonks meme between cash buyer and Musk |
| SH161 | 613.2 | 3.5 | 1 | Host smiles shrugs |
| SH162 | 616.8 | 1.1 | 1 | Rules scroll with red revisions |
| SH163 | 617.9 | 12.7 | 7 | Ride-height marker |
| SH164 | 630.6 | 4.5 | 4 | Rules reject SpaceX cartoon |
| SH165 | 635.2 | 2.1 | 2 | Fur-caped SpaceX alone |
| SH166 | 637.3 | 2.2 | 2 | Host and chalkboard teaser |
| SH167 | 639.5 | 1.5 | 1 | Confused-man reaction photograph |
| SH168 | 641.0 | 3.4 | 1 | Revised rules amid surrounding papers |
| SH169 | 644.3 | 1.0 | 1 | Paper framing shifts around rules |
| SH170 | 645.4 | 7.3 | 6 | Gold2x game star |
| SH171 | 652.7 | 7.3 | 4 | Chalkboard4% premise |
| SH172 | 660.0 | 1.8 | 1 | Host shrugs smiling |
| SH173 | 661.8 | 0.9 | 2 | Rules parchment |
| SH174 | 662.7 | 2.4 | 7 | Caped SpaceX and Musk on red runway; small Musk pose differences |
| SH175 | 665.1 | 6.9 | 4 | Numbered rules scroll |
| SH176 | 672.0 | 4.0 | 4 | Old rejection dialogue returns |
| SH177 | 675.9 | 5.5 | 2 | Analyst studies growth chart |
| SH178 | 681.4 | 3.9 | 3 | Nasdaq100 logo |
| SH179 | 685.3 | 8.1 | 3 | Balanced weighing scale |
| SH180 | 693.4 | 2.3 | 2 | Chalkboard demand word |
| SH181 | 695.7 | 1.8 | 2 | Host neutral |
| SH182 | 697.5 | 6.3 | 6 | SpaceX logo alone |
| SH183 | 703.8 | 1.6 | 1 | Host smiles shrugs |
| SH184 | 705.4 | 3.5 | 2 | Rules parchment again |
| SH185 | 708.9 | 3.1 | 2 | Nasdaq100 beside rules |
| SH186 | 712.0 | 3.3 | 1 | SpaceX logo alone |
| SH187 | 715.3 | 1.2 | 1 | SpaceX logo holds |
| SH188 | 716.5 | 5.1 | 3 | Host raises hand |
| SH189 | 721.6 | 3.1 | 2 | Chalkboard retail allocation |
| SH190 | 724.7 | 7.6 | 4 | Usual IPO equation |
| SH191 | 732.2 | 19.2 | 3 | Article excerpt about retail IPO participation |
| SH192 | 751.4 | 1.7 | 1 | Host thinks smiling hand on chin |
| SH193 | 753.1 | 9.4 | 5 | CFO caption alone |
| SH194 | 762.5 | 5.8 | 4 | Frowning host with blank chalkboard |
| SH195 | 768.2 | 1.9 | 5 | Musk alone with small arm and knee pose variations |
| SH196 | 770.2 | 2.0 | 1 | Host frowns arm out |
| SH197 | 772.2 | 3.2 | 2 | Worried black-haired investor holds cash |
| SH198 | 775.4 | 3.2 | 2 | Blindfolded figure above time arrow |
| SH199 | 778.7 | 1.7 | 2 | Four share cartons |
| SH200 | 780.4 | 6.9 | 2 | Fund manager with share carton opposite family |
| SH201 | 787.2 | 4.7 | 2 | Older man's photograph |
| SH202 | 792.0 | 5.3 | 2 | 401k paper alone |
| SH203 | 797.3 | 1.5 | 1 | Time phrase |
| SH204 | 798.8 | 1.5 | 2 | Neutral orange-tie buyer |
| SH205 | 800.4 | 1.5 | 1 | Host frowns arm out |
| SH206 | 801.9 | 4.0 | 2 | SpaceX logo alone |
| SH207 | 805.9 | 0.5 | 1 | Manager and family with 401k return |
| SH208 | 806.4 | 2.2 | 1 | Host smiles gestures |
| SH209 | 808.6 | 4.4 | 5 | Business one carton |
| SH210 | 813.0 | 3.2 | 1 | IPO rank chart returns |
| SH211 | 816.2 | 2.2 | 1 | Worried investor enlarged holding cash |
| SH212 | 818.4 | 2.0 | 2 | Chalkboard demand callback |
| SH213 | 820.5 | 3.5 | 1 | Reader behind newspaper |
| SH214 | 824.0 | 4.6 | 1 | Bored-office reaction meme |
| SH215 | 828.5 | 0.5 | 1 | Sensational valuation headline over newspaper |
| SH216 | 829.0 | 8.8 | 1 | Technical rule headline partially revealed |
| SH217 | 837.8 | 2.6 | 1 | Technical headline breaks into TLDR joke |
| SH218 | 840.4 | 7.0 | 7 | Host smiles |
| SH219 | 847.4 | 3.5 | 3 | Robot beside index-fund infographic |
| SH220 | 850.8 | 3.7 | 3 | Host board lists low fees |
| SH221 | 854.5 | 4.3 | 3 | Sleeping figure in red chair below fee and briefcase |
| SH222 | 858.8 | 3.7 | 2 | Host thinking smiling |
| SH223 | 862.5 | 5.7 | 5 | Black gear-and-flowchart icon |
| SH224 | 868.2 | 2.9 | 2 | Host points toward viewer |
| SH225 | 871.1 | 5.5 | 2 | Sleeping-chair benefits collage returns |
| SH226 | 876.6 | 1.1 | 1 | Worried investor holding cash close-up |
| SH227 | 877.7 | 3.0 | 2 | Nasdaq100 logo |
| SH228 | 880.7 | 1.0 | 1 | Host smiling |
| SH229 | 881.7 | 2.2 | 5 | Musk close-up leaning |
| SH230 | 883.9 | 8.2 | 1 | Final subscribe card and YouTube-only icons |

## Reviewed reconstruction and interpretation

OBSERVED: All572 representative states on48 sheets reviewed across21,410 decoded24fps frames (892.083s video timeline;892.13s container). Hand-drawn black outlines and flat white fields mix with original-looking stick characters, brand logos, red/green marks, photographed sources, memes and an attributed podcast insert. Technique labels are appearance-based inferences, not verified software, licensing or authorship. Motion labels describe reviewed before/after frames plus pixel-change measurements; no easing verification or independent visual QA.

0–43s establishes target valuation with ranked bars and familiar-company comparisons, then swaps scale into a personal retirement-account stake. 55–80s rejects a simple rocket identity through a street-interview gag and a three-business/western roadmap. 82–202s xAI chapter uses transaction excerpt, origin logos, flame loops, founder photo fade, social admission and sequential revenue-multiple chart. 216–250s rocket chapter uses globe/satellite graphics, Reuters revenue excerpt and a quarter pie. 251–421s Starlink chapter uses customer diagrams, subscriber/coverage graphics, an external podcast voice302–336s, revenue highlights and margin comparisons. The source calls margins adjusted EBITDA; narration's profit language remains flagged. The33s ASR sentence388–422s is preserved rather than falsely split into precise spoken clauses.

422–465s returns to the opening question and introduces rule chronology. Sponsor465–557s is distinguished by yellow progress strip, workstation/research metaphors, app icons and split dictation demo. Source data used inside that demonstration is recorded as sponsor context. 557–716s resumes the red-carpet metaphor and explains index assets, shortened seasoning, free-float threshold and multiplier through calendars, ride-height diagram, rule-scroll revisions, arithmetic board and weighing scale. Many rule details lack a readable primary methodology and remain unverified. 718–806s retail allocation uses5–10% versus30%, a source excerpt, CFO portrait and imagined dialogue. The excerpt describes a private meeting with anonymous sources; narration's on-record assertion and ASR name conflict remain in C32. 808–845s recaps all three businesses and critiques easy versus technical headlines;845s subscribe CTA precedes a qualification of passive-investing convenience through robot, benefits board and sleeping-versus-working comparison.883–892s punchline and final subscribe card conclude.

MEASURED audio only: Whole extracted signal processed;2754 ASR words,166 sentences,56 low-probability words,143 ASR word gaps>=0.35s,47 transient onsets under ASR speech. These are not47 confirmed SFX or143 audible silences. Low speech-gap signal median approximately-41.8dBFS does not identify music. Podcast insert's distinct visible speaker is observed; voice character, music identity, SFX identity and human/AI origin UNVERIFIED. Synchronization rows align pixel-derived timestamps to Whisper words with approximate ASR error, not proof of exact intentional timing.

QA: PASS_STRUCTURAL does not mean financial truth or AUDIOVISUAL_QA_FULLY_VERIFIED. Random representative-frame seeks emitted H264 mmco warnings; no independent decode-cleanliness certification. Public metadata is dated evidence; proposed IPO/rule statements are not updated to present-day facts. Mobile thumbnail320/160 inspected. Reconstructed production methods describe general techniques for original drawings and scripts; do not copy artwork or dialogue.
