# YIOS Selected Folders vs Canonical Repository — Read-Only Reconciliation (2026-11-11)

Audit only. Nothing was moved, deleted, renamed, committed, fetched, checked out or merged. No database was modified (SQLite opened `mode=ro&immutable=1`). Per-file manifest: [YIOS_SELECTED_FOLDERS_MANIFEST_2026-11-11.csv](YIOS_SELECTED_FOLDERS_MANIFEST_2026-11-11.csv) (34,351 rows: folder, relpath, size, SHA-256, class, match location, publication evidence).

## A. Executive summary

- 10 folders, **34,351 files, 32.28 GB** (matches Finder's 32.29 GB). Files inside nested `.git` directories (about 3,000, in `yios-senior-health` and two scratch clones) were not counted as files; no symlinks exist in any folder.
- `yios-senior-health` is a registered git worktree (branch `research/senior-health-metadata`, HEAD fd029485), not an independent copy.
- Remote heads: 55 live (`git ls-remote`) = 55 local remote-tracking refs, all equal. Evidence for "published" is therefore the local object store reachable from `--remotes`, which equals the live remote tip set.
- Canonical branch `research/finance-economics-intelligence` is **ahead of origin by 4 commits** (unpushed). One stash exists (`stash@{0}`, see E).

Verified classification (by bytes, SHA-256 and git blob SHA-1):

| Class | Files | GB |
|---|---|---|
| Exact bytes in canonical working tree AND blob on remote refs | 23,305 | 5.72 |
| Exact bytes in canonical tree, LFS pointer on remote refs (registry DB copies) | 7 | 0.99 |
| Exact bytes in canonical tree, NOT on remote (mostly my 2026-11-11 Senior Health copy, ignored raw) | 82 | 0.05 |
| In git history, blob on remote refs, absent from current tree | 4,049 | 0.29 |
| Byte-identical to an LFS object whose pointer is on remote refs (MP4s and large payloads) | 83 | 3.49 |
| In local git only: reachable from `stash@{0}` (untracked-files commit), not on remote | 1,730 | 0.76 |
| LOCAL_ONLY, unique | 3,501 | 4.93 |
| LOCAL_ONLY, but several byte-identical copies exist among the 10 folders | 1,594 | 16.06 |

Counting duplicate content once, the content with no copy in the project or any git ref (local-only, plus the stash-only files) is **5,931 unique contents, 13.35 GB**. All of it sits on this one Mac. The off-device backup was reported as owner-BLOCKED by the 2026-11-05 packages and I found no contrary evidence.

Not verified: whether GitHub's LFS server actually holds the LFS payloads (pointers are on remote refs, but I did not query the LFS server). Usage meters (five-hour/weekly) could not be read in this session, so they are UNVERIFIED; no paid usage was enabled.

## B. Folder by folder

| Folder | Files / size | What it is | Status vs YIOS |
|---|---|---|---|
| yios-senior-health | 3,340 / 1.28 GB | Worktree of the repo (Senior Health metadata branch). Contains `research/senior-health-metadata/` (untracked, incl. 16 channel `raw/full/*.json`) and the Dr Rehan/Decode Your Heart docs (`docs/research/decode-your-heart-2026-09-27`, 19 paths, privacy-classified). | 3,297 exact + remote; 35 exact in my copied dataset but not on remote; 1 DB via LFS; 5 local-only are `.pyc` and the `.git` pointer file. Not independent data. |
| YIOS-Visual-Forensics-Discovery-2026-10-28 | 22 / 27 MB | Earlier discovery audit of visual-forensics evidence (reports, CSV crosswalks). | 21 of 22 exact + remote; 1 local-only (`REPOSITORY_AND_GITHUB_CROSSWALK.csv`, 13 MB, a generated listing). |
| YIOS-handoffs | 2 / 8 KB | Machine-B release handoff. | Both exact and remote. |
| YIOS-Creator-Intelligence-Audit-2026-10-26 | 104 / 3.9 MB | Master guide, ledger, 87 `sources_text` files, 2 scripts. Analyst prose is AI paraphrase (see memory). | 100 local-only unique (84 source texts); 2 exact. **Not in repo.** |
| YIOS-Algorithm-Audit-2026-10-26 | 25 / 0.6 MB | Algorithm research, hypothesis tests, charts, derived CSV, receipts. | 25 of 25 local-only. **Not in repo.** |
| YIOS-local-audits | 26,547 / 22.4 GB | Four audit packages (2026-10-23, 11-02, 11-05-complete, 11-05-independent-remote-restore, 11-05-recovery-closure) plus scratch git clones and preservation stores. | 19,131 exact+remote; 2,926 git-history+remote; 66 LFS; 1,117 duplicated-within-folders (11.95 GB); 3,008 local-only (4.78 GB). |
| yios-worktree-preservation-2026-10-21 | 718 / 145 MB | Preserved worktree evidence (What If staging, thumbnails, audit). | 291 exact+remote; 23 history+remote; 49 stash-only; 321 unique local-only (115 MB, `evidence/`); 34 internal dups. |
| YIOS-Media-Library | 457 / 4.26 GB | Source MP4s: CasuallyFinance 216, xkcd 88, MonkeBiznis 64, PrimitiveEducation 45, PrimateEconomics 29, casual_economics 11, BarelyEvolved 3. | 17 files are LFS objects with pointers on remote refs; 439 have **no copy in the project/git**, each has exactly one other byte-identical copy in `YIOS-local-audits/2026-11-05-recovery-closure/recovery/payloads`. Both copies are on this Mac. |
| YIOS-recovery-2026-10-19-finance-short-experiment-01 | 1,100 / 36 MB | `original-moved` and `verified-copy` of the Finance Short experiment (each 547 files) with manifests. | 1,092 in git history, blob on remote; 2 exact; 4 local-only manifests/README; 2 internal dups. |
| yios-local-preservation-2026-10-12 | 2,281 / 841 MB | Pre-reset preservation of 2,244 original files plus inventories. | 559 exact+remote; 6 history+remote; **1,680 exist only in `stash@{0}`** (748 MB); 36 local-only inventories/scripts. |

## C. Comparison matrix (files)

| Folder | In project + remote | In project, not remote | Git history/LFS remote | Stash-only | Local-only unique | Local-only dup |
|---|---|---|---|---|---|---|
| yios-senior-health | 3,297 | 35 | 3 | 0 | 5 | 0 |
| VF-Discovery | 21 | 0 | 0 | 0 | 1 | 0 |
| handoffs | 2 | 0 | 0 | 0 | 0 | 0 |
| Creator-Intel | 2 | 0 | 0 | 0 | 100 | 2 |
| Algorithm-Audit | 0 | 0 | 0 | 0 | 25 | 0 |
| local-audits | 19,131 (+6 LFS) | 47 | 2,992 | 1 | 3,008 | 1,117 |
| worktree-preservation | 291 | 0 | 23 | 49 | 321 | 34 |
| Media-Library | 0 | 0 | 17 | 0 | 1 | 439 |
| recovery-10-19 | 2 | 0 | 1,092 | 0 | 4 | 2 |
| local-preservation-10-12 | 559 | 0 | 6 | 1,680 | 36 | 0 |

## D. Databases

20 SQLite files, 7 distinct SHA-256, all `integrity_check = ok`, user_version 0.

| SHA-256 (prefix) | Copies | Identity |
|---|---|---|
| 39e7a28ba592 (141,373,440 B) | 4 | **Identical to the canonical registry** `data/catalog/youtube_channel_registry.db` (LFS). 75 channels, 2,303 videos/transcripts, 33 datasets, 26 tables. |
| 277c09f64bc7 (52,391,936 B) | 4 | Identical to canonical `youtube_inventory.db`: 10 channels, 667 videos, 668 transcripts. |
| e3b0c44298fc | 1 | Empty 0-byte file, identical to canonical `inventory_catalog.db`. |
| a161871add6a | 6 | Reference knowledge DB, identical to the copy in project research scratch (63 constituent videos, 722 assessments). |
| d5f28e052ba0, 2aefd8b084b5, ed23b8a0462b, cbe37388ec9e, be05ff44f4d9 | 5 | **Independently rebuilt** reference DBs. Same 41 tables and same row counts (63 / 722) as the above, but different bytes (rebuild is non-deterministic). Derived, reproducible, no new records found by count. Row-level comparison was not done. |

No database holds channels, videos or transcripts beyond the canonical registry. No merge and no registry change was made.

## E. Research preservation: what is at risk

1. **`stash@{0}`** ("pre-switch from research/senior-health-complete-local-sync"): its untracked-files commit holds 1,729 files (about 757 MB, thumbnail forensics inspection panels, recovery thumbnails, `.codex` config). Exists only in this repository's local object store and in `yios-local-preservation-2026-10-12/original-files`. Both are on this Mac.
2. **4 unpushed commits** on `research/finance-economics-intelligence`.
3. **Source MP4s (4.1 GB, 439 files)**: two copies, same Mac, none in git.
4. **Creator-Intelligence and Algorithm audits**: 125 local-only files. Prior memory notes classify their prose as AI paraphrase and outcome-contaminated, so they are context, not evidence.
5. **`YIOS-local-audits` unique content** (about 12.6 GB unique, including 5.5 GB recovery payloads, 4.0 GB preservation store, 2.1 GB independent mirror clones). The 2026-11-05 packages state that 5,767 forensic checkpoint payloads remain unavailable anywhere. This audit did not find them either.
6. **Priority 1 visual forensics:** the prior 2026-10-28 discovery documents two accepted VISUAL_ONLY CT scans (`o3FQcd91MIs`, `Uumnx2Fo6cE`) with human listening and full AV BLOCKED. I did not re-run any analysis; I verified only that the discovery report and 21 of its files are published. Its other statuses (video 003 checkpoint 6 inaccessible, 645 unresolved events in 28 Shorts, 14 What If sources with unknown completion) are carried forward unverified, and none is upgraded here. The What If raw corpus (2,022 external-only files) sits in `~/GhilmanProjects/video data of what if`, outside the ten folders and **not audited here**.
7. Priority 2 (Finance 1,612-video corpus, new transcripts): no new Finance dataset was found in the ten folders beyond what the registry already has. Not re-verified at video level.
8. Priority 4: `yios-senior-health` holds competitor Senior Health data. Dr Rehan material (Decode Your Heart, DS-000032, registry says OWN_CHANNEL) is separate: docs under `docs/research/decode-your-heart-2026-09-27` and the privacy classification. The new Senior Health 16-channel and Dr Rehan Apify pilot packages (added to the project earlier today) live only in `~/YIOS-local-audits` (home directory, not Documents) and in the project; they are not in any of the ten folders.

## F. Missing project data (Documents folders vs repo)

- Source MP4 library and recovery payload store (see E3, E5).
- Stash-only thumbnail forensics files (E1).
- Creator and Algorithm audit packages.
- The 321 `evidence/` files in `yios-worktree-preservation-2026-10-21` (What If staging copies and related evidence, 115 MB). Prior discovery says the active `data/staging/what-if-forensic/v1.0.0` is absent from the checkout and this folder is the preserved external copy.
- Raw Senior Health `raw/full/*.json` of the earlier metadata acquisition: in the project (ignored) but not on remote.
- Anything outside these ten folders: UNVERIFIED.

## G. Duplicates and conflicts

- **Verified byte duplicates:** 456 Media-Library files = payloads in recovery-closure (pairs). `original-moved` vs `verified-copy` in recovery-10-19 (547 each, diff receipts empty). Registry and inventory DB copies (above).
- **Revision conflicts:** the five rebuilt reference DBs (same content counts, different bytes). Creator and Algorithm audit overlap with project docs was not found by hash; semantic overlap UNVERIFIED.
- No file was treated as duplicate by name alone.

## H. Proposed structure (not executed)

- Source MP4s: `data/raw/<channel>/media/` via LFS or external storage with a manifest (keep raw ignored by default, whitelist manifests).
- Stash-only thumbnail evidence: `data/raw/competitors/thumbnail-recovery-*` (as originally intended), with manifest.
- Creator/Algorithm audits: `docs/audits/external/` as HISTORICAL context with a "not evidence" label.
- Recovery/preservation packages: stay external and receive an off-device copy.
- Rebuilt DBs: do not archive; reproducible.

## I. Safe Phase 2 plan (proposal)

1. Push the 4 ahead commits (owner decision) and convert the stash to a branch ref (`git branch <name> stash@{0}^3` style, read-only to originals).
2. Create an off-device copy (owner must choose destination) of: MP4s, stash/preservation files, Creator/Algorithm audits. Verify hashes on the receiving side.
3. Integrate small, high-value local-only sets (Algorithm, Creator, evidence 115 MB) through the DATA_ENTRY_WORKFLOW intake.
4. Only after 1 to 3, consider redundancy review of: rebuilt DBs, `verified-copy` vs `original-moved`, scratch clones. No deletion is recommended now.

## J. Owner decisions

1. Off-device destination for the 13.35 GB at risk.
2. Push the 4 unpushed commits and preserve the stash as a branch.
3. Whether Creator/Algorithm audits enter the repo.
4. Whether `~/GhilmanProjects/video data of what if` is audited next.
5. Whether to confirm GitHub LFS server holds the payloads (needs a LFS fetch, which was out of scope).

## K. Reproducibility

- Index script and intermediate CSVs: `/private/tmp/claude-501/-Users-ghilmanislam360-Documents-youtube-intelligence-os/e79bc5e7-fda9-4b23-a154-c615d95a7ad6/scratchpad/audit/` (`idx.py`, `cls2.py`).
- Method: walk each folder (excluding `.git` internals, no symlinks found); canonical tree (7,157 files, excluding `.claude/worktrees`) plus 4 other worktrees (15,023 files) hashed with SHA-256 and git blob SHA-1 in one pass; git blobs enumerated with `git cat-file --batch-all-objects`; reachability with `git rev-list --objects --all` and `--remotes`; LFS OIDs from `git lfs ls-files --all -l` plus `.git/lfs/objects`.
- A source file was hashed only if its size equals a canonical/git/LFS blob size or another source file's size (32,468 files, 27.4 GB hashed). A file with a unique size cannot be byte-equal to anything, so classification LOCAL_ONLY is proven against the inspected stores (working tree, 4 worktrees, all local object store, LFS cache), not against objects that exist only on GitHub and were never fetched.
- Limits: usage meters unverified; no content-level comparison for "semantic overlap"; the SEMANTIC_OVERLAP and DIFFERENT_REVISION classes were not systematically computed (file-identity matching by path was not used); previous-package claims (5,767 unavailable payloads, CT status) are quoted, not re-verified.
