# Consolidation, Phase 2 batch 1 (2026-11-09)

Documentation PR cut from `main` @ `08e719264e31ecd82de24f8eeb8f065c08359fe5`. The measurements below were made on branch `cleanup/yios-phase2-batch1` (commit `34a79e46dc33b0469657d83a2af03458214c87e2`, local checkpoint, cut from `research/casually-finance-consolidated` @ `9a4023af358ad15eec24a11cc5c2818a9d0994c6`). Nothing was merged, deleted, renamed or reset. Source MP4s, existing ledgers and existing seals were only read. Entry page: [docs/START_HERE.md](../../docs/START_HERE.md). The Phase 1 audit is a local file and is not in git.

**What this PR contains:** the entry page, this folder (maps, pins, build script), and the Casual Finance hub index (`research/casually-finance/`: README, INDEX.csv, manifest, QC and checksum files, tools). **What it does not contain:** MP4s, frames, audio, Git LFS pointers, transcript bodies, the 202 files below, or any inherited change from the consolidated branch. Paths inside the CSVs point at the pinned branches or the local workspace, not at this tree. [tools/build_phase2_batch1.py](tools/build_phase2_batch1.py) is a provenance record: it needs the local workspace and cannot be re-run from `main` alone.

Labels: MEASURED = computed by [tools/build_phase2_batch1.py](tools/build_phase2_batch1.py) or a git command in this batch; CITED = read from a file, not recomputed; NOT CHECKED = not looked at.

## Ownership check before the branch was cut (MEASURED)

Working tree clean; HEAD `9a4023af`; worktrees `yios-audit-fixes` (`5d487623`) and `yios-finance-machine-a` (`9c6f42fb`) both clean; 1 stash kept; `vf_lock.sh status` = `FREE`, no `.xkcd_writer_lock` directory; no claim files in the tree; the only `claims/` refs on origin are the three `yios-test/...` test refs. Machine B was not reachable, so its unpushed work cannot be ruled out.

## 1. Visual evidence map and seals

[VISUAL_EVIDENCE_MAP.csv](VISUAL_EVIDENCE_MAP.csv): one row per local MP4 (454) plus 3 xkcd census IDs with no file. All 454 files were hashed again in this batch.

| Fact | Result |
|---|---|
| Files / distinct SHA-256 / bytes | 454 / 453 / 4,361,600,146 (one exact duplicate, a Casual Finance file) |
| Files without a video ID | 17: 11 `casual_economics` (excluded channel) + 6 `CasuallyFinance` |
| Casual Finance | 216 files = 207 distinct IDs; 206 are catalog IDs, 1 (`9eBM5IF_bco`) is not in the catalog; 3 IDs have two encodes (`2EZzwupIa80`, `PxgCsLSf-w4`, `rSa2aziEsAI`) |
| Casual Finance closures | 19 listed in `visual_complete_ledger.json`; all 19 file hashes equal the baseline; the counter script printed `VERIFIED_COMPLETE 19 / target 20`. 15 have a published evidence folder under `research/visual-forensics/channels/casual-finance/`; **4 are local only** (`7K991LgY3tc`, `Im-N3K9Pnf0`, `KTnp2OlQJHA`, `WCS1bK3KB3U`) |
| xkcd closures | 29 `VISUAL_ANALYSIS_COMPLETE` (20 Shorts + 9 long-forms), no failing gates, all 29 ledger hashes equal the file hashes. No local MP4 for `NxVdO7M2YdM`, `XwJAbyn5uGY`, `alkJ7xScBiw` |
| Full AV sign-off | 0 everywhere. The `av_status` column is `BLOCKED` on every row |
| Machine B manifest (PR #41) | all 454 file hashes appear in it (CITED, bytes at Machine B not verified) |

[VISUAL_SEAL_VERIFICATION.csv](VISUAL_SEAL_VERIFICATION.csv): 28 existing seal files, none rewritten.

| Result | Seals | Meaning |
|---|---|---|
| PASS | 5 | xkcd `SHA256SUMS_ct_closure_long_v9.txt` and the 4 local Casual Finance seals (roster, identity baseline, ASR-156 review, narration manifest) |
| SUPERSEDED_LIVING_FILE | 9 | older xkcd seals; the only differences are `CLOSURE_LEDGER_v1.csv` and later handoff files, which are living files re-sealed by v9. Frozen contract `VISUAL_CLOSURE_CONTRACT_v1.md` matches its `.sha256` |
| PASS_HEAVY_FILES_LOCAL_ONLY | 10 | published Casual Finance seals: text files match in git; frames and WAV files match only in the local workspace under `~/YIOS-local-audits`. That heavy evidence has one copy |
| **FAIL** | 4 | published seals for `CFrVTZBYa3Q`, `SYSUh-oow6M`, `Xkk9GnnJHBg`, `dPoDyl9Ys38`: `VALIDATION_RESULTS.json` differs from the hash in the seal. The committed file (commit `2697d3c6`) and the local copy agree with each other and report `failed: 0` (CFrV 42/42, SYSUh 43/43). Reading: the validator was re-run after the seal was written. **Not repaired**; a refreshed seal is a decision for the owner |

[LOCAL_EVIDENCE_PINS.sha256](LOCAL_EVIDENCE_PINS.sha256) records today's hashes of the xkcd and Casual Finance ledgers, the frozen contract, the Casual Finance transcript manifest and both databases. Registry DB `39e7a28ba592b902...` is unchanged from the 2026-09-28 snapshot.

## 2. Finance / economics corpus (1,612 videos)

[FINANCE_1612_RECONCILIATION.csv](FINANCE_1612_RECONCILIATION.csv) joins the continuation queue to the registry (opened read-only). Corpus membership, registry presence and verification are separate columns. Nothing was moved; the corpus stays on its branches.

Pins: queue read from `fix/finance-audit-validators` @ `5d487623d1f20a2388527a1611ce77fbf65ec203`, file SHA-256 `aa5057026637d55b79a21c2b2e662c5f57a7a36fe52be80ce525ef0cc364b0ec`, git blob `74dc8c5068abb3a052b97fea89c0b75f8bc57ecd`. `VIDEO_MASTER.csv` SHA-256 `15e5af152344944f3f9b7f041289a92cc365cf9d0bfad43cd95df84822f95615` equals `frozen_master_sha256` in `audit-baseline/MANIFEST.json`. The manifest's registry hash equals the live registry hash `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`. The frozen DB in that branch is a Git LFS pointer to the same oid.

| Fact (MEASURED) | Result |
|---|---|
| Queue rows / distinct IDs / channels | 1,612 / 1,612 / 27 |
| ORIGINAL | 966; all 966 are in the frozen ID list and in the registry; 0 channel mismatches |
| EXPANSION | 646; 0 in the registry, 0 in the frozen list |
| Frozen IDs missing from the queue | 0 |
| Fully reviewed (all six dimensions complete) | 558, all `ACCEPTED`, all ORIGINAL (Nick Invests 291, Primate Economics 28, others in the CSV) |
| Open mismatch from the Phase 1 audit: 558 vs 564-575 | **Resolved.** Per-dimension counts are topic 564, script 564, thumbnail 575, title 575, virality 558. The surplus over 558 is 6 to 17 non-accepted videos that finished only some dimensions (dimensions complete per video: 6 for 558, 1 for 392, 2 for 7, 3 for 4, 4 for 6, 0 for 645). `performance_status` is 954 because metrics exist for far more videos than were reviewed |
| Open mismatch: 11 vs 12 placeholders | **Resolved.** Registry placeholder transcripts that are in the queue: 11, equal to the queue's 11. The registry's twelfth placeholder is outside the Finance corpus |
| Registry channel for each queue row | matches for every row present in the registry |

Verification here means the queue's own status fields (CITED from the branch). It is not a re-review of any video.

## 3. Scoped Casual Finance integration

| Item | Result (MEASURED) |
|---|---|
| PR #28 (`research/casually-finance-success-playbook`), the 8 differing files under `data/extracted/forensic-analysis/casually-finance/2026-10-12/` | **Not ambiguous.** #28 branched from #21 at `7e2f6d3a3d5e4294d5f8bc4737dd0c784610c1f1` and never edited these 8 files: each equals its blob at that commit. The consolidated version equals the tip of #21 (`043b85bf58f84fb6a1c8981d54e3b233faa6a928`), which is 4 commits newer (claim-verification work: +227 / -80 lines). Keep the consolidated version. Nothing to merge from #28 for these files |
| #37 and #47 | #37: 880 of 880 changed files identical in the consolidated tree. #47: 10 of 10 identical (a scoped re-cut of #37's inventory folder; not an ancestor of #37). Nothing further to import |
| Finance-line Casual Finance evidence missing from the consolidated tree | **202 text files** (11.7 MB: 69 JSON, 64 py, 44 CSV, 20 md, 5 hash lists) under `research/visual-forensics/channels/casual-finance/Uumnx2Fo6cE/` (133 files) and `.../o3FQcd91MIs/` (69 files). 0 conflicts with the consolidated tree; byte-identical on five branches (#45, #36, Machine A, dual-machine, brain-preservation). They were imported on the local checkpoint branch only. **They are not in this PR** (scope review below). Blob IDs: [CF_FINANCE_LINE_FILES_NOT_IMPORTED.txt](CF_FINANCE_LINE_FILES_NOT_IMPORTED.txt). Secret-pattern scan: only the words "Secret Service" in video text |
| Left alone (not Casual Finance scope) | `EXPANSION_K01_CASUALLY_FINANCE.*` (Finance-line files), one Machine B recovery note |
| PR #41 `research/local-channel-media-library` @ `78e8fd2de654b622a5b1a093851886ef138c4d6a` | **Deferred, ambiguous.** Covers all channels, not only Casual Finance. It edits `AGENTS.md` with Machine B ownership statements that conflict with the 2026-11-06 owner decision, plus `README.md` and `.gitignore`. 16 other files (4 code, 3 docs, 9 indexes) do not conflict. The two media scripts write into `data/local-channel-media` and `.cache`; they should not land before the matching `.gitignore` lines. Needs an owner decision |
| Production branches (#29, #30, #34) and Casual Economics (#25) | Not touched: generated media and an excluded channel |
| Git LFS | On the pinned consolidated branch, `git lfs ls-files` lists **17** legacy Casual Finance source MP4s (261,336,715 bytes) under `data/raw/forensic-analysis/casually-finance/source-videos/`; git stores 133-byte pointers and the local LFS objects exist. **Whether GitHub holds these remote objects is NOT CHECKED** (the Phase 1 audit said 16; this tree has 17). This PR contains no LFS pointers. New raw media stays local and is never committed or put in LFS |
| Existing refs, stash, untracked and ignored files | unchanged |

### Review of the 202 files (why they stay out of this PR)

- Both video IDs are in the 206-video catalog (long-forms `Uumnx2Fo6cE` and `o3FQcd91MIs`) and in the Casual Finance closure ledger, so they are real closed videos, not stray files.
- `main` has no `research/visual-forensics/channels/casual-finance/` folder at all. The 202 files complete two per-video folders (269 files for `Uumnx2Fo6cE`, 133 for `o3FQcd91MIs` in total; the consolidated branch already holds the other 136 and 64), so on `main` they would be orphan fragments: manifests, reports and 64 Python scripts whose neighbours (frames, ledgers, validators) are absent.
- They are already on five existing branches and unchanged, so nothing is at risk of loss.
- Decision: keep them on their branches and link by pinned SHA. Bring them over together with the rest of the Casual Finance visual-forensics tree in a later, owner-approved integration PR.

## 4. Blocked or open

- **Off-device backup: BLOCKED.** No external drive. The only lead is Machine B's manifest for the 4.4 GB of MP4s, unverified. About 15 GB of analysis workspaces under `~/YIOS-local-audits` have no known second copy.
- **Machine B: BLOCKED.** No authorised connection from this Mac.
- 4 Casual Finance closures are not yet published; 16 roster videos are not closed; milestones 20 and 25 are open.
- 4 published seals fail on `VALIDATION_RESULTS.json` (section 1); heavy evidence exists once.
- Whether CI failures on 7 open PRs reflect billing or code was not investigated.
- Branch retirement, PR merges, Dr Rehan removal, `MonkeBiznis` channel identity, PR #41 import and any deletion are for later batches.
