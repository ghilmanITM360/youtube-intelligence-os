# Nia Prescott
Channel id `UC3a2fNfeG-zvJcuDD9R8bLw` · niche FINANCE · subs 33600 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 94 (Shorts 0, Long-form 94)
- Views (all): n=94 | total=6018955 | mean=64031.4 | median=6840.0 | max=1126239 | min=246 | p10=1114 | p25=1633 | p75=23030 | p90=180333 | p99=992677 | cv=2.76

## 2. Performance Distribution
- All: p10=1114 p25=1633 median=6840.0 p75=23030 p90=180333 p99=992677 CV=2.76
- Mean/median ratio: 9.36 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=94 | total=6018955 | mean=64031.4 | median=6840.0 | max=1126239 | min=246 | p10=1114 | p25=1633 | p75=23030 | p90=180333 | p99=992677 | cv=2.76

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 42 videos, median views 10257
- Debt/Banking: 28 videos, median views 6840
- Money/Personal Finance: 13 videos, median views 3046
- Real Estate/Housing: 4 videos, median views 2604
- Geopolitics/Trade: 3 videos, median views 7185
- History/Explainers: 3 videos, median views 2609
- Inflation/Recession/Macro: 1 videos, median views 9587
- Duration bins: {'8-15m': 91, '15-30m': 3}

## 5. Publishing Pattern
- Date range: 2026-06-03 → 2026-11-09 (160 days); uploads/week ≈ 4.11
- Days between upload dates: median=1, mean=1.7, max=10; consistency (CV of gaps)=0.83
- Weekday counts: {'Wed': 13, 'Sat': 12, 'Sun': 12, 'Thu': 17, 'Tue': 18, 'Mon': 10, 'Fri': 12}
- Upload hour (UTC, only where timestamp exists, n=94): {13: 42, 14: 18, 15: 17, 16: 7, 17: 8, 18: 2}
- Monthly (n, median views, age-adj median ratio):
  - 2026-06: 20, 14587, 1.20
  - 2026-07: 18, 5822, 0.52
  - 2026-08: 12, 2943, 0.33
  - 2026-09: 17, 2631, 0.34
  - 2026-10: 22, 6840, 1.23
  - 2026-11: 5, 13364, 3.72
- Quarterly:
  - 2026-Q2: 20, 14587, 1.20
  - 2026-Q3: 47, 2840, 0.35
  - 2026-Q4: 27, 6935, 1.35

## 6. Performance Classification
- All: {'Underperforming': 40, 'Breakout': 16, 'Successful': 18, 'Average': 20}
- Shorts: {}  Long-form: {'Underperforming': 40, 'Breakout': 16, 'Successful': 18, 'Average': 20}
- Top 5 by age-adjusted ratio:
  - QhSUdkcVljM "⚠️ Every Senior Must Do This Before October 1 — Most Never Do" views=982624 age=48d ratio=137.45 [LONG]
  - OjIHOntawFc "The Government Quietly Erases These 5 Bills for Seniors After 65 — and" views=1126239 age=132d ratio=98.92 [LONG]
  - boC96bE_7Os "5 Bills You Legally Stop Paying After 65 — Most Pay Them Anyway, Not K" views=397508 age=29d ratio=68.78 [LONG]
  - UKTqnf6pu88 "The Bills You No Longer Owe After You Turn 65 (Most Never Claim Them)" views=601027 age=141d ratio=51.16 [LONG]
  - qmInVQbOzBU "The IRS Is Watching Your Bank Account — Here's How Much Cash Is Too Mu" views=367488 age=151d ratio=30.27 [LONG]

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