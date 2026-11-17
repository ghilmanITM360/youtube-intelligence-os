# How Money Works
Channel id `UCkCGANrihzExmu9QiqZpPlQ` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 30 (Shorts 0, Long-form 30)
- Views (all): n=30 | total=30125000 | mean=1004166.7 | median=775000.0 | max=3000000 | min=288000 | p10=481300 | p25=637000 | p75=1275000 | p90=1710000 | p99=2768000 | cv=0.59

## 2. Performance Distribution
- All: p10=481300 p25=637000 median=775000.0 p75=1275000 p90=1710000 p99=2768000 CV=0.59
- Mean/median ratio: 1.3 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=30 | total=30125000 | mean=1004166.7 | median=775000.0 | max=3000000 | min=288000 | p10=481300 | p25=637000 | p75=1275000 | p90=1710000 | p99=2768000 | cv=0.59

## 4. Topic Distribution (heuristic)
- Other/Unclassified: 11 videos, median views 768000
- Inflation/Recession/Macro: 5 videos, median views 799000
- Geopolitics/Trade: 5 videos, median views 570000
- Stocks/Investing: 3 videos, median views 782000
- History/Explainers: 2 videos, median views 1032500
- Money/Personal Finance: 2 videos, median views 1219500
- Business/Companies: 1 videos, median views 1700000
- Debt/Banking: 1 videos, median views 3000000
- Duration bins: {'8-15m': 2, '15-30m': 28}

## 5. Publishing Pattern
- Date range: n/a → n/a (None days); uploads/week ≈ None
- Days between upload dates: median=n/a, mean=n/a, max=n/a; consistency (CV of gaps)=n/a
- Weekday counts: {}
- Upload hour (UTC, only where timestamp exists, n=0): {}
- Monthly (n, median views, age-adj median ratio):
- Quarterly:

## 6. Performance Classification
- All: {'Successful': 10, 'Average': 19, 'Underperforming': 1}
- Shorts: {}  Long-form: {'Successful': 10, 'Average': 19, 'Underperforming': 1}
- Top 5 by age-adjusted ratio:
  - QmWyQ-BCD8E "Why A National Debt Default Now Looks Genuinely Possible... (sort of)" views=3000000 age=Noned ratio=3.87 [LONG]
  - mUBBqAjVuco "WTF Is Happening To The Car Market?" views=2200000 age=Noned ratio=2.84 [LONG]
  - 4rmkiGMknpg "Can Meta Actually Survive This?" views=1800000 age=Noned ratio=2.32 [LONG]
  - w-DVTHH1ux8 "50% Of AI Data Centers Have Quietly Been Cancelled Or "Delayed"" views=1700000 age=Noned ratio=2.19 [LONG]
  - yU2raZftgmE "How Is Everything Outpacing Inflation At The Same Time?" views=1500000 age=Noned ratio=1.94 [LONG]

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