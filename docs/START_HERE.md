# YIOS: start here

Single entry point for the research workstreams. It indexes; it does not move evidence. Counts are MEASURED on the owner's Mac on 2026-11-09 unless marked CITED (read from a file) or NOT CHECKED. Method and detail: [research/consolidation/README.md](../research/consolidation/README.md). Rules: [AGENTS.md](../AGENTS.md).

**How links work on this page.** A relative link opens a file that is in this tree. A GitHub link is pinned to a full commit SHA: it opens evidence that stays on a research branch and is deliberately not copied into `main`. Local-only evidence lives on one Mac and has no link.

## Status words (do not mix them)

| Word | Meaning |
|---|---|
| `VISUAL_ANALYSIS_COMPLETE` | The per-video visual-only contract and its validator passed. No claim about sound. |
| `ASR_UNCERTIFIED` | Text comes from machine speech recognition (Whisper `base`); no human listened. |
| Full AV sign-off | A human heard the audio and signed off the visual. **0 videos.** Audio and AV are BLOCKED. |
| Off-device backup | **BLOCKED** (the owner has no external drive). Not a blocker for this documentation. |

## Integrity flags (read before trusting a seal)

- **4 published Casual Finance seals do not verify:** `CFrVTZBYa3Q`, `SYSUh-oow6M`, `Xkk9GnnJHBg`, `dPoDyl9Ys38`. In each, `VALIDATION_RESULTS.json` differs from the hash in its `SHA256SUMS`; the file reports `failed: 0`, so the validator was most likely re-run after the seal. The original seals were **not rewritten or repaired**. A refreshed seal is an owner decision. Per-seal result for all 28 seals: [VISUAL_SEAL_VERIFICATION.csv](../research/consolidation/VISUAL_SEAL_VERIFICATION.csv).
- **Heavy evidence has one copy.** Frames and audio under `~/YIOS-local-audits` (about 15 GB) and the 454 MP4s (4.4 GB) exist only on this Mac.
- **Open: 4 Casual Finance closures are local only** (`7K991LgY3tc`, `Im-N3K9Pnf0`, `KTnp2OlQJHA`, `WCS1bK3KB3U`), 16 roster videos are not closed, milestones 20 and 25 are open.

## Workstreams

| Priority | Workstream | Start here | Pinned source | Local-only evidence (this Mac) | State |
|---|---|---|---|---|---|
| 1 | **Casual Finance** (`UCrNfRFWnLC3tCy1TnyhVQ7g`) | [hub README](../research/casually-finance/README.md), [INDEX.csv](../research/casually-finance/INDEX.csv), [LOCAL_ONLY.md](../research/casually-finance/LOCAL_ONLY.md); [visual index at the pinned commit](https://github.com/ghilmanITM360/youtube-intelligence-os/blob/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/visual-forensics/channels/UCrNfRFWnLC3tCy1TnyhVQ7g/START_HERE.md) | branch `research/casually-finance-consolidated` @ [`9a4023af358ad15eec24a11cc5c2818a9d0994c6`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6) (no PR); 15-video milestone @ [`2697d3c6dfda5c744aa1e995235143858f14471d`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/2697d3c6dfda5c744aa1e995235143858f14471d) | `~/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104` (ledger, counter script) | 206 catalog videos, all with Whisper `base` text (below). **19 of target 20** visual-closed: 15 published, 4 local only. |
| 1 | **xkcd What If?** (`UC6IxnFzHofFJ5X2PycSMsww`) | [evidence map](../research/consolidation/VISUAL_EVIDENCE_MAP.csv) (filter `channel_folder = xkcd Channel`) | branch `research/xkcd-whatif-visual-forensics` @ [`3c6145ccde4a9ca8d155c8b9e63199b80d03625f`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/3c6145ccde4a9ca8d155c8b9e63199b80d03625f) (no PR) | `~/YIOS-local-audits/xkcd-whatif` (ledger `asset_library/_channel/ct_closure/CLOSURE_LEDGER_v1.csv`) | Census 91 (45 long + 46 Shorts). **29 closed** (20 Shorts + 9 long-forms). 3 census IDs have no local MP4; `alkJ7xScBiw` acquisition is owner-blocked. |
| 2 | **Finance / economics corpus** (1,612 videos, 27 channels) | [reconciliation CSV](../research/consolidation/FINANCE_1612_RECONCILIATION.csv) | PR #45 `fix/finance-audit-validators` @ [`5d487623d1f20a2388527a1611ce77fbf65ec203`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/5d487623d1f20a2388527a1611ce77fbf65ec203) (queue, frozen DB pointer, audit baseline); PR #36 `research/finance-economics-intelligence` @ [`f115285ba230fd9a8d8923dff1e5d477f8247d80`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/f115285ba230fd9a8d8923dff1e5d477f8247d80); Machine A `codex/finance-machine-a-owner-directed` @ [`9c6f42fb33e493314cced538d5c5fa599a29e6c5`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9c6f42fb33e493314cced538d5c5fa599a29e6c5) | `~/workprojects/yios-finance-machine-a` (worktree) | 966 original (all in the registry) + 646 expansion (none in the registry). 558 fully reviewed, all original. Nothing was moved; the corpus, its verification records and the frozen DB stay on those branches. |
| 3 | **What If** (own channel; xkcd is the reference) | [integration workflow](WHAT_IF_INTEGRATION_WORKFLOW.md), [source contract](WHAT_IF_FORENSIC_SOURCE_CONTRACT.md) | code and 83-video record on `main` | `~/workprojects/video data of what if` | See "Two different documents" below. |
| 4 | Barely Evolved | n/a | branch `research/barely-evolved-visual-forensics` @ [`3e587c757ed11731c1ce0f4b8975211b4474e00f`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/3e587c757ed11731c1ce0f4b8975211b4474e00f) | `~/YIOS-local-audits/barely-evolved` | Lower priority. Off-device transfer of the R20 evidence still open. |
| 4 | Primitive Education | n/a | branch `research/primitive-education-visual-forensics` @ [`ff2ff896ce7592fbb1ffad4477d306c327486bfa`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/ff2ff896ce7592fbb1ffad4477d306c327486bfa) | `~/YIOS-local-audits/primitive-education` | Lower priority, on hold. |
| 5 | Senior Health | n/a | production branch `production/senior-health-casually-finance-three-videos` @ [`65caa889a3e1b9f3a1be6fa28a31ae4f518577a1`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/65caa889a3e1b9f3a1be6fa28a31ae4f518577a1) | Dr Rehan material in `~/workprojects/dr rehan video` | Lowest priority. Dr Rehan material is a removal candidate for a later batch; **nothing removed**. |
| excluded | Casual Economics | n/a | branch `codex/casual-economics-forensic-research` @ [`fce81670bd2d6f29db6ef515732238fa3c5f09e3`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/fce81670bd2d6f29db6ef515732238fa3c5f09e3) | `~/Downloads/videos in mp3/casual_economics` (11 MP4) | Excluded from all Casual Finance milestones. |

## Casual Finance transcript coverage (206 catalog IDs, MEASURED from [INDEX.csv](../research/casually-finance/INDEX.csv))

| Source | Videos | Type |
|---|---:|---|
| Word-level transcript committed on the pinned branch (PR #21 line) | 16 | Whisper `base`, `ASR_UNCERTIFIED` (24,527 words; 22,710 high, 1,327 medium confidence, 490 unverified) |
| Local Whisper `base` run, 2026-11-09 | 199 | `ASR_UNCERTIFIED`; QC flagged 0. Hashes and QC: [manifest.csv](../research/casually-finance/transcripts_asr_base_20261109/manifest.csv), [transcript_qc.csv](../research/casually-finance/transcripts_asr_base_20261109/transcript_qc.csv), [SHA256SUMS.txt](../research/casually-finance/transcripts_asr_base_20261109/SHA256SUMS.txt) |
| In both | 9 | Same model run twice: **not independent evidence** |
| Only the committed 16 (no 2026-11-09 text) | 7 | |
| **Any text** | **206 / 206** (190 + 9 + 7) | No human-verified transcript, no official captions |

Transcript bodies (398 `.json`/`.txt` files, 12.9 MB) stay on the pinned branch and in `~/YIOS-local-audits/CF_TRANSCRIPTS_ASR_20261109/`; this tree carries only their manifest, QC and checksum files. Whisper `base` mishears proper nouns ([ASR_NAME_CHECK.md](../research/casually-finance/ASR_NAME_CHECK.md)): check names and numbers before reuse.

## Evidence maps (all in [research/consolidation/](../research/consolidation/README.md))

- [VISUAL_EVIDENCE_MAP.csv](../research/consolidation/VISUAL_EVIDENCE_MAP.csv): **457 rows = 454 local MP4 rows (each with SHA-256) + 3 xkcd census IDs that have no local file** (`NxVdO7M2YdM`, `XwJAbyn5uGY`, `alkJ7xScBiw`). The 454 files hold 453 distinct hashes (one exact duplicate). `av_status` is `BLOCKED` on every row.
- [VISUAL_SEAL_VERIFICATION.csv](../research/consolidation/VISUAL_SEAL_VERIFICATION.csv): re-check of 28 existing SHA-256 seals (5 PASS, 9 superseded living files, 10 pass with heavy files local only, **4 FAIL**).
- [FINANCE_1612_RECONCILIATION.csv](../research/consolidation/FINANCE_1612_RECONCILIATION.csv): membership, registry presence and verification, kept in separate columns.
- [LOCAL_EVIDENCE_PINS.sha256](../research/consolidation/LOCAL_EVIDENCE_PINS.sha256): hashes of the local ledgers and databases on 2026-11-09.
- [CF_FINANCE_LINE_FILES_NOT_IMPORTED.txt](../research/consolidation/CF_FINANCE_LINE_FILES_NOT_IMPORTED.txt): 202 Casual Finance evidence files that exist on the Finance line but not on the consolidated branch; listed with blob IDs and **not copied here** (see the consolidation README).
- [tools/build_phase2_batch1.py](../research/consolidation/tools/build_phase2_batch1.py): provenance record of how the CSVs were built. It reads the local workspace and pinned branch checkouts, so it cannot be re-run from `main` alone.

Paths inside these CSVs point at the pinned branches or the local workspace, not at this tree.

## Two different documents (do not mix them)

- **What If topic book** (the topics and reference list for the What If channel): **not identified.** No file was located, and none is claimed here. This remains an open owner question.
- **HumanCraft Video Studio V2 Complete Guide** (`~/Downloads/HumanCraft_Video_Studio_V2_Complete_Guide.pdf`, 35 pages, 181,440 bytes, SHA-256 prefix `1b1564cfd5fe144a`): a **production guide** for building video motion and assets. It is not a topic book, is not in git, and nothing in this PR summarizes it.

## Where the media is

New raw media (MP4, frames, audio) stays on the owner's Mac. It is not committed to git and not to Git LFS. This tree contains no media and no LFS pointers.

The older Casual Finance hub on the pinned branch (`research/casually-finance-consolidated` @ `9a4023af…`) holds **17 legacy Git LFS pointers**: Casual Finance source MP4s under `data/raw/forensic-analysis/casually-finance/source-videos/` (261,336,715 bytes). Local LFS objects exist; **whether GitHub holds those remote objects is NOT CHECKED**.

Machine B's manifest (PR #41, [`78e8fd2de654b622a5b1a093851886ef138c4d6a`](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/78e8fd2de654b622a5b1a093851886ef138c4d6a)) lists the same 453 distinct video hashes. That is a lead only: Machine B is BLOCKED and the bytes there are **not verified**.
