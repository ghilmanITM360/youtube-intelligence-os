# Held-out-2 evaluation (2026-11-04T16:31Z) — manual v0.3 vs HELDOUT_PROTOCOL_v2.md (pre-registered before ingest)
Videos: JqFSGkFPipM (2024-11, 337 s), UQgw50GQu1A (2025-07, 221 s), r7B0MzvwDcA (2026-03, 173 s). Same pipeline; all sheets opened by fresh sonnet reviewers (transcript-audited); primary spot-check 1 sheet each + primary dense strip for r7B0MzvwDcA G0008. Raw: campaign/heldout2_quant.csv, aggregate_heldout2.csv.

| Rule | JqFS | UQgw | r7B0 |
|---|---|---|---|
| Q1 events/min (16.6–32.5) | PASS 18.5 | PASS 17.7 | PASS 22.6 |
| Q2 cuts/min (2.69–8.26) | PASS 6.59 | PASS 5.97 | PASS 3.48 (lower bound: 3 cuts hidden in G0008) |
| Q3 median hold (1.35–2.52 s) | PASS 2.38 | PASS 2.44 | **FAIL 1.29** |
| Q5 1920x1080 24 fps | PASS | PASS | PASS |
| Q6 loudness (−17.3…−15.6) | **FAIL −18.0** | PASS −16.5 | PASS −16.6 |
| Q7 last HOLD 239–240 f | PASS 239 | **FAIL 235 f (9.79 s red credits card)** | PASS 239 |
| R4' question card + attribution | PASS (present f0) | PASS | PASS (present f0) |
| R4'' red title card 6–31 s, ≈2 s | PASS 9.4 s | PASS 16.3 s | PASS 13.8 s |
| R7 majority 1-frame activities | PASS 0.90 | PASS 0.74 | PASS 0.52 (marginal) |
| R1/R2 off-white default + red accent | PASS | PASS (long dark night/space scenes = known counterexample) | PASS |
| R10 deadpan aside | PASS (spot) | not checked on spot sheet | PASS 'THIS LOOKS LIKE A BAD IDEA' |

Score: 30/33 PASS. Failures: (1) r7B0 median hold 1.29 s — 2026 long-form continues the density trend (BO8r 1.48, 9VG0 1.75) and adds CONTINUOUS drawn animation (digger descent, growing temperature curve) inside long activities; v0.3 hold floor too high for 2026. (2) JqFS loudness −18.0 LUFS — loudness band is not universal (levels only, no listening). (3) Q7 exact 239–240 f too strict: a ~10 s red end card holds (UQgw 9.79 s).
Verdict: v0.3 HELD-OUT-2 PASS WITH 3 NARROW FAILURES. Rule changes for v0.4: median hold 1.25–2.5 s (2026 nearer the low end); loudness −16…−18 LUFS; end card "≈10 s (235–240 f)"; add continuous drawn growth/descent animation to §6 device table (r7B0 G0008).
