# Patrick Boyle
Channel id `UCASM0cgfkJxQ1ICmRilfHLw` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=44207000 | mean=1473566.7 | median=1400000.0 | max=2500000 | min=640000 | p10=885800 | p25=1125000 | p75=1675000 | p90=2300000 | p99=2471000 | cv=0.33

## 2. Performance Distribution
- All: p10=885800 p25=1125000 median=1400000.0 p75=1675000 p90=2300000 p99=2471000 CV=0.33
- Mean/median ratio: 1.05 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=44207000 | mean=1473566.7 | median=1400000.0 | max=2500000 | min=640000 | p10=885800 | p25=1125000 | p75=1675000 | p90=2300000 | p99=2471000 | cv=0.33

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 7 videos, median views 1400000
- History/Explainers: 5 videos, median views 1600000
- Geopolitics/Trade: 5 videos, median views 1400000
- Inflation/Recession/Macro: 4 videos, median views 1050000
- Stocks/Investing: 3 videos, median views 1300000
- Debt/Banking: 2 videos, median views 1600000
- Money/Personal Finance: 2 videos, median views 1497000
- Real Estate/Housing: 1 videos, median views 1000000
- Business/Companies: 1 videos, median views 1200000
- Duration bins: {'>30m': 24, '15-30m': 6}

## 5. Publishing Pattern
- Date range: n/a → n/a (None days); uploads/week ≈ None
- Days between upload dates: median=n/a, mean=n/a, max=n/a; consistency (CV of gaps)=n/a
- Weekday counts: {}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
- Quarterly:

## 6. Performance Classification
- All: {'Average': 24, 'Successful': 6}
- Shorts: {}  Long-form: {'Average': 24, 'Successful': 6}
- Top 5 by age-adjusted ratio:
  - wZaYyNAXHK4 "Scott Bessent Is at War With Prices — and Prices Are Winning!" views=2500000 age=Noned ratio=1.79 [LONG]
  - ajH6YVhdOZU "Why Germany Stopped Working" views=2400000 age=Noned ratio=1.71 [LONG]
  - T-oXyXwD6sE "Anthropic Just Filed to Go Public. Does the Math Add Up?" views=2300000 age=Noned ratio=1.64 [LONG]
  - 8BaSBjxNg-M "How Did the Metaverse Fail So Badly?" views=2300000 age=Noned ratio=1.64 [LONG]
  - wTiYaWFP59Q "How Much Would an AI Crash Destroy?" views=2100000 age=Noned ratio=1.50 [LONG]

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