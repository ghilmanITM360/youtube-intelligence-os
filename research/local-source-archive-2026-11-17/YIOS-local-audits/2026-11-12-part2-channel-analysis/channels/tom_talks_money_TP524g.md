# Tom Talks Money
Channel id `UCKqgbX0MOmE5ZzyFpTP524g` · niche FINANCE · subs 67700 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=264454 | mean=2644.5 | median=1798.5 | max=37409 | min=452 | p10=766 | p25=1050 | p75=2835 | p90=4382 | p99=11715 | cv=1.5

## 2. Performance Distribution
- All: p10=766 p25=1050 median=1798.5 p75=2835 p90=4382 p99=11715 CV=1.5
- Mean/median ratio: 1.47 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=264454 | mean=2644.5 | median=1798.5 | max=37409 | min=452 | p10=766 | p25=1050 | p75=2835 | p90=4382 | p99=11715 | cv=1.5

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 26 videos, median views 2246
- Money/Personal Finance: 23 videos, median views 1529
- History/Explainers: 15 videos, median views 1829
- Debt/Banking: 15 videos, median views 1322
- Stocks/Investing: 12 videos, median views 3548
- Inflation/Recession/Macro: 5 videos, median views 815
- Real Estate/Housing: 2 videos, median views 2494
- Geopolitics/Trade: 2 videos, median views 1726
- Duration bins: {'15-30m': 92, '>30m': 8}

## 5. Publishing Pattern
- Date range: 2026-03-21 → 2026-10-02 (196 days); uploads/week ≈ 3.57
- Days between upload dates: median=2, mean=2.0, max=7; consistency (CV of gaps)=0.66
- Weekday counts: {'Wed': 24, 'Mon': 22, 'Tue': 6, 'Sat': 7, 'Fri': 28, 'Thu': 6, 'Sun': 7}
- Upload hour (UTC, only where timestamp exists, n=100): {12: 91, 13: 9}
- Monthly (n, median views, age-adj median ratio):
  - 2026-03: 10, 4020, 2.03
  - 2026-04: 30, 1933, 0.99
  - 2026-05: 15, 1368, 0.72
  - 2026-06: 13, 1377, 0.74
  - 2026-07: 14, 1804, 1.02
  - 2026-08: 12, 971, 0.59
  - 2026-09: 5, 4159, 2.66
  - 2026-10: 1, 2109, 1.44
- Quarterly:
  - 2026-Q1: 10, 4020, 2.03
  - 2026-Q2: 58, 1520, 0.78
  - 2026-Q3: 31, 1858, 1.06
  - 2026-Q4: 1, 2109, 1.44

## 6. Performance Classification
- All: {'Average': 62, 'Underperforming': 9, 'Successful': 28, 'Breakout': 1}
- Shorts: {}  Long-form: {'Average': 62, 'Underperforming': 9, 'Successful': 28, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - H57itChL8J8 "When the S&P 500 Went Nowhere for 10 Straight Years" views=37409 age=229d ratio=18.86 [LONG]
  - EHYy06BVNdI "Stop Owning 20 ETFs Now to Build Wealth Faster Explained" views=11455 age=205d ratio=5.89 [LONG]
  - 9AxFQXSAjuU "Corporate Careers Aren't About IQ - They're About This" views=11234 age=223d ratio=5.69 [LONG]
  - rey2QzdJ_kw "Don't Accept That Credit Limit Increase Until You Watch This" views=7067 age=70d ratio=4.41 [LONG]
  - Eqb1Jm12PH4 "The Subscription Math They Don't Want You To Know" views=5925 age=75d ratio=3.65 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/218 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification