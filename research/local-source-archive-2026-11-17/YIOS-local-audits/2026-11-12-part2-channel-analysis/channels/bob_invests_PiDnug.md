# Bob Invests
Channel id `UCAKBDBaY1dP7OdZkGPiDnug` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 57 (Shorts 0, Long-form 57)
- Views (all): n=57 | total=3706353 | mean=65023.7 | median=24297 | max=769842 | min=1537 | p10=2829 | p25=4714 | p75=57661 | p90=116711 | p99=629976 | cv=2.02

## 2. Performance Distribution
- All: p10=2829 p25=4714 median=24297 p75=57661 p90=116711 p99=629976 CV=2.02
- Mean/median ratio: 2.68 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=57 | total=3706353 | mean=65023.7 | median=24297 | max=769842 | min=1537 | p10=2829 | p25=4714 | p75=57661 | p90=116711 | p99=629976 | cv=2.02

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 27 videos, median views 30276
- Other/Unclassified: 8 videos, median views 18773
- History/Explainers: 6 videos, median views 169458
- Debt/Banking: 6 videos, median views 7248
- Stocks/Investing: 5 videos, median views 4994
- Real Estate/Housing: 3 videos, median views 87158
- Geopolitics/Trade: 1 videos, median views 5260
- Business/Companies: 1 videos, median views 40512
- Duration bins: {'8-15m': 17, '15-30m': 38, '>30m': 2}

## 5. Publishing Pattern
- Date range: 2025-11-30 → 2026-09-09 (284 days); uploads/week ≈ 1.36
- Days between upload dates: median=2.0, mean=5.2, max=66; consistency (CV of gaps)=1.8
- Weekday counts: {'Fri': 10, 'Mon': 9, 'Thu': 7, 'Wed': 9, 'Sat': 5, 'Sun': 6, 'Tue': 9}
- Upload hour (UTC, only where timestamp exists, n=55): {14: 1, 15: 6, 16: 24, 17: 4, 18: 6, 19: 4, 20: 4, 21: 3, 22: 2, 23: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2025-11: 1, 232672, 3.42
  - 2025-12: 14, 70841, 1.21
  - 2026-01: 13, 34659, 0.74
  - 2026-02: 2, 31712, 0.82
  - 2026-03: 2, 36294, 1.13
  - 2026-05: 2, 3544, 0.23
  - 2026-06: 4, 6002, 0.49
  - 2026-07: 4, 2580, 0.38
  - 2026-08: 6, 3293, 0.69
  - 2026-09: 7, 7752, 3.69
- Quarterly:
  - 2025-Q4: 15, 75355, 1.35
  - 2026-Q1: 17, 34659, 0.77
  - 2026-Q2: 6, 4684, 0.38
  - 2026-Q3: 17, 3936, 1.10

## 6. Performance Classification
- All: {'Underperforming': 10, 'Successful': 13, 'Average': 32, 'Breakout': 2}
- Shorts: {}  Long-form: {'Underperforming': 10, 'Successful': 13, 'Average': 32, 'Breakout': 2}
- Top 5 by age-adjusted ratio:
  - pM3t-m0Zryk "Why Two Incomes Leave You Broker Than One (The Two-Income Trap)" views=769842 age=322d ratio=13.20 [LONG]
  - 8PeiQFJA2BU "The Math of Being Broke: Why You Pay Double for Everything" views=520082 age=339d ratio=7.99 [LONG]
  - Ut6gsmgRA8k "10 Travel Rules To Travel Like The 1% (Without The Luxury Price Tag)" views=14902 age=65d ratio=7.11 [LONG]
  - 1965iXdE--0 "The "Work" Scam: Why Your $30/Hour Job Pays You $4" views=383141 age=336d ratio=6.00 [LONG]
  - 8ZVbiGlJsdU "The "Upgrade Illusion": Why New Tech Makes Old Devices Obsolete" views=246056 age=292d ratio=5.20 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- 2 videos lack publish date (excluded from time/age analysis)
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification