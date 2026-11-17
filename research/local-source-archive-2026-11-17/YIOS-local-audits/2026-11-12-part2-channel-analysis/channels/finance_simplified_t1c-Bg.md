# Finance Simplified
Channel id `UCogYxvdGc8i7qfjPct1c-Bg` · niche FINANCE · subs 3690 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=698769 | mean=6987.7 | median=536.0 | max=205350 | min=5 | p10=27 | p25=100 | p75=4862 | p90=14543 | p99=129666 | cv=3.5

## 2. Performance Distribution
- All: p10=27 p25=100 median=536.0 p75=4862 p90=14543 p99=129666 CV=3.5
- Mean/median ratio: 13.04 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=698769 | mean=6987.7 | median=536.0 | max=205350 | min=5 | p10=27 | p25=100 | p75=4862 | p90=14543 | p99=129666 | cv=3.5

## 4. Topic Distribution (heuristic)
- Stocks/Investing: 45 videos, median views 1830
- Money/Personal Finance: 23 videos, median views 105
- Other/Unclassified: 10 videos, median views 64
- Geopolitics/Trade: 6 videos, median views 792
- Debt/Banking: 5 videos, median views 388
- Real Estate/Housing: 4 videos, median views 632
- History/Explainers: 3 videos, median views 133
- Inflation/Recession/Macro: 2 videos, median views 29096
- Crypto/Bitcoin: 2 videos, median views 936
- Duration bins: {'15-30m': 87, '8-15m': 12, '3-8m': 1}

## 5. Publishing Pattern
- Date range: 2026-03-30 → 2026-11-11 (227 days); uploads/week ≈ 3.08
- Days between upload dates: median=2, mean=2.3, max=15; consistency (CV of gaps)=0.84
- Weekday counts: {'Fri': 16, 'Sun': 15, 'Tue': 18, 'Sat': 13, 'Mon': 10, 'Wed': 15, 'Thu': 13}
- Upload hour (UTC, only where timestamp exists, n=100): {0: 1, 2: 1, 4: 2, 5: 1, 9: 3, 10: 2, 11: 5, 12: 10, 13: 8, 14: 18, 15: 9, 16: 11, 17: 8, 18: 12, 19: 5, 21: 1, 22: 3}
- Monthly (n, median views, age-adj median ratio):
  - 2026-03: 1, 133, 0.25
  - 2026-04: 9, 27, 0.05
  - 2026-05: 10, 58, 0.11
  - 2026-06: 7, 46, 0.09
  - 2026-07: 6, 145, 0.27
  - 2026-08: 14, 603, 1.12
  - 2026-09: 20, 10028, 18.68
  - 2026-10: 26, 1157, 2.16
  - 2026-11: 7, 352, 0.66
- Quarterly:
  - 2026-Q1: 1, 133, 0.25
  - 2026-Q2: 26, 42, 0.08
  - 2026-Q3: 40, 3496, 6.51
  - 2026-Q4: 33, 1043, 1.94

## 6. Performance Classification
- All: {'Average': 27, 'Breakout': 29, 'Underperforming': 31, 'Successful': 13}
- Shorts: {}  Long-form: {'Average': 27, 'Breakout': 29, 'Underperforming': 31, 'Successful': 13}
- Top 5 by age-adjusted ratio:
  - 4bg3bjvjCjE "Dividend Stocks vs. Growth Stocks: The Math Most Investors Ignore" views=205350 age=72d ratio=382.40 [LONG]
  - hkRXzD3CH3c "Stop Guessing! Growth vs Dividend Stocks Explained in 20 Minutes" views=128902 age=110d ratio=240.04 [LONG]
  - EFAlmTE_5Ug "The Fed Just Raised Rates — Where Should You Put $100,000 Now?" views=40519 age=52d ratio=75.46 [LONG]
  - Jedd-rsUdDU "S&P 500 vs. High-Dividend Portfolio: What 20 Years of Data Actually Pr" views=29278 age=62d ratio=54.52 [LONG]
  - 5v38Uvy57Cw "Bond Yields Are Surging Again — The Math Just Changed for Everyone" views=19875 age=70d ratio=37.01 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/108 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification