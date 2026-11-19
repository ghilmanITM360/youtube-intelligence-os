# Forensic report 04: Crayon Capital

Stage 2, 2026-11-19. Scope: this channel only, from `finance_economics_complete.db` (read-only). Data builder: `build_data.py`. Classified video list: `data/crayon-capital_classified.csv`.

**Evidence labels:** VERIFIED = read from the DB or raw Apify file. INFERRED = our reading of a pattern. HYPOTHESIS = untested idea. NOT AVAILABLE = no data or media in this workspace. Views are public counts as of the pull dates (2026-11-17 to 2026-11-19). Shorts = duration <= 180 s. No view count proves a cause; there is no CTR or retention data.

# Part 1. Reading

## A. Reading of the channel (INFERRED)

Crayon Capital is a long-form story channel (35 videos, 21.7M views, median 301,336, 15 min 18 s), no Shorts. It tells company, person and crisis stories as dramatised histories, using an "Explained Like You're 5" template for 21 titles (median 301K). Three breakouts: Wolf of Wall Street scam (4.22M, 14.0x), Great Depression (2.76M, 9.2x), 2008 Financial Crisis (2.29M, 7.6x).

## B. Finance AND Economics coverage

- Finance (27 long, 19.8M views): companies/billionaires (12 long, median 209K: Rockefeller 1.33M, Amazon 1.01M, Enron 920K, Theranos 372K, but also JP Morgan 303K, Steve Jobs 246K, PayPal, TSMC, Ozempic ~104K to 109K, BYD 98K), AI companies (6, median 569K: Anthropic 1.12M, Palantir 872K, NVIDIA 585K and 553K, AI bubble 438K), crashes (4: Great Depression 2.76M, 2008 2.29M, Dot-com 393K, Every Financial Crisis 69K), scams/markets (4: Wolf of Wall Street 4.22M, Margin Call 301K, $65B scam 207K, Bitcoin 118K).
- Economics (6 long, 1.8M views): trade/geopolitics (3: Singapore 974K, Xi 244K, Iran War 162K), money (3: Petrodollar 255K, 5000 Years of Gold 155K, WW2 economy 50K).
- Economics coverage is mostly HISTORICAL (Depression, 2008, petrodollar). It is not about this week's data release.

## C. Winning and failing topics

- 9 winners, 3 breakouts, 9 failures out of 30 older videos. Winners: scandals with a known villain (Wolf, Enron, Theranos), crisis history, AI companies in the 2026 hype cycle, Rockefeller/Bezos as origin stories.
- Failures (9, all <= 0.5x): BYD (98K), Ozempic (103K), TSMC (104K), PayPal (109K) in company history; Epstein (49K) and "Greatest Slave System" (41K) in non-finance; "Economic Secret of WW2" (50K); "Every Financial Crisis in 10 Minutes" (69K). The weak pattern is a single company the audience does not already know, or a niche history item; titles that name a famous villain or a famous crisis win. Note the crisis row has both a 2.76M winner and a 69K failure, so "crisis" alone is not enough.
- Both the top and bottom are within the same template, so the "Explained Like You're 5" label is not the differentiator; the SUBJECT'S fame is. INFERRED.

## D. Title structures

- 71% contain a digit (e.g. "$63 BILLION", "5", "5000 Years"); digit titles have lower median (255K vs 386K); same caution as elsewhere.
- 57% address "you/we"; "Explained Like You're 5" is the template (21 titles). Colon titles are rare (9%: "Rockefeller: The First Confirmed Billionaire (And How He Did It)").
- Stock phrases: "Actually" (4 titles; "How Jeff Bezos Actually Built Amazon", median 209K), "The $X BILLION Company That Sold Nothing".
- No question marks, no ellipsis, no years. 7 words median.

## E. Thumbnail patterns

Source: 9-image sample (thumbnail model doc): large hand-drawn cinematic character on a dark warm background, one name or one number, bow-tie boy mascot. INFERRED.

## F. Script and hook structure (VERIFIED text, INFERRED structure)

Strong, consistent 4-step opening: (1) a shocking fact or claim in the first sentence ("He lied about $1 stock, made millions, and only served 22 months in jail." / "You woke up rich, then went to bed broke."); (2) the stakes in numbers ($600 billion, 90% of America's oil); (3) "This is the story of [name]"; (4) a dated scene start ("Bayside, Queens, 1962", "September 2008", "July 8th, 1839"). Then a chronological story with a rising tension and an ending explaining the consequence. This is the channel's repeatable script spine. Music cues are marked in the transcript.

## G. Visual storytelling and editing

NOT AVAILABLE (no video files analysed). From transcript: dated scene-setting, character-driven narration, music cues. Illustration style only from thumbnails.

## H. Shorts vs long-form and frequency

No Shorts. 35 long videos over 571 days = 0.43 a week, i.e. about one every 2.3 weeks historically, and 1 to 3 a month in 2026 (3 in August and October). Saturday is the most frequent upload day (11 of 35). Last 90 days: 7 videos, median 303K. Output is flat and low, and the channel still holds a 301K median, which is evidence that a low cadence can sustain 300K median if every video has a famous-subject hook.

## I. Implications for our channel (HYPOTHESIS)

1. Crisis history (Depression, 2008) are huge, but evergreen explainers made by many channels. 2. A repeatable 4-step opening (fact, stakes, story, dated scene) is a script pattern we can adapt (structure only). 3. Company stories work when the subject is famous. 4. The channel is not Economics-data driven; our "number behind the price" angle is not covered here, so it is a gap, not a copy.

## J. Limits

35 of 35 reported are held. No media analysis; no subscriber conversion data.


# Part 2. Data tables

## 1. Full inventory (VERIFIED from DB)

- Videos held: **35** (long-form 35, Shorts 0 by duration <= 180 s). Date range 2025-04-22 to 2026-11-14.
- With public view counts: 35. Transcripts held: 35 of 35.
- Views, long-form: total 21,708,190, median 301,336, mean 620,234, max 4,219,017.
- Median long-form duration: 15 min 18 s.

## 2. Top videos

### Top 15 long-form
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 4,219,017 | 2025-10-03 | 16:33 | Investing, stocks & crypto | [The Wolf of Wall Street Scam Explained Like You're 5](https://www.youtube.com/watch?v=HawmGu7oNrc) |
| 2 | 2,762,821 | 2025-08-15 | 16:29 | Crashes, recessions & crises | [The Great Depression Explained Like You’re 5](https://www.youtube.com/watch?v=LuEcoqizj0o) |
| 3 | 2,285,772 | 2025-06-15 | 13:26 | Crashes, recessions & crises | [The 2008 Financial Crisis Explained Like You’re 5](https://www.youtube.com/watch?v=KE-WJevx-7c) |
| 4 | 1,326,122 | 2026-02-28 | 20:16 | Companies, billionaires & business history | [Rockefeller: The First Confirmed Billionaire (And How He Did It)](https://www.youtube.com/watch?v=sMH8WchxQR8) |
| 5 | 1,116,354 | 2026-10-16 | 17:50 | AI & tech bubble | [The Rise of Anthropic Explained Like You're 5](https://www.youtube.com/watch?v=H5GYXhpE5yI) |
| 6 | 1,006,867 | 2025-11-28 | 20:13 | Companies, billionaires & business history | [How Jeff Bezos Actually Built Amazon](https://www.youtube.com/watch?v=rSgS4wNLLDM) |
| 7 | 973,784 | 2025-12-27 | 16:08 | Trade, tariffs & geopolitics | [The Man Who Built Singapore in One Generation](https://www.youtube.com/watch?v=y51JjcymEAY) |
| 8 | 920,247 | 2025-07-19 | 13:12 | Companies, billionaires & business history | [The $63 BILLION Company That Sold Nothing](https://www.youtube.com/watch?v=VSbO8vmZNm0) |
| 9 | 871,891 | 2026-01-10 | 15:18 | AI & tech bubble | [Palantir Technologies Explained Like You’re 5](https://www.youtube.com/watch?v=GSkySDNmjV8) |
| 10 | 584,655 | 2026-07-09 | 14:30 | AI & tech bubble | [NVIDIA Explained Like You're 5](https://www.youtube.com/watch?v=1GowFTjbUnk) |
| 11 | 552,544 | 2026-11-14 | 14:30 | AI & tech bubble | [NVIDIA Scandal Explained Like You're 5](https://www.youtube.com/watch?v=eS1zZKHFzwE) |
| 12 | 469,938 | 2026-10-06 | 18:45 | AI & tech bubble | [The First Big Victim of the AI Bubble](https://www.youtube.com/watch?v=6X0ib0Jt9cs) |
| 13 | 469,234 | 2026-03-09 | 20:28 | Personal finance & consumer | [The Worst Time to be Rich as a Human](https://www.youtube.com/watch?v=wOjdbltaXSQ) |
| 14 | 438,100 | 2025-12-12 | 12:13 | AI & tech bubble | [The AI Bubble Explained Like You're 5](https://www.youtube.com/watch?v=kx_okFl98Vw) |
| 15 | 392,754 | 2025-10-27 | 12:08 | Crashes, recessions & crises | [The Dot-Com Bubble Explained Like You're 5](https://www.youtube.com/watch?v=CCXYfrAfW6g) |

## 3. Recent uploads (newest 12, any type)

| Date | Type | Views | Age (d) | Title |
|---|---|---:|---:|---|
| 2026-11-14 | Long | 552,544 | 5 | NVIDIA Scandal Explained Like You're 5 |
| 2026-11-10 | Long | 302,952 | 9 | J.P. Morgan: The Most Powerful Man in America |
| 2026-10-31 | Long | 246,037 | 19 | How Steve Jobs Actually Built Apple |
| 2026-10-16 | Long | 1,116,354 | 34 | The Rise of Anthropic Explained Like You're 5 |
| 2026-10-06 | Long | 469,938 | 44 | The First Big Victim of the AI Bubble |
| 2026-09-09 | Long | 98,218 | 71 | How BYD Actually Beat Tesla |
| 2026-08-22 | Long | 103,771 | 89 | TSMC Explained Like You're 5 |
| 2026-08-11 | Long | 171,778 | 100 | How Elon Musk Actually Became a Trillionaire |
| 2026-08-01 | Long | 103,452 | 110 | Ozempic Explained Like You're 5 |
| 2026-07-21 | Long | 48,867 | 121 | Epstein Situation Explained Like You're 5 |
| 2026-07-09 | Long | 584,655 | 133 | NVIDIA Explained Like You're 5 |
| 2026-06-28 | Long | 40,623 | 144 | The Greatest Slave System Ever Created |

## 4. 30 / 60 / 90-day patterns (to 2026-11-19)

| Window | Uploads | Long | Shorts | Long views median | Long views total | Per week |
|---|---:|---:|---:|---:|---:|---:|
| last 30 d | 3 | 3 | 0 | 302,952 | 1,101,533 | 0.7 |
| last 60 d | 5 | 5 | 0 | 469,938 | 2,687,825 | 0.6 |
| last 90 d | 7 | 7 | 0 | 302,952 | 2,889,814 | 0.5 |
| last 180 d | 14 | 14 | 0 | 165,251 | 4,047,804 | 0.5 |
| last 365 d | 25 | 25 | 0 | 254,882 | 10,251,666 | 0.5 |

Monthly uploads (last 14 active months): 2025-10: 2L/0S; 2025-11: 1L/0S; 2025-12: 2L/0S; 2026-01: 2L/0S; 2026-02: 2L/0S; 2026-03: 2L/0S; 2026-04: 2L/0S; 2026-05: 1L/0S; 2026-06: 2L/0S; 2026-07: 2L/0S; 2026-08: 3L/0S; 2026-09: 1L/0S; 2026-10: 3L/0S; 2026-11: 2L/0S

Long-form upload weekday: Sat 11, Tue 6, Fri 5, Mon 4, Sun 3, Wed 3, Thu 3

## 5. Finance / Economics categories and sub-niche distribution

Classification: title-keyword rules (`build_data.py`), then **audited by reading the titles** (section 9). Labels are INFERRED, not channel-declared.

| Sub-niche | F/E | Long n | Long median views | x channel median | Long total views | Shorts n |
|---|---|---:|---:|---:|---:|---:|
| Crashes, recessions & crises | Finance | 4 | 1,339,263 | 4.44 | 5,510,617 | 0 |
| Companies, billionaires & business history | Finance | 12 | 208,907 | 0.69 | 4,919,579 | 0 |
| Investing, stocks & crypto | Finance | 4 | 254,151 | 0.84 | 4,845,586 | 0 |
| AI & tech bubble | Finance | 6 | 568,599 | 1.89 | 4,033,482 | 0 |
| Trade, tariffs & geopolitics | Economics | 3 | 244,289 | 0.81 | 1,380,225 | 0 |
| Personal finance & consumer | Finance | 1 | 469,234 | 1.56 | 469,234 | 0 |
| Debt, Fed & inflation | Economics | 3 | 155,205 | 0.52 | 459,977 | 0 |
| Non-finance (gaming/social/tech culture) | Non-finance | 2 | 44,745 | 0.15 | 89,490 | 0 |

Finance vs Economics (long-form, public views): Finance: 27 videos / 19,778,498 views; Non-finance: 2 videos / 89,490 views; Economics: 6 videos / 1,840,202 views

## 6. Winning and failing topics (long-form, relative to channel long median 301,336)

- Winners (>= 2x median): **9** of 35; breakouts (>= 5x): **3**; failures (<= 0.5x, older than 60 d): **9** of 30.
- Winners by sub-niche: Companies, billionaires & business history 3; Crashes, recessions & crises 2; AI & tech bubble 2; Investing, stocks & crypto 1; Trade, tariffs & geopolitics 1.
- Failures by sub-niche: Companies, billionaires & business history 4; Non-finance (gaming/social/tech culture) 2; Crashes, recessions & crises 1; Investing, stocks & crypto 1; Debt, Fed & inflation 1.

Breakouts:

- 4,219,017 (14.0x) 2025-10-03 [The Wolf of Wall Street Scam Explained Like You're 5](https://www.youtube.com/watch?v=HawmGu7oNrc)
- 2,762,821 (9.2x) 2025-08-15 [The Great Depression Explained Like You’re 5](https://www.youtube.com/watch?v=LuEcoqizj0o)
- 2,285,772 (7.6x) 2025-06-15 [The 2008 Financial Crisis Explained Like You’re 5](https://www.youtube.com/watch?v=KE-WJevx-7c)

Lowest long-form (older than 60 d):

- 40,623 (0.13x) 2026-06-28 [The Greatest Slave System Ever Created](https://www.youtube.com/watch?v=GdpGd0U2wmo)
- 48,867 (0.16x) 2026-07-21 [Epstein Situation Explained Like You're 5](https://www.youtube.com/watch?v=AKrjI9m6fpk)
- 49,890 (0.17x) 2026-05-23 [The Economic Secret of WW2](https://www.youtube.com/watch?v=A_wtItX_kIE)
- 69,270 (0.23x) 2025-04-22 [Every Financial Crisis Explained in 10 Minutes](https://www.youtube.com/watch?v=KHLY6SyLvgQ)
- 98,218 (0.33x) 2026-09-09 [How BYD Actually Beat Tesla](https://www.youtube.com/watch?v=ggFpIjvXQi4)
- 103,452 (0.34x) 2026-08-01 [Ozempic Explained Like You're 5](https://www.youtube.com/watch?v=ybP8g6xzCIs)
- 103,771 (0.34x) 2026-08-22 [TSMC Explained Like You're 5](https://www.youtube.com/watch?v=aDCKVS8aA8E)
- 109,298 (0.36x) 2025-06-25 [The Rise of Paypal Explained Like You're 5](https://www.youtube.com/watch?v=EedHneVKmpo)

## 7. Title structures (long-form)

| Feature | Share of long titles | Median views with | Median views without |
|---|---:|---:|---:|
| Question mark | 0% | 0 | 301,336 |
| Contains a digit | 71% | 254,882 | 386,093 |
| Colon | 9% | 302,952 | 278,109 |
| Ellipsis | 0% | 0 | 301,336 |
| ALL-CAPS word | 23% | 230,838 | 301,336 |
| Year | 0% | 0 | 301,336 |
| Starts with how/why/what/is… | 14% | 206,967 | 337,532 |
| Addresses you/we | 57% | 336,724 | 246,037 |
| Negative/threat word | 9% | 158,725 | 302,144 |

Median title length 7 words (top-10 median 7). Feature medians are descriptive; they do not show causation.

## 8. Shorts vs long-form and upload frequency

- Long-form: 35 items, median views 301,336. Shorts: 0 items, median views 0.
- Whole-history cadence: 0.43 uploads/week (0.43 long, 0.00 Shorts) over 571 days.

## 9. Hook data (first ~60 words of transcript, top 8 long-form)

- **The Wolf of Wall Street Scam Explained Like You're 5** (4,219,017): "He lied about $1 stock, made millions, and only served 22 months in jail. Then Hollywood turned his crimes into a blockbuster. This is the story of Jordan Belelfford, the man who scammed America and got rich again doing it. And the wildest part, people still cheer for him. Bayside, Queens, 1962. A working-class Jewish neighborhood where dreams were modest"
- **The Great Depression Explained Like You’re 5** (2,762,821): "It's the Great Depression. You woke up rich, then went to bed broke. No war, no warning, just a terrifying crash that wiped out $200 billion and sent America spiraling into a decade of hunger and dust. So, what the hell happened? Let's rewind to the party before the fall. Imagine waking up in 1922. The war is over. The"
- **The 2008 Financial Crisis Explained Like You’re 5** (2,285,772): "September 2008, a 158-year-old bank collapsed overnight. $600 billion gone. Retirement accounts vanish. Millions lose jobs. But what if I told you the real cause started with a lie so simple you could fit it on a billboard? Why rent when you can own? Cue the upbeat music. It's 2002. America is still nursing a hangover from the do crash."
- **Rockefeller: The First Confirmed Billionaire (And How He Did It)** (1,326,122): "This man controlled 90% of America's oil. And when the government shattered his empire to stop him, he actually became richer. This is the story of John [music] D. Rockefeller, the most hated businessman who became the world's first billionaire. July 8th, 1839, Richford, New York. A baby was born into poverty. His name was John Davison Rockefeller. His mother,"
- **The Rise of Anthropic Explained Like You're 5** (1,116,354): "This is Anthropic. Soon it will go public at a $2 trillion valuation. The biggest IPO ever on Earth. Bigger than SpaceX [music] and Saudi Aramco. But how did it actually get this big? Wasn't this just the company [music] that made Claude? How did it become the company leading the AI revolution? Well, it all started [music] with a"
- **How Jeff Bezos Actually Built Amazon** (1,006,867): "This adopted kid built a $2 trillion empire from the passenger seat of a beat up Chevy Blazer. He typed out a business plan during [music] a cross-country drive in 1994. And 30 years later, his company makes $1.2 million [music] every single minute. Not from viral products or flashy ads, but from a strategy [music] that crushed entire industries"
- **The Man Who Built Singapore in One Generation** (973,784): "Singapore went from a tiny island with zero resources to one of the richest countries on Earth in just 50 years. The average person there is wealthier than the average American. But in 1965, everyone thought Singapore was dead. We just got kicked out of Malaysia. We have no natural resources. We're smaller than New York City. [music] Our unemployment"
- **The $63 BILLION Company That Sold Nothing** (920,247): "December 2001, America's seventh largest company files for bankruptcy. $63 billion gone. Thousands of employees wiped out. Wall Street shocked. But not because it happened. Because no one could explain how. This is the story of Enron. The company that sold nothing, made billions, and then imploded while everyone clapped. Imagine a company that made its fortune by moving gas"

## 10. Title audit list (all items with assigned sub-niche)

<details><summary>Show all 35 titles</summary>

| Date | T | Views | Sub-niche | Title |
|---|---|---:|---|---|
| 2026-11-14 | L | 552,544 | AI & tech bubble | NVIDIA Scandal Explained Like You're 5 |
| 2026-11-10 | L | 302,952 | Companies, billionaires & business history | J.P. Morgan: The Most Powerful Man in America |
| 2026-10-31 | L | 246,037 | Companies, billionaires & business history | How Steve Jobs Actually Built Apple |
| 2026-10-16 | L | 1,116,354 | AI & tech bubble | The Rise of Anthropic Explained Like You're 5 |
| 2026-10-06 | L | 469,938 | AI & tech bubble | The First Big Victim of the AI Bubble |
| 2026-09-09 | L | 98,218 | Companies, billionaires & business history | How BYD Actually Beat Tesla |
| 2026-08-22 | L | 103,771 | Companies, billionaires & business history | TSMC Explained Like You're 5 |
| 2026-08-11 | L | 171,778 | Companies, billionaires & business history | How Elon Musk Actually Became a Trillionaire |
| 2026-08-01 | L | 103,452 | Companies, billionaires & business history | Ozempic Explained Like You're 5 |
| 2026-07-21 | L | 48,867 | Non-finance (gaming/social/tech culture) | Epstein Situation Explained Like You're 5 |
| 2026-07-09 | L | 584,655 | AI & tech bubble | NVIDIA Explained Like You're 5 |
| 2026-06-28 | L | 40,623 | Non-finance (gaming/social/tech culture) | The Greatest Slave System Ever Created |
| 2026-06-24 | L | 158,725 | Companies, billionaires & business history | VOC: The $7.9 Trillion Company You've Never Heard Of |
| 2026-05-23 | L | 49,890 | Debt, Fed & inflation | The Economic Secret of WW2 |
| 2026-04-30 | L | 254,882 | Debt, Fed & inflation | Petrodollar Explained Like You're 5 |
| 2026-04-19 | L | 162,152 | Trade, tariffs & geopolitics | Iran War Explained Like You're 5 |
| 2026-03-30 | L | 301,336 | Investing, stocks & crypto | Margin Call Scandal Explained Like You're 5 |
| 2026-03-09 | L | 469,234 | Personal finance & consumer | The Worst Time to be Rich as a Human |
| 2026-02-28 | L | 1,326,122 | Companies, billionaires & business history | Rockefeller: The First Confirmed Billionaire (And How He Did It) |
| 2026-02-10 | L | 244,289 | Trade, tariffs & geopolitics | Xi Jinping Explained Like You’re 5 |
| 2026-01-31 | L | 155,205 | Debt, Fed & inflation | 5000 Years of Gold Explained in 16 Minutes |
| 2026-01-10 | L | 871,891 | AI & tech bubble | Palantir Technologies Explained Like You’re 5 |
| 2025-12-27 | L | 973,784 | Trade, tariffs & geopolitics | The Man Who Built Singapore in One Generation |
| 2025-12-12 | L | 438,100 | AI & tech bubble | The AI Bubble Explained Like You're 5 |
| 2025-11-28 | L | 1,006,867 | Companies, billionaires & business history | How Jeff Bezos Actually Built Amazon |
| 2025-10-27 | L | 392,754 | Crashes, recessions & crises | The Dot-Com Bubble Explained Like You're 5 |
| 2025-10-03 | L | 4,219,017 | Investing, stocks & crypto | The Wolf of Wall Street Scam Explained Like You're 5 |
| 2025-09-08 | L | 372,112 | Companies, billionaires & business history | Theranos Scandal Explained Like You're 5 |
| 2025-08-15 | L | 2,762,821 | Crashes, recessions & crises | The Great Depression Explained Like You’re 5 |
| 2025-07-19 | L | 920,247 | Companies, billionaires & business history | The $63 BILLION Company That Sold Nothing |
| 2025-07-12 | L | 118,266 | Investing, stocks & crypto | Bitcoin Explained Like You're 5 |
| 2025-06-25 | L | 109,298 | Companies, billionaires & business history | The Rise of Paypal Explained Like You're 5 |
| 2025-06-15 | L | 2,285,772 | Crashes, recessions & crises | The 2008 Financial Crisis Explained Like You’re 5 |
| 2025-05-08 | L | 206,967 | Investing, stocks & crypto | How One Man Pulled Off a $65 Billion Scam |
| 2025-04-22 | L | 69,270 | Crashes, recessions & crises | Every Financial Crisis Explained in 10 Minutes |

</details>

