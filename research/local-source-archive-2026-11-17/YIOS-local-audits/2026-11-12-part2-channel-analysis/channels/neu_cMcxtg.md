# Neu
Channel id `UChS4VG1jXDcxDnUvwcMcxtg` · niche ECONOMICS · subs 40000 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 56 (Shorts 0, Long-form 56)
- Views (all): n=56 | total=6115222 | mean=109200.4 | median=45626.5 | max=1120820 | min=626 | p10=10248 | p25=17424 | p75=102637 | p90=242348 | p99=861853 | cv=1.7

## 2. Performance Distribution
- All: p10=10248 p25=17424 median=45626.5 p75=102637 p90=242348 p99=861853 CV=1.7
- Mean/median ratio: 2.39 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=56 | total=6115222 | mean=109200.4 | median=45626.5 | max=1120820 | min=626 | p10=10248 | p25=17424 | p75=102637 | p90=242348 | p99=861853 | cv=1.7

## 4. Topic Distribution (heuristic)
- History/Explainers: 22 videos, median views 58528
- Geopolitics/Trade: 10 videos, median views 38418
- Business/Companies: 6 videos, median views 45490
- Other/Unclassified: 6 videos, median views 50007
- Inflation/Recession/Macro: 6 videos, median views 76291
- Real Estate/Housing: 2 videos, median views 176120
- Money/Personal Finance: 2 videos, median views 48208
- Stocks/Investing: 1 videos, median views 8592
- Debt/Banking: 1 videos, median views 626
- Duration bins: {'8-15m': 55, '15-30m': 1}

## 5. Publishing Pattern
- Date range: 2025-09-24 → 2026-11-11 (414 days); uploads/week ≈ 0.95
- Days between upload dates: median=5, mean=7.5, max=63; consistency (CV of gaps)=1.14
- Weekday counts: {'Wed': 9, 'Fri': 10, 'Thu': 7, 'Sat': 8, 'Sun': 7, 'Mon': 8, 'Tue': 7}
- Upload hour (UTC, only where timestamp exists, n=56): {0: 5, 1: 1, 2: 3, 3: 2, 4: 2, 5: 10, 6: 5, 7: 1, 8: 2, 10: 1, 11: 2, 12: 1, 13: 2, 15: 1, 16: 4, 18: 2, 19: 3, 20: 5, 21: 2, 22: 1, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2025-09: 1, 7603, 0.12
  - 2025-10: 1, 15259, 0.25
  - 2025-12: 2, 265798, 4.51
  - 2026-01: 4, 69158, 1.21
  - 2026-02: 8, 45490, 0.81
  - 2026-03: 6, 32710, 0.60
  - 2026-04: 2, 371835, 6.95
  - 2026-05: 3, 58882, 1.14
  - 2026-06: 3, 20614, 0.43
  - 2026-07: 4, 90600, 1.92
  - 2026-08: 6, 62218, 1.49
  - 2026-09: 5, 45305, 1.18
  - 2026-10: 6, 38404, 1.20
  - 2026-11: 5, 32971, 1.15
- Quarterly:
  - 2025-Q3: 1, 7603, 0.12
  - 2025-Q4: 3, 26690, 0.46
  - 2026-Q1: 18, 45490, 0.81
  - 2026-Q2: 8, 76291, 1.46
  - 2026-Q3: 15, 51601, 1.28
  - 2026-Q4: 11, 36302, 1.15

## 6. Performance Classification
- All: {'Underperforming': 14, 'Average': 19, 'Successful': 17, 'Breakout': 6}
- Shorts: {}  Long-form: {'Underperforming': 14, 'Average': 19, 'Successful': 17, 'Breakout': 6}
- Top 5 by age-adjusted ratio:
  - HyUjsfhX4-Y "The World's Largest Ship Graveyard" views=1120820 age=263d ratio=20.12 [LONG]
  - cQ4f-24Lp0U "The Economics of Owning A Ship" views=649970 age=223d ratio=12.13 [LONG]
  - nWUcDEfUiBU "Why BYD is Buying Ships" views=240462 age=7d ratio=8.80 [LONG]
  - eh4-CioOx6s "Why It’s Cheaper to Abandon This Container" views=504906 age=335d ratio=8.56 [LONG]
  - rqTJoriWdFk "How This Port Dominates Global Shipping" views=337144 age=101d ratio=7.55 [LONG]

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