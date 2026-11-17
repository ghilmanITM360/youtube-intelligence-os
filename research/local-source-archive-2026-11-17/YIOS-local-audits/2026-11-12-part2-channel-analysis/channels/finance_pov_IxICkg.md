# Finance POV
Channel id `UC4zls8vK8iiTSQpnaIxICkg` · niche FINANCE · subs 18400 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 77 (Shorts 0, Long-form 77)
- Views (all): n=77 | total=2034405 | mean=26420.8 | median=4295 | max=340689 | min=121 | p10=971 | p25=1991 | p75=11248 | p90=66836 | p99=267544 | cv=2.35

## 2. Performance Distribution
- All: p10=971 p25=1991 median=4295 p75=11248 p90=66836 p99=267544 CV=2.35
- Mean/median ratio: 6.15 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=77 | total=2034405 | mean=26420.8 | median=4295 | max=340689 | min=121 | p10=971 | p25=1991 | p75=11248 | p90=66836 | p99=267544 | cv=2.35

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 30 videos, median views 4756
- Other/Unclassified: 17 videos, median views 3396
- Business/Companies: 13 videos, median views 11082
- Stocks/Investing: 7 videos, median views 2144
- Real Estate/Housing: 3 videos, median views 4208
- Debt/Banking: 3 videos, median views 3155
- History/Explainers: 2 videos, median views 4356
- Geopolitics/Trade: 1 videos, median views 3681
- Inflation/Recession/Macro: 1 videos, median views 420
- Duration bins: {'15-30m': 66, '8-15m': 11}

## 5. Publishing Pattern
- Date range: 2026-05-10 → 2026-11-09 (184 days); uploads/week ≈ 2.93
- Days between upload dates: median=2.0, mean=2.4, max=7; consistency (CV of gaps)=0.57
- Weekday counts: {'Fri': 14, 'Sun': 12, 'Tue': 10, 'Mon': 10, 'Wed': 11, 'Sat': 9, 'Thu': 11}
- Upload hour (UTC, only where timestamp exists, n=77): {13: 1, 14: 2, 15: 10, 16: 5, 17: 22, 18: 12, 19: 9, 20: 3, 21: 5, 22: 5, 23: 3}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 10, 1397, 0.33
  - 2026-06: 10, 2664, 0.62
  - 2026-07: 13, 3784, 0.88
  - 2026-08: 8, 8157, 1.90
  - 2026-09: 17, 5901, 1.37
  - 2026-10: 14, 10562, 2.46
  - 2026-11: 5, 1208, 0.28
- Quarterly:
  - 2026-Q2: 20, 1810, 0.42
  - 2026-Q3: 38, 5558, 1.29
  - 2026-Q4: 19, 8817, 2.05

## 6. Performance Classification
- All: {'Average': 30, 'Underperforming': 17, 'Successful': 19, 'Breakout': 11}
- Shorts: {}  Long-form: {'Average': 30, 'Underperforming': 17, 'Successful': 19, 'Breakout': 11}
- Top 5 by age-adjusted ratio:
  - ZrXnvw9MqAE "POV: You Won the Lottery and Told No One—10 Years Later" views=340689 age=26d ratio=79.30 [LONG]
  - 3sLl-DmC_zE "Building a $600 Million Holding Company as a Silent Businessman" views=244445 age=53d ratio=56.90 [LONG]
  - 86LiyytGuA4 "POV: You're a Silent Businessman Building a $600M Empire" views=220425 age=40d ratio=51.31 [LONG]
  - l0svo03j00M "POV: You Building a Holding Company — $0 to $500M, Step by Step" views=207202 age=128d ratio=48.23 [LONG]
  - BEvQcR323uI "Life As Silent Millionaire | You Have $650 Million Nobody Knows" views=190706 age=176d ratio=44.39 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification