# YIOS: start here

Single entry point for the research workstreams. It indexes; it does not move evidence. Every path below was checked to exist when this page was written (2026-11-09, Phase 2 batch 1). Branch pins are full commit SHAs read from `origin`. Counts are MEASURED unless marked CITED or NOT CHECKED. Detail and method: [research/consolidation/README.md](../research/consolidation/README.md). Rules: [AGENTS.md](../AGENTS.md).

## Status words (do not mix them)

| Word | Meaning |
|---|---|
| `VISUAL_ANALYSIS_COMPLETE` | The per-video visual-only contract and its validator passed. No claim about sound. |
| `ASR_UNCERTIFIED` | Text comes from machine speech recognition (Whisper `base`) and no human listened. |
| Full AV sign-off | A human heard the audio and signed off the visual. **0 videos**. Audio and AV are BLOCKED. |
| Off-device backup | **BLOCKED** (owner has no external drive). |

## Workstreams

| Priority | Workstream | Start in this tree | Pinned source (branch @ commit) | Local-only evidence (this Mac) | State |
|---|---|---|---|---|---|
| 1 | **Casual Finance** (reference channel `UCrNfRFWnLC3tCy1TnyhVQ7g`) | [hub README](../research/casually-finance/README.md), [INDEX.csv](../research/casually-finance/INDEX.csv), [visual index](../research/visual-forensics/channels/UCrNfRFWnLC3tCy1TnyhVQ7g/START_HERE.md), [LOCAL_ONLY map](../research/casually-finance/LOCAL_ONLY.md) | `research/casually-finance-consolidated` @ `9a4023af358ad15eec24a11cc5c2818a9d0994c6` (also on origin, no PR); 15-video milestone commit `2697d3c6dfda5c744aa1e995235143858f14471d` | `~/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104` (ledger, counter `count_complete.py`) | 206 catalog videos, all with ASR text. **19 of target 20** visual-closed (15 published in git, 4 local only). Milestones 20 and 25 open. |
| 1 | **xkcd What If?** (`UC6IxnFzHofFJ5X2PycSMsww`) | [evidence map](../research/consolidation/VISUAL_EVIDENCE_MAP.csv) (filter `channel_folder = xkcd Channel`) | `research/xkcd-whatif-visual-forensics` @ `3c6145ccde4a9ca8d155c8b9e63199b80d03625f` (campaign text through checkpoint R, no PR) | `~/YIOS-local-audits/xkcd-whatif` (ledger `asset_library/_channel/ct_closure/CLOSURE_LEDGER_v1.csv`) | Census 91 (45 long + 46 Shorts). **29 closed** (20 Shorts + 9 long-forms). 3 census IDs have no local MP4; `alkJ7xScBiw` acquisition is owner-blocked. |
| 2 | **Finance / economics corpus** (1,612 videos, 27 channels) | [reconciliation CSV](../research/consolidation/FINANCE_1612_RECONCILIATION.csv) | `fix/finance-audit-validators` (PR #45) @ `5d487623d1f20a2388527a1611ce77fbf65ec203`; queue `research/finance-economics-intelligence/FINANCE_CONTINUATION_QUEUE.csv` there; `research/finance-economics-intelligence` (PR #36) @ `f115285ba230fd9a8d8923dff1e5d477f8247d80`; Machine A `codex/finance-machine-a-owner-directed` @ `9c6f42fb33e493314cced538d5c5fa599a29e6c5` | `~/workprojects/yios-finance-machine-a` (worktree) | 966 original (all in the registry) + 646 expansion (none in the registry). 558 fully reviewed, all in the original layer. |
| 3 | **What If** (own channel, xkcd as reference) | [What If integration workflow](WHAT_IF_INTEGRATION_WORKFLOW.md), [source contract](WHAT_IF_FORENSIC_SOURCE_CONTRACT.md) | code and 83-video record on `main` @ `08e719264e31ecd82de24f8eeb8f065c08359fe5` | `~/workprojects/video data of what if` | Reference-book question open: a candidate PDF exists in Downloads (identity checked only, content NOT read). |
| 4 | Barely Evolved | n/a | `research/barely-evolved-visual-forensics` @ `3e587c757ed11731c1ce0f4b8975211b4474e00f` | `~/YIOS-local-audits/barely-evolved` | Lower priority. Off-device transfer of the R20 evidence still open. |
| 4 | Primitive Education | n/a | `research/primitive-education-visual-forensics` @ `ff2ff896ce7592fbb1ffad4477d306c327486bfa` | `~/YIOS-local-audits/primitive-education` | Lower priority, on hold. |
| 5 | Senior Health | [senior-health notes](research/senior-health-2026-09-25) | merged to `main`; production branch `production/senior-health-casually-finance-three-videos` @ `65caa889a3e1b9f3a1be6fa28a31ae4f518577a1` | Dr Rehan material in `~/workprojects/dr rehan video` | Lowest priority. Third-party research stays. Dr Rehan material is a removal candidate for a later batch; **nothing removed**. |
| excluded | Casual Economics | n/a | `codex/casual-economics-forensic-research` @ `fce81670bd2d6f29db6ef515732238fa3c5f09e3` | `~/Downloads/videos in mp3/casual_economics` (11 MP4) | Excluded from all Casual Finance milestones. |

## Maps added in Phase 2 batch 1 (all in `research/consolidation/`)

- [VISUAL_EVIDENCE_MAP.csv](../research/consolidation/VISUAL_EVIDENCE_MAP.csv): 454 local MP4 files with video ID, SHA-256, closure status, published location, AV status.
- [VISUAL_SEAL_VERIFICATION.csv](../research/consolidation/VISUAL_SEAL_VERIFICATION.csv): re-check of 28 existing SHA-256 seals.
- [FINANCE_1612_RECONCILIATION.csv](../research/consolidation/FINANCE_1612_RECONCILIATION.csv): membership, registry presence and verification, kept in separate columns.
- [LOCAL_EVIDENCE_PINS.sha256](../research/consolidation/LOCAL_EVIDENCE_PINS.sha256): hashes of the local ledgers and the two databases at this time.
- [CF_INTEGRATION_IMPORTED_FILES.txt](../research/consolidation/CF_INTEGRATION_IMPORTED_FILES.txt): 202 Casual Finance evidence files added from the Finance line, with blob IDs.
- [tools/build_phase2_batch1.py](../research/consolidation/tools/build_phase2_batch1.py): rebuilds the first four files. Read-only on all sources.

## Where the media is

MP4s, frames and audio stay on this Mac. They are not in GitHub and must not be sent there. Machine B's manifest (PR #41, commit `78e8fd2de654b622a5b1a093851886ef138c4d6a`) lists the same 453 distinct video hashes under Machine B paths. That is a lead for the 4.4 GB of MP4s only. It is **not verified** that those bytes are still there (Machine B is BLOCKED), and the ~15 GB of analysis workspaces under `~/YIOS-local-audits` have no known second copy.
