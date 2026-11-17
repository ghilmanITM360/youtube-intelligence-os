# Mark Invests
Channel id `UCcj_KU4ZN6bx6Ki68hNJWqw` · niche FINANCE · subs 19800 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 98 (Shorts 0, Long-form 98)
- Views (all): n=98 | total=1787323 | mean=18238.0 | median=1429.5 | max=495096 | min=307 | p10=496 | p25=838 | p75=4012 | p90=14541 | p99=378565 | cv=3.98

## 2. Performance Distribution
- All: p10=496 p25=838 median=1429.5 p75=4012 p90=14541 p99=378565 CV=3.98
- Mean/median ratio: 12.76 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=98 | total=1787323 | mean=18238.0 | median=1429.5 | max=495096 | min=307 | p10=496 | p25=838 | p75=4012 | p90=14541 | p99=378565 | cv=3.98

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 36 videos, median views 1465
- Other/Unclassified: 21 videos, median views 1948
- Stocks/Investing: 12 videos, median views 1504
- History/Explainers: 9 videos, median views 1193
- Debt/Banking: 8 videos, median views 598
- Real Estate/Housing: 7 videos, median views 1378
- Geopolitics/Trade: 5 videos, median views 3346
- Duration bins: {'15-30m': 75, '8-15m': 23}

## 5. Publishing Pattern
- Date range: 2026-04-07 → 2026-11-09 (217 days); uploads/week ≈ 3.16
- Days between upload dates: median=2, mean=2.2, max=22; consistency (CV of gaps)=1.19
- Weekday counts: {'Sat': 16, 'Thu': 19, 'Fri': 11, 'Tue': 17, 'Wed': 10, 'Sun': 11, 'Mon': 14}
- Upload hour (UTC, only where timestamp exists, n=98): {0: 2, 11: 57, 12: 2, 21: 19, 22: 12, 23: 6}
- Monthly (n, median views, age-adj median ratio):
  - 2026-04: 16, 3902, 1.19
  - 2026-05: 14, 4618, 1.48
  - 2026-06: 10, 1190, 0.41
  - 2026-07: 11, 650, 0.24
  - 2026-08: 7, 917, 0.37
  - 2026-09: 11, 1532, 0.82
  - 2026-10: 23, 1937, 1.24
  - 2026-11: 6, 848, 0.73
- Quarterly:
  - 2026-Q2: 40, 3060, 1.01
  - 2026-Q3: 29, 936, 0.38
  - 2026-Q4: 29, 1162, 0.95

## 6. Performance Classification
- All: {'Underperforming': 36, 'Successful': 20, 'Average': 33, 'Breakout': 9}
- Shorts: {}  Long-form: {'Underperforming': 36, 'Successful': 20, 'Average': 33, 'Breakout': 9}
- Top 5 by age-adjusted ratio:
  - sj7tGa1-WWM "Why Everything Changes After Paying Off Your House" views=372131 age=27d ratio=227.08 [LONG]
  - pnJCpIhshX4 "Renting Vs Buying a Home — The Real Math" views=495096 age=164d ratio=165.23 [LONG]
  - k-ZxdjawYDs "Real Estate Vs Stocks — The Real Math (Which One Will Make You More Mo" views=374961 age=214d ratio=113.70 [LONG]
  - Gm28pBqyFT4 "401k VS Roth IRA — The Real Math" views=124121 age=209d ratio=37.96 [LONG]
  - bYV6AwPv_NU "5 Wealth Levels Where Money Starts Snowballing FAST" views=60276 age=59d ratio=28.71 [LONG]

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