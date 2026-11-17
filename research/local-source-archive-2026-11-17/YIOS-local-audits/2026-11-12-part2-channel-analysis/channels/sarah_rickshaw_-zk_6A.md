# Sarah Rickshaw
Channel id `UCn2nfMN6I-ozJikqW-zk_6A` · niche FINANCE · subs 1950 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 12 (Shorts 0, Long-form 12)
- Views (all): n=12 | total=452930 | mean=37744.2 | median=4869.0 | max=276511 | min=500 | p10=775 | p25=1008 | p75=35823 | p90=69816 | p99=254049 | cv=1.99

## 2. Performance Distribution
- All: p10=775 p25=1008 median=4869.0 p75=35823 p90=69816 p99=254049 CV=1.99
- Mean/median ratio: 7.75 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=12 | total=452930 | mean=37744.2 | median=4869.0 | max=276511 | min=500 | p10=775 | p25=1008 | p75=35823 | p90=69816 | p99=254049 | cv=1.99

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 10 videos, median views 4869
- Debt/Banking: 2 videos, median views 36641
- Duration bins: {'8-15m': 2, '15-30m': 9, '3-8m': 1}

## 5. Publishing Pattern
- Date range: 2026-10-12 → 2026-10-26 (15 days); uploads/week ≈ 5.6
- Days between upload dates: median=1, mean=1.3, max=3; consistency (CV of gaps)=0.48
- Weekday counts: {'Tue': 2, 'Mon': 3, 'Thu': 2, 'Sat': 1, 'Wed': 2, 'Fri': 2}
- Upload hour (UTC, only where timestamp exists, n=12): {14: 1, 15: 1, 17: 1, 18: 5, 19: 1, 20: 3}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 12, 4869, 1.00
- Quarterly:
  - 2026-Q4: 12, 4869, 1.00

## 6. Performance Classification
- All: {'Underperforming': 5, 'Breakout': 3, 'Average': 2, 'Successful': 2}
- Shorts: {}  Long-form: {'Underperforming': 5, 'Breakout': 3, 'Average': 2, 'Successful': 2}
- Top 5 by age-adjusted ratio:
  - 06XLtP1gyM0 "Every Senior Should Check These 7 Benefits for January 2027" views=276511 age=23d ratio=56.78 [LONG]
  - NXbwK51_1n8 "Never Keep More Than This in the Bank After 65 — Most Seniors Don’t Kn" views=72315 age=20d ratio=14.85 [LONG]
  - u8uufIVsWoc "Born Before 1967? 4 Social Security Changes Coming for You in 2027" views=47324 age=26d ratio=9.72 [LONG]
  - dJ0IX32h1fk "Seniors 65+: You Could Be Overpaying These 5 Bills Every Month" views=31989 age=30d ratio=6.57 [LONG]
  - 2khKtIjjx7s "Every Senior Should Check These 6 Things Before October Is Over" views=9984 age=27d ratio=2.05 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 12 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification