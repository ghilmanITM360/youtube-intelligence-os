# Ivan Invests
Channel id `UCDokTQePVxNZUqmzevDM7NQ` · niche FINANCE · subs 29900 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=1383861 | mean=13838.6 | median=7127.5 | max=195696 | min=202 | p10=1667 | p25=3033 | p75=9276 | p90=18688 | p99=186787 | cv=2.15

## 2. Performance Distribution
- All: p10=1667 p25=3033 median=7127.5 p75=9276 p90=18688 p99=186787 CV=2.15
- Mean/median ratio: 1.94 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=1383861 | mean=13838.6 | median=7127.5 | max=195696 | min=202 | p10=1667 | p25=3033 | p75=9276 | p90=18688 | p99=186787 | cv=2.15

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 62 videos, median views 7408
- Other/Unclassified: 15 videos, median views 7740
- Stocks/Investing: 9 videos, median views 6014
- History/Explainers: 6 videos, median views 3858
- Debt/Banking: 3 videos, median views 7058
- Real Estate/Housing: 2 videos, median views 3576
- Business/Companies: 1 videos, median views 15932
- Geopolitics/Trade: 1 videos, median views 2236
- Inflation/Recession/Macro: 1 videos, median views 690
- Duration bins: {'15-30m': 100}

## 5. Publishing Pattern
- Date range: 2026-07-11 → 2026-11-11 (124 days); uploads/week ≈ 5.65
- Days between upload dates: median=1, mean=1.2, max=3; consistency (CV of gaps)=0.38
- Weekday counts: {'Thu': 16, 'Fri': 17, 'Sun': 15, 'Wed': 16, 'Sat': 8, 'Tue': 10, 'Mon': 18}
- Upload hour (UTC, only where timestamp exists, n=100): {9: 1, 10: 1, 12: 90, 13: 8}
- Monthly (n, median views, age-adj median ratio):
  - 2026-07: 18, 2032, 0.29
  - 2026-08: 21, 2885, 0.40
  - 2026-09: 23, 7268, 1.02
  - 2026-10: 29, 8231, 1.15
  - 2026-11: 9, 6706, 0.94
- Quarterly:
  - 2026-Q3: 62, 5115, 0.72
  - 2026-Q4: 38, 8230, 1.15

## 6. Performance Classification
- All: {'Average': 55, 'Successful': 14, 'Underperforming': 25, 'Breakout': 6}
- Shorts: {}  Long-form: {'Average': 55, 'Successful': 14, 'Underperforming': 25, 'Breakout': 6}
- Top 5 by age-adjusted ratio:
  - Rz8_hmDacmI "16 Middle Class Purchases That Keep You Poor" views=195696 age=7d ratio=27.45 [LONG]
  - eOFlWP9yHak "17 Minimalist Money Rules That Make Going Broke Almost Impossible" views=186697 age=23d ratio=26.19 [LONG]
  - HSElgjgKPgQ "8 SIGNS You're Secretly Ahead Financially After 40 (Even If You Don't " views=91280 age=34d ratio=12.81 [LONG]
  - fgawdFwOZNY "At $250K, Compounding Gets Unstoppable!" views=86392 age=58d ratio=12.12 [LONG]
  - K6nAA7X7r5w "8 MORE Signs You're Secretly Getting Rich (That Nobody Talks About)" views=74233 age=51d ratio=10.41 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/490 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification