# Marcus Retires
Channel id `UCW_JmbBR0gsRGIUGRY3WA-Q` · niche FINANCE · subs 7500 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 29 (Shorts 0, Long-form 29)
- Views (all): n=29 | total=804591 | mean=27744.5 | median=2098 | max=244513 | min=93 | p10=219 | p25=538 | p75=21653 | p90=76850 | p99=215941 | cv=1.9

## 2. Performance Distribution
- All: p10=219 p25=538 median=2098 p75=21653 p90=76850 p99=215941 CV=1.9
- Mean/median ratio: 13.22 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=29 | total=804591 | mean=27744.5 | median=2098 | max=244513 | min=93 | p10=219 | p25=538 | p75=21653 | p90=76850 | p99=215941 | cv=1.9

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 15 videos, median views 6276
- Money/Personal Finance: 8 videos, median views 1731
- Debt/Banking: 4 videos, median views 78337
- History/Explainers: 2 videos, median views 326
- Duration bins: {'15-30m': 24, '8-15m': 5}

## 5. Publishing Pattern
- Date range: 2026-10-05 → 2026-11-09 (36 days); uploads/week ≈ 5.64
- Days between upload dates: median=1, mean=1.3, max=8; consistency (CV of gaps)=1.02
- Weekday counts: {'Mon': 5, 'Fri': 4, 'Thu': 4, 'Wed': 4, 'Sun': 3, 'Sat': 5, 'Tue': 4}
- Upload hour (UTC, only where timestamp exists, n=29): {0: 1, 5: 1, 8: 1, 9: 2, 10: 3, 11: 4, 12: 4, 13: 1, 14: 2, 15: 4, 16: 2, 17: 1, 20: 2, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 24, 4544, 1.08
  - 2026-11: 5, 387, 0.21
- Quarterly:
  - 2026-Q4: 29, 2098, 0.57

## 6. Performance Classification
- All: {'Breakout': 7, 'Successful': 7, 'Underperforming': 12, 'Average': 3}
- Shorts: {}  Long-form: {'Breakout': 7, 'Successful': 7, 'Underperforming': 12, 'Average': 3}
- Top 5 by age-adjusted ratio:
  - b-oBChjaZo4 "Never Keep More Than This in the Bank After 65 — Most Seniors Miss The" views=244513 age=20d ratio=64.16 [LONG]
  - MBrPZfSmVo0 "NEW Bank Rules for Social Security Direct Deposits in 2026 — What Ever" views=142470 age=15d ratio=46.08 [LONG]
  - VmpfwwTqhgY "🚨 NEW SSA RULES (Updated October 2026): Seniors Born in the 40s, 50s a" views=74611 age=16d ratio=23.06 [LONG]
  - 2jWRfKNHmaY "Breaking: Social Security Announces 4 Major Changes for 2027" views=70520 age=23d ratio=16.62 [LONG]
  - 5CIZ4R6LiQk "6 Places Seniors Should Never Keep Their Cash Before Nov 1" views=85806 age=33d ratio=15.07 [LONG]

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