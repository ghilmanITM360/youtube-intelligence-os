# Modern MBA
Channel id `UCbzVRTkX3bzNZuBd9In4XyA` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=13455000 | mean=448500 | median=282000.0 | max=2200000 | min=91000 | p10=147700 | p25=164250 | p75=613750 | p90=727100 | p99=2026000 | cv=1.0

## 2. Performance Distribution
- All: p10=147700 p25=164250 median=282000.0 p75=613750 p90=727100 p99=2026000 CV=1.0
- Mean/median ratio: 1.59 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=13455000 | mean=448500 | median=282000.0 | max=2200000 | min=91000 | p10=147700 | p25=164250 | p75=613750 | p90=727100 | p99=2026000 | cv=1.0

## 4. Topic Distribution (heuristic)
- History/Explainers: 13 videos, median views 522000
- Business/Companies: 4 videos, median views 431000
- Money/Personal Finance: 4 videos, median views 165000
- Geopolitics/Trade: 3 videos, median views 231000
- Debt/Banking: 2 videos, median views 316500
- Other/Unclassified: 2 videos, median views 200000
- Inflation/Recession/Macro: 1 videos, median views 278000
- Real Estate/Housing: 1 videos, median views 295000
- Duration bins: {'>30m': 22, '15-30m': 8}

## 5. Publishing Pattern
- Date range: n/a → n/a (None days); uploads/week ≈ None
- Days between upload dates: median=n/a, mean=n/a, max=n/a; consistency (CV of gaps)=n/a
- Weekday counts: {}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
- Quarterly:

## 6. Performance Classification
- All: {'Successful': 11, 'Average': 17, 'Underperforming': 1, 'Breakout': 1}
- Shorts: {}  Long-form: {'Successful': 11, 'Average': 17, 'Underperforming': 1, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - Ha2oNXDZuSg "Why Crumbl Cookies Can't Survive" views=2200000 age=Noned ratio=7.80 [LONG]
  - niQ7mk13xew "The Crumbling Business of Marijuana" views=1600000 age=Noned ratio=5.67 [LONG]
  - PU1zr8ka-0s "Why Buffets Suddenly Disappeared" views=809000 age=Noned ratio=2.87 [LONG]
  - oPeX6FO2zls "Why Self-Checkout Failed to Replace Cashiers" views=718000 age=Noned ratio=2.55 [LONG]
  - Gi1GDBEp1yA "Why Texas BBQ Joints Rarely Survive" views=696000 age=Noned ratio=2.47 [LONG]

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