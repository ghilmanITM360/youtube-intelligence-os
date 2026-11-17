# POV Wealth
Channel id `UCryM-LAkg31P_B0GeshJQjg` · niche FINANCE · subs 5810 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 60 (Shorts 0, Long-form 60)
- Views (all): n=60 | total=2204404 | mean=36740.1 | median=11833.5 | max=681604 | min=659 | p10=1839 | p25=3942 | p75=23509 | p90=45280 | p99=518970 | cv=2.77

## 2. Performance Distribution
- All: p10=1839 p25=3942 median=11833.5 p75=23509 p90=45280 p99=518970 CV=2.77
- Mean/median ratio: 3.1 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=60 | total=2204404 | mean=36740.1 | median=11833.5 | max=681604 | min=659 | p10=1839 | p25=3942 | p75=23509 | p90=45280 | p99=518970 | cv=2.77

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 30 videos, median views 11264
- Money/Personal Finance: 11 videos, median views 7082
- Real Estate/Housing: 11 videos, median views 13555
- Debt/Banking: 3 videos, median views 23569
- History/Explainers: 2 videos, median views 352536
- Business/Companies: 2 videos, median views 7430
- Stocks/Investing: 1 videos, median views 2039
- Duration bins: {'15-30m': 59, '8-15m': 1}

## 5. Publishing Pattern
- Date range: 2026-09-07 → 2026-11-09 (64 days); uploads/week ≈ 6.56
- Days between upload dates: median=1.0, mean=1.1, max=2; consistency (CV of gaps)=0.29
- Weekday counts: {'Wed': 10, 'Tue': 8, 'Sat': 9, 'Thu': 8, 'Mon': 12, 'Sun': 7, 'Fri': 6}
- Upload hour (UTC, only where timestamp exists, n=60): {1: 1, 8: 1, 9: 1, 10: 2, 13: 1, 14: 10, 15: 1, 17: 1, 19: 4, 20: 4, 21: 26, 22: 4, 23: 4}
- Monthly (n, median views, age-adj median ratio):
  - 2026-09: 22, 3774, 0.32
  - 2026-10: 29, 16789, 1.42
  - 2026-11: 9, 12539, 1.06
- Quarterly:
  - 2026-Q3: 22, 3774, 0.32
  - 2026-Q4: 38, 15376, 1.30

## 6. Performance Classification
- All: {'Average': 21, 'Successful': 16, 'Underperforming': 19, 'Breakout': 4}
- Shorts: {}  Long-form: {'Average': 21, 'Successful': 16, 'Underperforming': 19, 'Breakout': 4}
- Top 5 by age-adjusted ratio:
  - evtp6soM62Y "POV: You Won the Lottery — And Showed Up to Work the Next Day" views=681604 age=35d ratio=57.59 [LONG]
  - JsvUL561rak "POV: You Won the Lottery — And Kept Living in Your Tiny Apartment" views=405954 age=34d ratio=34.30 [LONG]
  - RSqrEsqItSw "POV: Your Boss Banned Side Hustles to "Keep You Focused" — He Didn't K" views=171123 age=7d ratio=14.46 [LONG]
  - 0VqARlMwRiw "POV: Your Neighbors Think You're Struggling — Yours Is the Only House " views=157129 age=61d ratio=13.28 [LONG]
  - HtXJ6425y_Y "Your Neighbors Pitied You for Buying the Worst House on the Street — 1" views=51830 age=16d ratio=4.38 [LONG]

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