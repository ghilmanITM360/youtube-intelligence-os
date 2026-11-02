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
