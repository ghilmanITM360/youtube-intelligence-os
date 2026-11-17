# This make cents
Channel id `UCWrtDO6izx1KXQu_BZBrQYg` · niche FINANCE · subs 4950 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 20 (Shorts 3, Long-form 17)
- Views (all): n=20 | total=1508465 | mean=75423.2 | median=18476.0 | max=611170 | min=170 | p10=324 | p25=1282 | p75=52863 | p90=145158 | p99=577083 | cv=2.05

## 2. Performance Distribution
- All: p10=324 p25=1282 median=18476.0 p75=52863 p90=145158 p99=577083 CV=2.05
- Mean/median ratio: 4.08 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=3 | total=735 | mean=245 | median=231 | max=334 | min=170 | p10=182 | p25=200 | p75=282 | p90=313 | p99=332 | cv=0.28
- Long-form: n=17 | total=1507730 | mean=88690 | median=27919 | max=611170 | min=888 | p10=1262 | p25=6621 | p75=75699 | p90=240693 | p99=582465 | cv=1.85

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 11 videos, median views 28415
- Money/Personal Finance: 3 videos, median views 1317
- Real Estate/Housing: 2 videos, median views 223570
- Business/Companies: 2 videos, median views 57100
- Debt/Banking: 1 videos, median views 6621
- Stocks/Investing: 1 videos, median views 334
- Duration bins: {'15-30m': 16, '8-15m': 1, '<=60s': 2, '1-3m': 1}

## 5. Publishing Pattern
- Date range: 2026-10-02 → 2026-11-05 (35 days); uploads/week ≈ 4.0
- Days between upload dates: median=2, mean=2, max=4; consistency (CV of gaps)=0.42
- Weekday counts: {'Wed': 4, 'Fri': 4, 'Mon': 2, 'Sun': 2, 'Sat': 3, 'Thu': 2, 'Tue': 3}
- Upload hour (UTC, only where timestamp exists, n=20): {0: 2, 1: 2, 2: 1, 11: 1, 16: 1, 17: 1, 18: 1, 19: 5, 20: 2, 21: 1, 22: 1, 23: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 17, 6623, 1.00
  - 2026-11: 3, 28415, 1.02
- Quarterly:
  - 2026-Q4: 20, 18476, 1.00

## 6. Performance Classification
- All: {'Underperforming': 6, 'Average': 8, 'Breakout': 2, 'Successful': 4}
- Shorts: {'Average': 3}  Long-form: {'Underperforming': 6, 'Average': 5, 'Breakout': 2, 'Successful': 4}
- Top 5 by age-adjusted ratio:
  - M0AcqoZ8zQg "Your Family Cut You Out of Grandpa's Will — Not Knowing You Already Ow" views=611170 age=18d ratio=21.89 [LONG]
  - po7HUg_7yYE "Your Wife Divorced You for a Richer Man — Now He Pays You Rent" views=431764 age=31d ratio=15.46 [LONG]
  - ce_tknjWnX4 "Your Ex-Wife Called You a Worthless Repairman — Not Knowing You Own th" views=113313 age=22d ratio=4.06 [LONG]
  - NKq_ay3HHWA "You Won $180 Million — And Your Boss Still Made You Work Christmas" views=89612 age=28d ratio=3.21 [LONG]
  - deu-mybF6Wg "Mom Signed Your Name for Your Brother’s $48,000 Truck — So You Took Yo" views=75699 age=12d ratio=2.71 [LONG]

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