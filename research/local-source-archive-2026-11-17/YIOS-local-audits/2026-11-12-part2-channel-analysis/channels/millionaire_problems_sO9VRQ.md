# Millionaire Problems
Channel id `UCQnC6FoEgp4VcmbPTsO9VRQ` · niche ECONOMICS · subs 29100 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 9 (Shorts 0, Long-form 9)
- Views (all): n=9 | total=1562319 | mean=173591 | median=106963 | max=700164 | min=11583 | p10=17216 | p25=43539 | p75=198864 | p90=351233 | p99=665271 | cv=1.16

## 2. Performance Distribution
- All: p10=17216 p25=43539 median=106963 p75=198864 p90=351233 p99=665271 CV=1.16
- Mean/median ratio: 1.62 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=9 | total=1562319 | mean=173591 | median=106963 | max=700164 | min=11583 | p10=17216 | p25=43539 | p75=198864 | p90=351233 | p99=665271 | cv=1.16

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 9 videos, median views 106963
- Duration bins: {'15-30m': 4, '8-15m': 5}

## 5. Publishing Pattern
- Date range: 2026-04-21 → 2026-07-26 (97 days); uploads/week ≈ 0.65
- Days between upload dates: median=7.5, mean=12, max=38; consistency (CV of gaps)=0.88
- Weekday counts: {'Tue': 3, 'Mon': 3, 'Fri': 1, 'Thu': 1, 'Sun': 1}
- Upload hour (UTC, only where timestamp exists, n=9): {12: 1, 13: 1, 16: 1, 17: 2, 18: 2, 22: 1, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-04: 2, 231432, 2.16
  - 2026-05: 3, 123269, 1.15
  - 2026-06: 1, 106963, 1.00
  - 2026-07: 3, 18624, 0.17
- Quarterly:
  - 2026-Q2: 6, 161066, 1.51
  - 2026-Q3: 3, 18624, 0.17

## 6. Performance Classification
- All: {'Successful': 3, 'Underperforming': 3, 'Average': 3}
- Shorts: {}  Long-form: {'Successful': 3, 'Underperforming': 3, 'Average': 3}
- Top 5 by age-adjusted ratio:
  - HE5xgQS53gc "The Economics of Owning a Casino" views=700164 age=190d ratio=6.55 [LONG]
  - XiDvK1r2l_k "The Economics of Owning an Offshore Oil Rig" views=264000 age=204d ratio=2.47 [LONG]
  - CcyLLvUj5jY "The Economics of Owning a McDonald's Franchise" views=198864 age=198d ratio=1.86 [LONG]
  - TFiTzviGMAE "The Economics of Owning a Private Military Company" views=123269 age=184d ratio=1.15 [LONG]
  - RbBLk-l-xIc "The Economics of Owning a Bank" views=106963 age=139d ratio=1.00 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 9 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification