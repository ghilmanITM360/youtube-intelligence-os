# Primitive Education campaign — continuation handoff
Read: selection/selection_v1.json, campaign/campaign_ledger.csv, campaign/progress_log.txt. Files override memory. Workspace ~/YIOS-local-audits/primitive-education; channel UCsuQtyrMiUPdHUQ8WaqsFvQ (not Primate Economics). Publish branch research/primitive-education-visual-forensics via scripts/pe_publish.py (plumbing, never checkout).

## Per-video procedure (dev queue in selection order; final_status from ledger)
1. scripts/pe_prep.sh <id> (idempotent; requires INGEST_DONE; run scripts/pe_ingest.sh <id> first if missing).
2. Launch ONE sonnet general-purpose subagent: "Read the file <video>/review_brief_rv1_<id>.md and follow it exactly. All relative paths in it are under <video>/."
3. ~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 -I scripts/pe_native.py videos/<id> 3 ; pe_stroke.py videos/<id> ; python3 -I scripts/pe_enc_audit.py videos/<id>. Read one native crop; write review/native_art_review.md (OBSERVED/INFERRED/UNAVAILABLE, state which crops were and were not opened).
4. Read one sheet; compare rows; write review/primary_spotcheck.json (fields reviewer, sheet, rows_compared, disagreements, summary). Fix class-name slips only via review/primary_corrections.csv (seg,field,old,new,reason,evidence).
5. scripts/pe_process.sh <id> <agent_id>.
6. Every 2-3 videos: python3 -I scripts/pe_publish.py <LABEL> --push and verify PUBLICATION_<LABEL>.json readback_mismatches==0.

## After dev set
7. python3 -I scripts/pe_aggregate.py . dev_final; write campaign/CHANNEL_PRODUCTION_MANUAL_v1.md (observed vs proposed separated).
8. Pre-register campaign/HELDOUT_PROTOCOL_v1.md from dev ranges BEFORE prepping held-out videos; run held-out through 1-5; record pass/fail in campaign/HELDOUT_EVALUATION.md without editing rules first.
9. Reconstruction test: fresh worker gets only manual + original beat list, renders an original animatic; evaluator compares frames to rules. A written blueprint alone is not a pass.
10. Touch campaign/CAMPAIGN_COMPLETE; scheduler disables itself.

## Limits
Listening BLOCKED_CAPABILITY. Never award CT_SCAN_COMPLETE/FULL_AV_SIGNOFF. Gates: five-hour >=0.85 checkpoint, weekly >=0.95 stop. Meter: scripts/pe_usage.sh.

## State at checkpoint G (2026-11-04T20:55Z)
DEV set complete: all 11 DEV videos built (VISUAL_ANALYSIS_PARTIAL); checkpoints E ac58cc33 (RmT, Dekae), F 29c11c39 (Nv4, RM_KBL). reuse_dev.json + aggregate_dev_final run. CHANNEL_PRODUCTION_MANUAL_v1.md and HELDOUT_PROTOCOL_v1.md frozen (campaign/HELDOUT_PROTOCOL_v1.sha256) BEFORE any held-out prep.
Read budget clause worked: reviewers opened each image once (RmT 19/19, Dekae 24/24, Nv4 10/10, RM_KBL 25/25 image results; 89k-154k subagent tokens each).
Exact next operation: acquire lock; for each held-out in order xBJ6suQSt98, 6YHva7Me2ls, C_jSOXP_XWY, 5gSIU30yiVs: pe_prep.sh <id> (adds briefs from template incl. read budget), one sonnet reviewer, steps 3-5; then pe_reuse.py with held-out (extend or run ad hoc, do not overwrite reuse_dev.json) and pe_aggregate.py . heldout --include-heldout; score every check in HELDOUT_PROTOCOL_v1 into HELDOUT_EVALUATION.md without editing v1. Then step 9 reconstruction (one landscape, one portrait; render + evaluate). Publish H after held-out.
First full scheduled worker ran 2026-11-04T20:31:26Z, found lock BUSY, exited 0 in 23 s (worker_last.json).
