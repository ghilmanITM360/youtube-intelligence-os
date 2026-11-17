# Tom - Lazy Investor
Channel id `UCHKwo7_qXD8ixLZmpPlIb_w` · niche FINANCE · subs 100000 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=2023376 | mean=20233.8 | median=13809.0 | max=282356 | min=334 | p10=4942 | p25=7304 | p75=22166 | p90=37882 | p99=91509 | cv=1.53

## 2. Performance Distribution
- All: p10=4942 p25=7304 median=13809.0 p75=22166 p90=37882 p99=91509 CV=1.53
- Mean/median ratio: 1.47 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=2023376 | mean=20233.8 | median=13809.0 | max=282356 | min=334 | p10=4942 | p25=7304 | p75=22166 | p90=37882 | p99=91509 | cv=1.53

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 47 videos, median views 14975
- Other/Unclassified: 29 videos, median views 13101
- History/Explainers: 7 videos, median views 17066
- Stocks/Investing: 5 videos, median views 15500
- Real Estate/Housing: 5 videos, median views 8311
- Debt/Banking: 4 videos, median views 7900
- Inflation/Recession/Macro: 2 videos, median views 19204
- Geopolitics/Trade: 1 videos, median views 6148
- Duration bins: {'15-30m': 30, '>30m': 70}

## 5. Publishing Pattern
- Date range: 2026-08-30 → 2026-11-11 (74 days); uploads/week ≈ 9.46
- Days between upload dates: median=1.0, mean=1.1, max=2; consistency (CV of gaps)=0.24
- Weekday counts: {'Sat': 10, 'Tue': 14, 'Thu': 15, 'Fri': 14, 'Mon': 18, 'Sun': 13, 'Wed': 16}
- Upload hour (UTC, only where timestamp exists, n=100): {0: 22, 1: 10, 12: 45, 13: 14, 14: 2, 15: 5, 16: 1, 20: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-08: 2, 16390, 0.89
  - 2026-09: 29, 14374, 0.79
  - 2026-10: 48, 16206, 1.26
  - 2026-11: 21, 7452, 0.83
- Quarterly:
  - 2026-Q3: 31, 14374, 0.79
  - 2026-Q4: 69, 13308, 1.17

## 6. Performance Classification
- All: {'Underperforming': 12, 'Average': 57, 'Successful': 30, 'Breakout': 1}
- Shorts: {}  Long-form: {'Underperforming': 12, 'Average': 57, 'Successful': 30, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - Gkx0f8OEQGg "You're Secretly Ahead at 55 If These Numbers Are True" views=282356 age=29d ratio=20.78 [LONG]
  - YklU63xsHVU "Same Name, Different Rules: Roth IRA vs Roth 401(k) Once You Hit 50" views=89581 age=28d ratio=6.66 [LONG]
  - Xx8YV5xulI4 "How Much Should You Have in Your 401(k) By Age? (2026)" views=61201 age=15d ratio=5.43 [LONG]
  - nyX96CbRYck "I Tested Converting a $2M IRA to Roth. Here's What I Found" views=89127 age=70d ratio=4.92 [LONG]
  - MPjV5FmBmBY "The Hardest Decade of Your Life Is Between 55 and 65. Here's Why" views=51213 age=20d ratio=4.20 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/535 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification