# Held-out protocol v4 (pre-registered 2026-11-05T15:59:08Z, BEFORE ingest of held-out-4; tests manual v0.5)
Videos: oTzW-mTQd5w (2026-03), s3oLIDaElaE (2026-01), qu8nx1qUwEU (2025-11) — selection/selection_v4_heldout4.json. Never used for any rule; no file under videos/<id> existed when this was written.
Quantitative (same ranges as v3 except Q3, which now tests v0.5 §9 directly; tolerance 15 % of range each side):
- Q1 events/min → PASS 15.75–32.65
- Q2 hard cuts/min (reviewer SHOT_CUT classes) → 2.69–8.26
- Q3 median hold (v0.5 §9: 1.2–2.4 s) → PASS 1.02–2.58
- Q3b v0.5 2026 claim "2026 long-form nearer 1.2–1.8 s" → for 2026 videos only, PASS 1.10–1.90 (tolerance 15 % of 0.6 s); 2025 video n/a
- Q4 activity frame share within dev long range ±15 % (script)
- Q5 1920x1080, 24/1 fps CFR
- Q6 integrated loudness −17.3…−15.6 LUFS
- Q7 last segment HOLD 235–240 f
Qualitative (v0.5), only if a reviewer pass runs: R1 off-white default; R2 red accent (marks) + red title/end card; v0.5 R2 note: red may also be content colour (fire/heat) — record if seen; R3 featureless stick figures, detailed objects; R4' question card + attribution (typed/scaled/present at f0); R4'' red title card at 6–31 s; R6 hard cuts advance steps; R7 majority 1-frame activities; R10 deadpan asides.
If usage forbids the reviewer pass, the qualitative part and Q2 are recorded NOT_EVALUATED (not PASS). If weekly usage reaches 100 % mid-run, the state is whatever the last progress_log line says.
