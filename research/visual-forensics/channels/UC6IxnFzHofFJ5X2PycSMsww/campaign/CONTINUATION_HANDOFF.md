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
