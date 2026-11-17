# The Wealth Engine
Channel id `UCfTD1TTaLoeF02x8wWFUcKw` · niche ECONOMICS · subs 5140 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 6 (Shorts 0, Long-form 6)
- Views (all): n=6 | total=493983 | mean=82330.5 | median=1100.5 | max=489223 | min=489 | p10=516 | p25=650 | p75=1452 | p90=245376 | p99=464838 | cv=2.21

## 2. Performance Distribution
- All: p10=516 p25=650 median=1100.5 p75=1452 p90=245376 p99=464838 CV=2.21
- Mean/median ratio: 74.81 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=6 | total=493983 | mean=82330.5 | median=1100.5 | max=489223 | min=489 | p10=516 | p25=650 | p75=1452 | p90=245376 | p99=464838 | cv=2.21

## 4. Topic Distribution (heuristic)
- Real Estate/Housing: 2 videos, median views 1035
- Inflation/Recession/Macro: 2 videos, median views 245099
- Debt/Banking: 1 videos, median views 489
- Money/Personal Finance: 1 videos, median views 1226
- Duration bins: {'15-30m': 4, '8-15m': 2}

## 5. Publishing Pattern
- Date range: 2026-10-04 → 2026-11-08 (36 days); uploads/week ≈ 1.17
- Days between upload dates: median=2, mean=7, max=24; consistency (CV of gaps)=1.23
- Weekday counts: {'Sun': 3, 'Fri': 2, 'Wed': 1}
- Upload hour (UTC, only where timestamp exists, n=6): {4: 1, 10: 1, 14: 1, 17: 2, 19: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 3, 1226, 1.11
  - 2026-11: 3, 542, 0.49
- Quarterly:
  - 2026-Q4: 6, 1100, 1.00

## 6. Performance Classification
- All: {'Average': 5, 'Breakout': 1}
- Shorts: {}  Long-form: {'Average': 5, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - YqAiWBFwbpg "How Economy Actually  Work?" views=489223 age=38d ratio=444.14 [LONG]
  - -7K3THinxOs "Renting vs Buying a House: Which Actually Makes You Richer?" views=1528 age=10d ratio=1.39 [LONG]
  - ytu4K0FNwJk "How the Wealthy Buy More Freedom" views=1226 age=14d ratio=1.11 [LONG]
  - 7wLPaWB8wUM "How a Shipping Disruption Overseas Can Hit the American Economy" views=975 age=12d ratio=0.89 [LONG]
  - PVBkCJakwUE "The Complete Real Estate Business Explained in 20 Minutes" views=542 age=5d ratio=0.49 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 6 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- coverage 6/8 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification