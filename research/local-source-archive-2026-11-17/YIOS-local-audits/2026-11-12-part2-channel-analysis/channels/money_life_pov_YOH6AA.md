# Money Life POV
Channel id `UCCEwJbv7D1CYzxdKYYOH6AA` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 20 (Shorts 0, Long-form 20)
- Views (all): n=20 | total=866011 | mean=43300.6 | median=15586.5 | max=153088 | min=971 | p10=3220 | p25=7346 | p75=70720 | p90=130252 | p99=152195 | cv=1.14

## 2. Performance Distribution
- All: p10=3220 p25=7346 median=15586.5 p75=70720 p90=130252 p99=152195 CV=1.14
- Mean/median ratio: 2.78 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=20 | total=866011 | mean=43300.6 | median=15586.5 | max=153088 | min=971 | p10=3220 | p25=7346 | p75=70720 | p90=130252 | p99=152195 | cv=1.14

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 12 videos, median views 12894
- Other/Unclassified: 5 videos, median views 65335
- Debt/Banking: 1 videos, median views 91954
- Geopolitics/Trade: 1 videos, median views 128237
- Stocks/Investing: 1 videos, median views 971
- Duration bins: {'8-15m': 9, '15-30m': 11}

## 5. Publishing Pattern
- Date range: 2026-08-23 → 2026-09-11 (20 days); uploads/week ≈ 7.0
- Days between upload dates: median=1, mean=1, max=1; consistency (CV of gaps)=0.0
- Weekday counts: {'Tue': 3, 'Wed': 3, 'Mon': 3, 'Sat': 2, 'Fri': 3, 'Thu': 3, 'Sun': 3}
- Upload hour (UTC, only where timestamp exists, n=18): {12: 2, 13: 14, 15: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-08: 9, 12665, 0.81
  - 2026-09: 11, 36722, 2.36
- Quarterly:
  - 2026-Q3: 20, 15586, 1.00

## 6. Performance Classification
- All: {'Successful': 5, 'Average': 9, 'Underperforming': 3, 'Breakout': 3}
- Shorts: {}  Long-form: {'Successful': 5, 'Average': 9, 'Underperforming': 3, 'Breakout': 3}
- Top 5 by age-adjusted ratio:
  - Bh13NQLk5uo "POV: You Became the Rich Friend — Then Things Got Awkward" views=153088 age=70d ratio=9.82 [LONG]
  - H5r9VQgsQIg "POV: What Happens When You Start Paying Cash for Cars" views=148390 age=77d ratio=9.52 [LONG]
  - ewSvbxYk35Y "POV: You Skip College and Learn a Trade — Here’s What Happens" views=128237 age=64d ratio=8.23 [LONG]
  - BiXUk28HSDw "POV: You Pay Off Your House While Everyone Else Still Has a Mortgage" views=91954 age=62d ratio=5.90 [LONG]
  - -uQnQ57J1lU "POV: You Start Buying Cars With Cash — Everything Changes" views=86877 age=68d ratio=5.57 [LONG]

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