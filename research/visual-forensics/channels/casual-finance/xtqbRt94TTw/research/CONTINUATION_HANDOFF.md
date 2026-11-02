# Video 006 xtqbRt94TTw handoff
## Checkpoint A0 (2026-11-01, lock manual-v006, five-hour 44%)
Source verified: sha256 030a85ad…efa7a66 computed fresh, 1920x1080 h264 24fps, 827.583 s, aac. Workspace + source_manifest.json created. Measurement (v1_scripts/measure_all.py) started in background -> FULL_FRAME_MEASUREMENTS.csv.
Next exact operation: when measure.log shows frame count, run episodes/states/scenedetect/evidence scripts (adapt 1280x720 constants to 1920x1080), then shard + first reviewer wave.
venv python: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python
Thresholds in v1_scripts episodes_v2/build_evidence scaled x2.25 for 1080p; ring 150. Swap nearly full (600MB free) - watch memory.
Checkpoint A1: measurement 19,862 frames OK; 606 episodes; 484 scenedetect scenes. Evidence build started.
ring 300 (150 failed on long episode; partial images from failed run get overwritten)
## Checkpoint A (pre-review): 19,862 frames measured; 606 episodes; 766 candidates (160 SUB); 447 draft states (0 uncovered/0 overlap); 339 scenedetect disputes; 10 shards 77/~45/~34 each; evidence images verified present. Source sha 030a85ad… Next: first reviewer wave shards 1,3 (2 reviewers), then gate usage.

## Checkpoint B (2026-11-01, five-hour usage 83% => sealed, no new waves)
First-pass reviewers shard 1 and shard 3 COMPLETE; v1_scripts/validate_shard.py PASS for both (ids/order == csvs; 77/23/3 and 77/56/9).
Reviewer claims (not validated): shard1 CONFIRMED 66, RECLASSIFIED 9, NOT_A_CHANGE 2, MERGE_WITH_PREV 10; shard3 CONFIRMED 70, RECLASSIFIED 2, NOT_A_CHANGE 5, MERGE_WITH_PREV 30 (29 duplicate prompts follow merges).
Caveats: shard1 reviewer says four-person table scene f226-f300 ("EGG FIRST!" bubble) falls in a gap between S0006 (ends f225) and S0007 (starts f302) - not a draft state; S0000 blank 2-frame lead-in; some shard1 rep_images viewed via evidence tiles only.
Cost: 2 reviewers took five-hour usage 46% -> 83% (about 18% each at 1080p evidence). Use ONE reviewer per wave for V006.
Lock note: my first lock (pid 45916 was a short-lived shell, not the session) was legitimately recovered by another run at 19:14Z; re-acquired for sealing. Lesson: heartbeat can fail with NOT_OWNER; check status before relying on lock.
Pending: shards 2,4,5,6,7,8,9,10 (disputes heavy in 2,4,6). Not published to Git.
Next exact operation (after five-hour reset ~22:10Z): preflight gates, acquire lock, launch ONE reviewer (shard 2), validate with validate_shard.py, continue singly.

## Checkpoint C (2026-11-02, Machine A ghilmankhan, session ceaf5788; five-hour 17% after shard 2)
Shard 2 first pass COMPLETE: reviewer (general-purpose subagent, single wave) wrote agents/shard_2/OUT_shard_2.json; validate_shard.py PASS (77 cand / 41 states / 66 disputes; ids==csv). STRUCTURAL ONLY; semantic review not independently done.
Reviewer claims (unvalidated): CONFIRMED 60, RECLASSIFIED 8, NOT_A_CHANGE 8, UNVERIFIED 1 (SUB032), CODEC_ARTIFACT 0; disputes REAL_MOTION 65 / REAL_STATE_CHANGE 1 (SD004), all mapped to a candidate; states: 28 MERGE_WITH_PREV by independent file count (reviewer said 29), SPLIT_NEEDED 0. Reviewer says it viewed all 77+41+66 images natively (self-report, not audited); no native ffmpeg crops, tiny text from 960x540 frames.
Cost: one reviewer shard ~15% five-hour (2% -> 17%).
Known issues: tables/ledgers/KNOWN_ISSUES_LEDGER_v1.md (KI-1 f226-f301 table scene CONFIRMED as uncovered by any draft state; KI-2, KI-3 open).
Lock: token-owned, owner pid recorded dead at acquire (short-lived shell issue NOT fixed); heartbeat loop used.
First pass done: shards 1,2,3. Pending: 4 (in progress), 5-10. Not integrated. Not published to Git yet.
Next exact operation: validate shard 4, seal checkpoint D, continue shard 5 while five-hour <=60% and gates pass.

## Checkpoint D (2026-11-02, five-hour 28% after shard 4)
Shard 4 first pass COMPLETE; validate_shard.py PASS (77/34/77, 0 dup prompts) - STRUCTURAL ONLY. Reviewer claims (unvalidated): CONFIRMED 68, RECLASSIFIED 2 (EP0192 falling-bills overlay ~58 fr ending in hard cut f6829-6830 to chalkboard, SD148; EP0211 full replace one figure -> two-character dialogue), NOT_A_CHANGE 7; disputes REAL_MOTION 76 / REAL_STATE_CHANGE 1; states MERGE_WITH_PREV 17 (independently counted), SPLIT_NEEDED 0. Self-reported native views 77/34/77 (not audited). Cost ~11% five-hour. partial chunk files part_*.json kept in agents/shard_4/.
First pass done: shards 1,2,3,4. Pending 5-10. Not integrated; not published.
Next: shard 5 reviewer running (only 6 disputes), then 6.

## Checkpoint E (2026-11-02, five-hour 42% after shard 5)
Shard 5 first pass COMPLETE; validate_shard.py PASS (77/49/6, 0 dup prompts) - STRUCTURAL ONLY. Reviewer claims (unvalidated): CONFIRMED 61, RECLASSIFIED 13, NOT_A_CHANGE 3; MERGE_WITH_PREV 24 (independently counted), SPLIT_NEEDED 0 (reviewer flagged unowned frames f8412-8543 (EP0249, SD158-160) as three compositions instead). Self-reported native views 77/49/6. Cost ~14% five-hour.
KI-4 (systemic): independent scan shows 123 inter-state gaps totalling 3,116 frames (11 gaps >=60 frames) in the 447 draft states -> tables/ledgers/draft_state_gaps_v1.csv. Integration must account every frame; "0 uncovered" in checkpoint A was not contiguous coverage.
First pass done: shards 1-5. Pending: 6 (reviewer running, launched at 42%), 7-10. Not integrated; not published.
Next: validate shard 6, seal F; start another reviewer only if five-hour <=60% (each shard ~11-15%).

## Checkpoint F (2026-11-02, five-hour 57% after shard 6)
Shard 6 first pass COMPLETE; validate_shard.py PASS (77/40/66, 0 dup prompts) - STRUCTURAL ONLY. Reviewer claims (unvalidated): CONFIRMED 68, RECLASSIFIED 8, NOT_A_CHANGE 1; MERGE_WITH_PREV 11 (independent count; reviewer says stricter rule would give 17), SPLIT_NEEDED 0; 5 states carry GAP_COMPOSITION flags (gaps near f9380, f10070, f10741, f11269, f11325, f11110, f11478 - see agents/shard_6/OUT_shard_6.json). Self-reported native views 77/40/66; 6 native ffmpeg crops in agents/shard_6/crops/. Cost ~15% five-hour.
First pass done: shards 1-6. Pending: 7 (reviewer launched at 57%), 8, 9, 10. Not integrated.
Next: validate shard 7, seal G. Do not start shard 8 unless five-hour <=60% (will not be). Resume after reset ~20:40Z (local 01:40) with shard 8 then 9, 10, ONE reviewer at a time.

## Checkpoint G (2026-11-02, five-hour 72% after shard 7; no new reviewer)
Shard 7 first pass COMPLETE; validate_shard.py PASS (77/47/32, 0 dup prompts) - STRUCTURAL ONLY. Reviewer claims (unvalidated): CONFIRMED 68, RECLASSIFIED 5, NOT_A_CHANGE 4; MERGE_WITH_PREV 10 (independent count), SPLIT_NEEDED 0, GAP_COMPOSITION 1 (S0266: f12771-12801 hard cut to EBITDA table, EP0379/SD251). Self-reported native views 77/47/32. Cost ~15%.
FIRST PASS: shards 1-7 DONE (structural); PENDING 8, 9, 10 (8: 77/55/46; 9: 77/48/14; 10: 73/54/20). Not integrated; semantic review not independently performed. Known issues: tables/ledgers/KNOWN_ISSUES_LEDGER_v1.md (KI-1 confirmed, KI-2 open, KI-3 open, KI-4 systemic 123 gaps/3,116 frames).
Resume rule: when five-hour <=60% (reset ~20:40Z), preflight, acquire lock, ONE reviewer for shard 8, then 9, 10. Weekly 29%.
