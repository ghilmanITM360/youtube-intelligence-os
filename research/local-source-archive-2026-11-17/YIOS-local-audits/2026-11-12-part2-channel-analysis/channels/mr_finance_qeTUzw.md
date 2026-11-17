# Mr. Finance
Channel id `UC6AwWrRKNrwt83CMJqeTUzw` · niche ECONOMICS · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 65 (Shorts 0, Long-form 65)
- Views (all): n=65 | total=2087298 | mean=32112.3 | median=16037 | max=265588 | min=401 | p10=2801 | p25=4288 | p75=45987 | p90=70983 | p99=204942 | cv=1.4

## 2. Performance Distribution
- All: p10=2801 p25=4288 median=16037 p75=45987 p90=70983 p99=204942 CV=1.4
- Mean/median ratio: 2.0 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=65 | total=2087298 | mean=32112.3 | median=16037 | max=265588 | min=401 | p10=2801 | p25=4288 | p75=45987 | p90=70983 | p99=204942 | cv=1.4

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 64 videos, median views 15749
- Stocks/Investing: 1 videos, median views 59794
- Duration bins: {'15-30m': 62, '>30m': 3}

## 5. Publishing Pattern
- Date range: 2026-06-28 → 2026-08-24 (58 days); uploads/week ≈ 7.48
- Days between upload dates: median=1.0, mean=1.2, max=4; consistency (CV of gaps)=0.48
- Weekday counts: {'Thu': 7, 'Mon': 9, 'Sat': 7, 'Fri': 10, 'Sun': 10, 'Tue': 9, 'Wed': 10}
- Upload hour (UTC, only where timestamp exists, n=62): {1: 1, 3: 2, 4: 1, 5: 5, 6: 7, 7: 7, 8: 1, 9: 3, 10: 3, 11: 3, 12: 6, 13: 2, 14: 3, 15: 1, 16: 3, 17: 6, 18: 4, 19: 3, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 3, 65170, 0.83
  - 2026-07: 35, 29886, 0.96
  - 2026-08: 24, 3730, 1.12
- Quarterly:
  - 2026-Q2: 3, 65170, 0.83
  - 2026-Q3: 59, 10115, 1.05

## 6. Performance Classification
- All: {'Successful': 22, 'Average': 33, 'Underperforming': 9, 'Breakout': 1}
- Shorts: {}  Long-form: {'Successful': 22, 'Average': 33, 'Underperforming': 9, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - 4nYkN0wTi2Q "The Economics of Owning a Gym" views=265588 age=121d ratio=7.93 [LONG]
  - yZrktmL624M "The Economics of Owning a Cafe" views=108250 age=Noned ratio=6.75 [LONG]
  - wDbackJX2hI "The Economics of Owning a Data Center" views=16415 age=92d ratio=3.57 [LONG]
  - yFF-415SyAA "The Economics of Owning a Cinema" views=56787 age=Noned ratio=3.54 [LONG]
  - n1DXp7Y3xA4 "The Economics of Owning a Ranch" views=170828 age=128d ratio=3.38 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- 3 videos lack publish date (excluded from time/age analysis)
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification