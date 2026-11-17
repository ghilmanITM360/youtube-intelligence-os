# Visual forensics skill — invocation examples

`/visual-ct-scan` is a Claude Code skill invocation. It is not a compiled CLI. Plain-language requests that use the trigger words also load it, by routing on the skill `description`. Always quote the Machine B source folder with its trailing space: `"/Users/ghilmanislam360/Downloads/all channels videos data /"`.

| Need | Example request | Mode | What it may claim at most |
|---|---|---|---|
| Identify files | `/visual-ct-scan INVENTORY on "<source>.mp4": confirm registered Video ID and SHA-256.` | `INVENTORY` | identity and probe facts; no visual review |
| 1 fps overview | `/visual-ct-scan STRUCTURAL on Video_ID GNaBxt_zIRA: full-timeline 1 fps sheets plus scene-score candidates, using tools/pilot_extract.sh.` | `STRUCTURAL` | `full_temporal_overview` gate; video stays `VISUAL_ANALYSIS_PARTIAL` |
| Deep native-frame review | `Do a deeper visual analysis of uPQcyookL0Y: verify every candidate state with dense native-frame windows; separate cuts, camera moves, pose swaps and text events.` | `DEEP` | complete within declared visual coverage; no AV sign-off |
| Short CT scan | `CT scan Short HERcUJ6fIlw frame by frame: every state interval at source PTS/frame index, art + motion + ASR-only alignment, per-state prompts, quality_gate.json.` | `CT_SCAN` | `VISUAL_ANALYSIS_COMPLETE` only if every changed-state interval is authored at frame accuracy; audio stays `AUDIO_REVIEW_PENDING` until a human listens |
| Long-form adaptive CT scan | `CT scan long-form uPQcyookL0Y adaptively: 1 fps/state-detector baseline over the whole 488.8 s, native-frame windows on every candidate and ambiguous span, compressed hold log, explicit unverified intervals.` | `CT_SCAN` (adaptive) | declared coverage fraction; never "100% native frames" unless done |
| Reconstruction | `Reconstruct the motion system of the Barely Evolved timeline opening as an ORIGINAL production blueprint: image prompts, image-to-video prompts, static anchors, continuity locks.` | `DEEP`/`CT_SCAN` + `RECONSTRUCTION` | original blueprint from verified states; no copied characters/brand |
| Channel comparison | `Channel visual DNA: compare Primate vs MonkeBiznis using only validated per-video reports; list counterexamples and n.` | `CHANNEL_DNA` | within-video facts only while n = 1 per channel (current state) |

Behaviour expected on every invocation:
1. Read the per-Video-ID ledger and `09_CONTINUATION_HANDOFF.md` first.
2. Check usage, disk and Git writer ownership.
3. Write outputs only to the external evidence folder.
4. Promote no existing status without meeting its contract.
