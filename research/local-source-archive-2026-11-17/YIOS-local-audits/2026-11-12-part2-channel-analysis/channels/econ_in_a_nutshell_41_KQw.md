# Econ in a Nutshell
Channel id `UC_DdIoJzHZXlEKTVy41_KQw` · niche ECONOMICS · subs 4550 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 14 (Shorts 0, Long-form 14)
- Views (all): n=14 | total=1445354 | mean=103239.6 | median=4831.5 | max=1039289 | min=190 | p10=247 | p25=1220 | p75=30993 | p90=201331 | p99=939550 | cv=2.6

## 2. Performance Distribution
- All: p10=247 p25=1220 median=4831.5 p75=30993 p90=201331 p99=939550 CV=2.6
- Mean/median ratio: 21.37 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=14 | total=1445354 | mean=103239.6 | median=4831.5 | max=1039289 | min=190 | p10=247 | p25=1220 | p75=30993 | p90=201331 | p99=939550 | cv=2.6

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 5 videos, median views 6119
- Real Estate/Housing: 2 videos, median views 31188
- Other/Unclassified: 2 videos, median views 12968
- Stocks/Investing: 1 videos, median views 203
- Crypto/Bitcoin: 1 videos, median views 190
- Inflation/Recession/Macro: 1 videos, median views 32624
- Debt/Banking: 1 videos, median views 3544
- Geopolitics/Trade: 1 videos, median views 350
- Duration bins: {'8-15m': 12, '3-8m': 2}

## 5. Publishing Pattern
- Date range: 2026-10-25 → 2026-11-11 (18 days); uploads/week ≈ 5.44
- Days between upload dates: median=1.0, mean=1.4, max=2; consistency (CV of gaps)=0.35
- Weekday counts: {'Wed': 3, 'Tue': 2, 'Sun': 4, 'Fri': 2, 'Mon': 3}
- Upload hour (UTC, only where timestamp exists, n=14): {2: 2, 3: 1, 6: 1, 10: 1, 13: 2, 14: 1, 15: 2, 16: 1, 18: 1, 19: 1, 21: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 5, 23261, 4.81
  - 2026-11: 9, 1542, 0.32
- Quarterly:
  - 2026-Q4: 14, 4832, 1.00

## 6. Performance Classification
- All: {'Underperforming': 5, 'Breakout': 3, 'Successful': 3, 'Average': 3}
- Shorts: {}  Long-form: {'Underperforming': 5, 'Breakout': 3, 'Successful': 3, 'Average': 3}
- Top 5 by age-adjusted ratio:
  - XgIo6SrSxS4 "Every Money Laundering Technique Explained" views=1039289 age=14d ratio=215.06 [LONG]
  - 5c81AORL5cI "Why You’ll Never Actually Spend Your Retirement Savings" views=272068 age=16d ratio=56.30 [LONG]
  - 337XyUfjfXs "Why Your Parents' Money Advice No Longer Works" views=36277 age=10d ratio=7.51 [LONG]
  - YPS4ag5a38E "How Inflation Actually Works (And Who It Really Hurts)" views=32624 age=5d ratio=6.75 [LONG]
  - 792HTqjzAJo "The Vancouver Model: How Drug Money Became Houses" views=26100 age=7d ratio=5.40 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 14 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification