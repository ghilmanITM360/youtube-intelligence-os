# Owner manual folder delete shortlist

2026-10-28, Machine A. **Whole folders eligible:** zero. **Child files certified for deletion:** zero. No files deleted. Machine B is not mounted; its saving is **unknown**, not zero.

## 1. Whole-folder candidates

None certified. A complete folder may hide one unique reviewer shard, script, source frame, Git object or cloud-only original. No directory in the matrix passed all required SHA, publication, restore, dependency, rights and APFS space tests.

## 2. Partial-cleanup opportunities, still blocked

| Exact path | Files | Logical / allocated | Why it looks promising | Verified replacement | Missing checks | Currently reclaimable | Owner action |
|---|---:|---|---|---|---|---:|---|
| `/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research` | 2,037 | 1.149 / 1.153 GiB | Older 6.5 KB report differs from PR #21 latest 29 KB report (`043b85bf`); `_work` may be derived | PR #21 current corpus only; external historical report SHA `99a3d375d3fe8c9293045cd75869cef8f9db6b6297cc4b8ee65e685734f1e38a` differs; JPG/cache/source not recovered | Per-file SHA crosswalk; private recovery of all original/support evidence; active dependency; APFS clone check | 0 certified | KEEP; review child inventory later |
| `/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd` | 1,781 | 1.557 / 1.561 GiB | Selected V7 backup contains historical duplicates | Historical receipts, not full restore proof | Per-file exact/independent restore; active ref; nested unique content | 0 certified | KEEP |
| `/Users/ghilmankhan/Downloads/video data of what if` | 2,472 | 0.644 / 0.649 GiB | Workprojects What If folder overlaps; 51 Brain files historically matched | PR #44 contains selected docs at `f345abde`; not originals | Whole-tree byte comparison, active CapCut dependencies, independently recoverable MP4s | 0 certified | KEEP |
| `/Users/ghilmankhan/workprojects/yios-visual-forensics-install-candidate-2026-10-24` | 45 | 0.0003 / 0.0004 GiB | Small methodology candidate may overlap installed kit | None certified | Prompt/version identity and install dependency | 0 certified | KEEP |

No child is certified redundant or deletion-ready. Exact child paths can become candidates only after source hashes, version comparison and recovery are proven. The `MANUAL_CLEANUP_REVIEW.md` from the prior audit also certified zero.

## 3. Folders to preserve

Canonical repo; three Casually Finance CT directories (especially protected Video 003); 38 Shorts evidence; all original MP4 folders; What If source/Brain; private backup mappings; research export audits; Finance checkpoint/recovery directories. `yios-git-recovery` mixes Finance with unrelated `offline-map` trees, so no whole-root decision.

| Large protected root | Allocated blocks | Why not a cleanup candidate |
|---|---:|---|
| `/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence` | 4.153 GiB | 38 Shorts' frame/audio/array evidence; Machine B exact match and independent restore unproved. |
| `/Users/ghilmankhan/Downloads/videos in mp3` | 4.065 GiB | Multi-channel original MP4s; no independently tested private recovery. |
| `/Users/ghilmankhan/YIOS-local-audits` | 3.297 GiB | CT evidence, Video 003 protected reviewer shards, Finance checkpoints and historical receipts. |
| `/Users/ghilmankhan/yios-git-recovery` | 2.788 GiB | Mixed Finance recovery and unrelated `offline-map` content; child identities and active dependencies need separate review. |
| `/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research` | 1.153 GiB | Derived/historical version and binary evidence; source report differs from latest published bytes. |

These are occupied sizes, **not** estimated safe savings. Parent/child rows overlap. `workprojects/youtube-intelligence-os` occupies 8.338 GiB including Git and untracked content; do not prune its objects or source files.

## 4. Blockers and real SSD estimate

Machine A: **0 bytes certified reclaimable now**. The table's allocated bytes show an upper bound for specific candidate roots, not guaranteed savings; nested rows overlap and APFS clones/hard links/cloud state can reduce it. Biggest inspected candidate roots alone occupy about 3.36 GiB in allocated blocks, but deleting them now risks unique evidence. Machine B: **not accessible**, so allocated size and possible savings are unknown. Machine B audit package was unavailable here. Need a verified private restore test, per-file exact content map, active writer/dependency confirmation and Machine B on-device inventory before any manual delete review can pass.

## Recovery / rollback requirement

Before a candidate can be marked REVIEW DELETE: retain exact SHA-256 of each required file, verify an independent durable backup, physically restore a representative essential sample to a safe destination and compare hashes, check Git/LFS payload rather than pointer alone, and confirm no active project references. iCloud-synced deletion can remove cloud copies. There is no approved rollback location for these current candidates.
