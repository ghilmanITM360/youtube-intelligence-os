# VISUAL RECONSTRUCTION — The New American Housing Crisis Has Landed (Uumnx2Fo6cE)

_Source: LONG_FORM · 1280×720 @ 24.0 fps · 920.7s · published 2026-09-29 · SHA256 `a57768bd5a32a8b0…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **22097** (every frame). Reviewed shots: **120**; stable states: **567**; motion rows: **565**; micro-changes below threshold (counted, not tabulated): 110.
- Shot length: median **6.6s**, mean 7.7s, p10 2.3s, p90 13.7s → **7.8 shots/min**.
- Visual-state length: median **1.08s**, mean 1.37s → **36.9 states/min** (a new composition state roughly every 1.6s incl. transitions).
- Time in transitions/animation (frames between stable states): **141s (15%)**; stable states **780s (85%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 93%; SCREEN_CAPTURE 69%; MOTION_GRAPHICS 12%; COMPOSITED_STILLS 7%. Shots made only of drawn assets + text motion: 27% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 216, POP_IN 128, HIGHLIGHT 30, ZOOM_IN 25, REPOSITION 23, TEXT_REVEAL 20, SCROLL 16, LOOP_ANIM 15, DRAW_ON 14, EXIT 13, FACE_CHANGE 10, SLIDE 9, SWAP 9, SLIDE_IN 6.
- Narration pace: **199 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 302, DURING_WORD 272, BEFORE_WORD 89, AFTER_WORD 21, IN_PAUSE 1.
- Shot-start offset vs nearest word start: median **-15 ms** (p10 -103, p90 274); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 95 of 218 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| HOST | CHARACTER_HOST | 317.46 | 71 | ORIGINAL_DRAWING |
| POINTER | PROP | 155.96 | 34 | ORIGINAL_DRAWING |
| HL_TEXT_MARKER_YELLOW | ANNOTATION_OVERLAY | 107.16 | 21 | MOTION_GRAPHICS |
| UI_YELLOW_PROGRESS_BAR | UI_OVERLAY | 69.42 | 7 | MOTION_GRAPHICS |
| TXT_HANDLETTER | TEXT_LETTERING | 54.91 | 23 | MOTION_GRAPHICS |
| LOGO_GROUNDNEWS_QR | LOGO | 50.58 | 6 | COMPOSITED_STILLS |
| HL_TEXT_MARKER_GREEN | ANNOTATION_OVERLAY | 47.21 | 8 | MOTION_GRAPHICS |
| HL_TEXT_MARKER_ORANGE | ANNOTATION_OVERLAY | 43.71 | 16 | MOTION_GRAPHICS |
| OBJ_HOUSE_ICONS | OBJECT | 36.79 | 10 | ORIGINAL_DRAWING |
| SS_FHFA_WP_LOCKIN | SCREENSHOT | 34.08 | 1 | SCREEN_CAPTURE |
| OBJ_BIG_HOUSE | OBJECT | 33.12 | 16 | ORIGINAL_DRAWING |
| OBJ_GREY_TOWER | OBJECT | 27.09 | 9 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 6 | 1 | 5 | 228 | 1 | 1 |
| 5-15s (5-15s) | 5 | 1 | 6 | 204 | 0 | 1 |
| 15-30s (15-30s) | 9 | 4 | 8 | 184 | 1 | 2 |
| 30-60s (30-60s) | 25 | 10 | 26 | 200 | 7 | 7 |
| 60s-midpoint (60-460s) | 247 | 54 | 246 | 200 | 37 | 42 |
| midpoint-last60s (460-861s) | 246 | 45 | 245 | 198 | 36 | 29 |
| last 60s (861-921s) | 29 | 5 | 29 | 177 | 3 | 3 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Blank white canvas; smiling host (round peach head, spiky black hair) at right third holding a pointer across his body [S001.1 @0.5s] Redfin News article page appears behind host: headline 'It's Now The Strongest Buyer's Market on Record, Driven by the Sun Belt' with bullets; host po [S001.2 @1.9s] Page zoomed down to the chart 'Surplus of Sellers Over Buyers Hits Record High'; red hand-lettered '58%' top right; host pointing at the line's end [S001.3 @2.4s] Chart shifted lower-left, '58%' re-positioned; same host pose

Closing frames: [S141.1 @911.3s] Page shifts to the left; a surprised curly dark-haired figure with a phone and banknote enters at lower right [S141.2 @912.2s] Banknotes rain down over the page and a top-hatted monocled moustached rich-man figure enters at lower left [S142.0 @914.4s] Final 6.3 s end card on white: an empty circle with 'Subscribe for more Casual Finance' at top left, an empty rectangle below (pla


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 13.7 | 10 | Hook: Redfin record seller surplus (58%) |
| SH002 | 13.7 | 2.5 | 1 | Host reset |
| SH003 | 16.2 | 0.8 | 1 | House for sale; buyer gleeful |
| SH004 | 16.9 | 3.0 | 3 | Sellers vs buyers: many sellers, few buyers |
| SH005 | 20.0 | 0.8 | 2 | Host reaction |
| SH006 | 20.8 | 9.6 | 3 | Evidence: NAR existing-home sales (August) |
| SH007 | 30.3 | 4.4 | 2 | Callback: Redfin chart vs NAR price |
| SH008 | 34.8 | 3.5 | 3 | Chalk board becomes a held sign: REASONS |
| SH009 | 38.3 | 4.9 | 2 | Evidence: investor home purchases fall to lowest level since 2020 (Redfin) |
| SH010 | 43.2 | 2.4 | 2 | Evidence: housing deficit 4.7M homes (Zillow) |
| SH011 | 45.6 | 2.0 | 4 | Dollar signs accumulate (money) |
| SH012 | 47.6 | 5.0 | 4 | Evidence: number of sellers jumps to a 6-year high |
| SH013 | 52.5 | 2.2 | 2 | Chalkboard: Still NOT cheap |
| SH014 | 54.8 | 1.4 | 4 | Mortgage rates near 7%: headline stack |
| SH015 | 56.2 | 3.1 | 1 | In theory: higher rates should cut prices |
| SH016 | 59.3 | 2.3 | 2 | Iceberg metaphor: hidden risk below the surface |
| SH017 | 61.6 | 4.0 | 2 | Tiny crooked houses: supply |
| SH018 | 65.7 | 10.3 | 4 | Homeowners with locked-in low rates ('your mum') |
| SH019 | 76.0 | 1.7 | 3 | Debt due dates pile up |
| SH020 | 77.7 | 1.2 | 2 | The bank: where's my money? |
| SH021 | 78.9 | 5.1 | 3 | Homeowner characters: house + owner |
| SH022 | 84.0 | 5.2 | 5 | Mid-roll channel plug: 'watch the other video' |
| SH023 | 89.2 | 7.0 | 2 | Evidence: Fed Monetary Policy Report, July 2026 — 'rate lock' |
| SH024 | 96.1 | 3.7 | 2 | Evidence: FRED 30-year mortgage rate chart |
| SH025 | 99.8 | 5.0 | 5 | Locked-in homeowners vs current buyers |
| SH026 | 104.8 | 5.3 | 2 | The homeowner who does nothing: stuck |
| SH027 | 110.0 | 8.3 | 8 | Evidence: who really owns the mortgage market — FHFA, Fannie, Freddie |
| SH028 | 118.4 | 38.4 | 15 | Evidence: Fed working paper 'The Lock-In Effect of Rising Mortgage Rates' (24-03) |
| SH029 | 156.8 | 4.3 | 4 | Gag: 'Maybe later!' — buyer vs seller |
| SH030 | 161.0 | 7.0 | 2 | Evidence: Redfin — home relistings on the rise |
| SH031 | 168.0 | 11.2 | 9 | Phone-scrolling metaphor: Hinge/phone |
| SH032 | 179.2 | 13.0 | 7 | Evidence: Austin median asking price falls (supply response) |
| SH033 | 192.2 | 5.2 | 4 | Abundant supply: buyer sees many options |
| SH034 | 197.4 | 0.5 | 1 | Prices fall as supply grows |
| SH035 | 197.9 | 5.2 | 7 | Contrast: Hartford, Connecticut |
| SH036 | 203.1 | 3.8 | 1 | Evidence: Zillow hottest markets 2026 — Hartford #1 by rank |
| SH037 | 206.9 | 8.5 | 6 | Evidence: Hartford home prices and inventory (NAR/Redfin charts) |
| SH038 | 215.3 | 2.6 | 5 | Mortgage-rate headline wall with the map character |
| SH039 | 217.9 | 8.1 | 3 | Recap: same country and rates, opposite results (Hartford vs Austin) |
| SH040 | 226.0 | 6.7 | 4 | The supply that moves prices comes from the builder, not owners |
| SH041 | 232.7 | 4.4 | 4 | A homeowner can sit on a cheap mortgage for years; a builder can't |
| SH042 | 237.1 | 7.4 | 4 | A builder has no 3% loan to protect: ~12% construction loans, must sell this house to fund |
| SH043 | 244.5 | 5.1 | 6 | When buyers pull back, builders cut prices |
| SH044 | 249.6 | 5.6 | 2 | Most finished unsold new homes since 2009 |
| SH045 | 255.2 | 6.2 | 3 | Builders cut prices: NAHB survey 38% cutting, 66% using incentives |
| SH046 | 261.4 | 5.0 | 4 | Builders must cut prices unlike homeowners |
| SH047 | 266.5 | 18.6 | 8 | Lennar: second-largest builder reports third-quarter results on the day of the Fed hike |
| SH048 | 285.1 | 12.3 | 6 | Translation: we are selling our houses cheaper just to keep selling houses |
| SH049 | 297.4 | 9.8 | 10 | Lennar's land was bought at better prices; the only way out is to build on it and sell at  |
| SH050 | 307.2 | 11.6 | 5 | Not just Lennar: two thirds of builders offer incentives; the biggest is the rate buydown |
| SH051 | 318.8 | 9.2 | 5 | D.R. Horton: buyers in the pipeline at 4.9% while the market rate was about 6.5% |
| SH052 | 328.0 | 10.0 | 4 | The situation that shouldn't be happening: a new house priced below the used one |
| SH053 | 338.1 | 7.8 | 3 | Chart: new-home median price now below existing; the widest gap ever measured |
| SH054 | 345.9 | 7.1 | 5 | Car-lot analogy: the new model costs less than the one with 90,000 miles |
| SH055 | 353.0 | 14.0 | 5 | Part of it: builders shrinking the product (smaller lots, smaller homes, cheaper areas) |
| SH056 | 367.0 | 18.8 | 6 | The thing between builder and sale isn't always price: sometimes it's the loan |
| SH057 | 385.8 | 5.8 | 6 | About half of Lennar's sales-office visitors cannot qualify for a mortgage |
| SH058 | 391.6 | 2.2 | 1 | Even with the incentives (buydown) on the table |
| SH059 | 393.8 | 2.0 | 2 | A price cut can't fix that |
| SH060 | 395.8 | 5.5 | 3 | Not another $10,000 off: the buyer who can't qualify still can't |
| SH061 | 401.3 | 2.3 | 2 | What can I get for $2? Buyers who cannot afford even a cut price |
| SH062 | 403.6 | 6.6 | 5 | When price cuts stop bringing in buyers, builders stop cutting and stop building the next  |
| SH063 | 410.2 | 6.6 | 2 | D.R. Horton CEO says they chose to hold margin a little more than push into the units |
| SH064 | 416.8 | 4.5 | 3 | Translation: he'd rather sell fewer houses than cut prices any further |
| SH065 | 421.3 | 9.4 | 3 | The one seller that has to sell is already cutting and the biggest is hitting its limit; f |
| SH066 | 430.7 | 3.0 | 6 | When Americans can't borrow enough, who steps in? Who do you call when you need more debt? |
| SH067 | 433.6 | 3.5 | 2 | Who do you call when you need more debt? The United States government (bat-signal gag) |
| SH068 | 437.1 | 4.4 | 5 | Quick pause before the sponsor: video-player pause gag and the channel's own page |
| SH069 | 441.5 | 17.5 | 19 | Sponsor integration (Ground News): why the channel was started, news without the whole pic |
| SH070 | 459.0 | 5.5 | 3 | Ground News gathers related articles from around the world into one place |
| SH071 | 464.5 | 13.4 | 7 | Example story: Trump banning certain outlets from White House press access |
| SH072 | 478.0 | 10.5 | 5 | Framing is all over the place: compare headlines Left, Center and Right |
| SH073 | 488.5 | 4.8 | 5 | The bigger issue: whether you see the story at all; missing context |
| SH074 | 493.3 | 8.9 | 5 | Blindspot feed: stories one side of the spectrum barely covers |
| SH075 | 502.2 | 17.4 | 9 | Sponsor offer: 40% off the Ground News Vantage plan via QR code or ground.news/casual |
| SH076 | 519.6 | 1.9 | 2 | Back to how the government stepped into the housing market |
| SH077 | 521.5 | 5.6 | 7 | Government housing policy either adds buyers or keeps owners in place |
| SH078 | 527.1 | 5.2 | 4 | The government rarely adds to the supply of homes; a new policy is announced |
| SH079 | 532.3 | 7.9 | 3 | On January 8 the president directed Fannie Mae and Freddie Mac to buy $200 billion of mort |
| SH080 | 540.2 | 9.3 | 6 | Fannie Mae and Freddie Mac buy the bonds; the announcing social-media post |
| SH081 | 549.5 | 7.6 | 3 | By late February the 30-year mortgage rate dipped under 6% for the first time in 3.5 years |
| SH082 | 557.1 | 5.9 | 3 | But it didn't last: rates drifted back up and the Fed hiked the policy rate |
| SH083 | 563.0 | 2.8 | 4 | Now mortgage rates are sitting around 7% |
| SH084 | 565.8 | 3.0 | 2 | A temporary solution to a structural problem; and it wasn't the first attempt |
| SH085 | 568.8 | 11.6 | 21 | Last November: a post of a president next to a 50-year mortgage idea; the housing-finance  |
| SH086 | 580.4 | 6.6 | 2 | The housing-finance director backs away: 'we have other priorities' |
| SH087 | 587.0 | 8.2 | 5 | Mid-January: the White House floats pulling 401(k) and college-fund money for down payment |
| SH088 | 595.2 | 2.3 | 2 | That one lasted about a week: the president backs off the 401(k) idea |
| SH089 | 597.5 | 7.0 | 4 | Each of these solutions targets the demand side, and we've run this experiment before |
| SH090 | 604.5 | 18.5 | 6 | 2015: the FHA cut its mortgage-insurance premium by half a point (about $900 a year), proj |
| SH091 | 622.9 | 18.9 | 6 | Researchers went back and counted: about 17,000 new first-time buyers in year one, far sho |
| SH092 | 641.8 | 5.5 | 5 | What it did do: about 6% more buying power, and FHA buyers paid about 2.5% more for their  |
| SH093 | 647.3 | 7.4 | 3 | Higher prices hit everyone buying in those neighbourhoods (treatment vs control tracts) |
| SH094 | 654.8 | 15.3 | 8 | Roughly 500,000 buyers paid about $6,200 extra each: $3.1 billion for about 17,000 new hom |
| SH095 | 670.0 | 5.8 | 3 | A trade so bad it can only be compared to the Griner prisoner swap (newspaper-cover gag) |
| SH096 | 675.8 | 8.8 | 6 | Handing buyers money without fixing the root problem: with supply stuck, it goes into the  |
| SH097 | 684.6 | 5.8 | 4 | That's the buyer's part of the story, the loud part; the quieter part is built into the ta |
| SH098 | 690.4 | 9.4 | 6 | More than a dozen states cap how fast a home's taxable value can rise; the Lincoln Institu |
| SH099 | 699.8 | 11.0 | 7 | Caps create tax-bill discrepancies between new and long-time owners (Miami has the largest |
| SH100 | 710.8 | 12.5 | 2 | Coconut Grove, Miami: two townhouses a few doors apart, one owner pays about $4,000 a year |
| SH101 | 723.4 | 5.2 | 4 | The only difference is when they bought: 2006 versus 2023 |
| SH102 | 728.5 | 5.1 | 2 | In Florida, like most states with a cap, the assessment resets when the house sells |
| SH103 | 733.6 | 15.5 | 13 | The longer you stay, the bigger your discount, so the typical homeowner has every reason n |
| SH104 | 749.1 | 10.8 | 4 | First-time buyers fell to 21% of home purchases, the lowest since records began in 1981; t |
| SH105 | 759.9 | 10.2 | 7 | By Redfin's analysis the typical household would spend 38% of income on the mortgage; sinc |
| SH106 | 770.2 | 6.2 | 3 | The usual rule of thumb is no more than 30%; past that you are house poor |
| SH107 | 776.4 | 7.2 | 7 | So who is still getting in? Not the people who save for years and make the usual sacrifice |
| SH108 | 783.6 | 9.1 | 3 | Nearly 40% of first-time buyers under 30 used a family cash gift or inheritance for the do |
| SH109 | 792.8 | 21.0 | 12 | The Federal Reserve even published a working paper: 'Illiquid Homeownership and the Bank o |
| SH110 | 813.8 | 9.5 | 5 | Who gets parental help: households whose parents hold more wealth (the paper's descriptive |
| SH111 | 823.2 | 7.3 | 3 | With limited supply, the boost to demand ended up raising home prices (the paper's conclus |
| SH112 | 830.5 | 12.2 | 11 | Money, prices and down payments: the discount is a percentage of price |
| SH113 | 842.8 | 8.9 | 5 | Parents help; the buyer finally 'did it' |
| SH114 | 851.7 | 4.8 | 7 | Buyers without rich parents lean on low-down-payment government-backed loans such as FHA o |
| SH115 | 856.5 | 9.2 | 5 | More than one in ten FHA loans are behind on payments; for conventional loans fewer than t |
| SH116 | 865.7 | 14.8 | 7 | About 813,000 borrowers now have negative equity, up 44% in a year; 75% used FHA or VA loa |
| SH117 | 880.5 | 10.4 | 8 | The smallest down payments at near-record prices: now they are the ones falling behind |
| SH118 | 890.9 | 12.6 | 3 | Take away parental help and young homeownership drops 13 percentage points; the 2008 crisi |
| SH119 | 903.5 | 11.0 | 8 | Closing: a system that protects those already inside and hands the bill to whoever is next |
| SH120 | 914.4 | 6.3 | 1 | End card: subscribe for more; supporters list ('the insider club') |
