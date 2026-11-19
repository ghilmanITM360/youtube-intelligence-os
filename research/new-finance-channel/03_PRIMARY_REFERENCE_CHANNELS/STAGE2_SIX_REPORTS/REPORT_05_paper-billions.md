# Forensic report 05: Paper Billions

Stage 2, 2026-11-19. Scope: this channel only, from `finance_economics_complete.db` (read-only). Data builder: `build_data.py`. Classified video list: `data/paper-billions_classified.csv`.

**Evidence labels:** VERIFIED = read from the DB or raw Apify file. INFERRED = our reading of a pattern. HYPOTHESIS = untested idea. NOT AVAILABLE = no data or media in this workspace. Views are public counts as of the pull dates (2026-11-17 to 2026-11-19). Shorts = duration <= 180 s. No view count proves a cause; there is no CTR or retention data.

# Part 1. Reading

## A. Reading of the channel (INFERRED)

PaperBillionsTV has 6 long videos, all uploaded 2026-11-06 to 2026-11-17 (12 days). Together 6.11M views, median 709,991, 14 to 24 min each. Videos are very young (age 2 to 13 days), so the numbers are launch numbers, not settled performance. The channel looks launched with a pre-produced batch: 3.8 uploads a week over 11 days, a pace not seen anywhere else in the set. Stage 1 confirmed that 6 is the complete inventory.

## B. Finance AND Economics coverage

- All 6 videos are Finance: AI/Nvidia/Anthropic stories (4 videos about Nvidia, Google or AI chips, 4.69M views; plus the Anthropic IPO video), one markets video ("Why the Stock Market Just Crashed" 1.20M), one IPO video ("The Biggest IPO in History Lost $80 Billion" 224K, about Anthropic).
- Economics: none as a topic. The market-crash video is the only macro-adjacent piece; it explains an Nvidia-driven sell-off and not a data release.
- This leaves Economics as a documented gap at this channel (no housing, no rates, no jobs).

## C. Winning and failing topics

- Winner (>= 2x median 709,991): "How a Chinese Spy Got Inside Nvidia" 3.24M (4.6x, 2026-11-10). Strong follow-ups: Jensen Huang 1.35M (2026-11-13), stock-market crash 1.20M (2026-11-08).
- Weak: the two sequel videos about the Chinese-spy theme at 88K and 18K (2026-11-15 and 2026-11-17), and the Anthropic IPO video at 224K. The sequel pair were published only 2 to 4 days ago, so their numbers are not final. HYPOTHESIS: audience fatigue on a repeated theme within a week; alternative: they are simply young.
- No failure can be defined yet (no video older than 60 days).

## D. Title structures

- 5 of 6 start with how/why/what: "How a Chinese Spy Got...", "Why Nvidia Would Fail Without Jensen Huang", "Why the Stock Market Just Crashed" (the beginning-with-how/why group has median 1.20M).
- Titles name a person or company and a surprising claim; no ellipses, questions, years or second person. The $ figure ("$80 Billion", "$77.5 Billion") appears in 2 of 6 and both are lower than the others (88K, 224K), so a big number alone does not carry a title in this sample.
- Median 7 words.

## E. Thumbnail patterns

Source: 6-image sample (thumbnail model doc): dark background with red and green glow, large caricature of real people (Jensen Huang), numeric overlay ("-$80 BILLION", "NVIDIA -$400B"), panic/sweat expressions. The model doc flagged sensational and sexualised framing in some thumbnails ("BLACKMAIL?", dinner-date framing) as not a model for a serious channel. INFERRED.

## F. Script and hook structure (VERIFIED text, INFERRED structure)

Two hook types. (1) Scene-first thriller: "In Singapore, the boss of the most valuable company on Earth is having dinner with a Chinese spy... American agents are taking pictures. Jensen has no idea." (2) Protagonist formula: "This is Jensen. And Jensen has a huge problem." and "This is Leon. And Leon has three jobs." — this is the same opening formula that MonkeyExplains uses ("This is Sam, and he's got a huge problem"); 2 of 6 PaperBillions videos use it. Other openings give a loss figure first: "On Thursday, Nvidia lost more than four hundred billion dollars in a single morning, and it hadn't done anything wrong." The scripts use character-and-intrigue storytelling for finance news.

## G. Visual storytelling and editing

NOT AVAILABLE (no video files analysed).

## H. Shorts vs long-form and frequency

No Shorts. 6 long in 12 days. Do not treat 3.8 per week as a sustainable cadence: the whole history is 11 days and the batch is probably pre-produced (INFERRED, no evidence of production method). Days of upload: 2026-11-06, 08, 10, 13, 15, 17, i.e. every 2 to 3 days.

## I. Implications for our channel (HYPOTHESIS)

