# Nick Invests
Channel id `UCXzNNA2ngRpRiWvyA7eGd6w` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=9561625 | mean=95616.2 | median=6382.5 | max=1098276 | min=2646 | p10=4004 | p25=4544 | p75=142628 | p90=300015 | p99=653546 | cv=1.87

## 2. Performance Distribution
- All: p10=4004 p25=4544 median=6382.5 p75=142628 p90=300015 p99=653546 CV=1.87
- Mean/median ratio: 14.98 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=9561625 | mean=95616.2 | median=6382.5 | max=1098276 | min=2646 | p10=4004 | p25=4544 | p75=142628 | p90=300015 | p99=653546 | cv=1.87

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 46 videos, median views 9438
- Other/Unclassified: 20 videos, median views 5279
- Stocks/Investing: 14 videos, median views 6299
- Real Estate/Housing: 7 videos, median views 5207
- Debt/Banking: 6 videos, median views 5736
- History/Explainers: 4 videos, median views 79902
- Inflation/Recession/Macro: 2 videos, median views 4256
- Crypto/Bitcoin: 1 videos, median views 6234
- Duration bins: {'15-30m': 90, '>30m': 10}

## 5. Publishing Pattern
- Date range: 2025-08-14 → 2026-09-10 (393 days); uploads/week ≈ 1.75
- Days between upload dates: median=1, mean=4.0, max=47; consistency (CV of gaps)=1.68
- Weekday counts: {'Tue': 15, 'Fri': 14, 'Wed': 16, 'Thu': 13, 'Mon': 12, 'Sun': 13, 'Sat': 15}
- Upload hour (UTC, only where timestamp exists, n=98): {1: 1, 9: 3, 10: 21, 11: 2, 14: 1, 20: 43, 21: 19, 22: 8}
- Monthly (n, median views, age-adj median ratio):
  - 2025-08: 3, 167634, 0.71
  - 2025-09: 3, 649054, 3.11
  - 2025-10: 10, 236036, 1.40
  - 2025-11: 6, 193456, 1.37
  - 2025-12: 2, 179470, 1.47
  - 2026-01: 3, 152384, 1.85
  - 2026-03: 2, 149358, 2.78
  - 2026-04: 3, 5344, 0.13
  - 2026-05: 3, 4459, 0.18
  - 2026-06: 6, 4606, 0.30
  - 2026-07: 20, 4809, 0.54
  - 2026-08: 30, 4862, 0.98
  - 2026-09: 7, 10609, 3.87
- Quarterly:
  - 2025-Q3: 6, 316692, 1.41
  - 2025-Q4: 18, 197733, 1.37
  - 2026-Q1: 5, 152384, 1.85
  - 2026-Q2: 12, 4613, 0.25
  - 2026-Q3: 57, 5025, 0.89

## 6. Performance Classification
- All: {'Average': 51, 'Underperforming': 18, 'Successful': 27, 'Breakout': 4}
- Shorts: {}  Long-form: {'Average': 51, 'Underperforming': 18, 'Successful': 27, 'Breakout': 4}
- Top 5 by age-adjusted ratio:
  - 15Gr4BAJi00 "Major MONEY Milestones To Accomplish In Your 30S" views=255936 age=Noned ratio=40.09 [LONG]
  - n5q80b8R8Tc "The 6 Wealth Levels Where Compounding Gets Insane" views=49925 age=65d ratio=18.86 [LONG]
  - KrvtiC-Jaz0 "Let's Watch What Happens to People AFTER They Hit $100,000" views=30597 age=75d ratio=8.41 [LONG]
  - f6HIYQUiMoU "WTF Just Happened To The Housing Market?!" views=361243 age=222d ratio=8.07 [LONG]
  - 1mIp0mUyCKU "Who Can Actually Afford a $500K House in 2026 (The Math Is Brutal)" views=529356 age=301d ratio=5.73 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- 2 videos lack publish date (excluded from time/age analysis)
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification