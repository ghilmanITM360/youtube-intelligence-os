# Kevin Explains
Channel id `UCMl8WtFdqfnzzKcC2KWZZnQ` · niche FINANCE · subs 122000 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=10020676 | mean=100206.8 | median=28244.5 | max=695683 | min=326 | p10=2978 | p25=6982 | p75=101918 | p90=388969 | p99=652264 | cv=1.6

## 2. Performance Distribution
- All: p10=2978 p25=6982 median=28244.5 p75=101918 p90=388969 p99=652264 CV=1.6
- Mean/median ratio: 3.55 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=10020676 | mean=100206.8 | median=28244.5 | max=695683 | min=326 | p10=2978 | p25=6982 | p75=101918 | p90=388969 | p99=652264 | cv=1.6

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 55 videos, median views 39271
- Debt/Banking: 17 videos, median views 24563
- Money/Personal Finance: 13 videos, median views 23898
- Geopolitics/Trade: 7 videos, median views 11730
- Real Estate/Housing: 4 videos, median views 7711
- History/Explainers: 2 videos, median views 20300
- Stocks/Investing: 1 videos, median views 3287
- Business/Companies: 1 videos, median views 118489
- Duration bins: {'15-30m': 72, '>30m': 28}

## 5. Publishing Pattern
- Date range: 2026-06-11 → 2026-11-09 (152 days); uploads/week ≈ 4.61
- Days between upload dates: median=1.0, mean=2.0, max=11; consistency (CV of gaps)=0.95
- Weekday counts: {'Sun': 17, 'Sat': 15, 'Mon': 17, 'Wed': 16, 'Fri': 17, 'Tue': 6, 'Thu': 12}
- Upload hour (UTC, only where timestamp exists, n=100): {5: 1, 7: 6, 8: 14, 9: 6, 10: 6, 11: 8, 12: 8, 13: 16, 14: 8, 15: 6, 16: 7, 17: 8, 18: 4, 19: 1, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 3, 37708, 1.02
  - 2026-07: 13, 8393, 0.25
  - 2026-08: 28, 39930, 1.30
  - 2026-09: 17, 60501, 2.33
  - 2026-10: 27, 31926, 1.47
  - 2026-11: 12, 8292, 0.53
- Quarterly:
  - 2026-Q2: 3, 37708, 1.02
  - 2026-Q3: 58, 42154, 1.37
  - 2026-Q4: 39, 15295, 0.76

## 6. Performance Classification
- All: {'Average': 23, 'Successful': 28, 'Underperforming': 33, 'Breakout': 16}
- Shorts: {}  Long-form: {'Average': 23, 'Successful': 28, 'Underperforming': 33, 'Breakout': 16}
- Top 5 by age-adjusted ratio:
  - G8Ks2zHPLD8 "BANKS ARE NOW FLAGGING SOCIAL SECURITY DIRECT DEPOSITS: Check Yours Be" views=651825 age=12d ratio=34.37 [LONG]
  - cEMxNQZ2tP0 "Born Before 1967? 4 Social Security Changes Hitting Your Birth Year In" views=695683 age=32d ratio=29.06 [LONG]
  - XOC514hXq70 "Every Senior Must Open This Before September 30 Or Pay All Year" views=546105 age=64d ratio=18.79 [LONG]
  - oWAgG7uSlIc "6 Places Seniors Should Never Keep Their Cash Before Nov 1" views=519014 age=56d ratio=18.56 [LONG]
  - FBT55AI0kvo "Good News for US Seniors: 3 Checks You Didn't Know You Qualify For" views=559346 age=98d ratio=16.95 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/166 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification