# Mr. Ranks
Channel id `UCGwJ94gUJNUWt-EW3zpWotA` · niche ECONOMICS · subs 31600 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 58 (Shorts 0, Long-form 58)
- Views (all): n=58 | total=3299318 | mean=56884.8 | median=13356.0 | max=399671 | min=1273 | p10=3687 | p25=7716 | p75=58651 | p90=177041 | p99=394218 | cv=1.58

## 2. Performance Distribution
- All: p10=3687 p25=7716 median=13356.0 p75=58651 p90=177041 p99=394218 CV=1.58
- Mean/median ratio: 4.26 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=58 | total=3299318 | mean=56884.8 | median=13356.0 | max=399671 | min=1273 | p10=3687 | p25=7716 | p75=58651 | p90=177041 | p99=394218 | cv=1.58

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 47 videos, median views 11964
- Crypto/Bitcoin: 4 videos, median views 84970
- Geopolitics/Trade: 2 videos, median views 40882
- Debt/Banking: 2 videos, median views 45148
- Real Estate/Housing: 1 videos, median views 78656
- Business/Companies: 1 videos, median views 116887
- Money/Personal Finance: 1 videos, median views 9864
- Duration bins: {'15-30m': 46, '>30m': 9, '8-15m': 3}

## 5. Publishing Pattern
- Date range: 2026-02-28 → 2026-11-09 (255 days); uploads/week ≈ 1.59
- Days between upload dates: median=4, mean=4.5, max=15; consistency (CV of gaps)=0.7
- Weekday counts: {'Sat': 11, 'Fri': 8, 'Mon': 8, 'Sun': 8, 'Tue': 8, 'Wed': 7, 'Thu': 8}
- Upload hour (UTC, only where timestamp exists, n=58): {0: 14, 1: 3, 2: 3, 3: 2, 4: 1, 8: 2, 10: 1, 11: 1, 12: 2, 13: 2, 14: 1, 15: 5, 16: 3, 17: 5, 18: 2, 19: 2, 22: 1, 23: 8}
- Monthly (n, median views, age-adj median ratio):
  - 2026-02: 1, 399671, 19.84
  - 2026-03: 13, 9989, 0.50
  - 2026-04: 11, 11964, 0.60
  - 2026-05: 7, 3619, 0.18
  - 2026-06: 2, 5270, 0.26
  - 2026-07: 4, 30506, 1.53
  - 2026-08: 4, 64982, 3.27
  - 2026-09: 6, 14704, 0.74
  - 2026-10: 6, 21343, 1.09
  - 2026-11: 4, 10612, 0.55
- Quarterly:
  - 2026-Q1: 14, 22532, 1.12
  - 2026-Q2: 20, 8364, 0.42
  - 2026-Q3: 14, 30506, 1.53
  - 2026-Q4: 10, 14300, 0.73

## 6. Performance Classification
- All: {'Average': 20, 'Breakout': 9, 'Successful': 12, 'Underperforming': 17}
- Shorts: {}  Long-form: {'Average': 20, 'Breakout': 9, 'Successful': 12, 'Underperforming': 17}
- Top 5 by age-adjusted ratio:
  - 6gSG4msCOz4 "Your Life as Every Dark Web Rank" views=399671 age=256d ratio=19.84 [LONG]
  - PmEsq-6eGEk "Your Life as an Airport Owner" views=390105 age=113d ratio=19.56 [LONG]
  - oFKjAJrLims "POV: You're a Crypto Miner Who Starts With One GPU" views=267459 age=222d ratio=13.30 [LONG]
  - cp2NBWVzRtk "Your Life as a Nightclub Owner" views=214484 age=43d ratio=10.87 [LONG]
  - 9zLJHTsmtk0 "Your Life as a Casino Owner" views=207978 age=48d ratio=10.53 [LONG]

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