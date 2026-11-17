# Lucas Grant
Channel id `UCTcOboZIhgrKHMDm-oTlTOg` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 95 (Shorts 0, Long-form 95)
- Views (all): n=85 | total=2090721 | mean=24596.7 | median=7141 | max=704753 | min=795 | p10=2694 | p25=3862 | p75=15152 | p90=30713 | p99=341843 | cv=3.31

## 2. Performance Distribution
- All: p10=2694 p25=3862 median=7141 p75=15152 p90=30713 p99=341843 CV=3.31
- Mean/median ratio: 3.44 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=85 | total=2090721 | mean=24596.7 | median=7141 | max=704753 | min=795 | p10=2694 | p25=3862 | p75=15152 | p90=30713 | p99=341843 | cv=3.31

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 47 videos, median views 7341
- Other/Unclassified: 13 videos, median views 16058
- Stocks/Investing: 11 videos, median views 6993
- Debt/Banking: 6 videos, median views 3426
- History/Explainers: 3 videos, median views 4274
- Real Estate/Housing: 3 videos, median views 7141
- Geopolitics/Trade: 1 videos, median views 4282
- Business/Companies: 1 videos, median views 5436
- Duration bins: {'15-30m': 95}

## 5. Publishing Pattern
- Date range: 2026-06-08 → 2026-09-10 (95 days); uploads/week ≈ 6.78
- Days between upload dates: median=1, mean=1.0, max=2; consistency (CV of gaps)=0.17
- Weekday counts: {'Fri': 12, 'Sat': 13, 'Thu': 14, 'Sun': 13, 'Tue': 14, 'Mon': 13, 'Wed': 13}
- Upload hour (UTC, only where timestamp exists, n=92): {11: 17, 12: 39, 13: 20, 14: 1, 15: 3, 16: 12}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 23, 13044, 1.07
  - 2026-07: 31, 6222, 0.66
  - 2026-08: 28, 4995, 0.62
  - 2026-09: 10, 7971, 1.32
- Quarterly:
  - 2026-Q2: 23, 13044, 1.07
  - 2026-Q3: 69, 6222, 0.78

## 6. Performance Classification
- All: {'Average': 40, 'Unclassified (no views)': 10, 'Successful': 20, 'Underperforming': 19, 'Breakout': 6}
- Shorts: {}  Long-form: {'Average': 40, 'Unclassified (no views)': 10, 'Successful': 20, 'Underperforming': 19, 'Breakout': 6}
- Top 5 by age-adjusted ratio:
  - ElGhlrZNb_4 "Living Rich in Secret Changes You More Than You Think." views=704753 age=155d ratio=57.75 [LONG]
  - by_Ah5cDyP8 "POV: What Happens When You Start Paying Cash for Cars" views=272717 age=72d ratio=44.07 [LONG]
  - PLgVQhvtU_A "Your Life After Winning the $600 Million Lottery And Nobody Knows" views=99219 age=118d ratio=10.39 [LONG]
  - 69VInHOHsYM "POV: You Paid Off Your Mortgage 20 Years Early — Life Is Never The Sam" views=55038 age=67d ratio=9.46 [LONG]
  - rkGn4RNQJC0 "POV: Living in the Same House for 20 Years — What It Quietly Does to Y" views=89159 age=139d ratio=8.06 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- 3 videos lack publish date (excluded from time/age analysis)
- 10 videos lack view counts
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification