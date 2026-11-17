# PensionCraft
Channel id `UC9OIwUcx-Uss7xj7s1P5XGw` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=1504300 | mean=50143.3 | median=41500.0 | max=123000 | min=9300 | p10=22600 | p25=29000 | p75=67250 | p90=91200 | p99=123000 | cv=0.59

## 2. Performance Distribution
- All: p10=22600 p25=29000 median=41500.0 p75=67250 p90=91200 p99=123000 CV=0.59
- Mean/median ratio: 1.21 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=1504300 | mean=50143.3 | median=41500.0 | max=123000 | min=9300 | p10=22600 | p25=29000 | p75=67250 | p90=91200 | p99=123000 | cv=0.59

## 4. Topic Distribution (heuristic)
- Stocks/Investing: 16 videos, median views 40000
- Money/Personal Finance: 6 videos, median views 42500
- Other/Unclassified: 4 videos, median views 53000
- Geopolitics/Trade: 1 videos, median views 29000
- Debt/Banking: 1 videos, median views 13000
- Real Estate/Housing: 1 videos, median views 69000
- Inflation/Recession/Macro: 1 videos, median views 91000
- Duration bins: {'15-30m': 22, '8-15m': 8}

## 5. Publishing Pattern
- Date range: n/a → n/a (None days); uploads/week ≈ None
- Days between upload dates: median=n/a, mean=n/a, max=n/a; consistency (CV of gaps)=n/a
- Weekday counts: {}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
- Quarterly:

## 6. Performance Classification
- All: {'Average': 19, 'Successful': 9, 'Underperforming': 2}
- Shorts: {}  Long-form: {'Average': 19, 'Successful': 9, 'Underperforming': 2}
- Top 5 by age-adjusted ratio:
  - 9Mn4dLMIKyI "How Much Do You Need To Retire in 2026?" views=123000 age=Noned ratio=2.96 [LONG]
  - rAA3fSUu9JQ "Best Index Funds For Long Term: One ETF To Rule Them All (2026)" views=123000 age=Noned ratio=2.96 [LONG]
  - xuIkpQpAzao "Is The European Stock Market A Huge Opportunity Or A Mistake?" views=93000 age=Noned ratio=2.24 [LONG]
  - KRP8RrjpdA0 "2008 Financial Crisis 2.0: Is It Already Happening?" views=91000 age=Noned ratio=2.19 [LONG]
  - 4ggYePA755I "Vanguard's New ETFs Compared: Worth It?" views=84000 age=Noned ratio=2.02 [LONG]

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