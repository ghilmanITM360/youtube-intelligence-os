# Primitive Education campaign — continuation handoff
Read: selection/selection_v1.json, campaign/campaign_ledger.csv, campaign/progress_log.txt. Files override memory. Workspace ~/YIOS-local-audits/primitive-education; channel UCsuQtyrMiUPdHUQ8WaqsFvQ (not Primate Economics). Publish branch research/primitive-education-visual-forensics via scripts/pe_publish.py (plumbing, never checkout).

## Per-video procedure (dev queue in selection order; final_status from ledger)
1. scripts/pe_prep.sh <id> (idempotent; requires INGEST_DONE; run scripts/pe_ingest.sh <id> first if missing).
2. Launch ONE sonnet general-purpose subagent: "Read the file <video>/review_brief_rv1_<id>.md and follow it exactly. All relative paths in it are under <video>/."
3. ~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 -I scripts/pe_native.py videos/<id> 3 ; pe_stroke.py videos/<id> ; python3 -I scripts/pe_enc_audit.py videos/<id>. Read one native crop; write review/native_art_review.md (OBSERVED/INFERRED/UNAVAILABLE, state which crops were and were not opened).
4. Read one sheet; compare rows; write review/primary_spotcheck.json (fields reviewer, sheet, rows_compared, disagreements, summary). Fix class-name slips only via review/primary_corrections.csv (seg,field,old,new,reason,evidence).
5. scripts/pe_process.sh <id> <agent_id>.
6. Every 2-3 videos: python3 -I scripts/pe_publish.py <LABEL> --push and verify PUBLICATION_<LABEL>_FINAL.json readback_mismatches==0 (run the preflight first: same command without --push, receipt PUBLICATION_<LABEL>_PREFLIGHT.json).

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

## Gate stop and non-audio closure brief (2026-11-05T18:45Z, interactive session 85559743)
Fresh read 18:45:12Z: five_hour 0.95 (gate 0.85), live reset field 1793916000 = 22:00:00Z, weekly 0.72, overage false. Remote HEAD = 4f4cfd64 (checkpoint I). Lock FREE before this note. launchd job loaded, not running. No analysis or reviewer started. Timer b6csmexrh (22:02Z) is session-bound, not persistent.
This brief from the owner supersedes the "exact next operation" above. Whoever holds the lock works it in order; re-read usage first; lock BUSY = no duplicate work. Every update's first line names Primitive Education.
1. PORTRAIT: judge RT_P1/attempt_5 sheets against frozen V1-V6 (open exact render frames where needed; run edge-ink check). FAIL: specific defect, versioned attempt_6, re-measure, keep failures, no relaxed criteria. Scope both RT results as "bounded animatic conformance", NOT source-level drawing quality, first-pass reproducibility or full-video approval.
2. OCCLUSION: pe_sheets.py label hides 8.1% landscape / 4.6% portrait. First list which finding classes could be affected (text, captions, CTA, object details, boundaries, end cards). Build a non-occluding sheet layout (labels outside the image, full frame visible) without touching original sheets. Source unavailable: use native frames/strips and state the gap. Targeted review of ACTIVITY tiles and remaining affected regions; 166 hold strips do NOT prove coverage for all 15. Record reviewed/unreviewed scope and corrections per video. Repeat accepted analysis only if needed.
3. CORRECTION: verify RmTdnXHbI8s G0009 "pervy neighbour" on native evidence, correct ledger and dependent findings traceably. New hidden text/CTA/captions: reconcile manual, held-out observations, gate implications. No silent rewriting of published results.
4. HELD-OUT: v1 scores unchanged. Means without dark holds = post-hoc diagnostic only, FAIL stays FAIL. Narration siblings are not independent. Manual v2 is not unseen-validated on these four. Check whether the actual campaign contract requires a fresh unseen v2 test: if required and an eligible independent source exists, freeze protocol then evaluate; else report the exact validation gap. Do not invent optional testing as a blocker.
5. GATES: establish from the actual contract what per-video reconstruction PENDING means. RT_L1/RT_P1 are channel-level, not per-video PASS. Execute required per-video tests or make an evidence-backed correction of a stale field. Deliver full non-audio matrix: PASS/PARTIAL/BLOCKED, evidence, remaining operation. Listening, sync and AV signoff stay separately BLOCKED; ASR is not listening.
6. SCHEDULER/PRESERVATION: Downloads TCC cause is still INFERRED. If scheduler operation is contractual, verify the actual scheduled-context error and fix narrowly via existing authorized paths; no silent broad OS permission changes. No successful-cycle claim without work/checkpoint/publication/release receipts. Complete hash manifest of local-only renders/source/dependencies; no off-device destination = only transfer BLOCKED.
7. PUBLISH: after worker writes finish, seal, verify exclusive ownership and remote base, normal push, full readback, no raw media, release own lock only.
Final report title: "Primitive Education — checkpoint [actual] non-audio closure report" (portrait, occlusion coverage/corrections, known text correction, held-out/manual limits, gates, publication receipts, exact remaining non-audio work). No CT_SCAN_COMPLETE/CAMPAIGN_COMPLETE without required evidence.

