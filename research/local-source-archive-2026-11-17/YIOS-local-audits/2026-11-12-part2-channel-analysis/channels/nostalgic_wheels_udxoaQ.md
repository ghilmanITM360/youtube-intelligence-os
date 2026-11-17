# Nostalgic Wheels
Channel id `UC3itSU41yG8jSOk8UudxoaQ` · niche ECONOMICS · subs 29200 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 39 (Shorts 0, Long-form 39)
- Views (all): n=39 | total=234018 | mean=6000.5 | median=653 | max=186865 | min=129 | p10=202 | p25=347 | p75=1671 | p90=4200 | p99=117662 | cv=4.89

## 2. Performance Distribution
- All: p10=202 p25=347 median=653 p75=1671 p90=4200 p99=117662 CV=4.89
- Mean/median ratio: 9.19 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=39 | total=234018 | mean=6000.5 | median=653 | max=186865 | min=129 | p10=202 | p25=347 | p75=1671 | p90=4200 | p99=117662 | cv=4.89

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 19 videos, median views 1270
- Other/Unclassified: 8 videos, median views 706
- History/Explainers: 6 videos, median views 530
- Money/Personal Finance: 3 videos, median views 191
- Business/Companies: 1 videos, median views 653
- Real Estate/Housing: 1 videos, median views 408
- Debt/Banking: 1 videos, median views 215
- Duration bins: {'15-30m': 25, '8-15m': 14}

## 5. Publishing Pattern
- Date range: 2026-06-17 → 2026-11-10 (147 days); uploads/week ≈ 1.86
- Days between upload dates: median=2.0, mean=3.8, max=62; consistency (CV of gaps)=2.52
- Weekday counts: {'Mon': 5, 'Sun': 6, 'Wed': 8, 'Sat': 5, 'Fri': 4, 'Tue': 6, 'Thu': 5}
- Upload hour (UTC, only where timestamp exists, n=39): {10: 1, 11: 3, 12: 4, 13: 19, 14: 11, 15: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 2, 461, 0.38
  - 2026-07: 18, 1383, 1.24
  - 2026-08: 5, 215, 0.21
  - 2026-10: 9, 653, 1.12
  - 2026-11: 5, 221, 0.62
- Quarterly:
  - 2026-Q2: 2, 461, 0.38
  - 2026-Q3: 23, 995, 0.90
  - 2026-Q4: 14, 633, 1.05

## 6. Performance Classification
- All: {'Underperforming': 12, 'Successful': 13, 'Average': 13, 'Breakout': 1}
- Shorts: {}  Long-form: {'Underperforming': 12, 'Successful': 13, 'Average': 13, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - Zii5ijysjZc "The Economics Of Owning a Cafe" views=186865 age=130d ratio=159.16 [LONG]
  - O199mD8gTO4 "Intel Is (Finally) Getting What They Deserve..." views=3206 age=35d ratio=4.63 [LONG]
  - cXg8nfa1WP8 "The Economics Of Owning a Bar" views=4752 age=121d ratio=4.17 [LONG]
  - 3CQlAQYasR0 "The Economics Of Owning a Laundromat Business" views=4570 age=122d ratio=4.00 [LONG]
  - 2DbwcwaxIlg "The Economics Of Owning a Gym" views=4377 age=128d ratio=3.75 [LONG]

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