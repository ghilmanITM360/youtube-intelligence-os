# Max Invests
Channel id `UCXSpMZ1S5In6aRCyWdM5CAw` · niche FINANCE · subs 1800 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=154599 | mean=1546.0 | median=177.5 | max=34787 | min=11 | p10=45 | p25=88 | p75=837 | p90=2518 | p99=28731 | cv=3.18

## 2. Performance Distribution
- All: p10=45 p25=88 median=177.5 p75=837 p90=2518 p99=28731 CV=3.18
- Mean/median ratio: 8.71 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=154599 | mean=1546.0 | median=177.5 | max=34787 | min=11 | p10=45 | p25=88 | p75=837 | p90=2518 | p99=28731 | cv=3.18

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 46 videos, median views 137
- Stocks/Investing: 44 videos, median views 752
- Other/Unclassified: 3 videos, median views 69
- Real Estate/Housing: 3 videos, median views 163
- History/Explainers: 2 videos, median views 114
- Debt/Banking: 1 videos, median views 97
- Inflation/Recession/Macro: 1 videos, median views 104
- Duration bins: {'15-30m': 99, '>30m': 1}

## 5. Publishing Pattern
- Date range: 2025-11-05 → 2026-04-16 (163 days); uploads/week ≈ 4.29
- Days between upload dates: median=1, mean=1.6, max=5; consistency (CV of gaps)=0.57
- Weekday counts: {'Sat': 16, 'Mon': 16, 'Tue': 13, 'Thu': 15, 'Wed': 18, 'Fri': 13, 'Sun': 9}
- Upload hour (UTC, only where timestamp exists, n=100): {10: 91, 11: 3, 12: 1, 13: 3, 14: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2025-11: 12, 158, 0.17
  - 2025-12: 24, 1916, 3.55
  - 2026-01: 22, 173, 0.60
  - 2026-02: 23, 88, 0.44
  - 2026-03: 14, 94, 0.87
  - 2026-04: 5, 112, 2.11
- Quarterly:
  - 2025-Q4: 36, 883, 1.84
  - 2026-Q1: 59, 148, 0.64
  - 2026-Q2: 5, 112, 2.11

## 6. Performance Classification
- All: {'Breakout': 9, 'Underperforming': 30, 'Average': 32, 'Successful': 29}
- Shorts: {}  Long-form: {'Breakout': 9, 'Underperforming': 30, 'Average': 32, 'Successful': 29}
- Top 5 by age-adjusted ratio:
  - -3NN2NecYS0 "How the Rich Stay Rich: The 5 Buying Strategies You Never Learned" views=34787 age=345d ratio=49.26 [LONG]
  - RVOk9zxRzKQ "7 Hidden Signs You’re Winning With Money (Even If It Doesn’t Feel Like" views=28670 age=337d ratio=46.28 [LONG]
  - TXdlI6Iu8C4 "What No One Tells You About Life After Your First $1,000,000 Invested " views=19219 age=340d ratio=29.53 [LONG]
  - hndpIPOZmmU "At What Age Most Americans Hit $100K, $500K & $1M | Investing 101" views=9104 age=327d ratio=17.39 [LONG]
  - hOzaTMoRXhM "Stop Saving Like An American, Start The Japanese Way| Personal Finance" views=1336 age=235d ratio=15.99 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/118 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification