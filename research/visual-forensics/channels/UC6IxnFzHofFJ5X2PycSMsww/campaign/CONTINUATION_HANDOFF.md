# xkcd What If campaign — continuation handoff (updated 2026-11-04T15:50Z [corrected; earlier hand-typed time was wrong], checkpoint E)

Read first: campaign/CAMPAIGN_GOAL_v1.md, CHANNEL_PRODUCTION_MANUAL_v0.2.md (v0.1 kept), HELDOUT_PROTOCOL_v1.md, HELDOUT_EVALUATION.md, IMAGE_READ_INTEGRITY_NOTE.md, campaign_matrix.csv.

## State
- Census: 45 long / 46 Shorts / 0 live / 91 unique (snapshot 2026-11-04T01:43:22Z).
- ALL 32 selected videos built (27 dev + 5 held-out): every frame measured, every segment classified by a transcript-audited sonnet reviewer (all sheets opened) except wBLVmEZV2Oc (primary-only annotations), primary 0.6-scale image spot-check recorded on 26/32 videos (others: validator + transcript audit only, see each review/primary_spotcheck.json). Status per video VISUAL_ANALYSIS_PARTIAL; listening BLOCKED.
- Dense-strip pass: 34 long activities of the 22 earlier dev videos re-reviewed (campaign/strip_review); 16 hidden internal cuts; 1 contradiction corrected (-1-ldW4kpLM G0118). 12 strips of 5 newer dev videos + 18 held-out strips NOT re-reviewed.
- Held-out: PARTIAL PASS (Shorts 18/18 quantitative; long rhythm Q1–Q3 failed v0.1 ranges; opening 'typed question' detail failed). See HELDOUT_EVALUATION.md.
- Reconstruction test RT1: PARTIAL (spec-only worker; grammar reproduced, rhythm too dense, object detail missing) — reconstruction/RT1/RT_EVALUATION.md.
- Publication: branch research/xkcd-whatif-visual-forensics; checkpoints A 591c2d84, B b2de413b, C 32471d3e, D 5a233d56, E (see PUBLICATION_E.json).

## Exact next operations
1. Acquire lock (vf_lock.sh acquire with VF_LOCK_DIR=~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock); check usage (5h <85%, weekly <90%).
2. Expansion batch justified by held-out long failure: select 3 NEW unseen long videos (prefer 2025–2026, from census.csv rows not in selection_v1.json; need local sources — acquisition not authorised, check ~/Downloads/videos in mp3/xkcd Channel first) as held-out-2 for manual v0.2; run xk_ingest.sh → xk_prep.sh → reviewer → xk_process.sh → xk_heldout_eval (point at v0.2 ranges).
3. Reconstruction test: fresh worker gets manual v0.2 §9 + an original beat list, renders a 20–30 s ORIGINAL animatic (Python/ffmpeg drawing), then run the same measurement pipeline on it and compare rhythm/device rules. Do not claim reconstruction-tested before this exists.
4. Re-review remaining strips (30) with campaign/strip_review/BRIEF_strip_rv1.md pattern.
5. Manual v0.3: relax R4 opening rule (question card typed / scaled-up / present at frame 0), add held-out evidence, 'landscape panel in upper half of 9:16' Shorts layout (Ny9m2l6h478).
6. Publish next checkpoint via `python3 -I scripts/xk_publish.py <X> --push`; verify seal via gh api.

## Known limitations
- No audio listening capability (campaign/AUDIO_LISTENING_CAPABILITY.json).
- Activity in-between frames sampled; holds verified by measurement + settled frame only.
- Reviewers are the same model family (sonnet subagents); primary image spot-checks on ~2/3 of videos (see each review/primary_spotcheck.json; some state "NO primary image spot-check").
- Barely Evolved lock dir ~/YIOS-local-audits/barely-evolved/.be_writer_lock names pid 4391 which was not running at 2026-11-04T01:50Z; not touched (other stream).
- (old) Session d2a98830 paused at 2026-11-04T04:40Z: 5h usage 87% (>=85% checkpoint rule), weekly 78%. Background jobs still running at pause: scripts/xk_ingest.sh (held-out ingest) and scripts/xk_prep_loop.sh (brief generation) — measurement-only, safe to let finish; check ingest_progress.txt. Lock released.
- Reviewer error rate is not zero: primary found 2 classification errors in jVy3qd70AqU (zoom direction; pop-off vs camera) and 1 in -1-ldW4kpLM via strips.
- RT1 done: RECONSTRUCTION_TEST_PARTIAL (reconstruction/RT1/RT_EVALUATION.md); v0.3 §9 must add event budget (~0.33–0.5 events/s) and object-detail rule, then RT2.
- RT2 (manual v0.3 §9, fresh worker): PASS on all measured rhythm checks + device grammar (reconstruction/RT2/RT_EVALUATION.md). Not tested: narration sync, long-form structure, 9:16 re-layout. Manual v0.3 written (campaign/CHANNEL_PRODUCTION_MANUAL_v0.3.md); because held-out videos now inform v0.3, a NEW held-out set is needed to test it (handoff step 2).
- Held-out-2 (JqFSGkFPipM, UQgw50GQu1A, r7B0MzvwDcA) done: v0.3 scored 30/33 (campaign/HELDOUT_EVALUATION_v2.md); manual v0.4 written with the 3 narrow fixes. Next: held-out-3 (3 new long, prefer 2026: FYoHYq8VRt0, TFhrRrRdUbA, 4ZVtHknKuvg) to test v0.4; ebur128 for the other 9 sources (only 23/35 captured); RT3 long-form structure test (title card + end card) and a 9:16 Short re-layout test.
- RT3 long-form structure PASS (reconstruction/RT3/RT_EVALUATION.md); object-detail density still weak in renders.
- Session d2a98830 stopped 2026-11-04T16:39Z at weekly 89% / 5h 78% (90% weekly no-new-reviewer rule). Checkpoint H f2187c44. Lock released.
- 2026-11-04T17:22:47Z held-out-3 started (HELDOUT_PROTOCOL_v3.md pre-registered before ingest). All 3 ingested+measured; 19/19 evaluated checks PASS (HELDOUT_EVALUATION_v3.md). FYoHYq8VRt0 fully reviewed+built (reviewer dir rvH3_* symlinked as rv1_*; G0058 CSV quoting fixed via primary_corrections.csv; xk_correct.py now drops overflow cells). NEXT: reviewer for TFhrRrRdUbA (18 sheets) and 4ZVtHknKuvg (22 sheets) using existing briefs, then symlink rv1_<id>, spot-check, xk_process.sh, add Q2 + qualitative to v3 evaluation. Stopped at 5h 85% / weekly 90%.
- 2026-11-04T17:24:15Z checkpoint I 97dde04c published (1082 files, 0 mismatches, seal verified via gh api). Lock released. Resume after 5h reset 2026-11-04T20:00Z; weekly 90% (CLAUDE.md hard stop 95%).

## Update 2026-11-05 (checkpoint J)
- TFhrRrRdUbA and 4ZVtHknKuvg reviewers (rvH3) done, spot-checked, processed. HELDOUT_EVALUATION_v3.md FINAL: 21/21 quantitative PASS, all evaluated qualitative rules PASS; caveats on hold floor (4ZVt 1.17 s) and R2 colour wording.
- xk_validate_review.py patched to accept rv1->rvH* symlink write paths.
- Next: manual v0.5 (R2 colour note, 2026 hold-floor review), re-review of 30 remaining strips, 9:16 Short RT, Phase 7 knowledge links. Weekly usage ~92% at this checkpoint; resume after weekly reset 2026-11-06T22:00Z.

## Update 2026-11-05T17:01:42Z (checkpoint N) — session d2a98830, owner-directed run to 100 % weekly (owner override of 95 % rule, 2026-11-05)
- Held-out-4 (protocol v4 sha c5cc516a…; oTzW-mTQd5w, s3oLIDaElaE, qu8nx1qUwEU): FINAL 20/23 quant (all 3 fails oTzW: continuous-journey rhythm), 27/27 qual. v0.5 2026 hold claim falsified → manual v0.6.
- Held-out-5 (protocol v5 sha c24b3249… + addendum; Z_xJ40QXu7Q, IdlQsjq5vKo, p2M8Y0z9Rl0): FINAL 21/21 quant, qual PASS; title-only story-type predictions substantive 1/3 → manual v0.7 demotes the story rule to a descriptive n=1 note; adds short blurred scale-reveal zoom device.
- Loudness: ingest's ebur128.txt lacks Summary for heldout3+ (ffmpeg -v error); always run scripts/xk_loudness.sh after ingest. heldout3_quant.csv was regenerated once and Q2 restored from HELDOUT_EVALUATION_v3.md (21/21).
- Checkpoints: L 6bae7cdf24810b906ece42322a07f050fc3f8d71 (1240 files), M d6b006ff6b2b3e30e90003ee2739bd59a188c56a (1279), N 87a757751bcc18ab9eef364bffedc7002240c0cc (1337); all readback 0 mismatches, seals match, 0 media.
- Reviewer scratch dir /private/tmp/claude-501/scratch unchanged (no new deviations).
- Next: population measurement-only run on the 20 remaining local long videos against frozen v4 ranges (pre-register before ingest); re-review 30 strips; 9:16 RT; Phase 7 links.

## Update 2026-11-05T19:15Z (checkpoint O published 2f0f1293ec0566a6f70803ff81eefe197e85a41b; session ea35c26f continuing campaign under token 70E8A861…; heartbeat renewed, prior holder pid 45018 dead)
- Population-6 prep completed this session (last 4 preps + loudness 20/20 + source sha 20/20 verified). Quant: 116/120 = 96.7 % PASS (frozen ≥90 %); 4 FAIL (UXA-Af-JeCE Q3 2.71 s; aIIBBj6KR-Y Q3 2.96 s; jgafb8G7i4o Q7 HOLD 231 f; DiWFXv9N0Vs Q7 ACTIVITY 1 f). Q2/qualitative NOT_EVALUATED. See campaign/HELDOUT_EVALUATION_v6.md. 21 Shorts in the corpus are narration excerpts of Pop-6 longs (text-level exposure). Manual unchanged (v0.7).
- Pop-6 per-video tables are NOT in checkpoint O (publisher only includes built videos): local-only under videos/<id>/ for the 20 ids in selection/selection_v6_pop6.json; sources are in ~/Downloads/videos in mp3/xkcd Channel (same Mac, not off-device backup). Hashes: campaign/source_hashes_all_2026-11-06.json.
- RT4_916 portrait Short: acceptance criteria frozen 19:09:06Z (reconstruction/RT4_916/ACCEPTANCE_CRITERIA_RT4_916.sha256) before render; attempt 1 worker launched.
- Strip re-review rv2: 31 strips of 9 videos (JcXpCyPc2Xw 11, lLlwvmu1ZeA 6, rGZ6TsXvi8E 6, BO8rOs05v48 3, WH4g1ptJ-70 2, 9VG0yqq_PHM, BnGqPxnQh9A, r7B0MzvwDcA 1 each) in campaign/strip_review/strip_tasks_rv2.csv; reviewer launched, output strip_rv2/strip_annotations.csv (validate before integrating).
- Phase 7: no authoritative xkcd-specific definition found; docs/Phases.md Phase 7 = Opportunity Engine (not requested; not started). 'Phase 7 knowledge links' needs owner clarification.
- Next: when RT4 attempt 1 returns → measure (xk_segment/xk_measure + xk_rt_eval on RT4_916/attempt_1), view sheets, score vs frozen criteria; when strip_rv2 returns → validate rows/format, compare with prior, record corrections; then checkpoint P, release lock.

## Update 2026-11-05T19:35Z (checkpoint P)
- strip_rv2 done: 31/31 strips, CONFIRMS 21 / REFINES 10 / CONTRADICTS 0, 16 internal cuts (campaign/strip_review/STRIP_RV2_SUMMARY.md). Not integrated into ledgers; transcript image-read audit not run.
- RT4_916 attempt 1: RT4_916_PASS_PORTRAIT (reconstruction/RT4_916/attempt_1/RT_EVALUATION.md); frozen criteria sha a27f4b41…; only 8 frames viewed; mp4 local-only (sha 8e63c969…). Not a long-form or audio claim.
- Phase 7 links: unresolved scope, owner clarification needed (repo Phase 7 = Opportunity Engine, not started).
- Remaining non-audio work: (a) optional xk_validate_review.py audit of strip_rv2 transcript; (b) integrate rv2 refinements into ledgers if owner wants; (c) full-frame review of RT4 + narration sync need audio/more evidence; (d) Phase 7 scope. Lock released at checkpoint P.
