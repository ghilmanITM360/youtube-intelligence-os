# xkcd's What If? — coverage honesty audit (P1, 2026-11-08, LOCAL ONLY)

Per-video table: `coverage_by_video.csv` (44 rows; built by `~/YIOS-local-audits/tooling/asset_library/xkcd/coverage_audit.py` from `library_manifest.csv`, `videos/<id>/source_manifest.json`, `videos/<id>/quality_gate.json`, `census/census.csv`, `campaign/short_long_text_reuse_population.csv`). No status was changed.

## 1. What the library covers (MEASURED)
- Channel CH-000004 (UC6IxnFzHofFJ5X2PycSMsww). Census 2026-11-04: 45 long + 46 Shorts = 91.
- Library: **24 of 45 long (53%)**, **20 of 46 Shorts (43%)**. All 24 long = 1920x1080, all 20 Shorts = 1080x1920, all 24 fps CFR (container `24/1`; manifests record a VFR "CHECK" note on packet durations, PTS checks all pass).
- Duration in library: long 5,526.8 s (92.1 min, 162–407 s each), Shorts 1,698.4 s (28.3 min, 21–150 s each). Publish dates 2023-11-29 → 2026-10-13.
- 5,458 states (one representative frame each), 2,755 near-duplicate clusters.
- Not in the library: 20 Pop-6 long videos (measured by the campaign's quant script only; no state ledger); 1 long + 2 Shorts with no local source; 24 Shorts with local media but no ledger.

## 2. Overlap (AGENTS rule 9)
| Shorts in library | n | Notes |
|---|---|---|
| Narration excerpt of a long video that is ALSO in the library | 9 | 2p305nzcVQE←FkUNHhVbQ1Q, 5k8ciEx__5w←-1-ldW4kpLM, GgEGcxJRDik←WH4g1ptJ-70, XvvXDEtMfhw←WH4g1ptJ-70, Ny9m2l6h478←p2M8Y0z9Rl0, d5TD3r1nLqM←YL2VNtus4xk, i6e4NnFnQi0←2LSyizrk8-0, kNry0bf7eC0←8fADp43wJwU, sFTRRdHqZIQ←EsUBRd1O2dU |
| Excerpt of a long video NOT in the library | 7 | Uj10jGq2O8o, _efsqO-4OoQ, aMshLs0YCTQ, jVy3qd70AqU, mEUqVgGf4e0, rGZ6TsXvi8E, wBLVmEZV2Oc |
| Standalone narration | 2 | SLd4hnmeW_g, oLoxdLfB6Gs |
| No caption text, parent UNKNOWN | 2 | 35KZm1yiyIE, TIDHee_Q5Gk |
- Manual v0.7 §1 says paired Shorts are the same drawings re-laid out for 9:16 (OBSERVED on 3 pairs). So the **independent visual sample is about 24 long + 11 Shorts**. The 9 overlapping Shorts are only evidence of how the channel re-lays art for 9:16, not extra style evidence. Counts in later phases are given per cluster and per video, and say when Shorts overlap.
- 10 videos also in the repo's forensic index have different media hashes there: a different evidence set, not merged (checkpoint R finding, not re-verified).

## 3. Kit reference 13 gates, per video (copied from each `quality_gate.json`)
| Gate (ref 13) | PASS | PARTIAL | BLOCKED | Meaning for xkcd |
|---|---|---|---|---|
| Source identity | 44 | 0 | 0 | MET |
| Temporal: full overview (every decoded frame measured) | 44 | 0 | 0 | MET |
| Temporal: candidate shots verified | 44 | 0 | 0 | MET |
| Temporal: meaningful state timing | 0 | 44 | 0 | NOT MET: some onsets unresolved; 11,685 of 173,344 frames (6.7%) sit in listed unviewed or unverified activity intervals |
| Motion design review | 2 | 42 | 0 | NOT MET: in-between frames sampled; easing UNAVAILABLE (manual §6) |
| Creative design review | 0 | 44 | 0 | NOT MET: tile-scale (1/4) review; small text partly unreadable |
| Visual-script mapping | 0 | 44 | 0 | NOT MET: ASR_UNCERTIFIED only |
| Production blueprint / reconstruction prompts | 0 | 44 | 0 | NOT MET per video; channel-level RT1–RT4 animatics exist (RT2/RT3/RT4 PASS on rhythm/grammar, silent) |
| Audio human listening | 0 | 0 | 44 | BLOCKED_CAPABILITY |
| Final AV sign-off | 0 | 0 | 44 | BLOCKED |
- Status stays **VISUAL_ANALYSIS_PARTIAL** for all 44. No video is CT_SCAN_COMPLETE. No audio sign-off.

## 4. What this means for clone readiness
- Enough for a **visual style system** (canvas, line, character, layout, rhythm, entering classes): 35 independent videos, 3 years, both formats, held-out sets 1–5 passed for rhythm/grammar (HELDOUT_EVALUATION v1–v6).
- Not enough for: exact motion curves (sampled, P4 adds a few measured windows), narration-driven timing (no listening), sound design (UNAVAILABLE), a claim that the whole channel was reviewed (53% / 43% sample).
- Known reviewer error rate is above zero (manual: 3 classification errors found by primary in 2 videos; 16 hidden cuts found by dense strips).
