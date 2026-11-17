# Mark Calloway
Channel id `UCAOeipQ5KGzZ2McMF1RNsrQ` · niche FINANCE · subs 22600 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 86 (Shorts 0, Long-form 86)
- Views (all): n=86 | total=2844948 | mean=33080.8 | median=2140.5 | max=723626 | min=220 | p10=349 | p25=842 | p75=5800 | p90=56272 | p99=447822 | cv=3.22

## 2. Performance Distribution
- All: p10=349 p25=842 median=2140.5 p75=5800 p90=56272 p99=447822 CV=3.22
- Mean/median ratio: 15.45 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=86 | total=2844948 | mean=33080.8 | median=2140.5 | max=723626 | min=220 | p10=349 | p25=842 | p75=5800 | p90=56272 | p99=447822 | cv=3.22

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 45 videos, median views 2555
- Money/Personal Finance: 18 videos, median views 2140
- Real Estate/Housing: 8 videos, median views 1387
- Debt/Banking: 7 videos, median views 4422
- History/Explainers: 4 videos, median views 286
- Geopolitics/Trade: 3 videos, median views 1509
- Inflation/Recession/Macro: 1 videos, median views 596
- Duration bins: {'15-30m': 73, '8-15m': 13}

## 5. Publishing Pattern
- Date range: 2026-03-27 → 2026-10-19 (207 days); uploads/week ≈ 2.91
- Days between upload dates: median=1, mean=2.9, max=40; consistency (CV of gaps)=2.09
- Weekday counts: {'Sat': 13, 'Wed': 13, 'Thu': 9, 'Tue': 18, 'Sun': 9, 'Fri': 14, 'Mon': 10}
- Upload hour (UTC, only where timestamp exists, n=86): {0: 10, 1: 10, 2: 4, 3: 7, 4: 2, 13: 4, 14: 1, 15: 4, 16: 1, 17: 4, 18: 3, 19: 3, 21: 15, 22: 10, 23: 8}
- Monthly (n, median views, age-adj median ratio):
  - 2026-03: 2, 2248, 0.78
  - 2026-04: 23, 3841, 1.33
  - 2026-06: 21, 888, 0.31
  - 2026-07: 2, 479, 0.17
  - 2026-08: 2, 572, 0.20
  - 2026-09: 19, 1509, 0.52
  - 2026-10: 17, 3156, 1.09
- Quarterly:
  - 2026-Q1: 2, 2248, 0.78
  - 2026-Q2: 44, 2150, 0.74
  - 2026-Q3: 23, 955, 0.33
  - 2026-Q4: 17, 3156, 1.09

## 6. Performance Classification
- All: {'Successful': 12, 'Underperforming': 35, 'Average': 25, 'Breakout': 14}
- Shorts: {}  Long-form: {'Successful': 12, 'Underperforming': 35, 'Average': 25, 'Breakout': 14}
- Top 5 by age-adjusted ratio:
  - wafLcwHvn5U "7 Things They Can't Take From You After 65 — Not Even the IRS" views=723626 age=54d ratio=250.27 [LONG]
  - UMoXeJWRRpE "6 Forms Seniors Forget That Cost Their Children The House" views=399151 age=215d ratio=137.97 [LONG]
  - AsOi1tX9R-o "The Government’s 5-Year Rule Takes Your Home and Most Seniors Never Kn" views=395099 age=216d ratio=136.57 [LONG]
  - OhxzTQyOFIQ "7 Types of Income the IRS Can't Touch After 65 (Most Seniors Only Know" views=321030 age=58d ratio=111.03 [LONG]
  - Pfm1t6xd88A "Seniors: 7 Pieces of Good News for Your Money in January (Most Don't K" views=294591 age=25d ratio=101.92 [LONG]

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