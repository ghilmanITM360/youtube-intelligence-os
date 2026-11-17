# Carl Invests
Channel id `UCxoC2voi0vPg2hwqgfjdhYw` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 80 (Shorts 0, Long-form 80)
- Views (all): n=80 | total=621625 | mean=7770.3 | median=1696.5 | max=125946 | min=87 | p10=255 | p25=531 | p75=5231 | p90=18635 | p99=91173 | cv=2.34

## 2. Performance Distribution
- All: p10=255 p25=531 median=1696.5 p75=5231 p90=18635 p99=91173 CV=2.34
- Mean/median ratio: 4.58 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=80 | total=621625 | mean=7770.3 | median=1696.5 | max=125946 | min=87 | p10=255 | p25=531 | p75=5231 | p90=18635 | p99=91173 | cv=2.34

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 44 videos, median views 1696
- Other/Unclassified: 16 videos, median views 1062
- Stocks/Investing: 8 videos, median views 7886
- History/Explainers: 7 videos, median views 2555
- Real Estate/Housing: 2 videos, median views 1133
- Debt/Banking: 1 videos, median views 5278
- Inflation/Recession/Macro: 1 videos, median views 112
- Business/Companies: 1 videos, median views 626
- Duration bins: {'15-30m': 76, '8-15m': 4}

## 5. Publishing Pattern
- Date range: 2026-02-14 → 2026-09-09 (208 days); uploads/week ≈ 2.69
- Days between upload dates: median=2, mean=2.6, max=42; consistency (CV of gaps)=2.01
- Weekday counts: {'Tue': 10, 'Wed': 13, 'Thu': 10, 'Mon': 17, 'Sat': 12, 'Fri': 11, 'Sun': 7}
- Upload hour (UTC, only where timestamp exists, n=80): {0: 1, 10: 11, 11: 4, 12: 13, 13: 5, 14: 1, 15: 7, 16: 18, 17: 13, 18: 2, 20: 1, 22: 2, 23: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-02: 1, 551, 0.26
  - 2026-03: 3, 2256, 1.10
  - 2026-04: 19, 3249, 1.61
  - 2026-05: 17, 1437, 0.72
  - 2026-06: 16, 2276, 1.19
  - 2026-07: 7, 472, 0.25
  - 2026-08: 13, 462, 0.26
  - 2026-09: 4, 19534, 11.53
- Quarterly:
  - 2026-Q1: 4, 1650, 0.81
  - 2026-Q2: 52, 2346, 1.17
  - 2026-Q3: 24, 604, 0.32

## 6. Performance Classification
- All: {'Underperforming': 27, 'Successful': 18, 'Average': 23, 'Breakout': 12}
- Shorts: {}  Long-form: {'Underperforming': 27, 'Successful': 18, 'Average': 23, 'Breakout': 12}
- Top 5 by age-adjusted ratio:
  - -HeOz5CF9ys "9 Signs Someone is Secretly Wealthy" views=125946 age=216d ratio=62.06 [LONG]
  - w7Xu8O5TNHQ "What Actually Happens When You Invest $1,000 a Month" views=81930 age=67d ratio=48.01 [LONG]
  - 7sbA9WZrfHk "What Happens If You Invest $100 Every Month (Most People Don't Realize" views=49117 age=85d ratio=27.81 [LONG]
  - TDEme_uxx4c "What Actually Happens When You Invest $500 a Month" views=37612 age=76d ratio=21.65 [LONG]
  - eZ-SNfBH-6s "How To Be A Millionaire On A Low Salary" views=33339 age=208d ratio=16.52 [LONG]

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