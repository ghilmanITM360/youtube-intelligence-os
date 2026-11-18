# Phase B: primary reference channels, strength matrix and learnings (2026-11-18)

Data: `data/catalog/finance_economics_complete.db` after R1-R3 (read-only), public views only. Script: `channel_metrics.py`; outputs `CHANNEL_METRICS_2026-11-18.csv`, `TOP_LONGFORM_VIDEOS_2026-11-18.csv`; thumbnails and montages in `07_THUMBNAIL_LIBRARY/primary/` (61 public thumbnails, 7 MB, manifest included). Labels: VERIFIED (counted from data or looked at) / INFERRED / HYPOTHESIS / NA (no evidence collected).

Limits that apply to every row: views are not CTR or retention; long videos are compared with the channel's own long-form median; videos less than 14 days old are left out of "outlier" counts; "Shorts" = type SHORT or 60 s or less; Shorts thumbnails in the DB are letterboxed crops, so they say nothing about packaging; hook lines are counted on the first 40 transcript words (a proxy); samples are small for Capital Case (13 videos) and Paper Billions (6 videos). Selection bias: channels were chosen because they perform.

## 1. Numbers (VERIFIED from DB)

| Channel | Subs | Videos (long / Shorts) | Items per 30 d (last 90 d) | Long median views | Shorts median views | Median long length | Long outliers (2x own median) | Title has number |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| Casual Finance | 440K | 223 (38 / 185) | 18.3 | 559,520 | 22,298 | 12.9 min | 24% | 16% |
| Monkey Economics | 224K | 60 (18 / 42) | 1.0 | 10,244 | **913,379** | 8.2 min | 24% | 28% |
| MonkeyExplains | 261K | 71 with views (51 / 20; the DB holds 73, 2 have no view count) | 7.7 | 353,570 | 16,487 | 14.1 min | 14% | 8% |
| Crayon Capital | 319K | 35 (35 / 0) | 2.3 | 301,336 | n/a | 15.3 min | 27% | 71% |
| Capital Case | 12K | 13 (13 / 0) | 1.3 | 54,627 | n/a | 11.5 min | 38% | 77% |
| Paper Billions | 23.6K | 6 (6 / 0) | 2.0 (6 videos in 12 days) | 709,991 | n/a | 16.7 min | n/a (too new) | 33% |

Same engine, opposite format: Monkey Economics earns its reach in Shorts (median 913K, top 7.7M) while its long videos median 10K; Casual Finance is the reverse (long median 560K, Shorts 22K).

Cadence note: "items per 30 d" divides the last 90 days by 3, so it understates channels that are younger than 90 days or were scraped only for their newest videos (Paper Billions has 6 videos in 12 days; PENNY, in the other file, has 21 in 30 days against a printed 7.3). The channel_metrics.py figures were recomputed from the DB on 2026-11-18 and match this table (audit pass).

## 2. Strength matrix (primary six)

| Channel | Topic selection | Visual editing | Storytelling | Titles | Thumbnails | Scripts | Best contribution to us |
|---|---|---|---|---|---|---|---|
| Casual Finance | Live macro/housing/market stress; one theme chased for weeks (housing crisis); 13 items in 30 d | NA here (repo has a separate editing forensic for this channel; not re-read) | Starts with a precise number or fact, then a contradiction ("prices should fall, except they haven't") | Short statement, no question (5%), few numbers (16%) | One short sentence in handwriting font plus one real chart with a year marker (2026) and a recurring map/character; same layout repeated | Opening of the top video: 58% sellers vs buyers, Redfin since 2013, then "except" | Data-chart-first packaging and topic cadence on one running story |
| Monkey Economics | Everyday money mechanics (banks, minimum wage, money laundering) as Shorts; long videos on rates and inflation | NA | Monkey characters act out the mechanism; long script opens with "Monkey walks through the jungle office" | Fragments ending "..." ; 22% start with Why/How/What | Long: text + monkey + chart; Shorts: no thumbnail value | Second-person is rare in hooks (11%) | Short-form mechanism explainers and the proof that a character can carry millions of Shorts views (7.7M top) |
| MonkeyExplains | One theme, AI bubble, across long and Shorts: 7 of the last 90 days' titles contain "bubble" | NA | Cast of animal characters; opening names a character with a "huge problem" | Hook words like "Worse Than You Think", "(Yet)?"; 14% questions | Gorilla characters, big red falling chart, 2-4 words in all caps with a stat badge ("15.28%") | 10% of openings (first 40 words) contain a question; 4% use "you" (n=48 long videos; an earlier draft wrongly printed "48%", which was the sample size) | Theme serial (the same story told from many angles) and the stat-badge thumbnail |
| Crayon Capital | Famous stories and companies with a "Explained Like You're 5" frame: Wolf of Wall Street 4.2M, Great Depression 2.8M, 2008 crisis 2.3M; now tied to news (NVIDIA scandal, Anthropic) | NA | Story-first openings: one-line stakes then a dated scene ("Bayside, Queens, 1962") | Number or title-template in 71% | Same character in glasses, big single word (ROCKEFELLER, Anthropic), glowing object, rich background | 91% of openings carry a number or big claim | Reusable series title template and proof that history+company stories scale to millions |
| Capital Case | Same history/company set (Rockefeller, Great Depression, WWII, Hormuz, BYD) with "Explained in N Minutes" | NA | Opens with a record or consequence ("controlled 90% of America's oil") | Number in 77% | Close visual copy of the Crayon style: a big word plus 2 to 3 cartoon people | 85% of openings contain a number | A 12K-subscriber channel reaching 54K median shows the format works at small scale; also a warning about look-alikes |
| Paper Billions | One news story at a time, framed as a spy/crime/money drama (Nvidia: 3.2M and 1.35M; stock-market crash 1.2M; corrected 2026-11-18 audit, the 1.2M video is not about Nvidia) | NA | Opens in a specific place and moment ("In Singapore, ... having dinner with a Chinese spy") | 83% start with Why/How; dollar amounts in the thumbnail text | Dark, glowing scene; one caricatured person with a shocked face; one big red or white number ("-$80 BILLION", "$2 BILLION OF CHIPS") | Scene-led, no greeting | Grew 14.1K (2026-11-13 scrape) to 23.6K subs (2026-11-18); it is the only channel with a before/after pair, so "fastest-growing" is NOT shown; packaging formula of person + object + number |

