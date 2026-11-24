# 02 Local vs GitHub comparison

Compared with `origin/main` = `cf2dbb2c` (PR #62 merge). Current branch is 0 behind and 8 ahead of it.

| Material | On `origin/main` | Local only / other branch |
|---|---|---|
| `research/what-if-channel-strategy/` | **No** (0 files) | Yes, on `research/what-if-channel-strategy-2026-11-18` (pushed to origin 2026-11-19) |
| `research/what-if-scripts/` (83 transcripts, audits, matrix) | Yes (179 files) | also in `.claude/worktrees/yios-canonical` |
| `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/` (campaign: 64 per-video dirs, manuals v0.1-0.7, held-outs, RT1-RT4) | **Yes** (1,599 files) | local-only: media-derived images/mp4 tables (`LOCAL_ONLY_MANIFEST.csv` lists hashes; same-Mac, not off-device backup) |
| `research/visual-forensics/channels/CH-000004/` (CHANNEL_DNA + Brain v1.0.0 package, 315 files) | Yes | |
| `data/intelligence/channels/CH-000004/forensic-observation-index-v1.json` (8,327 observations, 10 IDs) | Yes (per status doc) | |
| Brain v1.0.0 staging JSONL (8 files) | repo has a preserved copy under `data/raw/forensic-analysis/preserved-worktree-evidence-2026-10-21/` | external preservation folder holds a byte-identical copy |
| 88 xkcd MP4s | No (private media, by rule) | `YIOS-Media-Library/xkcd Channel/` |
| 14 Brain MP4s (different encodes) | No | `~/GhilmanProjects/video data of what if/videos/` |
| Competitor CT evidence (Fossil, Minute Zero, Tracer) | No | `YIOS-local-audits/2026-11-18/WHATIF_COMPETITOR_CT/` |
| 8fADp43wJwU deep pass with audio stems | No | `YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU/` |
| Book OCR (private) | hashes only | `~/Downloads/What_If_Full_Book_15_Files/` |

Open PRs seen earlier in this session: #59, #61, #63 (visual-audit import), #64 (CI allowlist). Whether any of them touches xkcd material was not checked in this audit.

Not checked: Machine A. Its branch, media and any newer work must not be inferred from Machine B.
