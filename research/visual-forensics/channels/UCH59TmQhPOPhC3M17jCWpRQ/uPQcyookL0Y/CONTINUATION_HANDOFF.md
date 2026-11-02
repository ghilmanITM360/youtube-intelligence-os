# Barely Evolved uPQcyookL0Y — continuation handoff (checkpoint F)
Executor: Ghilmans-Laptop.local (user ghilmankhan, macOS 26.5.1 arm64), session af9bd28b. Lock: ~/YIOS-local-audits/barely-evolved/.be_writer_lock (separate from Casually Finance .vf_writer_lock, which was HELD by scheduled CF V006 shard 9 and untouched).
Workspace: ~/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan (external; frames/montages kept out of Git).
Source: ~/Downloads/videos in mp3/BarelyEvolved-MP4/The Worst Time in History to Be Born as a Human [uPQcyookL0Y].mp4 sha256 1416669f…c69d, 48,986,292 B; all 3 local MP4 hashes match registry.
Done (MEASURED): 14,647 frames decoded; CFR; per-frame metrics in FULL_FRAME_MEASUREMENTS.csv. Thresholds derived from this source (cf>=0.5 runs); Finance thresholds NOT reused (24 fps whiteboard; would flag most frames here).
Done (OBSERVED, sparse): reviewer_1 viewed 9 montages, 44 rows: HARD_CUT 36, SAME_SCENE_MOTION 6, TRANSITION 1, UNCLEAR 1. Orchestrator spot-checked A001, A002, B005 vs images: consistent. Reviewer transcript confirms 9 image reads + own file write. claude-mem note #7911 claimed otherwise and is contradicted by that transcript (claude-mem is auxiliary, not evidence).
NOT done: A037-A077 review; intra-state motion scan (states up to 29.5 s); object/text/camera/art domains; ASR; audio listening; semantic validation; native-frame review. Candidate tier-A "TRANSITION" labels are detector output; reviewer says A001 is zoom/darken within one scene (not a cut).
Brutal Punishments 4X3xd3MDZro: no local source registered/found; reconcile separately (not a blocker).
Gates: before heavy work check 5h usage (was 12%), weekly (63%, reset ~18:00Z), swap (~90% used), disk 98 GiB free. Do not take .vf_writer_lock.
## Checkpoint C update
reviewer_2 viewed N01-N09 (A037-A077): HARD_CUT 36, TRANSITION 4 (A040,A055,A073,A075), UNCLEAR 1 (A051). Transcript confirms 18 image results and its own writes; claude-mem note #7921 (same claim as #7911) is contradicted and is not evidence.
Combined 85/85 sparse montage-level: HARD_CUT 72, SAME_SCENE_MOTION 6, TRANSITION 5, UNCLEAR 2 (A051 = zoom into box interior, B005). Table: tables/review_verdicts_sparse_montage.csv. Detector tier-A multi-frame runs are not all cuts (A001 zoom/darken); draft states from cuts are therefore NOT validated.
## Checkpoint D update
Intra-state scan (v1_scripts/be_intra_state_scan_reconcile.py): 26 long states, 165 detector candidates (113 BURST, 29 STILL_ONSET, 23 MOTION_ONSET_AFTER_STILL), UNVERIFIED. Orchestrator viewed 4 bursts: real in-scene animation, not cuts. States reconciled against reviewer verdicts: tables/states_reconciled_v1.csv flags 13/86 states (merge decisions NOT made; originals immutable).
## Checkpoint E update
reviewer_3 (31 stratified bursts, 8 montages; transcript: 16 image results, own write): SCALE_OR_CAMERA_MOVE 13, HARD_CUT 5, OBJECT_ENTRY_OR_EXIT 5, FADE_OR_WIPE 5, TEXT_OR_GRAPHIC_CHANGE 2, CHARACTER_ACTION 1. Orchestrator viewed P02 and P07.
FINDING (CORRECTED in checkpoint F): see below; seq61/seq141/seq39 were already tier-B candidates (B003/B007/B001), only seq49 and seq113 were new. Likely mostly-white cards -> low pixel change. Shot count is a lower bound; draft states under-segment. Splits proposed in tables/state_split_proposals_unapplied.csv, NOT applied.
## Checkpoint F update
CORRECTION: checkpoint E overstated misses. B001/B003/B007 were already candidates (reviewed HARD_CUT); v1 states just were not split on tier-B. Genuinely new: seq49 (C013), seq113 (C032).
Second detector (v1_scripts/be_structure_pass.py + be_second_detector_candidates.py): 42 clusters; reviewer_4 (9 montages, transcript confirmed): SAME_SHOT_MOTION 29, HARD_CUT 7 (C009,C013,C014,C022,C026,C032,C034), TEXT_OR_GRAPHIC_CHANGE 6. Orchestrator viewed Q05,Q07. C034 contested.
states_v2_draft.csv: 98 states (12 splits from tier-B and C hard cuts), 0 gaps/overlaps, DRAFT_UNVALIDATED. v1 states untouched. 79 reviewer-labelled hard cuts total = lower bound.
## Next exact operation
1) Independent check of states_v2 (sample of boundaries both sides: view frames at each V boundary); 2) bounded intra-state review of remaining bursts (82 unreviewed) now relative to v2; 3) provisional ASR; 4) independent semantic check; 5) then mNLNb-Z4T0M. Verify EVIDENCE_SHA256SUMS_checkpoint_F first.
