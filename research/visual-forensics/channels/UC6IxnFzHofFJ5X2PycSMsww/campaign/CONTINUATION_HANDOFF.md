# xkcd What If campaign — continuation handoff (updated 2026-11-04T04:30Z, checkpoint D)

Read first: campaign/CAMPAIGN_GOAL_v1.md, selection/selection_v1.json, campaign/campaign_matrix.csv, campaign/CHANNEL_PRODUCTION_MANUAL_v0.1.md.

## State
- Census: 45 long / 46 Shorts / 0 live / 91 unique (snapshot 2026-11-04T01:43:22Z).
- Built (kit deliverables, VISUAL_ANALYSIS_PARTIAL, listening BLOCKED): 21 dev videos + TIDHee_Q5Gk if checkpoint D lists it. See per-video quality_gate.json.
- Remaining development: WH4g1ptJ-70, lLlwvmu1ZeA, BO8rOs05v48, 9VG0yqq_PHM (long), 35KZm1yiyIE (Short) — all PREPPED (briefs exist: videos/<id>/review_brief_rv1_<id>.md).
- Held-out (do NOT use for rule development): JcXpCyPc2Xw, BnGqPxnQh9A, Ny9m2l6h478, jVy3qd70AqU, rGZ6TsXvi8E — ingest running/queued (scripts/xk_ingest.sh in background; prep loop scripts/xk_prep_loop.sh writes briefs automatically).
- Publication: branch research/xkcd-whatif-visual-forensics, prefix research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/. Checkpoints A 591c2d84, B b2de413b, C 32471d3e (each readback 0 mismatches + GitHub API seal hash match). Media never published.

## Exact next operations
1. Acquire lock: `VF_LOCK_DIR=~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock ~/YIOS-local-audits/vf_lock.sh acquire xkcd-whatif-campaign <session> "<task>"` (if this session's lock is still held and the session is dead, use `recover` with proof).
2. Check usage (5h <85%, weekly <90%) before each reviewer.
3. For each remaining dev video in order WH4g1ptJ-70, lLlwvmu1ZeA, 35KZm1yiyIE, BO8rOs05v48, 9VG0yqq_PHM: launch ONE sonnet general-purpose subagent with prompt "Read the file <brief> and follow it exactly…"; on completion write review/primary_spotcheck.json (view one 0.6-scale sheet via scripts/xk_spot.sh <id> <NN> on alternate videos) and run `scripts/xk_process.sh <id> <agent_id>`.
4. Dense-strip pass for long ACTIVITY segments sampled with ≤6 tiles (e.g., YL2VNtus4xk G0010, 2LSyizrk8-0 G0022, mEUqVgGf4e0 G0064) — new tool needed (all frames of the activity at 1/8 scale), then targeted re-review.
5. Aggregate dev set (scripts/xk_aggregate.py . dev_final), update manual to v0.2 incl. era comparison (2023-24 vs 2026 long-form).
6. Held-out evaluation: process held-out videos with the same pipeline, then compare to manual rules WITHOUT editing rules first; record pass/fail per rule in campaign/HELDOUT_EVALUATION.md.
7. Reconstruction test: fresh worker gets manual §9 + one original beat list, renders a 20–30 s original animatic (e.g., HyperFrames or Python/ffmpeg drawing), evaluator compares timing/layout rules. Not yet started — do not claim reconstruction-tested.
8. Publish checkpoint via `python3 -I scripts/xk_publish.py <X> --push`; verify seal via gh api.

## Known limitations
- No audio listening capability (campaign/AUDIO_LISTENING_CAPABILITY.json).
- Activity in-between frames sampled; holds verified by measurement + settled frame only.
- Reviewers are the same model family (sonnet subagents); primary image spot-checks on ~2/3 of videos (see each review/primary_spotcheck.json; some state "NO primary image spot-check").
- Barely Evolved lock dir ~/YIOS-local-audits/barely-evolved/.be_writer_lock names pid 4391 which was not running at 2026-11-04T01:50Z; not touched (other stream).
