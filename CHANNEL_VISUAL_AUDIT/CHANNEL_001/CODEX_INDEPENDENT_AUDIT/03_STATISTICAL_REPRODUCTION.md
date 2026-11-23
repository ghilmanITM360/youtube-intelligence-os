# Statistical reproduction

The independent Python implementation reads raw ASR word arrays, visual-state intervals and shot ledgers directly. It does not invoke Claude's generator. Run `python3 CHANNEL_VISUAL_AUDIT/CHANNEL_001/CODEX_INDEPENDENT_AUDIT/scripts/reproduce.py` from the worktree root. Full results are in [per-video counts](measurements/per_video.csv), [lag pairs](measurements/lag_pairs.csv) and [statistics](measurements/statistics.json).

| Metric | Numerical | Other | All | Numerical vs all | Numerical vs other |
|---|---:|---:|---:|---:|---:|
| Evidence-family overlap | 173/288 (60.1%) | 390/1,149 (33.9%) | 563/1,437 (39.2%) | 1.533 | 1.770 |
| Broad callout-family overlap | 40/288 (13.9%) | 62/1,149 (5.4%) | 102/1,437 (7.1%) | 1.957 | 2.574 |

The denominator is 1,437 punctuation-derived intervals from 13 selected landscape sources. Accumulate timed ASR tokens until terminal punctuation with at least four tokens, then flush any remainder. No ASR segment lacked a word array and every interval intersects a state. Those checks cannot detect missing words, incorrect transcription or timestamp drift. The number regex accepts digits and terms such as “dollar” or “million,” and misses spelled-out numerals with none of its keywords. Evidence includes any overlapping chart, logo, photo, article-like asset label and similar keywords. Callout accepts yellow, underline and other broad labels. Neither label establishes authentic provenance, substantive relevance, red color, or that a mark was added during the utterance. Some states use free-text shorthand, so unknown label recall matters. A longer interval can intersect more visual states. The figures are descriptive associations for the selected videos.

Resampling 13 whole videos with replacement, 5,000 draws, seed 103, gives 95% percentile ranges of 1.32–1.81 vs all and 1.45–2.21 vs other for evidence, and 1.63–2.29 vs all and 1.93–3.29 vs other for callouts. Leave-one-out ranges are 1.45–1.61 and 1.65–1.88 for evidence, 1.80–2.06 and 2.26–2.86 for callouts. No single video drives the direction. The oil video contributes 21/102 callout positives and the recession video 19/102. Some videos have zero matched numerical callouts. These intervals capture between-video variability within the available sample. Selection, coding, episode dependence within a video, and ASR error limit generalization.

## The 4.8-second result

95/724 evidence-labeled state rows, across 11 of 13 eligible videos, have a subsequent callout-labeled row within five states. 629 have no match under that rule. Min 0.21 s, quartiles 2.635, 4.800, 7.915 s, max 32.17 s. The algorithm can cross cuts and documents, counts a repeated source state as another starting point, skips callouts already present on entry, and can match props, different annotations and persistent labels. The 629 rows are unmatched under the lookahead rule and their true status is unknown. The table cannot estimate screenshot-to-passage, screenshot-to-first-marker, or animation onset/completion. A valid replacement needs document-instance IDs, source/target matching, simultaneous-entry cases, explicit censoring, and separately coded events. See the native examples in [04](04_INDEPENDENT_VISUAL_FINDINGS.md).

## Cutting rhythm

2,052 recorded shot intervals from 13 videos, median 2.8667 s, IQR 1.8666–4.4000 s, maximum 25.4583 s. Per-video medians range 2.125–4.367 s. Using 2,039 interior ledger boundaries and exact probed video-stream duration, per-video rates span 11.783–23.733 per minute. The canonical table divides shots, including the opening, by minutes. Its rounded range is still usable as a prior. The calculation excludes the other landscape sources and all Shorts, inherits editorial grouping and holds from Claude's ledgers, and is independent arithmetic with spot-checked cut labels. It does not establish detector precision or recall across the corpus.

Concrete invalid pairs are `Im-N3K9Pnf0` S081→S085 (11.13 s) and S082→S085 (8.00 s). S081/S082 describe market-cap and comparator charts. The underline in S085 marks 41.8% in a distinct return-attribution card, which first appears at S083. Both earlier charts receive the same future event in the aggregation.
