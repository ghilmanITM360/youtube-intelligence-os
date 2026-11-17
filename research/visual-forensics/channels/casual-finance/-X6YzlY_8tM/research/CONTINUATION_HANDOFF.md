# Video 005 -X6YzlY_8tM handoff
## Checkpoint A (2026-11-01)
Source sha256 adff66768f5545cdd6f6bd2d2ddac9392c127adbc54fac4799b29f294b1463ec (== queue note). h264 1280x720 24fps CFR, 21,410 decoded frames (892.083 s), aac 44.1k.
Done: FULL_FRAME_MEASUREMENTS.csv (21,410 rows), 715 episodes, 831 candidates (116 SUB) + evidence/*.jpg (831, verified exist), 479 draft states, 250 scenedetect cuts (109 disputes), 10 shards in agents/.
Reviewers launched: shards 1-5 (first pass). Pending: 6-10.
Next exact operation: collect OUT_shard_N.json, validate row counts, integrate (v1_scripts/integrate_first_pass.py from V004 as base), second pass.

## Checkpoint A-2 (sealed at five-hour usage 97%; no new waves started)
First-pass reviewers shards 1-5 COMPLETE (OUT_shard_1..5.json; row counts and ids match csvs: 84/84/84/84/84 candidates, 62/60/46/31/42 states, 3/2/33/4/22 disputes). Shards 6-10 NOT started (unreviewed). Nothing integrated yet. Verdict counts are reviewer claims, not validated.
Reviewer-reported caveats (to handle at integration): states.csv misses compositions inside long episodes (gaps f730-784, f1236-1280, f4712-4762, f6237-6349, f6815-6913, f7041-7080, f9324-9388, f10412-10479); shard 3 states S0128,S0138-S0167 (34) have thin descriptions -> redo; shard 1 reviewed contact sheets not each image; EP0342 f10014-10015 ellipse dropout codec-vs-intentional UNVERIFIED; frames 7261-8063 micro-events = embedded interview footage (OTHER).
Shard 3 and 5 had large dispute lists; many SD cuts are motion of one object.
Scheduler: task yios-visual-forensics-machine-a registered (cron 7 */2 * * *), saved in Bypass permission mode by the app (owner should switch to Auto in the app). Writer lock: ~/YIOS-local-audits/vf_lock.sh.
Not published to Git (raw first-pass, not integrated). Local-only, recoverable via EVIDENCE_SHA256SUMS_checkpoint_A.
Next exact operation (after five-hour reset ~11:40Z 2026-11-01): launch shards 6,7 ... 10 (max 3-4 at a time, check usage between; 5 shards cost ~42% of window), then integrate_first_pass, second pass, gaps, DNA, validate, publish.

## Checkpoint B (2026-11-01 ~12:50Z, five-hour usage 65%)
First-pass reviewers shards 1-10 ALL COMPLETE. OUT_shard_1..10.json validated structurally (ids and order == csvs: 831 candidates, 478 states, 109 disputes; 0 mismatches). Sums: EVIDENCE_SHA256SUMS_checkpoint_B (10 entries).
Reviewer-claim totals (shards 1-10 candidates): CONFIRMED 572, RECLASSIFIED 234, NOT_A_CHANGE 22, UNVERIFIED 3 (incl EP0342? no: EP0665 shard10, shard5 1, shard6 1); states MERGE_WITH_PREV 200, SPLIT_NEEDED 1 (S0279). NOT validated, NOT integrated.
New caveats: gap f11880-12001 (EP0411 laptop capture) uncovered; shards 6-10 reviewers viewed rep stable frames inside evidence images, not each rep_image file; SUB071/SUB073 LOW; S0288-S0292 thin; S0435 "5 BILLION" first glyph uncertain; merge rule in shards 7-10 = additive/pose-only => merge (judgement); some prompts padded with generic style sentence.
Next exact operation: integrate_first_pass (V004 script as base) -> composition merge rulings -> gaps (listed here + A-2) -> targeted second pass (small waves, max 3, gate 85%) -> ASR align -> DNA/specs -> validate -> publish PARTIAL via plumbing.

## Checkpoint C (2026-11-01) - first pass INTEGRATED, unruled (integrated_v1/, v2_scripts/)
- Counts (integration_stats.json): 831 cands / 478 states / 109 disputes, 0 dup ids, 0 frame overlaps, 0 missing machine candidates. Verdicts 572/234/22/3 are reviewer claims.
- Frame ownership: 18,604 of 21,410 frames owned by states; 2,806 frames in 109 UNOWNED intervals (unowned_intervals.csv) = still unreviewed, not absorbed.
- composition_groups_DRAFT.csv: 278 draft compositions from 200 MERGE_WITH_PREV flags; 43 flagged merges bridge an unowned gap (non-adjacent) - rule on these specifically.
- MEASURED merge signal (merge_measured_signal.csv): all 200 flagged boundaries have low changed_frac (<0.30) = NOT CONTRADICTED. NEGATIVE CONTROL: 202/277 UNFLAGGED state starts are also <0.30, so this signal does NOT discriminate; it cannot confirm merges. Final rulings = PENDING_SECOND_REVIEW (use before/after native crops).
- Next: second-pass plan (priority 234 RECLASSIFIED, 22 NOT_A_CHANGE, 3 UNVERIFIED, S0279 split, EP0411 f11880-12001, 109 unowned gaps, 34 thin shard-3 states, 200 merge rulings) in waves <=3, start only when five-hour <=60%. Usage at this checkpoint 67%.

## Checkpoint C+ (plan only) — 2026-11-01
- Usage at read: 5h 69% (resets 16:59:59Z), weekly 46%; heavy wave NOT started (gate ≤60%). Disk 29 GiB. Lock FREE. Checkpoint C verified 0 failures.
- New: `v2_scripts/plan_second_pass.py` -> `v2_scripts/second_pass_plan.csv` (821 items, 11 reviewer shards R01-R11 of ≤80, waves of 3; seed 20261101; sha256 6a338a19…). Order: R01 = 25 UNVERIFIED/NOT_A_CHANGE + S0279, then 234 RECLASSIFIED, 109 disputes, 109 unowned intervals, 200 merge flags (43 gap-crossing ruled only after their intervals), 143 stratified 25% CONFIRMED sample (negative-control strata by machine_kind x confidence).
- Cost est. ~13% 5h per shard -> ~3 shards per window. Next exact operation: after reset, gate (≤60%), acquire lock, run wave 1 = R01,R02,R03 with native-res crops, one output file each, validate + seal checkpoint D.

## Checkpoint D (2026-11-01, sealed at five-hour usage 98%; owner said "continue till 95%")
- Wave 1 R01,R02,R03 COMPLETE: agents/second_pass/R0N/OUT_R0N.json (80 items each, ids/order == items.csv, schema OK, evidence files exist; EP0229 evidence_file lists two crops joined by ';'). Seal: EVIDENCE_SHA256SUMS_checkpoint_D (OUT, items, BRIEF only; crops not sealed). Verdicts are reviewer claims, NOT integrated, NOT applied to integrated_v1.
- Gate note: 60% gate overridden by owner chat instruction; wave ran at 72->98%.
- R01: CONFIRMED 54, NOT_A_CHANGE 22, RECLASSIFIED 2, UNVERIFIED 1 (EP0342 stays), NO_SPLIT 1 (S0279: no split in 12002-12006; Docs icon enters f12007). Disagreements 5 (SUB001 real ADDITIVE_ENTRY f416, EP0160 fade, SUB069/EP0665 -> NOT_A_CHANGE). Viewing: 7 native, 2 evidence jpg, 71 SAMPLED; EP0004-0024 on diff numbers only; reviewer exceeded native budget (mostly programmatic).
- R02: CONFIRMED 67, SPLIT 13 (EP0114,0117,0120,0148,0185,0188,0206,0211,0212,0214,0215,0229,0230); EP0212 -> FULL_REPLACE. 14 native, 66 evidence jpg. Pairs to merge downstream: EP0161/SUB009/SUB010, SUB011/EP0176, SUB012/EP0179. Some exact event frames unpinned (EP0188, EP0215, EP0230, EP0185).
- R03: CONFIRMED 77, RECLASSIFIED 2 (EP0254 -> FULL_REPLACE f6991, SUB055), NOT_A_CHANGE 1 (SUB061). 17 native, 63 evidence jpg. Satellite drift SUB051/053/054/056 = one slow drift ~8261-8408. Cut frames overstated in EP0247/0312/0411.
- Next exact operation: after reset (~17:00Z, read usage, do not assume), gate per owner instruction, acquire lock, wave 2 = R04,R05,R06 (brief: agents/second_pass/BRIEF.md; build items.csv from second_pass_plan.csv like R01-03), validate, seal checkpoint E.

## Checkpoint E (2026-11-01 ~17:35Z, scheduled run, 5h usage 1% at start)
- Wave 2 R04,R05,R06 COMPLETE (agents/second_pass/R0N/OUT_R0N.json; validated by v2_scripts/validate_wave.py: ids/order == items.csv, schema OK; negative test OK). Seal: EVIDENCE_SHA256SUMS_checkpoint_E (OUT, items, addendum, scripts). Reviewer claims, NOT integrated into integrated_v1.
- R04 (20 RECLASSIFIED-cand + 60 disputes): CONFIRMED 77, RECLASSIFIED 3 (EP0695 -> POSE_SWAP; SD010 and SD020 -> REAL_MOTION, true cuts are SD009 f5278 / SD019 f5310). Corrections kept: EP0667 cut f19814 (not 19809); EP0715 cut f21212 (not 21209); EP0703 scale ~1.35-1.4x; SD042 hard cut of embedded clip. 20 native, 60 evidence-jpg.
- R05 (49 disputes + 31 unowned): CONFIRMED 70, RECLASSIFIED 10 (all unowned intervals containing a hard cut = new state boundaries at f281,1281,1321,1341,2343,3380,3478,4762,5278,5550); 0 dispute disagreements. All unowned SAMPLED; cuts 1341, 3380 have no native frame. U5310-5340 rocket dropout unclear.
- R06 (78 unowned + merge S0003,S0004): CONFIRMED 57 (incl. both merges), RECLASSIFIED 23 (unowned with new composition/cut, state_boundary YES, change frames approximate). ALL SAMPLED (downscaled tiles, no full-res reads); small-element changes may be missed; merge rep_image not opened.
- Remaining plan items: R07 (rest of unowned/merges), R08-R10 merges, R11 + CONFIRMED sample. 5h usage after wave 2 not yet read; not published (unintegrated second pass).
- Next exact operation: read usage; if <=60% run wave 3 = R07,R08,R09 (build items.csv with v2_scripts/build_items_wave2.py, edit shard list), validate with validate_wave.py, seal F; then integrate second pass into integrated_v2 and publish PARTIAL.

## Checkpoint F (2026-11-01 ~18:10Z, manual continuation session c1b75aa6, 5h usage 20% at start)
- Wave 3 R07,R08,R09 COMPLETE; validate_wave3.py OK + negative test OK; seal EVIDENCE_SHA256SUMS_checkpoint_F (OUT, items, addendum_wave3, wave3 scripts; E seal unchanged and re-verified 0 failures). Reviewer claims, NOT integrated.
- R07 (80 merges): CONFIRMED 79, RECLASSIFIED 1 (S0200 new chalkboard text -> keep separate). 41 native pairs, 39 SAMPLED. Caveat: additive-element merges (S0068,71,75,84,85,87,90,159,160,161,167,197,204) confirmed as same composition; stricter boundary rule would flip them.
- R08 (80 merges): CONFIRMED 78, RECLASSIFIED 2 (S0289,S0291 zoom + new annotation -> keep separate, MEDIUM). 17 pairs viewed native (downsampled side-by-side), 63 SAMPLED at 480px. Gaps of 8-19 frames before some merges (S0242,S0257,S0289) not natively checked; 'hehehe' bubble f14642-14661 vs S0335-S0337 boundaries unchecked.
- R09 (38 merges + 42 candidates): CONFIRMED 78, RECLASSIFIED 1 (S0464 MEDIUM, rep jpgs only), UNVERIFIED 1 (EP0250 LOW). 20 merges native, 18 SAMPLED; 42 candidates from first-pass montages only (no new native).
- Remaining plan: R10 (80), R11 (21) -> wave 4. Then integrated_v2, gap rulings, production package, publish PARTIAL.
- Next exact operation: read usage; if <=60% run wave 4 = R10,R11 (python3 v2_scripts/build_items_wave3.py R10 R11).

## Checkpoint G (2026-11-01 ~18:25Z, session c1b75aa6)
- Wave 4 R10,R11 COMPLETE; validate_wave3.py OK + negative test OK; seal EVIDENCE_SHA256SUMS_checkpoint_G; E and F re-verified 0 failures. ALL 11 REVIEWER SHARDS R01-R11 NOW HAVE OUTPUT. Reviewer claims, NOT yet integrated.
- R10 (80 CONFIRMED sample): CONFIRMED 77, RECLASSIFIED 3 (EP0167 -> OBJECT_MOTION head shift; EP0253 -> OBJECT_MOTION continuous drift not 1-frame step; SUB058 -> OTHER, motion inside embedded meme clip). Only 7 INDIVIDUALLY_VIEWED_NATIVE; 73 from evidence jpg (embedded native crops). SUB039/042/044/046/047/026 are source-footage motion, not editing events. Flame flicker frames 9557,9592,9620,9627 exact.
- R11 (21 CONFIRMED sample): CONFIRMED 19, UNVERIFIED 2 (EP0381, EP0664). Corrections: EP0282 cut f8067; EP0713 caption f21186, pose f21189; EP0463 first frame only sparkle; EP0637 slide starts after first frame; EP0691 props centre-right; EP0531 also removes Rules paper+2 captions. Later frames of multi-frame motions (EP0207,402,597,304,166,029,538) not natively checked.
- CONFIRMED sample (R10+R11, n=101 of planned 143?) error rate to be computed in integration from plan counts; do not claim all 572 second-passed.
- Next exact operation: build integrated_v2/ (never overwrite integrated_v1): apply R01-R11 verdicts as versioned ledgers; rule on 109 unowned + 43 gap-crossing merges; frame-accounting partition + validators; then production package; then publish PARTIAL.

## Checkpoint H (2026-11-01 ~18:40Z) integrated_v2 built (integrated_v1 untouched)
- integrated_v2/: second_pass_ledger (821 reviewer claims), candidates_v2, disputes_v2, gaps_v2 (109 kept as separate segments, NOT absorbed), merge_rulings_v2 (200), composition_groups_v2 (284), frame_partition_v2, integration_stats.json. validate_v2.py PASS + 4 negative tests DETECTED. Seal EVIDENCE_SHA256SUMS_checkpoint_H.
- Frames 21410: states 18604, gap segments 2806, unaccounted 0, overlaps 0 (structural only, not semantic certification).
- Gaps: 76 continuation claims, 33 new-composition/transition claims; ALL 109 SAMPLED. Merges: 194 accepted, 4 keep-separate, 2 keep-separate because gap has new composition; 43 gap-crossing rulings made after gap review. Stricter rule on additive-element merges would flip many.
- CONFIRMED sample n=143 of 572 (not all second-passed): 137 CONFIRMED, 3 RECLASSIFIED, 3 UNVERIFIED (wrong-type 2.1%, unverified 2.1%). 429 candidates remain FIRST_PASS_ONLY.
- 13 R02 SPLITs held as SPLIT_PROPOSED_UNVERIFIED pending my own frame check.
- Next: verify 13 SPLITs, then production package (DNA, specs, ASR align, claim map, scorecard, cold-start, audio checklist, Roman Urdu report), verify full source sha, publish PARTIAL, release lock.

## Checkpoint J (2026-11-01 ~19:30Z) production package v2 + PARTIAL publication prep
- Source sha256 adff6676…1463ec re-verified (full). Machine ASR (Whisper base, 214 sentences) in asr/ ; alignment 54.2% within 0.25 s of boundary vs shuffled 31.5% (p95 35.5%); NOT heard.
- production/: PRODUCTION_DNA_AND_BLUEPRINT_v2.md, dna_statistics_v2.json, per_state_specs_v2.csv (478), composition_family_specs_v2.csv, asr_sentence_to_state_v2.csv, claim_evidence_map_v2.csv (50 numeric sentences, claims NOT externally verified), QUALITY_SCORECARD_v2.md, QUALITY_GATE_v2.json, COLD_START_TEST_v2.md (retrieval completeness PASS only), AUDIO_HUMAN_REVIEW_CHECKLIST_v2.md, OWNER_SUMMARY_ROMAN_URDU.md. Seal EVIDENCE_SHA256SUMS_checkpoint_J (34 files, 0 failures).
- Status VIDEO_005_PARTIAL_STRUCTURE_SECOND_PASSED. AUDIO_NOT_VERIFIED, AV_CERTIFICATION_BLOCKED, CT_SCAN_COMPLETE not awarded.
- Open: 429 candidates first-pass only; 109 gaps sampled only; 8 SPLITs reviewer-claim only; EP0342 and EP0250/EP0381/EP0664 UNVERIFIED; S0288-S0292, S0435 glyph, SUB071/073, padded prompts not individually resolved; colours/typeface/easing UNAVAILABLE.
- Next exact operation: next queue video position 6 xtqbRt94TTw (Casual Finance). Optional return to V005: native-res review of 109 gaps and 429 first-pass candidates, human listening.
