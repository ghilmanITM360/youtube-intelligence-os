# Finance ANALYST
Channel id `UCWQA4bQidJMFH3odS-RGEyA` · niche FINANCE · subs 2850 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 29 (Shorts 0, Long-form 29)
- Views (all): n=29 | total=579587 | mean=19985.8 | median=1696 | max=367569 | min=145 | p10=337 | p25=801 | p75=6096 | p90=21974 | p99=285777 | cv=3.37

## 2. Performance Distribution
- All: p10=337 p25=801 median=1696 p75=6096 p90=21974 p99=285777 CV=3.37
- Mean/median ratio: 11.78 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=29 | total=579587 | mean=19985.8 | median=1696 | max=367569 | min=145 | p10=337 | p25=801 | p75=6096 | p90=21974 | p99=285777 | cv=3.37

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 12 videos, median views 1264
- Other/Unclassified: 9 videos, median views 987
- Business/Companies: 5 videos, median views 4048
- Debt/Banking: 2 videos, median views 15254
- Stocks/Investing: 1 videos, median views 1533
- Duration bins: {'15-30m': 18, '8-15m': 11}

## 5. Publishing Pattern
- Date range: 2026-06-05 → 2026-11-01 (150 days); uploads/week ≈ 1.35
- Days between upload dates: median=2.0, mean=5.3, max=94; consistency (CV of gaps)=3.22
- Weekday counts: {'Fri': 5, 'Thu': 4, 'Sun': 6, 'Mon': 4, 'Wed': 5, 'Tue': 1, 'Sat': 4}
- Upload hour (UTC, only where timestamp exists, n=29): {16: 2, 17: 5, 18: 12, 19: 3, 20: 2, 21: 5}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 8, 690, 0.41
  - 2026-09: 5, 801, 0.47
  - 2026-10: 15, 6070, 3.58
  - 2026-11: 1, 1631, 0.96
- Quarterly:
  - 2026-Q2: 8, 690, 0.41
  - 2026-Q3: 5, 801, 0.47
  - 2026-Q4: 16, 5042, 2.97

## 6. Performance Classification
- All: {'Successful': 6, 'Average': 10, 'Underperforming': 6, 'Breakout': 7}
- Shorts: {}  Long-form: {'Successful': 6, 'Average': 10, 'Underperforming': 6, 'Breakout': 7}
- Top 5 by age-adjusted ratio:
  - 3L4Mypm3uWo "POV: You Go to Your 10-Year Reunion as a Secret Multimillionaire" views=367569 age=37d ratio=216.60 [LONG]
  - vltf4XOWLg8 "POV: You Won the Lottery the Morning After Your Ex Left You" views=75455 age=16d ratio=44.46 [LONG]
  - BspuJfCPnFw "POV: You Turned a Bankrupt Factory Into an $800 Million Business" views=26494 age=28d ratio=15.61 [LONG]
  - DChwF6upfr0 "POV: You Won the Lottery and Told No One — 10 Years Later" views=20844 age=21d ratio=12.28 [LONG]
  - EaBdVxh2yiI "POV: Your Ex Found Out You Got Rich — Now She Wants You Back" views=18915 age=32d ratio=11.15 [LONG]

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