# Held-out evaluation v1 (2026-11-04T17:45Z) — against frozen HELDOUT_PROTOCOL_v1.md (manual v0.1)

Order of events (file mtimes, local GMT+5): protocol 20:06:10 → manual v0.2 written from dev only 20:34:28 → first held-out annotations 20:38:51. No held-out output was used to write v0.1 or v0.2.
Held-out: long JcXpCyPc2Xw (2023-12, "What if NASCAR had no rules?"), BnGqPxnQh9A (2026-05, bananas radioactivity); Shorts Ny9m2l6h478 (2025-11), jVy3qd70AqU (2026-06), rGZ6TsXvi8E (2026-08). All 5: full ingest, all frames measured, every segment classified by a fresh sonnet reviewer (all sheets opened, transcript-audited), primary 0.6-scale spot-check of 1 sheet each (2 corrections in jVy3qd70AqU). Raw: campaign/heldout_quant.csv, campaign/aggregate_heldout.csv.

## Quantitative (MEASURED)
| Rule | JcXp (L) | BnGq (L) | Ny9m (S) | jVy3 (S) | rGZ6 (S) |
|---|---|---|---|---|---|
| Q1 events/min | FAIL 23.6 (≤22.65) | FAIL 22.7 (≤22.65) | PASS 26.3 | PASS 32.7 | PASS 24.9 |
| Q2 cuts/min | FAIL 4.23 (≥4.50) | PASS 6.01 | PASS 6.80 | PASS 10.06 | PASS 6.93 |
| Q3 median hold | FAIL 1.63 s (≥2.12) | FAIL 1.92 s | PASS 1.96 | PASS 1.73 | PASS 1.46 |
| Q4 activity share | PASS 0.228 | PASS 0.055 | PASS | PASS | PASS |
| Q5 format 24 fps CFR + aspect | PASS | PASS | PASS | PASS | PASS |
| Q6 loudness −16.2…−16.8 ±0.5 | PASS −16.4 | PASS −16.6 | PASS −16.1 | PASS −16.4 | PASS −16.5 |
| Q7 10 s end card (last HOLD 239–240 f) | PASS 239 f | PASS 239 f | n/a | n/a | n/a |
Totals: Shorts 18/18 PASS. Long 9/14 PASS; **all 5 failures are the long-form rhythm rules Q1–Q3**: held-out long videos are denser (shorter holds) than the v0.1 dev range, which came from only 6 dev long videos (2023-11 → 2025-03). Root cause: range too narrow / under-sampled, not a measurement error. The v0.2 dev ranges (all 10 dev long, 2023–2026; written before held-out results) are events/min 18.4–30.7, cuts/min 3.33–7.62, median hold 1.48–2.38 s and **contain every held-out long value** — this is consistency, not a new independent test.

## Qualitative (OBSERVED; reviewer annotations + primary spot-check sheet)
| Rule | Result | Evidence |
|---|---|---|
| R1 off-white canvas default, counterexamples allowed | PASS 5/5 | bg #F7F7F7/#FDFDFD; rGZ6 dark gradient globe scene (SHEET_07) = known counterexample class |
| R2 red accent; full red title/end card in long | PASS 5/5 | red_hold_share 0.06–0.67; JcXp/BnGq red title + end card |
| R3 featureless stick figures; detailed objects | PASS 5/5 | JcXp rocket car vs stick figure (SHEET_01); BnGq nucleus/dice (SHEET_07) |
| R4 long opening: question box + attribution, typed letter-by-letter, red title card ~6–10 s | **PARTIAL** | Box + attribution PASS (both). Letter-by-letter typing FAIL: JcXp box scales up from tiny f10→f17; BnGq box already present at frame 0. Title card present but at 12.0 s / 14.0 s → FAIL vs v0.1 timing (v0.2 had already revised to "after cold-open premise, 6–31 s") |
| R5 Shorts: no title card, no end card | PASS 3/3 | 0 mentions in 3 annotation sets |
| R6 steps advance mainly by hard cut | PASS 5/5 | 12–19 SHOT_CUT activities per video |
| R7 majority of activities 1-frame | PASS 5/5 | 1-frame share 0.72, 0.63, 0.93, 0.90, 0.80 |
| R8 labels pop with/after their object | PASS (sampled) | Ny9m car box + 'X 1,000,000'; BnGq '40K' + 'EVERY SECOND' |
| R9 Shorts narration excerpt of one long | PASS 3/3 but **NOT INDEPENDENT** (population scan already included these Shorts) | short_long_text_reuse_population.csv 0.99/0.905/0.937 |
| R10 deadpan literal asides | PASS 5/5 | "DON'T STAND NEXT TO BANANAS. GOT IT." (BnGq), "WHATCHYA DOING?" / "ECONOMICS." (jVy3), "OH NO!" (rGZ6), "HOW DID WE GET HERE?" (Ny9m), "POINT OF FAILURE" (JcXp) |

## Verdict
Held-out PARTIAL PASS. Visual grammar, palette, character, red-accent, Shorts structure, format, loudness and end-card rules generalise (all 5 videos). Long-form rhythm ranges and the "typed question" opening detail did NOT generalise under v0.1. Actions taken in manual v0.2 (before held-out) already widen rhythm ranges and the title-card timing; the opening rule must be relaxed to "question card appears (typed, scaled-up, or present at frame 0)". Adequacy criterion (2) held-out success is therefore NOT fully met for v0.1; a further held-out test of v0.2 needs NEW unseen long videos (census has 45 long; 33 unselected, of which 1 known unavailable) — expansion batch of 3 long justified by this failure per CAMPAIGN_GOAL_v1.
