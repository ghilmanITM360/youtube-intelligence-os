# Phase C: sub-niche discovery (2026-11-18)

Data: `data/catalog/finance_economics_complete.db` after R1-R3, read-only; 3,404 dated long-form videos (Mr. Finance's 82 excluded, anomaly) from 71 channels (Shorts excluded; 28 videos undated). Script: `subniche_metrics.py`; outputs in this folder (`SUBNICHE_METRICS_2026-11-18.csv`, `PRIMARY_CHANNEL_BY_SUBNICHE_2026-11-18.csv`, `TOP_VIDEOS_BY_SUBNICHE_2026-11-18.csv`, `CLASSIFICATION_AUDIT_SAMPLE_2026-11-18.csv`).

## Method and limits (read first)
- Sub-niche = first matching keyword rule on the **title only** (INFERRED). I hand-read about 8 titles per bucket: most fit, but some do not (e.g. Housing holds senior-benefit titles; "Economic history" is mostly noise). 12% of videos stay Unclassified. Treat bucket sizes as rough (plus or minus a few points), not exact.
- "Ratio" = video views divided by that channel's own long-form median (channels with 8+ long videos only, videos 14+ days old). It removes channel size; 1.0 means typical for the channel. Public views only, not CTR or retention.
- "Small channels" = under 100K subscribers. Several channels show 0 subscribers (not collected), so they drop out of that column. Note: ratio medians use each channel's own median, so channels with very low medians inflate outliers.
- The set was chosen because channels perform, so it shows what works for these channels, not total market demand. **Demand (Trends, News, YouTube search) is UNKNOWN until Phase D; nothing here is a validated topic.**

Independence caveat (audit 2026-11-18): 89 titles appear on more than one channel (copy-style and pipeline channels; for example one "Never Keep More Than This in the Bank After 65" title sits on 5 channels). Those rows are not independent evidence, so bucket counts and medians can be inflated in the crowded retirement and personal-finance buckets. They were not removed.

## 1. Sub-niche map (long-form)

| Sub-niche | Videos | Channels | Median ratio | % at 2x+ own median | Small-channel median views (channels) | Videos last 90 d (channels) |
|---|---:|---:|---:|---:|---:|---:|
| Retirement, pensions and senior money | 917 | 39 | 1.07 | 33% | 5.2K (26) | 537 (30) |
| Personal finance and wealth | 765 | 57 | 1.05 | 30% | 2.7K (35) | 316 (40) |
| Unclassified | 419 | 57 | 0.98 | 27% | 3.5K (34) | 200 (48) |
| Wealth POV / fiction stories | 332 | 15 | 1.09 | 34% | 6.4K (8) | 228 (11) |
| Central banks, rates, inflation, debt | 159 | 51 | 0.99 | 34% | 4.0K (28) | 76 (32) |
| Business economics ("Economics of owning X", how X makes money) | 77 | 9 | **1.34** | **37%** | 6.4K (7) | 20 (6) |
| Jobs, wages, cost of living | 147 | 38 | 1.03 | 27% | 2.6K (22) | 60 (24) |
| Housing and real estate | 147 | 45 | 0.97 | 28% | 2.2K (26) | 58 (24) |
| AI and big-tech | 83 | 25 | 1.03 | 21% | 3.4K (12) | 42 (17) |
| Stock market and companies | 71 | 30 | 0.81 | 29% | 3.4K (15) | 29 (16) |
| Geopolitics, trade, energy | 60 | 18 | 0.80 | 14% | 9.2K (7) | 21 (10) |
| Economics concepts (ELI5) | 57 | 24 | 0.73 | 19% | 2.7K (12) | 18 (10) |
| Industry, logistics, infrastructure | 51 | 10 | 1.00 | 29% | **37.1K (7)** | 16 (4) |
| Crashes, crises, bubbles | 50 | 24 | 1.11 | 31% | 3.1K (8) | 20 (14) |
| Economic history and systems | 49 | 18 | 0.70 | 28% | 4.0K (11) | 27 (11) |
| Crypto, gold, commodities | 21 | 11 | 0.68 | 11% | 0.6K (3) | 8 (4) |

## 2. What the numbers say (INFERRED)
1. **The sub-niche barely predicts performance.** Median ratios sit between 0.68 and 1.34 (an earlier draft said 1.5, a figure from before Mr. Finance was excluded); 9 of 16 are within 0.95-1.1. Packaging, channel and the specific story matter more than the bucket.
2. **Supply is concentrated in retirement/senior and generic personal finance** (49% of long videos: 917 + 765 of 3,405; an earlier draft said 48%, from before Mr. Finance was excluded). Their small-channel medians are low (2.7K to 5.2K) and they are mostly list or POV formats. This is where the crowd is, not where our reference channels are. The six primaries put only 1 to 4 videos each there.
3. **Two buckets stand out for small channels:**
   - *Industry, logistics and infrastructure* (ships, ports, airlines, data centres): small-channel median 37K, but only 7 channels and mostly **Neu** (40.7K subs) plus **Brimm.** Top items: Brimm. airline layout 553K (71x its own median), Neu ship graveyard 1.12M (25x). Few competitors, but this rests on two channels (HYPOTHESIS that it generalises).
   - *Business economics* ("The Economics of Owning X"): ratio 1.34, 37% of videos beat 2x (first run 1.48 and 44% included Mr. Finance; re-run without it after review). 9 channels, one repeated template (Nostalgic Wheels, Millionaire Problems, The Expensive Part). Ratios for tiny channels are fragile (Nostalgic Wheels' top item is 283x a median of 661 views). A copied template is the exact "inauthentic / mass-produced" exposure from Phase A. A mechanism-led version of the same idea is possible; the template is not.
4. **AI/big-tech, crashes and geopolitics have huge medians (200K to 410K) only because the big channels cover them** (Casual Finance, MonkeyExplains, Patrick Boyle). For small channels the medians are 3.1K to 9.2K, with 7 to 12 channels. High ceiling, crowded, and fast news cycles. A new channel competes with the same-week uploads of four primaries (Phase B).
5. **Cost-of-living, housing, rates** are broad, many channels (22 to 28 small), small-channel medians 2.2K to 4K: weak opportunity unless the angle is specific.
6. **Wealth POV / fiction** (15 channels, ratio 1.09): reach is real but it is fiction, and several of these channels lean on AI voices. Not our category (decision log: adjacent categories stay P3).

## 3. Candidate sub-niches for Phase D (shortlist, none validated)

| # | Candidate | Evidence for | Evidence against / risk | Next test |
|---|---|---|---|---|
| S1 | **How a real industry makes money (ships, airlines, ports, data centres, food, retail)** | Neu and Brimm. outliers; 10 channels only; no primary channel covers it; fits "cost of ownership" gap in earlier research | 2 channels carry the evidence; needs real sourcing per video; demand UNKNOWN | Trends/search check on 10 topic seeds; title and thumbnail comparison |
| S2 | **Company and history stories with a mechanism** (Crayon, Built On You: Amazon 471K at 16.6K subs) | Proven at 12K to 320K subs; Capital Case shows format works small | Crayon, Capital Case, Paper Billions already own the cartoon look; AI companies are crowded | Pick non-AI companies; originality check vs three look-alikes |
| S3 | **Everyday money mechanisms as Shorts plus a long follow-up** | Monkey Economics Shorts median 913K | Its long videos median 10K; Shorts to long conversion is a HYPOTHESIS; character look must be our own | Test small batch of Shorts; track Studio traffic |
| S4 | **News translated into balance sheets** (rates, housing, tariffs) | Casual Finance, Money & Macro scale | Most crowded; speed and sourcing cost; news read-out is not monetizable | Only with a distinct data angle |
| S5 | **"Economics of owning X" mechanism series** | Highest ratio (1.34 after review) | Template copying, fragile small-channel ratios, mass-produced risk | Treat as a format to learn from, not copy |

Not pursued: retirement/senior (crowded, POV/AI-persona and monetization risk), wealth POV fiction, crypto (smallest and weakest bucket).

## 4. Not done / open
- No Trends, News or YouTube search validation yet (Phase D, with dated captures). No paid Apify run was used in this phase.
- Keyword classification is title-only; transcripts and descriptions were not used. A semantic re-label (by reading) would tighten the buckets.
- Single-channel dependence (Neu, Brimm.) must be broken by finding more small channels in S1 before relying on it.
- Subscribers are missing for several small channels.
- Manual check of Mr. Finance still pending (its rows are now excluded here).
