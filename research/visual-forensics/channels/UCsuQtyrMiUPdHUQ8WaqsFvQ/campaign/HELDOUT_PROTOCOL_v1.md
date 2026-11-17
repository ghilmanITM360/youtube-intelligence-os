# HELDOUT_PROTOCOL_v1 (pre-registered; frozen before any held-out prep or viewing)
Rules source: CHANNEL_PRODUCTION_MANUAL_v1.md (sha256 in HELDOUT_PROTOCOL_v1.sha256) and aggregate_dev_final.json. Held-out videos: LONG xBJ6suQSt98, 6YHva7Me2ls; SHORT C_jSOXP_XWY, 5gSIU30yiVs. Each goes through the normal pipeline (prep, one reviewer, native, spot-check, process). Results are recorded in HELDOUT_EVALUATION.md without editing v1 first; any rule revision becomes v2 with the original result preserved.

## Measured checks (per video, using the DEV range of its own format, inclusive, no widening)
| ID | Check | LONG pass range | SHORT pass range |
|---|---|---|---|
| H1 | 50 fps CFR and native 1920x1080 / 1080x1920, no letterbox | yes | yes |
| H2 | background_exact_rgb within #FAFAFA–#FFFFFF (KyB-type dark exception counts as FAIL, noted) | yes | yes |
| H3 | median hold s | 0.50–1.57 | 0.89–1.34 |
| H4 | single-frame share of activities | ≥0.833 | ≥0.923 |
| H5 | scene cuts/min | 18.4–32.4 | 18.9–25.3 |
| H6 | events/min | 34.1–59.7 | 35.7–47.9 |
| H7 | mean dark-ink fraction | 0.071–0.104 | 0.079–0.129 |
| H8 | holds containing yellow | 0.24–0.62 | 0.43–0.75 |

## Observed checks (reviewer + primary spot-check)
| ID | Check |
|---|---|
| O1 | Bearded caveman with yellow spotted tunic appears (manual A4) |
| O2 | No CTA / end card observed |
| O3 | At least one literalised narrated word (ASR_UNCERTIFIED) |
| O4 | Text built on white without a captions track |

## Reuse predictions (deterministic, pe_reuse run including held-out)
- R1: C_jSOXP_XWY (Capitalism Part 5) shares ≥0.80 of ASR words with 6YHva7Me2ls (Capitalism).
- R2: 5gSIU30yiVs (Modern Things Part 3) shares ≥0.80 with 3AsDdMQr_nQ (Modern Life). LOW prior: titles differ.
- R3: xBJ6suQSt98 (Nuclear Bomb) contains ≥0.80 of IUur04eOd4A (Nuclear Bomb Part 2) words. LOW prior: "Part 2" may be new material.

Scoring: report each check PASS/FAIL per video; summary = passed/total for measured, observed and reuse separately. No threshold is declared a channel-level pass; a FAIL is a counterexample to record.
