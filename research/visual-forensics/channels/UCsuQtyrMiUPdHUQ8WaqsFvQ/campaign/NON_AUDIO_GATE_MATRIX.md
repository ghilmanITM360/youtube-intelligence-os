# Primitive Education non-audio gate matrix (checkpoint J)
Status vocabulary: kit reference 13. All 15 videos stay VISUAL_ANALYSIS_PARTIAL. CT_SCAN_COMPLETE, FULL_AV_SIGNOFF and CAMPAIGN_COMPLETE are not awarded.

| Gate | Status | Evidence | Remaining operation |
|---|---|---|---|
| source_identity | PASS 15/15 | source_manifest.json, evidence/source_sha256.txt | none |
| full_temporal_overview | PASS 15/15 | tables/FULL_FRAME_MEASUREMENTS.csv, segments_v1.csv | none |
| candidate_shots_verified | PASS 15/15 | tables/state_ledger.csv | none |
| meaningful_state_timing | PASS 14, PARTIAL 1 (uIG2U_1xynQ) | campaign/gap_review | G0024, G0025 object identity; not determinable from pixels, owner or creator knowledge would settle it |
| motion_design_review | PASS 15/15 | coverage.json: all ACTIVITY frames now viewed; 675 frames added in tables/strip_frames.csv | none. Whole-sheet review scale stays small; viewed is not native-scale for every frame |
| native_art_review | PASS 15/15 for sampled key states | review/native_art_review.md | none required by gate |
| hidden-region coverage | PASS with stated limits | campaign/HIDDEN_REGION_AUDIT.md | none |
| creative_design_review | PARTIAL 15/15 | visual_ct_scan_report.md, tile scale plus sampled native | Native review of more states if owner wants it; not a defect found |
| production_blueprint | PARTIAL 15/15 | reconstruction_blueprint.md: prompts derived from descriptions, draft, not rendered | Render or generate from prompts: a production decision, no contract requires it per video |
| independent_review | PARTIAL 15/15 | same-family subagent plus primary spot-check | Review outside this model family not run; needs an owner-approved outside reviewer |
| visual_script_mapping | PARTIAL 15/15 | audio_visual_alignment.csv, ASR_UNCERTIFIED | Depends on listening: audio side BLOCKED |
| reconstruction_test, per video | NOT_APPLICABLE 15/15, corrected from stale PENDING | gate_corrections in quality_gate.json; brief section 5; ACCEPTANCE_RT_v1 | none per video |
| reconstruction_test, channel | PASS as bounded animatic conformance: RT_L1 attempt 5, RT_P1 attempt 6 | reconstruction/RT_*/attempt_*/RT_EVALUATION.md | Not source-level drawing quality, first-pass reproducibility or full-video production approval |
| Manual v2 unseen validation | Gap, not required | HELDOUT_EVALUATION.md addendum | Freeze a new protocol if owner wants it; LONG has 0 unseen sources |
| Off-device preservation | BLOCKED | LOCAL_ONLY_PRESERVATION_MANIFEST.txt; boot volume only | Owner names a destination, then copy and verify sha256 |
| Scheduled cycle | Launch and gate receipts only, no successful unattended research cycle | scheduler.log; tccd log below | None until there is executable work |

Audio, separate and BLOCKED: audio_human_listening 15/15, final_av_signoff 15/15, narration sync in both RT tests. ASR is not listening.

## Per video
| Video | Split | Format | Timing | Motion | Native art | Creative | Blueprint | Independent | Visual-script | RT per video | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qB_EKkMyuUE | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| IUur04eOd4A | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| 3AsDdMQr_nQ | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| f1vIzsTFrp4 | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| KyBWJPaF1KI | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| uIG2U_1xynQ | DEV | 9:16 | PARTIAL | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| RmTdnXHbI8s | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| W8AVd7RhTME | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| DekaeZPzTAQ | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| Nv4xJ_NsFdo | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| RM_KBLDLsnQ | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| xBJ6suQSt98 | HELD_OUT | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| 6YHva7Me2ls | HELD_OUT | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| C_jSOXP_XWY | HELD_OUT | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| 5gSIU30yiVs | HELD_OUT | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |

## Scheduler receipt
tccd log 2026-11-05 12:27:42Z: AUTHREQ_PROMPTING, service kTCCServiceSystemPolicyDownloadsFolder, responsible process the claude binary launched by launchd. A prompt nobody can answer unattended is consistent with the observed open() hang, and replaces the earlier TCC inference for that run. Hang-to-prompt link is INFERRED from timing; the prompt itself is MEASURED.
Fix: 15 sha256-verified copies in source_media (SOURCE_MEDIA_COPIES.json); evidence/source_path.txt points to them and source_path_original.txt keeps the original. No OS permission changed; no new scheduled job.

launchd receipts after the fix (scheduler.log):
- 2026-11-06T03:45:16Z PROBE source_media read OK (launchd context)
- 2026-11-06T03:45:16Z HOLD no executable non-audio work; waiting on owner for audio capability and off-device destination (see NON_AUDIO_GATE_MATRIX.md)
These show the gatekeeper reading a source copy in launchd context and holding with no model call. They are not a successful unattended research cycle.
