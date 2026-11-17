# Money & Macro
Channel id `UCCKpicnIwBP3VPxBAZWDeNA` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=7356000 | mean=245200 | median=228500.0 | max=510000 | min=88000 | p10=100500 | p25=142500 | p75=320250 | p90=398400 | p99=499850 | cv=0.46

## 2. Performance Distribution
- All: p10=100500 p25=142500 median=228500.0 p75=320250 p90=398400 p99=499850 CV=0.46
- Mean/median ratio: 1.07 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=7356000 | mean=245200 | median=228500.0 | max=510000 | min=88000 | p10=100500 | p25=142500 | p75=320250 | p90=398400 | p99=499850 | cv=0.46

## 4. Topic Distribution (heuristic)
- History/Explainers: 9 videos, median views 183000
- Inflation/Recession/Macro: 7 videos, median views 144000
- Geopolitics/Trade: 6 videos, median views 257000
- Other/Unclassified: 3 videos, median views 325000
- Money/Personal Finance: 3 videos, median views 272000
- Real Estate/Housing: 2 videos, median views 404000
- Duration bins: {'15-30m': 25, '8-15m': 4, '>30m': 1}

## 5. Publishing Pattern
- Date range: n/a → n/a (None days); uploads/week ≈ None
- Days between upload dates: median=n/a, mean=n/a, max=n/a; consistency (CV of gaps)=n/a
- Weekday counts: {}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
- Quarterly:

## 6. Performance Classification
- All: {'Successful': 5, 'Average': 23, 'Underperforming': 2}
- Shorts: {}  Long-form: {'Successful': 5, 'Average': 23, 'Underperforming': 2}
- Top 5 by age-adjusted ratio:
  - Y9LOOvJ7hKw "What happens when you stop taxing billionaires?" views=510000 age=Noned ratio=2.23 [LONG]
  - bufMa2Oscok "Is the Dollar finally on the way out?" views=475000 age=Noned ratio=2.08 [LONG]
  - 1N2C72OdOxo "What happened to China's property collapse?" views=411000 age=Noned ratio=1.80 [LONG]
  - yoT76zITRx8 "Why do 90% of economists oppose rent control?" views=397000 age=Noned ratio=1.74 [LONG]
  - uqSwRHc-1MQ "Who will pay for 100 million boomer pensions?" views=385000 age=Noned ratio=1.68 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- 30 videos lack publish date (excluded from time/age analysis)
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification