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

## BLOCKER at 2026-11-05T04:38:06Z (scheduled worker, held-out step 8)
pe_prep.sh xBJ6suQSt98: pe_segment.py hung in kernel open() on the source MP4 (sample: cv::VideoCapture -> avpriv_open -> __open, 0.18s CPU for >10 min). Plain `head -c 16` on the same file also blocks; ls/stat work. Diagnosis (INFERRED): macOS TCC privacy gate on ~/Downloads for this unattended process tree; all 4 held-out sources live under ~/Downloads/videos in mp3/PrimitiveEducation-MP4/. Stuck processes killed; no outputs written (no segments_v1.csv, no sheets, no brief) for xBJ6suQSt98. Nothing else touched; ledger unchanged; frozen protocol hashes re-verified OK.
OWNER ACTION NEEDED (one of): grant Downloads/Full Disk Access to the scheduler's process chain (launchd -> claude -> python/ffmpeg), OR copy the 4 held-out MP4s to durable storage outside Downloads (verify SHA-256 against videos/<id>/evidence/source_sha256.txt) and update source_path.txt.
Worker guard: before pe_prep, test readability with a bounded probe, e.g. ( head -c 16 "$(cat videos/<id>/evidence/source_path.txt)" >/dev/null ) & sleep 8; if still running -> BLOCKED, kill, checkpoint, exit. Never wait on an unbounded open().
Exact next operation unchanged: held-out xBJ6suQSt98, 6YHva7Me2ls, C_jSOXP_XWY, 5gSIU30yiVs via steps 1-5, then evaluation, then reconstruction (step 9; no beat list/reconstruction plan file exists yet).

## Recheck at 2026-11-05T12:54:40Z (scheduled worker)
Bounded probe (head -c 16, 6 s cap) on all 4 held-out sources: all BLOCKED (same ~/Downloads paths). No stray readers left. mdfind shows no copy outside ~/Downloads; no external volumes. Usage five_hour 0.02, weekly 0.78. No prep, no reviewer, no ledger/publication change. Blocker and OWNER ACTION above still apply; exact next operation unchanged.

## State at checkpoint H (2026-11-05T16:32:17Z, interactive session 85559743)
Held-out sources readable from the interactive session (TCC block applies to the unattended launchd chain only); source sha256 re-verified = ingest receipts. HELDOUT_PROTOCOL_v1.sha256 re-verified OK. Prep + native + stroke + enc-audit done for all 4 held-outs; native_art_review.md written for all 4.
Processed: xBJ6suQSt98 (rv1, 17/17 images once, 1 correction G0105), 6YHva7Me2ls (rv1, 21/21 once, 0 disagreements). Pending reviewers: C_jSOXP_XWY (2 sheets), 5gSIU30yiVs (4 sheets) - briefs ready.
Reconstruction: ACCEPTANCE_RT_v1 frozen (sha c0ee184e) before render. RT_L1 attempt_1 FAIL (C7 yellow 0.955, C8 stroke 16 px, V3/V6 title clipped), attempt_2 FAIL (C6 ink 0.068); attempt_3 in progress. RT_P1 not started (brief ready).
Next: finish RT_L1 attempt_3 eval; reviewers C_jSO, 5gSI (one at a time) + spot-check + pe_process; pe_reuse.py --include-heldout; pe_aggregate.py . heldout --include-heldout; HELDOUT_EVALUATION.md; RT_P1; publish I.

## State at checkpoint I (2026-11-05T18:39:53Z, interactive session 85559743)
Paused at five-hour 0.86 (gate 0.85), reset 2026-11-05T22:00:00Z, weekly 0.71. All 15 selected videos built, status VISUAL_ANALYSIS_PARTIAL. Held-out scored in HELDOUT_EVALUATION.md: measured 23/32 (LONG 14/16, SHORT 9/16), observed 14/16, reuse 3/3. Manual v2 written; v1 and protocol unchanged.
Reconstruction: RT_L1 PASS at attempt 5 (attempts 1-4 FAIL retained). RT_P1 measured 10/10 at attempt 5, V1-V6 NOT judged. Audio sync BLOCKED.
Evidence limit: sheet label hid bottom band (see HELDOUT_EVALUATION.md). RmTdnXHbI8s G0009 text "pervy neighbour" awaits a targeted row correction. ACTIVITY tiles not band-audited.
Storage: renders and media are local only; hashes in reconstruction/RENDER_SHA256_LOCAL_ONLY.txt. Off-device backup BLOCKED: no destination available (boot volume only, per the 2026-11-05 check).
Scheduler: unattended runs cannot read sources under ~/Downloads (TCC, inferred). No successful unattended research cycle is recorded. Its only full run so far exited on lock BUSY: that proves launch and duplicate prevention only.
Exact next operation: after reset and five-hour <0.85, open reconstruction/RT_P1/attempt_5/frames/sheets/SHEET_01..04 once each, judge V1-V6 into its RT_EVALUATION.md (on V6 FAIL: specific fix, attempt_6, re-measure with scripts/pe_rt_measure.sh). Then publish J. Do not create CAMPAIGN_COMPLETE on folder count; listening stays BLOCKED, no CT_SCAN_COMPLETE.
