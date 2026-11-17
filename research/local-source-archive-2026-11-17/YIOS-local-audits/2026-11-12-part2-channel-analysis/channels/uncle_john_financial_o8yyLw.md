# Uncle John Financial
Channel id `UCWugleQL2wqr5N1X4o8yyLw` · niche FINANCE · subs 47600 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 57 (Shorts 5, Long-form 52)
- Views (all): n=57 | total=4578511 | mean=80324.8 | median=10754 | max=631759 | min=365 | p10=1842 | p25=4483 | p75=100816 | p90=221640 | p99=524210 | cv=1.67

## 2. Performance Distribution
- All: p10=1842 p25=4483 median=10754 p75=100816 p90=221640 p99=524210 CV=1.67
- Mean/median ratio: 7.47 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=5 | total=3477 | mean=695.4 | median=534 | max=1453 | min=365 | p10=393 | p25=436 | p75=689 | p90=1147 | p99=1422 | cv=0.57
- Long-form: n=52 | total=4575034 | mean=87981.4 | median=13722.5 | max=631759 | min=1582 | p10=3259 | p25=5776 | p75=125209 | p90=243456 | p99=533812 | cv=1.57

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 31 videos, median views 10754
- Other/Unclassified: 15 videos, median views 4970
- History/Explainers: 7 videos, median views 54593
- Inflation/Recession/Macro: 2 videos, median views 173892
- Debt/Banking: 1 videos, median views 1582
- Stocks/Investing: 1 videos, median views 8840
- Duration bins: {'15-30m': 31, '8-15m': 19, '<=60s': 4, '>30m': 1, '3-8m': 1, '1-3m': 1}

## 5. Publishing Pattern
- Date range: 2026-01-16 → 2026-11-09 (298 days); uploads/week ≈ 1.34
- Days between upload dates: median=5.0, mean=5.5, max=13; consistency (CV of gaps)=0.53
- Weekday counts: {'Tue': 4, 'Sat': 10, 'Wed': 11, 'Sun': 10, 'Mon': 8, 'Thu': 6, 'Fri': 8}
- Upload hour (UTC, only where timestamp exists, n=57): {0: 2, 2: 1, 3: 3, 4: 1, 5: 3, 8: 2, 10: 1, 11: 2, 12: 2, 15: 1, 18: 1, 19: 1, 20: 28, 21: 4, 22: 4, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-01: 4, 2294, 0.23
  - 2026-02: 3, 54593, 1.11
  - 2026-03: 6, 37346, 0.85
  - 2026-04: 6, 35130, 0.86
  - 2026-05: 4, 11268, 0.32
  - 2026-06: 6, 87256, 4.01
  - 2026-07: 4, 117956, 4.93
  - 2026-08: 6, 174318, 7.94
  - 2026-09: 7, 8255, 0.48
  - 2026-10: 9, 3222, 0.65
  - 2026-11: 2, 2610, 0.71
- Quarterly:
  - 2026-Q1: 13, 21518, 0.60
  - 2026-Q2: 16, 24622, 0.86
  - 2026-Q3: 17, 49467, 2.68
  - 2026-Q4: 11, 3222, 0.65

## 6. Performance Classification
- All: {'Successful': 13, 'Underperforming': 19, 'Breakout': 7, 'Average': 18}
- Shorts: {'Successful': 1, 'Average': 4}  Long-form: {'Successful': 12, 'Underperforming': 19, 'Breakout': 7, 'Average': 14}
- Top 5 by age-adjusted ratio:
  - qjeLnPoGZ24 "What a Paid-Off Home Is Actually Worth in Retirement" views=439707 age=89d ratio=21.31 [LONG]
  - m-UIaaTzuvg "401(k), Social Security or Pension: How Claiming Order Affects Tax" views=631759 age=146d ratio=20.80 [LONG]
  - CaCQ0kPqv7Q "What the J.P. Morgan Retiree Spending Study Actually Found" views=360721 age=84d ratio=18.27 [LONG]
  - pMWONU01RO0 "The Five Years Before Retirement: A Planning Checklist" views=247819 age=98d ratio=11.15 [LONG]
  - jABYsMEoW20 "What Changes at Age 59½: Retirement Withdrawal Rules" views=398682 age=213d ratio=9.71 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- coverage 57/60 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification