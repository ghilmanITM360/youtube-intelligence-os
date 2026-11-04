# Held-out evaluation protocol v1 (pre-registered 2026-11-04T15:20Z, before any held-out reviewer output exists)
Held-out: long JcXpCyPc2Xw, BnGqPxnQh9A; Shorts Ny9m2l6h478, jVy3qd70AqU, rGZ6TsXvi8E. Rules frozen = CHANNEL_PRODUCTION_MANUAL_v0.1.md + dev ranges from aggregate_dev_interim2.csv (LONG n=6, SHORT n=16). Tolerance: PASS if inside dev [min,max] widened by 15 % of the range on each side; otherwise FAIL (recorded, not rewritten into rules before this file's results section is written).

## Quantitative rules (MEASURED + reviewer classes)
| ID | Rule | Long dev range | Short dev range |
|---|---|---|---|
| Q1 | events/min | 19.2–22.2 | 17.9–39.2 |
| Q2 | hard cuts/min | 4.91–7.62 | 0.72–11.37 |
| Q3 | median hold s | 2.15–2.33 | 1.13–2.84 |
| Q4 | activity frame share | 0.036–0.216 | 0.013–0.202 |
| Q5 | 24 fps CFR; 1920x1080 long / 1080x1920 Shorts | exact | exact |
| Q6 | loudness integrated −16.2…−16.8 LUFS (±0.5 tolerance) | | |
| Q7 | long-form ends with a full-frame red end card held 239–240 frames (observed post-hoc in dev 10/10 built long incl. unreviewed prepped dev; registered here before held-out review) | yes | n/a |

## Qualitative rules (OBSERVED by reviewer, checked by primary on ≥1 sheet)
| ID | Rule (manual §) |
|---|---|
| R1 | Off-white canvas + black hand line art as default; counterexample palettes allowed (§2) |
| R2 | Red = accent for strikes/paths/highlights; full-frame red title/end card in long (§2) |
| R3 | Stick figures without facial features; objects more detailed than figures (§2) |
| R4 | Long opens on typed reader question box (+attribution) and a red series title card within ~10 s (§3) |
| R5 | Shorts have no title card and no end card (§3, §8) |
| R6 | Reasoning steps advance mainly by hard cut to a new canvas (§4) |
| R7 | Majority of ACTIVITY events are 1-frame pops/swaps; multi-frame devices limited to write-on, dissolve ≈6 f, slide/pan 7–10 f, rare scroll (§6) |
| R8 | Labels pop on with/after their object (§5) |
| R9 | Shorts narration is an excerpt of one long video (≥90 % word reuse) unless standalone (§1) |
| R10 | Deadpan literal speech-text asides by stick figures appear (§7) |
