# Rick Finance
Channel id `UCDLINT0o_8a0kObYN5bBqUw` · niche FINANCE · subs 6490 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=1818265 | mean=18182.7 | median=8151.5 | max=247371 | min=19 | p10=371 | p25=765 | p75=13904 | p90=48853 | p99=205247 | cv=1.92

## 2. Performance Distribution
- All: p10=371 p25=765 median=8151.5 p75=13904 p90=48853 p99=205247 CV=1.92
- Mean/median ratio: 2.23 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=1818265 | mean=18182.7 | median=8151.5 | max=247371 | min=19 | p10=371 | p25=765 | p75=13904 | p90=48853 | p99=205247 | cv=1.92

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 51 videos, median views 9861
- Stocks/Investing: 23 videos, median views 8946
- Other/Unclassified: 14 videos, median views 5715
- History/Explainers: 9 videos, median views 4804
- Geopolitics/Trade: 1 videos, median views 3114
- Real Estate/Housing: 1 videos, median views 6250
- Inflation/Recession/Macro: 1 videos, median views 703
- Duration bins: {'15-30m': 95, '8-15m': 5}

## 5. Publishing Pattern
- Date range: 2026-05-26 → 2026-11-11 (170 days); uploads/week ≈ 4.12
- Days between upload dates: median=1, mean=1.7, max=9; consistency (CV of gaps)=0.85
- Weekday counts: {'Fri': 13, 'Sun': 10, 'Sat': 15, 'Thu': 17, 'Wed': 16, 'Mon': 14, 'Tue': 15}
- Upload hour (UTC, only where timestamp exists, n=100): {12: 5, 13: 41, 14: 23, 15: 16, 16: 8, 17: 4, 18: 2, 19: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 4, 19165, 3.26
  - 2026-06: 11, 10156, 1.76
  - 2026-07: 9, 488, 0.09
  - 2026-08: 12, 9935, 1.87
  - 2026-09: 23, 14162, 2.79
  - 2026-10: 30, 7228, 1.55
  - 2026-11: 11, 2103, 0.51
- Quarterly:
  - 2026-Q2: 15, 10156, 1.76
  - 2026-Q3: 44, 10516, 2.08
  - 2026-Q4: 41, 6188, 1.38

## 6. Performance Classification
- All: {'Average': 13, 'Underperforming': 32, 'Successful': 40, 'Breakout': 15}
- Shorts: {}  Long-form: {'Average': 13, 'Underperforming': 32, 'Successful': 40, 'Breakout': 15}
- Top 5 by age-adjusted ratio:
  - lrEZToFhBv0 "The 6 Wealth Levels Where Compounding Gets Insane" views=247371 age=70d ratio=47.56 [LONG]
  - 5qPNPf_8_LY "The Exact Moment Compounding Becomes a Wealth Machine" views=204822 age=161d ratio=35.00 [LONG]
  - ld-QmmPgh8s "5 Wealth Levels Where Money Starts Snowballing FAST" views=73890 age=60d ratio=14.51 [LONG]
  - FSBIFyYX4qo "What Really Happens After Your Portfolio Hits $250K" views=79612 age=169d ratio=13.51 [LONG]
  - xADW156N6AU "Once You Hit This Number, Saving Barely Matters" views=60847 age=69d ratio=11.72 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/169 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification