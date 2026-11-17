# The Expensive Part
Channel id `UCe2TLO3VWaMP8EthzGjSG6Q` · niche ECONOMICS · subs 4930 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 27 (Shorts 0, Long-form 27)
- Views (all): n=27 | total=285485 | mean=10573.5 | median=4847 | max=87845 | min=186 | p10=876 | p25=1470 | p75=10774 | p90=24111 | p99=74594 | cv=1.66

## 2. Performance Distribution
- All: p10=876 p25=1470 median=4847 p75=10774 p90=24111 p99=74594 CV=1.66
- Mean/median ratio: 2.18 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=27 | total=285485 | mean=10573.5 | median=4847 | max=87845 | min=186 | p10=876 | p25=1470 | p75=10774 | p90=24111 | p99=74594 | cv=1.66

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 21 videos, median views 6449
- Money/Personal Finance: 3 videos, median views 1543
- Other/Unclassified: 2 videos, median views 791
- Real Estate/Housing: 1 videos, median views 4847
- Duration bins: {'15-30m': 25, '8-15m': 2}

## 5. Publishing Pattern
- Date range: 2026-07-18 → 2026-11-10 (116 days); uploads/week ≈ 1.63
- Days between upload dates: median=1.0, mean=4.4, max=50; consistency (CV of gaps)=2.14
- Weekday counts: {'Sat': 6, 'Thu': 2, 'Wed': 5, 'Mon': 4, 'Fri': 3, 'Tue': 4, 'Sun': 3}
- Upload hour (UTC, only where timestamp exists, n=27): {4: 2, 8: 1, 10: 1, 11: 2, 12: 2, 13: 6, 14: 4, 16: 2, 17: 1, 18: 1, 19: 3, 20: 1, 21: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-07: 12, 12868, 2.00
  - 2026-08: 9, 2178, 0.36
  - 2026-09: 2, 1257, 0.31
  - 2026-10: 2, 1054, 1.10
  - 2026-11: 2, 2516, 3.98
- Quarterly:
  - 2026-Q3: 23, 6391, 0.95
  - 2026-Q4: 4, 1054, 1.10

## 6. Performance Classification
- All: {'Breakout': 2, 'Average': 10, 'Successful': 7, 'Underperforming': 8}
- Shorts: {}  Long-form: {'Breakout': 2, 'Average': 10, 'Successful': 7, 'Underperforming': 8}
- Top 5 by age-adjusted ratio:
  - tLFt7bOxa64 "The Economics of Owning a Medieval Tavern" views=87845 age=116d ratio=12.32 [LONG]
  - uFQ_yFkvYps "You Are The Owner of a Medieval Gatehouse" views=4847 age=9d ratio=7.32 [LONG]
  - zvMXV1rTV4M "The Economics of Owning a Medieval Blacksmith Shop" views=36879 age=111d ratio=5.43 [LONG]
  - TQrhIMOBBvo "The Economics of Owning a Silk Road Caravan" views=29839 age=113d ratio=4.31 [LONG]
  - S4Rh_n6LoX0 "The Economics of A Medieval Bank" views=20293 age=108d ratio=3.08 [LONG]

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