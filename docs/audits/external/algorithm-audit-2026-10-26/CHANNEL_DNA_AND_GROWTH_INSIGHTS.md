# Channel DNA & Growth Insights — evidence-bounded (2026-10-26)

**Rules applied:**
- Each statement cites video IDs and a denominator.
- "Prevalence" means the share of a channel's titles matching a pre-registered regex (`scripts/analyze.py`).
- "Peer ratio" is lifetime views/day ÷ the median of same-channel, same-format, age-matched peers (`YIOS_VIRALITY_HYPOTHESIS_TESTS.md §1`).
- All metrics are public frozen snapshots (2026-09-11 → 10-21). No CTR, retention or traffic data exists for any channel.
- Copying any creator's exact format carries originality, rights, YPP "inauthentic/mass-produced" policy and performance risks. These profiles describe; they are not templates.

Source table: `derived/channel_dna.json`. Titles: `derived/dna_titles.json`.

## Cross-channel lessons (the strongest evidence in this report)

1. **The channel is the biggest single factor.** Channel identity explains 38% of the variance in log lifetime views/day across 11 Finance channels, and 58% across 35 channels in all niches. Within each channel, outcomes are hit-driven: the top 10% of videos carry a median 67% of views.
2. **Identical concepts flip between channels.** For example, "Your Life If You Start Building Wealth in Your 30s" is 14.8× on Sonny Finance (`uByLqFbCcEA`) and 0.14× on Lucas Grant (`6dw0y-ATdwI`). "How banks treat you at every level of wealth" is 159× on Dark Ledger (`2LXED3ENhck`) and 0.07× on Shaami Finance (`eB0XSeS7y8Q`). A concept's past success on another channel is **weak evidence** for ours.
3. **Within-channel formulas still produce both outcomes.** Nick's "Why everything changes after…" series has 20 rated videos: 7 STRONG and 2 WEAK (18.8× `2DBQnxaDScs` vs 0.28× `rbnPR2Dnmz4`). Primitive Education's "Caveman Explains Capitalism" parts range 0.28×–1.83×. A repeated series grammar is not a guarantee.
4. **Recurring cross-channel winners are decision-math questions.** "Renting vs Buying — The Real Math" (Logical Money 350×, Mark Invests 297×), "Real estate vs stocks" (36×, 102×), "the number where compounding takes over" (Carl 51×, Uncle Frank 67×) and "paying cash for cars" (Lucas Grant 29×, Money Life POV 9.7×). These share a concrete, personally consequential comparison with numbers. `PLAUSIBLE_HYPOTHESIS`: durable search/browse demand. Traffic source is unknown.

## Channel profiles (channels with ≥ 20 rated videos, plus forensic channels)

### Nick Invests (CH: UCXzNNA2ngRpRiWvyA7eGd6w): the strongest-evidence channel
- **Denominators:** 363 videos (all long-form), 348 rated, 182 deep-audited. Median duration 21.1 min. Uploads roughly daily (median gap 1.0 day). Median peer ratio 1.01; STRONG 23% / WEAK 16%.
- **Packaging grammar (prevalence):** curiosity wording 39%, money amounts 23%, threat 22%, opportunity 21%, timely 14%, list 12%, explicit audience 10%. Openings: question 28%, number in first 60 words 66%.
- **Top:** `f6HIYQUiMoU` "WTF Just Happened To The Housing Market?!" 33.0×; `tynTfEi4518` "The Car Payment Trap Nobody Talks About" 24.5×; `1mIp0mUyCKU` "Who Can Actually Afford a $500K House in 2026 (The Math Is Brutal)" 23.0×.
- **Bottom:** `Y1OaaClH_eQ` "How Inflation Quietly Stole Your Raise" 0.12×; `zjSiRbmJGwo` "POV: Your Life As Every Level Of Career" 0.12×; `KfTnH7mQG6U` "Your Money Habits Are Making Someone ELSE Rich…" 0.13×.
- **Observation:** top videos tie a concrete purchase or affordability decision (car, house) to current numbers. Several bottom videos are abstract "system" framings. This is an n=6 illustration, not a tested rule. Topic tests did not reach significance.
- **Credibility pattern (deep-audit claim receipts, NICK_169–173):** recurring issues are rounded or irreconcilable arithmetic, survey statistics stretched to the whole population, and unverified personal-narrative outcomes. Example: NICK_173 `UfqNzF7sQzo` — $950/month for 7 years at 10% gives ≈$114.9K, not the $290K implied. **Differentiation opportunity:** the same decision-math topics with fully reconciled, sourced numbers.

### Carl Invests (UCxoC2voi0vPg2hwqgfjdhYw)
- 80 long-form, 76 rated, 80 deep-audited; median 20.7 min; median gap 1.9 days. Median ratio 0.87; STRONG 30% / WEAK 37% — very high variance.
- Prevalence: opportunity 29%, list 26%, curiosity 25%, threat 20%, money 16%, audience 14%, timely 14%.
- **Top:** `7sbA9WZrfHk` "What Happens If You Invest $100 Every Month (Most People Don't Realize This)" 160.6×; `TDEme_uxx4c` "What Actually Happens When You Invest $500 a Month" 55.6×; `rnbgKswe2nA` "The Number Where Compounding Suddenly Catches Fire" 51.4×.
- **Bottom:** `TTilKZZd3Es` "Should You Pay Off Your Mortgage Early or Invest? (The Real Math For 2026)" 0.06×; `w5rktnyQfCI` "Why Net Worth EXPLODES After $100K…" 0.11×; `slIKJx4U0YM` "The One Financial Mistake Every Generation Repeats" 0.12×.
- **Exception to watch:** "The Real Math" comparison framing won on Logical Money and Mark Invests but failed here (`TTilKZZd3Es`, 0.06×). The concept is not self-sufficient.

### Lucas Grant (UCTcOboZIhgrKHMDm-oTlTOg)
- 95 long-form, 75 rated, 85 deep-audited; median 22.6 min; daily cadence. Median ratio 1.04; STRONG 24% / WEAK 19%. Transcripts include placeholders (registry `COMPLETE_WITH_PLACEHOLDERS`).
- Prevalence: curiosity 40%, opportunity 38%, money 22%, threat 20%. Dominant grammar: second-person "POV / Your life…".
- **Top:** `ElGhlrZNb_4` "Living Rich in Secret Changes You More Than You Think." 34.4×; `by_Ah5cDyP8` "POV: What Happens When You Start Paying Cash for Cars" 29.1×; `PLgVQhvtU_A` "Your Life After Winning the $600 Million Lottery And Nobody Knows" 20.0×.
- **Bottom:** `6dw0y-ATdwI` "Your Life If You Start Building Wealth in Your 30s" 0.14×; `YQk4U4II7j4` "POV: You Hit $1 Million Invested — Not What You Expected" 0.19×; `-IpucSOwKgQ` "POV: You Live Off Dividends at 40…" 0.26×.

### Brimm. (UC1GwXFBhh1fiLLuZxs8VRXA): business/place explainers
- 44 long-form, 40 rated, 44 deep-audited; median 8.2 min; median gap 9.1 days. Median ratio 0.81; STRONG 33% / WEAK 35%.
- Low use of money/list/audience wording. Curiosity 25%.
- **Top:** `m5WPi3LX9z0` "Why Airlines Use This Exact Layout" 73.2×; `wlvup8NLKaY` "How This Unassuming Store Is Quietly Changing America" 62.5×; `S81NPqovOT8` "Why Are the Dutch So Good at Ecommerce?" 38.6×.
- **Bottom:** `IOBcBqb6igM` "How Walmart Outsmarted Amazon…" 0.11×; `IW5ARyOjZYU` "The Rise and Fall of Club 18-30" 0.13×; `tRwMoqQtzTY` "What Happens If America Abandons Europe" 0.13×.
- **Observation:** winners explain an everyday object or place that viewers have experienced. Losers cover familiar corporate or geopolitical narratives. n=6, a hypothesis only.

### Bob Invests (UCAKBDBaY1dP7OdZkGPiDnug)
- 57 long-form, 48 rated, **0 deep-audited**; median 18.0 min; gap 2.1 days. Median ratio 1.09; STRONG 19% / WEAK 15%. Curiosity wording 54%.
- **Top:** `pM3t-m0Zryk` "Why Two Incomes Leave You Broker Than One (The Two-Income Trap)" 10.9×; `8PeiQFJA2BU` "The Math of Being Broke: Why You Pay Double for Everything" 8.3×.
- **Bottom:** `a_UD8aeHcoQ` "The 'Free Money' Mistake That Is Costing You Millions" 0.26×; `0IhQ-8pzTS4` "You're Paying More Than You Think" 0.31×.
- Note: threat wording appears on both sides ("Broker", "Mistake"). What separates top from bottom here looks like **mechanism specificity** (two-income trap, poverty premium) versus vague loss. Hypothesis only.

### Sonny Finance (UCFvEZUMNoAVjSoSB8NrV7yw)
- 39 long-form, 34 rated, 0 deep; median 15.2 min. Median ratio 0.99; STRONG 29% / WEAK 26%. Explicit audience wording 26%.
- **Top:** `vb7UojsINvg` "Your Life If You Invested $5 a Day" 35.6×; `uByLqFbCcEA` "Your Life If You Start Building Wealth in Your 30s" 14.8×.
- **Bottom:** `2RAV0z4kDrs` "How Doctors Treat You at Every Level of Wealth" 0.08×; `_R_UJMOGTks` "Your Coworkers Complain About the Owner. It's You." 0.08×.

### Dark Ledger (UCDglfjh__GM2RFM1oAL3a6A), Crayon Capital, Shaami Finance, Money Life POV
- **Dark Ledger** (30 rated): "every level" ladders. Win: `2LXED3ENhck` 159.1×, `iONIlOyeSr4` "Your Life at Every Salary Level — $20K to $1M" 40.8×. Loss within the same grammar: `STe549lyFhs` "How the IRS Treats You at Every Income Level" 0.18×.
- **Crayon Capital** (27 rated, 30 deep): "Explained Like You're 5" series. NVIDIA `1GowFTjbUnk` 9.8× vs PayPal `EedHneVKmpo` 0.14× and Bitcoin `_pUOpoihjA4` 0.16×. Same grammar, opposite outcomes.
- **Shaami Finance** (9 rated): too small. Big wins (`Oj5enLUpPyU` 50.0×) and many near-zero results. Insufficient for DNA.
- **Money Life POV** (13 rated): POV grammar. Both car-cash videos won (`H5r9VQgsQIg` 9.7×, `-uQnQ57J1lU` 4.4×). "Investments start making more money than you" lost (`Z5FKuB7wZJA` 0.05×). Small n.

### Replication channels (metadata only, not deep-audited)
- **Mark Invests** (74 rated): rent-vs-buy `pnJCpIhshX4` 297×, real estate vs stocks `k-ZxdjawYDs` 102×. Psychology-of-money summaries lose (`R2gYICl_VR0` 0.08×).
- **Uncle John Financial** (46 rated): specific rule explainers win (`jABYsMEoW20` "What Changes at Age 59½" 20.7×; `_H2fenN5lSo` "401(k) Balances by Age in 2026: Federal Reserve Survey Data" 18.5×). Other specific rule explainers lose badly (`-oWpfkh0mGY` "$6,000 Senior Deduction" 0.02×). Specificity alone is not sufficient.
- **Uncle Frank Retirement** (23 rated): `OX-fSJzHyPI` compounding number 67.1×; "RMD mistake 84% make" `YL3stNaRSRc` 0.04×.
- **MonkeyExplains** (52 rated, 15 Shorts) and **Primate Economics** (23 rated): banana/monkey animated explainers. National-debt topics lead on Monkey (`Jz7pmE66OqE` 5.8×, `bz0OGtrkjv0` 5.5×). Primate's biggest is a Short, "Inflation" (`ne0MlVZQasE`, 90.4×). Low variance on Monkey (STRONG 17%, WEAK 19%).

### Casually Finance (branch-only data; 206 videos: 173 Shorts, 33 long-form)
- Shorts-heavy, daily. Top Shorts: `Qof71Ef-3EU` "The Cheap Money Era Is Coming to an End" 19.9×, `turJ6VMfUjI` "Why You (Mathematically) Need Inflation" 15.0×. Bottom: Bitcoin Shorts `yDxPLckhxMI` 0.21×, `UAZwkrxS9RA` 0.21×.
- **Visual Forensics (visual-only, accepted 2026-10-24):**
  - `Uumnx2Fo6cE` "The New American Housing Crisis Has Landed": 921 s, 507 visual states (~33 states/min), 194 inferred shots. Grammar: source-first news captures, pointer/highlight, doodle metaphors after evidence, big handwritten red numbers. Branch method rates it BREAKOUT (6.65). Our rule gives no ratio: at 12 days old it had fewer than 5 age peers.
  - `o3FQcd91MIs` "Why The Dumbest Investors Win": 278 s, 76 parent states (~16/min), 47 inferred shots. Peer ratio 1.25 (TYPICAL).
  - **Do not infer** that visual density caused the breakout. n=2, different lengths, topics and dates; narration is ASR-only and unheard.

### xkcd's What If? (CH-000004): visual documentary/explainer (PR #44 package, unmerged)
- 83 registry videos (42 long-form / 39 Shorts with views). Lifetime views/day is similar for Shorts and long-form (median 4,676 vs 4,123).
- The production brain decodes **14 videos**. The 10 that match registry IDs include the channel's largest videos (e.g. `8fADp43wJwU` 9.53M, `UXA-Af-JeCE` 8.52M, `e3uk7jU3RHo` 7.93M views). The decoded set is therefore **hit-heavy**: good for describing house production grammar (7,864 words, 581 states, 438 motions, 200 shots, 1,421 A/V sync rows), but **unusable for success-vs-failure inference**.
- YIOS-created reconstruction experiments (`research/production-experiments/what-if-derived/`, e.g. `chair_test_v2_review/FAILED_VIDEO_VISUAL_AUDIT.md`) are **our own prototypes**, including rejected ones. They are evidence about our production process, never about YouTube's algorithm.

### Not profiled (insufficient evidence)
Matty Invests and Mr. Finance (DS-000001: 159 videos, undated, format null → no peer ratio). Health-niche and story channels in the registry: metadata only, no audits. They are used only in structural statistics (concentration, variance share, age slope).

## What this means for an original channel

- Pick a **channel-level audience promise** first. Channel identity outweighs title wording in our data, and wording effects did not transfer.
- Favour **concrete decision questions with checkable numbers**. That is the recurring cross-channel winner shape, and those numbers are where competitors repeatedly fail our claim audits (credibility gap = differentiation).
- Expect a hit distribution. Plan for many shots on goal, with the same audience and quality bar, and judge the channel on medians and the frequency of STRONG videos, not on single videos.
