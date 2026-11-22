# VISUAL RECONSTRUCTION — The World's Safest Market Is Breaking (0ll9rEtoRrs)

_Source: LONG_FORM · 1280×720 @ 24.0 fps · 1012.4s · published 2026-09-01 · SHA256 `8fd0c2bfd7b89d46…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **24298** (every frame). Reviewed shots: **283**; stable states: **577**; motion rows: **574**; micro-changes below threshold (counted, not tabulated): 168.
- Shot length: median **3.0s**, mean 3.6s, p10 0.8s, p90 7.0s → **16.8 shots/min**.
- Visual-state length: median **1.04s**, mean 1.44s → **34.2 states/min** (a new composition state roughly every 1.8s incl. transitions).
- Time in transitions/animation (frames between stable states): **182s (18%)**; stable states **830s (82%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): MOTION_GRAPHICS 100%; ORIGINAL_DRAWING 53%; SCREEN_CAPTURE 46%; STOCK_FOOTAGE 1%. Shots made only of drawn assets + text motion: 53% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 259, POP_IN 114, TEXT_REVEAL 44, BUILD 22, ZOOM_IN 16, SWAP 15, FACE_CHANGE 15, HIGHLIGHT 15, REFRAME 14, POSE_CHANGE 11, TEXT_SWAP 11, SCROLL 8, STRIKE 6, HOLD 4.
- Narration pace: **196 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 427, DURING_WORD 349, BEFORE_WORD 61, AFTER_WORD 18, IN_PAUSE 2.
- Shot-start offset vs nearest word start: median **42 ms** (p10 -58, p90 291); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 108 of 243 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| HOST | CHARACTER_HOST | 271.17 | 98 | ORIGINAL_DRAWING |
| HL_YELLOW | ANNOTATION_OVERLAY | 164.17 | 29 | MOTION_GRAPHICS |
| POINTER | PROP | 122.59 | 30 | ORIGINAL_DRAWING |
| MAP_USA | CHARACTER_MAP | 58.42 | 23 | ORIGINAL_DRAWING |
| OBJ_BONDS | OBJECT | 58.38 | 30 | ORIGINAL_DRAWING |
| OBJ_BAG | OBJECT | 55.92 | 29 | ORIGINAL_DRAWING |
| OBJ_DEBT | OBJECT | 54.59 | 21 | ORIGINAL_DRAWING |
| OBJ_LAPTOP | OBJECT | 46.67 | 17 | ORIGINAL_DRAWING |
| OBJ_BUBBLE | OBJECT | 46.54 | 24 | ORIGINAL_DRAWING |
| MAP_UK | CHARACTER_MAP | 46.21 | 13 | ORIGINAL_DRAWING |
| OBJ_CHECK | OBJECT | 45.29 | 18 | ORIGINAL_DRAWING |
| CHAR_DWIGHT | CHARACTER | 44.09 | 19 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 4 | 2 | 3 | 228 | 0 | 2 |
| 5-15s (5-15s) | 10 | 4 | 11 | 162 | 3 | 2 |
| 15-30s (15-30s) | 7 | 2 | 6 | 164 | 5 | 0 |
| 30-60s (30-60s) | 20 | 8 | 21 | 186 | 3 | 5 |
| 60s-midpoint (60-506s) | 272 | 129 | 272 | 199 | 36 | 84 |
| midpoint-last60s (506-952s) | 228 | 113 | 225 | 194 | 38 | 68 |
| last 60s (952-1012s) | 36 | 25 | 36 | 180 | 1 | 16 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Small green Treasury paper on white [S001.1 @3.2s] Treasury paper surrounded by bond cards, calendar, host, globe and newspaper reader [S001.2 @3.5s] Second calendar added to collage [S002.0 @3.9s] Three stick observers peek in from left

Closing frames: [S135.1 @1000.7s] Reader face becomes worried [S135.2 @1002.0s] Dark red-eyed monster behind worried reader [S136.0 @1003.7s] Drawn endcard with empty circle rectangle and supporter heading


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 3.9 | 3 | Small green Treasury paper on white |
| SH002 | 3.9 | 4.3 | 4 | Three stick observers peek in from left |
| SH003 | 8.2 | 2.8 | 4 | Treasury seal alone |
| SH004 | 11.0 | 2.2 | 1 | Smiling host hands on hips |
| SH005 | 13.3 | 0.8 | 1 | Green USA map reads blue US-flag book |
| SH006 | 14.1 | 3.6 | 1 | Open heart bond locket |
| SH007 | 17.7 | 0.4 | 1 | USA map below left of bond heart |
| SH008 | 18.1 | 15.7 | 7 | Red calendar alone |
| SH009 | 33.8 | 3.3 | 3 | USA and Germany green maps |
| SH010 | 37.1 | 3.9 | 3 | Stick figure reads newspaper |
| SH011 | 41.0 | 1.4 | 1 | Animated film character in glasses beside TV |
| SH012 | 42.4 | 1.7 | 1 | Close-up film character |
| SH013 | 44.0 | 2.6 | 2 | Host with pointer beside blank chalkboard |
| SH014 | 46.7 | 2.8 | 5 | Smiling USA map alone |
| SH015 | 49.5 | 2.1 | 1 | Grinning tie figure holding green notes |
| SH016 | 51.6 | 12.8 | 5 | Host with palms up |
| SH017 | 64.4 | 2.0 | 1 | Host wearing detective cap holding magnifier |
| SH018 | 66.4 | 3.5 | 3 | Six country map characters on white |
| SH019 | 69.9 | 4.1 | 2 | Detective host with magnifier enlarged |
| SH020 | 74.0 | 3.3 | 3 | Small question disk alone |
| SH021 | 77.2 | 3.2 | 1 | Ponytailed detective with magnifier and question disk |
| SH022 | 80.5 | 0.8 | 1 | Glasses figure with headband beside cropped decade arrow |
| SH023 | 81.3 | 1.1 | 1 | Host with doubtful mouth |
| SH024 | 82.4 | 1.4 | 1 | Red fictional paper-company logo |
| SH025 | 83.8 | 2.5 | 1 | Embedded cartoon workplace scene |
| SH026 | 86.4 | 0.6 | 1 | Cartoon employee portrait wall |
| SH027 | 87.0 | 3.0 | 3 | Glasses tie character labeled Dwight with arrow |
| SH028 | 90.0 | 3.5 | 2 | Farmer Dwight in straw hat holding beets in field |
| SH029 | 93.5 | 3.2 | 3 | Paper-company logo alone |
| SH030 | 96.8 | 0.5 | 1 | Intertitle on white |
| SH031 | 97.2 | 4.1 | 3 | Older Dwight leaning on cane |
| SH032 | 101.4 | 1.7 | 2 | Six money bags above calendar row |
| SH033 | 103.0 | 0.5 | 1 | Host with pointer |
| SH034 | 103.5 | 0.9 | 1 | Host points at blue pension definition card |
| SH035 | 104.4 | 4.3 | 3 | Dwight alone |
| SH036 | 108.7 | 0.7 | 1 | Host close-up pointing toward viewer |
| SH037 | 109.4 | 2.2 | 3 | Company logo alone |
| SH038 | 111.6 | 1.7 | 1 | Many bill sheets fill frame |
| SH039 | 113.3 | 4.5 | 8 | Older employee with cane small on white |
| SH040 | 117.8 | 4.9 | 2 | Host with one hand raised |
| SH041 | 122.7 | 0.7 | 1 | Pile of overlapping bills |
| SH042 | 123.4 | 5.3 | 4 | Dwight gives thumbs-up |
| SH043 | 128.8 | 1.1 | 2 | Company logo enlarged |
| SH044 | 129.8 | 2.7 | 3 | Farmer employee with beets |
| SH045 | 132.5 | 7.0 | 2 | Large pension check |
| SH046 | 139.6 | 2.8 | 2 | Single check beside money bag |
| SH047 | 142.4 | 1.9 | 2 | Frowning host with raised hand |
| SH048 | 144.2 | 1.7 | 1 | Pension check alone |
| SH049 | 146.0 | 1.8 | 1 | Green rising line above red time axis with stock meme |
| SH050 | 147.8 | 4.6 | 5 | Rising line extended upward |
| SH051 | 152.4 | 2.4 | 1 | Tiny red-tie figure falling under large grey edge |
| SH052 | 154.8 | 0.8 | 1 | Company logo and money bag |
| SH053 | 155.7 | 0.7 | 1 | Employee beside bag and company |
| SH054 | 156.3 | 1.2 | 1 | Pension check equals promise note |
| SH055 | 157.5 | 1.5 | 1 | Two economic collapse meme stills |
| SH056 | 159.1 | 2.2 | 3 | Check and large money bag |
| SH057 | 161.3 | 3.2 | 1 | Host with uncertain face |
| SH058 | 164.5 | 5.7 | 3 | Money bag alone |
| SH059 | 170.1 | 5.3 | 1 | US 30-year yield chart fills frame |
| SH060 | 175.4 | 3.6 | 3 | Host palms up |
| SH061 | 179.0 | 2.6 | 3 | Blue liability-driven investment definition |
| SH062 | 181.6 | 3.3 | 1 | Yield decomposition formula above two puzzled figures |
| SH063 | 184.9 | 1.6 | 1 | Bowtie figure with red questions beside bond |
| SH064 | 186.5 | 3.7 | 2 | Anthropomorphic Federal Reserve building with reassurance bubble |
| SH065 | 190.1 | 2.1 | 1 | Smiling host palms up |
| SH066 | 192.2 | 3.0 | 4 | Bond alone |
| SH067 | 195.3 | 1.3 | 2 | Host points at viewer close-up |
| SH068 | 196.6 | 1.8 | 2 | Bond certificate alone |
| SH069 | 198.3 | 5.5 | 2 | Employee with eyes shut and hand raised |
| SH070 | 203.9 | 1.2 | 2 | Red timeline bond at start bag at end notes underneath |
| SH071 | 205.1 | 2.0 | 1 | Uncertain host hand raised |
| SH072 | 207.0 | 6.5 | 1 | Clock money-bag pile and law sheet |
| SH073 | 213.6 | 2.0 | 1 | Host peeks below clock money and law |
| SH074 | 215.6 | 4.1 | 4 | Pension definition card |
| SH075 | 219.7 | 2.2 | 1 | Defined contribution and benefit participant chart |
| SH076 | 222.0 | 1.6 | 1 | Participant chart held at slightly different crop |
| SH077 | 223.5 | 1.7 | 1 | Detective host beside question disk |
| SH078 | 225.2 | 2.2 | 2 | Bond and Treasury stack over question |
| SH079 | 227.5 | 0.5 | 1 | Detective host alone |
| SH080 | 228.0 | 1.4 | 1 | Laptop video player shows host with pause overlay |
| SH081 | 229.4 | 1.5 | 1 | Laptop player with play triangle |
| SH082 | 231.0 | 1.7 | 1 | Host seated at desk behind CF laptop |
| SH083 | 232.6 | 2.4 | 1 | Laptop text page with pointing hand |
| SH084 | 235.0 | 2.2 | 1 | Clock beside words-per-minute label |
| SH085 | 237.3 | 0.7 | 1 | Angry host at CF laptop |
| SH086 | 238.0 | 6.9 | 1 | Pink Turbo Type screen with small car |
| SH087 | 244.9 | 2.1 | 3 | Host talking palms open |
| SH088 | 247.0 | 2.3 | 3 | Angry host at laptop again |
| SH089 | 249.4 | 3.4 | 2 | Host with pointer beside blank board |
| SH090 | 252.8 | 5.8 | 3 | Glasses host at laptop, sponsor figure and desk behind |
| SH091 | 258.6 | 7.2 | 4 | Side-by-side email demo sponsor and typing |
| SH092 | 265.9 | 4.9 | 4 | Host at laptop with misheard-letter balloon |
| SH093 | 270.8 | 8.1 | 4 | Sponsor versus built-in voice text demo |
| SH094 | 278.8 | 3.5 | 2 | Host praises sponsor figure |
| SH095 | 282.4 | 1.6 | 3 | Host surrounded by AI and messaging icons |
| SH096 | 284.0 | 9.1 | 5 | Small host with hand raised |
| SH097 | 293.0 | 3.5 | 2 | Host beside sponsor figure |
| SH098 | 296.5 | 2.8 | 2 | Debt stack above question disk |
| SH099 | 299.3 | 13.0 | 9 | BLS pension participation PDF in dark viewer |
| SH100 | 312.3 | 2.3 | 3 | BLS benefits PDF in viewer with bar charts |
| SH101 | 314.7 | 1.6 | 1 | Frowning host one hand raised |
| SH102 | 316.3 | 6.4 | 4 | Big Business building beside pension check |
| SH103 | 322.7 | 2.8 | 1 | Smiling host palms open |
| SH104 | 325.5 | 0.6 | 1 | Text intertitle with red negation |
| SH105 | 326.0 | 4.6 | 1 | Pension check enlarged |
| SH106 | 330.7 | 1.4 | 2 | Retirement timeline checks and bags |
| SH107 | 332.1 | 3.5 | 2 | Blue 401k definition card |
| SH108 | 335.5 | 4.1 | 4 | Pink piggy bank |
| SH109 | 339.7 | 2.8 | 2 | Employee enlarged beside Treasury paper |
| SH110 | 342.5 | 11.1 | 6 | 401k asset-allocation bar chart |
| SH111 | 353.6 | 2.5 | 2 | Host alone palms out |
| SH112 | 356.1 | 1.6 | 2 | Bond card large |
| SH113 | 357.8 | 3.2 | 2 | Bob-haired caller with purple tie and phone |
| SH114 | 361.0 | 2.6 | 1 | OECD logo and partial expansion |
| SH115 | 363.6 | 3.3 | 5 | World map OECD members gold |
| SH116 | 366.9 | 1.5 | 1 | Marvel Avengers wordmark |
| SH117 | 368.5 | 1.7 | 1 | USA with shield beside superhero-styled Europe map |
| SH118 | 370.1 | 8.3 | 1 | Highlighted OECD debt-report paragraph with check bag and logo |
| SH119 | 378.4 | 3.1 | 2 | Federal Reserve minutes web page |
| SH120 | 381.5 | 13.1 | 1 | Highlighted minutes passage beside pointing host |
| SH121 | 394.6 | 2.7 | 1 | Host with sweat drop |
| SH122 | 397.3 | 1.2 | 2 | Company logo beside bond and downward curved arrow |
| SH123 | 398.6 | 5.4 | 2 | Pensive employee hand to cheek |
| SH124 | 404.0 | 4.2 | 1 | Thirty-year bond-payment timeline |
| SH125 | 408.2 | 2.6 | 2 | UK map alone |
| SH126 | 410.8 | 4.3 | 3 | UK map enlarged |
| SH127 | 415.0 | 10.5 | 1 | OBR excerpt with highlighted future holdings |
| SH128 | 425.6 | 2.1 | 2 | Frowning host hand raised |
| SH129 | 427.7 | 10.9 | 1 | OBR chart excerpt beside pointing host |
| SH130 | 438.6 | 1.7 | 1 | USA map face close-up |
| SH131 | 440.3 | 3.2 | 3 | UK map with teacup |
| SH132 | 443.5 | 6.7 | 3 | Dutch flag beside pension-assets table |
| SH133 | 450.2 | 2.1 | 2 | Netherlands row red-boxed |
| SH134 | 452.3 | 7.4 | 1 | Dutch parliamentary excerpt highlighted first line |
| SH135 | 459.7 | 1.0 | 1 | Second line highlighted |
| SH136 | 460.7 | 5.6 | 2 | Defined-benefit heading over employer pension and Treasury paper |
| SH137 | 466.2 | 4.6 | 4 | Netherlands map beside Dutch flag |
| SH138 | 470.9 | 1.2 | 1 | Bond-matched retirement timeline repeated |
| SH139 | 472.1 | 6.5 | 6 | Dutch foreign-government-bond holdings bars |
| SH140 | 478.6 | 5.5 | 2 | Purple-tie woman beside Netherlands map |
| SH141 | 484.1 | 2.8 | 2 | Highlighted pension ownership excerpt above Germany and Netherlands |
| SH142 | 486.9 | 3.1 | 2 | Host beside chalkboard |
| SH143 | 490.0 | 8.1 | 2 | IPE paragraph on reducing holdings |
| SH144 | 498.0 | 2.3 | 2 | Large blue wave with white foam |
| SH145 | 500.4 | 9.9 | 5 | ING excerpt on ABP transition |
| SH146 | 510.2 | 4.7 | 1 | Dutch reform headline excerpt above map |
| SH147 | 514.9 | 6.2 | 4 | Bond alone |
| SH148 | 521.1 | 2.4 | 2 | Host with pointer |
| SH149 | 523.5 | 1.4 | 1 | Host palms open |
| SH150 | 524.9 | 3.0 | 3 | Debt paper alone |
| SH151 | 527.9 | 5.6 | 3 | Host points at Dutch holdings chart |
| SH152 | 533.5 | 9.6 | 4 | PIMCO hedging scenario table with base circled |
| SH153 | 543.1 | 0.8 | 1 | Host one hand raised |
| SH154 | 543.8 | 3.5 | 6 | Debt stack left and single debt paper right |
| SH155 | 547.3 | 4.2 | 4 | Old and New headings over single papers |
| SH156 | 551.5 | 2.7 | 1 | Long bond low left short bond upper right around rate disk |
| SH157 | 554.2 | 8.4 | 2 | Nomura slide in laptop |
| SH158 | 562.6 | 3.3 | 1 | Country cast beneath yield strip |
| SH159 | 566.0 | 6.4 | 3 | Glasses bald lender with briefcase beside Japan |
| SH160 | 572.4 | 0.7 | 1 | Pension participant chart again |
| SH161 | 573.1 | 3.0 | 2 | US Treasury auction-yield chart with lender |
| SH162 | 576.0 | 1.6 | 2 | Pensive Dwight close-up |
| SH163 | 577.6 | 3.6 | 1 | Doubtful host with raised hand |
| SH164 | 581.2 | 4.5 | 5 | Lender with case and note beside debt paper |
| SH165 | 585.8 | 2.5 | 1 | Bond beside woman at CF laptop |
| SH166 | 588.2 | 0.4 | 1 | US yield chart alone |
| SH167 | 588.6 | 0.4 | 1 | German yield chart alone |
| SH168 | 589.0 | 0.4 | 1 | UK yield chart alone |
| SH169 | 589.5 | 0.5 | 1 | France quote alone |
| SH170 | 589.9 | 0.5 | 1 | Canada quote alone |
| SH171 | 590.5 | 3.5 | 2 | Japan multi-maturity chart alone |
| SH172 | 593.9 | 0.7 | 1 | Intertitle with eyes below |
| SH173 | 594.6 | 1.1 | 1 | UK flag beside UK map |
| SH174 | 595.7 | 7.2 | 2 | Issuance maturity chart with long category circled |
| SH175 | 602.9 | 9.3 | 1 | HM Treasury demand excerpt with highlighted pension demand |
| SH176 | 612.2 | 7.1 | 2 | Host palms open |
| SH177 | 619.3 | 10.5 | 5 | Japan Reuters excerpt highlighted |
| SH178 | 629.8 | 1.3 | 1 | USA map holding Treasury paper |
| SH179 | 631.1 | 3.6 | 1 | Office of Debt Management hypothetical financing excerpt |
| SH180 | 634.8 | 3.2 | 1 | Treasury T-bill advisory slide |
| SH181 | 637.9 | 2.4 | 1 | Same T-bill slide held |
| SH182 | 640.3 | 11.2 | 4 | OECD borrowing composition figure |
| SH183 | 651.6 | 4.1 | 1 | OECD debt-report bullet list highlighted |
| SH184 | 655.7 | 0.3 | 1 | Highlighted OECD paragraph held |
| SH185 | 656.0 | 1.8 | 1 | Host at laptop beside dictionary page |
| SH186 | 657.8 | 2.8 | 2 | Host beside borrowing composition chart |
| SH187 | 660.6 | 4.8 | 5 | Two Treasury papers |
| SH188 | 665.4 | 5.1 | 5 | Worried USA map beside debt |
| SH189 | 670.5 | 2.0 | 1 | USA close-up wearing pixel sunglasses |
| SH190 | 672.5 | 0.7 | 1 | Host palms open |
| SH191 | 673.2 | 1.9 | 2 | USA dialogue beside debt |
| SH192 | 675.0 | 3.8 | 2 | Debt sheet enlarged |
| SH193 | 678.8 | 4.5 | 1 | USA between debt sheets with money bag |
| SH194 | 683.2 | 3.4 | 2 | Host one hand raised |
| SH195 | 686.7 | 2.3 | 1 | Rollover-risk definition card beside pointing host |
| SH196 | 689.0 | 3.0 | 5 | Bond under 30-year label |
| SH197 | 692.0 | 4.4 | 6 | USA beside large debt sheet |
| SH198 | 696.3 | 3.2 | 1 | Host palms open |
| SH199 | 699.5 | 3.4 | 2 | Treasury average-rate bar chart |
| SH200 | 702.9 | 4.4 | 2 | OECD yields and maturity multi-panel figure |
| SH201 | 707.3 | 5.0 | 2 | Pensive bald tie figure beside average-rate chart |
| SH202 | 712.2 | 6.7 | 1 | CNBC Treasury yield table with 1-year and 30-year rows boxed |
| SH203 | 718.9 | 2.8 | 2 | US debt composition excerpt with three debt sheets |
| SH204 | 721.8 | 5.5 | 4 | Host beside debt paper and note |
| SH205 | 727.2 | 9.5 | 4 | Historical Treasury average-rate lines with arrow at early low point |
| SH206 | 736.8 | 1.1 | 1 | Host palms open |
| SH207 | 737.8 | 1.0 | 1 | Drawn purple villain with gold jeweled glove |
| SH208 | 738.8 | 4.0 | 1 | FRED interest-expenditure line chart beside host |
| SH209 | 742.8 | 10.2 | 2 | Peterson spending comparison excerpt highlighted |
| SH210 | 752.9 | 2.5 | 2 | Blue net interest projection area chart |
| SH211 | 755.4 | 3.8 | 1 | Country cast around office reaction still |
| SH212 | 759.2 | 11.6 | 7 | Host at laptop beside OECD report cover |
| SH213 | 770.9 | 2.1 | 1 | Detective host smiling with magnifier |
| SH214 | 773.0 | 7.0 | 2 | OECD borrowing outlook excerpt highlighted |
| SH215 | 779.9 | 1.8 | 2 | USA map beside green phrase |
| SH216 | 781.7 | 2.4 | 1 | Debt paper with grey beard |
| SH217 | 784.0 | 9.5 | 2 | Refinancing excerpt returns highlighted |
| SH218 | 793.6 | 1.6 | 2 | Host pointer beside blank chalkboard |
| SH219 | 795.2 | 4.4 | 3 | Three staggered debt sheets |
| SH220 | 799.6 | 2.0 | 1 | Doubtful host raised hand |
| SH221 | 801.6 | 6.7 | 1 | Treasury historical average-rate chart |
| SH222 | 808.3 | 5.5 | 1 | OECD 2025 paragraph with debt sheets and highlighted vintage |
| SH223 | 813.8 | 7.2 | 2 | OECD yield-at-issuance and maturity figure |
| SH224 | 821.0 | 3.9 | 1 | Host points to OECD paragraph first sentence |
| SH225 | 824.9 | 3.4 | 3 | Same highlighted paragraph held |
| SH226 | 828.2 | 4.2 | 1 | Frowning host |
| SH227 | 832.5 | 5.3 | 1 | OECD debt-stock excerpt and two bonds |
| SH228 | 837.8 | 5.1 | 1 | Hyperscaler issuance charts |
| SH229 | 843.0 | 5.5 | 5 | Blue box around total amount issued panel |
| SH230 | 848.5 | 8.2 | 5 | Hyperscaler capex and issuance projection |
| SH231 | 856.8 | 6.8 | 1 | OECD capex paragraph with factory and robot |
| SH232 | 863.5 | 2.8 | 1 | Blue key-facts infographic |
| SH233 | 866.3 | 6.8 | 3 | Bond issuance panel cropped alone |
| SH234 | 873.1 | 4.6 | 2 | Long-term issuance share infographic |
| SH235 | 877.7 | 1.9 | 1 | Globe beside debt maturity multi-panel figure |
| SH236 | 879.5 | 2.7 | 1 | Capex projection figure again |
| SH237 | 882.2 | 6.8 | 5 | Hyperscaler issuance figure again |
| SH238 | 889.0 | 2.5 | 1 | Doubtful host raised hand |
| SH239 | 891.5 | 1.3 | 1 | Host at chalkboard with closing question |
| SH240 | 892.8 | 4.0 | 2 | USA map reading red economics book |
| SH241 | 896.8 | 1.2 | 2 | Paper-company logo with paper stacks and borrowing panel |
| SH242 | 898.0 | 5.4 | 1 | Country cast with two yield charts above |
| SH243 | 903.4 | 1.6 | 1 | Full yield strip above country cast |
| SH244 | 905.0 | 5.8 | 3 | OECD borrowing composition figure |
| SH245 | 910.8 | 5.2 | 3 | FRED money-market asset chart above reclining USA and money bags |
| SH246 | 916.0 | 1.9 | 1 | Globe face close-up |
| SH247 | 917.9 | 1.8 | 1 | Orange-haired figure holding wallet |
| SH248 | 919.8 | 0.8 | 1 | Globe surrounded by money bags |
| SH249 | 920.6 | 5.6 | 2 | Host palms open |
| SH250 | 926.2 | 5.4 | 3 | Thirty- and five-year bond comparison |
| SH251 | 931.6 | 1.8 | 1 | Host palms open |
| SH252 | 933.5 | 1.0 | 1 | Debt paper with live-action return clip inside balloon |
| SH253 | 934.5 | 6.0 | 1 | OECD maturity excerpt with debt sheets |
| SH254 | 940.5 | 1.2 | 1 | Excerpt emphasis extends through refinancing sentence |
| SH255 | 941.7 | 1.2 | 1 | Frowning host hand raised |
| SH256 | 942.8 | 5.7 | 2 | Debt-stock maturity figure |
| SH257 | 948.5 | 3.2 | 1 | Host palms open |
| SH258 | 951.7 | 1.1 | 2 | Bond cashflow timeline |
| SH259 | 952.8 | 3.7 | 1 | Crash meme below dramatic-event phrase |
| SH260 | 956.5 | 1.3 | 2 | Large cyan bubble |
| SH261 | 957.8 | 1.0 | 2 | Newspaper reader close-up |
| SH262 | 958.8 | 4.0 | 3 | Folded newspaper |
| SH263 | 962.8 | 2.3 | 2 | Orange-tie figure at desktop computer |
| SH264 | 965.1 | 3.9 | 1 | Host puzzled beside CF laptop |
| SH265 | 969.0 | 3.1 | 1 | Globe resting on green turtle |
| SH266 | 972.0 | 1.9 | 1 | Detective host with magnifier |
| SH267 | 973.9 | 0.3 | 1 | OECD yield and maturity figure |
| SH268 | 974.2 | 0.6 | 1 | Full blue OECD facts infographic |
| SH269 | 974.9 | 0.4 | 1 | OECD borrowing outlook paragraph |
| SH270 | 975.2 | 0.7 | 1 | OECD debt-stock maturity figure |
| SH271 | 976.0 | 0.6 | 1 | Hyperscaler corporate issuance figure |
| SH272 | 976.5 | 0.6 | 1 | Hyperscaler capex paragraph excerpt |
| SH273 | 977.2 | 0.5 | 1 | Hyperscaler capex projection figure |
| SH274 | 977.7 | 3.2 | 2 | Host beside corkboard red strings and pinned notes |
| SH275 | 980.9 | 1.8 | 1 | Smiling host close-up arms raised |
| SH276 | 982.7 | 3.5 | 4 | Laptop shows channel homepage subscribe banner |
| SH277 | 986.2 | 3.2 | 1 | Host hands on hips |
| SH278 | 989.5 | 2.3 | 1 | Country cast under one yield chart |
| SH279 | 991.8 | 3.8 | 1 | Full chart strip above country cast |
| SH280 | 995.6 | 0.8 | 1 | Heart locket containing market imagery |
| SH281 | 996.4 | 2.5 | 1 | Globe face close-up |
| SH282 | 999.0 | 4.7 | 3 | Reader with newspaper |
| SH283 | 1003.7 | 8.8 | 1 | Drawn endcard with empty circle rectangle and supporter heading |

## Reviewer interpretation and evidence limits

All 577 state representatives reviewed on 49 contact sheets through endcard; before/after wording describes those frames, not direct playback of every animation. Pixel-diff events support timing and region, not easing or exact software. H264 seeking emitted `mmco: unref short failure` warnings; frame staging finished with 24,298 frames. Decoded video duration 1012.417s differs from container duration 1012.525s by 0.108s (audio/container tail); retain both. No source modification.

Illustration: irregular heavy black contours, peach faces, thin stick limbs, green anthropomorphic countries, restrained white backgrounds and red emphasis. The pension analogy 81–227s builds cashflow symbols and recurring employee poses before showing documentary sources 299–394s. Evidence alternates with plain diagrams, source crops, highlights and short reaction gags. Asset reuse and labels are appearance-based observations; hand-drawn software/workflow is not verified.

Motion: successive card/symbol appearances, framing changes, face/pose swaps, scrolling PDFs, line highlights and chart close-ups. Reviewed states do not prove smooth interpolation or ease curves. Long-form explanation adds several states inside one composition; distinguish visual-state frequency from cuts.

Audio: entire soundtrack signal-analysed and both spectrogram sheets viewed. Speech-like harmonic/broadband structure follows ASR spans, with a quieter tail after the last words near 1003s. No music identity, music event, SFX or vocal timbre is certified by listening. 29 strong onsets were classified under ASR speech; this does not prove absence of SFX.

Script: global-news mismatch → Germany counterexample → missing-buyer promise → fictional pension analogy → disclosed sponsor 228–295s → US/UK/Dutch documentary examples → duration and issuance shift → rollover repricing → AI-capex escalation → patient-capital thesis → subscribe request 986–990s and opening callback. Beats are reviewer interpretation on unverified ASR.

Targeted numerical QA preserves BLS denominator changes, OBR narration 27% versus visible 28.7%, ABP 500B rounding versus €530bn excerpt, Japan completed-action wording versus Reuters forecast, average-versus-spot yield dates, gross/net interest scope, and refinancing requirements versus borrowing-cost wording. Structural QA is not audiovisual correctness certification.
