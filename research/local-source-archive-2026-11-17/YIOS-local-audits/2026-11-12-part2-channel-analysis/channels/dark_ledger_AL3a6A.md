# Dark Ledger
Channel id `UCDglfjh__GM2RFM1oAL3a6A` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 38 (Shorts 0, Long-form 38)
- Views (all): n=38 | total=2740763 | mean=72125.3 | median=12383.5 | max=1112119 | min=1371 | p10=3965 | p25=5776 | p75=47744 | p90=179990 | p99=808494 | cv=2.56

## 2. Performance Distribution
- All: p10=3965 p25=5776 median=12383.5 p75=47744 p90=179990 p99=808494 CV=2.56
- Mean/median ratio: 5.82 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=38 | total=2740763 | mean=72125.3 | median=12383.5 | max=1112119 | min=1371 | p10=3965 | p25=5776 | p75=47744 | p90=179990 | p99=808494 | cv=2.56

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 15 videos, median views 15055
- Other/Unclassified: 5 videos, median views 12340
- Real Estate/Housing: 4 videos, median views 9139
- History/Explainers: 4 videos, median views 8724
- Stocks/Investing: 4 videos, median views 39194
- Debt/Banking: 3 videos, median views 48593
- Geopolitics/Trade: 2 videos, median views 4066
- Business/Companies: 1 videos, median views 4425
- Duration bins: {'15-30m': 15, '8-15m': 23}

## 5. Publishing Pattern
- Date range: 2026-03-21 → 2026-09-11 (175 days); uploads/week ≈ 1.52
- Days between upload dates: median=4, mean=4.7, max=13; consistency (CV of gaps)=0.62
- Weekday counts: {'Sun': 11, 'Mon': 6, 'Sat': 4, 'Wed': 3, 'Thu': 4, 'Fri': 6, 'Tue': 4}
- Upload hour (UTC, only where timestamp exists, n=38): {8: 3, 10: 1, 11: 6, 13: 3, 14: 3, 15: 3, 16: 2, 17: 4, 18: 5, 19: 4, 20: 1, 21: 1, 23: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-03: 4, 3658, 0.30
  - 2026-04: 6, 5532, 0.45
  - 2026-05: 8, 57522, 4.64
  - 2026-06: 5, 22690, 1.83
  - 2026-07: 4, 12714, 1.03
  - 2026-08: 6, 12314, 0.99
  - 2026-09: 5, 11789, 0.95
- Quarterly:
  - 2026-Q1: 4, 3658, 0.30
  - 2026-Q2: 19, 22690, 1.83
  - 2026-Q3: 15, 12340, 1.00

## 6. Performance Classification
- All: {'Breakout': 7, 'Underperforming': 8, 'Average': 16, 'Successful': 7}
- Shorts: {}  Long-form: {'Breakout': 7, 'Underperforming': 8, 'Average': 16, 'Successful': 7}
- Top 5 by age-adjusted ratio:
  - 2LXED3ENhck "How Banks Treat You at Every Level of Wealth — $0 to $25M" views=1112119 age=192d ratio=89.80 [LONG]
  - iONIlOyeSr4 "Your Life at Every Salary Level — $20K to $1M" views=291512 age=195d ratio=23.54 [LONG]
  - Jn3N9OzSY1c "How Much You Need Invested to Live Off Dividends" views=235502 age=164d ratio=19.02 [LONG]
  - KT0fxCW56UU "You Escaped the Rat Race. Nobody Noticed." views=193076 age=159d ratio=15.59 [LONG]
  - 2_TcC2ohCFs "Your Life Driving the Same Car for 10 Years" views=174381 age=167d ratio=14.08 [LONG]

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