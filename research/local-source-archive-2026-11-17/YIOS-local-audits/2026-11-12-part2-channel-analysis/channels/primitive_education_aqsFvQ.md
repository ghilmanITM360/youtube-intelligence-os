# Primitive Education
Channel id `UCsuQtyrMiUPdHUQ8WaqsFvQ` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 13 (Shorts 11, Long-form 2)
- Views (all): n=13 | total=236170 | mean=18166.9 | median=14186 | max=80739 | min=3184 | p10=5753 | p25=9053 | p75=19802 | p90=21706 | p99=73662 | cv=1.04

## 2. Performance Distribution
- All: p10=5753 p25=9053 median=14186 p75=19802 p90=21706 p99=73662 CV=1.04
- Mean/median ratio: 1.28 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=11 | total=135629 | mean=12329.9 | median=11994 | max=21766 | min=3184 | p10=5277 | p25=8356 | p75=15698 | p90=21464 | p99=21736 | cv=0.47
- Long-form: n=2 | total=100541 | mean=50270.5 | median=50270.5 | max=80739 | min=19802 | p10=25896 | p25=35036 | p75=65505 | p90=74645 | p99=80130 | cv=0.61

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 8 videos, median views 9352
- Debt/Banking: 5 videos, median views 21464
- Duration bins: {'<=60s': 11, '1-3m': 2}

## 5. Publishing Pattern
- Date range: 2025-05-28 → 2025-08-18 (83 days); uploads/week ≈ 1.1
- Days between upload dates: median=1.0, mean=8.2, max=52; consistency (CV of gaps)=1.94
- Weekday counts: {'Thu': 3, 'Mon': 1, 'Wed': 3, 'Sat': 2, 'Sun': 1, 'Fri': 2, 'Tue': 1}
- Upload hour (UTC, only where timestamp exists, n=13): {10: 1, 16: 1, 18: 2, 19: 5, 20: 3, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2025-05: 5, 21464, 1.61
  - 2025-06: 1, 19802, 0.39
  - 2025-08: 7, 9053, 0.75
- Quarterly:
  - 2025-Q2: 6, 20633, 1.44
  - 2025-Q3: 7, 9053, 0.75

## 6. Performance Classification
- All: {'Average': 8, 'Successful': 3, 'Underperforming': 2}
- Shorts: {'Average': 8, 'Successful': 2, 'Underperforming': 1}  Long-form: {'Successful': 1, 'Underperforming': 1}
- Top 5 by age-adjusted ratio:
  - W8AVd7RhTME "caveman explain how mortgage work - part 4" views=21766 age=530d ratio=1.81 [SHORT]
  - S0tDBKXjuKc "caveman explain how mortgage work" views=21464 age=532d ratio=1.79 [SHORT]
  - RmTdnXHbI8s "Caveman Explain How Mortgage Work" views=80739 age=532d ratio=1.61 [LONG]
  - 5RYkAq7eMbg "A Caveman Explains Capitalism - Part 2" views=16057 age=455d ratio=1.34 [SHORT]
  - cZYdi9aFv6I "caveman explain how mortgage work - part 3" views=15338 age=531d ratio=1.28 [SHORT]

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