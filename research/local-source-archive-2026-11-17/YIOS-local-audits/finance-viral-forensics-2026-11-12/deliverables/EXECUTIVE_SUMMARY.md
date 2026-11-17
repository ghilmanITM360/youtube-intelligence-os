# Executive Summary — Finance/Economics Viral Intelligence (2026-11-12)

**Answer to the research question:** in this 69-channel database, the strongest evidence-backed pattern is not a hook, title or thumbnail *style*. It is **who published** (channel identity explains 44–53% of log-view variance) and **which specific subject** a video covers. Within a channel, hook/title/script/thumbnail *wording and design* features are close to indistinguishable between winners and losers.

## Verified facts
- Database = **3,634 unique videos** (not 3,410); 3,410 is the count of videos that have a transcript. 3,450 transcript rows = 3,410 + 40 second-source rows. 3,576 of 3,634 thumbnail URLs return HTTP 200 (56 are 404; 545 are derived patterns, not captured).
- 3,056 long-form videos in 60 channels classified against their own temporal-neighbour baseline: **398 Breakout, 424 Successful, 1,451 Average, 783 Underperforming**.
- Held-out-channel prediction from text features: AUC 0.50 (titles) – 0.59 (script). Not useful for forecasting.

## What the data supports / contradicts
- **Contradicts** common advice in this niche: titles ≤60 characters (0.89×), "enhancer" words like secret/money/mistake (0.86×), titles ending in a question (0.79×, matching a DS-000018 creator's 0.82× claim), and a monotonic "more Viral-Checklist boxes = more viral" (flat to slightly negative, peak at ~3 boxes).
- **Weakly supports**: addressing the viewer ("you") in the first ~30 s (1.16×, not significant after correction); longer videos and evidence-dense scripts (small positive).
- **Null (no detectable effect)**: numbers, dollar figures, urgency, contrarian wording, open loops, question hooks, BUT/THEREFORE density, thumbnail face/text/colour (after multiple-testing correction), posting day/hour, upload cadence.
- Same title template, same thumbnail layout, PI from 0.15 to 445: Costco (569k views) and Aldi (348k) vs Amazon (4.6k) and Airlines (0.8k) — the subject drove the difference.

## Exploratory opportunities (post-hoc; need holdout tests)
1. Concrete-entitlement framing for seniors ("owes you / free / can't be taken"): 2.5× (95% CI 1.27–4.86), n≈58.
2. True deadline/new-rule framing in senior content: 1.45× (1.06–1.97), n=132.
3. Bank-account-rule topic, "real math" comparisons, and ELI5 explainers have supporting examples but are weaker or scale-confounded.
The earlier-looking "senior formula" (audience age + "most miss") collapses when near-duplicate scripts are excluded.

## Caveats
Independence is compromised (73 near-duplicate script pairs, 170 videos sharing a title with another channel — 26% of those are Breakouts, consistent with title cloning). No CTR/retention/velocity data, so none of those claims are tested. DS-000018 cannot establish an algorithm change from a static snapshot. **External research (VidIQ, Google Trends US) was not executed.** Full detail: `REPORT.md`, `27_evidence_ledger.csv`.
