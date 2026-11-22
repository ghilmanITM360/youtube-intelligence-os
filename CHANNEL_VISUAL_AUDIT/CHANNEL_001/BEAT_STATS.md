> **CORRECTION 2026-11-22 (Codex audit accepted):** "callout" here means *callout-family label overlap*, not verified red callouts. Report as: evidence-family overlap 173/288 numeric sentences vs 563/1,437 all (1.53x) and 390/1,149 other (1.77x); callout-family overlap 40/288 vs 102/1,437 (1.96x) and 62/1,149 (2.57x). The "median 4.8 s after the source enters" figure derived from `EVIDENCE_SEQUENCES.csv` is SUPERSEDED/RETRACTED: it is the median future label interval among 95 of 724 evidence-state rows within a five-state lookahead, can cross cuts and documents, and does not measure screenshot-to-mark delay. Corrected matched-event measurements: `CLOSURE2/forensics/EVIDENCE_EVENTS.csv`.

# BEAT_STATS (13 long-form CH001, ASR-sentence vs visual-state families; generated)

Base rate = share of ALL narration sentences whose time window contains the family. Conditional = share among sentences with the narration pattern. Lift = cond/base. Correlational only: window overlap, ASR unverified, asset_ids come from prior ledgers.

Sentences: 1437

| narration pattern | n | evidence (lift) | callout (lift) | character (lift) | text (lift) | object (lift) | map (lift) |
|---|---|---|---|---|---|---|---|
| ALL (base) | 1437 | 0.39 | 0.07 | 0.46 | 0.40 | 0.20 | 0.01 |
| number | 288 | 0.60 (1.53) | 0.14 (1.96) | 0.39 (0.86) | 0.48 (1.21) | 0.22 (1.06) | 0.01 (0.50) |
| date | 96 | 0.54 (1.38) | 0.12 (1.76) | 0.36 (0.80) | 0.43 (1.07) | 0.19 (0.92) | 0.01 (0.75) |
| question | 167 | 0.28 (0.72) | 0.05 (0.67) | 0.52 (1.14) | 0.49 (1.23) | 0.12 (0.59) | 0.01 (0.43) |
| contrast | 181 | 0.32 (0.82) | 0.07 (1.01) | 0.56 (1.23) | 0.44 (1.10) | 0.18 (0.87) | 0.01 (0.40) |
| cause | 256 | 0.39 (1.00) | 0.09 (1.21) | 0.54 (1.18) | 0.45 (1.12) | 0.28 (1.38) | 0.03 (2.25) |
| org | 102 | 0.44 (1.13) | 0.11 (1.52) | 0.36 (0.79) | 0.37 (0.94) | 0.25 (1.21) | 0.02 (1.41) |
| example | 6 | 0.83 (2.13) | 0.00 (0.00) | 0.33 (0.73) | 0.17 (0.42) | 0.17 (0.82) | 0.00 (0.00) |
