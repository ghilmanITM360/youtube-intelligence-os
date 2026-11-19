# Forensic report 03: Monkey Economics

Stage 2, 2026-11-19. Scope: this channel only, from `finance_economics_complete.db` (read-only). Data builder: `build_data.py`. Classified video list: `data/monkey-economics_classified.csv`.

**Evidence labels:** VERIFIED = read from the DB or raw Apify file. INFERRED = our reading of a pattern. HYPOTHESIS = untested idea. NOT AVAILABLE = no data or media in this workspace. Views are public counts as of the pull dates (2026-11-17 to 2026-11-19). Shorts = duration <= 180 s. No view count proves a cause; there is no CTR or retention data.

# Part 1. Reading

## A. Reading of the channel (INFERRED)

Monkey Economics is a Shorts-first channel that later added a few long videos. Its 42 Shorts total 57.2M views (median 913,379; 18 of 42 above 1M; max 7.69M); its 18 long videos total only 446K (median 10,244, max 212K). The Shorts burst: 6 in April, 18 in May and 10 in June 2025 (34 of 42, 55.4M of the 57.2M Shorts views), then 2 in July, 5 in October 2025 and 1 in August 2026. Long videos came in 2026 (Jan to Apr, then 3 more since October). The channel's size is a Shorts story.

## B. Finance AND Economics coverage

- Economics-style concept explainers dominate the Shorts: How Bank Works (7.69M), Money Laundering (5.35M, finance), Golden Exchange (3.73M), Minimum Wage (3.31M), "Just Print More!" inflation (3.14M), How Tariff Works (2.62M), Recession (2.08M), Mortgage (2.07M). These are basic concept explainers: one question, one monkey cast, under a minute (37 to 58 s).
- Long-form: Debt/Fed/inflation (6 long, 3 of the 5 winners), jobs/career (2; "Stop Being Good at Your Job..." 212K is the long outlier, 20.7x median), personal finance (4, all 6K to 9K), trade (2), housing (1, 6.6K).
- Both Finance and Economics are covered, but finance-basics (bank, laundering, gold) and economics-basics (wages, inflation, tariffs) are both explained at beginner level.

## C. Winning and failing topics

- Long winners: Stop Being Good at Your Job (212K, 20.7x, breakout), How to Start a Business (44K), Everything Is About To Change On This Day (rare earths, 24.5K), Interest Rates Going Up Again (23.9K), New Inflation (21.5K). Most winners are timely (rare earth deadline, rates) or personal-career framed.
- Shorts winners cluster in the first month of the channel (2025-04-23 to 2025-05-21). They are the same format repeated: "Monkey Economics [Concept]".
- There are no long-form failures below 0.5x in videos older than 60 days, but the bar is low (median 10K). The 6K to 9K videos are personal-finance and housing/market explainers.
- Caution: a channel median of 10,244 means a 2x winner is only 20K views. This channel's long-form data is a weak model for a new channel's ceiling; its Shorts data is the useful signal.

## D. Title structures

- Shorts: "Monkey Economics [Concept]" ("How Bank Work", "Minimum Wage", "Ressesion", sic). Plain, un-hooked, with typos. Nothing about the title seems to drive the views; the format and animation are the likely drivers. HYPOTHESIS.
- Long: "..." trailing ellipsis in 6 of 18 (33%, median 16.8K vs 7.5K); second-person ("Stop Being Good at Your Job...", "Why Your Job is a Trap...") in 22%, median 16.8K vs 9.0K; digit titles 28%, median 8.9K.
- No question marks. 7-word median.

## E. Thumbnail patterns

Source: our 11-image sample (thumbnail model doc, viewed 2026-11-19): monkey character in a jungle-office world, white or dark ground, 2 to 4 word text. Shorts thumbnails are vertical frames. INFERRED; no CTR.

## F. Script and hook structure (VERIFIED text, INFERRED structure)

