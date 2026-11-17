# Wealth Logic Australia
Channel id `UCpUvGrDOLrlhpUr5hXnpD9g` · niche FINANCE · subs 952 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 21 (Shorts 0, Long-form 21)
- Views (all): n=21 | total=97309 | mean=4633.8 | median=3311 | max=23929 | min=606 | p10=897 | p25=1408 | p75=4572 | p90=7840 | p99=21809 | cv=1.13

## 2. Performance Distribution
- All: p10=897 p25=1408 median=3311 p75=4572 p90=7840 p99=21809 CV=1.13
- Mean/median ratio: 1.4 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=21 | total=97309 | mean=4633.8 | median=3311 | max=23929 | min=606 | p10=897 | p25=1408 | p75=4572 | p90=7840 | p99=21809 | cv=1.13

## 4. Topic Distribution (heuristic)
- Money/Personal Finance: 9 videos, median views 3043
- Stocks/Investing: 5 videos, median views 2774
- Other/Unclassified: 4 videos, median views 2990
- Inflation/Recession/Macro: 2 videos, median views 6148
- Debt/Banking: 1 videos, median views 6532
- Duration bins: {'8-15m': 17, '3-8m': 3, '15-30m': 1}

## 5. Publishing Pattern
- Date range: 2026-05-15 → 2026-07-18 (65 days); uploads/week ≈ 2.26
- Days between upload dates: median=2.0, mean=3.2, max=9; consistency (CV of gaps)=0.72
- Weekday counts: {'Sat': 3, 'Tue': 5, 'Thu': 4, 'Mon': 2, 'Fri': 2, 'Wed': 2, 'Sun': 3}
- Upload hour (UTC, only where timestamp exists, n=21): {2: 6, 3: 12, 4: 2, 6: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-05: 6, 1003, 0.30
  - 2026-06: 12, 3896, 1.18
  - 2026-07: 3, 2242, 0.68
- Quarterly:
  - 2026-Q2: 18, 3471, 1.05
  - 2026-Q3: 3, 2242, 0.68

## 6. Performance Classification
- All: {'Successful': 4, 'Average': 11, 'Underperforming': 5, 'Breakout': 1}
- Shorts: {}  Long-form: {'Successful': 4, 'Average': 11, 'Underperforming': 5, 'Breakout': 1}
- Top 5 by age-adjusted ratio:
  - jph7IBd-790 "The ATO’s New 2026 Crackdown Is Catching Ordinary Australians" views=23929 age=167d ratio=7.23 [LONG]
  - m3yjYv1o21Y "How Much You Need Invested To Earn $100,000/Year In Dividends In Austr" views=13330 age=161d ratio=4.03 [LONG]
  - BPAueV0Ack0 "The Australian Economy Is Cracking In Places Nobody Talks About" views=7840 age=144d ratio=2.37 [LONG]
  - 3yTDKS2a5m8 "The ATO Is Now Tracking These 5 Aussie Income Sources" views=6533 age=162d ratio=1.97 [LONG]
  - E8DnTRDxorw "Never Keep More Than This In Your Bank Account In Australia" views=6532 age=158d ratio=1.97 [LONG]

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