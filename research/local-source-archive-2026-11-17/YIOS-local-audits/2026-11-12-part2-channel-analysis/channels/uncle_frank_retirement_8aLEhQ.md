# Uncle Frank Retirement
Channel id `UCLh3aiudWdnfR0QDC8aLEhQ` · niche FINANCE · subs 899 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 35 (Shorts 0, Long-form 35)
- Views (all): n=35 | total=247959 | mean=7084.5 | median=1593 | max=37154 | min=33 | p10=325 | p25=500 | p75=7964 | p90=23588 | p99=33589 | cv=1.35

## 2. Performance Distribution
- All: p10=325 p25=500 median=1593 p75=7964 p90=23588 p99=33589 CV=1.35
- Mean/median ratio: 4.45 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=35 | total=247959 | mean=7084.5 | median=1593 | max=37154 | min=33 | p10=325 | p25=500 | p75=7964 | p90=23588 | p99=33589 | cv=1.35

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 23 videos, median views 2524
- Other/Unclassified: 7 videos, median views 1032
- Stocks/Investing: 2 videos, median views 3815
- Geopolitics/Trade: 2 videos, median views 4234
- Debt/Banking: 1 videos, median views 1478
- Duration bins: {'8-15m': 32, '15-30m': 3}

## 5. Publishing Pattern
- Date range: 2026-07-30 → 2026-11-09 (103 days); uploads/week ≈ 2.38
- Days between upload dates: median=3.0, mean=3, max=5; consistency (CV of gaps)=0.3
- Weekday counts: {'Wed': 6, 'Sun': 6, 'Thu': 7, 'Sat': 3, 'Fri': 3, 'Tue': 8, 'Mon': 2}
- Upload hour (UTC, only where timestamp exists, n=35): {13: 1, 15: 10, 16: 9, 17: 14, 18: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-07: 1, 148, 0.09
  - 2026-08: 9, 421, 0.26
  - 2026-09: 10, 1345, 0.84
  - 2026-10: 12, 7178, 4.50
  - 2026-11: 3, 3573, 2.24
- Quarterly:
  - 2026-Q3: 20, 960, 0.60
  - 2026-Q4: 15, 7100, 4.45

## 6. Performance Classification
- All: {'Successful': 10, 'Average': 7, 'Breakout': 7, 'Underperforming': 11}
- Shorts: {}  Long-form: {'Successful': 10, 'Average': 7, 'Breakout': 7, 'Underperforming': 11}
- Top 5 by age-adjusted ratio:
  - jAtHTgTbhrE "What $500,000 Really Looks Like in Retirement — It’s Not What You Thin" views=37154 age=35d ratio=23.31 [LONG]
  - Pg1vebmk7Vg "What $1 Million Really Looks Like in Retirement (The Real Math)" views=26670 age=22d ratio=16.73 [LONG]
  - OX-fSJzHyPI "The 401(k) Number Where COMPOUNDING Finally Takes Over (It's Not $1 Mi" views=26594 age=85d ratio=16.68 [LONG]
  - z6oUxuw_-Z4 "The Retirement Cash Buffer Sweet Spot You Are Missing" views=23866 age=53d ratio=14.97 [LONG]
  - _OJARWVUURg "The 401(k) Milestones Where Your Money Starts SnowBalling FAST" views=23170 age=20d ratio=14.54 [LONG]

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