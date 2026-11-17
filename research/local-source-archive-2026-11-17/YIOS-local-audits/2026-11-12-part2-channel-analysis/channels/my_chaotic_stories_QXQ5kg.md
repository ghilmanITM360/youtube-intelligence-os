# My Chaotic Stories
Channel id `UC9m3w-9L_Bt34x02IQXQ5kg` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 23 (Shorts 0, Long-form 23)
- Views (all): n=23 | total=1172814 | mean=50991.9 | median=3605 | max=592649 | min=742 | p10=943 | p25=2090 | p75=13761 | p90=39624 | p99=552138 | cv=2.78

## 2. Performance Distribution
- All: p10=943 p25=2090 median=3605 p75=13761 p90=39624 p99=552138 CV=2.78
- Mean/median ratio: 14.14 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=23 | total=1172814 | mean=50991.9 | median=3605 | max=592649 | min=742 | p10=943 | p25=2090 | p75=13761 | p90=39624 | p99=552138 | cv=2.78

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 11 videos, median views 2521
- Money/Personal Finance: 9 videos, median views 7726
- History/Explainers: 1 videos, median views 764
- Debt/Banking: 1 videos, median views 4083
- Geopolitics/Trade: 1 videos, median views 1349
- Duration bins: {'8-15m': 23}

## 5. Publishing Pattern
- Date range: 2026-05-02 → 2026-08-01 (92 days); uploads/week ≈ 1.75
- Days between upload dates: median=3.0, mean=4.1, max=15; consistency (CV of gaps)=0.72
- Weekday counts: {'Fri': 4, 'Sat': 4, 'Thu': 1, 'Wed': 6, 'Mon': 2, 'Sun': 5, 'Tue': 1}
- Upload hour (UTC, only where timestamp exists, n=23): {11: 1, 12: 3, 13: 4, 14: 2, 15: 5, 16: 1, 17: 2, 18: 4, 19: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 13, 4343, 0.65
  - 2026-06: 6, 3160, 0.66
  - 2026-07: 3, 2581, 1.06
  - 2026-08: 1, 2237, 1.37
- Quarterly:
  - 2026-Q2: 19, 4083, 0.65
  - 2026-Q3: 4, 2551, 1.22

## 6. Performance Classification
- All: {'Underperforming': 7, 'Successful': 6, 'Average': 8, 'Breakout': 2}
- Shorts: {}  Long-form: {'Underperforming': 7, 'Successful': 6, 'Average': 8, 'Breakout': 2}
- Top 5 by age-adjusted ratio:
  - dwSfdH1K7Zk "POV: You Have $1 Trillion (But Only 7 Days To Spend It)" views=592649 age=167d ratio=83.93 [LONG]
  - elR5mlDg7sY "What It’s Like to Be a Billionaire’s Family Member" views=408509 age=189d ratio=39.83 [LONG]
  - ZGwFdQ8KY4M "POV: You're a Saudi Prince Born Into a $1.4 TRILLION Dynasty." views=41799 age=169d ratio=5.71 [LONG]
  - j0b82s0_o-M "How People Treat You Based On Your Wealth" views=30923 age=186d ratio=3.16 [LONG]
  - Ume6pLifF7A "Your Life at Every Level of North Korean Society" views=26302 age=180d ratio=2.97 [LONG]

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