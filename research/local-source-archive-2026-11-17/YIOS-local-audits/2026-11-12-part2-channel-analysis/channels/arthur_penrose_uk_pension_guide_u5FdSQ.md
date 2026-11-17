# Arthur Penrose | UK Pension Guide
Channel id `UCsAnRVKKrZCD7YRVLu5FdSQ` · niche FINANCE · subs 3420 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 22 (Shorts 0, Long-form 22)
- Views (all): n=22 | total=596885 | mean=27131.1 | median=9536.0 | max=154987 | min=553 | p10=993 | p25=1907 | p75=25202 | p90=91935 | p99=147846 | cv=1.52

## 2. Performance Distribution
- All: p10=993 p25=1907 median=9536.0 p75=25202 p90=91935 p99=147846 CV=1.52
- Mean/median ratio: 2.85 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=22 | total=596885 | mean=27131.1 | median=9536.0 | max=154987 | min=553 | p10=993 | p25=1907 | p75=25202 | p90=91935 | p99=147846 | cv=1.52

## 4. Topic Distribution (heuristic)
- Debt/Banking: 7 videos, median views 1718
- Other/Unclassified: 7 videos, median views 14610
- Money/Personal Finance: 5 videos, median views 5507
- History/Explainers: 2 videos, median views 27865
- Real Estate/Housing: 1 videos, median views 20408
- Duration bins: {'15-30m': 9, '8-15m': 13}

## 5. Publishing Pattern
- Date range: 2026-10-11 → 2026-11-09 (30 days); uploads/week ≈ 5.13
- Days between upload dates: median=1, mean=1.4, max=5; consistency (CV of gaps)=0.76
- Weekday counts: {'Mon': 3, 'Sat': 4, 'Fri': 4, 'Tue': 2, 'Thu': 3, 'Wed': 2, 'Sun': 4}
- Upload hour (UTC, only where timestamp exists, n=22): {11: 1, 13: 1, 15: 1, 17: 6, 18: 8, 19: 2, 20: 2, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-10: 18, 14148, 1.30
  - 2026-11: 4, 855, 0.34
- Quarterly:
  - 2026-Q4: 22, 9536, 0.98

## 6. Performance Classification
- All: {'Underperforming': 8, 'Breakout': 4, 'Successful': 4, 'Average': 6}
- Shorts: {}  Long-form: {'Underperforming': 8, 'Breakout': 4, 'Successful': 4, 'Average': 6}
- Top 5 by age-adjusted ratio:
  - lnL7tyjfysY "BORN BEFORE 1955 You're Being Paid the Wrong State Pension Amount" views=120981 age=11d ratio=22.83 [LONG]
  - t603-fd_CNk "Never Keep More Than This in the Bank After 65 — Most Seniors Miss The" views=154987 age=23d ratio=12.65 [LONG]
  - 2cTv1qbHWHE "Born Before 1962 4 State Pension Changes Hitting Your Birth Year in 20" views=49103 age=13d ratio=7.79 [LONG]
  - 3SlwsDdaimk "Never Keep This Much Money in Bank   HMRC Sees It All in 2026 UK" views=96694 age=24d ratio=7.48 [LONG]
  - gFFM3-TTtr0 "🚨 NEW DWP RULES JULY 2026 Seniors Born in the 40s, 50s & 60s Are Affec" views=24526 age=12d ratio=4.23 [LONG]

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