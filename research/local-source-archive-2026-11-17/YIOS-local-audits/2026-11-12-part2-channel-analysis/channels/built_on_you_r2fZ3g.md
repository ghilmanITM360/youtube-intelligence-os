# Built On You
Channel id `UC8p5EKG8jlsL2R2bvr2fZ3g` · niche ECONOMICS · subs 15400 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 10 (Shorts 0, Long-form 10)
- Views (all): n=10 | total=1191559 | mean=119155.9 | median=75261.0 | max=430614 | min=1828 | p10=2959 | p25=16440 | p75=175180 | p90=260433 | p99=413596 | cv=1.1

## 2. Performance Distribution
- All: p10=2959 p25=16440 median=75261.0 p75=175180 p90=260433 p99=413596 CV=1.1
- Mean/median ratio: 1.58 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=10 | total=1191559 | mean=119155.9 | median=75261.0 | max=430614 | min=1828 | p10=2959 | p25=16440 | p75=175180 | p90=260433 | p99=413596 | cv=1.1

## 4. Topic Distribution (heuristic)
- History/Explainers: 7 videos, median views 37830
- Business/Companies: 3 videos, median views 112692
- Duration bins: {'15-30m': 9, '8-15m': 1}

## 5. Publishing Pattern
- Date range: 2026-10-04 → 2026-11-10 (38 days); uploads/week ≈ 1.84
- Days between upload dates: median=4, mean=4.1, max=9; consistency (CV of gaps)=0.46
- Weekday counts: {'Sun': 1, 'Fri': 3, 'Tue': 5, 'Thu': 1}
- Upload hour (UTC, only where timestamp exists, n=10): {13: 8, 14: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 8, 124004, 1.65
  - 2026-11: 2, 2456, 0.03
- Quarterly:
  - 2026-Q4: 10, 75261, 1.00

## 6. Performance Classification
- All: {'Successful': 5, 'Underperforming': 4, 'Average': 1}
- Shorts: {}  Long-form: {'Successful': 5, 'Underperforming': 4, 'Average': 1}
- Top 5 by age-adjusted ratio:
  - jOo8wSIeGus "The ENTIRE History of Amazon in 20 Minutes" views=430614 age=38d ratio=5.72 [LONG]
  - bOc-RUVrLSo "The ENTIRE History of Toyota in 20 Minutes" views=241524 age=29d ratio=3.21 [LONG]
  - AwxcZVfJUSA "The ENTIRE History of Costco in 19 Minutes" views=188468 age=22d ratio=2.50 [LONG]
  - EtNH4mzw7AM "The ENTIRE History of Walmart in 19 Minutes" views=135316 age=36d ratio=1.80 [LONG]
  - 8oGSERdqoUI "The ENTIRE History of Microsoft in 21 Minutes" views=112692 age=26d ratio=1.50 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 10 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification