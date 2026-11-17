# Finance ANALYST — Channel Forensic Report

Channel #046 of 69 · investigation tier 2 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** Small POV channel (2.9k subs) that produced the dataset's clearest **packaging A/B-like pair**: the same 10-year-reunion story opened as "POV: Your Life After You Became a Millionaire in Your 20s" (28 Sep, 367 views) and, a week later, as **"POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire" (5 Oct, 368k views, PI 147)** — a concrete scene + secrecy in the title turned a flop into the channel's biggest hit. Lottery-secrecy POVs also win; generic "things not worth your money" and "rat race" titles flop.

## 1. Channel identity and positioning
Comic-style second-person POV channel (handle @FinanceANALYST1; registered "wealth/business POV"); 45% of titles share word-sets with other channels (POV cluster). Audience: 25-45 fantasy/status viewers. 93-day gap before an Oct 2026 restart that produced all winners (median PI first third 0.85 → last third 6.37).

## 2. Database inventory and coverage
- Channel ID `UCWQA4bQidJMFH3odS-RGEyA` · handle @FinanceANALYST1 · https://www.youtube.com/channel/UCWQA4bQidJMFH3odS-RGEyA
- Registered sub-niche: wealth/business POV · subscribers: 2,850 · availability: AVAILABLE nan
- Description: USA Finance with Liam is an animated documentary channel that shows you exactly what your financial decisions are building — or destroying — in real time. No hype. No stock tips. No shortcuts. Just cinematic, honest stories about wealth, debt, identity, and the real cost of every money decision you have ever made or avoided. If you have ever wondered why your salary keeps rising but nothing change…
- Videos in DB 29 (long 29, Shorts 0); views 29; transcripts 29 (100%); thumbnail images 29 (100%); FULL metadata 100%; PI-classified long 26
- Dates 2026-06-05 → 2026-11-01; median views 1,696; p90 21,974; max 367,569
- Cadence: 5.9 uploads/month over 4.9 months; median gap 1.0 d; max gap 93 d; weekday mode Sunday
- Duration (min): median 15.7; p10 11.0; p90 17.2; first-third median 13.5 vs last-third 17.0
- Spearman(gap-before-upload, PI) = 0.44; Spearman(duration, PI) = 0.64; median PI first third 0.85 vs last third 6.37
- PI classes (long): Underperforming 11, Breakout 7, Average 6, Successful 2; near-duplicate-script flags 0
- Titles whose word-set also appears on another channel: 13 (45%)
- **POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire** — [3L4Mypm3uWo](https://www.youtube.com/watch?v=3L4Mypm3uWo) · 2026-10-05 · 17.42 min · 367,569 views · PI 147.44 (Breakout) · pov_story/pov_story · face=False · thumb text: “1./if”
- **POV: You Won the Lottery the Morning After Your Ex Left You** — [vltf4XOWLg8](https://www.youtube.com/watch?v=vltf4XOWLg8) · 2026-10-26 · 15.70 min · 75,455 views · PI 30.03 (Breakout) · pov_story/pov_story · face=True · thumb text: “Qt”
- **POV: You Turned a Bankrupt Factory Into an $800 Million Business** — [BspuJfCPnFw](https://www.youtube.com/watch?v=BspuJfCPnFw) · 2026-10-14 · 17.17 min · 26,494 views · PI 10.54 (Breakout) · banking_cash/pov_story · face=True · thumb text: “al/ay”
- **POV: You Won the Lottery and Told No One — 10 Years Later** — [DChwF6upfr0](https://www.youtube.com/watch?v=DChwF6upfr0) · 2026-10-21 · 16.40 min · 20,844 views · PI 8.29 (Breakout) · pov_story/pov_story · face=True · thumb text: “nan”
- **POV: Your Life After You Became a Millionaire in Your 20s** — [07d35Lx5Kco](https://www.youtube.com/watch?v=07d35Lx5Kco) · 2026-09-28 · 14.12 min · 367 views · PI 0.15 (Underperforming) · pov_story/pov_story · face=False · thumb text: “Al/=)”
- **5 Things No Longer Worth Your Money In The US** — [w1WcHaOCXPk](https://www.youtube.com/watch?v=w1WcHaOCXPk) · 2026-06-05 · 10.18 min · 145 views · PI 0.17 (Underperforming) · taxes_irs/list_countdown · face=True · thumb text: “NOT/WORTH/fil”
- **POV: You Retired at 45 — Nobody Knows** — [xB1N_Rrh44k](https://www.youtube.com/watch?v=xB1N_Rrh44k) · 2026-09-25 · 16.48 min · 533 views · PI 0.21 (Underperforming) · retirement_accounts_tax/pov_story · face=False · thumb text: “Bs”
- **You Escaped the Rat Race In US. Nobody Noticed.** — [9IKQqagWkjE](https://www.youtube.com/watch?v=9IKQqagWkjE) · 2026-06-06 · 11.18 min · 186 views · PI 0.22 (Underperforming) · banking_cash/statement_other · face=True · thumb text: “nan”

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 29 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-06-05 | [5 Things No Longer Worth Your Money In The US](https://www.youtube.com/watch?v=w1WcHaOCXPk) | 10.2 | 145 | 0.17 | Underperforming | taxes_irs | list_countdown | Y |
| 2 | 2026-06-06 | [You Escaped the Rat Race In US. Nobody Noticed.](https://www.youtube.com/watch?v=9IKQqagWkjE) | 11.2 | 186 | 0.22 | Underperforming | banking_cash | statement_other | Y |
| 3 | 2026-06-07 | [Your Life Driving the Same Car for 10 Years In US](https://www.youtube.com/watch?v=oRIMUdbx5RE) | 14.5 | 1,026 | 1.28 | Average | banking_cash | statement_other | Y |
| 4 | 2026-06-09 | [You Won The Lottery at a Random Store. Your Life Changes Overnight.](https://www.youtube.com/watch?v=ge7eEmwERFI) | 13.5 | 395 | 0.47 | Underperforming | company_business_case | news_change_update | Y |
| 5 | 2026-06-11 | [You Have $450 Million Nobody Knows / Life As Silent Millionaire](https://www.youtube.com/watch?v=jwypWP6wY6c) | 16.4 | 1,696 | 2.12 | Successful | wealth_psychology_habits | statement_other | Y |
| 6 | 2026-06-13 | [Don't Buy The SpaceX IPO Until You See This (Don't Make The Mistake)](https://www.youtube.com/watch?v=wHgclvnO2uA) | 10.3 | 984 | 1.23 | Average | social_security | warning_mistake | Y |
| 7 | 2026-06-14 | [How Your Friends Treat You at Every Level of Wealth / From $1,800 to $100 Million](https://www.youtube.com/watch?v=e8luGvCZV7g) | 10.0 | 215 | 0.26 | Underperforming | wealth_psychology_habits | statement_other | Y |
| 8 | 2026-06-22 | [POV: You're Worth $19 Million and Nobody Knows It](https://www.youtube.com/watch?v=2bh_EdIbV68) | 15.7 | 987 | 1.23 | Average | pov_story | pov_story | Y |
| 9 | 2026-09-24 | [Building a $600 Million Holding Company as a Silent Businessman](https://www.youtube.com/watch?v=Bh1eCGV9oMU) | 16.0 | 4,048 | 1.62 | Average | company_business_case | statement_other | Y |
| 10 | 2026-09-25 | [POV: You Retired at 45 — Nobody Knows](https://www.youtube.com/watch?v=xB1N_Rrh44k) | 16.5 | 533 | 0.21 | Underperforming | retirement_accounts_tax | pov_story | Y |
| 11 | 2026-09-27 | [POV: You Won the $600 Million Lottery — And Told No One](https://www.youtube.com/watch?v=pBZG0L6XFww) | 15.0 | 801 | 0.32 | Underperforming | pov_story | pov_story | Y |
| 12 | 2026-09-28 | [POV: Your Life After You Became a Millionaire in Your 20s](https://www.youtube.com/watch?v=07d35Lx5Kco) | 14.1 | 367 | 0.15 | Underperforming | pov_story | pov_story | Y |
| 13 | 2026-09-30 | [Dating as a Silent Millionaire — She Thought I Was a Mechanic](https://www.youtube.com/watch?v=6MZrUtB_1FI) | 14.8 | 18,484 | 7.41 | Breakout | wealth_psychology_habits | pov_story | Y |
| 14 | 2026-10-02 | [POV: You Adopted the Old Money Mindset — Your Life Changed](https://www.youtube.com/watch?v=Lc52P0PTbP4) | 13.9 | 734 | 0.29 | Underperforming | pov_story | pov_story | Y |
| 15 | 2026-10-04 | [POV: You Chose Wealth Over Looking Rich](https://www.youtube.com/watch?v=Bwolr-sZu4M) | 15.6 | 832 | 0.33 | Underperforming | pov_story | pov_story | Y |
| 16 | 2026-10-05 | [POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire](https://www.youtube.com/watch?v=3L4Mypm3uWo) | 17.4 | 367,569 | 147.44 | Breakout | pov_story | pov_story | Y |
| 17 | 2026-10-07 | [POV: You Won $50 Million and Turned It Into a $600 Million Business Empire](https://www.youtube.com/watch?v=KcNixNQVLQM) | 16.8 | 2,493 | 0.99 | Average | company_business_case | pov_story | Y |
| 18 | 2026-10-08 | [POV: You’re the Broke Looking Friend With a Six-Figure Portfolio](https://www.youtube.com/watch?v=gJ1PhZ-V3P8) | 14.9 | 1,533 | 0.61 | Average | investing_stocks | pov_story | Y |
| 19 | 2026-10-09 | [POV: Your Girlfriend Left You for a Richer Man—Then Discovered You Had Built Quiet Old Mon](https://www.youtube.com/watch?v=67kdyNBTgwU) | 16.8 | 12,821 | 5.14 | Breakout | pov_story | pov_story | Y |
| 20 | 2026-10-10 | [POV: Your Ex Found Out You Got Rich — Now She Wants You Back](https://www.youtube.com/watch?v=EaBdVxh2yiI) | 16.8 | 18,915 | 7.59 | Breakout | pov_story | pov_story | Y |
| 21 | 2026-10-14 | [POV: You Turned a Bankrupt Factory Into an $800 Million Business](https://www.youtube.com/watch?v=BspuJfCPnFw) | 17.2 | 26,494 | 10.54 | Breakout | banking_cash | pov_story | Y |
| 22 | 2026-10-16 | [POV: You Lived Like Old Money for 10 Years—Here’s What Happened](https://www.youtube.com/watch?v=LgvemOYeZsA) | 16.0 | 2,513 | 0.41 | Underperforming | pov_story | pov_story | Y |
| 23 | 2026-10-17 | [POV: You Turned Grandpa’s Failing Business Into a $650 Million Empire](https://www.youtube.com/watch?v=OBH_hGmlLrU) | 17.0 | 6,096 | 2.43 | Successful | company_business_case | pov_story | Y |
| 24 | 2026-10-18 | [POV: You Pretended to Be Broke on Your First Date—She Paid for Dinner](https://www.youtube.com/watch?v=JhTsw5uD-8A) | 15.4 | 1,706 | 0.28 | Underperforming | pov_story | pov_story | Y |
| 25 | 2026-10-21 | [POV: You Won the Lottery and Told No One — 10 Years Later](https://www.youtube.com/watch?v=DChwF6upfr0) | 16.4 | 20,844 | 8.29 | Breakout | pov_story | pov_story | Y |
| 26 | 2026-10-26 | [POV: You Won the Lottery the Morning After Your Ex Left You](https://www.youtube.com/watch?v=vltf4XOWLg8) | 15.7 | 75,455 | 30.03 | Breakout | pov_story | pov_story | Y |
| 27 | 2026-10-28 | [POV: You Bought a Bankrupt Hotel for $1 Million—Now It’s Worth $400 Million](https://www.youtube.com/watch?v=ybXOD52VOLQ) | 17.4 | 4,014 |  | NOT_CLASSIFIED | banking_cash | pov_story | Y |
| 28 | 2026-10-29 | [POV: You Bought Your First Business at 25—10 Years Later](https://www.youtube.com/watch?v=eSapT17m7oc) | 17.4 | 6,070 |  | NOT_CLASSIFIED | pov_story | pov_story | Y |
| 29 | 2026-11-01 | [How a Silent Businessman Spends His First $10 Million](https://www.youtube.com/watch?v=Nk5Zoh28-Bs) | 17.2 | 1,631 |  | NOT_CLASSIFIED | taxes_irs | statement_other | Y |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| pov_story | 13 | 13 | 2,513 | 0.82 | 5 | 6 | 2026-06-22 | 2026-10-29 |
| banking_cash | 4 | 4 | 2,520 | 1.28 | 1 | 1 | 2026-06-06 | 2026-10-28 |
| company_business_case | 4 | 4 | 3,270 | 1.31 | 1 | 1 | 2026-06-09 | 2026-10-17 |
| wealth_psychology_habits | 3 | 3 | 1,696 | 2.12 | 2 | 1 | 2026-06-11 | 2026-09-30 |
| taxes_irs | 2 | 2 | 888 | 0.17 | 0 | 1 | 2026-06-05 | 2026-11-01 |
| investing_stocks | 1 | 1 | 1,533 | 0.61 | 0 | 0 | 2026-10-08 | 2026-10-08 |
| retirement_accounts_tax | 1 | 1 | 533 | 0.21 | 0 | 1 | 2026-09-25 | 2026-09-25 |
| social_security | 1 | 1 | 984 | 1.23 | 0 | 0 | 2026-06-13 | 2026-06-13 |

Title-format mix (INFERRED tags): pov_story: n=20.0, medPI=1.11 · statement_other: n=6.0, medPI=1.28 · list_countdown: n=1.0, medPI=0.17 · news_change_update: n=1.0, medPI=0.47 · warning_mistake: n=1.0, medPI=1.23

POV stories (13, median 0.82 but 5 hits); wealth-psychology (2.12); taxes/retirement weak.

## 5. Winning video analysis
1. **POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire** (3L4Mypm3uWo, 368k, PI 147): "7:40 on a Saturday night… parking an 8-year-old pickup truck next to a brand new Range Rover in your old high school parking lot… ladder rack… faded magnet" — status contrast in one image.
2. **POV: You Won the Lottery the Morning After Your Ex Left You** (vltf4XOWLg8, 75k, PI 30): "sitting on the floor… because there's no longer a couch… four dents where its legs pressed" — loss then windfall.
3. **POV: You Turned a Bankrupt Factory Into an $800 Million Business** (BspuJfCPnFw, PI 10.5) and **POV: You Won the Lottery and Told No One — 10 Years Later** (DChwF6upfr0, PI 8.3 — the same title as Finance POV's 16 Oct video, 5 days later; weaker than the original's 341k).

### Evidence: top-PI long-form videos
- **POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire** — [3L4Mypm3uWo](https://www.youtube.com/watch?v=3L4Mypm3uWo) · 2026-10-05 · 17.42 min · 367,569 views · PI 147.44 (Breakout) · pov_story/pov_story · face=False · thumb text: “1./if”
  - 0-30s: “It's 7:40 on a Saturday night and you're parking an 8-year-old pickup truck next to a brand new Range Rover in your old high school parking lot. There's still a ladder rack on the truck. There's a faded magnet on the door that says Brightline Exterior Cleaning. You thought about renting something nicer for tonight. You decided against it. Inside the gym, there's a banner that says class of 2016, 10 years, and a table”
  - end: “succeed. They were voting on the wrong things. The car, the continents, the grades, the noise. Real success doesn't show up at a reunion. It's built on driveways and in spreadsheets, on cold mornings when nobody's watchi…” · sources: Academic / research study
- **POV: You Won the Lottery the Morning After Your Ex Left You** — [vltf4XOWLg8](https://www.youtube.com/watch?v=vltf4XOWLg8) · 2026-10-26 · 15.70 min · 75,455 views · PI 30.03 (Breakout) · pov_story/pov_story · face=True · thumb text: “Qt”
  - 0-30s: “It's 7:12 on a Sunday morning in Tampa, Florida, and you're sitting on the floor of your apartment because there's no longer a couch to sit on. There's a rectangle of cleaner carpet where it used to be. There are four dents where its legs pressed down for 2 years. Your girlfriend took it last night along with the TV, the good towels, the air fryer, and the framed photo of the two of you”
  - end: “think about who really shows up for you, hit like, share it with someone who was there for you on day one, and subscribe for more stories like this. This channel is still small, and every subscriber genuinely helps. And …” · sources: CBO / Treasury
- **POV: You Turned a Bankrupt Factory Into an $800 Million Business** — [BspuJfCPnFw](https://www.youtube.com/watch?v=BspuJfCPnFw) · 2026-10-14 · 17.17 min · 26,494 views · PI 10.54 (Breakout) · banking_cash/pov_story · face=True · thumb text: “al/ay”
  - 0-30s: “It's 9:40 on a Tuesday morning and you're sitting at the end of a long glass conference table on the 52nd floor of a tower in downtown Chicago. Through the window, Lake Michigan is the color of an old nickel. In front of you sits a leather folder nobody has opened yet. Inside it is a number, $800 million. That's what a cookware conglomerate from Germany is offering for your company. Seven bankers in navy”
  - end: “stops to ask who he is. That's exactly how you like it. If this story made you think differently about business and real wealth, hit like and subscribe for more stories like this one. And tell me in the comments, would y…”
- **POV: You Won the Lottery and Told No One — 10 Years Later** — [DChwF6upfr0](https://www.youtube.com/watch?v=DChwF6upfr0) · 2026-10-21 · 16.40 min · 20,844 views · PI 8.29 (Breakout) · pov_story/pov_story · face=True · thumb text: “nan”
  - 0-30s: “It's 5:50 on a Friday morning. You're sitting in the break room of a cold storage warehouse wearing a faded orange safety vest eating a peanut butter sandwich out of a plastic bag. The vending machine hums. The coffee tastes like cardboard. Outside a line of refrigerated trucks is waiting to be unloaded. Across the table your buddy Benny is stressing out. His daughter Sophie graduates high school tonight. She got into a great …”
  - end: “tell? And would they still treat you the same? If this story made you think, hit that like button and subscribe for more stories about quiet wealth and doing things your own way. And tell me in the comments, what's the f…” · sources: Academic / research study

## 6. Underperforming video analysis
- **POV: Your Life After You Became a Millionaire in Your 20s** (07d35Lx5Kco, 367 views): *same reunion-gym opening* as the winner, but a generic title (VERIFIED in transcripts: both open at a 10-year reunion).
- **5 Things No Longer Worth Your Money In The US** (w1WcHaOCXPk, 145) and **You Escaped the Rat Race In US. Nobody Noticed.** (9IKQqagWkjE, 186): early generic lists/POVs with "In US" keyword stuffing.
- **POV: You Retired at 45 — Nobody Knows** (xB1N_Rrh44k, 533): secrecy premise that won for Sonny Finance ("Retired at 35") — late variant.

### Evidence: bottom-PI long-form videos
- **POV: Your Life After You Became a Millionaire in Your 20s** — [07d35Lx5Kco](https://www.youtube.com/watch?v=07d35Lx5Kco) · 2026-09-28 · 14.12 min · 367 views · PI 0.15 (Underperforming) · pov_story/pov_story · face=False · thumb text: “Al/=)”
  - 0-30s: “POV, your life after you became a millionaire in your 20s. It's 8:40 on a Saturday night, and you're standing in a high school gymnasium you haven't walked into in 10 years, wearing a name tag with your senior photo printed on it. The gym smells exactly the same, floor wax, old popcorn, and something vaguely like chlorine drifting in from the pool down the hall. Somebody has hung blue and white streamers from the”
  - end: “They look like someone at a reunion who doesn't need to tell you anything. If you're in your 20s and working toward your own number, tell me in the comments what you do with your life if money was no longer the reason yo…”
- **5 Things No Longer Worth Your Money In The US** — [w1WcHaOCXPk](https://www.youtube.com/watch?v=w1WcHaOCXPk) · 2026-06-05 · 10.18 min · 145 views · PI 0.17 (Underperforming) · taxes_irs/list_countdown · face=True · thumb text: “NOT/WORTH/fil”
  - 0-30s: “Right now, while you're watching this, your bank account is being quietly emptied. Not from some catastrophe, not from one bad decision, just a slow, invisible bleed. $15 here, $25 there. The kind of losses that never feel like losses until you sit down at the end of the month and wonder where it all went. Here's the part that stings. Most of these expenses felt completely reasonable 5 years ago. They made sense, they”
  - end: “finance on installment, every ghost membership you finally cancel this week, you're not being frugal, you're not depriving yourself, you're widening the gap. And the gap, tended carefully over time, is where every real f…” · sources: IRS; Federal Reserve; Company filings / earnings; Academic / research study
- **POV: You Retired at 45 — Nobody Knows** — [xB1N_Rrh44k](https://www.youtube.com/watch?v=xB1N_Rrh44k) · 2026-09-25 · 16.48 min · 533 views · PI 0.21 (Underperforming) · retirement_accounts_tax/pov_story · face=False · thumb text: “Bs”
  - 0-30s: “Saturday, 2:15 in the afternoon. You're standing in your sister's backyard, holding a paper plate with a burger that went cold 10 minutes ago. Still wearing the gray work pants you had on this morning, because a restaurant's main panel tripped at 7:00 a.m. and nobody else could get there. There are blue and gold balloons tied to the fence. A banner over the garage has your nephew Owen's name on it and the year”
  - end: “years that later matters. If you're 19 right now, or 29, or 45 and feeling like you started too late, Make your own envelopes. Pay later first. The amount matters much less than the habit. Tell me in the comments what yo…” · sources: Academic / research study
- **You Escaped the Rat Race In US. Nobody Noticed.** — [9IKQqagWkjE](https://www.youtube.com/watch?v=9IKQqagWkjE) · 2026-06-06 · 11.18 min · 186 views · PI 0.22 (Underperforming) · banking_cash/statement_other · face=True · thumb text: “nan”
  - 0-30s: “You are 34. Last night, Marcus sat across from you at your kitchen table and asked you how you did it. 10 years ago, you and Marcus were hired the same month, same company, same starting salary, same rung on the same ladder. Marcus had worked you on paper. He had the energy, the ambition, the handshake that made managers remember him. Last night, Marcus sat at your table with a coffee going cold in”
  - end: “you stop running it for people who weren't watching you anyway. Maybe you already know which direction the exit is. Maybe you already circled a date that no one else will ever see. If you do, keep it quiet. That's not a …”

## 7. Successful vs failed comparison
The reunion pair holds topic and script opening constant and changes the title (and likely thumbnail) — 1,000x difference (the confound is one week of channel momentum; INFERRED but the strongest packaging evidence in the dataset). Winners name a **specific scene + secret** ("10-Year Reunion as a Secret Multimillionaire"); losers name an abstract state ("Your Life After You Became a Millionaire").

| feature | upper half | lower half |
|---|---|---|
| t_number | 62% | 54% |
| t_dollar | 38% | 23% |
| t_question | 0% | 0% |
| t_you | 85% | 100% |
| t_fear_risk | 15% | 15% |
| t_urgency | 8% | 0% |
| t_secret_truth | 31% | 23% |
| t_named_entity | 0% | 0% |
| t_caps_word | 8% | 0% |
| t_year | 0% | 0% |
| h_first_sentence_q | 0% | 0% |
| h_you_in_30s | 100% | 100% |
| h_number_30s | 92% | 100% |
| h_dollar_30s | 23% | 46% |
| h_stakes_30s | 0% | 8% |
| h_contrarian_30s | 23% | 8% |
| h_open_loop_30s | 15% | 8% |
| h_promise_30s | 0% | 15% |
| h_story_open | 62% | 46% |
| h_greeting_open | 0% | 0% |
| h_first_person_30s | 8% | 0% |
| s_cta_end | 77% | 69% |
| tx_words (median) | 2,895 | 2,700 |
| s_num_density (median) | 2.65 | 2.86 |
| s_q_density (median) | 0.17 | 0.23 |
| s_but_density (median) | 0.18 | 0.21 |
| s_example_density (median) | 0.07 | 0.08 |
| s_data_density (median) | 0.75 | 0.95 |
| s_loop_density (median) | 0.00 | 0.00 |
| s_you_density (median) | 6.18 | 7.20 |
| s_wpm (median) | 178 | 176 |
| h_title_overlap_150 (median) | 0.22 | 0.25 |
| i_promise_pos (median) | 860 | 106 |
| t_len (median) | 63.00 | 58.00 |
| th_text_words (median) | 1.00 | 1.00 |
| th_colorfulness (median) | 39.19 | 49.26 |
| thumbnail has face | 46% | 69% |



## 8. Topic discovery and research sources
Fiction; cluster-circulated premises (lottery secrecy, retired-young secrecy).

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): Academic / research study 11, IRS 3, CBO / Treasury 3, Federal Reserve 1, Company filings / earnings 1
Description link domains: none
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
Rode the Oct 2026 POV lottery/secrecy wave; late copies weaker.

## 10. Thumbnail strategy
Montage not inspected; OCR near-empty (wordless scenes); faces in 46% of winners vs 69% of losers.

## 11. Title strategy
Winning: "POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire". Losing: "Your Life After You Became a Millionaire in Your 20s", "…In The US".

## 12. Hook and introduction strategy
Exact time + vehicle/object contrast; loss-before-windfall scenes.

## 13. Script and storytelling strategy
14-17 min literary second person.

## 14. Audience engagement model
Status-reveal anticipation.

## 15. Upload and publishing strategy
~6/month with a 93-day pause; Oct restart.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | 7 long-form ≥5x and 3 ≥10x own baseline; after 6 winners, next-10 uploads repeat the winner's topic 36% vs base rate 29% | **FOLLOWED** |  |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (pov_story, banking_cash) = 59% of uploads; explicit audience marker in 7% of titles | **PARTIALLY FOLLOWED** |  |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 2 title-format types each ≥10% of uploads (pov_story 69%, statement_other 21%, list_countdown 3%, news_change_update 3%) | **PARTIALLY FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 0% of videos; repeated title word-sets within channel 0% | **FOLLOWED** |  |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **NOT TESTABLE** |  |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 45% of titles share a word-set with another channel; this channel published first on 5 of 13 | **FOLLOWED** |  |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 14% of titles match a 100-format family; median PI with 0.82 (n=4) vs without 1.11 (n=22) | **NOT FOLLOWED** |  |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 62% of titles carry a number/$/named entity; median PI with 1.23 vs without 0.61 | **FOLLOWED** | the winning title names subject + situation + tension (reunion, secret multimillionaire), exactly the PDF five-part engine; the generic version failed. |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 0%; vague 'this/they' opener 0%; double-question 0% | **FOLLOWED** |  |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 17%; median share of thumbnail words repeated from title 0.00 | **INSUFFICIENT DATA** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 1.0 (OCR undercounts stylised text); face/character detected 59% (cartoon faces often missed) | **NOT TESTABLE** | montage not inspected. |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | opening ~75 words contain question/number/contradiction/story/you-hook in 100%; greeting/channel-intro opening 0% | **FOLLOWED** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | explicit stakes/why-it-matters language early in 7% | **NOT FOLLOWED** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | explicit open-loop/promise phrase in first ~150 words of 10% | **NOT FOLLOWED** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | bridge/cliffhanger phrases per 100 words (median) 0.000 | **NOT FOLLOWED** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | data/citation terms per 100 words 0.78; videos naming an institution/source 55% | **PARTIALLY FOLLOWED** |  |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | 'you/your' per 100 words (median) 6.85 | **FOLLOWED** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | next-video tease in final ~60 words 14%; any CTA in final 10% 76% | **PARTIALLY FOLLOWED** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 15.7 min; Spearman(duration, PI) 0.64 — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | median gap 1.0 d, gap CV 3.68, longest pause 93 d | **NOT FOLLOWED** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | spread of median PI across topics 2.58x (best wealth_psychology_habits) vs across title formats 1.15x (best statement_other) | **CONTRADICTED BY EVIDENCE** | in the reunion pair, topic and script were constant and the title/packaging changed the result. |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words 0.25 | **FOLLOWED** | same opening, but only the specific title made a promise the opening confirmed. |

## 17. Strengths and weaknesses
Learned from a flop within a week; vivid scenes. Weaknesses: copies of cluster titles, keyword stuffing early.

## 18. Replicable working model
**"Specific Scene + Secret"** POVs; retitle a flopped story with a concrete situation.

## 19. What to copy
Concrete-scene secret titles; repackaging a failed video's story.

## 20. What not to copy
Abstract "your life after…" titles; verbatim cluster titles; "In US" stuffing.

## 21. Missing evidence and limitations
Thumbnails not inspected; one-week confound in the pair.

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
1) Small channel that hit by reframing the same story with a specific, secret-laden title. 2) Advantage: fast iteration. 3) Model: scene + secret POV. 4) Topic: status reveals. 5) Packaging: concrete situation titles. 6) Script: literary. 7) Interest: vindication at a reunion. 8) Failures: abstract titles, copies. 9) Learn: title specificity can be decisive when topic is held. 10) Don't copy: other channels' titles. 11) Repeatable: yes. 12) Reputation: none. 13) Lesson: **put the scene and the secret in the title.**
"If I wanted to build a channel like this, I would study 3L4Mypm3uWo against 07d35Lx5Kco and replicate: one vivid status scene, a title that names the place and the secret, and an opening that drops the viewer into that exact scene — retitling flops rather than abandoning good stories."
