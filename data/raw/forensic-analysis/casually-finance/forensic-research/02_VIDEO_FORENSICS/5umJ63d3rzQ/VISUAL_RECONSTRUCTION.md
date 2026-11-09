# VISUAL RECONSTRUCTION — Brace For Impact. (5umJ63d3rzQ)

_Source: LONG_FORM · 1280×720 @ 30.0 fps · 752.8s · published 2026-03-10 · SHA256 `b07b2a4b55e2b83d…`_

## 1. Measured summary (from per-frame analysis; no interpretation)

- Frames decoded: **22583** (every frame). Reviewed shots: **124**; stable states: **479**; motion rows: **478**; micro-changes below threshold (counted, not tabulated): 50.
- Shot length: median **4.9s**, mean 6.1s, p10 2.5s, p90 9.3s → **9.9 shots/min**.
- Visual-state length: median **1.10s**, mean 1.33s → **38.2 states/min** (a new composition state roughly every 1.6s incl. transitions).
- Time in transitions/animation (frames between stable states): **114s (15%)**; stable states **639s (85%)**.
- Shot-time by technique tag (reviewer tags; a shot can carry several): ORIGINAL_DRAWING 95%; MOTION_GRAPHICS 47%; SCREEN_CAPTURE 20%; FOOTAGE_CLIP 9%; COMPOSITED_STILLS 8%; RASTER_ART 1%. Shots made only of drawn assets + text motion: 64% of runtime.
- Motion vocabulary (reviewer labels, count): CUT 239, POP_IN 69, TEXT_REVEAL 36, POSE_CHANGE 32, ZOOM_IN 11, BUILD 11, FACE_CHANGE 10, ANIM 9, REPOSITION 9, FOOTAGE_CUT 8, TEXT_SWAP 7, REFRAME 6, STRIKE 5, EXIT 5.
- Narration pace: **185 words/min** over the voiced span; sync of visual events vs ASR word times: ON_WORD_START 235, DURING_WORD 235, BEFORE_WORD 89, AFTER_WORD 43.
- Shot-start offset vs nearest word start: median **0 ms** (p10 -111, p90 284); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.
- Reused assets: 86 of 253 asset keys appear in more than one shot. Longest on-screen assets:

| Asset | Type | Seconds on screen | Shots | Technique class |
|---|---|---:|---:|---|
| HOST | CHARACTER_HOST | 198.43 | 69 | ORIGINAL_DRAWING |
| OBJ_CHALKBOARD | OBJECT | 76.33 | 23 | ORIGINAL_DRAWING |
| UI_SPONSOR_BAR | UI_OVERLAY | 69.36 | 16 | MOTION_GRAPHICS |
| POINTER | PROP | 59.7 | 25 | ORIGINAL_DRAWING |
| CHAR_JAPAN_FACE | CHARACTER | 38.93 | 12 | ORIGINAL_DRAWING |
| MAP_JAPAN | CHARACTER_MAP | 34.24 | 13 | ORIGINAL_DRAWING |
| OBJ_BANKNOTE_BIG | OBJECT | 33.2 | 12 | ORIGINAL_DRAWING |
| OBJ_TREASURY_CERT | OBJECT | 33.04 | 11 | ORIGINAL_DRAWING |
| BLDG_FED | OBJECT_BUILDING | 31.07 | 10 | ORIGINAL_DRAWING |
| OBJ_MONEY_BAG_BIG | OBJECT | 30.96 | 15 | ORIGINAL_DRAWING |
| ICON_PERCENT_ORANGE | ICON | 28.33 | 12 | ORIGINAL_DRAWING |
| OBJ_YEN_NOTES | OBJECT | 26.76 | 9 | ORIGINAL_DRAWING |

## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)

| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |
|---|---:|---:|---:|---:|---:|---:|
| 0-5s (0-5s) | 9 | 1 | 8 | 216 | 0 | 1 |
| 5-15s (5-15s) | 11 | 2 | 11 | 204 | 0 | 2 |
| 15-30s (15-30s) | 13 | 4 | 13 | 188 | 3 | 2 |
| 30-60s (30-60s) | 28 | 7 | 29 | 174 | 3 | 6 |
| 60s-midpoint (60-376s) | 194 | 50 | 193 | 175 | 16 | 34 |
| midpoint-last60s (376-693s) | 183 | 50 | 183 | 192 | 18 | 31 |
| last 60s (693-753s) | 41 | 10 | 41 | 180 | 4 | 7 |

*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.

First visual states (literal): [S001.0 @0.0s] Small figure lying anxiously in a bed at the upper left of a blank canvas [S001.1 @0.5s] A dark monster with glowing red eyes peeks out from under the bed [S001.2 @1.1s] Large green USA-map shape (no face) appears at the right [S001.3 @1.7s] Map smaller with money bags and banknotes drawn on it

Closing frames: [S115.2 @744.2s] Bald figure behind an open NEWS newspaper at the lower left [S115.3 @745.4s] Second newspaper held up by the US map character at the right of the bald reader [S116.0 @746.8s] White end card: a small lead-in and the video-platform logo above three crossed-out round social-media icons at left and the title


## 2. Shot list index

Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.

