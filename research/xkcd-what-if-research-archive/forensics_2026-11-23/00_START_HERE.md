# Start here: xkcd What If? complete forensics (2026-11-23)

**Folder:** `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/`

Everything produced in this research is in this one folder (outside the Git repo, nothing pushed). **RESEARCH IN PROGRESS, NOT COMPLETE and NOT independently validated** (the folder name repeats the directive's title). Mostly self-review; one partial independent review by a different tool (Codex, 2026-11-23); no audio listening.

## CONTINUATION 4 (2026-11-23): reconciliation of the Codex review and the external audit
Read first: `14_RECONCILIATION_CODEX_AND_EXTERNAL_AUDIT_2026-11-23.md` (F01 to F14, external audit points, phase table against the directive, who checked what), then `13_FINAL_REPORT.md` (v4).
| File | What it is |
|---|---|
| `14_COVERAGE_PLAN_AND_SCOPE.md` | what the directive requires for visual coverage, unit definitions, defensible plan for the rest |
| `14_SAMPLE_DESIGN_ANALYSIS.json`, `06_LEDGER_REVIEW_METHOD_AND_COVERAGE.md` (addendum) | how to read the 156-shot statistics |
| `14_MOTION_SEQUENCE_16_CODING.csv`, `phase14_motion/` | 16 shots viewed as dense sequences |
| `14_TOPIC_FAMILY_PREREGISTRATION.md`, `14_TOPIC_FAMILY_HOLDOUT.md` | topic-family stability check |
| `14_HASH_VERIFY_88.csv` | 88 media hashes recomputed |
| `14_LISTENING_PACK_ADDITIONS.csv` | 9 more items for a listener (25 in total with the earlier pack) |
| `knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv` | operative rule text revised; old text in `rule_text_prior_v3` |
| `versions_before_reconcile_2026-11-23/` | every file before it was edited |


## START HERE (read in this order)

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/13_FINAL_REPORT.md` | Final report: proof of work, key findings, what is not done |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/README_CHECKPOINT.md` | Checkpoints 1 to 6 in order: what each stage added |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_MASTER_SCRIPT_PLAYBOOK.md` | Playbook: how the xkcd What If scripts are built (descriptive, no performance claims) |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/README_LEDGERS.md` | What the new ledgers are, columns, validation, limits |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/12_CODEX_CLAUDE_WORKFLOW.md` | Rules and next steps for any agent continuing this work |

## Phase 0 to 3: workspace, strategy audit, channel inventory

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/00_PHASE0_WORKSPACE_STATE.md` | Repo state when the audit began |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/01_EXISTING_STRATEGY_DEEP_AUDIT.md` | Audit of the existing What If channel strategy |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/01_STRATEGY_CLAIM_EVIDENCE_MATRIX.csv` | 25 strategy claims with evidence tier |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/01_STRATEGY_GAPS_AND_CONFLICTS.md` | Gaps and conflicts (G3 pacing corrected after Phase 6) |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/02_DUPLICATES_AND_PROVENANCE.md` | Duplicate and provenance findings |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/02_LOCAL_VS_GITHUB_COMPARISON.md` | Local files against GitHub |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/02_LOCAL_WORKSPACE_INVENTORY.csv` | Local workspace file inventory |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/02_MEDIA_AND_TRANSCRIPT_AVAILABILITY.md` | Which media and transcripts exist |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/02_WHAT_IF_RELATED_FILE_REGISTER.csv` | Every What If related file found |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/03_CHANNEL_MASTER_INVENTORY.csv` | 92-video master inventory with visual coverage tier |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/03_CORPUS_COMPLETENESS_REPORT.md` | How complete the corpus is |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/03_VIDEO_IDENTITY_CROSSWALK.csv` | Video ID crosswalk across layers |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/media_probe_88.csv` | ffprobe and SHA-256 of the 88 library MP4s |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/rss_2026-11-23.xml` | Channel RSS snapshot |

## Phase 5: script study

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_CROSS_VIDEO_SYNTHESIS.md` | Synthesis of the 83 transcripts |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_FAMILY_AND_REUSE_TABLE.csv` | 45 content families, Shorts as cuts of long scripts |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_SCRIPT_METRICS.csv` | Per-script word and structure metrics |

## Phase 6: timing and layer reconciliation

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_LAYER_RECONCILIATION.md` | Brain vs campaign vs deep pass; pacing conflict resolved by definitions |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_ALIGNED_TIMING_TABLE.csv` | 44 videos: shots, events, narration pace on one definition set |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_BRAIN_VS_CAMPAIGN_SAME_VIDEOS.csv` | 8 videos in both layers |

## Phase 7: science and physics visuals (125 frames)

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_SCIENCE_VISUAL_PASS.md` | First pass and holdout, 24 long videos |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07b_SCIENCE_VISUAL_PASS_20_LONG.md` | The other 20 long videos |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07c_SCIENCE_VISUAL_PASS_SHORTS.md` | Shorts |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_SCIENCE_VISUAL_CODING_SAMPLE.csv` | Coding, first set |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_SCIENCE_VISUAL_CODING_HOLDOUT.csv` | Coding, holdout |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07b_SCIENCE_VISUAL_CODING_20LONG.csv` | Coding, 20 long |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07c_SCIENCE_VISUAL_CODING_SHORTS.csv` | Coding, Shorts |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_SAMPLE_FRAMES.csv` | Frame list |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_HOLDOUT_FRAMES.csv` | Frame list |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07b_SAMPLE_FRAMES.csv` | Frame list |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07c_SAMPLE_FRAMES.csv` | Frame list |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07c_SHORTS_INVENTORY.csv` | Which Shorts have media and ASR |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/phase7_frames/` | Contact sheets and frames, first set |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/holdout7/` | Contact sheets, holdout |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/phase7b_frames/` | Contact sheets, 20 long |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/phase7c_frames/` | Contact sheets, Shorts |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/phase7b_asr/` | Local whisper transcripts, 20 long videos |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/phase7c_asr/` | Local whisper transcripts, 24 Shorts |

## Phases 8 to 10: status, audio, validation

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_10_STATUS_VISUAL_SCIENCE_ASSET_AUDIO_VALIDATION.md` | Honest per-phase status |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/09_AUDIO_LEVELS_88.csv` | Machine loudness, peak and silence for 88 files (not listening) |

## Evidence

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/11_EVIDENCE_REGISTER_PHASE5_13.csv` | Claim register with tier, source and recompute path |

## Ledgers (new)

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/` | 20 long and 24 Shorts: per-video ledgers and keyframes |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/INDEX.csv` | One row per video |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/ALL_SHOT_LEDGER.csv` | All 719 shots |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/ALL_EVENT_LEDGER.csv` | All 2,160 events |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/review_sample/REVIEWED_SAMPLE.csv` | 60 measured shots viewed and coded (subject, setting, function, boundary true or false) |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/review_sample/README_REVIEW_SAMPLE.md` | Method, results (50 of 60 boundaries true; end card in 20 of 20 long videos), limits; sheets `long_1-5.jpg`, `short_1-5.jpg`, `endcards_long.jpg`, `endcards_short.jpg` |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_pilot_9VG0yqq_PHM/visual_ct_scan_report.md` | CT_SCAN pilot on one video (every frame measured, 104 change windows viewed) |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_pilot_9VG0yqq_PHM/per_frame_table.csv` | One row for each of the 3,893 frames |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_pilot_9VG0yqq_PHM/visual_event_ledger_ct.csv` | 104 change spans coded after viewing; `shot_ledger_ct.csv`, `state_intervals.csv`, `coverage.json`, `quality_gate.json`, `sheet_01-18.jpg` in the same folder |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_pilot_9VG0yqq_PHM/span_960_1679/SPAN_REPORT.md` | All 720 frames of a 30 s span viewed and checked at full resolution; sheets, `fullres_changes.csv`, `diff/` in the same folder |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_pilot_9VG0yqq_PHM/ALL_FRAMES_VIEW_REPORT.md` | All 3,893 frames viewed and differenced at full resolution: result, corrections, limits; sheets in `span_0_959/`, `span_960_1679/`, `span_1680_3892/` |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_batch/BATCH_REPORT.md` | CT_SCAN machine stage on all 88 videos (measured, not viewed): per-frame tables, state intervals, residual runs; `BATCH_SUMMARY.csv` and one folder per video in the same folder |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ct_scan_batch/RUN_REVIEW_REPORT.md` | Viewed review of flagged residual runs (153 compact and mid, 36 control) and the two outlier videos; `run_review/REVIEWED_RUNS.csv` and sheets in the same folder |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/SMALL_ADDITIONS_ALL.csv` | The 74 real small additions (35 videos: 58 compact/mid pass, 16 scattered pass) with frame, PTS, bbox, shot_id; per-video copies in `small_additions.csv`; 18 videos without a ledger in `ledgers_small_additions_only/` |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/review_sample/endcards_long_other24.jpg` | End-card check for the other 24 long videos (24 of 24 show it) |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/scripts/review_sample.py` | Picks the 24-shot sample and builds the sheets; `review_sample2.py` adds 36; `review_sample_code.py` and `review_sample_code2.py` hold the coding |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/VALIDATION_vs_campaign.csv` | Per-video validation against the campaign ledgers |

## Scripts (recompute everything)

| File | What it is |
|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/scripts/` | All Python used; recompute commands in 12_CODEX_CLAUDE_WORKFLOW.md and ledgers_measured/README_LEDGERS.md |


## CONTINUATION (checkpoint 16, 2026-11-23): files added or rewritten

The v1 versions of rewritten files are kept beside them as `*_v1_*`. Stale before this continuation and now replaced: 13_FINAL_REPORT, 03 inventory and report, 02 availability, 05 playbook, 12 workflow, claim matrix (C02, C17), register (P05).

| File | What it is | State |
|---|---|---|
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/13_FINAL_REPORT.md` | START HERE: final report v2 (Phase 0 to 13 status, A to F, proof of work); COMPLETE as a report, research not finished | provisional |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/03_CORPUS_COMPLETENESS_REPORT.md` | Counts, live recount, layers by logical ID, v2 tiers | provisional (self-review) |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/03_CHANNEL_MASTER_INVENTORY.csv` | 92-row inventory v2 (layers, ASR status, tiers, article candidates) | provisional |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/03_ASR_VALIDATION.csv` | 88 ASR files checked for duration and identity | machine |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/live_channel_ids_2026-11-23.json` | live listing: 46 long + 46 Shorts | observed 2026-11-23 |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/what_if_xkcd_archive_2026-11-23.json` | 162 article titles from what-if.xkcd.com/archive | observed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/02_WHAT_IF_RELATED_FILE_REGISTER.csv` | 1,371 files with provenance attributes (rule-derived) | provisional |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_PHASE5_VERIFICATION.md` | Phase 5 rule links, families vs videos, era holdout | self-reviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_RULE_EVIDENCE_LINKS.csv` | rule to video ID and locator table | machine |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/05_MASTER_SCRIPT_PLAYBOOK.md` | playbook v0.2 (v0.1 kept) | self-reviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_PACING_CORRECTION.md` | pacing by definition, sample, source | self-reviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_STYLE_ANALYSIS_PHASE62.md` | Phase 6.2 style on 125 frames | self-reviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_STYLE_MEASUREMENTS_125.csv` | per-frame style measurements with frame references | machine |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/06_LEDGER_REVIEW_METHOD_AND_COVERAGE.md` | sampling method, 156 shots viewed (batch 4 added), failure modes | self-reviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/07_SCIENCE_CLAIM_CHECKS.md` | 10 physics claims recomputed | self-reviewed, not expert |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/08_ORIGINAL_ASSET_RECIPES.md` | original asset recipes and method rule | draft |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/09_AUDIO_ALIGNMENT_AND_LISTENING_PROTOCOL.md` | machine alignment and a listening protocol; listening BLOCKED | machine + draft |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/09_LISTENING_REVIEW_PACK.csv` | 4,439-row pack for a human listener | unreviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/10_VALIDATION_HYPOTHESES_AND_HOLDOUTS.md` | hypotheses H1 to H9 and checklist | self-reviewed |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/knowledge_base_draft/WHAT_IF_NEW_AI_START_PROMPT.md` | knowledge-base entry (14 documents + RULE_EVIDENCE_LEDGER.csv in the same folder) | draft |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/12_CODEX_CLAUDE_WORKFLOW.md` | Codex + Claude workflow v2 | design draft |
| `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/11_EVIDENCE_REGISTER_PHASE5_13.csv` | evidence register, 57 rows (P43 to P57 new) | self-reviewed |

## CONTINUATION 3 (checkpoint 17, 2026-11-23): files added or rewritten
| File | What | Review kind |
|---|---|---|
| `13_FINAL_REPORT.md` (v3; v2 kept as `_before_v3`) | status, counts, section H changes | self-review |
| `07_SC03_LIGHTNING_REWORK.md/.json`, `07_SCIENCE_CLAIM_CHECKS.md/.csv` (v2) | lightning reopened, 10 claims rechecked | same-model |
| `07e_TEN_EPISODE_PHYSICS_STUDIES.md`, `07e_EPISODE_CLAIM_CHECKS.csv`, `07e_EPISODE_SHEET_FRAMES.csv`, `phase7e_frames/` | the directive's ten episodes | sampled and viewed, same-model |
| `11_RULE_AUDIT_2026-11-23.csv`, `11_RULE_RECOMPUTE.json`, `11_RULE_COLOUR_160_FRAMES.csv`, `11_LEADING_SILENCE_88.json` | 23-rule audit | machine + self-review |
| `knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv` (+ audit columns) and revised KB documents | wording changes | self-review |
| `review_sample/REVIEWED_SAMPLE.csv` (156 rows), `06_LEDGER_REVIEW_METHOD_AND_COVERAGE.md` addendum | shot review batch 4 | one coder |
| `09_LISTENING_PRIORITY_ITEMS.csv`, protocol addendum | lines a listener should hear first | nobody has listened |
Older versions: `*_v1_*`, `*_v2prelight_*`, `13_FINAL_REPORT_v2_2026-11-23_before_v3.md`.

| `phase15_scene_coding/PROGRESS.md` | literal Phase 6.4 scene coding: tranche A (ten episodes, 260 shots) done; B and C pending |
