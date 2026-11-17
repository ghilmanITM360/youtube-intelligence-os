# Held-out evaluation v4 — FINAL (2026-11-05T16:22:47Z) — against pre-registered HELDOUT_PROTOCOL_v4.md (manual v0.5)
Protocol sha256 c5cc516a… (HELDOUT_PROTOCOL_v4.sha256) written 2026-11-05 before ingest. Videos: oTzW-mTQd5w (2026-03, floating upwards), s3oLIDaElaE (2026-01, no DNA), qu8nx1qUwEU (2025-11, sun laser). Full ingest, all frames measured, one fresh sonnet reviewer per video (all sheets opened: 10/17/12, verified from transcripts), primary 0.6-scale spot-check of 1 sheet each (11/11/8 rows, 0 disagreements). Raw: heldout4_quant.csv.

## Quantitative (MEASURED)
| Rule | oTzW (2026) | s3oL (2026) | qu8n (2025) |
|---|---|---|---|
| Q1 events/min 15.75–32.65 | **FAIL 14.9** | PASS 27.3 | PASS 22.6 |
| Q2 hard cuts/min 2.69–8.26 | PASS 5.21 | PASS 6.45 | PASS 5.29 |
| Q3 median hold 1.02–2.58 s (v0.5 §9) | PASS 2.50 | PASS 1.52 | PASS 2.00 |
| Q3b 2026 hold 1.10–1.90 s (v0.5 claim) | **FAIL 2.50** | PASS 1.52 | n/a |
| Q4 activity frame share | **FAIL 0.291** | PASS 0.039 | PASS 0.032 |
| Q5 1920x1080 24/1 | PASS | PASS | PASS |
| Q6 loudness −17.3…−15.6 | PASS −16.3 | PASS −16.5 | PASS −16.7 |
| Q7 end card HOLD 235–240 f | PASS 239 | PASS 239 | PASS 239 |
Totals 20/23 PASS; all 3 failures in oTzW-mTQd5w.

Cause (OBSERVED, reviewer rows + primary SHEET_03): oTzW is a continuous-journey story. Long multi-scene ACTIVITY spans (G0018 397 f incl. title card and altitude ladder; G0042 51.7–73.9 s rising through cloud with wind streaks; G0074/G0076 zoom-out to heliopause) hold ~28 % of frames, so the segmenter counts few events and long holds. Not a measurement error; the measure merges continuous motion into one event. INFERRED: rhythm density depends on story structure (stepwise comparison vs continuous ascent), not only on year.

## Qualitative (OBSERVED)
| Rule | oTzW | s3oL | qu8n |
|---|---|---|---|
| R1 off-white default | PASS (white-on-black space scenes from G0074 = known counterexample class) | PASS | PASS (opens off-white then greys at G0002; dark space after title) |
| R2 red marks + red title/end card | PASS (strike on EARTH G0083; red title + end card) | PASS (red scribbles/marks G0050, circles; red title G0020, end card G0178) | PASS (red strike G0028, stepwise red arcs G0066–78) |
| R2 v0.5 note: red as content colour | seen: red sun glow G0078, red figure G0070 | not seen | seen: large red glows/backgrounds |
| R3 featureless stick figures, detailed objects | PASS (Empire State, Lisbon elevator, helicopter) | PASS | PASS |
| R4' question card + attribution | PASS present at f0 ('Rebecca B.') | PASS present at f0 ('Nina Charest') | PASS present at f0 ('Max Schäfer') |
| R4'' red title card 6–31 s | PASS ~13 s (f311, inside G0018) | PASS 11.7–13.7 s (G0020, onset unresolved) | PASS 14.5 s (G0010) |
| R6 hard cuts advance steps | PASS (15) | PASS (21) | PASS (15) |
| R7 majority 1-frame activities | PASS 0.81 | PASS 0.89 | PASS 0.92 |
| R10 deadpan asides | PASS ('RIP REBECCA' tombstone G0084) | PASS (mailbox gag 'NO. NEGATIVE. NO DNA PRESENT.') | PASS (sunglasses pose swap G0008; tombstone callbacks) |

## Verdict
Held-out-4 PARTIAL PASS. All visual-grammar rules generalise (27/27 qualitative). Format, loudness, end card, cuts all pass. **v0.5's "2026 long-form holds nearer 1.2–1.8 s" is FALSIFIED as a year rule** (oTzW 2.50 s); the general 1.2–2.4 s range (with tolerance) still holds. Events/min and activity-share ranges fail for continuous-journey videos. Action → manual v0.6: rhythm conditional on story structure; drop the year-based floor.
Caveats: one reviewer per video; ASR not listening (no AV signoff); "story structure" explanation is INFERRED from n=1 failing video.
