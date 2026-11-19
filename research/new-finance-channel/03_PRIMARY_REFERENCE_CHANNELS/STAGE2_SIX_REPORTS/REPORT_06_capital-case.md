# Forensic report 06: Capital Case

Stage 2, 2026-11-19. Scope: this channel only, from `finance_economics_complete.db` (read-only). Data builder: `build_data.py`. Classified video list: `data/capital-case_classified.csv`.

**Evidence labels:** VERIFIED = read from the DB or raw Apify file. INFERRED = our reading of a pattern. HYPOTHESIS = untested idea. NOT AVAILABLE = no data or media in this workspace. Views are public counts as of the pull dates (2026-11-17 to 2026-11-19). Shorts = duration <= 180 s. No view count proves a cause; there is no CTR or retention data.

# Part 1. Reading

## A. Reading of the channel (INFERRED)

Capital Case is a young (first video 2026-02-22), small story channel: 13 long videos, 1.51M views total, median 54,627, 11 min 31 s. It is the closest structural copy of Crayon Capital in the set ("Explained Like You're 5", "Explained in 11 Minutes", dated-scene openers). It is also the weakest performer: median is 18% of Crayon's. It has two breakouts: Rockefeller (385K, 7.1x) and The Great Depression (294K, 5.4x).

## B. Finance AND Economics coverage

- Finance (9 long, 1.06M views): companies/billionaires (5: Rockefeller 385K, BYD 152K, SpaceX 55K, Rothschilds 41K, BlackRock 5K), crashes (2: Great Depression 294K, FTX 5K), Epstein (86K), OpenAI (33K).
- Economics (4 long, 451K views): Strait of Hormuz/oil (250K, 4.6x), WW2 appeasement (189K, 3.5x), debt/currency (2 videos: "If Every Country is in Debt, Who Owns the Money?" 6K and "When $100 Trillion Couldn't Buy a Bread" 6K).
- Economics winners are geopolitics-linked and news-timed (Hormuz after the 2026-02-28 strikes). The two money-theory videos are the worst in the channel (both ~0.1x).

## C. Winning and failing topics

- Winners (5 of 13): Rockefeller, Great Depression, Hormuz, WW2 appeasement, Epstein (86K, 1.6x).
- Failures (4 of 11 older videos): BlackRock conspiracies (5K, 0.09x), FTX (5K), 100 trillion bread (6K), who owns the debt (6K). Conspiracy framing and abstract money-theory both fail; named historical events and one famous person work.
- Cross-check with Crayon, same topics: Rockefeller Crayon 1.33M vs Capital Case 385K; Great Depression 2.76M vs 294K; BYD 98K vs 152K (Capital Case ahead); Epstein 49K vs 86K (ahead); Iran/Hormuz 162K vs 250K (ahead). So Capital Case beat the larger channel on the three newest, news-linked topics. INFERRED from 5 pairs; publish dates and subscriber bases differ.

## D. Title structures

- 6 of 13 use "Explained" templates (median 47.6K); "Explained in N Minutes" (4) is the channel's own variation.
- 77% contain a digit (median 70.5K vs 6.4K without). Small n; the non-digit titles are the 4 failures.
- Colon titles (2): "BlackRock: The Conspiracies..." (5K), "Epstein: The $1.9 Billion Mystery..." (86K).
- "How the Great Depression Actually Happened (The Fatal Decisions)" (294K) is the only explicit explanatory-causal title and the best non-Rockefeller title, with a parenthesised subtitle.

## E. Thumbnail patterns

Source: 8-image sample (thumbnail model doc): round-head cartoon characters, dark cinematic ground, one name or event. INFERRED.

## F. Script and hook structure (VERIFIED text, INFERRED structure)

Same spine as Crayon: a dated scene or a stakes statement, no greeting. Examples: "September 30th, 1938, Munich, Germany. Neville Chamberlain..."; "In 1928, an economist at Harvard stood up and told an audience that poverty in America was nearly solved... One year later, a quarter of the American workforce had nowhere to go."; "On February 28th, 2026, the United States and Israel launched nearly 900 strikes on Iran in 12 hours." The hook states an irony or reversal (confident prediction then collapse; hero then failure). Rockefeller and SpaceX open with a stats-first claim ("controlled 90% of America's oil"). Narration is formal and measured.

## G. Visual storytelling and editing

NOT AVAILABLE (no video files analysed).

## H. Shorts vs long-form and frequency

No Shorts. 13 long in 253 days = 0.36 a week, 1 to 2 a month (none in 2026-09). Monday is the most common day (5 of 13). Last 30 days: 1; 90 days: 4. Cadence is flat and low; views per video did not rise steadily; three of the four lowest videos (5K to 6K) are from 2026-02 to 2026-03.

## I. Implications for our channel (HYPOTHESIS)

1. A Crayon clone format on a small channel did not reach Crayon's views; "same format, newer channel" is not enough. 2. Topics timed to a current event (Hormuz, BYD, Epstein) outperformed evergreen money-theory. 3. Two videos per month is the floor evidence of viable survival for a story channel in this set, and its median is only 55K.

## J. Limits

Only 13 videos; many have had less than 60 days. Subscriber base not compared. No CTR or retention data.


# Part 2. Data tables

## 1. Full inventory (VERIFIED from DB)

- Videos held: **13** (long-form 13, Shorts 0 by duration <= 180 s). Date range 2026-02-22 to 2026-11-02.
- With public view counts: 13. Transcripts held: 13 of 13.
- Views, long-form: total 1,507,780, median 54,627, mean 115,983, max 385,205.
- Median long-form duration: 11 min 31 s.

## 2. Top videos

