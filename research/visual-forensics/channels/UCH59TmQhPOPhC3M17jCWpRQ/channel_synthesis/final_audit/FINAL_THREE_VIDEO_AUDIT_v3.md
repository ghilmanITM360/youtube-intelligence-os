# Barely Evolved: three-video audit v3 (N17, 2026-11-05)

Session 15f69c1b. Kit visual-ct-scan v1.0. Supersedes `FINAL_THREE_VIDEO_AUDIT_v2.md` (kept) for the rows below.

## Decision
**Analysis/reporting complete; off-device portability pending.** `NON_AUDIO_COMPLETE` is not awarded, because R20 needs an off-device transfer. `CT_SCAN_COMPLETE` is not awarded, because audio gates are unmet.

## Matrix (`FINAL_AUDIT_MATRIX_v3.csv`)
| Status | Rows |
|---|---|
| BLOCKED | R09, R21 |
| FAIL | R22 |
| PARTIAL | R08, R20 |
| PASS | R01, R02, R03, R04, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19 |
| PASS (state-level; sparse frames) | R06 |
| PASS_WITHIN_DECLARED_COVERAGE | R05, R07 |

**R22 unmet dependencies:** R08 PARTIAL (ASR only), R09 BLOCKED (no listening), R21 BLOCKED (no AV sign-off), R20 PARTIAL (transfer pending).

## R05/R07: measured coverage and visual inspection are separate
| Video | Intervals | Frames measured | Interior frames viewed | Intervals fully viewed | Blind rows | Orchestrator native rows | CAMERA_FRAMEWIDE | Camera not established |
|---|---|---|---|---|---|---|---|---|
| uPQcyookL0Y | 282 | 11910 | 1135/11910 | 70 | 20 | 9 | 52 | 137 |
| mNLNb-Z4T0M | 288 | 14301 | 1209/14301 | 68 | 40 | 13 | 100 | 124 |
| GNaBxt_zIRA | 280 | 14113 | 1267/14113 | 48 | 39 | 14 | 79 | 112 |

Measured frames were not all seen. PASS applies within this declared coverage.

## Batch 2
All 30 rows were tile-only STATIC_HOLD labels that measurement contradicted, so this is a targeted sample and not a population error rate.
- Ledger STATIC_HOLD confirmed 0, corrected 30.
- Blind class upheld 15, differs 15.
- Final classes: {'CHARACTER': 10, 'INTRA_SHOT_STATE': 2, 'WHOLE_CONTENT_MOVE': 10, 'MIXED': 7, 'CAMERA': 1}.
- Attribution: {'NOT_CAMERA': 12, 'CAMERA_VS_SLIDE_UNRESOLVED': 10, 'CAMERA': 6, 'CAMERA_SUBTHRESHOLD_UNRESOLVED': 2}. 12 rows stay unresolved on camera attribution (10 camera vs artwork slide, 2 subthreshold).

## Methods
See `nonaudio_completion/method_v3/METHOD_CHANGE_LOG_N17.md`. Only M0 was preregistered. M1, M2, M3 and R-v3 came after observation. Frame-wide moves the ledger class did not name (excluding MIXED): 145 under M3; the N16 note reported 173 under M2.

## Open evidence items
- 6 R3 rows flagged where the blind label conflicts with M3, not re-inspected: ['mNLN-U0189', 'mNLN-U0231', 'mNLN-U0254', 'GNaB-U0109', 'GNaB-U0192', 'GNaB-U0239'].
- Ledger CAMERA rows with M3 NO_CAMERA or OBJECT_MOVE are flagged in `camera_m3_vs_ledger`, not changed. Rows outside the samples keep their ledger class.

## R13
**PASS.** Criterion: "Describe actual reviewer independence accurately. Do not invent an additional human-review requirement unless the kit explicitly requires it." Location: owner final-audit prompt, session 1e8761b1 transcript line 14, 2026-11-04T16:41:27Z (same text in session 7a28d062 line 2442); owner N15 prompt 2026-11-05T16:15:12Z asks whether independence means a separate reviewer or an explicitly different vendor/model and states same vendor is not automatically a failure. visual-ct-scan 13_completion_gates_validation_handoffs.md:44 asks quality_gate.json for a reviewer locator; 10_script_and_creator_brain.md:22 warns a simulated panel is not independent validation; no kit file requires a different vendor or a human. Limit: every reviewer and the orchestrator are Claude models, so this is separate-context independence, not vendor independence. Cross-vendor review was not run and is not required.

## R18/R19
Fresh values before N17 (`FINAL_VALIDATION_v3_pre_N17.json`), remote 16bd0cc7:
- uPQcyookL0Y: EVIDENCE_SHA256SUMS_checkpoint_N15 1099 entries, 0 mismatches; 304 remote files, 0 sha mismatches, 1 unmapped.
- mNLNb-Z4T0M: EVIDENCE_SHA256SUMS_checkpoint_N5 40 entries, 0 mismatches; 208 remote files, 0 sha mismatches, 0 unmapped.
- GNaBxt_zIRA: EVIDENCE_SHA256SUMS_checkpoint_N6 698 entries, 0 mismatches; 189 remote files, 0 sha mismatches, 0 unmapped.
- channel_synthesis: EVIDENCE_SHA256SUMS_checkpoint_N16 150 entries; 4 files differ: the 3 v2 ledgers (N17 columns appended) and scripts/blind_adjudicate_measure.py (edited for batch 2 after the N16 seal); all re-sealed by N17.

## R20
The 17-item package is verified fresh (249,052,569 bytes, 0 hash mismatches). See `portability/R20_VERIFY_N17.json` for sources, dependencies and gaps. Transfer BLOCKED; R20 PARTIAL.

## Remaining
1. R20: owner names an approved off-device destination; then run `scripts/stage_and_verify.sh <DEST>`.
2. Audio: R08, R09, R21 need actual listening.
