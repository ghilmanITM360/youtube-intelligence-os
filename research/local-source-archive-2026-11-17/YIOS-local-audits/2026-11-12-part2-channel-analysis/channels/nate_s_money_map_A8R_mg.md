# Nate’s Money Map
Channel id `UCtOrKVgo-bsh4XoSCA8R_mg` · niche FINANCE · subs 1140 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 32 (Shorts 0, Long-form 32)
- Views (all): n=32 | total=1264450 | mean=39514.1 | median=4506.5 | max=322060 | min=372 | p10=849 | p25=1810 | p75=10822 | p90=118016 | p99=320709 | cv=2.34

## 2. Performance Distribution
- All: p10=849 p25=1810 median=4506.5 p75=10822 p90=118016 p99=320709 CV=2.34
- Mean/median ratio: 8.77 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=32 | total=1264450 | mean=39514.1 | median=4506.5 | max=322060 | min=372 | p10=849 | p25=1810 | p75=10822 | p90=118016 | p99=320709 | cv=2.34

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 17 videos, median views 4838
- Real Estate/Housing: 6 videos, median views 4635
- Money/Personal Finance: 5 videos, median views 6297
- Debt/Banking: 3 videos, median views 840
- Stocks/Investing: 1 videos, median views 1019
- Duration bins: {'8-15m': 28, '3-8m': 4}

## 5. Publishing Pattern
- Date range: 2026-09-26 → 2026-11-09 (45 days); uploads/week ≈ 4.98
- Days between upload dates: median=1, mean=1.5, max=8; consistency (CV of gaps)=0.96
- Weekday counts: {'Tue': 5, 'Sun': 4, 'Thu': 5, 'Fri': 5, 'Mon': 5, 'Sat': 5, 'Wed': 3}
- Upload hour (UTC, only where timestamp exists, n=32): {0: 2, 1: 1, 14: 3, 15: 1, 17: 2, 18: 1, 20: 10, 21: 9, 22: 3}
- Monthly (n, median views, age-adj median ratio):
  - 2026-09: 1, 942, 0.05
  - 2026-10: 24, 7338, 0.99
  - 2026-11: 7, 1019, 0.51
- Quarterly:
  - 2026-Q3: 1, 942, 0.05
  - 2026-Q4: 31, 4838, 0.93

## 6. Performance Classification
- All: {'Average': 12, 'Underperforming': 10, 'Successful': 6, 'Breakout': 4}
- Shorts: {}  Long-form: {'Average': 12, 'Underperforming': 10, 'Successful': 6, 'Breakout': 4}
- Top 5 by age-adjusted ratio:
  - V7vssWL3sdA "POV: Your Boss Cut Your Pay 15% to "Teach You a Lesson" — He Didn't Kn" views=322060 age=16d ratio=60.60 [LONG]
  - EFdMxvuYd8k "POV: Your New Boss Fires You After 19 Years — He Doesn't Know You Neve" views=315630 age=24d ratio=37.93 [LONG]
  - c8QJeBLLlE4 "POV: Your Side Hustle Pays More Than Your Job — Then Your Boss Finds O" views=317703 age=33d ratio=26.03 [LONG]
  - y0qkcS7wlk4 "POV: Your Brother Wants to Sell Dad's House Fast — He Doesn't Know You" views=126475 age=34d ratio=9.98 [LONG]
  - fixgUyuuXoI "POV: The Girl Who Dumped You for a Rich Guy Calls You for Help 16 Year" views=41887 age=25d ratio=4.80 [LONG]

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