Two scripting styles. (1) Short-form and early long: simplified "Monkey Island have big problem... Monkey government say easy just print more leaves" — broken-English narration of a monkey-economy parable; the concept is explained in a story. (2) 2026 long videos: standard narrated explainers ("Chinese monkeys makes more than 31% of everything manufactured on Earth... that's about to change on November 10..."). A deadline-driven hook ("By the end of this video, you'll know exactly where oil is hiding") appears in the inflation video. The list video "Loopholes that are banned forever.." opens "Number one, ..." straight into item one with no preamble.

## G. Visual storytelling and editing

NOT AVAILABLE. No video files were analysed; transcripts show narration only. Not claimed.

## H. Shorts vs long-form and frequency

- Shorts median 913K vs long median 10K: a 89x gap. The April to June 2025 burst (34 Shorts) produced 55.4M of the 57.2M Shorts views.
- Cadence collapsed: 0.74 uploads/week whole history (0.52 Shorts), but only 3 uploads in the last 90 days. The last Shorts batch was 2025-10; one Short in 2026-08.
- Does Shorts virality convert to long-form? The channel's long median is 10K with the Shorts at ~1M, so in this sample it did not convert. INFERRED from two numbers; no analytics.
- Subscribers data in DB lets Shorts reach be compared; not done in Stage 2.

## I. Implications for our channel (HYPOTHESIS)

1. Concept-explainer Shorts of one basic economics question can reach seven figures, but this does not transfer to long-form views. 2. A Shorts-first plan would need a separate audience-to-long bridge that this channel did not build. 3. Do not model long-form ambitions on this channel.

## J. Limits

DB has all 60 reported. Shorts dated by Apify R2. Views as of the pull dates. No subscriber-conversion data.


# Part 2. Data tables

## 1. Full inventory (VERIFIED from DB)

- Videos held: **60** (long-form 18, Shorts 42 by duration <= 180 s). Date range 2025-04-23 to 2026-11-09.
- With public view counts: 60. Transcripts held: 60 of 60.
- Views, long-form: total 446,143, median 10,244, mean 24,785, max 211,692.
- Views, Shorts: total 57,225,439, median 913,379, max 7,690,991.
- Median long-form duration: 8 min 10 s.

## 2. Top videos

### Top 15 long-form
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 211,692 | 2026-04-01 | 8:38 | Jobs, wages & labour | [Stop Being Good at Your Job...](https://www.youtube.com/watch?v=GkJCXwm7Ous) |
| 2 | 43,845 | 2025-06-07 | 4:15 | Debt, Fed & inflation | [Monkey Economics - How to Start a Business](https://www.youtube.com/watch?v=QZdM9DlrMTE) |
| 3 | 24,508 | 2026-11-09 | 10:00 | Trade, tariffs & geopolitics | [Everything Is About To Change On This Day](https://www.youtube.com/watch?v=UNzjgBbmt3o) |
| 4 | 23,933 | 2026-10-13 | 9:55 | Debt, Fed & inflation | [The Interest Rates Are Going Up Again...](https://www.youtube.com/watch?v=ePES31n6NV8) |
| 5 | 21,531 | 2026-10-25 | 12:00 | Debt, Fed & inflation | [The New Inflation Is Here... And You Dont Even Know it Yet](https://www.youtube.com/watch?v=HCOr-nryE0Y) |
| 6 | 17,331 | 2025-06-12 | 16:09 | Debt, Fed & inflation | [Monkey Economics Compilation Part 1](https://www.youtube.com/watch?v=-BqoR3LbfkU) |
| 7 | 15,505 | 2026-04-21 | 8:28 | Other / unclassified | [Loopholes that are banned forever..](https://www.youtube.com/watch?v=krWeHgin-E0) |
| 8 | 11,997 | 2026-04-18 | 9:01 | Jobs, wages & labour | [Why Your Job is a Trap...](https://www.youtube.com/watch?v=AhpAwRg79zo) |
| 9 | 11,420 | 2026-01-04 | 5:18 | Crashes, recessions & crises | [Oversimplified The Great Depression in 5 mins](https://www.youtube.com/watch?v=97owJXL-8rg) |
| 10 | 9,069 | 2026-01-28 | 6:14 | Government, politics & policy | [The Government Situation Right Now...](https://www.youtube.com/watch?v=awOgsY9IMbk) |
| 11 | 8,936 | 2026-04-05 | 9:39 | Personal finance & consumer | [The 5 Money Traps 99% of Monkeys Fall Into...](https://www.youtube.com/watch?v=yDaa-Ael_jU) |
| 12 | 7,983 | 2026-02-17 | 6:05 | Trade, tariffs & geopolitics | [It was never about Oil or Gold..](https://www.youtube.com/watch?v=2JzM2q-Y3qE) |
| 13 | 7,027 | 2026-03-25 | 10:25 | Personal finance & consumer | [Every Way To Get Rich In 2026 Explained By Monkeys](https://www.youtube.com/watch?v=TlItPXhiwfg) |
| 14 | 6,590 | 2026-04-08 | 7:52 | Housing & real estate | [Why No One Can Buy Homes Anymore](https://www.youtube.com/watch?v=TD0d55zLohw) |
| 15 | 6,543 | 2026-03-22 | 7:48 | Personal finance & consumer | [Monkey Explains EVERY level of Wealth Explain](https://www.youtube.com/watch?v=oyLEGSHpif4) |

### Top 8 Shorts
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 7,690,991 | 2025-04-28 | 0:49 | Jobs, wages & labour | [Monkey Economics How Bank Work](https://www.youtube.com/shorts/rWbZwFnI7dQ) |
| 2 | 5,351,485 | 2025-05-21 | 0:49 | Debt, Fed & inflation | [Monkey Economic Money Laundring](https://www.youtube.com/shorts/dyzgdD_kk1o) |
| 3 | 3,727,416 | 2025-05-04 | 0:48 | Debt, Fed & inflation | [Monkey Economics Golden Exchange](https://www.youtube.com/shorts/ARVgtRiCE_w) |
| 4 | 3,309,333 | 2025-05-02 | 0:42 | Jobs, wages & labour | [Monkey Economics Minimum Wage](https://www.youtube.com/shorts/2IO49htPrQg) |
| 5 | 3,138,340 | 2025-04-25 | 0:58 | Debt, Fed & inflation | [Monkey Economics Just Print More! - Inflation](https://www.youtube.com/shorts/Jdl13JwUuRM) |
| 6 | 2,618,729 | 2025-04-26 | 0:37 | Trade, tariffs & geopolitics | [Monkey Economics How Tariff Works](https://www.youtube.com/shorts/c_ipt9C1Gas) |
| 7 | 2,079,637 | 2025-04-23 | 0:45 | Debt, Fed & inflation | [Monkey Economics Ressesion](https://www.youtube.com/shorts/mXNp2L9QR2c) |
| 8 | 2,070,053 | 2025-05-01 | 0:45 | Housing & real estate | [Monkey Economics How Bank Mortgage Works](https://www.youtube.com/shorts/2Ven3O_l_ew) |

## 3. Recent uploads (newest 12, any type)

| Date | Type | Views | Age (d) | Title |
|---|---|---:|---:|---|
| 2026-11-09 | Long | 24,508 | 10 | Everything Is About To Change On This Day |
| 2026-10-25 | Long | 21,531 | 25 | The New Inflation Is Here... And You Dont Even Know it Yet |
| 2026-10-13 | Long | 23,933 | 37 | The Interest Rates Are Going Up Again... |
| 2026-08-05 | Short | 30,325 | 106 | Bank vs Credit Union |
| 2026-04-21 | Long | 15,505 | 212 | Loopholes that are banned forever.. |
| 2026-04-18 | Long | 11,997 | 215 | Why Your Job is a Trap... |
| 2026-04-08 | Long | 6,590 | 225 | Why No One Can Buy Homes Anymore |
| 2026-04-05 | Long | 8,936 | 228 | The 5 Money Traps 99% of Monkeys Fall Into... |
| 2026-04-01 | Long | 211,692 | 232 | Stop Being Good at Your Job... |
| 2026-03-28 | Long | 6,178 | 236 | Stock Market Explain with Bananas |
| 2026-03-25 | Long | 7,027 | 239 | Every Way To Get Rich In 2026 Explained By Monkeys |
| 2026-03-22 | Long | 6,543 | 242 | Monkey Explains EVERY level of Wealth Explain |

## 4. 30 / 60 / 90-day patterns (to 2026-11-19)

| Window | Uploads | Long | Shorts | Long views median | Long views total | Per week |
|---|---:|---:|---:|---:|---:|---:|
| last 30 d | 2 | 2 | 0 | 23,019 | 46,039 | 0.5 |
| last 60 d | 3 | 3 | 0 | 23,933 | 69,972 | 0.4 |
| last 90 d | 3 | 3 | 0 | 23,933 | 69,972 | 0.2 |
| last 180 d | 4 | 3 | 1 | 23,933 | 69,972 | 0.2 |
| last 365 d | 17 | 16 | 1 | 9,002 | 384,967 | 0.3 |

Monthly uploads (last 14 active months): 2025-04: 0L/6S; 2025-05: 0L/18S; 2025-06: 2L/10S; 2025-07: 0L/2S; 2025-10: 0L/5S; 2026-01: 2L/0S; 2026-02: 1L/0S; 2026-03: 5L/0S; 2026-04: 5L/0S; 2026-08: 0L/1S; 2026-10: 2L/0S; 2026-11: 1L/0S

Long-form upload weekday: Wed 5, Sun 4, Tue 3, Sat 3, Thu 2, Mon 1

## 5. Finance / Economics categories and sub-niche distribution

Classification: title-keyword rules (`build_data.py`), then **audited by reading the titles** (section 9). Labels are INFERRED, not channel-declared.

| Sub-niche | F/E | Long n | Long median views | x channel median | Long total views | Shorts n |
|---|---|---:|---:|---:|---:|---:|
| Jobs, wages & labour | Economics | 2 | 111,844 | 10.92 | 223,689 | 4 |
| Debt, Fed & inflation | Economics | 5 | 21,531 | 2.10 | 112,436 | 30 |
| Trade, tariffs & geopolitics | Economics | 2 | 16,245 | 1.59 | 32,491 | 2 |
| Personal finance & consumer | Finance | 4 | 6,785 | 0.66 | 28,765 | 1 |
| Other / unclassified | Unclassified | 1 | 15,505 | 1.51 | 15,505 | 1 |
| Crashes, recessions & crises | Finance | 1 | 11,420 | 1.11 | 11,420 | 1 |
| Government, politics & policy | Economics | 1 | 9,069 | 0.89 | 9,069 | 1 |
| Housing & real estate | Economics | 1 | 6,590 | 0.64 | 6,590 | 1 |
| Investing, stocks & crypto | Finance | 1 | 6,178 | 0.60 | 6,178 | 1 |

Finance vs Economics (long-form, public views): Economics: 11 videos / 384,275 views; Finance: 6 videos / 46,363 views; Unclassified: 1 videos / 15,505 views

## 6. Winning and failing topics (long-form, relative to channel long median 10,244)

- Winners (>= 2x median): **5** of 18; breakouts (>= 5x): **1**; failures (<= 0.5x, older than 60 d): **0** of 15.
- Winners by sub-niche: Debt, Fed & inflation 3; Jobs, wages & labour 1; Trade, tariffs & geopolitics 1.
- Failures by sub-niche: none.

Breakouts:

- 211,692 (20.7x) 2026-04-01 [Stop Being Good at Your Job...](https://www.youtube.com/watch?v=GkJCXwm7Ous)

Lowest long-form (older than 60 d):

- 5,796 (0.57x) 2026-03-12 [Why Gold Always Go Up Explained With Bananas](https://www.youtube.com/watch?v=Y0aFpODhcXc)
- 6,178 (0.60x) 2026-03-28 [Stock Market Explain with Bananas](https://www.youtube.com/watch?v=M_VyQyd8q38)
- 6,259 (0.61x) 2026-03-18 [How EVERYTHING changes After you save $10,000](https://www.youtube.com/watch?v=Ok84V8uQgeI)
- 6,543 (0.64x) 2026-03-22 [Monkey Explains EVERY level of Wealth Explain](https://www.youtube.com/watch?v=oyLEGSHpif4)
- 6,590 (0.64x) 2026-04-08 [Why No One Can Buy Homes Anymore](https://www.youtube.com/watch?v=TD0d55zLohw)
- 7,027 (0.69x) 2026-03-25 [Every Way To Get Rich In 2026 Explained By Monkeys](https://www.youtube.com/watch?v=TlItPXhiwfg)
- 7,983 (0.78x) 2026-02-17 [It was never about Oil or Gold..](https://www.youtube.com/watch?v=2JzM2q-Y3qE)
- 8,936 (0.87x) 2026-04-05 [The 5 Money Traps 99% of Monkeys Fall Into...](https://www.youtube.com/watch?v=yDaa-Ael_jU)

## 7. Title structures (long-form)

| Feature | Share of long titles | Median views with | Median views without |
|---|---:|---:|---:|
| Question mark | 0% | 0 | 10,244 |
| Contains a digit | 28% | 8,936 | 11,997 |
| Colon | 0% | 0 | 10,244 |
| Ellipsis | 33% | 16,764 | 7,505 |
| ALL-CAPS word | 11% | 6,401 | 11,708 |
| Year | 6% | 7,027 | 11,420 |
| Starts with how/why/what/is… | 22% | 6,424 | 13,462 |
| Addresses you/we | 22% | 16,764 | 9,002 |
| Negative/threat word | 17% | 7,983 | 11,420 |

Median title length 7 words (top-10 median 6). Feature medians are descriptive; they do not show causation.

## 8. Shorts vs long-form and upload frequency

- Long-form: 18 items, median views 10,244. Shorts: 42 items, median views 913,379.
- Whole-history cadence: 0.74 uploads/week (0.22 long, 0.52 Shorts) over 565 days.

## 9. Hook data (first ~60 words of transcript, top 8 long-form)

- **Stop Being Good at Your Job...** (211,692): "Monkey walks through the jungle office, carrying stacks of leaves and papers. Monkey finishes tasks, fixes problems, and helps other monkeys. Monkey feels like everything is going right, but what if doing everything right is exactly what monkey is doing wrong? And that's what is keeping monkey trapped. The beginning. Monkey becomes very good at the jungle job, but monkey"
- **Monkey Economics - How to Start a Business** (43,845): "Monkey Boss tried getting a job, but job is not it for Monkey Boss. Monkey Boss worked for 10 hours, but only got paid with Tiny Leaf. Monkey Boss says jobs are lowpaying and work long hours for other Monkey Boss. So, Monkey Boss goes and starts his own business. If Boss Monkey wants to make millions of leaves, Boss"
- **Everything Is About To Change On This Day** (24,508): "Chinese monkeys makes more than 31% of everything manufactured on Earth. And that's a big part of why so much of monkey stuff is so cheap. But that's about to change on November 10 because China's temporary pause on certain rare earth export controls is set to expire. Rare earth minerals are used to make everything from smartphones to powerful"
- **The Interest Rates Are Going Up Again...** (23,933): "Monkey might think the biggest threat to a paycheck right now is a barista up charging for oat milk or the crypto market crashing again. But the real threat to what monkey pays every month on a treehouse loan, a car loan, or a credit card has nothing to do with lattes. It's sitting quietly inside a marble building in"
- **The New Inflation Is Here... And You Dont Even Know it Yet** (21,531): "You've seen the number at the pump go up. What you haven't seen is how it hides in your everyday items. It's baked into your bread, tucked into your plane, and even sitting inside your mortgage rate. By the end of this video, you'll know exactly where oil is hiding and why the number everyone quotes is barely telling half"
- **Monkey Economics Compilation Part 1** (17,331): "Monkey Island have big problem. Monkey government broke. Monkey government say easy just print more leaves. Prin or go. Now monkeys have lots of leaves. Monkeys feel rich. Monkeys buy house, buy car, buy a lots of bananas. But banana farmers say, "I didn't grow more bananas. Only the same bananas as last year, but now too many monkeys can"
- **Loopholes that are banned forever..** (15,505): "Number one, the monkeys who exploited the lottery system. Most monkeys buy lottery tickets and lose leaves every single time. But a group of very smart monkeys in Massachusetts found a lottery where buying enough tickets almost guaranteed a profit. The lottery was called cash windfall and it had a strange rule called a roll down. The top prize was"
- **Why Your Job is a Trap...** (11,997): "If monkey doesn't find a way to make leaves while monkey sleeps, monkey will work until monkey dies. This is not a motivational quote. This is a warning about monkey's future. Welcome to the most dangerous trap in the jungle. Monkey calls it the employee trap. Most monkeys watching this video are currently selling the only asset that monkey cannot"

## 10. Title audit list (all items with assigned sub-niche)

<details><summary>Show all 60 titles</summary>

| Date | T | Views | Sub-niche | Title |
|---|---|---:|---|---|
| 2026-11-09 | L | 24,508 | Trade, tariffs & geopolitics | Everything Is About To Change On This Day |
| 2026-10-25 | L | 21,531 | Debt, Fed & inflation | The New Inflation Is Here... And You Dont Even Know it Yet |
| 2026-10-13 | L | 23,933 | Debt, Fed & inflation | The Interest Rates Are Going Up Again... |
| 2026-08-05 | S | 30,325 | Investing, stocks & crypto | Bank vs Credit Union |
| 2026-04-21 | L | 15,505 | Other / unclassified | Loopholes that are banned forever.. |
| 2026-04-18 | L | 11,997 | Jobs, wages & labour | Why Your Job is a Trap... |
| 2026-04-08 | L | 6,590 | Housing & real estate | Why No One Can Buy Homes Anymore |
| 2026-04-05 | L | 8,936 | Personal finance & consumer | The 5 Money Traps 99% of Monkeys Fall Into... |
| 2026-04-01 | L | 211,692 | Jobs, wages & labour | Stop Being Good at Your Job... |
| 2026-03-28 | L | 6,178 | Investing, stocks & crypto | Stock Market Explain with Bananas |
| 2026-03-25 | L | 7,027 | Personal finance & consumer | Every Way To Get Rich In 2026 Explained By Monkeys |
| 2026-03-22 | L | 6,543 | Personal finance & consumer | Monkey Explains EVERY level of Wealth Explain |
| 2026-03-18 | L | 6,259 | Personal finance & consumer | How EVERYTHING changes After you save $10,000 |
| 2026-03-12 | L | 5,796 | Debt, Fed & inflation | Why Gold Always Go Up Explained With Bananas |
| 2026-02-17 | L | 7,983 | Trade, tariffs & geopolitics | It was never about Oil or Gold.. |
| 2026-01-28 | L | 9,069 | Government, politics & policy | The Government Situation Right Now... |
| 2026-01-04 | L | 11,420 | Crashes, recessions & crises | Oversimplified The Great Depression in 5 mins |
| 2025-10-30 | S | 50,560 | Government, politics & policy | Monkey Explains Gov Shutdown |
| 2025-10-22 | S | 81,404 | Other / unclassified | Monkey Explains Prohibition |
| 2025-10-17 | S | 301,294 | Personal finance & consumer | Monkey Explain How to Build Credit |
| 2025-10-15 | S | 377,620 | Debt, Fed & inflation | Monkey Economics Diamond Economics |
| 2025-10-14 | S | 131,759 | Debt, Fed & inflation | Monkey Economics Debt Ceiling |
| 2025-07-05 | S | 332,164 | Debt, Fed & inflation | Monkey Economics Insurance Thing |
| 2025-07-01 | S | 553,631 | Debt, Fed & inflation | Monkey Economics Cartel |
| 2025-06-28 | S | 709,062 | Debt, Fed & inflation | Monkey Economics Communist |
| 2025-06-27 | S | 684,741 | Debt, Fed & inflation | Monkey Economics Government Bailout |
| 2025-06-25 | S | 542,058 | Debt, Fed & inflation | Monkey Economics Charity |
| 2025-06-24 | S | 745,289 | Debt, Fed & inflation | Monkey Economics Insider monkey |
| 2025-06-23 | S | 1,675,716 | Debt, Fed & inflation | Monkey Economics Tax Write Off |
| 2025-06-21 | S | 396,425 | Debt, Fed & inflation | Monkey Economics Tax Evasion |
| 2025-06-18 | S | 453,567 | Debt, Fed & inflation | Monkey Economic Capitalism |
| 2025-06-16 | S | 678,644 | Jobs, wages & labour | Monkey Economics Pension |
| 2025-06-15 | S | 826,946 | Debt, Fed & inflation | Monkey Economics Disability |
| 2025-06-13 | S | 964,232 | Debt, Fed & inflation | Monkey Economics Social Security |
| 2025-06-12 | L | 17,331 | Debt, Fed & inflation | Monkey Economics Compilation Part 1 |
| 2025-06-07 | L | 43,845 | Debt, Fed & inflation | Monkey Economics - How to Start a Business |
| 2025-05-31 | S | 896,097 | Debt, Fed & inflation | Monkey Economics Credit Card |
| 2025-05-30 | S | 609,391 | Debt, Fed & inflation | Monkey Economics Insurance |
| 2025-05-28 | S | 932,145 | Jobs, wages & labour | Monkey Economics Ghost Jobs |
| 2025-05-27 | S | 1,025,218 | Debt, Fed & inflation | Monkey Economics Capital Gain Tax |
| 2025-05-24 | S | 1,607,220 | Debt, Fed & inflation | Monkey Economics Taxes |
| 2025-05-21 | S | 5,351,485 | Debt, Fed & inflation | Monkey Economic Money Laundring |
| 2025-05-20 | S | 899,507 | Debt, Fed & inflation | Monkey Economics Treasury Bonds |
| 2025-05-19 | S | 1,050,661 | Debt, Fed & inflation | Monkey Economics Federal Reserve Bank |
| 2025-05-15 | S | 464,017 | Debt, Fed & inflation | Monkey Economics How Bank Inflation works |
| 2025-05-13 | S | 1,715,832 | Debt, Fed & inflation | Monkey Economics Monopoly |
| 2025-05-10 | S | 1,494,388 | Debt, Fed & inflation | Monkey Economics Union and Strike |
| 2025-05-08 | S | 1,279,584 | Debt, Fed & inflation | Monkeys Economics Shortage and Surplus |
| 2025-05-07 | S | 927,252 | Crashes, recessions & crises | Monkey Economics Bank Crash |
| 2025-05-05 | S | 1,542,108 | Debt, Fed & inflation | Monkey Economics Competition |
| 2025-05-05 | S | 1,785,132 | Debt, Fed & inflation | Monkey Economics Ponzi Scheme |
| 2025-05-04 | S | 3,727,416 | Debt, Fed & inflation | Monkey Economics Golden Exchange |
| 2025-05-02 | S | 3,309,333 | Jobs, wages & labour | Monkey Economics Minimum Wage |
| 2025-05-01 | S | 2,070,053 | Housing & real estate | Monkey Economics How Bank Mortgage Works |
| 2025-04-29 | S | 1,413,689 | Debt, Fed & inflation | Monkey Economics How Crypto Works |
| 2025-04-28 | S | 7,690,991 | Jobs, wages & labour | Monkey Economics How Bank Work |
| 2025-04-27 | S | 61,777 | Trade, tariffs & geopolitics | Monkey Economics - Tariff |
| 2025-04-26 | S | 2,618,729 | Trade, tariffs & geopolitics | Monkey Economics How Tariff Works |
| 2025-04-25 | S | 3,138,340 | Debt, Fed & inflation | Monkey Economics Just Print More! - Inflation |
| 2025-04-23 | S | 2,079,637 | Debt, Fed & inflation | Monkey Economics Ressesion |

</details>

