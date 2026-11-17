# Primate Economics
Channel id `UC14Fb2zWTEZklONPXFbLrTQ` · niche FINANCE · subs 577000 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 13, Long-form 17)
- Views (all): n=30 | total=31893308 | mean=1063110.3 | median=296211.5 | max=15723552 | min=70064 | p10=108853 | p25=131234 | p75=960996 | p90=1467254 | p99=11674576 | cv=2.61

## 2. Performance Distribution
- All: p10=108853 p25=131234 median=296211.5 p75=960996 p90=1467254 p99=11674576 CV=2.61
- Mean/median ratio: 3.59 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=13 | total=19887105 | mean=1529777.3 | median=129622 | max=15723552 | min=70064 | p10=90670 | p25=109643 | p75=676622 | p90=1288204 | p99=14002901 | cv=2.69
- Long-form: n=17 | total=12006203 | mean=706247.2 | median=449156 | max=1761567 | min=119327 | p10=138809 | p25=168488 | p75=1121340 | p90=1496765 | p99=1728642 | cv=0.77

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 8 videos, median views 1144408
- Money/Personal Finance: 5 videos, median views 119327
- Crypto/Bitcoin: 4 videos, median views 157941
- Stocks/Investing: 4 videos, median views 671184
- History/Explainers: 3 videos, median views 254855
- Debt/Banking: 3 videos, median views 87902
- Geopolitics/Trade: 1 videos, median views 155558
- Business/Companies: 1 videos, median views 140634
- Real Estate/Housing: 1 videos, median views 449156
- Duration bins: {'8-15m': 12, '1-3m': 7, '<=60s': 7, '3-8m': 4}

## 5. Publishing Pattern
- Date range: 2025-03-28 → 2026-10-27 (579 days); uploads/week ≈ 0.36
- Days between upload dates: median=16, mean=19.9, max=63; consistency (CV of gaps)=0.85
- Weekday counts: {'Fri': 9, 'Mon': 6, 'Thu': 2, 'Sat': 3, 'Tue': 5, 'Wed': 4, 'Sun': 1}
- Upload hour (UTC, only where timestamp exists, n=30): {0: 1, 1: 2, 4: 1, 5: 2, 6: 1, 7: 2, 8: 2, 10: 1, 11: 6, 12: 6, 13: 3, 19: 1, 21: 1, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2025-03: 1, 1761567, 1.61
  - 2025-04: 4, 1182388, 8.82
  - 2025-05: 5, 676622, 1.42
  - 2025-06: 3, 129622, 1.00
  - 2025-07: 3, 87902, 0.68
  - 2025-08: 1, 1555788, 1.82
  - 2025-09: 2, 113232, 0.87
  - 2025-10: 1, 440510, 0.58
  - 2025-11: 1, 904024, 1.26
  - 2025-12: 1, 449156, 0.69
  - 2026-01: 1, 1121340, 1.91
  - 2026-03: 1, 254855, 0.53
  - 2026-05: 1, 155558, 0.42
  - 2026-07: 2, 241124, 0.93
  - 2026-08: 1, 136071, 0.66
  - 2026-09: 1, 140634, 1.11
  - 2026-10: 1, 119327, 1.98
- Quarterly:
  - 2025-Q1: 1, 1761567, 1.61
  - 2025-Q2: 12, 762062, 1.43
  - 2025-Q3: 6, 113232, 0.87
  - 2025-Q4: 3, 449156, 0.69
  - 2026-Q1: 2, 688098, 1.22
  - 2026-Q2: 1, 155558, 0.42
  - 2026-Q3: 4, 154561, 0.89
  - 2026-Q4: 1, 119327, 1.98

## 6. Performance Classification
- All: {'Average': 20, 'Successful': 7, 'Breakout': 2, 'Underperforming': 1}
- Shorts: {'Breakout': 2, 'Average': 8, 'Successful': 3}  Long-form: {'Average': 12, 'Successful': 4, 'Underperforming': 1}
- Top 5 by age-adjusted ratio:
  - ne0MlVZQasE "Inflation #animation #finance" views=15723552 age=581d ratio=121.30 [SHORT]
  - sQCillGdKk8 "Monkey explain Inflation #finance #animation" views=1384791 age=572d ratio=10.68 [SHORT]
  - tHgo3J-4iJA "Stocks explained with bananas #finance #investing" views=901857 age=565d ratio=6.96 [SHORT]
  - RMJtUGRJ8cs "Tariffs Explained with Bananas #finance" views=676622 age=552d ratio=5.22 [SHORT]
  - OU2Yehvtvik "#finance #investing #stockmarket" views=278664 age=557d ratio=2.15 [SHORT]

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