# Chronofold
Channel id `UCN87LLx0N_ZZ9BZBegN1WXA` · niche LANDSCAPE/OTHER(MachineA) · subs None · snapshot 2026-11-11

## 1. Channel Performance Report
- Total videos in DB: 2 (Shorts 0, Long-form 2)
- Views (all): n=2 | total=426958 | mean=213479 | median=213479.0 | max=425204 | min=1754 | p10=44099 | p25=107616 | p75=319342 | p90=382859 | p99=420970 | cv=0.99

## 2. Performance Distribution
- All: p10=44099 p25=107616 median=213479.0 p75=319342 p90=382859 p99=420970 CV=0.99
- Mean/median ratio: 1.0 (>1 = right-skew, a few hits dominate)

## 3. Shorts vs Long-form
- Shorts: n=0
- Long-form: n=2 | total=426958 | mean=213479 | median=213479.0 | max=425204 | min=1754 | p10=44099 | p25=107616 | p75=319342 | p90=382859 | p99=420970 | cv=0.99

## 4. Topic Distribution (heuristic)
- History/Explainers: 2 videos, median views 213479
- Duration bins: {'8-15m': 2}

## 5. Publishing Pattern
- Date range: 2026-09-05 → 2026-10-17 (43 days); uploads/week ≈ 0.33
- Days between upload dates: median=42, mean=42, max=42; consistency (CV of gaps)=0.0
- Weekday counts: {'Sat': 2}
- Upload hour (UTC, only where timestamp exists, n=2): {13: 1, 22: 1}
- Monthly (n, median views, age-adj median ratio):
  - 2026-09: 1, 425204, 1.99
  - 2026-10: 1, 1754, 0.01
- Quarterly:
  - 2026-Q3: 1, 425204, 1.99
  - 2026-Q4: 1, 1754, 0.01

## 6. Performance Classification
- All: {'Underperforming': 1, 'Successful': 1}
- Shorts: {}  Long-form: {'Underperforming': 1, 'Successful': 1}
- Top 5 by age-adjusted ratio:
  - nB3WRMupmW4 "The ENTIRE History of Afghanistan in 15 Minutes" views=425204 age=67d ratio=1.99 [LONG]
  - -2_MAElCGCc "The ENTIRE History of Switzerland in 15 Minutes" views=1754 age=25d ratio=0.01 [LONG]

## 7. Baseline Methodology
- Format split: label SHORT/Short = Short; empty label with duration<=60s = Short (inferred); everything else Long-form. Baseline = median views per format.
- Age adjustment: per channel+format with n>=15 dated videos, OLS ln(views+1) = a + b·ln(age_days+7); expected views = fitted value; ratio = (views+1)/(expected+1). If n<15, slope<0 or no date: ratio vs format median (no age adjustment).
- Thresholds from pooled ratio distribution of all 3624 classified videos: Underperforming < P25 (0.42); Average P25–P65 (<1.45); Successful P65–P90 (<7.13); Breakout ≥ P90 (7.13).
- Percentile cut-offs are descriptive conventions, not performance claims.

## 8. Data Limitations
- only 2 videos: baselines low-confidence
- dataset may be a newest-N sample, not full catalogue; compare with channel_total_videos
- single view-count snapshot; no historical snapshots, so no growth curves
- topic = keyword heuristic on title (inference, not fact)
- likes/comments/CTR/retention not used for classification