### Top 15 long-form
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 385,205 | 2026-08-25 | 10:02 | Companies, billionaires & business history | [Rockefeller Explained in 10 Minutes](https://www.youtube.com/watch?v=sGtEBUIppYc) |
| 2 | 294,004 | 2026-06-22 | 11:29 | Crashes, recessions & crises | [How the Great Depression Actually Happened (The Fatal Decisions)](https://www.youtube.com/watch?v=CAsim5HC-uI) |
| 3 | 249,538 | 2026-05-02 | 9:30 | Energy, oil & commodities | [Strait of Hormuz Explained Like You're 5](https://www.youtube.com/watch?v=0k5C-MrLjAI) |
| 4 | 189,476 | 2026-06-15 | 11:47 | Trade, tariffs & geopolitics | [The Mistake That Started World War 2](https://www.youtube.com/watch?v=SwO1JS_9MCw) |
| 5 | 152,354 | 2026-10-14 | 11:16 | Companies, billionaires & business history | [The Rise (And Fall?) of BYD in 11 Minutes](https://www.youtube.com/watch?v=jjRo2QSMybU) |
| 6 | 86,396 | 2026-04-03 | 11:59 | Personal finance & consumer | [Epstein: The $1.9 Billion Mystery Nobody Can Explain](https://www.youtube.com/watch?v=du4FfP8UY6k) |
| 7 | 54,627 | 2026-07-23 | 10:57 | Companies, billionaires & business history | [The Rise of SpaceX Explained in 11 Minutes](https://www.youtube.com/watch?v=GDlvUd_BUPY) |
| 8 | 40,603 | 2026-11-02 | 11:33 | Companies, billionaires & business history | [The Rothschilds Explained in 11 Minutes](https://www.youtube.com/watch?v=uJ_vkUHLJNs) |
| 9 | 33,116 | 2026-08-28 | 11:10 | AI & tech bubble | [The Rise of OpenAI Explained in 11 Minutes](https://www.youtube.com/watch?v=WgpX3oyOKY4) |
| 10 | 6,379 | 2026-02-23 | 11:48 | Debt, Fed & inflation | [If Every Country is in Debt, Who Owns the Money?](https://www.youtube.com/watch?v=HA1BLrrkYjg) |
| 11 | 5,558 | 2026-02-22 | 12:15 | Debt, Fed & inflation | [When $100 Trillion Couldn't Buy a Bread](https://www.youtube.com/watch?v=Voky9e_WNHY) |
| 12 | 5,396 | 2026-03-27 | 11:50 | Crashes, recessions & crises | [FTX Collapse Explained Like You're 5](https://www.youtube.com/watch?v=F0q0tg7JHKI) |
| 13 | 5,128 | 2026-05-18 | 11:31 | Companies, billionaires & business history | [BlackRock: The Conspiracies You're Currently Living In](https://www.youtube.com/watch?v=Fv3STb4g23Q) |

## 3. Recent uploads (newest 12, any type)

| Date | Type | Views | Age (d) | Title |
|---|---|---:|---:|---|
| 2026-11-02 | Long | 40,603 | 17 | The Rothschilds Explained in 11 Minutes |
| 2026-10-14 | Long | 152,354 | 36 | The Rise (And Fall?) of BYD in 11 Minutes |
| 2026-08-28 | Long | 33,116 | 83 | The Rise of OpenAI Explained in 11 Minutes |
| 2026-08-25 | Long | 385,205 | 86 | Rockefeller Explained in 10 Minutes |
| 2026-07-23 | Long | 54,627 | 119 | The Rise of SpaceX Explained in 11 Minutes |
| 2026-06-22 | Long | 294,004 | 150 | How the Great Depression Actually Happened (The Fatal Decisions) |
| 2026-06-15 | Long | 189,476 | 157 | The Mistake That Started World War 2 |
| 2026-05-18 | Long | 5,128 | 185 | BlackRock: The Conspiracies You're Currently Living In |
| 2026-05-02 | Long | 249,538 | 201 | Strait of Hormuz Explained Like You're 5 |
| 2026-04-03 | Long | 86,396 | 230 | Epstein: The $1.9 Billion Mystery Nobody Can Explain |
| 2026-03-27 | Long | 5,396 | 237 | FTX Collapse Explained Like You're 5 |
| 2026-02-23 | Long | 6,379 | 269 | If Every Country is in Debt, Who Owns the Money? |

## 4. 30 / 60 / 90-day patterns (to 2026-11-19)

| Window | Uploads | Long | Shorts | Long views median | Long views total | Per week |
|---|---:|---:|---:|---:|---:|---:|
| last 30 d | 1 | 1 | 0 | 40,603 | 40,603 | 0.2 |
| last 60 d | 2 | 2 | 0 | 96,478 | 192,957 | 0.2 |
| last 90 d | 4 | 4 | 0 | 96,478 | 611,278 | 0.3 |
| last 180 d | 7 | 7 | 0 | 152,354 | 1,149,385 | 0.3 |
| last 365 d | 13 | 13 | 0 | 54,627 | 1,507,780 | 0.2 |

Monthly uploads (last 14 active months): 2026-02: 2L/0S; 2026-03: 1L/0S; 2026-04: 1L/0S; 2026-05: 2L/0S; 2026-06: 2L/0S; 2026-07: 1L/0S; 2026-08: 2L/0S; 2026-10: 1L/0S; 2026-11: 1L/0S

Long-form upload weekday: Mon 5, Fri 3, Sun 1, Wed 1, Tue 1, Sat 1, Thu 1

## 5. Finance / Economics categories and sub-niche distribution

Classification: title-keyword rules (`build_data.py`), then **audited by reading the titles** (section 9). Labels are INFERRED, not channel-declared.

| Sub-niche | F/E | Long n | Long median views | x channel median | Long total views | Shorts n |
|---|---|---:|---:|---:|---:|---:|
| Companies, billionaires & business history | Finance | 5 | 54,627 | 1.00 | 637,917 | 0 |
| Crashes, recessions & crises | Finance | 2 | 149,700 | 2.74 | 299,400 | 0 |
| Energy, oil & commodities | Economics | 1 | 249,538 | 4.57 | 249,538 | 0 |
| Trade, tariffs & geopolitics | Economics | 1 | 189,476 | 3.47 | 189,476 | 0 |
| Personal finance & consumer | Finance | 1 | 86,396 | 1.58 | 86,396 | 0 |
| AI & tech bubble | Finance | 1 | 33,116 | 0.61 | 33,116 | 0 |
| Debt, Fed & inflation | Economics | 2 | 5,968 | 0.11 | 11,937 | 0 |

Finance vs Economics (long-form, public views): Finance: 9 videos / 1,056,829 views; Economics: 4 videos / 450,951 views

## 6. Winning and failing topics (long-form, relative to channel long median 54,627)

- Winners (>= 2x median): **5** of 13; breakouts (>= 5x): **2**; failures (<= 0.5x, older than 60 d): **4** of 11.
- Winners by sub-niche: Companies, billionaires & business history 2; Trade, tariffs & geopolitics 1; Crashes, recessions & crises 1; Energy, oil & commodities 1.
- Failures by sub-niche: Debt, Fed & inflation 2; Companies, billionaires & business history 1; Crashes, recessions & crises 1.

Breakouts:

- 385,205 (7.1x) 2026-08-25 [Rockefeller Explained in 10 Minutes](https://www.youtube.com/watch?v=sGtEBUIppYc)
- 294,004 (5.4x) 2026-06-22 [How the Great Depression Actually Happened (The Fatal Decisions)](https://www.youtube.com/watch?v=CAsim5HC-uI)

Lowest long-form (older than 60 d):

- 5,128 (0.09x) 2026-05-18 [BlackRock: The Conspiracies You're Currently Living In](https://www.youtube.com/watch?v=Fv3STb4g23Q)
- 5,396 (0.10x) 2026-03-27 [FTX Collapse Explained Like You're 5](https://www.youtube.com/watch?v=F0q0tg7JHKI)
- 5,558 (0.10x) 2026-02-22 [When $100 Trillion Couldn't Buy a Bread](https://www.youtube.com/watch?v=Voky9e_WNHY)
- 6,379 (0.12x) 2026-02-23 [If Every Country is in Debt, Who Owns the Money?](https://www.youtube.com/watch?v=HA1BLrrkYjg)
- 33,116 (0.61x) 2026-08-28 [The Rise of OpenAI Explained in 11 Minutes](https://www.youtube.com/watch?v=WgpX3oyOKY4)
- 54,627 (1.00x) 2026-07-23 [The Rise of SpaceX Explained in 11 Minutes](https://www.youtube.com/watch?v=GDlvUd_BUPY)
- 86,396 (1.58x) 2026-04-03 [Epstein: The $1.9 Billion Mystery Nobody Can Explain](https://www.youtube.com/watch?v=du4FfP8UY6k)
- 189,476 (3.47x) 2026-06-15 [The Mistake That Started World War 2](https://www.youtube.com/watch?v=SwO1JS_9MCw)

## 7. Title structures (long-form)

| Feature | Share of long titles | Median views with | Median views without |
|---|---:|---:|---:|
| Question mark | 15% | 79,366 | 54,627 |
| Contains a digit | 77% | 70,511 | 6,379 |
| Colon | 15% | 45,762 | 54,627 |
| Ellipsis | 0% | 0 | 54,627 |
| ALL-CAPS word | 15% | 78,875 | 54,627 |
| Year | 0% | 0 | 54,627 |
| Starts with how/why/what/is… | 15% | 149,781 | 54,627 |
| Addresses you/we | 23% | 5,396 | 70,511 |
| Negative/threat word | 15% | 45,896 | 54,627 |

Median title length 7 words (top-10 median 8). Feature medians are descriptive; they do not show causation.

## 8. Shorts vs long-form and upload frequency

- Long-form: 13 items, median views 54,627. Shorts: 0 items, median views 0.
- Whole-history cadence: 0.36 uploads/week (0.36 long, 0.00 Shorts) over 253 days.

## 9. Hook data (first ~60 words of transcript, top 8 long-form)

- **Rockefeller Explained in 10 Minutes** (385,205): "At its peak, one company controlled 90% of America's oil. Every lamp in every home burned on terms it set. The government spent 11 years trying to kill it, and did. The greatest legal victory the country had ever won. The man who built it didn't seem to notice. Two years later, he was the richest human being in recorded"
- **How the Great Depression Actually Happened (The Fatal Decisions)** (294,004): "In 1928, an economist at Harvard stood up and told an audience that poverty in America was nearly solved. He wasn't alone in thinking it. Presidents said it. Bankers said it. Confidently, publicly, on the record. One year later, a quarter of the American workforce had nowhere to go. The breadlines stretched around city blocks. Families packed everything [music] they"
- **Strait of Hormuz Explained Like You're 5** (249,538): "On February 28th, 2026, the United States and Israel launched nearly 900 strikes on Iran in 12 hours. Military bases, missile sites, nuclear facilities, one of the most devastating opening salvos in modern history. [music] Iran's response didn't come with missiles. It closed a gap of water 21 miles wide. >> [music] >> In the weeks that followed, oil surged"
- **The Mistake That Started World War 2** (189,476): "September 30th, 1938, Munich, Germany. Neville Chamberlain just spent 13 hours sitting across from the most dangerous man in Europe and gave him everything he asked for. He flew home to London, stepped off the plane, held the paper up to a crowd of thousands. Peace of our time. He was called a hero, a statesman, the man who just"
- **The Rise (And Fall?) of BYD in 11 Minutes** (152,354): "October 2011, a Bloomberg reporter asks Elon Musk if a Chinese battery company called BYD could ever threaten Tesla. Have you seen their car? 15 years later, BYD sells more electric cars in a year than anyone alive, Tesla included. Then the crown nearly kills it. By March 2026, BYD's own factories are running under half capacity. Mega pain. This"
- **Epstein: The $1.9 Billion Mystery Nobody Can Explain** (86,396): "August 10th, 2019. A man passed away in a Manhattan jail cell. The guards assigned to watch him hadn't checked in 3 hours. The cameras outside his cell had malfunctioned that night. No official time of death was ever determined. Two days before he was found, he had signed a will. $577 million. The dollars. The media called him a"
- **The Rise of SpaceX Explained in 11 Minutes** (54,627): "June 12th, 2026. The largest stock sale in Wall Street history happens on the Nasdaq. Bigger than Saudi Aramco, bigger than any tech company that's ever listed. Hundreds of thousands of people buy in on day one. They get almost no say in how the company is run. Buried in the paperwork, a second class of stock held almost entirely"
- **The Rothschilds Explained in 11 Minutes** (40,603): "1815, two decades of war finally end. And within a few years, the kings of Europe are lining up to borrow from the same family. 50 years earlier, that family wasn't legally allowed to own the ground under their own house. The street they lived on had a gate, and every night someone locked it from the outside. Nearly everything"

## 10. Title audit list (all items with assigned sub-niche)

<details><summary>Show all 13 titles</summary>

| Date | T | Views | Sub-niche | Title |
|---|---|---:|---|---|
| 2026-11-02 | L | 40,603 | Companies, billionaires & business history | The Rothschilds Explained in 11 Minutes |
| 2026-10-14 | L | 152,354 | Companies, billionaires & business history | The Rise (And Fall?) of BYD in 11 Minutes |
| 2026-08-28 | L | 33,116 | AI & tech bubble | The Rise of OpenAI Explained in 11 Minutes |
| 2026-08-25 | L | 385,205 | Companies, billionaires & business history | Rockefeller Explained in 10 Minutes |
| 2026-07-23 | L | 54,627 | Companies, billionaires & business history | The Rise of SpaceX Explained in 11 Minutes |
| 2026-06-22 | L | 294,004 | Crashes, recessions & crises | How the Great Depression Actually Happened (The Fatal Decisions) |
| 2026-06-15 | L | 189,476 | Trade, tariffs & geopolitics | The Mistake That Started World War 2 |
| 2026-05-18 | L | 5,128 | Companies, billionaires & business history | BlackRock: The Conspiracies You're Currently Living In |
| 2026-05-02 | L | 249,538 | Energy, oil & commodities | Strait of Hormuz Explained Like You're 5 |
| 2026-04-03 | L | 86,396 | Personal finance & consumer | Epstein: The $1.9 Billion Mystery Nobody Can Explain |
| 2026-03-27 | L | 5,396 | Crashes, recessions & crises | FTX Collapse Explained Like You're 5 |
| 2026-02-23 | L | 6,379 | Debt, Fed & inflation | If Every Country is in Debt, Who Owns the Money? |
| 2026-02-22 | L | 5,558 | Debt, Fed & inflation | When $100 Trillion Couldn't Buy a Bread |

</details>

