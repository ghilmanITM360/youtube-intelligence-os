# Economics Explained
Channel id `UCZ4AMrDcNrfy3X6nsU8-rPg` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=18602000 | mean=620066.7 | median=546000.0 | max=1500000 | min=149000 | p10=235700 | p25=330250 | p75=821750 | p90=1110000 | p99=1442000 | cv=0.57

## 2. Performance Distribution
- All: p10=235700 p25=330250 median=546000.0 p75=821750 p90=1110000 p99=1442000 CV=0.57
- Mean/median ratio: 1.14 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=18602000 | mean=620066.7 | median=546000.0 | max=1500000 | min=149000 | p10=235700 | p25=330250 | p75=821750 | p90=1110000 | p99=1442000 | cv=0.57

## 4. Topic Distribution (heuristic)
- Inflation/Recession/Macro: 10 videos, median views 763000
- Business/Companies: 5 videos, median views 553000
- Geopolitics/Trade: 5 videos, median views 252000
- Money/Personal Finance: 4 videos, median views 496000
- History/Explainers: 2 videos, median views 794000
- Other/Unclassified: 2 videos, median views 594500
- Real Estate/Housing: 1 videos, median views 415000
- Debt/Banking: 1 videos, median views 321000
- Duration bins: {'15-30m': 23, '8-15m': 6, '>30m': 1}

## 5. Publishing Pattern
- Date range: n/a → n/a (None days); uploads/week ≈ None
- Days between upload dates: median=n/a, mean=n/a, max=n/a; consistency (CV of gaps)=n/a
- Weekday counts: {}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
- Quarterly:

## 6. Performance Classification
- All: {'Underperforming': 2, 'Average': 20, 'Successful': 8}
- Shorts: {}  Long-form: {'Underperforming': 2, 'Average': 20, 'Successful': 8}
- Top 5 by age-adjusted ratio:
  - QtZfbWOkoIY "Australia May Have Just Solved The Housing Crisis" views=1500000 age=Noned ratio=2.75 [LONG]
  - jknb1YE6zdY "Finally a Country Is Taxing Its Billionaires" views=1300000 age=Noned ratio=2.38 [LONG]
  - TsfsoaNFyTQ "Economics Is A Junk Science" views=1200000 age=Noned ratio=2.20 [LONG]
  - 4kSd7zyXGo0 "Why New Zealand Is the Only Safe Haven Left" views=1100000 age=Noned ratio=2.01 [LONG]
  - J9PzjUlyzAY "The Economy Gave Up On Young People ... It's Starting To Show" views=1100000 age=Noned ratio=2.01 [LONG]

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