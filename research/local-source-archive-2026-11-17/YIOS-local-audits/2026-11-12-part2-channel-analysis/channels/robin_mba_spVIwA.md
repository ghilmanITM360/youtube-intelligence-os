# Robin MBA
Channel id `UCOvq-1piPnzCmrqfSspVIwA` · niche FINANCE · subs 10800 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 56 (Shorts 0, Long-form 56)
- Views (all): n=56 | total=2023735 | mean=36138.1 | median=1801.5 | max=569470 | min=135 | p10=354 | p25=674 | p75=6257 | p90=119166 | p99=447692 | cv=2.75

## 2. Performance Distribution
- All: p10=354 p25=674 median=1801.5 p75=6257 p90=119166 p99=447692 CV=2.75
- Mean/median ratio: 20.06 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=56 | total=2023735 | mean=36138.1 | median=1801.5 | max=569470 | min=135 | p10=354 | p25=674 | p75=6257 | p90=119166 | p99=447692 | cv=2.75

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 36 videos, median views 2100
- Money/Personal Finance: 5 videos, median views 691
- Debt/Banking: 5 videos, median views 2219
- Real Estate/Housing: 5 videos, median views 438
- History/Explainers: 2 videos, median views 286
- Stocks/Investing: 1 videos, median views 172
- Business/Companies: 1 videos, median views 4618
- Inflation/Recession/Macro: 1 videos, median views 2126
- Duration bins: {'15-30m': 17, '8-15m': 35, '3-8m': 4}

## 5. Publishing Pattern
- Date range: 2026-06-30 → 2026-10-16 (109 days); uploads/week ≈ 3.6
- Days between upload dates: median=1, mean=2.0, max=14; consistency (CV of gaps)=1.11
- Weekday counts: {'Wed': 7, 'Tue': 9, 'Fri': 8, 'Sun': 5, 'Thu': 12, 'Sat': 9, 'Mon': 6}
- Upload hour (UTC, only where timestamp exists, n=56): {12: 4, 13: 9, 14: 9, 15: 17, 16: 9, 17: 6, 18: 1, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 1, 115119, 63.87
  - 2026-07: 16, 1540, 0.85
  - 2026-08: 8, 404, 0.22
  - 2026-09: 18, 2015, 1.12
  - 2026-10: 13, 4618, 2.56
- Quarterly:
  - 2026-Q2: 1, 115119, 63.87
  - 2026-Q3: 42, 1372, 0.76
  - 2026-Q4: 13, 4618, 2.56

## 6. Performance Classification
- All: {'Breakout': 11, 'Underperforming': 15, 'Average': 22, 'Successful': 8}
- Shorts: {}  Long-form: {'Breakout': 11, 'Underperforming': 15, 'Average': 22, 'Successful': 8}
- Top 5 by age-adjusted ratio:
  - A4hPtQsiWoA "If You're Over 60, Costco Owes You These 15 Free Things" views=569470 age=62d ratio=315.93 [LONG]
  - BfOcC1094eo "If You're Over 60, Aldi Will Give You These 14 Things (If You Ask)" views=348055 age=35d ratio=193.10 [LONG]
  - 0na9DiXBEK8 "Never Keep This Much Money in One Bank Account — and the Innocent Mist" views=269948 age=125d ratio=149.76 [LONG]
  - Qjbv7iuTk5A "New Food Assistance Rules for Seniors Starting This October 1 (One Era" views=234031 age=47d ratio=129.84 [LONG]
  - C3EThjSb9e4 "Free Food Benefits Start at Age 60 (Not 65) — Many Seniors Never Claim" views=144630 age=37d ratio=80.24 [LONG]

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