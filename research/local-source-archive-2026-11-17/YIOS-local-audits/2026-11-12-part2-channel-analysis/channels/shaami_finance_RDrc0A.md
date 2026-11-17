# Shaami Finance
Channel id `UC5ZSqmk7PKry99xdiRDrc0A` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 13 (Shorts 0, Long-form 13)
- Views (all): n=13 | total=461081 | mean=35467.8 | median=6176 | max=253898 | min=746 | p10=2757 | p25=3529 | p75=25212 | p90=88025 | p99=235486 | cv=1.92

## 2. Performance Distribution
- All: p10=2757 p25=3529 median=6176 p75=25212 p90=88025 p99=235486 CV=1.92
- Mean/median ratio: 5.74 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=13 | total=461081 | mean=35467.8 | median=6176 | max=253898 | min=746 | p10=2757 | p25=3529 | p75=25212 | p90=88025 | p99=235486 | cv=1.92

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 4 videos, median views 15310
- Real Estate/Housing: 3 videos, median views 6176
- History/Explainers: 2 videos, median views 132424
- Other/Unclassified: 1 videos, median views 6992
- Debt/Banking: 1 videos, median views 746
- Stocks/Investing: 1 videos, median views 3529
- Business/Companies: 1 videos, median views 3249
- Duration bins: {'8-15m': 3, '15-30m': 7, '>30m': 3}

## 5. Publishing Pattern
- Date range: 2026-06-18 → 2026-09-09 (84 days); uploads/week ≈ 1.08
- Days between upload dates: median=7.0, mean=6.9, max=15; consistency (CV of gaps)=0.46
- Weekday counts: {'Thu': 3, 'Wed': 5, 'Fri': 2, 'Sun': 2, 'Mon': 1}
- Upload hour (UTC, only where timestamp exists, n=13): {13: 13}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 3, 2634, 0.43
  - 2026-07: 3, 100463, 16.26
  - 2026-08: 5, 6992, 1.13
  - 2026-09: 2, 5792, 0.94
- Quarterly:
  - 2026-Q2: 3, 2634, 0.43
  - 2026-Q3: 10, 6584, 1.07

## 6. Performance Classification
- All: {'Average': 7, 'Successful': 3, 'Underperforming': 1, 'Breakout': 2}
- Shorts: {}  Long-form: {'Average': 7, 'Successful': 3, 'Underperforming': 1, 'Breakout': 2}
- Top 5 by age-adjusted ratio:
  - Oj5enLUpPyU "You Escaped The Rat Race & Nobody Noticed (Here's How)" views=253898 age=117d ratio=41.10 [LONG]
  - 4OO-DQjN_-g "You Have 560 Million Dollars. Nobody Knows.Your life as a Silent Milli" views=100463 age=125d ratio=16.26 [LONG]
  - fMEr9QkgxsQ "Never Tell Your Parents How Much Money You Have — Here's Why" views=38271 age=84d ratio=6.20 [LONG]
  - Mw3vUeUFHAs "Why The Richest People Look Completely Ordinary (A Millionaire's Confe" views=25212 age=89d ratio=4.08 [LONG]
  - A3D-Z5lONO4 "How to Become Financially Free in 5 Years — The Exact Plan" views=10950 age=143d ratio=1.77 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 13 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification