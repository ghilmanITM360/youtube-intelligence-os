# MonkeyExplains
Channel id `UCiBGqUxeTe4AYQyRseSZaKw` · niche ECONOMICS · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 63 (Shorts 15, Long-form 48)
- Views (all): n=63 | total=20332546 | mean=322738.8 | median=227762 | max=1920233 | min=3771 | p10=19126 | p25=116336 | p75=430940 | p90=683678 | p99=1551259 | cv=1.03

## 2. Performance Distribution
- All: p10=19126 p25=116336 median=227762 p75=430940 p90=683678 p99=1551259 CV=1.03
- Mean/median ratio: 1.42 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=15 | total=442646 | mean=29509.7 | median=21792 | max=131980 | min=3771 | p10=4812 | p25=7524 | p75=40908 | p90=43477 | p99=119599 | cv=1.06
- Long-form: n=48 | total=19889900 | mean=414372.9 | median=348056.0 | max=1920233 | min=88487 | p10=143332 | p25=193787 | p75=464861 | p90=719682 | p99=1640527 | cv=0.8

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 19 videos, median views 391566
- Other/Unclassified: 9 videos, median views 149139
- Stocks/Investing: 9 videos, median views 21792
- History/Explainers: 8 videos, median views 389212
- Business/Companies: 5 videos, median views 43547
- Money/Personal Finance: 5 videos, median views 141683
- Geopolitics/Trade: 4 videos, median views 312592
- Debt/Banking: 3 videos, median views 227584
- Real Estate/Housing: 1 videos, median views 276070
- Duration bins: {'15-30m': 15, '8-15m': 29, '1-3m': 14, '3-8m': 4, '<=60s': 1}

## 5. Publishing Pattern
- Date range: 2025-05-26 → 2026-10-18 (511 days); uploads/week ≈ 0.86
- Days between upload dates: median=8, mean=9.3, max=47; consistency (CV of gaps)=0.81
- Weekday counts: {'Sun': 22, 'Wed': 8, 'Fri': 9, 'Sat': 10, 'Thu': 8, 'Mon': 4, 'Tue': 2}
- Upload hour (UTC, only where timestamp exists, n=63): {6: 1, 7: 2, 10: 1, 12: 1, 13: 2, 14: 9, 15: 44, 16: 2, 18: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2025-05: 2, 146215, 0.82
  - 2025-06: 11, 24313, 0.40
  - 2025-07: 2, 429370, 1.26
  - 2025-08: 3, 387530, 1.14
  - 2025-09: 2, 592351, 1.74
  - 2025-10: 1, 725803, 2.15
  - 2025-11: 2, 321790, 0.96
  - 2025-12: 1, 1325113, 3.95
  - 2026-01: 3, 276070, 0.83
  - 2026-02: 4, 392943, 1.19
  - 2026-03: 3, 185160, 0.56
  - 2026-04: 4, 208706, 0.64
  - 2026-05: 3, 144038, 0.44
  - 2026-06: 1, 999806, 3.11
  - 2026-07: 3, 433617, 1.36
  - 2026-08: 4, 355628, 1.13
  - 2026-09: 4, 410852, 1.34
  - 2026-10: 10, 43460, 1.54
- Quarterly:
  - 2025-Q2: 13, 24313, 0.56
  - 2025-Q3: 7, 500813, 1.47
  - 2025-Q4: 4, 578552, 1.72
  - 2026-Q1: 10, 258429, 0.78
  - 2026-Q2: 8, 179598, 0.55
  - 2026-Q3: 11, 410455, 1.34
  - 2026-Q4: 10, 43460, 1.54

## 6. Performance Classification
- All: {'Average': 35, 'Successful': 19, 'Underperforming': 9}
- Shorts: {'Successful': 6, 'Underperforming': 5, 'Average': 4}  Long-form: {'Average': 31, 'Successful': 13, 'Underperforming': 4}
- Top 5 by age-adjusted ratio:
  - HoMjC5lG6Sk "OpenAI is (Probably) Not Gonna Survive #animation #openai" views=131980 age=27d ratio=6.06 [SHORT]
  - bz0OGtrkjv0 "The US National Debt Crisis Explained with Bananas" views=1920233 age=516d ratio=5.60 [LONG]
  - LfQIJgU_W2w "The OpenAI Bubble is Worse Than You Think" views=1325113 age=342d ratio=3.95 [LONG]
  - sy4HzG_qzKw "The SpaceX Bubble Crash Is Worse Than It Looks" views=999806 age=141d ratio=3.11 [LONG]
  - TSJQ8SjcTPk "How did Apestein Get So Rich?" views=838476 age=271d ratio=2.53 [LONG]

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