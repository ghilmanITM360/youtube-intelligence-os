# Business Decoded
Channel id `UCr1NnI7dwgIqeGJymhKL37A` · niche ECONOMICS · subs 5810 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 43 (Shorts 0, Long-form 43)
- Views (all): n=43 | total=2100130 | mean=48840.2 | median=2559 | max=1463404 | min=161 | p10=303 | p25=666 | p75=9695 | p90=54756 | p99=923987 | cv=4.53

## 2. Performance Distribution
- All: p10=303 p25=666 median=2559 p75=9695 p90=54756 p99=923987 CV=4.53
- Mean/median ratio: 19.09 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=43 | total=2100130 | mean=48840.2 | median=2559 | max=1463404 | min=161 | p10=303 | p25=666 | p75=9695 | p90=54756 | p99=923987 | cv=4.53

## 4. Topic Distribution (heuristic)
- History/Explainers: 15 videos, median views 5005
- Business/Companies: 9 videos, median views 932
- Money/Personal Finance: 8 videos, median views 11068
- Inflation/Recession/Macro: 6 videos, median views 430
- Other/Unclassified: 3 videos, median views 1282
- Stocks/Investing: 1 videos, median views 639
- Debt/Banking: 1 videos, median views 256
- Duration bins: {'15-30m': 23, '8-15m': 19, '<=60s': 1}

## 5. Publishing Pattern
- Date range: 2026-07-22 → 2026-11-10 (112 days); uploads/week ≈ 2.69
- Days between upload dates: median=2, mean=2.7, max=44; consistency (CV of gaps)=2.43
- Weekday counts: {'Sat': 7, 'Thu': 4, 'Wed': 5, 'Mon': 8, 'Sun': 6, 'Fri': 7, 'Tue': 6}
- Upload hour (UTC, only where timestamp exists, n=43): {7: 2, 16: 1, 17: 1, 19: 33, 20: 3, 21: 1, 22: 1, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-07: 2, 711, 0.28
  - 2026-09: 16, 605, 0.24
  - 2026-10: 20, 5682, 2.22
  - 2026-11: 5, 2563, 1.00
- Quarterly:
  - 2026-Q3: 18, 613, 0.24
  - 2026-Q4: 25, 5005, 1.96

## 6. Performance Classification
- All: {'Successful': 14, 'Average': 8, 'Underperforming': 16, 'Breakout': 5}
- Shorts: {}  Long-form: {'Successful': 14, 'Average': 8, 'Underperforming': 16, 'Breakout': 5}
- Top 5 by age-adjusted ratio:
  - 2T8JrUE_bz4 "Why Buffets Don’t Care How Much You Eat" views=1463404 age=29d ratio=571.64 [LONG]
  - nt2Zn2GftOQ "Why Restaurants Give You Free Bread — And Still Make More Money" views=179079 age=35d ratio=69.95 [LONG]
  - YDTDdDZVtfk "Why Outlet Stores Sell “Designer” Clothes So Cheap" views=137971 age=39d ratio=53.90 [LONG]
  - LMGT7NErBL8 "How Empty Mattress Stores Make So Much Money" views=100594 age=45d ratio=39.29 [LONG]
  - RKWqzLwpj6M "Why Little Caesars Can Sell Pizza So Cheap" views=63995 age=14d ratio=25.00 [LONG]

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