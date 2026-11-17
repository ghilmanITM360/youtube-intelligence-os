# Frank Law
Channel id `UCdFjOki_gKUfvDq3SmL36mg` · niche FINANCE · subs 10100 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 24 (Shorts 0, Long-form 24)
- Views (all): n=24 | total=1361526 | mean=56730.2 | median=10814.0 | max=767510 | min=641 | p10=1362 | p25=4260 | p75=35837 | p90=83690 | p99=623646 | cv=2.68

## 2. Performance Distribution
- All: p10=1362 p25=4260 median=10814.0 p75=35837 p90=83690 p99=623646 CV=2.68
- Mean/median ratio: 5.25 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=24 | total=1361526 | mean=56730.2 | median=10814.0 | max=767510 | min=641 | p10=1362 | p25=4260 | p75=35837 | p90=83690 | p99=623646 | cv=2.68

## 4. Topic Distribution (heuristic)
- Debt/Banking: 13 videos, median views 9540
- Money/Personal Finance: 6 videos, median views 13653
- Other/Unclassified: 4 videos, median views 6086
- Real Estate/Housing: 1 videos, median views 78054
- Duration bins: {'8-15m': 24}

## 5. Publishing Pattern
- Date range: 2026-10-13 → 2026-11-09 (28 days); uploads/week ≈ 6.0
- Days between upload dates: median=1, mean=1.2, max=3; consistency (CV of gaps)=0.41
- Weekday counts: {'Fri': 4, 'Sat': 3, 'Mon': 4, 'Wed': 4, 'Thu': 3, 'Tue': 3, 'Sun': 3}
- Upload hour (UTC, only where timestamp exists, n=24): {12: 16, 13: 7, 18: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 15, 22570, 0.57
  - 2026-11: 9, 2412, 0.97
- Quarterly:
  - 2026-Q4: 24, 10814, 0.95

## 6. Performance Classification
- All: {'Average': 7, 'Successful': 9, 'Breakout': 1, 'Underperforming': 7}
- Shorts: {}  Long-form: {'Average': 7, 'Successful': 9, 'Breakout': 1, 'Underperforming': 7}
- Top 5 by age-adjusted ratio:
  - V7lLK0JhzBQ "Never Keep More Than This in the Bank After 65 — Most Seniors Miss The" views=767510 age=27d ratio=14.13 [LONG]
  - 2k96-SsWwnk "Never Keep This Much Money in the Bank – HMRC Sees It All in 2026 (UK)" views=50502 age=14d ratio=3.87 [LONG]
  - WSswjv4iaTA "If You Have a Current Account, These 3 New Rules Could Affect You Righ" views=78054 age=19d ratio=3.18 [LONG]
  - G_V88MqGsvk "3 Banking Changes to Watch in 2026 That Could Affect Your Current Acco" views=142015 age=26d ratio=2.86 [LONG]
  - N3k728yvTK0 "The New £10,000 Bank Rule UK Seniors Are Never Told About" views=22570 age=11d ratio=2.73 [LONG]

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