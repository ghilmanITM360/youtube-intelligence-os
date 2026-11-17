# EXISTING_RESEARCH_AUDIT
## What is real
- Census, selection, state ledgers (5,458 states), per-video gates, closure ledger, model sheets, 13 motion windows, frozen rules v1-v4 with held-out tests. Source: workspace files above.
- Held-out results (recorded in handoffs, not re-run today): v7 19/23, v8 32/34 (colour 17/18, motion 15/16), v9 9/9 scorable but 0 feature-present cases, so rules v3/v4 changes are UNTESTED.
- Two silent 8 s proofs (16:9, 9:16) pass all machine criteria: 1-frame pops, linear 6-frame dissolve, no overshoot, 24 fps CFR, 0 decode errors, no clipping. P8 human playback review and P9 HumanCraft scorecard are PENDING_HUMAN.
## What is overstated if read carelessly
- "Visual forensics" here = decoded-frame metrics + sampled viewed sheets. 8.7% of clusters were viewed as images in the P2 pass; reviewer error rate above zero (3 classification errors, 16 hidden cuts found later).
- 29 "VISUAL_ANALYSIS_COMPLETE" is a visual-only contract. No audio, no AV, no script mapping.
- Today's concurrent CasuallyFinance session found image-sheet "viewed" claims that failed to decode. The xkcd record was not re-audited for this; treat per-video "viewed" claims as unverified until spot-checked.
- Prompt packs are text. No character image exists. No model was chosen.
- The 2026-09 chair test (CapCut) was REJECTED by its own audit: filled-in human, noun-icon assembly, no consequence-led drawing. This is the only real recreation failure on record and shows the gap between documentation and output quality.
## Duplicates
14-video corpus (Sep) = subset of the 88-file set. Release folder + ZIP of the brain = duplicate distribution. Set A/B pairs: 12 re-downloads, same video/audio.
