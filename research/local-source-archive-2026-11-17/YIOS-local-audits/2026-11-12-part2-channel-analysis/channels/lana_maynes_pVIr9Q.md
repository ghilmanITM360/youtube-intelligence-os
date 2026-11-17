# Lana Maynes
Channel id `UCj0uhARVVmROWv9TBpVIr9Q` · niche FINANCE · subs 49400 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 89 (Shorts 0, Long-form 89)
- Views (all): n=89 | total=3521606 | mean=39568.6 | median=5397 | max=593426 | min=325 | p10=1503 | p25=2395 | p75=26532 | p90=121956 | p99=408429 | cv=2.23

## 2. Performance Distribution
- All: p10=1503 p25=2395 median=5397 p75=26532 p90=121956 p99=408429 CV=2.23
- Mean/median ratio: 7.33 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=89 | total=3521606 | mean=39568.6 | median=5397 | max=593426 | min=325 | p10=1503 | p25=2395 | p75=26532 | p90=121956 | p99=408429 | cv=2.23

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 45 videos, median views 3969
- Debt/Banking: 22 videos, median views 5396
- Money/Personal Finance: 17 videos, median views 9897
- Real Estate/Housing: 3 videos, median views 6531
- History/Explainers: 1 videos, median views 112436
- Geopolitics/Trade: 1 videos, median views 56414
- Duration bins: {'15-30m': 64, '8-15m': 23, '>30m': 2}

## 5. Publishing Pattern
- Date range: 2026-05-29 → 2026-11-08 (164 days); uploads/week ≈ 3.8
- Days between upload dates: median=2.0, mean=1.9, max=5; consistency (CV of gaps)=0.54
- Weekday counts: {'Mon': 10, 'Sat': 15, 'Sun': 13, 'Tue': 13, 'Thu': 13, 'Fri': 14, 'Wed': 11}
- Upload hour (UTC, only where timestamp exists, n=89): {0: 30, 1: 2, 2: 27, 11: 1, 13: 1, 15: 1, 17: 1, 19: 1, 21: 2, 22: 21, 23: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 3, 2092, 0.21
  - 2026-06: 26, 3990, 0.41
  - 2026-07: 17, 9660, 1.05
  - 2026-08: 11, 11322, 1.33
  - 2026-09: 14, 14223, 1.75
  - 2026-10: 16, 3930, 0.57
  - 2026-11: 2, 1300, 0.23
- Quarterly:
  - 2026-Q2: 29, 3617, 0.37
  - 2026-Q3: 42, 12333, 1.43
  - 2026-Q4: 18, 3388, 0.50

## 6. Performance Classification
- All: {'Underperforming': 36, 'Breakout': 14, 'Successful': 19, 'Average': 20}
- Shorts: {}  Long-form: {'Underperforming': 36, 'Breakout': 14, 'Successful': 19, 'Average': 20}
- Top 5 by age-adjusted ratio:
  - l3fJNx2rsnQ "If You Get Direct Deposits, These 3 New Rules Could Affect You Right N" views=593426 age=103d ratio=65.39 [LONG]
  - Iagjpu1NgcM "Born Before 1966? Your Bank Account Could Freeze After You Die" views=383202 age=135d ratio=39.93 [LONG]
  - gYOxqYgrcHY "If You Have a Checking Account, These 3 New Rules Could Affect You Rig" views=272897 age=106d ratio=29.89 [LONG]
  - HsXxk_4LHmA "SENIORS: Never Tell Your Bank These 3 Things — Could Freeze Your Accou" views=204432 age=34d ratio=27.94 [LONG]
  - aRQCASWpk2o "You Could Be Missing a Check (And Most People Don't Know It)" views=239539 age=142d ratio=24.70 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- coverage 89/90 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification