# Video 004 (0ll9rEtoRrs) "The World's Safest Market Is Breaking" - CT handoff
Status: FIRST_PASS_COMPLETE_UNINTEGRATED (checkpoint D, shards 1-10 all reviewed). NOT_CT_COMPLETE. NOT_CT_COMPLETE. AUDIO_NOT_VERIFIED. Identity HIGH_CONFIDENCE_NEEDS_REVIEW.
Source: see source_manifest.json (SHA-256 8fd0c2bf...5b73, 24,298 frames, 24 fps CFR, 1280x720; video stream 1012.4167 s = 24298/24, container 1012.52 s is audio length).
Done (MEASURED): FULL_FRAME_MEASUREMENTS.csv (24,298 rows), PySceneDetect 356 scenes (candidates only), episodes_v2 749, candidates 1,032 (749 EP + 283 SUB), 524 machine-draft states (0 uncovered/overlap), 148 unmatched scenedetect cuts as disputes, audio silencedetect (53 silences) and ebur128 summary.
Done (OBSERVED by reviewers, first pass): shards 1-4 = frames 0-8255 (~34%): 416 candidates (328 CONFIRMED, 78 RECLASSIFIED, 9 NOT_A_CHANGE, 1 CODEC_ARTIFACT), 221 states, 59 disputes (40 REAL_MOTION, 19 REAL_STATE_CHANGE). Output ids validated equal to shard CSVs.
Pending: shards 5-10 (frames 8287-end), second-pass reviewers, integration (SPLIT_NEEDED/MERGE_WITH_PREV flags: shard1 S0033 split, 36 merges; shard2 3 splits 1 merge; shard4 16 merges; shard3 7 merges), motion ledger, DNA, specs, human audio listening.
Known limits: reviewers had no evidence/ overlay tiles (build_evidence wrote frames/stable/ only); tiny text mostly not native-cropped. SUB088 appears in states.csv micro_events but has no candidate row. Intervals not in any draft state: shard2 f3681-3715, f4383-4436; shard3 f5025-5125, 5657-5694, 5730-5877, 6343-6358.
Scripts: v1_scripts (copied from Video 003; fps 30->24, source paths changed). Reuse: reviewer brief agents/BRIEF.md.
Next: run shards 5-10 (each ~104 candidates), check get_usage first; one shard costs ~9% of the 5-hour window.

Checkpoint C: shards 1-8 (frames 0-19085, ~79%) validated: 832 candidates (633 CONFIRMED, 179 RECLASSIFIED, 19 NOT_A_CHANGE, 1 CODEC_ARTIFACT), 426 states, 110 disputes. Reviewer limits: several reviewers saw stable frames only via contact sheets; ffmpeg -ss seek landed ~1 frame late for reviewer-made PRE strips; EP0544/EP0545 in states.csv but no candidate rows; many draft states flagged MERGE_WITH_PREV; unowned intervals (e.g. f16322-16397, f17607-17681, f18170-18221) need second-pass ownership. Late state starts noted: S0231/S0232, S0328, S0357, S0421 truncated.

Checkpoint D: all 10 first-pass shards reviewed and id-validated (see tables below via validator). Remaining: integration of splits/merges/unowned intervals, second-pass reviewers on disputed/low-confidence rows (not yet run), motion ledger, DNA, reconstruction specs, claim-evidence map, human audio listening, identity check against YouTube metadata. Shard 9/10 flags: S0466 split at f21628, S0438 should span 20108-20182, S0475 three compositions (22094-22227). Next action: write integrate_first_pass.py (states split/merge, unowned intervals), then second-pass A-D reviewers per Video 003 method.


## Checkpoint E (2026-10-31, usage 81-82%): evidence repair + structural integration
- Root cause of missing evidence/: build_evidence.py had no mkdir; cv2.imwrite silently returns False. Rebuilt exact-frame evidence for 227 priority candidates (190 RECLASSIFIED, 34 NOT_A_CHANGE, 1 CODEC_ARTIFACT, EP0544, EP0545) into repair/evidence/ (sequential decode, indices identical to original table). Other 805 candidates remain FIRST_PASS_REVIEWER_ONLY.
- integrated/: reviewed_candidates/states/disputes CSV, cross_shard_references, split_needed_pending, anomaly_ledger, integration_summary.json (structure only, NOT semantically certified).
- CORRECTION: draft states cover 21,216 of 24,298 frames; 144 unowned motion-run intervals = 3,082 frames (repair/unowned_intervals.csv). Earlier "no uncovered frames" was wrong.
- EP0544/EP0545 resolved (cross-shard ref). S0231/S0232 boundary 8725/8726 confirmed frame-exact.
- Still NOT done: second-pass reviewers (A: 34 NOT_A_CHANGE+codec+6 splits; B: reclassified; C: disputes/tiny text; D: unowned motion runs), motion ledger, DNA, specs, audio listening, YouTube metadata identity. Status stays NOT_CT_COMPLETE, AUDIO_NOT_VERIFIED, AV blocked. Unpublished.
- Next: if 5h usage <60%, launch second-pass shard A using repair/evidence/<id>.jpg.

## Checkpoint E re-verification (continuation session)
- Preflight: five-hour 85% (resets 2026-10-31T18:20Z), weekly 19%, context 9%, disk 14 GiB free, no extra usage enabled.
- Checkpoint E: 1,718 entries re-checked, 0 failures. No active reviewer processes. Repo shows only the 3 pre-existing untracked folders.
- Resource gate (<=60% five-hour) FAILED: second-pass A/B/C/D NOT started. 0 shards completed.
- Next: second-pass A (34 NOT_A_CHANGE + 1 CODEC_ARTIFACT + 6 SPLIT_NEEDED) using repair/evidence/ once gate passes.

## Second pass A (continuation, five-hour usage 0% at start)
- A1: 35 NOT_A_CHANGE/CODEC_ARTIFACT all AGREE (second_pass/A/A_decisions.csv). 3 viewed at native crop, 32 via PRE/STABLE contact sheets (downscaled), all repaired evidence.
- A2: 6 SPLIT_NEEDED checked on exact frames (second_pass/A/A_split_decisions.csv): 5 evidence-supported, S0033 CORRECTED (no split; infographic f1295-1323 is in an unowned interval).
- Splits not yet applied to integrated/ ledgers (final integration pending). Handoff hash differs from checkpoint E seal (appended notes).

## Second pass A/B/C/D complete (reviewer decisions only; ledgers NOT yet updated)
- A: 35 AGREE; splits 5 AGREE + S0033 CORRECTED_NO_SPLIT.
- B: 190/190 viewed: 177 AGREE, 13 CORRECTED (second_pass/B/B1-5_decisions.csv).
- C: 148/148 AGREE. 102 had repaired evidence viewed; 45 strips only (14 CONFIRMED candidates were never in the 227-image repair set); strips may lag a few frames.
- D: 144/144 classified (MOTION_IN_COMPOSITION 90, EMBEDDED_VIDEO 35, CONTINUOUS_ANIMATION 13, FADE_OR_TRANSITION 4, DISTINCT 1, UNCERTAIN 1), 3,082 frames; sparse 6-frame sheets. 13 gaps end on hard cuts (candidate boundaries). EMBEDDED_VIDEO for PDF/browser scrolls is INFERRED.
- Validators: coverage/duplicate/foreign-id negative tests pass. Audio AUDIO_NOT_VERIFIED. Nothing committed.

## Second-pass applied to ledgers -> integrated_v2/ (originals in integrated/ untouched)
- Script: v1_scripts/integrate_second_pass_v004.py (positive + 5 negative tests pass). Status SECOND_PASS_INTEGRATED_STRUCTURE_ONLY_NOT_SEMANTICALLY_CERTIFIED.
- States 524 -> 530 (S0089/S0097/S0116 x2, S0475 x3, new S0466P; S0466 start 21628 INFERRED). Child descriptive fields inherited from parent, pending review. Split IDs use .1/.2/.3 with parent_id.
- Unowned 144 -> 143 intervals (U129 consumed), 3,082 -> 3,012 frames; state frames 21,286. Total 24,298, no gap/overlap. Other 143 classified, NOT absorbed.
- Candidates: 1,032; 225 second-passed (212 AGREE, 13 CORRECTED); 807 CONFIRMED not second-passed (by design). Disputes 148 AGREE.
- Not done: merges (161 MERGE flags untouched), semantic certification, production DNA, audio, git.

## Production DNA started (PARTIAL)
- production/: dna_statistics.json, composition_family_specs.csv, PRODUCTION_DNA_AND_BLUEPRINT.md, OWNER_SUMMARY_ROMAN_URDU.md. Built from integrated_v2 (structure only). Script v1_scripts/build_dna_v004.py.
- UNAVAILABLE: shot count, ASR/claim map, scorecard, colours/typeface, per-state specs. Verdict VIDEO_004_PARTIAL_STRUCTURE_ONLY; CT_SCAN_COMPLETE not awarded.

## Checkpoint I (2026-11-01) — merge/split/gap reconciliation, sampled candidate review, ASR alignment, per-state specs
Starting point: Checkpoint H (229 entries; scope = second_pass/, integrated_v2/, production/, v1_scripts/ subset, NOT all raw research; verified 0 failures at start). Source SHA re-verified.
Done (all new files; originals `integrated/`, `integrated_v2/`, reviewer outputs untouched):
- `phaseA/merge_review_{1,2,3}.csv` (161 pairs: 158 MERGE_CONFIRMED, 3 UNCERTAIN S0022/S0035/S0056) + blind control `control_review.csv` vs `control_key.csv` (6/6 flagged same, 10/12 unflagged different, S0080/S0212 possibly missed merges, not applied).
- `phaseA/split_children/*.jpg` own review; corrections in `integrated_v3/split_child_corrections_v3.csv`; S0466 start f21628 observed.
- `phaseA/gap_dense_metrics.csv` + `gap_review_{1,2}.csv` (48 priority gaps / 1,060 frames; 6 measured hard cuts; embedded-video label reduced to 6 gaps/221 frames).
- Candidates: 201 stratified sample + 20 blind controls + 57 expansion rows (OBJECT_MOTION/TEXT_CHANGE/CHARACTER_ANIMATION): 258 independently viewed (218 OK, 22 type wrong, 18 no visible change); 549 remain first-pass only; 17 types updated in `final_type_v3` (`smp_*` columns hold provenance; originals unchanged).
- `integrated_v3/` (530 states, 370 compositions, 143 gaps with rr_* columns, 1,032 candidates). Validators `v1_scripts/integrate_v3.py` + `validate_v3.py`: positive PASS, 16 negative tests DETECTED.
- `phaseB/asr_sentence_to_state.csv`, `asr_alignment_stats.json` (192 historical Whisper-base sentences from origin/codex/casually-finance-forensic-research 2026-10-12; extracted copies in `phaseB/historical_asr/`; 74% sentence starts within 0.25 s of a state start vs 25% shuffled). Not listened to.
- `production/`: `PRODUCTION_DNA_AND_BLUEPRINT_v3.md`, `dna_statistics_v3.json`, `composition_family_specs_v3.csv`, `per_state_specs_v3.csv` (530), `AUDIO_HUMAN_REVIEW_CHECKLIST.md`, `OWNER_SUMMARY_ROMAN_URDU.md` (updated in place with Video 003 comparison).
Seal: `EVIDENCE_SHA256SUMS_checkpoint_I` (scope: handoff, integrated_v3, phaseA csv/key files + sheets, phaseB, production, v1_scripts; excludes `frames/`, source MP4 and earlier sealed files, which keep their own manifests).
Not done: 549 candidates, 95 gaps, 3 UNCERTAIN merges, possible merges S0080/S0212, gap-cut boundary ownership, colours/typeface, listening/AV, live identity check, claim map/scorecard of the video.
Next Video 004 step: second-pass the 549 first-pass candidates (risk-stratified, error-prone types first) and the 95 unreviewed gaps; or hand audio checklist to owner. Next queue video: position 5 `-X6YzlY_8tM`.

## Checkpoint J (2026-11-01) — all 807 first-pass CONFIRMED candidates second-passed
8 reviewers viewed the remaining 549 rows (`phaseA/cand_rest_review_{1..8}.csv`, sheets `cand_sheets_r/`). Totals over all 807: 749 CONFIRMED_TYPE_OK, 33 CONFIRMED_TYPE_WRONG, 25 NO_VISIBLE_CHANGE (15 LOW/10 MEDIUM). 25 types updated in `final_type_v3` (HIGH/MEDIUM only); `smp_*` columns keep provenance; originals unchanged. Rebuilt per-state specs and `dna_statistics_v3.json`; extended validator PASS, 8 negatives DETECTED.
Correction to Checkpoint I text: "549 first-pass only" is superseded; remaining Video 004 gaps are the 95 unreviewed unowned gaps, 3 UNCERTAIN merges, S0080/S0212 possible merges, native-resolution check of 58 flagged candidate rows, listening/AV, colours/typeface, live identity.

## Checkpoint K (2026-11-01) — all 143 unowned gaps re-reviewed
4 reviewers covered the remaining 95 gaps (1,952 frames; `phaseA/gap_dense_metrics_r.csv`, `gap_review_r{1..4}.csv`, sheets `gap_sheets_r/`); no measured >50% hard cut among them. Combined (143): MOTION_IN_COMPOSITION 99, CONTINUOUS_ANIMATION 13, STATIC 13, HARD_CUT_INSIDE 6, THIRD_PARTY_PLAYBACK 6, FADE 6; 29 limited_by_sampling; 13 gaps end on a new composition (U031, U035, U044, U059, U069, U073, U074, U077, U083, U088, U096, U120, U123): candidate boundary corrections, not applied. `integrated_v3/unowned_intervals_v3.csv` rr_* columns now cover all 143; validator PASS. Supersedes "95 first-pass only" in Checkpoints I/J text.
Remaining Video 004: ruling on absorbing gaps/boundary corrections, 3 UNCERTAIN merges, S0080/S0212, native-resolution check of 58 flagged candidate rows, listening/AV, colours/typeface, live identity, claim map/scorecard.
