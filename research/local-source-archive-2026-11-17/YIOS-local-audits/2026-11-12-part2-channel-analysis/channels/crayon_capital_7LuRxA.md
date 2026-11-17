# Crayon Capital
Channel id `UCP9RPj_BG0vit2TNM7LuRxA` · niche ECONOMICS · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=19020365 | mean=634012.2 | median=249585.5 | max=4219017 | min=40623 | p10=67332 | p25=111540 | p75=800082 | p90=1422087 | p99=3796720 | cv=1.45

## 2. Performance Distribution
- All: p10=67332 p25=111540 median=249585.5 p75=800082 p90=1422087 p99=3796720 CV=1.45
- Mean/median ratio: 2.54 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=19020365 | mean=634012.2 | median=249585.5 | max=4219017 | min=40623 | p10=67332 | p25=111540 | p75=800082 | p90=1422087 | p99=3796720 | cv=1.45

## 4. Topic Distribution (heuristic)
- History/Explainers: 12 videos, median views 225628
- Business/Companies: 6 videos, median views 511378
- Inflation/Recession/Macro: 4 videos, median views 1177521
- Geopolitics/Trade: 3 videos, median views 162152
- Other/Unclassified: 2 videos, median views 507204
- Money/Personal Finance: 2 videos, median views 897678
- Crypto/Bitcoin: 1 videos, median views 118266
- Duration bins: {'15-30m': 14, '8-15m': 16}

## 5. Publishing Pattern
- Date range: 2025-04-22 → 2026-09-09 (506 days); uploads/week ≈ 0.42
- Days between upload dates: median=16, mean=17.4, max=38; consistency (CV of gaps)=0.46
- Weekday counts: {'Sat': 9, 'Fri': 4, 'Sun': 3, 'Tue': 4, 'Mon': 4, 'Wed': 3, 'Thu': 3}
- Upload hour (UTC, only where timestamp exists, n=29): {3: 2, 5: 1, 7: 1, 9: 1, 10: 5, 11: 3, 12: 2, 13: 4, 14: 5, 15: 1, 16: 3, 17: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2025-04: 1, 69270, 0.11
  - 2025-05: 1, 206967, 0.33
  - 2025-06: 2, 1197535, 2.05
  - 2025-07: 2, 519256, 0.95
  - 2025-08: 1, 2762821, 5.33
  - 2025-09: 1, 372112, 0.76
  - 2025-10: 2, 2305886, 4.99
  - 2025-11: 1, 1006867, 2.49
  - 2025-12: 2, 705942, 1.87
  - 2026-01: 2, 513548, 1.46
  - 2026-02: 2, 785206, 2.57
  - 2026-03: 2, 385285, 1.36
  - 2026-04: 2, 208517, 0.87
  - 2026-05: 1, 49890, 0.24
  - 2026-06: 2, 99674, 0.58
  - 2026-07: 2, 316761, 2.05
  - 2026-08: 3, 103771, 0.98
  - 2026-09: 1, 98218, 1.16
- Quarterly:
  - 2025-Q2: 4, 158132, 0.26
  - 2025-Q3: 4, 646180, 1.22
  - 2025-Q4: 5, 973784, 2.49
  - 2026-Q1: 6, 385285, 1.36
  - 2026-Q2: 5, 158725, 0.66
  - 2026-Q3: 6, 103612, 1.07

## 6. Performance Classification
- All: {'Average': 12, 'Breakout': 1, 'Successful': 10, 'Underperforming': 7}
- Shorts: {}  Long-form: {'Average': 12, 'Breakout': 1, 'Successful': 10, 'Underperforming': 7}
- Top 5 by age-adjusted ratio:
  - HawmGu7oNrc "The Wolf of Wall Street Scam Explained Like You're 5" views=4219017 age=404d ratio=9.08 [LONG]
  - LuEcoqizj0o "The Great Depression Explained Like You’re 5" views=2762821 age=453d ratio=5.33 [LONG]
  - sMH8WchxQR8 "Rockefeller: The First Confirmed Billionaire (And How He Did It)" views=1326122 age=256d ratio=4.38 [LONG]
  - KE-WJevx-7c "The 2008 Financial Crisis Explained Like You’re 5" views=2285772 age=514d ratio=3.91 [LONG]
  - 1GowFTjbUnk "NVIDIA Explained Like You're 5" views=584655 age=125d ratio=3.75 [LONG]

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