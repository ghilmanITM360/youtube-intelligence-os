# Brimm.
Channel id `UC1GwXFBhh1fiLLuZxs8VRXA` · niche ECONOMICS · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 44 (Shorts 0, Long-form 44)
- Views (all): n=44 | total=1838962 | mean=41794.6 | median=6404.5 | max=536220 | min=838 | p10=1639 | p25=3098 | p75=17538 | p90=115105 | p99=432599 | cv=2.38

## 2. Performance Distribution
- All: p10=1639 p25=3098 median=6404.5 p75=17538 p90=115105 p99=432599 CV=2.38
- Mean/median ratio: 6.53 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=44 | total=1838962 | mean=41794.6 | median=6404.5 | max=536220 | min=838 | p10=1639 | p25=3098 | p75=17538 | p90=115105 | p99=432599 | cv=2.38

## 4. Topic Distribution (heuristic)
- History/Explainers: 19 videos, median views 6401
- Geopolitics/Trade: 9 videos, median views 6408
- Business/Companies: 5 videos, median views 11118
- Money/Personal Finance: 4 videos, median views 19618
- Inflation/Recession/Macro: 4 videos, median views 5520
- Other/Unclassified: 3 videos, median views 2886
- Duration bins: {'8-15m': 39, '3-8m': 5}

## 5. Publishing Pattern
- Date range: 2024-08-09 → 2026-09-03 (756 days); uploads/week ≈ 0.41
- Days between upload dates: median=9, mean=17.6, max=216; consistency (CV of gaps)=1.89
- Weekday counts: {'Sun': 17, 'Wed': 8, 'Mon': 5, 'Thu': 9, 'Fri': 1, 'Tue': 4}
- Upload hour (UTC, only where timestamp exists, n=44): {10: 1, 11: 1, 12: 2, 14: 1, 15: 12, 16: 10, 17: 11, 18: 3, 19: 2, 21: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2024-08: 1, 9681, 1.51
  - 2024-09: 1, 1558, 0.24
  - 2025-04: 1, 1619, 0.25
  - 2025-07: 1, 2378, 0.37
  - 2025-08: 2, 79488, 12.41
  - 2025-09: 2, 62485, 9.76
  - 2025-10: 3, 13922, 2.17
  - 2025-11: 2, 2704, 0.42
  - 2025-12: 3, 46928, 7.33
  - 2026-01: 2, 7054, 1.10
  - 2026-02: 4, 3166, 0.49
  - 2026-03: 4, 7214, 1.13
  - 2026-04: 4, 8692, 1.36
  - 2026-05: 2, 5822, 0.91
  - 2026-06: 3, 21250, 3.32
  - 2026-07: 3, 15368, 2.40
  - 2026-08: 5, 5798, 0.91
  - 2026-09: 1, 16249, 2.54
- Quarterly:
  - 2024-Q3: 2, 5620, 0.88
  - 2025-Q2: 1, 1619, 0.25
  - 2025-Q3: 5, 12418, 1.94
  - 2025-Q4: 8, 8951, 1.40
  - 2026-Q1: 10, 5001, 0.78
  - 2026-Q2: 9, 8498, 1.33
  - 2026-Q3: 9, 6408, 1.00

## 6. Performance Classification
- All: {'Average': 17, 'Successful': 12, 'Underperforming': 8, 'Breakout': 7}
- Shorts: {}  Long-form: {'Average': 17, 'Successful': 12, 'Underperforming': 8, 'Breakout': 7}
- Top 5 by age-adjusted ratio:
  - m5WPi3LX9z0 "Why Airlines Use This Exact Layout" views=536220 age=209d ratio=83.71 [LONG]
  - S81NPqovOT8 "Why Are the Dutch So Good at Ecommerce?" views=295240 age=154d ratio=46.09 [LONG]
  - wlvup8NLKaY "How This Unassuming Store Is Quietly Changing America" views=282388 age=318d ratio=44.09 [LONG]
  - ptSGP4msJyQ "What Airbnb Did to Athens in 10 Years" views=157291 age=458d ratio=24.56 [LONG]
  - xduAgq_9xNk "How the Rich Ruined Berlin's Nightlife" views=116199 age=401d ratio=18.14 [LONG]

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