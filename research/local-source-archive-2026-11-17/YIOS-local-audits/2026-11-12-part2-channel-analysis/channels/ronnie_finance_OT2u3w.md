# Ronnie Finance
Channel id `UCA-ucSJ_2mY4EqjenOT2u3w` · niche FINANCE · subs 1670 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 61 (Shorts 0, Long-form 61)
- Views (all): n=61 | total=508955 | mean=8343.5 | median=405 | max=281847 | min=28 | p10=57 | p25=105 | p75=2458 | p90=15860 | p99=144983 | cv=4.36

## 2. Performance Distribution
- All: p10=57 p25=105 median=405 p75=2458 p90=15860 p99=144983 CV=4.36
- Mean/median ratio: 20.6 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=61 | total=508955 | mean=8343.5 | median=405 | max=281847 | min=28 | p10=57 | p25=105 | p75=2458 | p90=15860 | p99=144983 | cv=4.36

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 24 videos, median views 161
- Other/Unclassified: 16 videos, median views 709
- Business/Companies: 7 videos, median views 2458
- Real Estate/Housing: 4 videos, median views 4298
- Debt/Banking: 3 videos, median views 4977
- History/Explainers: 2 videos, median views 390
- Stocks/Investing: 2 videos, median views 218
- Geopolitics/Trade: 2 videos, median views 11562
- Inflation/Recession/Macro: 1 videos, median views 193
- Duration bins: {'15-30m': 21, '8-15m': 39, '3-8m': 1}

## 5. Publishing Pattern
- Date range: 2026-05-01 → 2026-11-09 (193 days); uploads/week ≈ 2.21
- Days between upload dates: median=2.0, mean=3.2, max=25; consistency (CV of gaps)=1.25
- Weekday counts: {'Sun': 14, 'Tue': 9, 'Mon': 7, 'Sat': 6, 'Thu': 9, 'Wed': 7, 'Fri': 9}
- Upload hour (UTC, only where timestamp exists, n=61): {14: 1, 15: 1, 16: 2, 17: 3, 18: 7, 19: 30, 20: 11, 21: 5, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 10, 194, 0.48
  - 2026-06: 4, 112, 0.28
  - 2026-07: 3, 51, 0.13
  - 2026-08: 7, 111, 0.28
  - 2026-09: 12, 176, 0.44
  - 2026-10: 19, 4977, 12.26
  - 2026-11: 6, 1137, 2.80
- Quarterly:
  - 2026-Q2: 14, 170, 0.42
  - 2026-Q3: 22, 112, 0.28
  - 2026-Q4: 25, 3497, 8.62

## 6. Performance Classification
- All: {'Underperforming': 23, 'Successful': 12, 'Average': 11, 'Breakout': 15}
- Shorts: {}  Long-form: {'Underperforming': 23, 'Successful': 12, 'Average': 11, 'Breakout': 15}
- Top 5 by age-adjusted ratio:
  - piJ-diS4zng "POV: Your Stepdad Kicked You Out at 15. Then Learned You Were Worth $6" views=281847 age=33d ratio=694.21 [LONG]
  - xFmGTIJu6hA "POV: Dad Left You $1 and His Stepchildren $4 Million— They Didn't Know" views=53740 age=30d ratio=132.37 [LONG]
  - O9YfXilMgC8 "You Grew Up Broke But Think Like Old Money" views=27948 age=178d ratio=68.84 [LONG]
  - YtfT_whXNcI "POV: You Quit College to Raise Your Siblings — They Mock Your Job, Una" views=20965 age=25d ratio=51.64 [LONG]
  - 59H7ieUTxlQ "POV: Stepdad Said You'd Amount to Nothing. You Bought His Company for " views=16971 age=36d ratio=41.80 [LONG]

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