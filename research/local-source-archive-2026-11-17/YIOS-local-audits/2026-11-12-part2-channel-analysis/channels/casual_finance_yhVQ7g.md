# Casual Finance
Channel id `UCrNfRFWnLC3tCy1TnyhVQ7g` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 206 (Shorts 173, Long-form 33)
- Views (all): n=206 | total=28278526 | mean=137274.4 | median=24779.5 | max=2352982 | min=2930 | p10=9799 | p25=15618 | p75=48196 | p90=374266 | p99=1784725 | cv=2.53

## 2. Performance Distribution
- All: p10=9799 p25=15618 median=24779.5 p75=48196 p90=374266 p99=1784725 CV=2.53
- Mean/median ratio: 5.54 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=173 | total=5869988 | mean=33930.6 | median=21787 | max=389111 | min=2930 | p10=9102 | p25=14341 | p75=33730 | p90=49578 | p99=303510 | cv=1.5
- Long-form: n=33 | total=22408538 | mean=679046.6 | median=484561 | max=2352982 | min=48404 | p10=98713 | p25=191741 | p75=774085 | p90=1666396 | p99=2252443 | cv=0.92

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 40 videos, median views 23220
- Other/Unclassified: 34 videos, median views 22976
- Stocks/Investing: 28 videos, median views 21632
- Debt/Banking: 22 videos, median views 24550
- Geopolitics/Trade: 19 videos, median views 25273
- Business/Companies: 19 videos, median views 33730
- Money/Personal Finance: 18 videos, median views 25653
- History/Explainers: 13 videos, median views 29722
- Crypto/Bitcoin: 13 videos, median views 21787
- Duration bins: {'<=60s': 105, '1-3m': 68, '8-15m': 21, '15-30m': 9, '3-8m': 3}

## 5. Publishing Pattern
- Date range: 2025-07-28 → 2026-10-10 (440 days); uploads/week ≈ 3.28
- Days between upload dates: median=1, mean=2.3, max=28; consistency (CV of gaps)=1.88
- Weekday counts: {'Wed': 30, 'Thu': 30, 'Fri': 27, 'Sat': 26, 'Tue': 34, 'Mon': 33, 'Sun': 26}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
  - 2025-07: 1, 236601, 0.49
  - 2025-08: 1, 50259, 0.10
  - 2025-09: 1, 191741, 0.40
  - 2025-10: 2, 664844, 1.37
  - 2025-11: 2, 353442, 0.73
  - 2025-12: 2, 242272, 0.50
  - 2026-01: 1, 568510, 1.17
  - 2026-02: 3, 116235, 0.24
  - 2026-03: 33, 12662, 0.54
  - 2026-04: 8, 19324, 0.60
  - 2026-05: 30, 22911, 1.05
  - 2026-06: 32, 34047, 1.49
  - 2026-07: 32, 24404, 1.05
  - 2026-08: 31, 23953, 1.09
  - 2026-09: 21, 24203, 1.11
  - 2026-10: 6, 40872, 1.88
- Quarterly:
  - 2025-Q3: 3, 191741, 0.40
  - 2025-Q4: 6, 257877, 0.53
  - 2026-Q1: 37, 15871, 0.50
  - 2026-Q2: 70, 26162, 1.15
  - 2026-Q3: 84, 24078, 1.09
  - 2026-Q4: 6, 40872, 1.88

## 6. Performance Classification
- All: {'Successful': 53, 'Average': 119, 'Underperforming': 28, 'Breakout': 6}
- Shorts: {'Successful': 42, 'Average': 107, 'Underperforming': 18, 'Breakout': 6}  Long-form: {'Successful': 11, 'Underperforming': 10, 'Average': 12}
- Top 5 by age-adjusted ratio:
  - turJ6VMfUjI "Why You (Mathematically) Need Inflation" views=389111 age=101d ratio=17.86 [SHORT]
  - Qof71Ef-3EU "The Cheap Money Era Is Coming to an End" views=366349 age=64d ratio=16.81 [SHORT]
  - rSa2aziEsAI "Why Japan's Economy Is Awful" views=279072 age=77d ratio=12.81 [SHORT]
  - JsK53moCyZA "The SpaceX IPO Nobody Can (Actually) Explain..." views=212576 age=163d ratio=9.76 [SHORT]
  - SYSUh-oow6M "Why Being a Millionaire Doesn't Impress Anyone..." views=206481 age=157d ratio=9.48 [SHORT]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification