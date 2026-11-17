# Capital Case
Channel id `UCZXShYiBJlahi8mCNiU3XBg` · niche ECONOMICS · subs 11700 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 13 (Shorts 0, Long-form 13)
- Views (all): n=13 | total=1493121 | mean=114855.5 | median=54229 | max=380137 | min=5128 | p10=5428 | p25=6379 | p75=189476 | p90=285111 | p99=369801 | cv=1.06

## 2. Performance Distribution
- All: p10=5428 p25=6379 median=54229 p75=189476 p90=285111 p99=369801 CV=1.06
- Mean/median ratio: 2.12 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=13 | total=1493121 | mean=114855.5 | median=54229 | max=380137 | min=5128 | p10=5428 | p25=6379 | p75=189476 | p90=285111 | p99=369801 | cv=1.06

## 4. Topic Distribution (heuristic)
- History/Explainers: 7 videos, median views 54229
- Other/Unclassified: 2 videos, median views 45977
- Geopolitics/Trade: 1 videos, median views 189476
- Real Estate/Housing: 1 videos, median views 5128
- Debt/Banking: 1 videos, median views 6379
- Inflation/Recession/Macro: 1 videos, median views 294004
- Duration bins: {'8-15m': 13}

## 5. Publishing Pattern
- Date range: 2026-02-22 → 2026-11-02 (254 days); uploads/week ≈ 0.36
- Days between upload dates: median=23.5, mean=21.1, max=47; consistency (CV of gaps)=0.66
- Weekday counts: {'Mon': 5, 'Fri': 3, 'Sun': 1, 'Wed': 1, 'Tue': 1, 'Sat': 1, 'Thu': 1}
- Upload hour (UTC, only where timestamp exists, n=13): {3: 1, 4: 2, 6: 1, 7: 2, 10: 1, 14: 1, 16: 2, 17: 2, 18: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-02: 2, 5968, 0.11
  - 2026-03: 1, 5396, 0.10
  - 2026-04: 1, 86396, 1.59
  - 2026-05: 2, 127333, 2.35
  - 2026-06: 2, 241740, 4.46
  - 2026-07: 1, 54229, 1.00
  - 2026-08: 2, 206362, 3.81
  - 2026-10: 1, 151523, 2.79
  - 2026-11: 1, 32769, 0.60
- Quarterly:
  - 2026-Q1: 3, 5558, 0.10
  - 2026-Q2: 5, 189476, 3.49
  - 2026-Q3: 3, 54229, 1.00
  - 2026-Q4: 2, 92146, 1.70

## 6. Performance Classification
- All: {'Average': 3, 'Successful': 6, 'Underperforming': 4}
- Shorts: {}  Long-form: {'Average': 3, 'Successful': 6, 'Underperforming': 4}
- Top 5 by age-adjusted ratio:
  - sGtEBUIppYc "Rockefeller Explained in 10 Minutes" views=380137 age=78d ratio=7.01 [LONG]
  - CAsim5HC-uI "How the Great Depression Actually Happened (The Fatal Decisions)" views=294004 age=142d ratio=5.42 [LONG]
  - 0k5C-MrLjAI "Strait of Hormuz Explained Like You're 5" views=249538 age=193d ratio=4.60 [LONG]
  - SwO1JS_9MCw "The Mistake That Started World War 2" views=189476 age=149d ratio=3.49 [LONG]
  - jjRo2QSMybU "The Rise (And Fall?) of BYD in 11 Minutes" views=151523 age=28d ratio=2.79 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 13 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification