# Primitive Education non-audio gate matrix (checkpoint K, acceptance reconciliation)
Status vocabulary: kit reference 13. All 15 videos stay VISUAL_ANALYSIS_PARTIAL. CT_SCAN_COMPLETE, FULL_AV_SIGNOFF and CAMPAIGN_COMPLETE are not awarded.

| Gate | Status | Evidence | Remaining operation |
|---|---|---|---|
| source_identity | PASS 15/15 | source_manifest.json, evidence/source_sha256.txt | none |
| full_temporal_overview | PASS 15/15 | tables/FULL_FRAME_MEASUREMENTS.csv, segments_v1.csv | none |
| candidate_shots_verified | PASS 15/15 | tables/state_ledger.csv | none |
| meaningful_state_timing | PASS 15/15 | campaign/gap_review; quality_gate.json gate_corrections | none. uIG2U_1xynQ G0024/G0025 identity stays UNKNOWN in the ledger; it affects naming, not onset f646 or cut f679 |
| motion_design_review | PASS 15/15 | coverage.json: all ACTIVITY frames now viewed; 675 frames added in tables/strip_frames.csv | none. Whole-sheet review scale stays small; viewed is not native-scale for every frame |
| native_art_review | PASS 15/15 for sampled key states | review/native_art_review.md | none required by gate |
| hidden-region coverage | PASS for the reviewed scope; 1672 tiles numeric only | campaign/HIDDEN_REGION_AUDIT.md, K addendum | none |
| creative_design_review | PARTIAL 15/15, declared limit only | visual_ct_scan_report.md; review/attention_hypotheses.md; review/attention_timeline.csv; review/state_composition.csv | none required. Limit: state review at tile scale, native sampled |
| production_blueprint | PARTIAL 15/15, declared limit only | reconstruction_blueprint.md: image and image-to-video prompt per state, measured layout, continuity locks, editor steps, QA | none required. Limit: prompts are drafts, not rendered per video |
| independent_review | PARTIAL 15/15, declared limit only | same-family subagent plus primary spot-check; gap reviewer | none required. Limit: same model family, sampled |
| visual_script_mapping | PARTIAL 15/15 | audio_visual_alignment.csv, ASR_UNCERTIFIED | Depends on listening: audio side BLOCKED |
| reconstruction_test, per video | NOT_APPLICABLE 15/15, corrected from stale PENDING | gate_corrections in quality_gate.json; brief section 5; ACCEPTANCE_RT_v1 | none per video |
| reconstruction_test, channel | PASS as bounded animatic conformance: RT_L1 attempt 5, RT_P1 attempt 6 | reconstruction/RT_*/attempt_*/RT_EVALUATION.md | Not source-level drawing quality, first-pass reproducibility or full-video production approval |
| Manual v2 unseen validation | Gap, not required | HELDOUT_EVALUATION.md addendum | Freeze a new protocol if owner wants it; LONG has 0 unseen sources |
| Off-device preservation | BLOCKED | LOCAL_ONLY_PRESERVATION_MANIFEST.txt; boot volume only | Owner names a destination, then copy and verify sha256 |
| Relocated source-read preflight | PASS | scheduler.log 2026-11-06T03:45:16Z | none |
| Full unattended research cycle | NOT_PROVEN | scheduler.log; tccd log below | Nothing to run; HOLD_NO_EXECUTABLE_WORK stays until an authorized executable task exists |

Audio, separate and BLOCKED: audio_human_listening 15/15, final_av_signoff 15/15, narration sync in both RT tests. ASR is not listening.

## Contract classification of every PARTIAL item (checkpoint K)
Locators: "brief" = the owner's 15-video campaign brief, "closure" = closure brief in CONTINUATION_HANDOFF.md, "ref" = visual-ct-scan references. The kit template has no independent_review or reconstruction_test gate; pe_finalize.py added both.

| Gate | Item | Class | Locator | Result |
|---|---|---|---|---|
| Creative | Attention and emotional hypotheses with timestamps | REQUIRED_EXECUTABLE, closed at K | ref 13 Creative gate bullet 1; ref 08 attention timeline; ref 02 phase I | The J check found 0 attention hits in 15 observation files. Added per video |
| Creative | Per-state composition coordinates and negative space | REQUIRED_EXECUTABLE, closed at K | ref 04 Composition | MEASURED in review/state_composition.csv |
| Creative | Object continuity, on-screen text, counterexamples | Required, already met | ref 13 Creative bullet 2 | asset_inventory.csv, ledger, observation Contradictions |
| Creative | Native review of more states | OPTIONAL | ref 13 Temporal asks native at ambiguous events, met by gap_review | Limit kept: tile scale |
| Creative | Improvement scorecards, fine-art parallels | OPTIONAL | ref 13 bullet 5; ref 12 | Not done |
| Blueprint | Image and image-to-video prompt per state | REQUIRED_EXECUTABLE, closed at K | ref 13 Creative bullet 3; ref 09 | J column named only event and time. Now start, event, end state, measured static region |
| Blueprint | Timeline, editor steps, QA, continuity locks | Required, closed at K | ref 13 Creative bullet 4; ref 09 | Continuity locks added. One table keyed by state replaces two prompt files |
| Blueprint | Per-video render | OUTSIDE_SCOPE | brief section 5; ACCEPTANCE_RT_v1 | Bounded channel tests only, RT_L1 and RT_P1 |
| Blueprint | Variants, new original storyboard | OPTIONAL | ref 09 Deliverables | Not done |
| Independent | Tracked second check | Required, met | brief section 3 | Reviewer, primary spot-check 15/15, gap reviewer |
| Independent | Outside-family reviewer | OPTIONAL | no contract line asks for it | Not a blocker; limit stated |
| State timing | uIG2U_1xynQ G0024/G0025 | REQUIRED_EXECUTABLE, closed at K | ref 13 Temporal; ref 03 "uncertain means partial" | Event verified. Identity UNKNOWN, reading INFERRED; KyBWJPaF1KI sibling is not independent |
| Visual-script | Audio side | REQUIRED_BLOCKED | ref 13 Audio gate | ASR overlap exists; listening capability absent |
| Off-device copy | Transfer | REQUIRED_BLOCKED | closure step 6; YIOS preservation policy | No destination; same-Mac copies are not a backup |

## Per video
| Video | Split | Format | Timing | Motion | Native art | Creative | Blueprint | Independent | Visual-script | RT per video | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qB_EKkMyuUE | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| IUur04eOd4A | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| 3AsDdMQr_nQ | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| f1vIzsTFrp4 | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| KyBWJPaF1KI | DEV | 16:9 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
| uIG2U_1xynQ | DEV | 9:16 | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | NOT_APPLICABLE | VISUAL_ANALYSIS_PARTIAL |
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
These show the gatekeeper reading a source copy in launchd context and holding with no model call. Preflight PASS, full cycle NOT_PROVEN: brief section 8 asks for registration and one supervised invocation, both recorded earlier; no research cycle has run unattended.
