# Project Current-State Deep Audit — 2026-10-03

Status: READ-ONLY audit (baseline captured 2026-10-03 at HEAD 373bf37); see **Update 2026-10-04** below for the canonicalization pass that followed. Source data modified by the audit: NO. This file and its JSON companion were the only files the audit itself created. Nothing was staged, committed, pushed, merged, rebuilt-in-place or deleted. Rebuild/test experiments ran only in a disposable clone under the session scratchpad.

Evidence rule: every number is re-derived from files, git, SQLite or `gh` during this audit. Previous reports and session memory were treated as claims to verify. Confidence tags: VERIFIED (computed from files this session), REPORTED (stated in a document, not recomputed), INFERRED, UNKNOWN (never converted to zero), NOT FOUND (searched, absent).

## Update 2026-10-04 — canonicalization pass (integration branch)

Baseline sections below describe the state at 373bf37 and are kept as written; this section records what changed afterwards and corrects two wording issues.

**Integration branch:** `integration/yios-current-canonical-2026-10-03` (worktree `/Users/ghilmankhan/workprojects/yios-integration`), created from `origin/main` 812f249, PR #7 -> `main`. Merge order and results:

| Step | Source | Result |
|---|---|---|
| A | `research/senior-health-acquisition-phase-2` @ 373bf37 (10 commits) | merged `--no-ff`, no conflicts (fast-forward-equivalent) |
| B | PR #6 branch @ 814a027 (shares 4 commits with A; 1 unique) | merged, no textual conflicts. Overlapping files (registry DB LFS pointer, inventory DB, registry JSON, tracker xlsx, validator, checkpoint md) were all changed only on the PR #6 side after the shared base, so the PR #6 versions were taken by git; this was verified by rebuilding rather than trusted |
| C | `origin/research/senior-health-complete-local-sync` @ 0cbabf5 (1 unique commit, `docs/research/thumbnail-forensics-2026-10-02/` only) | merged, no overlap |
| D | uncommitted `forensic-v3/scripts/build_master_inventory.py` change in `yios-expansion` | reviewed: complete, backward-compatible (merges several public-metadata dirs, first record per Video ID wins, docstring and report text updated). Committed to the integration branch as its own commit. The `yios-expansion` worktree was not touched |

**Derived outputs rebuilt from merged sources:** registry DB and registry JSON rebuilt (`build_youtube_channel_registry --write-ledgers`): all 26 tables content-identical to the merged DB except the `generated_at` timestamp (idempotent), so the committed files were kept. Master tracker workbook rebuilt to scratch: all 9 sheets cell-identical. Registry: 33 datasets (DS-000034 registered metadata-only, 0 `dataset_channels`, 0 `dataset_videos`), 75 channels, 2,303 videos.

**DS-000034 verified:** 73/73 manifest SHA-256 match; 72 channel files, 5,007 JSONL lines, 4,883 unique video IDs (124 retry duplicates), 4,648 records with `video_details`, 0 error rows. Still metadata-only; no transcripts.

**Red test resolved (G02):** `test_bhwa_structural_analysis_covers_all_98_and_separates_deep_review`. Root cause: commit 373bf37 updated the test to expect 25 `VERIFIED_DEEP_INVESTIGATION` rows after the 25-case deep register was built, but `analyze_better_health_while_aging.py` still hardcoded the original nine. Evidence check: the deep register holds 25 breakout investigations, all `COMPLETE_TRANSCRIPT_REVIEWED`, and the IDs equal the 25 breakout inventory IDs. Verdict: the test and evidence were right, the implementation was stale. Fix: the analyzer derives the state from the register. Test expectation unchanged. Regenerated structure JSON differs only in the state label of 25 videos.

**Validation (clean clone of the integration HEAD):** compileall OK; ruff clean; `scan_tracked_secrets` 0 findings; both DBs integrity `ok`, 0 FK violations; `rebuild_inventory_catalog` bootstrap OK; `validate_dataset_ledgers`, `validate_youtube_channel_registry`, `validate_legacy_dataset_manifests` PASS; `git lfs fsck` OK; full pytest 411 passed, 1 skipped (media fixture absent, also skipped in CI), 0 failed, and the tree stays clean afterwards. CI on the combined HEAD is the PR #7 `validate` check (see PR).

**Thumbnail checkpoint preserved, not extended:** `CHECKSUMS.sha256` verifies with 0 mismatches; `completion-ledger.csv` has B000 and B001 COMPLETE, B002-B009 PENDING. No claim of 2,275 local thumbnails, 78 audits or 140 families is restored. Verified thumbnail truth is unchanged: 200 local current-public thumbnails, 0 historical snapshots, 6 audits.

**Privacy (G03) — corrected wording.** Two different things were previously blurred:
- RAW_PRIVATE_STUDIO exports (69 Studio ZIPs in `~/Downloads`, plus the 70-file ignored copy in `data/raw/first-party/youtube-studio/`) are **ignored / local-only** and were never committed or pushed.
- DERIVED_PRIVATE_ANALYTICS (the five tracked files) are **tracked and already on the private remote** (origin `research/senior-health-acquisition-phase-2`, pushed 2026-09-29).
`remote_push_performed` in the checkpoint JSON and its builder is corrected to `true`; HANDOFF-2026-09-28.md carries a dated correction. Recommendation: KEEP_PRIVATE_REPO_ONLY + SANITIZE_FUTURE_COMMITS; no history rewrite (private repo, one collaborator); HISTORY_REWRITE_REQUIRED only if the repo is ever shared or made public. Detail: `docs/audits/DECODE-YOUR-HEART-PRIVACY-CLASSIFICATION-2026-10-03.md`. An independent backup now exists at `~/Documents/yios-private-backups/studio-exports-2026-10-03/` (139 files, SHA256SUMS verified; originals untouched). It is outside the repo and `~/Downloads`, and must never be committed.

**Reconciling "two untracked files" vs "working tree clean, 0 untracked".** Both were true at different moments. The Section 2 row `Working tree: clean, 0 untracked` was measured at the start of the audit, before any file was written. The audit then created exactly two new files, `docs/audits/PROJECT-CURRENT-STATE-DEEP-AUDIT-2026-10-03.md` and `.json`; from that point the audited checkout showed those 2 untracked files (the only non-ignored changes). The 46 "untracked" files in `scripts/` counted in the code section are ignored `__pycache__` bytecode. In the integration branch these two files are tracked (this file), so the integration worktree has 0 untracked files.

**Gap status after this pass:** G01 resolved on the integration branch (pending merge of PR #7); G02 fixed; G03 wording corrected and recommendation recorded (owner decision still open on removing the five files); Studio backup done (G08 reproducibility is still open). All other gaps unchanged. PR #6 (814a027) and the phase-2 branch are fully contained in the integration branch; they become superseded once PR #7 merges.


Audited checkout: branch `research/senior-health-acquisition-phase-2`, HEAD `373bf37e930bbfedefb9ae2423a3fde9a1ad151b`; `origin/main` = `812f2499719d4b8e93d71b517072881278e8ddbd`. Also inspected read-only: worktree `/Users/ghilmankhan/workprojects/yios-expansion` (branch `research/senior-health-data-expansion-2026-09-28`), remote-only branch `origin/research/senior-health-complete-local-sync`, ~/Downloads, ~/.codex, /private/tmp.

## 1. Executive Summary

**What the project actually is today.** A file-first evidence repository (1.28 GB tracked, 3.7 GB `.git` incl. 2.4 GB LFS store) holding 75 canonical YouTube channels, of which 46 have video-level data (2,303 unique videos, 2,291 real transcripts). The V1 intelligence engines exist and are generic, but generated intelligence artifacts exist for only 5 legacy channels (CH-000001..5, produced 2026-09-11). At least 40 further data channels are `DATA_READY` (inputs exist, engines can run) with no generated artifacts. First-party Studio data exists only for the own channel (Decode Your Heart / Dr. Rehan), only locally and gitignored, and was not ingested through the first-party pipeline.

**Top findings (all VERIFIED unless noted):**

1. **The work is split across three places and no single checkout holds it all.** This checkout has Decode Your Heart (DS-000032) research and BHWA backfill but NOT DS-000034 or the 143-row Senior Health inventory (those live on PR #6 / `yios-expansion`), and NOT the thumbnail-forensics checkpoint (remote-only branch `origin/research/senior-health-complete-local-sync`, commit 0cbabf5, 2026-10-02). PR #6 and the current branch each hold 5-10 unique commits on a shared base; they touch disjoint files (clean merge at file level), but both are unmerged. `origin/main` is 10 commits behind the current branch.
2. **DS-000034 is real and verified** (73/73 manifest hashes match; 4,648 successful per-video metadata records across 63 channels; 235 refusals unresolved; 4,245 video IDs new to the registry). It is branch-only and metadata-only.
3. **DS-000035 does not exist anywhere on disk.** A background collection was reported in session memory; no manifest, data or staging directory was found. Treat as NOT PRESERVED.
4. **Thumbnail reality is much smaller than the later-agent claims.** Only 200 local current-public thumbnails exist (DS-006 32, DS-017 83, DS-019 29, DS-032 56 ignored). Claims of 2,299 videos / 2,131 downloaded / 2,275 local / 24 failed / 78 audits / 140 pairs have NO artifact on this machine or in git history. The remote-only checkpoint contains 144 ledger rows, 6 audits (B001) and PENDING B002-B009. No thumbnail is `HISTORICAL_SNAPSHOT_VERIFIED`; every local thumbnail is `CURRENT_PUBLIC_ONLY`.
5. **Privacy:** per-video private Studio metrics are inside 5 tracked files in `docs/research/decode-your-heart-2026-09-27/` and are on the remote (pushed 2026-09-29). The repo is PRIVATE (verified). The checkpoint's `remote_push_performed=false` is wrong. Raw Studio ZIPs are correctly ignored and local-only, and their only copies of record sit in ~/Downloads and the ignored folder (independent backup made 2026-10-04: `~/Documents/yios-private-backups/studio-exports-2026-10-03/`).
6. **Test suite is not green at HEAD:** 405 passed, 1 failed (`test_bhwa_structural_analysis_covers_all_98_and_separates_deep_review`, PROJECT DEFECT: test/script drift introduced by commit 373bf37), 1 skipped. No CI run exists for HEAD. Last CI on main and on PR #6: success.
7. **Registry is reproducible from committed sources:** a disposable-clone rebuild produced identical content in all 13 compared tables (2,303 videos, 75 channels), differing only in a timestamp; validator PASS. The historical inventory DB (10 channels / 667 videos) is NOT rebuildable from a clean clone (documented gap).
8. **Video type is unresolved for 159 videos** (Mr. Finance 65, Matty Invests 94; raw value NULL). The earlier 216 figure was the total availability-gap rows (159 video_type + 29 identity-only + 28 other), not a type count.

**Final status: VERIFIED WITH WARNINGS.**

## 2. Git / GitHub State

| Item | Value |
|---|---|
| Current checkout | `research/senior-health-acquisition-phase-2` @ `373bf37` (commit message literally `commit`) |
| `origin/main` | `812f249` (PR #5 merge baseline, 2026-09-25) |
| Current vs origin/main | 10 ahead, 0 behind; `origin/research/senior-health-acquisition-phase-2` = HEAD (nothing unpushed) |
| Remote | `https://github.com/ghilmanITM360/youtube-intelligence-os.git`, **PRIVATE**; partial clone (`blob:none`, promisor) |
| Working tree | clean at audit start: 0 staged, 0 modified, 0 untracked (non-ignored); the audit then added 2 untracked files (these audit .md/.json; see Update 2026-10-04) |
| Stash | 1 (`stash@{0}`, 2026-09-24, one-line checkpoint-doc edit; not evidence) |
| Local `main` | `2511013`, 62 commits behind origin/main (stale; do not use) |
| Branch protection | HTTP 403 (not available on this plan for private repos): UNKNOWN |
| LFS | 1 file (`youtube_channel_registry.db`); `git lfs fsck` OK; object present on GitHub for main, HEAD and PR #6 versions (LFS batch API: AVAILABLE) |
| Garbage | 7 `tmp_pack_*` files (84 MB) in `.git/objects/pack`: interrupted fetch debris |

## 3. Branch and PR Reality

| PR | Title | Head | State | Merge | CI |
|---|---|---|---|---|---|
| #6 | Research/senior health data expansion 2026 09 28 | `814a027` (`research/senior-health-data-expansion-2026-09-28`) | OPEN | MERGEABLE, CLEAN | `validate` SUCCESS (2026-09-28) |
| #5 | Consolidate PR#2/#3/#4 | `73816f1` | MERGED 2026-09-25 | n/a | success |
| #4 | chore/full local data sync | `f3c5635` | MERGED | ancestor of main | success |
| #3 | complete local sync | `9f0454c` | MERGED | ancestor of main | n/a |
| #2 | forensic v2 | `206d67b` | MERGED | ancestor of main | n/a |
| #1 | chore/full local data sync | `1a46d84` | MERGED 2026-09-24 | ancestor of main | success |

PR #6 contains unique work: DS-000034, the 143-row inventory, paid-acquisition plan (not executed), and the live catalog. The current branch has NO pull request and no CI run. The two heads share base `31ea9a5`; they change disjoint file sets (37 vs 243 files), so no textual conflict, but the LFS registry pointer differs (PR #6 registry `39e7a28b…`, current `48ffb558…`, origin/main `63c1f894…`) and would need a deliberate rebuild after merging.

| Branch | Unique vs origin/main | Classification |
|---|---|---|
| research/senior-health-acquisition-phase-2 (local+remote) | 10 | UNMERGED, unique (DYH research, BHWA backfill) |
| research/senior-health-data-expansion-2026-09-28 (local+remote, PR #6) | 5 | UNMERGED, unique (DS-000034) |
| origin/research/senior-health-complete-local-sync | 1 | UNMERGED, **remote-only**, unique (thumbnail-forensics-2026-10-02, 2026-10-02) |
| backup/decode-15cbe9f-original (local only) | 5 | BACKUP; no remote ref; superseded by phase-2 branch |
| fix/repository-health-remediation-2026-09-21 | 4 | STALE (net deletions vs main per prior audit) |
| origin/ui/v1 | 1 | STALE doc-only (backend audit/UI handoff) |
| chore/…, codex/ds-000027-dr-ares, integration/…-consolidation, integration/…-superset, research/senior-health-forensic-v2, main (local) | 0 | MERGED / stale pointers |

Worktrees: `/private/tmp/wt-integration` is registered but the directory is gone (prunable); `/Users/ghilmankhan/workprojects/yios-expansion` is a live worktree with **1 uncommitted modified tracked file** (`forensic-v3/scripts/build_master_inventory.py`, the multi-directory metadata merge enhancement). That change exists nowhere else.

## 4. Local Working Tree Reality

Main checkout: clean. Ignored-but-present local-only content (not on any remote): `data/raw/first-party/` (70 files, 0.8 MB, Studio ZIPs/JSON), `data/raw/competitors/DS-000032/public-browser-2026-09-27/` (75 files, 10 MB; 56 thumbnails, 14 contact sheets), `data/raw/competitors/DS-000030/apify/*/evidence/run_metadata.json`, `output/chair-stand-safety/` (38 files, 3 MB, a Shorts production project), `outputs/` (15 files, 15.6 MB, 3 Apify run folders), `output.zip` (2.8 MB). Caches: `.venv`, `.pytest_cache`, `.ruff_cache`, `__pycache__`, egg-info.

Outside the repo: ~/Downloads holds the original Studio export ZIPs for Decode Your Heart (byte-identical to the ignored repo copies), older copies of the Rehan workbook/DOCX, several Rehan production workbooks and an mp4 that are not registered anywhere.

## 5. Repository Structure

| Path | Purpose | Class | Git state | Files | MB | Status |
|---|---|---|---|---:|---:|---|
| `data/raw/competitors` | Raw competitor/own evidence by dataset (screenshots, Apify payloads, transcripts) | AUTHORITATIVE | 803 tracked / 76 ignored | 879 | 619.7 | CURRENT |
| `data/raw/channel-data` | Immutable Apify JSON + supplied workbooks (DS-020..027) | AUTHORITATIVE | tracked | 88 | 33.4 | CURRENT |
| `data/raw/forensic-analysis` | Forensic video reconstructions DS-002,012-016 | AUTHORITATIVE | tracked | 1314 | 228.4 | LEGACY |
| `data/raw/global-youtube-knowledge` | DS-011/018/031 knowledge sources | AUTHORITATIVE | tracked | 20 | 7.6 | CURRENT |
| `data/raw/first-party` | Private YouTube Studio exports (DS-032) | AUTHORITATIVE, PRIVATE | IGNORED, local-only | 70 | 0.8 | CURRENT |
| `data/manifests` | Dataset manifests, ledgers, Apify run manifests | AUTHORITATIVE | tracked | 105 | 14.1 | CURRENT (no DS-026, no DS-034 in this checkout) |
| `data/extracted` | Standard channel packages (xlsx + transcript ZIP) and combined exports | DERIVED | tracked | 152 | 143.8 | CURRENT |
| `data/catalog` | Inventory DB (historical, 25 datasets) + registry DB (LFS) + channel_registry ledgers | DERIVED | tracked (registry via LFS) | 5 | 193.7 | registry CURRENT; inventory STALE/historical |
| `data/normalized` | Registry JSON/ledger exports | DERIVED | tracked | 3 | 0.8 | CURRENT |
| `data/intelligence` | V1 intelligence artifacts for 5 legacy channels + global + system registries | DERIVED | tracked | 69 | 8.9 | CURRENT for 5 channels; dated 2026-09-11 |
| `docs/audits` | Prior audits/checkpoints (29 files) | DERIVED | tracked | 29 | 1.4 | MIXED, see section 16 |
| `docs/research/senior-health-2026-09-25` | Senior Health forensic V1/V2/V3 research | DERIVED | tracked | 194 | 8.7 | V3 current; V1/V2 superseded |
| `docs/research/decode-your-heart-2026-09-27` | DYH report, workbook, evidence register, checkpoint | DERIVED, PRIVATE METRICS | tracked + on remote (private repo) | 6 | 2.2 | CURRENT, contains stale text |
| `exports` | 2026-09-27 master knowledge + Senior Health export (docx/xlsx/json/zip) | EXPORT | tracked | 16 | 23.3 | CURRENT but duplicate of data/raw |
| `scripts` | Pipelines, reporters, validators | CODE | tracked | 61 | 1.5 | CURRENT |
| `tests` | pytest suite (407 tests) | CODE | tracked | 43 | 0.4 | 1 failing |
| `schemas / config / channels / timeline / logs / .github / .codex` | SQL schemas, READMEs, CI workflow, Codex skills | CODE/CONFIG | tracked |  |  | CURRENT |
| `output/, outputs/, output.zip` | Production project + early Apify outputs | CACHE/EXPORT | IGNORED, local-only | 54 | 21.4 | TEMPORARY/LEGACY; outputs/ duplicates data/extracted |

Tracked file mix: 2,988 files; 1,320 JPG (155 MB), 129 PNG (568 MB), 380 JSON, 66 CSV, 65 XLSX, 51 ZIP, 4 WAV (74 MB), 2 DB (194 MB).

## 6. Dataset Inventory

Highest registered dataset in this checkout: **DS-000033**. DS-000034 exists on the PR #6 branch only. **DS-000035 does not exist.** DS-000026 never started (2 preflight files, no manifest). The registry holds 32 datasets; the historical inventory DB holds 25.

| ID | Class | Name/purpose | Source | Date | Raw files/MB (tracked) | Registry ch/vid/real tr | Evidence | Limitations |
|---|---|---|---|---|---|---|---|---|
| DS-000001 | CHANNEL_DATA / LEGACY | Matty Invests + Mr. Finance competitor export (historical catalog format) | Apify-style export in historical catalog | 2026-08-27 | 2/1.6 (2) | 2/159/158 | 159 videos; 158 real transcripts; 94+65 videos have no raw video_type (UNKNOWN); no thumbnail URLs | Historical; depends on inventory DB for operational rows |
| DS-000002 | FORENSIC_VISUAL | Forensic reconstruction of one finance video (frames/audio) | User-supplied forensic bundle | 2026-08-27 | 4/0.7 (4) | 0/0/0 | Video-level forensic evidence only; no channel video population | Historical case study |
| DS-000003 | METADATA_DISCOVERY (screenshots) | Doctor Thomas channel screenshots | User screenshots (2026-08-16) | 2026-08-27 | 5/26.4 (5) | 0/0/0 | 5 screenshots; superseded for data by DS-000029 | Screenshot-only; no video population |
| DS-000004 | METADATA_DISCOVERY (screenshots) | Dr. Adewale screenshots | User screenshots | 2026-08-27 | 13/72.3 (13) | 0/0/0 | 13 screenshots; identity unresolved (SUBJ-000001) | Not a canonical channel |
| DS-000005 | METADATA_DISCOVERY (screenshots) | Dr. Okoro screenshots | User screenshots | 2026-08-27 | 10/56.4 (10) | 0/0/0 | 10 screenshots; superseded by DS-000028 | Screenshot-only |
| DS-000006 | CHANNEL_DATA / LEGACY | Dr. Aliza Wright / Advice screenshots plus supplied video export | User screenshots + supplied snapshot | 2026-08-27 | 71/40.3 (71) | 1/32/32 | 32 videos, 32 real transcripts; 32 CURRENT_PUBLIC thumbnails (tracked) | Historical catalog channel |
| DS-000007 | METADATA_DISCOVERY (screenshots) | Dr. Waterling screenshots | User screenshots | 2026-08-27 | 13/54.1 (13) | 0/0/0 | 13 screenshots; identity unresolved (SUBJ-000002) | Not a canonical channel |
| DS-000008 | METADATA_DISCOVERY (screenshots) | The Senior Health Podcast screenshots | User screenshots | 2026-08-27 | 37/151.9 (37) | 0/0/0 | 37 screenshots; identity unresolved (SUBJ-000003) | Not a canonical channel |
| DS-000009 | METADATA_DISCOVERY (screenshots) | Senior Health Hub screenshots | User screenshots | 2026-08-27 | 24/99.5 (24) | 0/0/0 | 24 screenshots; superseded by DS-000030 | Screenshot-only |
| DS-000010 | METADATA_DISCOVERY (screenshots) | The Health Educator screenshots | User screenshots | 2026-08-27 | 11/65.6 (11) | 0/0/0 | 11 screenshots; identity unresolved (SUBJ-000004) | Not a canonical channel |
| DS-000011 | GLOBAL_KNOWLEDGE | All Training Data of YouTube: creative/reference guides (PDF/DOCX/MD) | User-supplied corpus | 2026-08-27 | 17/7.0 (17) | 0/0/0 | 17 files, 16 unique texts, 17 extracted rules (11 AI-synthesis, 3 human, 3 creator-attributed) | Rules are not platform facts |
| DS-000012 | FORENSIC_VISUAL | Sunset video forensic reconstruction, case 1 | User forensic bundle | 2026-08-27 | 7/1.2 (7) | 1/0/0 | 7 files; relationship to DS-000015 = SAME_SOURCE_INDEPENDENT_ANALYSIS | Do not treat DS-000012/15 as independent evidence |
| DS-000013 | FORENSIC_VISUAL | Moon/electron physics video reconstruction | User forensic bundle | 2026-08-27 | 63/27.8 (63) | 1/0/0 | 63 files, frames + audio | Historical case study |
| DS-000014 | FORENSIC_VISUAL | 'Weird and Worrying Questions' reconstruction | User forensic bundle | 2026-08-27 | 54/17.3 (54) | 1/0/0 | 54 files | Historical case study |
| DS-000015 | FORENSIC_VISUAL | Sunset video reconstruction, case 2 (re-run) | User forensic bundle | 2026-08-27 | 50/31.0 (50) | 1/0/0 | 50 files | Same source as DS-000012 |
| DS-000016 | FORENSIC_VISUAL | Retiree daily-routines video reconstruction | User forensic bundle | 2026-08-27 | 1135/150.5 (1135) | 0/0/0 | 1,135 files (1,102 forensic images); only dataset giving FORENSIC_VIDEO_EVIDENCE for CH-000004 (xkcd) | Editing intelligence rests only on this |
| DS-000017 | CHANNEL_DATA / LEGACY | xkcd's What If? Apify acquisition | Apify | 2026-08-31 | 167/6.8 (167) | 1/83/83 | 83 videos, 83 real transcripts, 83 thumbnails (CURRENT_PUBLIC) | Registered via historical catalog |
| DS-000018 | GLOBAL_KNOWLEDGE | 2026 Algorithm Update multi-tab creator research corpus (ZIP, 63 tabs) | User-supplied corpus | n/a | 1/0.6 (1) | 0/0/0 | 33 original claims audited (10 SUPPORTED/12 PARTIAL/1 CONTRADICTED/8 NOT_SUPPORTED/2 NOT_VERIFIABLE); 666 further AI-extracted claims unvalidated, exports only | Creator claims, not official YouTube facts |
| DS-000019 | CHANNEL_DATA / LEGACY | Dr. Elias Senior Health supplied canonical export | User-supplied workbook | n/a | 60/5.8 (60) | 1/29/29 | 29 videos, 29 transcripts, 29 CURRENT_PUBLIC thumbnails | Repo holds 29; live public count 43 at 2026-09-28 |
| DS-000020 | CHANNEL_DATA | Five-channel Apify packages | Apify | n/a | 3/2.1 (3) | 5/132/132 | 5 channels, 132 videos, 132 transcripts | Standard package |
| DS-000021 | CHANNEL_DATA | Eleven-channel Apify packages | Apify | n/a | 1/4.6 (1) | 11/216/216 | 11 channels, 216 videos, 216 transcripts | Standard package |
| DS-000022 | CHANNEL_DATA | Seven user-provided channel packages | User workbooks + transcript ZIPs + 1 targeted Apify recovery | n/a | 18/7.2 (18) | 7/732/722 | 7 channels, 732 videos, 722 real + 10 members-only placeholders | 10 Lucas Grant transcripts unavailable |
| DS-000023 | CHANNEL_DATA | Funded master extraction batch 1 | Apify | n/a | 8/6.3 (8) | 5/110/110 | 5 channels, 110 videos, 110 transcripts | Standard package |
| DS-000024 | CHANNEL_DATA | Funded master extraction batch 2 | Apify | n/a | 11/3.6 (11) | 4/178/178 | 4 channels, 178 videos, 178 transcripts | Standard package |
| DS-000025 | CHANNEL_DATA | Funded master extraction batch 3 | Apify | n/a | 25/7.3 (25) | 3/233/233 | 3 channels, 233 videos, 233 transcripts | Standard package |
| DS-000026 | PROPOSAL_ONLY | Planned 29-channel acquisition; never started | Preflight JSON only | n/a | 2/0.0 (2) | 0/0/0 | 2 preflight files; no manifest, not in registry or inventory | Unstarted; 29 identity-only channels remain unacquired |
| DS-000027 | CHANNEL_DATA | Dr. Ares Senior complete extraction (Senior Health) | Apify | n/a | 19/2.3 (19) | 1/35/35 | 35 videos, 35 transcripts, 35 thumbnail URLs, 0 local thumbnails | Live public count 39 at 2026-09-28 (4 new) |
| DS-000028 | CHANNEL_DATA | Dr. Okoro complete extraction (Senior Health) | Apify | n/a | 73/3.2 (73) | 1/66/66 | 66 videos (65 regular/1 Short), 66 transcripts, 66 thumbnail URLs | Complete at 2026-09-28 snapshot |
| DS-000029 | CHANNEL_DATA | Doctor Thomas acquisition (Senior Health) | Apify | 2026-09-23 | 25/7.3 (25) | 1/22/21 | 22 videos, 21 transcripts + 1 placeholder | Complete at snapshot |
| DS-000030 | CHANNEL_DATA | Senior Health Hub acquisition (Senior Health) | Apify | 2026-09-24 | 127/5.7 (126) | 1/122/122 | 122 videos, 122 transcripts; registry counts SHH as HISTORICAL_CATALOG with 0 thumbnail URLs in `videos` | Live public count 124 (+2 Shorts) |
| DS-000031 | GLOBAL_KNOWLEDGE | Creator strategy, audience psychology and experimentation corpus | User-supplied corpus | 2026-09-24 | 1/0.1 (1) | 0/0/0 | 1 file, 15 segments, 63 concepts, 15 formulas; 52/63 concepts tagged heuristic-not-platform-rule | Strategy heuristics, not facts |
| DS-000032 | FIRST_PARTY + CHANNEL_DATA (own) | Decode Your Heart - Dr. Rehan (OWN channel) public acquisition; Studio exports live under ignored data/raw/first-party | Apify + authenticated browser + Studio exports | 2026-09-25 | 135/11.1 (60) | 1/56/56 | 56 videos (27 regular/29 Shorts), 56 transcripts, 56 local thumbnails (ignored), Studio exports local-only | Manifest still labels it 'Competitor evidence, not yet analyzed' |
| DS-000033 | CHANNEL_DATA | Better Health While Aging acquisition (Senior Health) | Apify (+4-Short backfill) | 2026-09-25 | 105/11.7 (105) | 1/98/98 | 98 videos (80 regular/18 Shorts), 98 transcripts, 98 thumbnail URLs, 0 local thumbnails | Complete at 2026-09-28 snapshot |
| DS-000034 | METADATA_DISCOVERY | Senior Health public per-video metadata, 2026-09-28 (partial, zero-spend) | Public YouTube web player endpoint, unauthenticated | 2026-09-28 | - | n/a | 72 files, 4,648 successful records (63 channels), 359 bot-check refusals of which 235 unresolved; 403 IDs overlap registry, 4,245 new | BRANCH-ONLY: exists on PR #6 head 814a027 and worktree yios-expansion, absent from this checkout; metadata only, no transcripts/thumbnails |
| DS-000035 | NOT_PRESENT | Claimed in session memory as collecting more Senior Health metadata | none on disk | n/a | - | n/a | No manifest, files or staging directory found anywhere on this machine | LOST_OR_NEVER_PRESERVED |

Classes in this checkout: CHANNEL_DATA 17 (DS-001, 006, 017, 019-025, 027-030, 033, plus own 032), GLOBAL_KNOWLEDGE 3, FIRST_PARTY 1 (DS-032, mixed), FORENSIC_VISUAL 6, METADATA_DISCOVERY 7 screenshot sets (+DS-034 branch-only), PROPOSAL_ONLY 1 (DS-026).

Historical descriptions checked: DS-011 (creative/reference knowledge) CONFIRMED; DS-018 (creator claims) CONFIRMED but split 33 audited vs 666 AI unvalidated; DS-031 CONFIRMED; DS-032 CONFIRMED as own channel (manifest wording still says 'Competitor evidence'); DS-033 CONFIRMED; DS-034 CONFIRMED with corrections: 72 channel files / 63 channels with data / 4,648 records / 235 unresolved refusals (the 'partial, zero-spend' title is accurate).

Duplication check before treating datasets as independent: DS-012/DS-015 share a source (`SAME_SOURCE_INDEPENDENT_ANALYSIS`); screenshot datasets DS-003/005/009 are superseded by DS-029/028/030 for the same channels; DS-034's 403 overlapping video IDs duplicate registry rows for the 7 acquired channels and must not be counted twice.

## 7. Channel Inventory

Canonical identities (deduplicated by YouTube Channel ID, registry): **75**. With video-level data **46** (40 standard packages + 6 historical-format; 41 package workbooks incl. Senior Health Hub/Doctor Thomas which are also historical). Identity-only **29** (identity verified, no data extracted). Metadata-only channels in this checkout: **0** (DS-034 metadata-only coverage is branch-only). Channels with real transcripts: 46. With thumbnail URLs in registry `videos`: 41 (inventory DB adds Aliza, Elias, xkcd, Senior Health Hub; Mr. Finance and Matty Invests have none anywhere). With downloaded local thumbnails: 4 (Aliza 32, Elias 29, xkcd 83, Rehan 56). With forensic video evidence: 1 (CH-000004 xkcd). With first-party Analytics ingested through the pipeline: 0 (registry: all 75 `SCHEMA_READY_NO_DATA`); Rehan Studio exports exist locally outside the pipeline. Removed/unavailable identities: 0 in registry (11 in the branch-only Senior Health inventory). Non-channel subjects: 4 (screenshot-only: Dr. Adewale, Dr. Waterling, The Senior Health Podcast, The Health Educator).

Niche is not a registry field. Niche below comes from `docs/audits/CHANNEL-NICHE-SUBNICHE-AUDIT.md` (2026-09-20, 70 channels, name-matched). 6 channels did not name-match or post-date it (marked UNKNOWN; they are all Senior Health/own-channel health channels): INFERRED Health / Senior Health.

**Master channel table (46 channels with video data).** Intel = registry intelligence_status (VALIDATED = generated artifacts exist; DATA_READY = engines can run, no artifact). R/S/U = regular/Shorts/unknown type. TR = real transcripts/placeholders. Thumb = URL in registry / local file. Complete 75-row table incl. per-capability status is in the JSON companion.

| Channel ID | Name | Datasets | Niche (conf.) | Role | Videos (R/S/U) | Desc | TR | Thumb URL/local | Registry status | Intel |
|---|---|---|---|---|---|---:|---|---|---|---|
| `UCAKBDBaY1dP7OdZkGPiDnug` | Bob Invests | DS-000022 | Finance (VERIFIED) | COMP/REF | 57 (57/0/0) | 57 | 57/0 | 57/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UC1GwXFBhh1fiLLuZxs8VRXA` | Brimm. | DS-000024 | Finance (HIGH) | COMP/REF | 44 (44/0/0) | 44 | 44/0 | 44/0 | COMPLETE | DATA_READY |
| `UCxoC2voi0vPg2hwqgfjdhYw` | Carl Invests | DS-000022 | Finance (VERIFIED) | COMP/REF | 80 (80/0/0) | 80 | 80/0 | 80/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UCP9RPj_BG0vit2TNM7LuRxA` | Crayon Capital | DS-000023 | Finance (HIGH) | COMP/REF | 30 (30/0/0) | 30 | 30/0 | 30/0 | COMPLETE | DATA_READY |
| `UCDglfjh__GM2RFM1oAL3a6A` | Dark Ledger | DS-000021 | Finance (HIGH) | COMP/REF | 38 (38/0/0) | 38 | 38/0 | 38/0 | COMPLETE | DATA_READY |
| `UCTcOboZIhgrKHMDm-oTlTOg` | Lucas Grant | DS-000022 | Finance (HIGH) | COMP/REF | 95 (95/0/0) | 95 | 85/10 | 95/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UCkqzov98m_7niJOXwbRQgBA` | Matty Invests | DS-000001 | Finance (VERIFIED) | COMP/REF | 94 (0/0/94) | 94 | 93/1 | 0/0 | COMPLETE_WITH_LIMITATIONS | PARTIAL |
| `UCCEwJbv7D1CYzxdKYYOH6AA` | Money Life POV | DS-000020 | Finance (HIGH) | COMP/REF | 20 (20/0/0) | 20 | 20/0 | 20/0 | COMPLETE | DATA_READY |
| `UC6AwWrRKNrwt83CMJqeTUzw` | Mr. Finance | DS-000001 | Finance (VERIFIED) | COMP/REF | 65 (0/0/65) | 65 | 65/0 | 0/0 | COMPLETE_WITH_LIMITATIONS | PARTIAL |
| `UCXzNNA2ngRpRiWvyA7eGd6w` | Nick Invests | DS-000022 | Finance (VERIFIED) | COMP/REF | 363 (363/0/0) | 363 | 363/0 | 363/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UC14Fb2zWTEZklONPXFbLrTQ` | Primate Economics | DS-000020 | Finance (VERIFIED) | COMP/REF | 28 (15/13/0) | 15 | 28/0 | 28/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UC5ZSqmk7PKry99xdiRDrc0A` | Shaami Finance | DS-000021 | Finance (VERIFIED) | COMP/REF | 13 (13/0/0) | 13 | 13/0 | 13/0 | COMPLETE | DATA_READY |
| `UCFvEZUMNoAVjSoSB8NrV7yw` | Sonny Finance | DS-000020 | Finance (HIGH) | COMP/REF | 39 (39/0/0) | 39 | 39/0 | 39/0 | COMPLETE | DATA_READY |
| `UCGnTHU6UMQQlR6cl4CP3jlg` | Apesthetic | DS-000020 | Fitness (HIGH) | COMP/REF | 22 (21/1/0) | 21 | 22/0 | 22/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UCQTcmLiL5_HMUnO1GRwCdjQ` | Bro Pump | DS-000023 | Fitness (VERIFIED) | COMP/REF | 21 (21/0/0) | 21 | 21/0 | 21/0 | COMPLETE | DATA_READY |
| `UC356D-NzdnznBOftTpYoBLw` | Dr. Ares Senior | DS-000027 | Health (HIGH) | COMP/REF | 35 (35/0/0) | 35 | 35/0 | 35/0 | COMPLETE | DATA_READY |
| `UCQcBYZxFW7YwNMU8-DsT3Uw` | Dr. Elias Senior Health | DS-000019 | Health (VERIFIED) | COMP/REF | 29 (29/0/0) | 29 | 29/0 | 29/29 | COMPLETE | PARTIAL |
| `UC-q0RDBWjYlYA2KkPzq0WSQ` | Genius History | DS-000021 | History (VERIFIED) | COMP/REF | 10 (10/0/0) | 10 | 10/0 | 10/0 | COMPLETE | DATA_READY |
| `UC96yqt8xjtShTpgdoIo0Lqg` | Lost Legacy | DS-000024 | History (HIGH) | COMP/REF | 45 (45/0/0) | 45 | 45/0 | 45/0 | COMPLETE | DATA_READY |
| `UCJgTBuO9fbNvgL_IS8pqtqg` | Maximus | DS-000023 | History (HIGH) | COMP/REF | 5 (5/0/0) | 5 | 5/0 | 5/0 | COMPLETE | DATA_READY |
| `UCm1yxl_4qMbStLHpHQu6xWg` | Unknown Frequencies | DS-000021 | History (VERIFIED) | COMP/REF | 19 (19/0/0) | 19 | 19/0 | 19/0 | COMPLETE | DATA_READY |
| `UCW4NZzZ-6At6DFrCn7rJ0bQ` | Well. | DS-000022 | History (HIGH) | COMP/REF | 32 (32/0/0) | 32 | 32/0 | 32/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UCJqZXjdkolPUgVcf6WBm8VA` | ago. | DS-000024 | History (HIGH) | COMP/REF | 50 (50/0/0) | 50 | 50/0 | 50/0 | COMPLETE | DATA_READY |
| `UCK8TbMQGDbB94EOR3aGJo3Q` | Zenn | DS-000021 | Psychology / Human Behaviour (HIGH) | COMP/REF | 35 (35/0/0) | 35 | 35/0 | 35/0 | COMPLETE | DATA_READY |
| `UC9ibMPcwu9pesqKEyzlut7w` | CIPHER UNIT | DS-000021 | Science / Knowledge (HIGH) | COMP/REF | 17 (17/0/0) | 17 | 17/0 | 17/0 | COMPLETE | DATA_READY |
| `UCmYG4TVuzHphjTrP3YKYGYQ` | Explain In Paint | DS-000025 | Science / Knowledge (VERIFIED) | COMP/REF | 82 (82/0/0) | 82 | 82/0 | 82/0 | COMPLETE | DATA_READY |
| `UCpgrEMx8diLrw7YNQ6r3uUw` | Ink Explainer | DS-000021 | Science / Knowledge (VERIFIED) | COMP/REF | 15 (15/0/0) | 15 | 15/0 | 15/0 | COMPLETE | DATA_READY |
| `UChGF6aMxELhXOKg2EDDLYNg` | Luco | DS-000021 | Science / Knowledge (HIGH) | COMP/REF | 4 (4/0/0) | 4 | 4/0 | 4/0 | COMPLETE | DATA_READY |
| `UCaS30yIIV6y2zqSnHGdIGMQ` | Mack | DS-000025 | Science / Knowledge (VERIFIED) | COMP/REF | 76 (76/0/0) | 76 | 76/0 | 76/0 | COMPLETE | DATA_READY |
| `UCxyQ6jK98CCOsy-gwV8QaFA` | Oddlyhuman | DS-000021 | Science / Knowledge (VERIFIED) | COMP/REF | 13 (13/0/0) | 13 | 13/0 | 13/0 | COMPLETE | DATA_READY |
| `UCS3iXffTKXrhKWGXaPckb8A` | Past Tense | DS-000021 | Science / Knowledge (HIGH) | COMP/REF | 24 (24/0/0) | 24 | 24/0 | 24/0 | COMPLETE | DATA_READY |
| `UC53wkzZ3aXyeH9-eIgi17WA` | Stickly | DS-000025 | Science / Knowledge (VERIFIED) | COMP/REF | 75 (75/0/0) | 75 | 75/0 | 75/0 | COMPLETE | DATA_READY |
| `UCFKmBxFC3dOkUv1GirzTjww` | Tp Dossier | DS-000022 | Science / Knowledge (VERIFIED) | COMP/REF | 92 (92/0/0) | 92 | 92/0 | 92/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UChFs6t9iB1yv0X8fuKtNIvA` | Zoozle | DS-000023 | Science / Knowledge (HIGH) | COMP/REF | 39 (39/0/0) | 39 | 39/0 | 39/0 | COMPLETE | DATA_READY |
| `UCcWtWryYdHHiNWfZGSROl1A` | inkly | DS-000021 | Science / Knowledge (HIGH) | COMP/REF | 28 (28/0/0) | 28 | 28/0 | 28/0 | COMPLETE | DATA_READY |
| `UC6IxnFzHofFJ5X2PycSMsww` | xkcd's What If? | DS-000012;DS-000013;DS-000014;DS-000015;DS-000017 | Science / Knowledge (VERIFIED) | COMP/REF | 83 (43/40/0) | 83 | 83/0 | 0/83 | COMPLETE_WITH_LIMITATIONS | PARTIAL |
| `UC0L9hD7HMwWU7xuU5HRA6Iw` | Hypothetically | DS-000024 | Storytelling (HIGH) | COMP/REF | 39 (39/0/0) | 39 | 39/0 | 39/0 | COMPLETE | DATA_READY |
| `UCNO35SZS-e3f1hLIDon_mag` | Just Some Guy Stories | DS-000022 | Storytelling (HIGH) | COMP/REF | 13 (13/0/0) | 13 | 13/0 | 13/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UC9m3w-9L_Bt34x02IQXQ5kg` | My Chaotic Stories | DS-000020 | Storytelling (HIGH) | COMP/REF | 23 (23/0/0) | 23 | 23/0 | 23/0 | COMPLETE | DATA_READY |
| `UCeVwhrEnYjCNdaDr47x4dSw` | The Life Outline | DS-000023 | Storytelling (HIGH) | COMP/REF | 15 (15/0/0) | 15 | 15/0 | 15/0 | COMPLETE | DATA_READY |
| `UCFpxvukIqCAUA7YizI-q9Dw` | Better Health While Aging | DS-000033 | UNKNOWN (NOT_IN_2026-09-20_AUDIT) | COMP/REF | 98 (80/18/0) | 98 | 98/0 | 98/0 | COMPLETE | DATA_READY |
| `UCQIzqH7QZ9viBYpOFqgSXMg` | Decode Your Heart - Dr. Rehan | DS-000032 | UNKNOWN (NOT_IN_2026-09-20_AUDIT) | OWN | 56 (27/29/0) | 56 | 56/0 | 56/56 | COMPLETE | DATA_READY |
| `UCFuGMi0idGeyXl6wYK9hg7Q` | Doctor Thomas | DS-000029 | UNKNOWN (NOT_IN_2026-09-20_AUDIT) | COMP/REF | 22 (22/0/0) | 21 | 21/1 | 22/0 | COMPLETE_WITH_LIMITATIONS | DATA_READY |
| `UCXZi5JVeuTluazF-fYqQgNA` | Dr. Aliza Wright / Advice | DS-000006 | UNKNOWN (NOT_IN_2026-09-20_AUDIT) | COMP/REF | 32 (32/0/0) | 32 | 32/0 | 0/32 | COMPLETE | PARTIAL |
| `UCMJxAeBJ0d1JC937de1eZ0Q` | Dr. Okoro | DS-000028 | UNKNOWN (NOT_IN_2026-09-20_AUDIT) | COMP/REF | 66 (65/1/0) | 66 | 66/0 | 66/0 | COMPLETE | DATA_READY |
| `UCAYG0fzUyxv6OevH88qA45w` | Senior Health Hub | DS-000030 | UNKNOWN (NOT_IN_2026-09-20_AUDIT) | COMP/REF | 122 (120/2/0) | 120 | 122/0 | 0/0 | COMPLETE_WITH_LIMITATIONS | PARTIAL |

**Identity-only channels (29)** — identity verified from official sources, zero video data, never acquired (the unstarted DS-000026 population): Alicia Invests (Finance); Bernard (History); Brick Body (Fitness); Brofessor Stein (History); Casual Finance (Finance); Casually Explained (Humor / Comedy); Chat History (History); Chill Dude Explains (Science / Knowledge); David Explains Money (Finance); Fasted Fred (Health); Finance Simplified (Finance); Ivan Invests (Finance); Mark - Retired at 55 (Finance); Max Invests (Finance); Millionaire Problems (Finance); Neu (Finance); Nostalgic Wheels (Finance); Overhead (Finance); Parenting Hacks (Parenting); Parentitude (Parenting); Rick Finance (Finance); The Career Machine (Career / Self-Improvement); The Expensive Part (History); The Wise Future (Finance); Tom - Lazy Dividend Investor (Finance); Tom - Lazy Investor (Finance); Tom Talks Money (Finance); Wealth Logic (Finance); quack doc (Science / Knowledge).

Own channel: **Decode Your Heart - Dr. Rehan** (`UCQIzqH7QZ9viBYpOFqgSXMg`, DS-000032). It is the only OWN channel and must never be pooled with competitor aggregates. Note: registry role flag is derived from DS-000032 membership; the manifest itself still labels it competitor evidence.

## 8. Senior Health Inventory

Old figures (6/7 channels, 14/19 pending, 69 leads, 143 inventory channels) were re-derived. Results depend on which checkout is read:

| View | Source | Rows | Notes |
|---|---|---:|---|
| This checkout (HEAD) | `forensic-v3/SENIOR-HEALTH-MASTER-INVENTORY.json` (2026-09-26) | 69 | STALE: classes A6/B1/E48/F13/OWN1; superseded by the 2026-09-28 rebuild |
| PR #6 / yios-expansion | `SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.json` | 143 rows | 138 unique canonical IDs + 5 removed handles with no ID (the '143 channels' figure over-counts channels by 5) |

**Current categories (PR #6 inventory, live snapshot 2026-09-28, recounted from JSON):**

| Category | Channels | Live public videos (R+S+L) | In repository |
|---|---:|---:|---:|
| OWN_CHANNEL (Dr. Rehan) | 1 | 56 | 56 |
| ACQUIRED competitors, complete at snapshot (Okoro, Doctor Thomas, Aliza Wright, BHWA) | 4 | 217 | 218 |
| ACQUIRED competitors with new public uploads (Senior Health Hub +2, Dr. Ares +4, Dr. Elias +14) | 3 | 206 | 186 |
| QUALIFIED_PENDING (not acquired; listing/metadata only) | 14 | 2,034 | 0 |
| HEALTH_RELEVANT_IDENTITY_ONLY | 71 | 6,505 | 0 |
| ADJACENT_HEALTH_REFERENCE | 35 | 7,359 | 0 |
| EXCLUDED_BY_REVIEW | 4 | 89 | 0 |
| REMOVED_OR_UNAVAILABLE (5 without channel ID) | 11 | 0 | 0 |

Acquired Senior Health competitors = **7** (Senior Health Hub, Dr. Okoro, Doctor Thomas, Dr. Aliza Wright, Dr. Ares, Dr. Elias, Better Health While Aging); 404 videos in repository vs 423 live. International (non-US) channels in inventory: 39 (13 adjacent, 11 identity-only, 11 removed, 3 pending, 1 acquired). Failure-comparison (`prior_class=breakout_failure`): 4, all identity-only. **Metadata-only channels with per-video records (DS-034, branch-only): 63**, of which 13 of the 14 pending channels are PER_VIDEO_COMPLETE; all 7 acquired channels are PER_VIDEO_COMPLETE. Estimated cost to acquire the 14 pending channels: $8.136 (2,034 results at $0.004, REPORTED, unverified price); nothing has been spent on it.

| Acquired channel | Channel ID | DS | Videos in repo | Transcripts | Thumbnail URLs / local | Live count (2026-09-28) |
|---|---|---|---:|---:|---|---|
| Senior Health Hub | `UCAYG0fzUyxv6OevH88qA45w` | DS-030 | 122 | 122 | URL in inventory only / 0 | 124 |
| Dr. Okoro | `UCMJxAeBJ0d1JC937de1eZ0Q` | DS-028 | 66 | 66 | 66 / 0 | 66 |
| Doctor Thomas | `UCFuGMi0idGeyXl6wYK9hg7Q` | DS-029 | 22 | 21+1 placeholder | 22 / 0 | 21 listed (+DS-034 differences) |
| Dr. Aliza Wright | Advice | `UCXZi5JVeuTluazF-fYqQgNA` | DS-006 | 32 | 32 | inventory / 32 | 32 |
| Dr. Ares Senior | `UC356D-NzdnznBOftTpYoBLw` | DS-027 | 35 | 35 | 35 / 0 | 39 |
| Dr. Elias Senior Health | `UCQcBYZxFW7YwNMU8-DsT3Uw` | DS-019 | 29 | 29 | 29 / 29 | 43 |
| Better Health While Aging | `UCFpxvukIqCAUA7YizI-q9Dw` | DS-033 | 98 | 98 | 98 / 0 | 98 |
| Decode Your Heart - Dr. Rehan (OWN) | `UCQIzqH7QZ9viBYpOFqgSXMg` | DS-032 | 56 | 56 | 56 / 56 (ignored) | 56 |

Missing video population: Dr. Elias 14, Dr. Ares 4, Senior Health Hub 2 (+ all pending/identity-only channels). The 14 qualified-pending channel list, costs and per-channel metadata coverage are in `SENIOR-HEALTH-MASTER-INVENTORY-REPORT-2026-09-28.md` on PR #6.

## 9. Video Inventory

| Metric | Count | Basis |
|---|---:|---|
| Unique canonical videos (registry) | 2,303 | 0 duplicate IDs; sum of dataset_videos = 2,303; all 2,000 package workbook IDs present; remaining 303 are historical-catalog rows |
| With description | 2,286 | 17 have a documented unavailable reason in availability_gaps |
| With publication date / duration | 2,303 / 2,303 |  |
| With public views / likes / comments | 2,293 / 2,303 / 2,303 | 10 NULL views (Lucas Grant) |
| Regular | 2,040 | normalised via `video_type_classification.py` (raw vocabulary: video, regular video, Short, shorts, NULL) |
| Shorts | 104 |  |
| Streams | 0 | raw vocabulary has no stream label; UNKNOWN whether any streams are inside 'video' |
| UNKNOWN type | 159 | Mr. Finance 65 + Matty Invests 94, raw type NULL; all 159 have duration >180 s, so likely regular but NOT classified (INFERRED) |
| Inconsistency flags | 3 | 3 'regular' videos with duration <=60 s; 0 Shorts >181 s |
| Registry thumbnail URLs | 1,907 | 396 videos (SHH 122, Matty 94, xkcd 83, Mr. Finance 65, Aliza 32) have none in registry; inventory DB covers 237 of them; 159 have none anywhere |

The earlier '216 gap' is NOT a video-type count. `availability_gaps` has 216 rows: 159 video_type, 29 identity-only channels, 17 descriptions, 10 views, 1 handle. The true unresolved video-type count is **159**, unchanged by raw-data recovery because the source rows carry no type.

Note: 2,303 here vs the 2,299 reported by a later agent (UNREPRODUCED; no artifact found). DS-034 adds 4,245 unique video IDs of metadata-only evidence (branch-only), not counted above.

## 10. Transcript Inventory

| Metric | Count |
|---|---:|
| Videos | 2,303 |
| Real transcripts with text (word_count > 0) | 2,291 |
| Placeholders (explicit unavailable reason) | 12 (10 members-only Lucas Grant, 1 Mr. Finance/DS-001, 1 Doctor Thomas) |
| Missing (no row) | 0 |
| user_generated captions | 172 (+26 'user, auto') |
| auto_generated captions | 2,042 (+34 'auto, user') |
| Caption type unknown on real transcripts | 17 |
| Subtitle track rows | 2,455 |
| Distinct hash groups shared by >1 video | 2 (identical transcript text on different videos; unexplained) |

Checks: all 41 transcript ZIPs contain exactly (registry count + 1 index file); 2,000 package transcripts reconcile with the registry. Registry transcript rows carry text, so DB-only rows are not counted without text. Archive-only / catalog-only: DS-001's 159-video transcript archive and the historical-channel transcripts are retained in ZIPs referenced by `evidence_locator`. The knowledge export carries 459 transcript copies of which 183 match `data/raw` byte-for-byte; 276 are a disclosed hash-drift set (export is a derived duplicate, not independent evidence). Transcript analysis is not playback analysis.

## 11. Thumbnail / Image Inventory

Verified from files (1,528 images on disk, all decodable, 1,528 unique SHA-256, 0 exact duplicates):

| Class | Count | Tracked | Ignored | Temporal alignment |
|---|---:|---:|---:|---|
| LOCAL_CURRENT_PUBLIC_THUMBNAIL | 200 | 144 | 56 | CURRENT_PUBLIC_ONLY |
| HISTORICAL_SNAPSHOT_THUMBNAIL | 0 | 0 | 0 | none exist; 'thumbnail-snapshot' manifests are 2026-09-09/10 current fetches |
| SCREENSHOT_DERIVED (DS-003..010 screenshots) | 120 | 120 | 0 | UNKNOWN (captured 2026-08-13/16, not mapped to videos) |
| FORENSIC_SUPPORT_IMAGE (incl. 1,012 video frames, 38 montages, 136 other) | 1,186 | 1,186 | 0 | n/a (video evidence) |
| CONTACT_SHEET (DS-032) | 14 | 0 | 14 | n/a |
| PREFLIGHT_UI | 2 | 2 | 0 | n/a |
| UNKNOWN (`output/chair-stand-safety` assets) | 6 | 0 | 6 | n/a |

Historical figures re-verified: 1,452 decodable tracked images = 144 + 120 + 1,186 + 2 EXACT. 144 registered snapshots (DS-006 32, DS-017 83, DS-019 29) EXACT. The later-agent figures do NOT reproduce: 2,299 videos (registry: 2,303); 2,131 newly downloaded / 2,275 local thumbnails / 24 failed URLs (NOT FOUND; local = 200); 78 audit records (remote checkpoint: 6); 140 similarity pairs (our dHash<=6 check gave 184 pairs but 171 are xkcd comics from one channel; unreliable; same-creative-different-resolution NOT computed).

URL vs file: registry has 1,907 thumbnail URLs (all `i.ytimg.com`); with inventory evidence 2,144 videos have a URL; 159 have none anywhere. 1,944 videos have a URL but no local file. Videos with at least one local thumbnail: 200; without: 2,103. Failed-download records: 0 on this machine (NOT FOUND for the claimed 24). Embedded images: 61 JPGs in `SUPPLEMENTAL-DATA-ARCHIVE.zip` and 6 in `output.zip` are exact duplicates of on-disk files; 14 PDFs contain ~240 image-object markers, UNCOUNTED. 5 local thumbnails are low-resolution AVIF. Dr. Rehan: 56 local thumbnails (ignored). Senior Health competitor thumbnails: 61 (Aliza 32, Elias 29); SHH, BHWA, Okoro, Ares have URLs but 0 local files.

`creative_temporal_alignment`: no thumbnail is HISTORICAL_SNAPSHOT_VERIFIED or SAME_PERIOD_VERIFIED. All 200 are CURRENT_PUBLIC_ONLY. Do not pair them with lifetime views; public views are not CTR.

## 12. Thumbnail Forensics Progress

The only forensic ledgers live on the REMOTE-ONLY branch `origin/research/senior-health-complete-local-sync` (commit 0cbabf5, 2026-10-02, `docs/research/thumbnail-forensics-2026-10-02/`, 18 files). They are NOT in HEAD, NOT in any local branch. Verified there: all 16 CHECKSUMS entries pass; ledger 144 unique rows, titles and views match registry; `local_path` values are foreign absolute paths (0 resolve literally; 144/144 resolve after remapping, SHA matches); asset inventory 7,031 rows (1,452 image rows match the tracked set; it omits the 56 ignored DS-032 images, so the DS-032 thumbnails are outside the ledger).

| Batch | Status | Evidence |
|---|---|---|
| B000 inventory | COMPLETE | asset-inventory.csv, inventory-summary.json |
| B001 individual audits | COMPLETE (6 rows) | 6 unique IDs; score components sum to total on all 6; identical `confidence`/`evidence_labels` strings on all 6; 2 of 6 are xkcd (not Senior Health) |
| B002 thumbnail audits (138) | PENDING | no files anywhere |
| B003 screenshot extraction (120) | PENDING | none |
| B004 support-image triage (1,186) | PENDING | none |
| B005 preflight (2) | PENDING | none |
| B006 document/PDF imagery | PENDING (scope uncounted) | none |
| B007 near-duplicate verification | PENDING | dHash probe only, not a verification |
| B008 title/metrics reconciliation | PENDING | none |
| B009 synthesis | PENDING | none |

Data-quality checks on audits: unique audits 6; duplicate audit rows 0; missing Thumbnail_ID 0; score arithmetic failures 0; generic duplicated prose: yes (all 6 share confidence/evidence strings); unmapped video IDs 0; current-vs-historical mismatch: all 144 ledger rows `temporal_alignment=UNKNOWN`, analytics columns empty. 83 of 144 ledger rows are xkcd with niche label 'Science explanations': only 61 are Senior Health. NOT FOUND anywhere: `thumbnail-universe.csv`, `visual-family-candidates.csv`, any B002+ audit batch. Visual research is NOT complete: 6 audits of 200 current thumbnails (3%).

DS-032 thumbnail inspection records (56) are marked COMPLETE but `intended_audience`, `analysis_basis`, `quality_status` are identical on all 56 and three more fields are identical on 46 of 56 (templated prose): treat as structured placeholders, not independent visual audits.

## 13. Decode Your Heart / Dr. Rehan Status

| Item | Current status |
|---|---|
| Videos | 56 (27 regular, 29 Shorts, 0 streams); public refresh 2026-09-28: 0 new |
| Descriptions / transcripts | 56 / 56 real (41 user-generated, 15 auto; 10 have caption timecode defects) |
| Thumbnail URLs / local images | 56 / 56 (ignored; sha256 matches recovery manifest) |
| Studio exports | 70 files in ignored `data/raw/first-party/youtube-studio/DS-000032`: 11 channel-level ZIPs + 56 per-video retention ZIPs + provenance JSON + derived `audience-retention-analysis.json`; originals byte-identical in ~/Downloads |
| Per-video metrics | 56 basic + 56 extended rows (private) |
| Retention | 56 exports; 46 with curves; 10 exported-but-empty (undisclosed, not zero); new/returning split for 12 |
| Channel-level search/suggested/geo/device/audience | PRESENT (channel level only) |
| Per-video search/suggested/traffic drill-downs | NOT EXPORTED |
| Playback investigations | Browser seek-sampling + frames: 44 sampled; 12 'reported full' backed only by text notes; 19 audio-level/cut pass (levels only; audio never listened); 12 storyboard reviews; 0 verified full playback, 0 spoken-audio reviews |
| Retention-linked investigations / matched comparisons | 46 / 22 (workbook sheet shows 7: different definition) |
| Medical claim review | 15 claims over 12 videos (5 need action); 44 videos NOT reviewed |
| Deliverables | Word report, Excel workbook, evidence register (56 records, 0 dup IDs, 0 broken pointers locally), checkpoint (status PARTIALLY_COMPLETE), HANDOFF-2026-09-28.md |
| First-party pipeline use | NOT USED: `ingest_youtube_analytics.py` / `report_first_party_channel_diagnosis.py` were not applied; no `data/intelligence/first-party/`; ingestion used DS-032-hardcoded `ingest_decode_retention_exports.py` reading ~/Downloads (not reproducible from the repo) |

Classification: RAW_PRIVATE_STUDIO_DATA = Studio ZIPs and provenance JSON (IGNORED, local-only). DERIVED_PRIVATE = `audience-retention-analysis.json` (ignored) and the five tracked files (evidence register, checkpoint, workbook, DOCX, HANDOFF) which embed per-video private metrics and ARE on the remote. PUBLIC_SAFE = Apify dataset, transcripts, manifest, local asset inventory JSON (paths scrubbed). On a fresh clone, 56 thumbnail + 56 retention + 56 Studio file pointers in the register would be missing.

Contradictions inside the DYH deliverables (not silently reconciled): HANDOFF is stale (HEAD 9212e00, 'do not push', 34 retention-analyzed, 24 sampled vs 46/44+12 now); checkpoint `remote_push_performed=false` is wrong (pushed 2026-09-29); DOCX intro/scope text still says Studio data absent / no retention curves while section 19 supersedes it; workbook README/Dashboard stale; DOCX cross-references off by one; status wording differs (PARTIALLY_COMPLETE vs 'COMPLETE WITH DATA LIMITATIONS'). AGENTS.md says no real first-party export has been ingested; Studio data is in fact present locally.

Strict reading: browser observations and seek-sampled frames are not exported Analytics; transcript analysis is not playback; per-video CTR/impressions exist only in the private export and are not used to claim causal thumbnail effects here.

## 14. Global Knowledge Corpus

| Dataset | Sources | Extracted | Validation state | Notes |
|---|---|---|---|---|
| DS-000011 | 17 files / 7.0 MB, 16 unique texts (Hook (1).pdf and Hook guide.pdf identical text) | 17 rules: 11 AI-synthesis, 3 human-authored, 3 creator-attributed | rules are training heuristics | Full text 17/17; all hashes match; `RECONCILIATION-MANIFEST.json` says 17 unique (wrong, true = 16) |
| DS-000018 | 1 ZIP (566,739 B), 63 tabs + manifest, 245,914 words; 61 unique tabs per audit (REPORTED) | 33 original claims (18 claims/5 interpretations/10 recommendations) | 33 `HUMAN_AUDITED_ORIGINAL_33` against official sources: 10 SUPPORTED, 12 PARTIAL, 1 CONTRADICTED, 8 NOT_SUPPORTED, 2 NOT_VERIFIABLE (reviewer identity INFERRED from an AI-driven audit session); **666 additional claims `AI_GROUNDED_EXTRACTION_UNVALIDATED`** (274 numeric, 5 duplicate texts, no IDs), exports only, mislabelled `prior_status=NOT_CURRENTLY_VERIFIABLE` | Only 10 of 33 supported: creator claims are NOT official YouTube facts |
| DS-000031 | 1 file, 70,730 B, 1,426 lines, 15 segments | 63 concepts, 15 formulas, 12 numeric heuristics, 1 scorecard, 9 examples, 15 relationships | 52/63 `SOURCE_HEURISTIC_NOT_PLATFORM_RULE`; 16 primary-source checks: 1 confirmed, 2 consistent, 2 partial, 2 insufficient, 2 contradicted, 7 heuristic-not-rule | All 63 line anchors resolve |

Training registries: `youtube-strategy-training-knowledge-2026-09-11.json` 50 rules; `…-2026-09-24.json` 66 rules (adds 16 from DS-031); consumers still point at the 09-11 file. All sources tracked, none LFS, all on the remote. The export folder duplicates raw evidence (DS-031 and 63 DS-018 tabs byte-identical to raw).

## 15. Intelligence Outputs

| Output | Count / scope | Status | Authoritative version |
|---|---|---|---|
| Topic Opportunity | 5 channels VALIDATED; 40 DATA_READY (no artifact); 30 NOT_AVAILABLE | PARTIAL (artifacts for 5/75) | data/intelligence/channels/CH-*/topic-opportunity-intelligence-2026-09-09.json |
| Packaging (title/visual) | 3 VALIDATED, 2 PARTIAL (title-only), 40 DATA_READY | PARTIAL | packaging-intelligence-2026-09-10 per channel; cross-channel packaging-comparison-2026-09-10 = historical, excluded by freshness registry |
| Hook / Script | 5 VALIDATED; 40 DATA_READY | PARTIAL | hook-script-intelligence-2026-09-11 |
| Editing / Visual | 1 PARTIAL (CH-000004 xkcd); 74 NOT_AVAILABLE | PARTIAL by design | DS-016 forensic evidence only |
| Channel strategy | 4 PARTIAL; 71 NOT_AVAILABLE; 2 blueprints (finance, senior-health) + 2 benchmarks | PARTIAL (GENERALIZED_WORKING engine, 2 niches) | blueprints/*-2026-09-11.json |
| Unified content plans | 5 (CH-000001..5), `content-intelligence-v1` | VALIDATED for 5 channels only | plans/CH-*-content-intelligence-v1 |
| First-party diagnosis | 0 produced via pipeline; DYH diagnosis is a separate research deliverable | NOT_AVAILABLE (pipeline) / PARTIAL (DYH) | docs/research/decode-your-heart-2026-09-27 |
| Freshness registry | 35 artifacts, all CURRENT, 0 sha mismatches, 0 dependency drift | VALIDATED but frozen at 2026-09-11 / commit 4559e39 (25 datasets, 10 channels) | intelligence-freshness-registry.json |
| Senior Health research | V1 (2026-09-25 root files), V2 (forensic-v2), V3 (forensic-v3) + 2026-09-28 inventory (PR #6) | V3 current; V1/V2 SUPERSEDED but historical; HEAD copy of master inventory STALE | forensic-v3/ + PR #6 inventory |
| Thumbnail research | 6 audits / 144-row ledger (remote-only) | PARTIAL, not in HEAD | origin/research/senior-health-complete-local-sync |
| Small-channel breakout | SMALL-CHANNEL-BREAKOUTS.json (v2) + SMALL-CHANNEL-BREAKOUT-FORENSICS.md (v3) + BHWA Case 13 deep dive (25 breakout candidates at >=5x median, descriptive) | PARTIAL, DATA_READY | v3 md + BHWA dossier |
| Google Trends | TRENDS-REGISTER.json (v2), trends-raw/, TRENDS-RECAPTURE-SUMMARY.md (v3) | PARTIAL; DYH report says Trends blocked in its stale text | v3 recapture |
| External research | forensic-v2/external, EXTERNAL-BREAKOUT-RESEARCH-RAW.md | DATA_READY, unvalidated | v3 |
| Medical review | MEDICAL-VALIDATION.json (v2); registry: medical validation VALIDATION_REQUIRED, no authoritative source wired; DYH 15 claims/12 videos reviewed | PARTIAL | NONE authoritative |

**Overstatement flag:** AGENTS.md rule 12 says V1 is 'generalized across all canonical channels'. Verified: the engines are generic (no niche branching) but outputs were generated for 5 channels; the other 40 data channels have inputs only. That wording describes capability, not coverage.

## 16. Research Artifacts

| Artifact | Class | Notes |
|---|---|---|
| docs/audits/PROJECT-CURRENT-DATA-REALITY-AUDIT-2026-09-24.md | SUPERSEDED BUT HISTORICAL | Baseline 73 ch / 2,149 videos; arithmetic consistent with today's 75 / 2,303 (+Rehan 56, +BHWA 98) |
| This file | CURRENT AUTHORITATIVE | Replaces all prior project-wide audits |
| docs/audits/SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md | INCOMPLETE / MIXED | Newest section first, older 2026-09-22 sections appended below; says 393 passed, now 405+1 failed |
| docs/research/senior-health-2026-09-25/forensic-v3/* | CURRENT (HEAD copy of inventory STALE) | V3 report + workbook; 69-row inventory superseded by 143-row (PR #6) |
| …/forensic-v2/*, root V1 files | SUPERSEDED BUT HISTORICAL | SENIOR-HEALTH-COMPETITIVE-INTELLIGENCE*.md exist in 2 near-duplicate versions |
| docs/research/decode-your-heart-2026-09-27/* | CURRENT, stale internal text | See section 13; contains private metrics |
| exports/2026-09-27-master-knowledge-and-senior-health-export | DUPLICATE (derived) | Duplicates data/raw knowledge sources and transcripts; 276/459 transcripts hash-drifted |
| REPOSITORY-SUPERSET-CONSOLIDATION-REPORT-2026-09-23, SENIOR-HEALTH-*-2026-09-22 (root) | SUPERSEDED BUT HISTORICAL | Root-level reports |
| docs/YOUTUBE_INTELLIGENCE_OS_*AUDIT*-2026-08-31/09-01/09-11 | SUPERSEDED BUT HISTORICAL | Pre-registry |
| docs/audits/HISTORICAL-INVENTORY-REBUILD-GAP-2026-09-24.md | CURRENT | Still true (verified 10 channels / 667 videos in inventory DB) |
| thumbnail-forensics-2026-10-02 (remote-only) | INCOMPLETE | See section 12 |
| output/, outputs/ | TEMPORARY / LEGACY | local-only |

Contradictions found (not silently reconciled): (1) AGENTS.md first-party 'no real export ingested' vs local Studio data; (2) AGENTS.md 'generalized across all channels' vs artifacts for 5; (3) DS-032 manifest 'competitor evidence' vs OWN; (4) 2,299 vs 2,303 videos; (5) 143 'channels' vs 138 IDs; (6) 63 channels vs 72 DS-034 files; (7) DS-011 17 vs 16 unique sources; (8) HEAD master inventory (69) vs PR #6 (143); (9) thumbnail ledger labelled Senior Health but 83/144 are xkcd; (10) checkpoint 393 passed vs 405 passed + 1 failed; (11) DYH checkpoint `remote_push_performed=false` vs pushed; (12) manifests for DS-032/033/034 cite `/private/tmp/...` scratch source paths and another home directory (`/Users/ghilmanislam360`): provenance exists but is not portable; (13) origin/main's registry DB (`63c1f894`) is older than HEAD's (`48ffb558`), i.e. main lacks the BHWA 4-Short backfill.

## 17. Database State

| DB | Git | Size | SHA-256 (prefix) | integrity / FK | Tables & key rows | Authority | Rebuildable from clean clone |
|---|---|---:|---|---|---|---|---|
| `data/catalog/youtube_channel_registry.db` | LFS (real file locally; remote object AVAILABLE) | 141,373,440 B | 48ffb558adf40ac7 | ok / 0 | 75 channels, 2,303 videos, 2,303 transcripts, 2,455 subtitle_tracks, 32 datasets, 825 data-layer rows, 600 intelligence_coverage, 216 availability_gaps, 4 non-channel subjects | Derived index; canonical operational registry | **YES**: rebuild in disposable clone gave identical content in 13 tables; validator PASS; byte hash differs only by timestamp |
| `data/catalog/youtube_inventory.db` | tracked normal file | 52,338,688 B | 9cf5e78b4d15b07c | ok / 0 | 25 datasets, 10 channels, 667 videos, 668 transcripts, 604 classifications, 5,172 visual assets, 45,774 discovered files | Authoritative ONLY for the 6 historical channels; otherwise a historical index | **NO / PARTIAL**: `rebuild_inventory_catalog` regenerates only manifest bookkeeping (32 datasets, integrity ok, `SEMANTIC_MANIFEST_INDEX_NOT_BYTE_IDENTICAL`); channels/videos/transcripts cannot be rebuilt |

The registry records `historical_catalog_sha256` = current inventory hash (consistent). No other SQLite files exist. Neither DB has Studio rows. DS-034 would add a 33rd dataset with 0 dataset_channels links on the PR #6 registry (`39e7a28b`).

## 18. Scripts and Pipelines

76 tracked code files audited (28,994 LOC; `scripts/` = 60 files, 24,148 LOC). The 46 'untracked' files in `scripts/` are all `__pycache__` bytecode; there are no real untracked scripts.

| Function | Scripts | Notes |
|---|---|---|
| Ingestion | apify_youtube_ingest (only paid-network pipeline, APIFY_TOKEN from env), ingest_youtube_analytics (file import, hash-guarded), ingest_decode_retention_exports (DS-032 hardcoded) | only first generic |
| Registration / catalog | register_batch, register_structured_source, register_supplied_channel, inventory_catalog, rebuild_inventory_catalog, load_*_results | generic; rebuild is partial |
| Registry / tracker | build_youtube_channel_registry, build_youtube_channel_master_tracker (.py and .mjs twins), normalize_tracker_hyperlinks | generic |
| Package build | package_youtube_channel_dataset.mjs (generic), package_five_channel (older), build_dr_rehan/doctor_thomas/better_health_while_aging_package.py (copy-paste per channel) | 3 duplicates, 0 refs |
| Collection | acquire_registered_thumbnails, recover_ds32_thumbnails.sh, forensic-v3 yt_tabs.py / yt_video_meta.py (DS-034 collector, branch-only) | network |
| Thumbnail/visual | image_pipeline.py, image_text_recognition.swift, build_ds32_thumbnail_evidence.py | DS-032 one-off |
| Intelligence | run/refresh/plan_youtube_intelligence, report_topic/packaging/hook_script/editing_visual/channel_strategy/first_party/common/coverage | generic, no niche branching |
| Validation | validate_dataset_ledgers, validate_youtube_channel_registry, validate_legacy_dataset_manifests, validate_supplied_channel_packages, scan_tracked_secrets | read-only |
| Dataset-specific one-offs | build_decode_your_heart_recovery (1,489 LOC), decode_your_heart_final_diagnosis, update_decode_report/workbook, analyze_better_health_while_aging, build_bhwa_deep_investigations | hardcoded DS-032/033 |
| Legacy | production_pipeline*.py, exports/*/scripts, forensic-v2/v3 scripts, ~45 forensic work scripts under data/raw/forensic-analysis | outside pipeline |

Absolute `/Users` paths in code: 6 files (`scripts/source_adapters/batch_rules.py` 12 historical provenance paths; 4 tests; 1 forensic script). Zero-reference scripts: build_dr_rehan_package, build_ds32_thumbnail_evidence, build_better_health_while_aging_package, ingest_decode_retention_exports, inspect_decode_workbook.mjs, recover_ds32_thumbnails.sh. ENVIRONMENT BLOCKERS: `python-docx` not installed and not declared (blocks update_decode_report.py, extract_master_data.py); npm `docx` undeclared; two workbook scripts need a Codex artifact-tool runtime; system python3 is 3.9.6 (project requires >=3.12; repo `.venv` is 3.12.14).

Overwrite-risk (static, none executed): build_ds32_thumbnail_evidence.py (unconditional write into the raw DS-032 tree) and ingest_decode_retention_exports.py (copy over private first-party data with no exists/hash check) are HIGH; build_youtube_channel_registry.py and rebuild_inventory_catalog.py replace tracked DBs by design (staged + `os.replace`); update_decode_report.py saves the tracked DOCX in place; tests invoking analyze_better_health_while_aging rewrite a tracked JSON, so **the test suite is not read-only**. Guarded/idempotent: acquire_registered_thumbnails, ingest_youtube_analytics, register_*.

## 19. Test / CI State

| Item | Result |
|---|---|
| CI workflow | `.github/workflows/validate.yml`: py3.12, node (.nvmrc 24.14.0), LFS, compileall, ruff (rule set E9/F63/F7/F82: weak), secret scan, inventory integrity, partial rebuild to temp DB, registry rebuild `--write-ledgers`, ledger + registry validators, `pytest -q`, junk/DB reject. Triggers: pull_request and push to main |
| Remote CI | 10 most recent runs success; latest main run 36191743459 (2026-09-25); latest PR #6 run 36430758310 (2026-09-28). **No run for HEAD 373bf37** (no PR) |
| Local tests (clean clone @373bf37, py3.12.14) | 407 collected: 405 passed, 1 FAILED, 1 skipped, 0 errors, 5 warnings, 74.7 s |
| FAILED | `tests/test_bhwa_forensic_research.py::test_bhwa_structural_analysis_covers_all_98_and_separates_deep_review`: PROJECT DEFECT (test changed in 373bf37 expects 25 VERIFIED_DEEP_INVESTIGATION; script emits 9 PREVIOUSLY_REPORTED + 89 NOT_YET). Expected totals NOT altered |
| SKIPPED | `test_production_pipeline.py`: media fixture absent (ignored `output/chair-stand-safety`): MISSING-DATA-IN-CLEAN-CLONE; also skips in CI |
| compile / ruff | pass / pass |
| Validators (clean clone) | validate_dataset_ledgers PASS (DS-021..030); validate_youtube_channel_registry PASS (2,303/2,303); validate_legacy_dataset_manifests PASS; scan_tracked_secrets 0 findings (covers tracked text only, 5 patterns) |
| CI-parity steps run by this audit in the disposable clone | `rebuild_inventory_catalog --database <tmp>`: ok, 32 datasets, 0 FK violations; `build_youtube_channel_registry --write-ledgers`: identical content; DB integrity ok / 0 FK for both DBs. (A subagent's attempt to run these as one bundled command was blocked by the permission classifier; this audit re-ran them individually, inside the clone only.) |
| Full-local-repo test run | NOT RUN (tests write into the repo): UNKNOWN |
| validate_supplied_channel_packages on real data | NOT RUN (config schema mismatch): UNKNOWN |
| Branch protection / required checks | UNKNOWN (403) |

## 20. Clean-Clone Reproducibility

| Capability | CLEAN CLONE | FULL LOCAL REPO | PRIVATE LOCAL DATA | STATUS |
|---|---|---|---|---|
| Run tests | Yes (405/407; 1 project defect, 1 data skip) | same (not run: tests write) | not needed | PARTIAL |
| Rebuild registry | Yes, content-identical | Yes | not needed | READY |
| Rebuild inventory DB | Bookkeeping only; channels/videos not rebuildable | Committed snapshot is authoritative | not needed | PARTIAL (documented gap) |
| Recreate standard packages | Committed packages present; regeneration needs raw Apify payloads (tracked) + node scripts | Yes | not needed | READY (not re-run) |
| Reproduce Senior Health inventory | 69-row Sep-26 version only; 143-row needs PR #6 | needs yios-expansion | live catalog is tracked on PR #6 | PARTIAL / BRANCH-SPLIT |
| Reproduce thumbnail universe | Tracked 1,452 images only; 56 DS-032 thumbs + 14 sheets absent; forensic ledger not in HEAD | 1,528 images | DS-032 ignored images | PARTIAL |
| Regenerate current reports | Generic V1 reporters yes for 5 legacy channels; DYH report not (python-docx missing, private inputs) | partial | Studio ZIPs in ~/Downloads | PARTIAL |
| Reproduce DYH Studio ingestion | No | Only with ~/Downloads | Required | NOT REPRODUCIBLE |

Caveat: the audit clone was a local clone, so LFS was served from the local store; an LFS-less checkout is not proven. Remote object availability was verified separately via the LFS batch API. The repo itself is a partial clone (`blob:none`): history operations fetch blobs lazily from GitHub.

## 21. Git LFS / Large Files

`.gitattributes` tracks only `data/catalog/youtube_channel_registry.db` through LFS (`git lfs ls-files`: 1 object, `*` = real content present; oid 48ffb558…; matches file SHA-256). `.git/lfs/objects` holds 19 objects / 2.4 GB (old registry versions), so 17 stale local LFS copies. `youtube_inventory.db` (52 MB) is a normal git object. Largest tracked non-DB files are forensic WAVs (27/23/16/8 MB), a 18 MB master CSV and 13.9 MB supplemental ZIP; no tracked file exceeds 100 MiB except via LFS. 65 XLSX and 51 ZIP are normal tracked objects (not LFS), including the DS-032 package workbook. Private Studio exports: not tracked, not LFS.

## 22. Storage / Duplication

Working tree 1.31 GB; `.git` 3.7 GB (1.0 GB objects incl. 84 MB garbage, 2.4 GB LFS). Exact duplicates (>=20 KB): 29 redundant files, 51.5 MB (DERIVED_COPY: `*_master.json` vs `*_clean.json` in 6 combined/ folders, 25 MB; EXACT_REDUNDANT_COPY: `outputs/apify-*` vs `data/extracted/.../combined` 11.3 MB; EXPECTED_LINEAGE_DUPLICATION: `dataset.json` vs `apify/*/raw/dataset.json` for DS-029/030/033, 10 MB; Nick Invests transcript ZIP in `raw` and `extracted`, 3.4 MB). Exports duplicate raw knowledge content (61 thumbnails inside SUPPLEMENTAL-DATA-ARCHIVE.zip duplicate on-disk files; 276/459 transcripts drifted). Largest consumers: screenshots in `data/raw/competitors` (~570 MB PNG), forensic frames (228 MB), registry+inventory DBs (194 MB). Same thumbnails at multiple resolutions: not computed (no exact-hash duplicates exist; xkcd comics defeat dHash). Nothing deleted.

## 23. Security / Privacy

| Check | Result | Class |
|---|---|---|
| Tracked secrets/tokens (apify_api_, sk-, ghp_, gho_, github_pat_, AIza, AKIA, xox*, Bearer, api_key=, password=, private key) | 0 hits at HEAD; official scanner 0 findings; APIFY_TOKEN referenced by name only | SAFE_TO_PUSH |
| .env / credentials tracked | none | SAFE_TO_PUSH |
| Git history | 7 of ~155 revisions sampled: 0 hits; remainder UNKNOWN | UNKNOWN |
| Scanner coverage | text only; 5 patterns; blind to xlsx/zip/docx/pdf/db | UNKNOWN for 65 xlsx, 51 zip, 4 docx, 10 pdf, 2 db |
| Absolute home paths in tracked text | 91 files (`/Users/ghilmanislam360` 62 files/972 occurrences; `/Users/ghilmankhan` 31 files/212) | NEEDS_SANITIZATION before any public sharing |
| Third-party emails scraped from competitor descriptions | 26 tracked files | NEEDS_SANITIZATION before public sharing |
| Private Studio ZIPs / retention / public-browser DS-032 / run_metadata / output* | ignored, untracked | PRIVATE_LOCAL_ONLY (correct) |
| Per-video private metrics inside 5 tracked DYH deliverables | on private remote; HANDOFF says 'do not push' | NEEDS_SANITIZATION if repo ever leaves private; push already occurred |
| Repo visibility | PRIVATE | — |

## 24. Capability Matrix

| Capability | Status | Available data | Missing data | Main limitation | Next unlock |
|---|---|---|---|---|---|
| Channel identity research | READY | 75 verified identities, 4 subjects, 143 Senior Health identities (PR #6) | — | niche not a registry field | merge PR #6; add niche column |
| Competitor discovery | READY | 143-row Senior Health inventory (branch), live catalog 2026-09-28 | 7 hand-off channels not yet in registry | inventory lives on a branch | merge PR #6 |
| Topic research | PARTIAL | titles/descriptions/transcripts for 46 channels; artifacts for 5 | artifacts for 40 channels | not run beyond 5 legacy | run generic reporter per channel |
| Title analysis | READY | 2,303 titles | — | generic engine only run for 5 | run for Senior Health |
| Thumbnail analysis | PARTIAL | 200 local current-public thumbnails; 6 audits (remote-only) | download for 2,103 videos; audits B002+ | only 3% audited; ledger not in HEAD | merge forensic branch; download Senior Health thumbs |
| Thumbnail-performance correlation | BLOCKED | public views; Rehan private CTR local | historical snapshots, same-period thumbnails, CTR for competitors | current-public thumbnails != exposed creative | start own thumbnail A/B log |
| Script research | READY | 2,291 transcripts | — | generic engine for 5 channels | run for acquired 7 |
| Hook research | READY | same | — | same | same |
| Editing research | PARTIAL | 1 channel forensic (xkcd); Rehan seek-sampled frames | frame evidence for competitors | evidence-bound | acquire frames/clips (browser) |
| Public performance benchmarking | PARTIAL | views/likes/comments 2,293+ | view history over time | single-time snapshots | DS-034-style recollection |
| Senior Health competitor research | PARTIAL | 7 acquired + 63 metadata-only (branch) | 14 pending per-video acquisition; thumbnails; transcripts for 63 | branch split | merge; approve $8.136 pending acquisition |
| Small-channel breakout analysis | PARTIAL | 25 BHWA candidates; v3 forensics | comparable small-channel populations | descriptive 5x median only | acquire pending channels |
| First-party Dr. Rehan diagnosis | PARTIAL | Studio exports, retention for 46/56, channel-level traffic/audience | per-video traffic/search; verified playback | not reproducible from repo; stale DYH text | correct docs; ingest through first-party pipeline |
| Google Trends analysis | PARTIAL | trends registers v2/v3 | fresh recapture | dated | re-run |
| Medical safety review | PARTIAL | 15 DYH claims reviewed; competitor claims | no authoritative source wired; 44 DYH videos unreviewed | VALIDATION_REQUIRED | wire primary-source list |
| Content blueprint generation | PARTIAL | blueprints for 2 niches; 5 unified plans | blueprints for others | engine generic, outputs few | run orchestrator for Senior Health |
| A/B-test planning | PARTIAL | DYH matched comparisons (22), diagnosis | clean experiments | no real first-party experiment data | define Dr. Rehan experiments |
| Cross-channel pattern mining | PARTIAL | calibration across 2 niches; no ROBUST_CROSS_NICHE_PATTERN | more channels per niche | 2 channels per niche | more channels |
| Training / RAG knowledge corpus | READY | 66 rules, 3 knowledge datasets, full text | 666 AI claims unvalidated | creator claims not facts | validate or quarantine AI claims |
| Automated report generation | PARTIAL | V1 reporters, orchestrator | python-docx, tests non-read-only | 1 failing test, env gaps | declare deps; fix test |

## 25. Missing Data

29 identity-only channels with no videos; 14 qualified-pending Senior Health channels (2,034 videos) lacking transcripts/thumbnails/acquisition; 63 metadata-only channels lacking transcripts; 235 unresolved DS-034 refusals; 2,103 videos without a local thumbnail (1,944 with a URL); 159 videos with no thumbnail URL at all; 159 videos with unknown type; 20 videos not yet acquired for 3 acquired channels; 12 transcript placeholders; 17 real transcripts of unknown caption type; Rehan per-video traffic/search drill-downs, 10 empty retention exports, verified full playback, spoken-audio review, 44 unreviewed medical-claim videos; historical thumbnail snapshots (none exist); competitor CTR/impressions (never available); authoritative medical sources.

## 26. Broken / Stale Components

- BROKEN: `test_bhwa_structural_analysis_covers_all_98_and_separates_deep_review` (test/script drift, HEAD).
- BROKEN: `validate_supplied_channel_packages` has no runnable config for committed datasets (usage mismatch).
- STALE: HEAD `SENIOR-HEALTH-MASTER-INVENTORY.*` (69 rows) and `AGENTS.md`/status wording; DYH HANDOFF, checkpoint, DOCX/workbook intro text; freshness registry canonical_state (25 datasets/10 channels, 2026-09-11); inventory DB (does not know DS-020..027); origin/main registry DB (lacks BHWA backfill); local `main` branch (62 behind).
- STALE: intelligence artifacts dated 2026-09-09..11 for 5 channels; consumers of the 50-rule training registry instead of 66.
- HYGIENE: 84 MB `.git` garbage, 17 stale LFS objects (2.4 GB), prunable worktree, 46 `.pyc` files, 3 duplicate per-channel package builders, `output/` Shorts project inside the research repo.
- ENVIRONMENT: python-docx and npm docx undeclared/missing; system python 3.9.

## 27. Local-Only Evidence

- `data/raw/first-party/youtube-studio/DS-000032/` (70 files; also in ~/Downloads, no independent backup)
- `data/raw/competitors/DS-000032/public-browser-2026-09-27/` (75 files: 56 thumbnails, 14 contact sheets, trends CSVs)
- `data/raw/competitors/DS-000030/apify/ai1C2ifFj7SPFkINt/evidence/run_metadata.json`
- `output/`, `outputs/`, `output.zip` (production project and early Apify outputs; outputs/ largely duplicated in data/extracted)
- yios-expansion uncommitted `build_master_inventory.py` change
- ~/Downloads: DYH production workbooks, mp4, original Studio ZIPs, Dr. Rehan older workbook/DOCX copies, methodology PDFs
- One stash entry (non-evidence)

## 28. Remote-Preserved Evidence

On `origin/research/senior-health-acquisition-phase-2` (= HEAD): all tracked content including DYH deliverables (with private metrics), BHWA backfill, knowledge exports. On PR #6 head: DS-000034 (73 files verified), 143-row inventory, live catalog, paid-acquisition plan. On `origin/main` (812f249): everything through PR #5 (registry DB older). On remote-only branch `origin/research/senior-health-complete-local-sync` (0cbabf5): thumbnail forensics checkpoint. LFS: registry versions for main, HEAD and PR #6 confirmed present on GitHub. NOT on any remote: section 27 items, DS-035.

## 29. Paid-Acquisition Dependencies

Nothing in this audit started paid acquisition. Apify (`streamers/youtube-scraper`, ~$4.00/1,000 results, REPORTED) is the only paid path (`apify_youtube_ingest.py`, `APIFY_TOKEN` env). Planned but unexecuted: 14 qualified-pending channels = $8.136 (2,034 results); 71 identity-only channels = $26.020 (6,505 results; recomputed from the 2026-09-28 inventory report); 35 adjacent channels = $29.436 (7,359 results); the 3 acquired channels' 20 missing videos = $0.080; full non-acquired total $63.672 for 15,918 results (all at the REPORTED $0.004/result, unverified; an earlier $54.648/14,210 figure in session memory is superseded). Prior account state reported $4.28/$5.00 used (2026-09-22, REPORTED, unverified now). No paid dependency for: thumbnail downloads (public i.ytimg.com), metadata via public player endpoint (DS-034 method, bot-checks throttle it), Studio exports (user account), Trends (browser).

## 30. Top Priority Gaps

Priority is qualitative (impact x affected records x strategic value / effort); no numeric precision claimed.

| Gap | Priority | Area | Current | Required | Affected | Evidence | Impact | Effort | Money? | Browser/private account? | Engineering? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G01 | CRITICAL | Repository integrity | Work split across 3 branches + 1 worktree; thumbnail checkpoint on remote-only branch; yios-expansion has uncommitted change | One reviewed, tested integration path to main | PR #6, phase-2, complete-local-sync, yios worktree | Git refs/diff | Any further work builds on divergent bases | Low-Med | No | No | Yes (merge/conflict handling) |
| G02 | CRITICAL | Tests/CI | 1 failing test; no CI for HEAD; tests write into repo | green, read-only suite | HEAD | pytest run | Merging red/unknown | Low | No | No | Yes |
| G03 | CRITICAL | Privacy | Per-video private Studio metrics in 5 tracked files, pushed | derived-private files kept out of git or sanitized; HANDOFF corrected | DYH deliverables | tracked file list | Leak if repo shared; wrong 'not pushed' claim | Low | No | No | No (policy + edit) |
| G04 | CRITICAL | Thumbnail forensics | 6/200 current thumbnails audited; ledger not in HEAD; templated DS-032 inspections | complete audited set with alignment labels | 200 thumbnails (61 Senior Health) | remote ledger | Visual conclusions unsupported | High | No | Browser for gaps | Some |
| G05 | HIGH | Senior Health coverage | 14 pending channels (2,034 videos) unacquired; 63 metadata-only; 235 refusals | acquired per-video + transcripts for priority channels | 14 channels | DS-034/inventory | Competitor benchmark thin | Med | $8.136 for pending 14 | No | Low |
| G06 | HIGH | Thumbnail acquisition | 1,944 videos have URL but no local file; 159 no URL | local public thumbnails for Senior Health set at least | SHH 122, BHWA 98, Okoro 66, Ares 35, plus pending | registry/inventory | Cannot run packaging visual intel | Low (urllib, public) | No | No | Existing script |
| G07 | HIGH | Intelligence coverage | Artifacts for 5/45 data-ready channels | Run generic V1 engines for 7 acquired Senior Health channels + own | 40 channels | registry coverage | V1 claim overstated | Low-Med | No | No | Run only |
| G08 | HIGH | First-party | Studio exports bypass pipeline; not reproducible; per-video traffic/search missing | pipeline-ingested, repo-reproducible private store | Dr. Rehan 56 videos | DYH audit | Diagnosis cannot be re-derived | Med | No | Studio account | Yes |
| G09 | HIGH | Temporal alignment | No historical thumbnail snapshots; current thumbs vs lifetime views | Start dated thumbnail snapshots; Rehan A/B log | all | manifests | Spurious causal reads | Low | No | No | No |
| G10 | HIGH | Video type | 159 UNKNOWN type (Mr. Finance, Matty) | Documented rule or re-acquisition | 159 | registry | Format analysis skewed | Low | No | No | Maybe |
| G11 | MEDIUM | Inventory DB | Not rebuildable; stale vs registry | Documented authority; optional rebuild of full history | 6 channels | gap doc | Single point of truth | High | No | No | Yes |
| G12 | MEDIUM | Docs consistency | AGENTS.md rule 12, checkpoint, HANDOFF, DOCX, manifests contradict reality (section 16) | one baseline (this file) + corrections | — | section 16 | Agent confusion | Low | No | No | No |
| G13 | MEDIUM | Medical validation | No authoritative source; 44 DYH videos unreviewed | source list + review | Rehan + health channels | registry | Safety risk for health content | Med | No | No | Some |
| G14 | MEDIUM | AI claims | 666 AI-extracted DS-018 claims unvalidated, mislabelled, not in data/intelligence | quarantine or validate | 666 claims | knowledge audit | Contaminates RAG | Med | No | No | Some |
| G15 | MEDIUM | Dependencies | python-docx/npm docx undeclared; py3.9 system | declared deps | scripts | code audit | Reports unrunnable | Low | No | No | Yes |
| G16 | LOW | Storage hygiene | 84 MB garbage, 17 stale LFS objects, duplicate JSONs, outputs/, prunable worktree | cleaned (with approval) | ~2.5 GB | du | Disk/clone weight | Low | No | No | No |
| G17 | LOW | Provenance portability | manifests cite /private/tmp and other-home paths | normalize provenance | 91 files | grep | Audit friction | Med | No | No | Yes |
| G18 | LOW | DS-035 | Reported collection absent | Decide: re-run (zero-spend) or drop | — | none found | Lost effort | Med | No | No | No |

## 31. Recommended Next Sequence (not performed)

**NOW**
- Do not start new research until G01-G03 settle. Decide integration order: merge PR #6 and the phase-2 branch (disjoint files), bring in the remote-only thumbnail checkpoint, rebuild registry afterwards.
- Fix or revert the one failing BHWA test; open a PR for the current branch so CI runs.
- Resolve the DYH privacy question (keep private metrics out of tracked files or accept private-repo-only) and correct the stale HANDOFF/checkpoint push claim.
- Back up the Studio exports outside ~/Downloads (local-only evidence).

**NEXT**
- Download public thumbnails for the Senior Health acquired set (zero cost), then continue thumbnail forensic batches with temporal-alignment labels; replace templated DS-032 inspections.
- Run the generic V1 engines for the 7 acquired Senior Health channels and the own channel.
- Ingest Dr. Rehan Studio data through the first-party pipeline so it is reproducible; set up dated thumbnail experiments.
- Decide on the $8.136 pending-14 acquisition (explicit approval required).

**LATER**
- Acquire remaining identity-only/adjacent channels by priority; add niche as a registry field; compare more than 2 channels per niche for cross-niche patterns.
- Validate or quarantine the 666 AI claims; wire an authoritative medical source list.

**OPTIONAL**
- Storage cleanup (garbage packs, stale LFS objects, duplicate JSON), provenance path normalization, deduplicate per-channel package builders, stronger ruff rule set, pin dependencies (python-docx).

No new infrastructure is recommended; every item uses existing scripts, branches and files.

## 32. Final Mental Model

The canonical truth is the tracked raw evidence and manifests; the registry DB is a reproducible index over them (75 channels, 46 with data, 2,303 videos, 2,291 real transcripts). Knowledge corpora (DS-011/018/031) are heuristics, not platform facts. Intelligence engines are generic but have only been exercised on 5 legacy channels. Senior Health is a branch-split program: 7 acquired competitors in this checkout, 63 metadata-only channels and a 143-row inventory on PR #6, 14 qualified pending behind a $8.136 gate, 71 identity-only leads. Dr. Rehan is the own channel with private Studio data held outside the pipeline. Thumbnails: 200 current-public images exist, none historically verified, 6 audited; the claimed 2,000+ thumbnails and 78 audits do not exist here. Before any further research, unify the branches, fix the red test, settle the privacy question, and treat this file as the only baseline.
