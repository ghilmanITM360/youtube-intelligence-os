# Forensic report 01: MonkeyExplains

Stage 2, 2026-11-19. Scope: this channel only, from `finance_economics_complete.db` (read-only) plus Apify R4/R5 merge. Data builder: `build_data.py`. Classified video list: `data/monkeyexplains_classified.csv`.

**Evidence labels:** VERIFIED = read from the DB or raw Apify file. INFERRED = our reading of a pattern. HYPOTHESIS = untested idea. NOT AVAILABLE = no data or media in this workspace. Views are public counts as of the pull dates (2026-11-17 to 2026-11-19). Shorts = duration <= 180 s. No view count proves a cause; there is no CTR or retention data.

# Part 1. Reading

## A. Reading of the channel (INFERRED from the data above)

MonkeyExplains is an animated monkey-allegory news explainer. It is not a finance-only channel: of 64 public long videos, 34 are Finance by our labels, 12 Economics, 15 unclassified-to-political, 3 non-finance (gaming, Roblox, Discord). Its biggest hits are still finance/economics: AI bubble (5 of 12 winners), the US national debt, tariffs, the shutdown. The older stable format is "X Explained Using Bananas" (19 long titles, median 273,970 views); since early 2026 it moved to news-reactive "...Worse Than You Think" titles (11 titles, median 431,300), which is the stronger group in this sample.

Stage 1 correction: the earlier guess "100% AI bubble" was wrong. AI is the largest single sub-niche (17 long, 20 of 37 Shorts) but it is about a quarter of long output.

## B. Finance AND Economics coverage

- Economics: Debt/Fed, tariffs/trade, government shutdown, jobs, demographics (South Korea), energy shortage. Winners: National Debt (1.92M, 7.0x median), Shutdown (726K), Tariff Wars (653K), Fed Rate Cut (518K), South Korea population (501K).
- Finance: AI/OpenAI/SpaceX bubble, credit cards, 401k, scams, billionaires. Winners: AI bubble videos (2.66M, 1.33M, 1.05M, 1.00M), Apestein wealth (838K), credit card duopoly (666K).
- Weakest: scam/fraud explainers (Wolf of Wall Street 88K, Art Market 130K, Global Scam Industry 144K), culture/politics items (UK colonising YouTube 120K, DOJ 108K), Iran war profiteering (102K). Evidence of a pattern: topics that are about people or institutions without a number or crisis hook underperform. HYPOTHESIS, not tested.

## C. Winning and failing topics

Breakouts (>= 5x median 275,020): "Why Hasn't The AI Bubble Popped (Yet)?" (2.66M, 9.7x, 2026-11-01) and "The US National Debt Crisis Explained with Bananas" (1.92M, 7.0x, 2025-06-13). Both are a single big number or a single big question applied to the whole economy. The 7 failures (<= 0.5x, older than 60 days) are Wolf of Wall Street scams, AI influencers, Drug Trafficking, Iran war, DOJ, UK/YouTube and the Art Market. Age matters: 2026-11 videos have had few days to accumulate views, so ranking recent videos against old ones is biased in favour of older ones; the top AI videos are nevertheless recent, which shows the topic is currently pulling.

## D. Title structures

- Template 1 (2025): "[Topic] Explained Using Bananas / with Bananas / using Monkeys" (19 titles, median 273,970).
- Template 2 (2026): "[Subject] Is/Are Worse Than You Think/Thought" (11 titles, median 431,300; the group contains 3 of the top 5). No colon, no year, few digits (9%); digit titles have lower median (192K vs 280K).
- Question titles are 12% of the set but have higher median (401K vs 251K). "Addresses you/we" 28% with median 348K vs 234K. All are descriptive medians, not causal.
- Median 7 words. Capitalised words (14%) are linked to lower medians (183K vs 277K); do not copy ALL-CAPS.
- Shorts titles: 37 of 37 carry hashtags (#finance #economics etc.), a different format from long titles.

## E. Thumbnail patterns

Source: our 12-image sample of the channel's top thumbnails, viewed 2026-11-19 (`14_WINNING_THUMBNAIL_MODELS/THUMBNAIL_MODEL_SIX_CHANNELS_2026-11-19.md`). Observed: hand-drawn gorilla/monkey mascot, white or dark ground, one chart with red downward line, percent badge, 2 to 4 word headline ("It's Over...", "There's no way out..."). INFERRED, no CTR data exists. No new image review was done in Stage 2.

## F. Script and hook structure (from transcripts; VERIFIED text, INFERRED structure)

Seven of the top eight videos open with the same formula: "This is [Sam/Uncle Don/Marcus/Charlie], and he's got a huge problem. See, ..." followed by a monkey-jungle allegory (jungle = country, bananas = money, "head honcho"). It names a person or company as the protagonist, then states the problem within the first 20 seconds, then explains the mechanism with the allegory, ending with a consequence. The formula is the channel's brand. The eighth (Stop Killing Games) starts with a consumer-rights hypothetical. Member Edition versions repeat topics (35 items) and are not analysable.

Average pace and length: median 14 min 07 s long video. Music cues are marked in the transcript (`[music]`).

## G. Visual storytelling and editing

NOT AVAILABLE. No MonkeyExplains video files are in our media library or workspace, and no frame analysis was run in this stage. Only the transcript-visible parts (allegory, character names, music cues) and thumbnails are reported. Nothing about camera, motion or cut rhythm is claimed.

## H. Shorts vs long-form and frequency

- Long: 99 held (64 public + 35 Member Edition). Shorts: 37, median 15,539 views, max 131,980. Long median is 17.7x the Shorts median.
- Shorts are recent: 8 in June 2025, then 29 in the last 30 days, almost all on the AI bubble. This looks like a Shorts test cluster, 2026-10 onwards. Result in the data: 9,886 to 43,547 views each except one outlier (131,980).
- Long cadence: 2025-10 to 2026-02: 2 to 5 a month; 2026-03 to 2026-09: 7 to 10 a month; 2026-10: 9. That is roughly 2 per week, mostly Sat and Sun (53 of 99 long uploads, including Members). Last 30 days: 6 long + 22 Shorts.
- HYPOTHESIS: MonkeyExplains scaled from ~1 to ~2 long videos a week in March 2026 while median views stayed above 250K, so output volume did not collapse per-video views in this sample.

## I. Implications for our channel (HYPOTHESIS)

1. One big number or open question about the whole economy beats a named scandal. 2. A recurring protagonist formula can be copied as a STRUCTURE only (problem in first 20 seconds), never the monkey allegory itself. 3. Current-news titles ("Worse Than You Think") perform in this sample; our own alternative would be a data claim phrased without exaggeration. 4. Shorts did not rescue long-form views here.

## J. Limits

136 of 149 items held; 13 probable Member Edition items missing. Views for Member Edition are not public. DB not updated; data comes from the merged CSV. Labels are our keyword rules plus manual overrides listed in `build_data.py`.


# Part 2. Data tables

## 1. Full inventory (VERIFIED from DB + Apify R4/R5 merge)

- Videos held: **136** (long-form 99, Shorts 37 by duration <= 180 s). Date range 2025-05-26 to 2026-11-14.
- With public view counts: 101. Transcripts held: 99 of 136.
- Member Edition items: **35** (no public views or transcripts; excluded from every views statistic below). Coverage 136 of 149 reported; 13 items not recovered (Stage 1, INFERRED probable Member Edition).
- Views, long-form: total 25,960,948, median 275,020, mean 405,639, max 2,660,895.
- Views, Shorts: total 759,591, median 15,539, max 131,980.
- Median long-form duration: 14 min 07 s.

## 2. Top videos

### Top 15 long-form
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 2,660,895 | 2026-11-01 | 13:56 | AI & tech bubble | [Why Hasn't The AI Bubble Popped (Yet)?](https://www.youtube.com/watch?v=7rtn4doHIuY) |
| 2 | 1,920,233 | 2025-06-13 | 6:56 | Debt, Fed & inflation | [The US National Debt Crisis Explained with Bananas](https://www.youtube.com/watch?v=bz0OGtrkjv0) |
| 3 | 1,325,113 | 2025-12-04 | 13:57 | AI & tech bubble | [The OpenAI Bubble is Worse Than You Think](https://www.youtube.com/watch?v=LfQIJgU_W2w) |
| 4 | 1,053,556 | 2026-11-11 | 15:50 | AI & tech bubble | [The AI Bubble Just Claimed Its First Victim](https://www.youtube.com/watch?v=9hXlMbSMHeU) |
| 5 | 999,806 | 2026-06-23 | 15:38 | Companies, billionaires & business history | [The SpaceX Bubble Crash Is Worse Than It Looks](https://www.youtube.com/watch?v=sy4HzG_qzKw) |
| 6 | 838,476 | 2026-02-13 | 15:21 | Companies, billionaires & business history | [How did Apestein Get So Rich?](https://www.youtube.com/watch?v=TSJQ8SjcTPk) |
| 7 | 725,803 | 2025-10-29 | 9:56 | Government, politics & policy | [The US Shutdown Explained Using Bananas](https://www.youtube.com/watch?v=ZyHwdD26BtY) |
| 8 | 717,058 | 2025-07-11 | 8:38 | Non-finance (gaming/social/tech culture) | [Stop Killing Games Explained Using Bananas](https://www.youtube.com/watch?v=zLDMOAlWLfc) |
| 9 | 687,982 | 2026-01-18 | 10:44 | Personal finance & consumer | [RAM Prices Are Worse Than You Think](https://www.youtube.com/watch?v=IfOREULEqRU) |
| 10 | 666,463 | 2025-09-12 | 13:23 | Investing, stocks & crypto | [Explaining how 2 Companies Ruined the Credit Card Market](https://www.youtube.com/watch?v=hn5RqOTOlhk) |
| 11 | 652,686 | 2025-06-01 | 6:45 | Trade, tariffs & geopolitics | [Tariff Wars Explained Using Bananas](https://www.youtube.com/watch?v=bPHZkC1XLcE) |
| 12 | 585,401 | 2026-07-06 | 15:05 | AI & tech bubble | [OpenAI's Financial Crisis Keeps Getting Worse](https://www.youtube.com/watch?v=eXbZrx5XW_k) |
| 13 | 518,239 | 2025-09-04 | 14:33 | Debt, Fed & inflation | [The Fed Rate Cut Saga Explained using Bananas](https://www.youtube.com/watch?v=xTFdCPKduy4) |
| 14 | 500,813 | 2025-08-14 | 9:55 | Jobs, wages & labour | [The South Korean Population Disaster Explained using Monkeys](https://www.youtube.com/watch?v=rgm0ZDdNLOA) |
| 15 | 478,910 | 2025-10-17 | 11:05 | Trade, tariffs & geopolitics | [The Indonesian Gen-Z Protests Explained Using Bananas](https://www.youtube.com/watch?v=PejedlEOsh0) |

### Top 8 Shorts
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 131,980 | 2026-10-15 | 1:27 | AI & tech bubble | [OpenAI is (Probably) Not Gonna Survive #animation #openai](https://www.youtube.com/watch?v=HoMjC5lG6Sk) |
| 2 | 43,547 | 2026-10-14 | 1:29 | AI & tech bubble | [OpenAI's Finances Make 0 Sense  #animation #ai](https://www.youtube.com/watch?v=_TMPLVQAHWE) |
| 3 | 43,372 | 2026-10-16 | 1:18 | AI & tech bubble | [BuT We'RE GOinG To Be PRofitabLE In 4 YeaRS! #ai #openai](https://www.youtube.com/watch?v=VhY4CwtKOXI) |
| 4 | 43,032 | 2026-10-15 | 1:54 | AI & tech bubble | [The AI Business Model in a nutshell #finance #economics](https://www.youtube.com/watch?v=PolXkEFii0I) |
| 5 | 38,783 | 2026-10-18 | 1:11 | AI & tech bubble | [Yes, your company probably did this too #ai #layoffs](https://www.youtube.com/watch?v=jkg3EdgDomA) |
| 6 | 36,542 | 2025-06-21 | 2:05 | Debt, Fed & inflation | [US National Debt Explained with Bananas #finance #animation #debt](https://www.youtube.com/watch?v=Jz7pmE66OqE) |
| 7 | 34,437 | 2026-10-20 | 1:36 | AI & tech bubble | [We've all played these games before #ai #bigtech](https://www.youtube.com/shorts/p6qVNXt7kuo) |
| 8 | 24,313 | 2025-06-23 | 1:25 | Debt, Fed & inflation | [US National Debt Keeps Growing #finance #debt #economics](https://www.youtube.com/watch?v=fw0z4xdJNww) |

## 3. Recent uploads (newest 12, any type)

| Date | Type | Views | Age (d) | Title |
|---|---|---:|---:|---|
| 2026-11-14 | Short | 17,158 | 5 | They're ALL Unprofitable... #finance #inflation #debt |
| 2026-11-13 | Short | 14,825 | 6 | Even The Banks Are Scared of The AI Bubble #finance #investing |
| 2026-11-12 | Short | 8,884 | 7 | South Korea's AI Bubble Is A Warning #kospi #finance #economics |
| 2026-11-11 | Short | 15,727 | 8 | What happens if the AI Bubble Pops? #finance #crash #economics |
| 2026-11-11 | Long | 1,053,556 | 8 | The AI Bubble Just Claimed Its First Victim |
| 2026-11-10 | Short | 15,816 | 9 | What Happens When Funding Runs Out? #ai #finance #economics |
| 2026-11-10 | Member | — | 9 | (Member Edition) If Everyone Loves Meta's AI, Why Did The Stock Crash? |
| 2026-11-09 | Short | 15,539 | 10 | OpenAI's Business Model Sucks, Actually #openai #finance #economics |
| 2026-11-08 | Short | 17,040 | 11 | How Nvidia ALWAYS Wins #nvidia #finance #economics |
| 2026-11-08 | Short | 11,606 | 11 | The AI Hype Train in a Nutshell #useconomy #finance #ai |
| 2026-11-07 | Short | 19,851 | 12 | OpenAI Isn't The Only AI Loser #ai #useconomy #debt |
| 2026-11-07 | Short | 9,886 | 12 | Why Hasn't the AI Bubble Popped Yet? #ai #finance #economics |

## 4. 30 / 60 / 90-day patterns (to 2026-11-19)

| Window | Uploads | Long | Shorts | Long views median | Long views total | Per week |
|---|---:|---:|---:|---:|---:|---:|
| last 30 d | 28 | 6 | 22 | 1,053,556 | 3,905,875 | 6.5 |
| last 60 d | 44 | 15 | 29 | 399,503 | 5,628,699 | 5.1 |
| last 90 d | 51 | 22 | 29 | 391,566 | 6,773,944 | 4.0 |
| last 180 d | 75 | 46 | 29 | 390,894 | 10,798,249 | 2.9 |
| last 365 d | 109 | 80 | 29 | 276,070 | 17,707,993 | 2.1 |

Monthly uploads (last 14 active months): 2025-10: 3L/0S; 2025-11: 4L/0S; 2025-12: 2L/0S; 2026-01: 3L/0S; 2026-02: 5L/0S; 2026-03: 8L/0S; 2026-04: 10L/0S; 2026-05: 8L/0S; 2026-06: 8L/0S; 2026-07: 7L/0S; 2026-08: 7L/0S; 2026-09: 8L/0S; 2026-10: 9L/18S; 2026-11: 3L/11S

Long-form upload weekday: Sun 30, Sat 23, Fri 15, Thu 10, Wed 8, Tue 7, Mon 6

## 5. Finance / Economics categories and sub-niche distribution

Classification: title-keyword rules (`build_data.py`), then **audited by reading the titles** (section 9). Labels are INFERRED, not channel-declared.

| Sub-niche | F/E | Long n | Long median views | x channel median | Long total views | Shorts n |
|---|---|---:|---:|---:|---:|---:|
| AI & tech bubble | Finance | 15 | 431,300 | 1.57 | 9,095,864 | 20 |
| Debt, Fed & inflation | Economics | 4 | 430,390 | 1.56 | 2,921,147 | 7 |
| Trade, tariffs & geopolitics | Economics | 10 | 193,070 | 0.70 | 2,688,808 | 6 |
| Companies, billionaires & business history | Finance | 3 | 838,476 | 3.05 | 2,248,737 | 0 |
| Non-finance (gaming/social/tech culture) | Non-finance | 8 | 156,431 | 0.57 | 1,915,909 | 0 |
| Crashes, recessions & crises | Finance | 6 | 244,572 | 0.89 | 1,638,461 | 2 |
| Investing, stocks & crypto | Finance | 7 | 144,400 | 0.53 | 1,636,484 | 1 |
| Government, politics & policy | Economics | 5 | 169,661 | 0.62 | 1,539,645 | 0 |
| Personal finance & consumer | Finance | 2 | 457,783 | 1.66 | 915,566 | 1 |
| Jobs, wages & labour | Economics | 2 | 400,807 | 1.46 | 801,615 | 0 |
| Energy, oil & commodities | Economics | 1 | 282,642 | 1.03 | 282,642 | 0 |
| Housing & real estate | Economics | 1 | 276,070 | 1.00 | 276,070 | 0 |
| Other / unclassified | Unclassified | 0 | 0 | 0.00 | 0 | 0 |

Finance vs Economics (long-form, public views): Finance: 33 videos / 15,535,112 views; Economics: 23 videos / 8,509,927 views; Non-finance: 8 videos / 1,915,909 views

## 6. Winning and failing topics (long-form, relative to channel long median 275,020)

- Winners (>= 2x median): **12** of 64; breakouts (>= 5x): **2**; failures (<= 0.5x, older than 60 d): **7** of 57.
- Winners by sub-niche: AI & tech bubble 4; Companies, billionaires & business history 2; Trade, tariffs & geopolitics 1; Debt, Fed & inflation 1; Non-finance (gaming/social/tech culture) 1; Investing, stocks & crypto 1; Government, politics & policy 1; Personal finance & consumer 1.
- Failures by sub-niche: Investing, stocks & crypto 2; Non-finance (gaming/social/tech culture) 2; AI & tech bubble 1; Trade, tariffs & geopolitics 1; Government, politics & policy 1.

Breakouts:

- 2,660,895 (9.7x) 2026-11-01 [Why Hasn't The AI Bubble Popped (Yet)?](https://www.youtube.com/watch?v=7rtn4doHIuY)
- 1,920,233 (7.0x) 2025-06-13 [The US National Debt Crisis Explained with Bananas](https://www.youtube.com/watch?v=bz0OGtrkjv0)

Lowest long-form (older than 60 d):

- 88,487 (0.32x) 2026-05-24 [The REAL Wolf of Wall Street is Still Scamming People Today](https://www.youtube.com/watch?v=JY-mDrPh5nY)
- 90,109 (0.33x) 2026-03-20 [The AI Influencer Epidemic Keeps Getting Worse](https://www.youtube.com/watch?v=Y41XmFbsG2s)
- 92,274 (0.34x) 2025-06-20 [Drug Trafficking Explained using Bananas](https://www.youtube.com/watch?v=v-2hJnwK5yw)
- 102,187 (0.37x) 2026-04-26 [Who's Getting Rich from the Iran War?](https://www.youtube.com/watch?v=BHg5pLQmIew)
- 107,512 (0.39x) 2026-05-18 [The US DOJ Is Imploding](https://www.youtube.com/watch?v=84YaEDQMY1c)
- 119,857 (0.44x) 2026-06-30 [The UK is Colonising YouTube](https://www.youtube.com/watch?v=VY9zxl-YqGo)
- 130,484 (0.47x) 2025-06-06 [The Art Market Scam Explained Using Bananas](https://www.youtube.com/watch?v=dHy07B-UHkE)
- 137,778 (0.50x) 2026-06-05 [The Embarrassing Apestein File Situation](https://www.youtube.com/watch?v=OQgRqLUmvPk)

## 7. Title structures (long-form)

| Feature | Share of long titles | Median views with | Median views without |
|---|---:|---:|---:|
| Question mark | 12% | 400,674 | 250,866 |
| Contains a digit | 9% | 192,355 | 279,752 |
| Colon | 0% | 0 | 275,020 |
| Ellipsis | 3% | 188,613 | 276,466 |
| ALL-CAPS word | 14% | 182,509 | 276,863 |
| Year | 0% | 0 | 275,020 |
| Starts with how/why/what/is… | 12% | 297,179 | 275,020 |
| Addresses you/we | 28% | 348,056 | 234,275 |
| Negative/threat word | 30% | 282,642 | 240,788 |

Median title length 7 words (top-10 median 7). Feature medians are descriptive; they do not show causation.

## 8. Shorts vs long-form and upload frequency

- Long-form: 99 items, median views 275,020. Shorts: 37 items, median views 15,539.
- Whole-history cadence: 1.77 uploads/week (1.29 long, 0.48 Shorts) over 537 days.

## 9. Hook data (first ~60 words of transcript, top 8 long-form)

- **Why Hasn't The AI Bubble Popped (Yet)?** (2,660,895): "This is Sam, and he's got a huge problem. See, Sam and his friends in the Silicon Valley Mafia are on a generational run, each leading what might be the most valuable companies in US jungle history. There's just one problem. Their industry looks like a giant bubble, and a growing number of monkeys think it's all one big game"
- **The US National Debt Crisis Explained with Bananas** (1,920,233): "This is Uncle Dawn, and he's got a huge problem. See, Uncle Dawn's jungle owes a lot of bananas to many, many creditors. 37 trillion bananas to be exact. Now, that's bananas. That's over a thousand times more bananas than there are monkeys on the entire globe. Potentially even more bananas than stars in the night sky. This is called"
- **The OpenAI Bubble is Worse Than You Think** (1,325,113): "This is Sam and he's got a huge problem. See, Sam's the boss of the biggest AI company in the jungle. Together, they've put out the software that's revolutionized everything from cheating on college essays [music] to writing pointless pitch decks by consulting firms. And nowadays, AI is everywhere you go. Sam's seen the headlines, his face plastered across countless"
- **The AI Bubble Just Claimed Its First Victim** (1,053,556): "This is Marcus, and he's got a huge problem. See, Marcus is the head honcho of Meta, but things aren' going too good for his company because just a few weeks ago, Meta launched its very own shiniest, newest product. [music] And no, it's not another set of weirdo sun shades, and it seems that monkeys everywhere loved it. Behold,"
- **The SpaceX Bubble Crash Is Worse Than It Looks** (999,806): "This is Charlie, and he's got a huge problem. See, Charlie likes to dabble in the stock market, and just a few days ago, the biggest IPO in the history of monkey kind hit the news. Because SpaceX just finished the paperwork necessary to hit the stock market, and knowing the cult-like following around Uncle Elon's series of companies, it's"
- **How did Apestein Get So Rich?** (838,476): "This is Uncle Don, and he's got a huge problem. See, just a few weeks ago, his jungle released 3 million pages of documents, videos, images, emails, flight logs related [music] to the case of the disgraced financeier and monkey trafficker to the public. Let's call him Jeff for reasons. They called it Transparency Day, where monkeys celebrated. They could"
- **The US Shutdown Explained Using Bananas** (725,803): "This is Uncle Don, and he's got a huge problem. He's the head honcho of the world's largest jungle, but the jungle's economy is about to shut down. Why? Bananas. See, the US jungle government operates on a budget, and every year this budget renews, accounting for things like changes in spending and shifting national priorities. Some years the military"
- **Stop Killing Games Explained Using Bananas** (717,058): "If monkeys buy a copy of Donkey Kong Country, they should be able to play whenever they want. Whether it's 2 AM, 2077, or on their OG Nintendo Switch. But today, if monkeys buy a digital copy of any game, they run the risk of not being able to play it in a few years time. Why? Because Corpo Monkeys"

## 10. Title audit list (all items with assigned sub-niche)

<details><summary>Show all 136 titles</summary>

| Date | T | Views | Sub-niche | Title |
|---|---|---:|---|---|
| 2026-11-14 | S | 17,158 | Debt, Fed & inflation | They're ALL Unprofitable... #finance #inflation #debt |
| 2026-11-13 | S | 14,825 | AI & tech bubble | Even The Banks Are Scared of The AI Bubble #finance #investing |
| 2026-11-12 | S | 8,884 | AI & tech bubble | South Korea's AI Bubble Is A Warning #kospi #finance #economics |
| 2026-11-11 | S | 15,727 | AI & tech bubble | What happens if the AI Bubble Pops? #finance #crash #economics |
| 2026-11-11 | L | 1,053,556 | AI & tech bubble | The AI Bubble Just Claimed Its First Victim |
| 2026-11-10 | S | 15,816 | AI & tech bubble | What Happens When Funding Runs Out? #ai #finance #economics |
| 2026-11-10 | M | — | AI & tech bubble | (Member Edition) If Everyone Loves Meta's AI, Why Did The Stock Crash? |
| 2026-11-09 | S | 15,539 | AI & tech bubble | OpenAI's Business Model Sucks, Actually #openai #finance #economics |
| 2026-11-08 | S | 17,040 | AI & tech bubble | How Nvidia ALWAYS Wins #nvidia #finance #economics |
| 2026-11-08 | S | 11,606 | AI & tech bubble | The AI Hype Train in a Nutshell #useconomy #finance #ai |
| 2026-11-07 | S | 19,851 | AI & tech bubble | OpenAI Isn't The Only AI Loser #ai #useconomy #debt |
| 2026-11-07 | S | 9,886 | AI & tech bubble | Why Hasn't the AI Bubble Popped Yet? #ai #finance #economics |
| 2026-11-06 | S | 18,739 | AI & tech bubble | If Not Bubble, Why Bubble Shaped? #ai #finance #economics |
| 2026-11-01 | L | 2,660,895 | AI & tech bubble | Why Hasn't The AI Bubble Popped (Yet)? |
| 2026-10-31 | M | — | AI & tech bubble | (Member Edition) Why Hasn't The AI Bubble Burst (Yet)? |
| 2026-10-24 | L | 191,424 | Trade, tariffs & geopolitics | The EU is Quietly Destroying The Internet |
| 2026-10-24 | M | — | Other / unclassified | (Member Edition) The "Kids Act" That Won't Protect Kids |
| 2026-10-24 | S | 11,789 | Personal finance & consumer | Will Diesel Prices Come Down in 2027? #oilprices #finance |
| 2026-10-23 | S | 12,324 | Debt, Fed & inflation | Trump's Diesel Export Ban Could Backfire #Economics #gasprices |
| 2026-10-22 | S | 9,628 | Trade, tariffs & geopolitics | The Oil Shortage Coming this Christmas #Inflation #christmas |
| 2026-10-22 | S | 9,589 | Crashes, recessions & crises | Now is the Worst Possible Time to Run Short on Diesel #fuelcrisis #economics |
| 2026-10-22 | S | 14,317 | AI & tech bubble | Why are AI Data Centers Everywhere now? #ai #animation |
| 2026-10-21 | S | 21,054 | AI & tech bubble | This Makes 0 Sense, But OpenAI keeps doing it #openai #finance |
| 2026-10-21 | S | 17,120 | Crashes, recessions & crises | Why the Whole World Is Buying America's Diesel #oilcrisis  #straitofhormuz |
| 2026-10-21 | S | 5,684 | Trade, tariffs & geopolitics | Why America Can't Just Make More Diesel #oil #economy |
| 2026-10-20 | S | 8,445 | Trade, tariffs & geopolitics | You're Already Paying for the Oil Shock #dieselprices  #costofliving |
| 2026-10-20 | S | 7,487 | Trade, tariffs & geopolitics | Is the US Really Running Out of Diesel? #dieselshortage #oil |
| 2026-10-20 | S | 34,437 | AI & tech bubble | We've all played these games before #ai #bigtech |
| 2026-10-18 | L | 282,642 | Energy, oil & commodities | The One Shortage America Can't Fix |
| 2026-10-18 | S | 38,783 | AI & tech bubble | Yes, your company probably did this too #ai #layoffs |
| 2026-10-18 | M | — | Other / unclassified | (Member Edition) The One Shortage America Can't Fix |
| 2026-10-17 | S | 21,792 | AI & tech bubble | AI isn't as good as the Corpos want you to think #investing #ai |
| 2026-10-16 | S | 43,372 | AI & tech bubble | BuT We'RE GOinG To Be PRofitabLE In 4 YeaRS! #ai #openai |
| 2026-10-15 | S | 131,980 | AI & tech bubble | OpenAI is (Probably) Not Gonna Survive #animation #openai |
| 2026-10-15 | S | 43,032 | AI & tech bubble | The AI Business Model in a nutshell #finance #economics |
| 2026-10-14 | S | 43,547 | AI & tech bubble | OpenAI's Finances Make 0 Sense  #animation #ai |
| 2026-10-14 | S | 12,096 | AI & tech bubble | No, it's not just OpenAI, it's all of them #stockmarket #ai |
| 2026-10-11 | L | 227,584 | Personal finance & consumer | The 2 Trillion Credit Wave No One Sees Coming |
| 2026-10-10 | M | — | Crashes, recessions & crises | (Member Edition) America's next debt crisis is here |
| 2026-10-04 | L | 390,894 | AI & tech bubble | If Not Bubble, Why Bubble Shaped? |
| 2026-10-04 | M | — | AI & tech bubble | (Member Edition) Big Tech Can't Hide This For Much Longer |
| 2026-09-27 | L | 408,113 | Crashes, recessions & crises | China's Unsolvable Economic Crisis |
| 2026-09-26 | M | — | Crashes, recessions & crises | (Member Edition) The One Crisis China Can't Fix |
| 2026-09-20 | L | 413,591 | Trade, tariffs & geopolitics | Is America Winning Yet? |
| 2026-09-19 | M | — | Other / unclassified | (Member Edition) Is America Winning Yet? |
| 2026-09-13 | L | 391,566 | Crashes, recessions & crises | The US Debt Crisis Has Reached a Breaking Point |
| 2026-09-12 | M | — | Crashes, recessions & crises | (Member Edition) The US Debt Crisis Is Way Worse Than It Looks |
| 2026-09-05 | L | 452,877 | AI & tech bubble | OpenAI's Financial Crisis is Worse Than You Think |
| 2026-09-03 | M | — | AI & tech bubble | (Member Edition) The OpenAI IPO ... It's Worse Than You Think |
| 2026-08-30 | L | 300,802 | Jobs, wages & labour | America's Job Market Is Completely F*cked |
| 2026-08-27 | M | — | Jobs, wages & labour | (Member Edition) America's Job Market Is Completely F*cked |
| 2026-08-15 | L | 430,580 | AI & tech bubble | South Korea's AI Bubble Crash Is Terrifying, Actually |
| 2026-08-15 | M | — | Other / unclassified | (Member Edition) South Korea Is A Warning To The World |
| 2026-08-09 | L | 410,455 | Companies, billionaires & business history | WTF Is Happening To SpaceX? |
| 2026-08-09 | M | — | Companies, billionaires & business history | (Member Edition) WTF Is Happening To SpaceX? |
| 2026-08-01 | L | 276,863 | Crashes, recessions & crises | The (Overdue) Collapse of Ubisoft |
| 2026-07-31 | M | — | Crashes, recessions & crises | (Member Edition) Ubisoft's Financial Crisis Is Worse Than It Seems |
| 2026-07-22 | L | 227,762 | Trade, tariffs & geopolitics | America is Losing The Tariff War |
| 2026-07-22 | M | — | Jobs, wages & labour | (Member Edition) Did Trump's Tariff War Work? |
| 2026-07-14 | L | 433,617 | AI & tech bubble | Meta's Disturbing AI "Gulags" |
| 2026-07-13 | M | — | AI & tech bubble | (Member Edition) Meta's AI Crash Has Just Begun |
| 2026-07-06 | L | 585,401 | AI & tech bubble | OpenAI's Financial Crisis Keeps Getting Worse |
| 2026-07-06 | M | — | AI & tech bubble | (Member Edition) OpenAI Finances Just Leaked. We're Cooked |
| 2026-06-30 | M | — | Non-finance (gaming/social/tech culture) | (Member Edition) The UK Just Hijacked Your YouTube Feed |
| 2026-06-30 | L | 119,857 | Non-finance (gaming/social/tech culture) | The UK is Colonising YouTube |
| 2026-06-23 | L | 999,806 | Companies, billionaires & business history | The SpaceX Bubble Crash Is Worse Than It Looks |
| 2026-06-23 | M | — | Companies, billionaires & business history | (Member Edition) The SpaceX Bubble Crash Is Worse Than It Looks |
| 2026-06-20 | L | 169,661 | Government, politics & policy | Who Even Asked For This? |
| 2026-06-20 | M | — | Other / unclassified | (Member Edition) The Trump Phone Is Worse Than You Think |
| 2026-06-05 | L | 137,778 | Non-finance (gaming/social/tech culture) | The Embarrassing Apestein File Situation |
| 2026-06-04 | M | — | Other / unclassified | (Member Edition) Why Haven't We Had Apestein File Arrests Yet? |
| 2026-05-31 | L | 144,038 | Trade, tariffs & geopolitics | The US Military Industrial Complex Explained with Bananas |
| 2026-05-31 | M | — | Companies, billionaires & business history | (Member Edition) How the US Made Peace Bad For Business |
| 2026-05-24 | L | 88,487 | Investing, stocks & crypto | The REAL Wolf of Wall Street is Still Scamming People Today |
| 2026-05-23 | M | — | Investing, stocks & crypto | (Member Edition) The Wolf of Wall Street Scam Is Worse Than You Think |
| 2026-05-18 | M | — | Other / unclassified | (Member Edition) America's DOJ Is Collapsing |
| 2026-05-18 | L | 107,512 | Government, politics & policy | The US DOJ Is Imploding |
| 2026-05-09 | L | 164,478 | Crashes, recessions & crises | The Commodity Crisis Hiding In Plain Sight |
| 2026-05-07 | M | — | Personal finance & consumer | (Member Edition) The Commodity Price Shock Is About To Hit |
| 2026-04-30 | L | 222,696 | AI & tech bubble | OpenAI Just Can't Stop Taking Ls |
| 2026-04-29 | M | — | Other / unclassified | (Member Edition) SORA Never Stood A Chance |
| 2026-04-26 | L | 102,187 | Trade, tariffs & geopolitics | Who's Getting Rich from the Iran War? |
| 2026-04-26 | M | — | Trade, tariffs & geopolitics | (Member Edition) Who's Getting Paid From The Iran War? |
| 2026-04-18 | L | 194,717 | Trade, tariffs & geopolitics | Oh Great, Another War In the Middle East... |
| 2026-04-16 | M | — | Trade, tariffs & geopolitics | (Member Edition) The US Petrodollar War Explained using Bananas |
| 2026-04-11 | L | 153,165 | AI & tech bubble | Pentagon VS Anthropic Explained in 14 Minutes |
| 2026-04-08 | M | — | AI & tech bubble | (Member Edition) The Pentagon’s AI Scandal Keeps Getting Worse |
| 2026-04-05 | L | 353,570 | Non-finance (gaming/social/tech culture) | How AAA Turned Your Favourite Games Into Slop |
| 2026-04-04 | M | — | Crashes, recessions & crises | (Member Edition) The (Overdue) Collapse of The AAA Gaming Industry |
| 2026-03-29 | L | 240,788 | AI & tech bubble | Is OpenAI Going to Bankrupt Big Tech? |
| 2026-03-27 | M | — | AI & tech bubble | (Member Edition) OpenAI's Debt Crisis Keeps Getting Worse |
| 2026-03-20 | L | 90,109 | AI & tech bubble | The AI Influencer Epidemic Keeps Getting Worse |
| 2026-03-19 | M | — | AI & tech bubble | (Member Edition) TikTok's AI Influencer Crisis Keeps Getting Worse |
| 2026-03-15 | L | 144,400 | Investing, stocks & crypto | The Global Scam Industry Keeps Getting Worse |
| 2026-03-15 | M | — | Investing, stocks & crypto | (Member Edition) Inside Asia's $44 Billion Scam Cities |
| 2026-03-08 | L | 185,160 | Crashes, recessions & crises | The Greenland Crisis was Dumber Than You Think |
| 2026-03-08 | M | — | Other / unclassified | (Member Edition) Why The US Suddenly Wants Greenland |
| 2026-02-28 | L | 443,344 | AI & tech bubble | The AI Data Center Crisis is Worse Than You Think |
| 2026-02-28 | M | — | AI & tech bubble | (Member Edition) How AI Data Centers are Eating The World |
| 2026-02-22 | L | 140,133 | Debt, Fed & inflation | The Fed Lawsuit is Worse Than You Think |
| 2026-02-13 | L | 838,476 | Companies, billionaires & business history | How did Apestein Get So Rich? |
| 2026-02-08 | L | 342,542 | Debt, Fed & inflation | The US Gold Card Scam Is Worse Than You Thought |
| 2026-01-25 | L | 276,070 | Housing & real estate | The US Housing Bubble Explained with Bananas |
| 2026-01-18 | L | 687,982 | Personal finance & consumer | RAM Prices Are Worse Than You Think |
| 2026-01-03 | L | 144,487 | Trade, tariffs & geopolitics | The EA-Saudi Buyout is Worse Than You Think |
| 2025-12-21 | L | 139,006 | Trade, tariffs & geopolitics | The U.S Venezuela Attack is Worse Than You Thought |
| 2025-12-04 | L | 1,325,113 | AI & tech bubble | The OpenAI Bubble is Worse Than You Think |
| 2025-11-26 | L | 431,300 | AI & tech bubble | Microsoft is Worse Than You Thought |
| 2025-11-21 | L | 182,509 | Non-finance (gaming/social/tech culture) | So... THIS is why Countries are Banning Social Media |
| 2025-11-14 | L | 140,434 | Non-finance (gaming/social/tech culture) | The Discord Data Leak Is Worse Than You Thought |
| 2025-11-07 | L | 212,281 | Crashes, recessions & crises | The 2008 Financial Crisis Explained Using Bananas |
| 2025-10-29 | L | 725,803 | Government, politics & policy | The US Shutdown Explained Using Bananas |
| 2025-10-17 | L | 478,910 | Trade, tariffs & geopolitics | The Indonesian Gen-Z Protests Explained Using Bananas |
| 2025-10-11 | L | 172,429 | Non-finance (gaming/social/tech culture) | Roblox's Dark Predatory Side Explained in 13 Minutes |
| 2025-09-12 | L | 666,463 | Investing, stocks & crypto | Explaining how 2 Companies Ruined the Credit Card Market |
| 2025-09-04 | L | 518,239 | Debt, Fed & inflation | The Fed Rate Cut Saga Explained using Bananas |
| 2025-08-22 | L | 149,139 | Government, politics & policy | A Monkey's Guide to Lobbying the U.S Government |
| 2025-08-14 | L | 500,813 | Jobs, wages & labour | The South Korean Population Disaster Explained using Monkeys |
| 2025-08-09 | L | 387,530 | Government, politics & policy | The Big Beautiful Bill Explained Using Bananas |
| 2025-07-30 | L | 141,683 | Investing, stocks & crypto | 401k Explained Using Bananas |
| 2025-07-22 | L | 181,529 | AI & tech bubble | Artificial Intelligence Explained Using Bananas |
| 2025-07-11 | L | 717,058 | Non-finance (gaming/social/tech culture) | Stop Killing Games Explained Using Bananas |
| 2025-06-29 | L | 190,997 | Investing, stocks & crypto | How Congress ALWAYS Wins on the Stock Market Explained with Bananas |
| 2025-06-23 | S | 24,313 | Debt, Fed & inflation | US National Debt Keeps Growing #finance #debt #economics |
| 2025-06-21 | S | 36,542 | Debt, Fed & inflation | US National Debt Explained with Bananas #finance #animation #debt |
| 2025-06-20 | L | 92,274 | Non-finance (gaming/social/tech culture) | Drug Trafficking Explained using Bananas |
| 2025-06-13 | S | 8,673 | Debt, Fed & inflation | art market tax evasion explained #finance #animation #crime |
| 2025-06-13 | L | 1,920,233 | Debt, Fed & inflation | The US National Debt Crisis Explained with Bananas |
| 2025-06-12 | S | 5,668 | Debt, Fed & inflation | Tax Evasion explained using Bananas #finance #crimestory #animation  #money |
| 2025-06-12 | S | 6,375 | Trade, tariffs & geopolitics | Tariffs Explained #finance #tariffs #finance #economics |
| 2025-06-11 | S | 4,242 | Trade, tariffs & geopolitics | Tariff Wars #tariffs #finance #internationaltrade |
| 2025-06-11 | S | 3,771 | Debt, Fed & inflation | art market scam exaplained #finance #crime #taxes |
| 2025-06-06 | L | 130,484 | Investing, stocks & crypto | The Art Market Scam Explained Using Bananas |
| 2025-06-01 | L | 652,686 | Trade, tariffs & geopolitics | Tariff Wars Explained Using Bananas |
| 2025-05-26 | S | 18,460 | Investing, stocks & crypto | Money Laundering Explained #animation #finance #money #investing |
| 2025-05-26 | L | 273,970 | Investing, stocks & crypto | Money Laundering Explained Using Bananas |

</details>