| Shot | Start | Dur | States | Purpose |
|---|---:|---:|---:|---|
| SH001 | 0.0 | 7.4 | 15 | Hook: the biggest risk to the US economy was never the AI bubble, China or the man in the  |
| SH002 | 7.4 | 7.4 | 4 | It's something much more boring that you've likely never heard of unless you've gone down  |
| SH003 | 14.8 | 3.2 | 2 | And that's exactly why nobody's paying attention |
| SH004 | 18.0 | 2.5 | 3 | If you've been wondering why mortgage rates refuse to fall |
| SH005 | 20.5 | 3.5 | 1 | Why stocks randomly freak out every few months |
| SH006 | 24.0 | 4.9 | 5 | The Federal Reserve can talk about cutting rates but financial conditions still feel tight |
| SH007 | 28.9 | 1.9 | 5 | The answer doesn't start in Washington |
| SH008 | 30.8 | 2.7 | 3 | It starts in Tokyo |
| SH009 | 33.5 | 4.1 | 3 | The most boring asset on earth: Japanese government bonds |
| SH010 | 37.7 | 3.0 | 2 | The country best known for attracting American weebs |
| SH011 | 40.6 | 5.5 | 4 | Has also been the duct tape quietly holding the global financial system together for 30 ye |
| SH012 | 46.1 | 2.1 | 2 | And that duct tape is starting to peel |
| SH013 | 48.2 | 4.9 | 5 | To understand why Japan is so important, you first have to rewind to the early 90s |
| SH014 | 53.1 | 10.6 | 8 | In 1992 Japan's asset bubble burst: real estate and equities collapsed, and Japan entered  |
| SH015 | 63.7 | 6.6 | 8 | It was a three-decade-long period of being financially f**ked: no real growth, no inflatio |
| SH016 | 70.3 | 2.8 | 2 | It was like the economy hit pause and nobody could find the remote |
| SH017 | 73.1 | 2.1 | 4 | Nobody could find the remote: a figure searching a living room |
| SH018 | 75.2 | 8.6 | 8 | So the Bank of Japan cut rates to zero and then below zero |
| SH019 | 83.8 | 5.9 | 5 | Then they introduced yield curve control, which sounds like a Marvel villain |
| SH020 | 89.6 | 3.6 | 2 | It just means we're going to cap long-term bond yields whether the market likes it or not |
| SH021 | 93.2 | 5.0 | 3 | The Japanese government superglued interest rates to the floor |
| SH022 | 98.2 | 2.9 | 2 | For decades Japanese government bonds yielded pretty much nothing |
| SH023 | 101.1 | 10.1 | 9 | That created massive problems for Japanese investors: a life insurer, pension fund or bank |
| SH024 | 111.2 | 3.4 | 3 | Your domestic government bonds are paying you 0% |
| SH025 | 114.6 | 2.1 | 2 | This leaves you with two choices |
| SH026 | 116.8 | 2.7 | 4 | Option one: accept no return on your cash |
| SH027 | 119.5 | 2.9 | 3 | Option two: go shopping overseas, and they chose option two |
| SH028 | 122.4 | 4.7 | 2 | Japan entered a multi-decade global shopping spree |
| SH029 | 127.1 | 2.6 | 1 | Japan became the largest foreign holder of US Treasuries |
| SH030 | 129.7 | 3.0 | 1 | One of the largest buyers of US mortgage-backed securities |
| SH031 | 132.7 | 3.8 | 2 | The world's largest net creditor nation: Japan became the world's ATM |
| SH032 | 136.5 | 9.4 | 6 | It's not because Japan just loves sending capital to America; the math made sense |
| SH033 | 145.9 | 3.7 | 3 | Meet Bob: he wants to start making money through investing |
| SH034 | 149.6 | 5.0 | 4 | Bob goes to the Japanese markets and borrows money in yen at near-zero interest rates |
| SH035 | 154.6 | 4.9 | 7 | Then Bob converts that yen into dollars and buys US Treasuries yielding 4% |
| SH036 | 159.4 | 3.0 | 4 | After hedging costs and fees he pockets the spread |
| SH037 | 162.5 | 9.0 | 9 | That's what became known as the yen carry trade: investors borrow in yen at near zero and  |
| SH038 | 171.5 | 8.4 | 5 | When borrowing costs are near zero they don't just buy Treasuries; they buy tech stocks, r |
| SH039 | 179.9 | 4.5 | 4 | If it's got a pulse and it yields more than 0%, they'll buy it |
| SH040 | 184.4 | 4.3 | 4 | This trade became one of the largest sources of global liquidity |
| SH041 | 188.8 | 4.5 | 4 | At its peak the yen carry trade was estimated by some banks to be in the trillions |
| SH042 | 193.3 | 3.2 | 3 | It was like the global markets were running on Japanese Wi-Fi |
| SH043 | 196.5 | 8.0 | 6 | The trade relied on one assumption: Japanese yields would stay near zero forever |
| SH044 | 204.5 | 5.7 | 7 | But in 2024 that assumption broke when the Bank of Japan ended its yield curve control pol |
| SH045 | 210.2 | 3.5 | 3 | And Japan raised interest rates for the first time in 17 years |
| SH046 | 213.7 | 1.6 | 3 | And then they raised them again |
| SH047 | 215.3 | 13.0 | 5 | Immediately after the second hike the S&P 500 dropped 6% and Japan's Nikkei 225 plummeted  |
| SH048 | 228.3 | 3.2 | 2 | It was a clear signal that markets were officially spooked |
| SH049 | 231.5 | 5.6 | 4 | Because when Japanese yields rise, two things happen: borrowing in yen gets more expensive |
| SH050 | 237.1 | 3.4 | 2 | And two, hedging currency risk becomes more expensive too |
| SH051 | 240.5 | 2.9 | 2 | And suddenly the free-money trade isn't so free anymore |
| SH052 | 243.4 | 4.4 | 3 | And that 4% US Treasury Bob was looking at doesn't look so good anymore |
| SH053 | 247.8 | 2.9 | 1 | This was the beginning of the end for the yen carry trade |
| SH054 | 250.7 | 6.4 | 2 | Because now the math had flipped; when the math flips, the capital flows flip too |
| SH055 | 257.1 | 3.9 | 1 | And the money that flowed out of Japan for decades was starting to return home |
| SH056 | 261.0 | 5.2 | 3 | This is what's called repatriation |
| SH057 | 266.2 | 10.5 | 4 | And it's one of the biggest threats in global markets today: investors realize the cheapes |
| SH058 | 276.7 | 7.7 | 5 | For decades Japan was one of the most consistent, price-insensitive buyers of long-term Tr |
| SH059 | 284.4 | 9.9 | 6 | The yields on long-term Treasuries aren't set by the Fed chair: the Fed controls short-ter |
| SH060 | 294.2 | 2.4 | 1 | Those yields are largely determined by supply and demand |
| SH061 | 296.7 | 4.2 | 4 | The problem is everyone's staring at the wrong lever |
| SH062 | 300.8 | 69.8 | 10 | Legendary investor and founder of the world's largest hedge fund explains it: watch the bo |
| SH063 | 370.6 | 5.5 | 4 | While everyone is hyper-analysing the Fed chair's press conferences like a new game-traile |
| SH064 | 376.1 | 13.3 | 4 | They're looking at the wrong end of the yield curve: the Fed controls the short end, the o |
| SH065 | 389.4 | 4.9 | 5 | The long end is driven by supply and demand; the US runs trillion-dollar deficits annually |
| SH066 | 394.3 | 8.4 | 2 | The Treasury has to issue massive amounts of new debt every year just to keep the lights o |
| SH067 | 402.7 | 3.6 | 2 | And as this debt issuance keeps growing, someone has to absorb it: where does it go? |
| SH068 | 406.2 | 9.2 | 4 | For the last few decades Japan was a key part of that absorption machine |
| SH069 | 415.4 | 4.1 | 3 | Sponsor segue: a quick pause, because this video is sponsored by Gamma |
| SH070 | 419.5 | 3.8 | 2 | I personally use Gamma because the hardest part about creating finance videos isn't the re |
| SH071 | 423.2 | 3.0 | 2 | It's turning scattered ideas into a clear structure |
| SH072 | 426.2 | 6.8 | 5 | When I'm breaking down complex topics like the cross-currency carry trade, the thinking is |
| SH073 | 433.0 | 3.1 | 2 | Notes everywhere, half-formed arguments, and connections that make sense in my head |
| SH074 | 436.1 | 3.4 | 3 | If the structure isn't clear, the whole thing falls apart |
| SH075 | 439.5 | 8.6 | 5 | That's where Gamma comes in: it isn't just a presentation tool, it's the bridge between ra |
| SH076 | 448.1 | 8.8 | 4 | Here's how I've been using it: start inside an AI assistant and upload research and notes |
| SH077 | 456.9 | 6.6 | 3 | From there I go into the assistant's settings and enable the new Gamma connector |
| SH078 | 463.5 | 15.4 | 9 | All I have to do is ask Gamma to create a presentation; in seconds it builds a clean struc |
| SH079 | 478.9 | 4.5 | 2 | Gamma allows you to go from brainstorming to a finished deck without losing momentum |
| SH080 | 483.4 | 1.8 | 2 | It's not just limited to the AI assistant |
| SH081 | 485.2 | 3.5 | 4 | Gamma can connect to your GitHub, Notion and even your Gmail |
| SH082 | 488.7 | 3.2 | 2 | Gamma makes sure your ideas don't stay trapped as notes |
| SH083 | 491.9 | 5.9 | 3 | If you're interested, head to gamma.app or find it inside the assistant's connectors |
| SH084 | 497.8 | 2.4 | 2 | Thank you again to Gamma for sponsoring this video |
| SH085 | 500.2 | 9.7 | 9 | Now back to how Japan might wreck our economy: if one of the largest buyers stops buying,  |
| SH086 | 509.9 | 5.4 | 3 | And that's how supply and demand shape long-term bond yields |
| SH087 | 515.3 | 5.9 | 4 | The Fed cuts the federal funds rate and short-term yields fall, but long-term yields stay  |
| SH088 | 521.2 | 3.3 | 2 | And that's how you get what's called a steepening yield curve |
| SH089 | 524.5 | 7.7 | 5 | If long-term rates stop cooperating it stops being a bond-market story and becomes an ever |
| SH090 | 532.2 | 7.8 | 1 | When analysts build models to value stocks they discount cash flows using long-term yields |
| SH091 | 540.0 | 8.3 | 5 | When long-term yields remain elevated the present value of future cash flows falls, valuat |
| SH092 | 548.3 | 8.8 | 4 | So even if earnings are fine, the price investors are willing to pay for those earnings ch |
| SH093 | 557.1 | 5.8 | 3 | Markets can suddenly feel unstable even when the headlines look calm |
| SH094 | 563.0 | 4.4 | 5 | The 10-year yield sets the price of money and is the foundation of nearly every asset valu |
| SH095 | 567.4 | 2.1 | 2 | Mortgage rates are another example |
| SH096 | 569.5 | 6.6 | 5 | Like stock valuations, mortgage rates are largely anchored to long-term Treasury yields |
| SH097 | 576.1 | 5.3 | 3 | If the 10-year yield doesn't meaningfully fall, mortgage rates don't magically drift back  |
| SH098 | 581.4 | 8.3 | 5 | So the Fed can cut the federal funds rate all they want, but if global demand for Treasuri |
| SH099 | 589.7 | 14.2 | 8 | When that happens mortgage rates stay high, housing affordability stays strained, refinanc |
| SH100 | 603.9 | 7.3 | 3 | It's not just mortgage rates and equity valuations: if you zoom out to corporate credit it |
| SH101 | 611.2 | 6.6 | 2 | When capital was cheap in 2020 and 2021 and rates were suppressed, companies issued debt l |
| SH102 | 617.8 | 8.0 | 7 | Credit is the bloodstream of the corporate world; with cheap financing we see more deal fl |
| SH103 | 625.8 | 8.7 | 5 | If borrowing costs stay elevated we see the opposite: risk appetite falls, growth slows an |
| SH104 | 634.6 | 6.6 | 2 | And this is the main point of the video: for 30 years the US benefited from being on the r |
| SH105 | 641.2 | 1.7 | 1 | And now that trade is unwinding |
| SH106 | 642.9 | 1.3 | 1 | As the investor said, the bond market is the backbone of all markets and the interest rate |
| SH107 | 644.2 | 2.3 | 3 | And what we are currently seeing is a tangible catalyst reshaping the foundation of the bo |
| SH108 | 646.5 | 9.1 | 4 | There's a reason traditional financial media is ignoring this: it's not clickable and woul |
| SH109 | 655.6 | 6.5 | 5 | Because it requires patience and nuance; instead the narratives become dramatically oversi |
| SH110 | 662.1 | 9.6 | 5 | Nobody wants to hear 'let's discuss the cross-currency carry trade' because that requires  |
| SH111 | 671.7 | 1.6 | 2 | And more brain cells than doom-scrolling allows for |
| SH112 | 673.3 | 6.7 | 1 | Instead people want inflation, AI and whatever Nvidia did last week: visible, loud topics |
| SH113 | 680.0 | 11.2 | 7 | The narratives become dramatically oversimplified: if the Fed cuts rates, financial condit |
| SH114 | 691.2 | 7.0 | 6 | And that's the lie we're being sold: one rate cut fixes everything, liquidity is automatic |
| SH115 | 698.2 | 4.9 | 5 | But what if they don't? What if the largest foreign holder of US Treasuries steps back? |
| SH116 | 703.1 | 8.9 | 7 | Then you see global liquidity tighten; liquidity is the oxygen in markets |
| SH117 | 712.0 | 3.6 | 2 | And when it tightens the cost of money changes everywhere |
| SH118 | 715.6 | 5.4 | 6 | Like I covered, it affects everything from stock valuations to mortgage rates to corporate |
| SH119 | 721.0 | 4.7 | 4 | That's why I made this channel: to shine a light on the issues that actually matter |
| SH120 | 725.7 | 4.7 | 2 | The issues that traditional financial media won't touch because they don't get clicks |
| SH121 | 730.4 | 6.0 | 4 | If you're interested in what's actually happening in markets, hit subscribe and turn notif |
| SH122 | 736.4 | 6.1 | 2 | The real threats in markets aren't the loud ones; those are usually priced in |
| SH123 | 742.5 | 4.4 | 4 | The real threats are the ones hiding in plain sight |
| SH124 | 746.8 | 5.9 | 1 | End card: subscribe for more, only on this platform |
