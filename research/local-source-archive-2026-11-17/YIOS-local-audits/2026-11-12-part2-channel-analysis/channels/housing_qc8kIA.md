# Housing
Channel id `UC3Tzh0Wu1C9s3AI2Oqc8kIA` · niche FINANCE · subs 3690 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 24 (Shorts 0, Long-form 24)
- Views (all): n=24 | total=577588 | mean=24066.2 | median=668.5 | max=185127 | min=29 | p10=44 | p25=119 | p75=9490 | p90=114066 | p99=171581 | cv=2.09

## 2. Performance Distribution
- All: p10=44 p25=119 median=668.5 p75=9490 p90=114066 p99=171581 CV=2.09
- Mean/median ratio: 36.0 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=24 | total=577588 | mean=24066.2 | median=668.5 | max=185127 | min=29 | p10=44 | p25=119 | p75=9490 | p90=114066 | p99=171581 | cv=2.09

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 8 videos, median views 166
- Other/Unclassified: 8 videos, median views 2542
- Debt/Banking: 4 videos, median views 63138
- Inflation/Recession/Macro: 2 videos, median views 430
- History/Explainers: 1 videos, median views 13698
- Real Estate/Housing: 1 videos, median views 1077
- Duration bins: {'15-30m': 18, '>30m': 3, '8-15m': 3}

## 5. Publishing Pattern
- Date range: 2026-09-14 → 2026-11-09 (57 days); uploads/week ≈ 2.95
- Days between upload dates: median=2.0, mean=2.5, max=20; consistency (CV of gaps)=1.52
- Weekday counts: {'Mon': 4, 'Fri': 3, 'Tue': 3, 'Thu': 3, 'Sat': 4, 'Sun': 3, 'Wed': 4}
- Upload hour (UTC, only where timestamp exists, n=24): {0: 1, 3: 1, 17: 1, 18: 7, 19: 3, 20: 1, 22: 2, 23: 8}
- Monthly (n, median views, age-adj median ratio):
  - 2026-09: 11, 124, 0.19
  - 2026-10: 11, 6033, 9.01
  - 2026-11: 2, 135, 0.20
- Quarterly:
  - 2026-Q3: 11, 124, 0.19
  - 2026-Q4: 13, 3972, 5.93

## 6. Performance Classification
- All: {'Underperforming': 10, 'Average': 3, 'Breakout': 8, 'Successful': 3}
- Shorts: {}  Long-form: {'Underperforming': 10, 'Average': 3, 'Breakout': 8, 'Successful': 3}
- Top 5 by age-adjusted ratio:
  - NXhhbwvx3Fg "Never Keep More Than This in the Bank After 65 — Most Seniors Miss The" views=185127 age=32d ratio=276.52 [LONG]
  - oPZjqx_6d1g "3 Banking Changes to Watch in 2026 That Could Affect Your Checking Acc" views=126232 age=55d ratio=188.55 [LONG]
  - tamw1y1Yd24 "Seniors: Don’t Miss This October 30 Deadline — Most Seniors Miss These" views=121418 age=24d ratio=181.36 [LONG]
  - hNuWYk9YQsc "7 Types of Income the IRS May Not Tax After 65 — Most Seniors Miss The" views=96911 age=44d ratio=144.75 [LONG]
  - e403nRaArVM "THE IRS JUST SENT MILLIONS A LETTER — Why Most Seniors May Get NOTHING" views=13698 age=36d ratio=20.46 [LONG]

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