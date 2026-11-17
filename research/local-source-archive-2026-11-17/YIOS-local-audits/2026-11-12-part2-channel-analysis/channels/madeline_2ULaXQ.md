# Madeline
Channel id `UChghyih02gp-TC7w22ULaXQ` · niche FINANCE · subs 3430 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 49 (Shorts 0, Long-form 49)
- Views (all): n=49 | total=423984 | mean=8652.7 | median=661 | max=243085 | min=28 | p10=83 | p25=164 | p75=3057 | p90=13623 | p99=142181 | cv=4.0

## 2. Performance Distribution
- All: p10=83 p25=164 median=661 p75=3057 p90=13623 p99=142181 CV=4.0
- Mean/median ratio: 13.09 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=49 | total=423984 | mean=8652.7 | median=661 | max=243085 | min=28 | p10=83 | p25=164 | p75=3057 | p90=13623 | p99=142181 | cv=4.0

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 21 videos, median views 866
- Debt/Banking: 15 videos, median views 1418
- Money/Personal Finance: 5 videos, median views 449
- History/Explainers: 5 videos, median views 341
- Real Estate/Housing: 2 videos, median views 185
- Geopolitics/Trade: 1 videos, median views 33
- Duration bins: {'15-30m': 33, '8-15m': 16}

## 5. Publishing Pattern
- Date range: 2026-08-04 → 2026-11-07 (96 days); uploads/week ≈ 3.57
- Days between upload dates: median=1.0, mean=2.3, max=25; consistency (CV of gaps)=1.75
- Weekday counts: {'Sun': 5, 'Mon': 7, 'Fri': 7, 'Sat': 9, 'Thu': 7, 'Tue': 7, 'Wed': 7}
- Upload hour (UTC, only where timestamp exists, n=49): {0: 1, 1: 6, 2: 5, 3: 2, 4: 4, 5: 1, 7: 1, 8: 2, 9: 2, 11: 4, 12: 2, 15: 7, 16: 8, 17: 1, 18: 3}
- Monthly (n, median views, age-adj median ratio):
  - 2026-08: 23, 1089, 1.65
  - 2026-09: 14, 284, 0.43
  - 2026-10: 8, 1009, 1.53
  - 2026-11: 4, 1256, 1.90
- Quarterly:
  - 2026-Q3: 37, 354, 0.54
  - 2026-Q4: 12, 1172, 1.77

## 6. Performance Classification
- All: {'Breakout': 11, 'Average': 14, 'Underperforming': 15, 'Successful': 9}
- Shorts: {}  Long-form: {'Breakout': 11, 'Average': 14, 'Underperforming': 15, 'Successful': 9}
- Top 5 by age-adjusted ratio:
  - sNpbDH7IUKw "IRS Sets New $600 Checking Account Threshold — What Seniors Need to Kn" views=243085 age=83d ratio=367.20 [LONG]
  - PDoAlsQ0Juo "Banks Are Required to Tell You This — But Most Never Do" views=32868 age=97d ratio=49.65 [LONG]
  - 5gTpEMJcThM "Every Senior Must Do This Before September 2026" views=31825 age=81d ratio=48.08 [LONG]
  - 0bAvVO82O54 "The VA Won't Tell You This One Move Locks Your Rating Forever" views=15793 age=81d ratio=23.86 [LONG]
  - 3javKka8rUE "The Hidden Bank Account Rule Every Senior Needs to Know in 2026" views=14043 age=93d ratio=21.21 [LONG]

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