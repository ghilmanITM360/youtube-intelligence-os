# SECOND-PASS independent verifier brief — video 5umJ63d3rzQ "Brace For Impact." (Casual Finance)

You are an INDEPENDENT second reviewer. A first reviewer already wrote findings; they were only ~41% fully accurate on a prior video, so do NOT trust them. LOOK at the images yourself first, form your own reading, then compare.
ROOT = /Users/ghilmankhan/YIOS-local-audits/2026-10-24-5umJ63d3rzQ-deep-ct-scan
Write ONLY ROOT/agents2/OUT2_<NAME>.json (optional crops in ROOT/agents2/crops_<NAME>/). Touch nothing else (no source MP4, repo, other files). No installs, no network. Use python3 -I for JSON; Read tool for images. Venv python (cv2, numpy) ~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 may be used for bounded crops/contact sheets of source frames in ROOT/frames or evidence; decoding the source MP4 is NOT needed (read-only decode of a few frames is allowed only if evidence images are insufficient: /Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/Brace For Impact. - Casual Finance (720p, h264).mp4, 30fps, frame i has PTS (i+1)/30 s).

Video: 752.847 s, 1280x720, 30fps CFR, 22,583 frames. Flat off-white whiteboard explainer, stick-figure presenters, doodle props, third-party screenshots; mostly 1-frame hard replacements plus motion intervals.

## Inputs
For each first-pass shard N in your assignment: ROOT/tables/first_pass/FIRST_PASS_shard_N.json (keys shard, candidates, states, disputes; every record has 'id'; states also have 'id' = state_id), plus ROOT/agents/shard_N/{candidates,states,disputes}.csv, ROOT/evidence/<ID>.jpg, ROOT/disputes/SDxxx.jpg, state rep images ROOT/<rep_image>.

## What to do (per shard)
1. CANDIDATES: view each evidence image. Decide verdict yourself, then compare to first pass. Record: id, first_pass_verdict, second_pass_verdict, second_pass_state_boundary (YES/NO/UNCERTAIN), second_pass_type, agreement (AGREE|CORRECTED|UNVERIFIED), evidence (<=35 words: what you saw, frame numbers), final_decision (ACCEPT_FIRST|USE_SECOND|UNVERIFIED), confidence.
2. STATES: view the rep image. Re-judge objects, text, background, poses, and whether the state is merge/split/late-start. Record: id, agreement (AGREE|CORRECTED), corrections (list of {field, first_pass, second_pass_evidence, final}), merge_with_prev (true/false/UNCERTAIN), split_needed, true_start_frame (if you can show it), final_state_description (<=40 words), readable_text (only what you truly read; else UNREADABLE), confidence. Also record any text/number misread by first pass.
3. DISPUTES: each needs a verdict. Contiguous REAL_MOTION disputes inside one scene may be verified by viewing a representative subset (at least every 5th plus first and last of the run, state the sampled ids) — mark non-sampled ones sampled=false and inherit the run verdict. All non-motion verdicts must be viewed individually.
4. UNOWNED INTERVALS: the first-pass listed frame intervals owned by no draft state (see ROOT/CONTINUATION_HANDOFF.md checkpoint 4 and the OUT notes in the first-pass JSON). For each interval in your range, verify and return {start,end,description,hard_cut_in,hard_cut_out,confidence}.
5. ROLE-LEVEL ADDITIONS in 'extra': any missed overlays, micro-events, motion type labels (zoom/pan/scroll/draw-on/typing/pose-swap/fade), text reveals, character animation, codec artifacts the first pass missed.

## Rules
Never invent unreadable text. UNVERIFIED is acceptable. Label MEASURED (from numbers in CSVs) vs VISUALLY_VERIFIED vs INFERRED. No audience-retention claims. Output: {"name":..., "shards":[...], "candidates":[...], "states":[...], "disputes":[...], "unowned_intervals":[...], "extra":[...]}. One record per input row, same order. Final reply: counts, tallies of AGREE/CORRECTED/UNVERIFIED per section, and the 5 most consequential corrections.
