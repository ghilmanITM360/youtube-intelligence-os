# Tom - Lazy Dividend Investor
Channel id `UCUhTFmf6v8Kk2-ofFD2udkg` · niche FINANCE · subs 2740 · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 100 (Shorts 0, Long-form 100)
- Views (all): n=100 | total=578121 | mean=5781.2 | median=3926.5 | max=61617 | min=203 | p10=366 | p25=1614 | p75=7659 | p90=12017 | p99=22231 | cv=1.27

## 2. Performance Distribution
- All: p10=366 p25=1614 median=3926.5 p75=7659 p90=12017 p99=22231 CV=1.27
- Mean/median ratio: 1.47 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=100 | total=578121 | mean=5781.2 | median=3926.5 | max=61617 | min=203 | p10=366 | p25=1614 | p75=7659 | p90=12017 | p99=22231 | cv=1.27

## 4. Topic Distribution (heuristic)
- Stocks/Investing: 66 videos, median views 3904
- Money/Personal Finance: 16 videos, median views 1173
- Other/Unclassified: 14 videos, median views 7944
- History/Explainers: 4 videos, median views 7646
- Duration bins: {'15-30m': 38, '>30m': 62}

## 5. Publishing Pattern
- Date range: 2026-08-01 → 2026-11-09 (101 days); uploads/week ≈ 6.93
- Days between upload dates: median=1.0, mean=1.4, max=7; consistency (CV of gaps)=0.83
- Weekday counts: {'Thu': 15, 'Sat': 15, 'Mon': 17, 'Sun': 13, 'Fri': 15, 'Wed': 14, 'Tue': 11}
- Upload hour (UTC, only where timestamp exists, n=100): {0: 19, 1: 7, 12: 54, 13: 15, 14: 2, 15: 2, 16: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-08: 16, 2864, 0.51
  - 2026-09: 18, 3460, 0.84
  - 2026-10: 48, 7313, 2.88
  - 2026-11: 18, 306, 0.20
- Quarterly:
  - 2026-Q3: 34, 3026, 0.62
  - 2026-Q4: 66, 4834, 1.86

## 6. Performance Classification
- All: {'Underperforming': 29, 'Successful': 38, 'Average': 31, 'Breakout': 2}
- Shorts: {}  Long-form: {'Underperforming': 29, 'Successful': 38, 'Average': 31, 'Breakout': 2}
- Top 5 by age-adjusted ratio:
  - qCO8HvpAGqc "Don't Stop Buying Dividends in a Crash Until You See This Math" views=61617 age=27d ratio=20.58 [LONG]
  - S1kkIad_pQ4 "Here’s What Happens When You Own $100,000 of SCHD" views=21833 age=13d ratio=9.93 [LONG]
  - etrZWtRFLn8 "I Tested 3 New Dividend ETFs Against SCHD: The Results Are Shocking" views=16805 age=20d ratio=6.42 [LONG]
  - V5gTH3N_kL0 "$600,000 in SCHD and a 0.84% Raise: Sell, Hold, or Fix This Instead?" views=17326 age=22d ratio=6.35 [LONG]
  - 34RoU8F6CFM "Don't Swap Your Dividends for 5% Treasuries Until You See This Math" views=18338 age=27d ratio=6.12 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- coverage 100/121 of channel's reported videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification