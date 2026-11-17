# Mark - Retired at 55
Channel id `UCegPlgZVNg0g1pAzZtGH4dw` · niche FINANCE · subs 14900 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=929606 | mean=9296.1 | median=5389.5 | max=103107 | min=733 | p10=1609 | p25=2654 | p75=10102 | p90=19815 | p99=66554 | cv=1.44

## 2. Performance Distribution
- All: p10=1609 p25=2654 median=5389.5 p75=10102 p90=19815 p99=66554 CV=1.44
- Mean/median ratio: 1.72 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=929606 | mean=9296.1 | median=5389.5 | max=103107 | min=733 | p10=1609 | p25=2654 | p75=10102 | p90=19815 | p99=66554 | cv=1.44

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 57 videos, median views 4883
- Other/Unclassified: 32 videos, median views 6659
- Stocks/Investing: 5 videos, median views 6992
- History/Explainers: 3 videos, median views 10962
- Inflation/Recession/Macro: 2 videos, median views 5955
- Debt/Banking: 1 videos, median views 6006
- Duration bins: {'15-30m': 61, '>30m': 39}

## 5. Publishing Pattern
- Date range: 2026-08-07 → 2026-11-10 (96 days); uploads/week ≈ 7.29
- Days between upload dates: median=1.0, mean=1.0, max=2; consistency (CV of gaps)=0.1
- Weekday counts: {'Mon': 15, 'Fri': 13, 'Sat': 16, 'Thu': 13, 'Wed': 13, 'Tue': 15, 'Sun': 15}
- Upload hour (UTC, only where timestamp exists, n=100): {4: 1, 11: 4, 14: 1, 15: 1, 16: 1, 21: 83, 22: 9}
- Monthly (n, median views, age-adj median ratio):
  - 2026-08: 29, 3792, 0.70
  - 2026-09: 30, 6601, 1.22
  - 2026-10: 31, 5770, 1.07
  - 2026-11: 10, 5586, 1.04
- Quarterly:
  - 2026-Q3: 59, 5106, 0.95
  - 2026-Q4: 41, 5770, 1.07

## 6. Performance Classification
- All: {'Average': 44, 'Underperforming': 24, 'Successful': 29, 'Breakout': 3}
- Shorts: {}  Long-form: {'Average': 44, 'Underperforming': 24, 'Successful': 29, 'Breakout': 3}
- Top 5 by age-adjusted ratio:
  - XdgondihYkk "The Net Worth Levels Where You Can Finally Quit Your Job After 50" views=103107 age=25d ratio=19.13 [LONG]
  - Mono7UYXBZA "Almost No One Retires With $1 Million—Here’s Why" views=66185 age=59d ratio=12.28 [LONG]
  - mToypbkGul8 "Why Everything Changes After You Reach $600,000" views=38902 age=19d ratio=7.22 [LONG]
  - TdXe2zRnTZs "Social Security at 62 vs 70: The Math Everyone Gets Wrong" views=31225 age=94d ratio=5.79 [LONG]
  - -8n61C7wRvA "The Number That Makes Work Optional at 50, 55, and 60" views=29851 age=77d ratio=5.54 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/385 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification