# Logical Money
Channel id `UCKhpM-cu2Cod-GyG6KngNYg` · niche FINANCE · subs 28500 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 26 (Shorts 1, Long-form 25)
- Views (all): n=26 | total=2228734 | mean=85720.5 | median=3549.5 | max=1730664 | min=1227 | p10=1770 | p25=2269 | p75=10196 | p90=86431 | p99=1354424 | cv=3.88

## 2. Performance Distribution
- All: p10=1770 p25=2269 median=3549.5 p75=10196 p90=86431 p99=1354424 CV=3.88
- Mean/median ratio: 24.15 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=1 | total=2798 | mean=2798 | median=2798 | max=2798 | min=2798 | p10=2798 | p25=2798 | p75=2798 | p90=2798 | p99=2798 | cv=0.0
- Long-form: n=25 | total=2225936 | mean=89037.4 | median=3716 | max=1730664 | min=1227 | p10=1757 | p25=2234 | p75=10730 | p90=101106 | p99=1369474 | cv=3.81

## 4. Topic Distribution (heuristic)
- Stocks/Investing: 11 videos, median views 2563
- Money/Personal Finance: 7 videos, median views 8596
- Debt/Banking: 3 videos, median views 3716
- Real Estate/Housing: 2 videos, median views 871079
- Inflation/Recession/Macro: 2 videos, median views 4398
- Other/Unclassified: 1 videos, median views 10730
- Duration bins: {'15-30m': 6, '8-15m': 19, '1-3m': 1}

## 5. Publishing Pattern
- Date range: 2026-06-27 → 2026-11-06 (133 days); uploads/week ≈ 1.37
- Days between upload dates: median=5, mean=5.3, max=12; consistency (CV of gaps)=0.44
- Weekday counts: {'Sun': 5, 'Tue': 8, 'Fri': 4, 'Thu': 2, 'Mon': 6, 'Sat': 1}
- Upload hour (UTC, only where timestamp exists, n=26): {8: 1, 10: 1, 11: 6, 12: 8, 13: 3, 14: 3, 15: 3, 16: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 2, 6864, 0.43
  - 2026-07: 6, 3257, 0.65
  - 2026-08: 4, 5718, 0.51
  - 2026-09: 5, 8596, 1.34
  - 2026-10: 7, 2375, 0.76
  - 2026-11: 2, 1608, 0.99
- Quarterly:
  - 2026-Q2: 2, 6864, 0.43
  - 2026-Q3: 15, 6691, 1.00
  - 2026-Q4: 9, 2231, 0.82

## 6. Performance Classification
- All: {'Breakout': 3, 'Average': 12, 'Underperforming': 8, 'Successful': 3}
- Shorts: {'Average': 1}  Long-form: {'Breakout': 3, 'Average': 11, 'Underperforming': 8, 'Successful': 3}
- Top 5 by age-adjusted ratio:
  - nkT_K8l1rEw "Renting Vs Buying a Home - The Real Math" views=1730664 age=108d ratio=135.94 [LONG]
  - MpRWRSHlXd8 "8 Minimalist Money Habits to Stay Financially Stable" views=159806 age=78d ratio=16.84 [LONG]
  - bbP8Mr_MThk "Real Estate vs Stocks - Which Makes More Money? (The Real Math)" views=225706 age=131d ratio=14.85 [LONG]
  - w-_hUZn5aoE "If YOU Are Saving Money, You NEED To Stop!" views=13056 age=38d ratio=2.55 [LONG]
  - aADicDzTcuM "America's $40 Trillion Debt Explained in Simple English" views=4557 age=12d ratio=2.06 [LONG]

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