## State at checkpoint J (session 85559743, non-audio closure brief executed)
Read campaign/NON_AUDIO_GATE_MATRIX.md first. RT_P1 attempt 5 FAIL on V6, attempt 6 PASS (bounded animatic conformance). Hidden regions: HIDDEN_REGION_AUDIT.md. Gap review: gap_review/REVIEW_NOTE.md. Held-out addendum: HELDOUT_EVALUATION.md. Corrections live in videos/*/review/primary_corrections.csv; raw annotations are untouched.
Sources for any run: evidence/source_path.txt -> source_media copies. Do not read ~/Downloads unattended.
Exact next operation: none executable without a new capability or owner decision. campaign/HOLD_NO_EXECUTABLE_WORK makes the scheduler skip model calls; delete it to resume. Waiting on owner: (1) audio listening capability, (2) off-device destination, (3) optional: outside-family independent review, native review of more states, unseen v2 protocol.
Do not create CAMPAIGN_COMPLETE: audio gates are BLOCKED.

## State at checkpoint K (acceptance reconciliation, interactive session 85559743)
Supersedes earlier exact-next-operation notes. Required non-audio analysis is complete within declared coverage; all 15 stay VISUAL_ANALYSIS_PARTIAL. See campaign/NON_AUDIO_GATE_MATRIX.md for each PARTIAL's class.
Pending required items: listening, final AV signoff, narration sync, visual-script audio side (capability); off-device transfer (destination). Do not run new visual review to fill these.
HOLD_NO_EXECUTABLE_WORK stays. Delete it only when an authorized executable task exists. Preflight PASS; full unattended cycle NOT_PROVEN. J seal is historical: verify it against commit 7fd90bb459, since working files moved on.

## State at checkpoint L (publication integrity, interactive session 85559743)
Bookkeeping only: no analysis repeated, visual-coverage limits unchanged. See campaign/PUBLICATION_INTEGRITY_L.md.
Publisher: preflight run first (no --push, receipt PUBLICATION_<X>_PREFLIGHT.json), then --push (receipt PUBLICATION_<X>_FINAL.json). A label already on the remote is refused. Receipts of X are published by the next checkpoint, so PUBLICATION_L_PREFLIGHT.json and PUBLICATION_L_FINAL.json stay local until one exists. Test: python3 -I scripts/test_pe_publish.py.
Verify a seal against its own commit, not against working files. Ledger publication column names the last substantive checkpoint, K fa118b9b28.
Pending required items unchanged: listening, final AV signoff, narration sync, visual-script audio side, off-device transfer. HOLD_NO_EXECUTABLE_WORK stays.
Checkpoint M: corrects one sentence of the L report (PUBLICATION_INTEGRITY_M.md) and publishes the L receipts. No other change.
