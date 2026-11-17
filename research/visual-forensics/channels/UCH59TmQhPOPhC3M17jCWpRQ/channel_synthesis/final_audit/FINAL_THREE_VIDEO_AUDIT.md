# Barely Evolved — final three-video completeness audit (2026-11-04)

- **Channel:** UCH59TmQhPOPhC3M17jCWpRQ.
- **Auditor:** Claude session 1e8761b1 (opus orchestrator).
- **Standard:** YIOS Visual Forensics Intelligence Standard v1.0 (installed skill `visual-ct-scan`, reference 13 acceptance gates).
- **Branch:** research/barely-evolved-visual-forensics.
- **Audit base:** remote 7b3c3e7b8eacce0928ebc85d7661bcea18b94049.
- **Scope:** only these three videos. Nothing here is a channel-wide rule.

## Decision

All three videos remain `VISUAL_ANALYSIS_PARTIAL`. **None meets the kit's full completion contract** (`CT_SCAN_COMPLETE` and `FULL_AV_SIGNOFF` are both false).

They are ready for one limited use: **a bounded original-production experiment** that reuses the modules measured and tested below (timing and geometry only). That readiness is not CT_SCAN_COMPLETE.

## Identity (re-verified in this audit)

| video | sha256 | bytes | frames | states |
|---|---|---|---|---|
| uPQcyookL0Y | 1416669f10d7231f8110eb27044986912984dcdbacbd7d9f6440726349a0c69d | 48986292 | 14647 | 89 |
| mNLNb-Z4T0M | e6799e8f16ad31772020d98404f2c9cf90536a255c6169d29e838c55bd1dd061 | 57325446 | 16689 | 136 |
| GNaBxt_zIRA | cbe7a3afac6c6b7b13db10b7ce2493715f5299208d6f3ebffb7fd74e2bf5c0f7 | 101042486 | 16319 | 113 |

Each hash was recomputed from the MP4 in `~/Downloads/videos in mp3/BarelyEvolved-MP4/` and matches the registry row on the branch.

## Requirement matrix

The full matrix is `FINAL_AUDIT_MATRIX.csv`: 22 requirements, with a status and evidence column for each video. Per-video gates are in `kit_outputs/<vid>_<sha8>/quality_gate_FINAL.json`.

**PASS for all three:**
- R01 source identity
- R02 decoded timeline
- R03 partition (no gaps or overlaps)
- R06 state-level art direction
- R12 per-state prompts
- R14 corrections
- R17 kit files
- R18 checksum seals
- R19 remote readback

R04 boundaries: PASS for v2 and v3, PARTIAL for v1.

**PARTIAL for all three:**
- R05 intra-state motion
- R07 long-state interiors
- R08 narration alignment (ASR-based)
- R10 aliases
- R11 specs
- R13 reviewer independence
- R15 reconstruction tests
- R20 portability

R16 report and blueprint: PASS for v1, PARTIAL for v2 and v3.

**BLOCKED:** R09 listening and R21 AV sign-off.

**FAIL:** R22 CT_SCAN_COMPLETE.

## What was checked anew vs reused

**Checked anew in this audit:**
- **Source hashes.** Recomputed from the MP4s.
- **Registry readback.** Compared against the registry on the branch.
- **Calibration JSON.** Both `detector_calibration.json` files parse locally and on the remote.
- **mNLNb-Z4T0M calibration repair.** The prior bytes (in 10a7865f) were invalid JSON. Only the keys `clustering` and `note` were added, and every prior value is preserved verbatim.
- **GNaBxt_zIRA calibration repair.** Its pre-repair bytes were never published, so only the fix note documents it.
- **Deterministic validation.** `FINAL_VALIDATION.json` covers seals, remote readback, partitions and coverage.
- **17 visual checks.** Listed in `FINAL_VISUAL_CHECK.csv`:
  - 10 opening, middle, ending and ledger spot frames, all MATCH;
  - 3 dense or native measurements on disputed motion;
  - 3 adjudications of open boundaries;
  - 1 detector calibration.
- **Two new bounded reconstruction tests.** See the reconstruction section below.

**Reused, not rerun:**
- every reviewer batch;
- the full-frame measurements;
- boundary reviews;
- ASR;
- RT-01.

## Preserved findings and what changed

- **One-frame pose swaps, short entry/exit animations and fades:** still OBSERVED.
  - The v2 citation for single-frame pose swaps (S003) was wrong. Its f14-26 change is a monotonic global settle, not a swap (VC-13).
  - v2's valid example is PC-001 (f4936→4937).
- **Overshoot pop-ins in v1 and v3:** still OBSERVED.
  - v3 S015 is now MEASURED: inset height 266 → 363 → 344, about +5.5% (VC-11).
- **Overshoot in v2:** still not established either way.
  - New: four squash-expand picture swaps were MEASURED with no overshoot (VC-12).
- **v2 "jerky camera" claim:** still rejected (PC-002, per-frame measurement).

## Corrections made in this audit (`FINAL_CORRECTIONS.csv`)

- **FC-01..03:** wording corrections to the synthesis, applied in `../CHANNEL_SYNTHESIS_v1_1.md`. v1 is preserved.
- **FC-04:** UBC-001..003 adjudicated.
  - UBC-002 and UBC-003 are single-frame punch-ins.
  - UBC-001 is a continuous reframe, not a cut.
  - states_v6 was not re-partitioned.
- **FC-05:** v1's 89/89 prompts consolidated from six reviewer files.
- **FC-06:** new v1 coverage file. The old `coverage.json` (86 states) was stale and is kept as historical.
- **FC-07:** derived kit ledgers added for v2 and v3.
- **FC-08:** the 121 v2 boundary "NSF" flags are explained; they mark no defect.
- **FC-09:** v2 and v3 gate entries updated to show their reconstruction tests were run.

Raw reviewer outputs and all earlier gates, ledgers and reports are unchanged.

## Listening

- **Status:** BLOCKED_CAPABILITY for all three videos.
- **Why:** this agent can decode frames and read text and images but cannot hear audio.
- **What exists:** provisional ASR only (faster-whisper small.en, `ASR_UNCERTIFIED`).
- **Kit gates blocked as a result:**
  - the audio gate;
  - FULL_AV_SIGNOFF_COMPLETE;
  - audible synchronisation;
  - beat, SFX and music rules;
  - narration-to-visual timing beyond ASR segment level.
- The kit does not require a human for anything else, and none is claimed.

## Reconstruction tests (`RECONSTRUCTION_TESTS_FINAL.csv`)

In each test, a fresh Claude sonnet worker saw only its spec folder, and the evaluation was measured from the rendered pixels.

| test | modules | result |
|---|---|---|
| RT-01 (v1, reused) | M1 clip reveal, M3 pop overshoot, M5 pose swap | PASS for timing; style FAIL_BY_OMISSION |
| RT-V2-01 (new) | squash swap; camera push with ease | Squash PASS. Camera push FAIL on the pre-registered threshold (14 frames above 0.3 diff, 15-19 required). A post-hoc diagnostic found 16 changing frames, no held frames and an ease-in-out profile; it was not re-scored. |
| RT-V3-01 (new) | inset pop overshoot; single-frame pop-in | PASS |

None of these tests covered style, characters, full scenes or sound.

## Production manual (scoped to these three videos; timing and geometry)

| module | parameters | source | tested |
|---|---|---|---|
| White-card clip reveal | 3-6 frames, left to right, hard edge | v1 M1 | RT-01 PASS |
| Pop-in with overshoot | peak within 2 frames, settles smaller; v3 about +5% for 2 frames, settled from frame 3 | v1 M3, v3 S015 | RT-01, RT-V3-01 PASS |
| Single-frame pose/prop swap or pop-in | 1 frame, no in-between | v1 M5, v3 S003, v2 PC-001 | RT-01, RT-V3-01 PASS |
| Squash-expand picture swap | collapse 2, band 2, expand 2 frames; linear; band about 22% height; no overshoot | v2 (4 events) | RT-V2-01 PASS |
| Camera push/pan | continuous, about 16 frames, ease-in-out, no held frames | v2 PC-002 | RT-V2-01 FAIL as pre-registered |
| Single-frame punch-in reframe | 1-frame discontinuous scale change on the same artwork | v1 UBC-002/003 | untested |

**Art and prompts:**
- Per-state art and prompts are in each video's consolidated tables. For v1, use `kit_outputs/uPQcyookL0Y_1416669f/state_prompts_consolidated.csv`.
- All characters and wording must be new and original.
- Fonts, easing curves, software and sound are UNAVAILABLE.

## Portability

**Recoverable from Git on any machine** (branch research/barely-evolved-visual-forensics):
- tables, ledgers, reports, specs, prompts, gates, seals;
- scripts, briefs, RT specs and evaluations;
- this audit.

**Local-only on this Mac (Machine A)** in `~/YIOS-local-audits/barely-evolved/`:
- source MP4s;
- decoded PNG frames and strips;
- `frames_local_only/`;
- ASR WAVs;
- RT `rt.mp4` renders (their SHA-256 hashes are recorded).

Another machine can verify the text evidence but cannot redo any visual check without the MP4s, whose hashes are listed above.

## Remaining for full completion contract

1. A qualified listener reviews each source end to end: the audio gate and FULL_AV_SIGNOFF.
2. Dense review of long-state interiors and of motion outside the measured peaks, so R05 and R07 can reach PASS.
3. A states_v7 split of v1 at f2835 and f5429 (optional), plus the W085b fade-out.
4. A camera-ease evaluator recalibrated before the next run, then RT-V2-01 run again; also style and full-scene reconstruction tests.
5. A video-level asset crosswalk for v2 and v3.