Visual-editing column is NA on purpose: this pass looked at thumbnails and transcripts only. Motion, pacing and animation style were not analysed here.

## 3. What the thumbnails show (looked at all six montages)
- Casual Finance and MonkeyExplains/Monkey Economics use a hand-drawn, flat, chart-led look with a few words; Crayon Capital, Capital Case and Paper Billions use a polished, high-contrast, cartoon-character look with one big word or number.
- Three of the six (Crayon, Capital Case, Paper Billions) share a family look: round-headed cartoon people, big glasses or exaggerated faces, dark dramatic backgrounds. Looking alike is also a risk: our channel must not copy any of these characters or layouts (originality and "inauthentic content" exposure, see Phase A).
- Common devices across the strongest packages: one dominant word or number; one character with a clear emotion; one object that makes the story concrete (zipper, bell, chip, flame); a real chart with a year marker in the macro channels.

## 4. Topic evolution (INFERRED from titles, last 90 days)
- Casual Finance: market, America, crisis, debt, housing. MonkeyExplains: bubble, OpenAI. Paper Billions: Nvidia, spy, Chinese. Crayon Capital: "Explained Like You're 5", tech and company stories (TSMC, Tesla, BYD, Nvidia). Capital Case: history plus companies (Rockefeller, Rothschilds, BYD, OpenAI).
- Overlap in the same weeks: AI/Nvidia/OpenAI (MonkeyExplains, Crayon Capital, Paper Billions, Capital Case), SpaceX IPO (Casual Finance, MonkeyExplains), housing (Casual Finance). These are crowded news topics; the 11-14 screening already rejected most such topics for a new channel.

## 5. Combined intelligence framework (HYPOTHESES for Phase F, none tested on our own channel)
1. **One running story, many angles** (Casual Finance housing, MonkeyExplains AI bubble) beats one-off topics on cadence and recognition; needs a story that stays current.
2. **Concrete mechanism or person-and-event beats abstract concept** (Paper Billions' spy dinner, Crayon's Wolf of Wall Street, Casual Finance's 58% figure): open with the specific fact, not a greeting or question.
3. **Format by job**: Shorts for mechanisms and reach (Monkey Economics), long form for depth (Casual Finance, Crayon). Our earlier "no Shorts in the first 10" rule is not supported by this data, but no source proves Shorts help long-form growth (HYPOTHESIS).
4. **Packaging**: one big word or number, one emotion, one object; keep text in the thumbnail different from the title.
5. **Differentiation requirement**: the current leaders already own the cartoon-character look; ours needs its own visual system and sourcing (charts, filings) to avoid look-alike risk.

## 6. Not yet done in Phase B
Frame-level editing/animation analysis, comment analysis, Studio data (UNKNOWN permanently for competitors), the Monkey Economics channel report (it has no folder in the old forensics package), and reading more than the top video's opening per channel. Next: additional-channel learnings (`04_ADDITIONAL_FINANCE_CHANNELS/`).
