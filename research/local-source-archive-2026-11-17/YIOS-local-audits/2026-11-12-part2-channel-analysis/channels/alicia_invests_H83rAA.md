# Alicia Invests
Channel id `UCFPfloFwa6X2UddqRH83rAA` · niche FINANCE · subs 105000 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=1660674 | mean=16606.7 | median=10584.5 | max=229969 | min=1996 | p10=5362 | p25=7178 | p75=16476 | p90=27242 | p99=101683 | cv=1.54

## 2. Performance Distribution
- All: p10=5362 p25=7178 median=10584.5 p75=16476 p90=27242 p99=101683 CV=1.54
- Mean/median ratio: 1.57 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=1660674 | mean=16606.7 | median=10584.5 | max=229969 | min=1996 | p10=5362 | p25=7178 | p75=16476 | p90=27242 | p99=101683 | cv=1.54

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 75 videos, median views 10214
- Other/Unclassified: 15 videos, median views 16579
- Real Estate/Housing: 4 videos, median views 6406
- Debt/Banking: 3 videos, median views 3362
- History/Explainers: 2 videos, median views 21590
- Stocks/Investing: 1 videos, median views 12168
- Duration bins: {'15-30m': 98, '>30m': 2}

## 5. Publishing Pattern
- Date range: 2026-07-23 → 2026-11-03 (104 days); uploads/week ≈ 6.73
- Days between upload dates: median=1, mean=1.0, max=3; consistency (CV of gaps)=0.23
- Weekday counts: {'Mon': 15, 'Fri': 15, 'Thu': 15, 'Tue': 13, 'Wed': 13, 'Sat': 14, 'Sun': 15}
- Upload hour (UTC, only where timestamp exists, n=100): {10: 1, 11: 90, 12: 2, 13: 2, 14: 2, 15: 1, 16: 1, 17: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-07: 9, 8683, 0.82
  - 2026-08: 31, 7626, 0.72
  - 2026-09: 29, 13433, 1.27
  - 2026-10: 28, 12250, 1.16
  - 2026-11: 3, 7559, 0.71
- Quarterly:
  - 2026-Q3: 69, 9190, 0.87
  - 2026-Q4: 31, 11338, 1.07

## 6. Performance Classification
- All: {'Average': 68, 'Underperforming': 5, 'Successful': 25, 'Breakout': 2}
- Shorts: {}  Long-form: {'Average': 68, 'Underperforming': 5, 'Successful': 25, 'Breakout': 2}
- Top 5 by age-adjusted ratio:
  - ylv5PYLrMVM "12 Free Upgrades That Make Life Feel Expensive" views=229969 age=79d ratio=21.73 [LONG]
  - BFQb7NJeLEc "How I Built a Full Year of Emergency Savings on a $30,000 Salary (The " views=100387 age=96d ratio=9.48 [LONG]
  - foiSbDDMqQU "10 Things Wealthy People Notice That Everyone Else Misses" views=67162 age=50d ratio=6.34 [LONG]
  - FckxFw8Kt_E "20 Old-School "Poor Man's Habits" That Still Save $2,000 a Month" views=58228 age=70d ratio=5.50 [LONG]
  - cUf5-5BnIug "10 Signs Someone Has Real Money (Not Just a Big Salary)" views=46257 age=97d ratio=4.37 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/275 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification