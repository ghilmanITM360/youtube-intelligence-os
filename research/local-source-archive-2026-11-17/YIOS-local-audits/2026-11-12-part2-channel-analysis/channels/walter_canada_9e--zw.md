# Walter Canada
Channel id `UCQng0CgVwiA79VEPJ9e--zw` · niche FINANCE · subs 43700 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 69 (Shorts 0, Long-form 69)
- Views (all): n=69 | total=3531199 | mean=51176.8 | median=17858 | max=299536 | min=516 | p10=1790 | p25=4205 | p75=60052 | p90=167994 | p99=278885 | cv=1.41

## 2. Performance Distribution
- All: p10=1790 p25=4205 median=17858 p75=60052 p90=167994 p99=278885 CV=1.41
- Mean/median ratio: 2.87 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=69 | total=3531199 | mean=51176.8 | median=17858 | max=299536 | min=516 | p10=1790 | p25=4205 | p75=60052 | p90=167994 | p99=278885 | cv=1.41

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 31 videos, median views 17830
- Money/Personal Finance: 14 videos, median views 8145
- Debt/Banking: 12 videos, median views 44728
- Geopolitics/Trade: 4 videos, median views 4289
- History/Explainers: 3 videos, median views 10113
- Real Estate/Housing: 3 videos, median views 166493
- Stocks/Investing: 2 videos, median views 82216
- Duration bins: {'15-30m': 66, '8-15m': 2, '1-3m': 1}

## 5. Publishing Pattern
- Date range: 2026-06-02 → 2026-11-09 (161 days); uploads/week ≈ 3.0
- Days between upload dates: median=1.0, mean=2.5, max=76; consistency (CV of gaps)=3.74
- Weekday counts: {'Wed': 8, 'Thu': 11, 'Mon': 11, 'Sun': 9, 'Tue': 11, 'Fri': 11, 'Sat': 8}
- Upload hour (UTC, only where timestamp exists, n=69): {0: 1, 1: 1, 2: 2, 3: 1, 4: 1, 10: 1, 11: 8, 12: 7, 13: 6, 14: 2, 15: 8, 16: 6, 17: 6, 18: 5, 19: 7, 20: 3, 22: 3, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 1, 516, 0.03
  - 2026-08: 9, 13335, 0.75
  - 2026-09: 19, 17858, 1.00
  - 2026-10: 30, 18440, 1.03
  - 2026-11: 10, 8390, 0.47
- Quarterly:
  - 2026-Q2: 1, 516, 0.03
  - 2026-Q3: 28, 15596, 0.87
  - 2026-Q4: 40, 18038, 1.01

## 6. Performance Classification
- All: {'Underperforming': 23, 'Successful': 16, 'Breakout': 11, 'Average': 19}
- Shorts: {}  Long-form: {'Underperforming': 23, 'Successful': 16, 'Breakout': 11, 'Average': 19}
- Top 5 by age-adjusted ratio:
  - t_7Eywj3t4g "MOVE THESE 4 ASSETS BEFORE YOUR SPOUSE PASSES: The CRA Takes 44% If Yo" views=299536 age=42d ratio=16.77 [LONG]
  - ADbKCKygKgE "CPP and OAS Just Changed for Every Canadian Born Before 1967" views=269167 age=12d ratio=15.07 [LONG]
  - SF1Nop3vmEg "New 401 and Highway Rules Begin NOW — Millions of Canadian Drivers Cou" views=240657 age=19d ratio=13.48 [LONG]
  - ypXxNxsTOFU "Never Keep Over THIS AMOUNT in Your Bank After 65 — It Quietly Destroy" views=208799 age=38d ratio=11.69 [LONG]
  - 6dJBzSTa7bU "Every Canadian Senior Must Do This Before October 1 — Most Never Do" views=187649 age=46d ratio=10.51 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- coverage 69/107 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification