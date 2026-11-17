# Matty Invests
Channel id `UCkqzov98m_7niJOXwbRQgBA` · niche FINANCE · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 94 (Shorts 0, Long-form 94)
- Views (all): n=94 | total=2595340 | mean=27610 | median=3984.5 | max=1084237 | min=171 | p10=907 | p25=2102 | p75=11248 | p90=31699 | p99=283368 | cv=4.2

## 2. Performance Distribution
- All: p10=907 p25=2102 median=3984.5 p75=11248 p90=31699 p99=283368 CV=4.2
- Mean/median ratio: 6.93 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=94 | total=2595340 | mean=27610 | median=3984.5 | max=1084237 | min=171 | p10=907 | p25=2102 | p75=11248 | p90=31699 | p99=283368 | cv=4.2

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 86 videos, median views 3984
- Stocks/Investing: 5 videos, median views 5910
- Real Estate/Housing: 1 videos, median views 1279
- History/Explainers: 1 videos, median views 201
- Debt/Banking: 1 videos, median views 4800
- Duration bins: {'15-30m': 8, '8-15m': 86}

## 5. Publishing Pattern
- Date range: 2026-01-24 → 2026-08-22 (211 days); uploads/week ≈ 3.05
- Days between upload dates: median=2, mean=2.3, max=5; consistency (CV of gaps)=0.37
- Weekday counts: {'Sat': 30, 'Thu': 26, 'Mon': 29, 'Tue': 7}
- Upload hour (UTC, only where timestamp exists, n=92): {21: 92}
- Monthly (n, median views, age-adj median ratio):
  - 2026-01: 5, 346, 0.09
  - 2026-02: 14, 7753, 1.95
  - 2026-03: 16, 4299, 1.08
  - 2026-04: 11, 2412, 0.61
  - 2026-05: 13, 2176, 0.55
  - 2026-06: 12, 2668, 0.67
  - 2026-07: 11, 12373, 3.10
  - 2026-08: 10, 8668, 2.18
- Quarterly:
  - 2026-Q1: 35, 4137, 1.04
  - 2026-Q2: 36, 2450, 0.61
  - 2026-Q3: 21, 9338, 2.34

## 6. Performance Classification
- All: {'Average': 39, 'Successful': 25, 'Underperforming': 20, 'Breakout': 10}
- Shorts: {}  Long-form: {'Average': 39, 'Successful': 25, 'Underperforming': 20, 'Breakout': 10}
- Top 5 by age-adjusted ratio:
  - 5V1gCUvdqMs "7 Things Wealthy Retirees Stopped Buying to Stay Rich" views=1084237 age=184d ratio=272.05 [LONG]
  - 7mqI2YgRW1w "Why People Get Richer After Retirement" views=223088 age=284d ratio=55.98 [LONG]
  - A-lvYmMpGSA "10 Things Retirees Just Stopped Caring About" views=219096 age=121d ratio=54.97 [LONG]
  - 6U9jXkpQBzE "What Retirement Looks Like With a $2Million Portfolio" views=146923 age=230d ratio=36.86 [LONG]
  - Q1RP8c_9bKs "Simple Routines Thriving Retirees Practice Daily" views=122987 age=107d ratio=30.86 [LONG]

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