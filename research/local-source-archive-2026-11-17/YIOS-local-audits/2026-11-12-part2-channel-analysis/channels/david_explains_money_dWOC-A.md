# David Explains Money
Channel id `UC2ExrTzlNc8uNmNXodWOC-A` · niche FINANCE · subs 43500 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 4 (Shorts 0, Long-form 4)
- Views (all): n=4 | total=1659547 | mean=414886.8 | median=115031.5 | max=1427725 | min=1759 | p10=35500 | p25=86112 | p75=443807 | p90=1034158 | p99=1388368 | cv=1.41

## 2. Performance Distribution
- All: p10=35500 p25=86112 median=115031.5 p75=443807 p90=1034158 p99=1388368 CV=1.41
- Mean/median ratio: 3.61 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=4 | total=1659547 | mean=414886.8 | median=115031.5 | max=1427725 | min=1759 | p10=35500 | p25=86112 | p75=443807 | p90=1034158 | p99=1388368 | cv=1.41

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 3 videos, median views 115834
- Geopolitics/Trade: 1 videos, median views 114229
- Duration bins: {'8-15m': 1, '>30m': 1, '15-30m': 2}

## 5. Publishing Pattern
- Date range: 2026-06-18 → 2026-08-07 (51 days); uploads/week ≈ 0.55
- Days between upload dates: median=6, mean=16.7, max=38; consistency (CV of gaps)=0.91
- Weekday counts: {'Thu': 1, 'Wed': 1, 'Fri': 1, 'Tue': 1}
- Upload hour (UTC, only where timestamp exists, n=4): {19: 1, 20: 1, 22: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 3, 114229, 0.99
  - 2026-08: 1, 115834, 1.01
- Quarterly:
  - 2026-Q2: 3, 114229, 0.99
  - 2026-Q3: 1, 115834, 1.01

## 6. Performance Classification
- All: {'Underperforming': 1, 'Average': 2, 'Breakout': 1}
- Shorts: {}  Long-form: {'Underperforming': 1, 'Average': 2, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - oA0Pk1J9_mw "20 BORING BUSINESSES That Make Money While You Sleep" views=1427725 age=134d ratio=12.41 [LONG]
  - xA6oBoVyQ9I "10 BORING BUSINESSES That Quietly Make Money" views=115834 age=96d ratio=1.01 [LONG]
  - CVbUTKov9mQ "30 MACHINES to Import From CHINA to START Your HOME BUSINESS" views=114229 age=140d ratio=0.99 [LONG]
  - lMBDlOgjObI "Passive income vs Running a Business: Which One Actually Makes You Wea" views=1759 age=146d ratio=0.02 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 4 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification