# The Wise Future
Channel id `UC5OaD2jizn_ZFQrB6jzXo4g` · niche FINANCE · subs 9410 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 93 (Shorts 0, Long-form 93)
- Views (all): n=93 | total=1094389 | mean=11767.6 | median=3582 | max=153100 | min=246 | p10=813 | p25=1476 | p75=13068 | p90=29359 | p99=83013 | cv=1.79

## 2. Performance Distribution
- All: p10=813 p25=1476 median=3582 p75=13068 p90=29359 p99=83013 CV=1.79
- Mean/median ratio: 3.29 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=93 | total=1094389 | mean=11767.6 | median=3582 | max=153100 | min=246 | p10=813 | p25=1476 | p75=13068 | p90=29359 | p99=83013 | cv=1.79

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 74 videos, median views 4784
- Stocks/Investing: 6 videos, median views 2378
- Other/Unclassified: 4 videos, median views 4041
- History/Explainers: 3 videos, median views 2886
- Debt/Banking: 3 videos, median views 1318
- Real Estate/Housing: 2 videos, median views 1099
- Geopolitics/Trade: 1 videos, median views 795
- Duration bins: {'15-30m': 72, '8-15m': 19, '>30m': 2}

## 5. Publishing Pattern
- Date range: 2026-01-24 → 2026-11-10 (291 days); uploads/week ≈ 2.24
- Days between upload dates: median=1.5, mean=3.2, max=58; consistency (CV of gaps)=2.07
- Weekday counts: {'Sat': 12, 'Thu': 10, 'Mon': 15, 'Wed': 14, 'Tue': 13, 'Fri': 14, 'Sun': 15}
- Upload hour (UTC, only where timestamp exists, n=93): {15: 14, 21: 78, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-01: 1, 10033, 1.43
  - 2026-02: 3, 1652, 0.24
  - 2026-03: 7, 4021, 0.61
  - 2026-04: 7, 1604, 0.26
  - 2026-05: 13, 2424, 0.43
  - 2026-06: 14, 13208, 2.58
  - 2026-07: 25, 8476, 1.92
  - 2026-08: 9, 4822, 1.12
  - 2026-10: 8, 4842, 2.16
  - 2026-11: 6, 420, 0.28
- Quarterly:
  - 2026-Q1: 11, 3539, 0.55
  - 2026-Q2: 34, 2798, 0.50
  - 2026-Q3: 34, 6940, 1.57
  - 2026-Q4: 14, 784, 0.45

## 6. Performance Classification
- All: {'Underperforming': 31, 'Successful': 27, 'Average': 26, 'Breakout': 9}
- Shorts: {}  Long-form: {'Underperforming': 31, 'Successful': 27, 'Average': 26, 'Breakout': 9}
- Top 5 by age-adjusted ratio:
  - Tb7UOW1YQvQ "How Rich Is The Average Retiree? The Numbers May Surprise You" views=153100 age=149d ratio=29.76 [LONG]
  - 6BE5R3ezaA0 "The Psychology of Money's Lesson Most People Ignore" views=76918 age=139d ratio=15.44 [LONG]
  - D-VAe0-EMjM "Why So Many Retired Government Workers Become Quiet Millionaires" views=72862 age=126d ratio=15.30 [LONG]
  - UWsFzSG7aXc "What Monthly Income Does The Average Retiree Live On?" views=26749 age=16d ratio=13.10 [LONG]
  - 0eCcQaP6KDo "6 Signs You're Already in the Top 10% of Retirees" views=30021 age=26d ratio=12.35 [LONG]

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