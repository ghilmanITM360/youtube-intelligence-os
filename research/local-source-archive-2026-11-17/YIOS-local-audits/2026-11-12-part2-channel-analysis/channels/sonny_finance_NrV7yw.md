# Sonny Finance
Channel id `UCFvEZUMNoAVjSoSB8NrV7yw` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 39 (Shorts 0, Long-form 39)
- Views (all): n=39 | total=962491 | mean=24679.3 | median=7313 | max=254580 | min=813 | p10=1953 | p25=4052 | p75=13007 | p90=81414 | p99=207529 | cv=1.95

## 2. Performance Distribution
- All: p10=1953 p25=4052 median=7313 p75=13007 p90=81414 p99=207529 CV=1.95
- Mean/median ratio: 3.37 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=39 | total=962491 | mean=24679.3 | median=7313 | max=254580 | min=813 | p10=1953 | p25=4052 | p75=13007 | p90=81414 | p99=207529 | cv=1.95

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 23 videos, median views 8065
- Other/Unclassified: 10 videos, median views 4157
- Stocks/Investing: 4 videos, median views 7612
- Business/Companies: 2 videos, median views 3873
- Duration bins: {'15-30m': 21, '8-15m': 18}

## 5. Publishing Pattern
- Date range: 2026-05-06 → 2026-09-11 (129 days); uploads/week ≈ 2.12
- Days between upload dates: median=3.0, mean=3.4, max=7; consistency (CV of gaps)=0.35
- Weekday counts: {'Tue': 7, 'Wed': 6, 'Thu': 5, 'Fri': 5, 'Sat': 6, 'Sun': 6, 'Mon': 4}
- Upload hour (UTC, only where timestamp exists, n=36): {10: 1, 11: 1, 12: 5, 13: 25, 14: 1, 16: 3}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 8, 5094, 0.70
  - 2026-06: 12, 6840, 0.94
  - 2026-07: 7, 9121, 1.25
  - 2026-08: 8, 11388, 1.56
  - 2026-09: 4, 5382, 0.74
- Quarterly:
  - 2026-Q2: 20, 5912, 0.81
  - 2026-Q3: 19, 7561, 1.03

## 6. Performance Classification
- All: {'Average': 19, 'Underperforming': 9, 'Breakout': 6, 'Successful': 5}
- Shorts: {}  Long-form: {'Average': 19, 'Underperforming': 9, 'Breakout': 6, 'Successful': 5}
- Top 5 by age-adjusted ratio:
  - vb7UojsINvg "Your Life If You Invested $5 a Day" views=254580 age=148d ratio=34.81 [LONG]
  - My_1AkxdOjM "POV: You Retired at 35 and Told No One" views=130762 age=87d ratio=17.88 [LONG]
  - uByLqFbCcEA "Your Life If You Start Building Wealth in Your 30s" views=107973 age=164d ratio=14.76 [LONG]
  - 7GWaPTKwP78 "POV: You Quietly Became the Richest Person You Know" views=82699 age=105d ratio=11.31 [LONG]
  - KJY6yUEn4po "POV: You Get Rich Faster Than Everyone You Grew Up With" views=81093 age=151d ratio=11.09 [LONG]

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