1. A launch batch at roughly one video every two days produced 6.1M views in 12 days, but we have no evidence that cadence was a cause. 2. Story-first finance news about a single famous company/person outperforms the abstract. 3. The "This is X, and he has a huge problem" formula is shared by two channels, so it is becoming a category trope and should not be our hook. 4. Real-person caricature and clickbait thumbnails are policy and brand risks to avoid.

## J. Limits

n = 6; all videos under 14 days old; no longitudinal view data. DB held only one snapshot of views. No media analysis.


# Part 2. Data tables

## 1. Full inventory (VERIFIED from DB)

- Videos held: **6** (long-form 6, Shorts 0 by duration <= 180 s). Date range 2026-11-06 to 2026-11-17.
- With public view counts: 6. Transcripts held: 6 of 6.
- Views, long-form: total 6,114,081, median 709,991, mean 1,019,013, max 3,237,543.
- Median long-form duration: 16 min 41 s.

## 2. Top videos

### Top 15 long-form
| # | Views | Date | Dur | Category | Title |
|---:|---:|---|---:|---|---|
| 1 | 3,237,543 | 2026-11-10 | 19:48 | AI & tech bubble | [How a Chinese Spy Got Inside Nvidia](https://www.youtube.com/watch?v=_MG4v3foET8) |
| 2 | 1,350,908 | 2026-11-13 | 14:20 | AI & tech bubble | [Why Nvidia Would Fail Without Jensen Huang](https://www.youtube.com/watch?v=Vy1m4ZXNzpo) |
| 3 | 1,196,142 | 2026-11-08 | 15:00 | Crashes, recessions & crises | [Why the Stock Market Just Crashed](https://www.youtube.com/watch?v=zEUKLSrbRZk) |
| 4 | 223,840 | 2026-11-06 | 14:08 | Investing, stocks & crypto | [The Biggest IPO in History Lost $80 Billion](https://www.youtube.com/watch?v=hPCywNDA60o) |
| 5 | 87,918 | 2026-11-15 | 24:10 | AI & tech bubble | [How a Chinese Spy Got $77.5 Billion of Nvidia Chips](https://www.youtube.com/watch?v=DLNT1JfIf6I) |
| 6 | 17,730 | 2026-11-17 | 18:22 | AI & tech bubble | [Why Google Hired a Chinese Spy](https://www.youtube.com/watch?v=X-hlJ0fdBM4) |

## 3. Recent uploads (newest 12, any type)

| Date | Type | Views | Age (d) | Title |
|---|---|---:|---:|---|
| 2026-11-17 | Long | 17,730 | 2 | Why Google Hired a Chinese Spy |
| 2026-11-15 | Long | 87,918 | 4 | How a Chinese Spy Got $77.5 Billion of Nvidia Chips |
| 2026-11-13 | Long | 1,350,908 | 6 | Why Nvidia Would Fail Without Jensen Huang |
| 2026-11-10 | Long | 3,237,543 | 9 | How a Chinese Spy Got Inside Nvidia |
| 2026-11-08 | Long | 1,196,142 | 11 | Why the Stock Market Just Crashed |
| 2026-11-06 | Long | 223,840 | 13 | The Biggest IPO in History Lost $80 Billion |

## 4. 30 / 60 / 90-day patterns (to 2026-11-19)

| Window | Uploads | Long | Shorts | Long views median | Long views total | Per week |
|---|---:|---:|---:|---:|---:|---:|
| last 30 d | 6 | 6 | 0 | 709,991 | 6,114,081 | 1.4 |
| last 60 d | 6 | 6 | 0 | 709,991 | 6,114,081 | 0.7 |
| last 90 d | 6 | 6 | 0 | 709,991 | 6,114,081 | 0.5 |
| last 180 d | 6 | 6 | 0 | 709,991 | 6,114,081 | 0.2 |
| last 365 d | 6 | 6 | 0 | 709,991 | 6,114,081 | 0.1 |

Monthly uploads (last 14 active months): 2026-11: 6L/0S

Long-form upload weekday: Tue 2, Fri 2, Sun 2

## 5. Finance / Economics categories and sub-niche distribution

Classification: title-keyword rules (`build_data.py`), then **audited by reading the titles** (section 9). Labels are INFERRED, not channel-declared.

| Sub-niche | F/E | Long n | Long median views | x channel median | Long total views | Shorts n |
|---|---|---:|---:|---:|---:|---:|
| AI & tech bubble | Finance | 4 | 719,413 | 1.01 | 4,694,099 | 0 |
| Crashes, recessions & crises | Finance | 1 | 1,196,142 | 1.68 | 1,196,142 | 0 |
| Investing, stocks & crypto | Finance | 1 | 223,840 | 0.32 | 223,840 | 0 |

Finance vs Economics (long-form, public views): Finance: 6 videos / 6,114,081 views

## 6. Winning and failing topics (long-form, relative to channel long median 709,991)

- Winners (>= 2x median): **1** of 6; breakouts (>= 5x): **0**; failures (<= 0.5x, older than 60 d): **0** of 0.
- Winners by sub-niche: AI & tech bubble 1.
- Failures by sub-niche: none.

Breakouts:


Lowest long-form (older than 60 d):


## 7. Title structures (long-form)

| Feature | Share of long titles | Median views with | Median views without |
|---|---:|---:|---:|
| Question mark | 0% | 0 | 709,991 |
| Contains a digit | 33% | 155,879 | 1,273,525 |
| Colon | 0% | 0 | 709,991 |
| Ellipsis | 0% | 0 | 709,991 |
| ALL-CAPS word | 17% | 223,840 | 1,196,142 |
| Year | 0% | 0 | 709,991 |
| Starts with how/why/what/is… | 83% | 1,196,142 | 223,840 |
| Addresses you/we | 0% | 0 | 709,991 |
| Negative/threat word | 33% | 787,374 | 642,030 |

Median title length 7 words (top-10 median 7). Feature medians are descriptive; they do not show causation.

## 8. Shorts vs long-form and upload frequency

- Long-form: 6 items, median views 709,991. Shorts: 0 items, median views 0.
- Whole-history cadence: 3.82 uploads/week (3.82 long, 0.00 Shorts) over 11 days.

## 9. Hook data (first ~60 words of transcript, top 8 long-form)

- **How a Chinese Spy Got Inside Nvidia** (3,237,543): "In Singapore, the boss of the most valuable company on Earth is having dinner with a Chinese spy. He's Jensen Huang, who runs Nvidia. She's Alice Huang, no relation, and she runs one of his biggest customers. But here's the strange part. Somewhere nearby, American agents are taking pictures. They know exactly who she is. Jensen has no idea. To"
- **Why Nvidia Would Fail Without Jensen Huang** (1,350,908): "This is Jensen. And Jensen has a huge problem. For thirty-three years, he built one company. It almost went broke, and he saved it. He bet a huge share of his profits on software nobody wanted, and waited ten years to be right. He turned a video game chip maker into the most valuable company on Earth. Thirty-three years. And"
- **Why the Stock Market Just Crashed** (1,196,142): "On Thursday, Nvidia lost more than four hundred billion dollars in a single morning, and it hadn't done anything wrong. Nobody had. No bank failed. No law passed. The economy looked fine. The S&P five hundred still lost more than two trillion dollars by midmorning. And the Nasdaq needed just six minutes to give back a rally that was one"
- **The Biggest IPO in History Lost $80 Billion** (223,840): "In the first six months of this year, the company behind Claude lost eighty billion dollars. That's about eighteen million dollars an hour. Nights included. And Wall Street's answer? We want in. Because Anthropic is about to sell itself to the public, in the biggest IPO ever planned. Wait. It lost how much? Eighty billion. Okay. Where do I tap?"
- **How a Chinese Spy Got $77.5 Billion of Nvidia Chips** (87,918): "This is a love letter. And it's the most expensive one ever sent. Inside are two hundred and forty thousand Nvidia chips. Seven and a half billion dollars of them. The kind America banned China from buying. The man holding it is Jensen Huang, who built the most valuable company on Earth. The woman it's going to is a Chinese"
- **Why Google Hired a Chinese Spy** (17,730): "This is Leon. And Leon has three jobs. Job one: he's an engineer at Google, on the supercomputers that train its AI. Job two: he's the technology chief of an AI startup in Beijing. Job three: he's the boss of his own AI company in Shanghai. Google only knows about the first one. Where are you going? Lunch. For how"

## 10. Title audit list (all items with assigned sub-niche)

<details><summary>Show all 6 titles</summary>

| Date | T | Views | Sub-niche | Title |
|---|---|---:|---|---|
| 2026-11-17 | L | 17,730 | AI & tech bubble | Why Google Hired a Chinese Spy |
| 2026-11-15 | L | 87,918 | AI & tech bubble | How a Chinese Spy Got $77.5 Billion of Nvidia Chips |
| 2026-11-13 | L | 1,350,908 | AI & tech bubble | Why Nvidia Would Fail Without Jensen Huang |
| 2026-11-10 | L | 3,237,543 | AI & tech bubble | How a Chinese Spy Got Inside Nvidia |
| 2026-11-08 | L | 1,196,142 | Crashes, recessions & crises | Why the Stock Market Just Crashed |
| 2026-11-06 | L | 223,840 | Investing, stocks & crypto | The Biggest IPO in History Lost $80 Billion |

</details>

