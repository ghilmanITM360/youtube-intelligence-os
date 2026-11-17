# YIOS ancestry-aware archive integration review

Dated 2026-10-25, Machine A. **READ-ONLY REVIEW COMPLETED. Integration NOT EXECUTED.**

## Decision

Recommend **Option A: a separately authorized archive-only branch from validated main**, with a narrowly scoped documentation-link adjustment. Main already contains the required What If implementation. No Finance code/schema prerequisite was identified. Applying all five commits without adjustment would leave eight broken documentation links to seven Finance-side targets. Preserve those authorities using immutable GitHub links, rather than importing their history or copying their contents.

Do not merge the existing topic branch into main: its complete comparison includes 134 unapproved inherited commits. Option A is viable for repository archival integration, not standalone production or binary restoration. No branch, commit, PR, cherry-pick, merge, checkout switch, rebase, clone or worktree was created in this review.

## Live refs, ownership and preserved state

Local HEAD, upstream and advertised origin topic ref agree:
`abdcf8e04c16bfc0c9495fcbd05b0c6bb64951b0`, branch `research/what-if-brain-preservation-batch1`.

| Ref | Independently advertised live SHA |
|---|---|
| main | `08e719264e31ecd82de24f8eeb8f065c08359fe5` |
| research/finance-economics-intelligence | `1adb8129f689207552f0838414e5823e4255bde1` |
| research/casually-finance-editing-forensics | `090f84b3292a3b6c6e94653a6ef1867726e4ebdd` |

No movement from the supplied snapshot. Authenticated GitHub PR #36 remains OPEN/DRAFT, Finance head above, base main above; its title still says 966-video audit and must not be used to infer current population. No modification to PR #36.

Tracked/index status clean before and after review. One canonical worktree. Stash `5b6c3042679400b16aa1024b79058b71dade0ab9` unchanged. Untracked roots unchanged: `finance-short-02-visual-calibration/`, `productions/`, `research/casually-finance-script-intelligence/`. No source, forensic evidence, archived bytes or repository documentation was edited.

PID 79913/helper 79948 absent. Persistent observed checkout cwd holders 64032/64035/64036/64056 are Codex helpers under this app server PID 49883; transient inspection commands exited. App thread inventory showed only this YIOS chat active; no competing local YIOS writer observed. This is bounded local evidence, not a distributed lock or proof about Machine B's unpushed disk state. Current authority is read-only only. Conflicting historical Finance ownership declarations remain unresolved; protected forensic writer Claude session `873b9a27-ba03-4183-aa61-f82d01f65998` remains reserved. Fresh exclusive writer authorization/checks are mandatory before any future branch operation.

## Exact ancestry and change sets

Merge base of main and archive topic is **main itself**, `08e719264e31ecd82de24f8eeb8f065c08359fe5`. Main has no commits beyond the recorded snapshot. Finance head is an ancestor of topic HEAD. There are 134 linear Finance-side commits between main and Finance head, zero merge commits, followed by five authorized commits. “Finance-side” describes ancestry: it also includes unrelated YouTube knowledge, status and Visual Forensics work.

| Authorized commit | Exact parent | Change |
|---|---|---|
| `5f7afcbf16e27ed93aa37401208baa7fe6167052` | `1adb8129f689207552f0838414e5823e4255bde1` | 51 brain additions / 2,252,704 bytes |
| `b928b95d96f5903b111336c495df80227ad31f36` | `5f7afcbf16e27ed93aa37401208baa7fe6167052` | 258 per-video additions / 2,610,687 bytes |
| `1c5a2d4b222eb5b4902eab9765dbb5423f594948` | `b928b95d96f5903b111336c495df80227ad31f36` | 82 experiment additions / 3,230,459 bytes |
| `dcbdc7d8c24d5d3ccd28bdd4fdf5e9fc90a7cf67` | `1c5a2d4b222eb5b4902eab9765dbb5423f594948` | Six report/frozen-metadata additions / 127,534 bytes |
| `abdcf8e04c16bfc0c9495fcbd05b0c6bb64951b0` | `dcbdc7d8c24d5d3ccd28bdd4fdf5e9fc90a7cf67` | Two documentation additions; README navigation only |

| Comparison | Commits | Distinct changed paths | Net status |
|---|---:|---:|---|
| main → Finance checkpoint | 134 | 1,337 | 1,335 added, two modified |
| Finance checkpoint → topic HEAD | 5 | 400 | 399 added, one modified |
| main → topic HEAD (ordinary PR to main) | 139 | 1,736 | 1,734 added, two modified |

Inherited paths: 1,066 Finance research; 230 Visual Forensics; 30 `knowledge/youtube`; seven dated project-status reports; plus `.gitattributes`, root README, `docs/research/README.md` and `research/README.md`. Finance-side changes include audit ledgers/JSONL, workbook and thumbnails, forensic methodology/evidence, research indexes and whitespace attributes. These are not authorized archive additions. Full exact commit and path inventories are in the associated JSON receipt.

Authorized research is **397 files / 8,221,384 bytes**, independently recomputed from committed blobs: 315 paths below `research/visual-forensics/channels/CH-000004/what-if-source-package/` and 82 below `research/production-experiments/what-if-derived/`. Add two documents and modified README = 400 paths. Only README overlaps the inherited changed-path set. Batch 4's immutable 401-additions claim remains erroneous and unchanged.

## Archive-only tree/dependency assessment

Performed object/tree reads and an in-memory path union, not a checkout or Git patch application. All 399 added paths are absent from main; no add/add collision. Directories need no separate Git records. The sole modified file's patch context matches main: inserting the two README navigation lines preserves all main README content. Do not copy HEAD's entire README: that would also import the inherited Finance “Research discovery” footer. Simulated main-plus-navigation README SHA-256: `a2c1a9206668d59362ae5799bed25e14116a2d79b1ed9593c31e2c983699a413`.

No differences between main and topic under `scripts/`, `data/`, `schemas/` or `tests/`. In particular main contains:

- `data/manifests/what-if-forensic-source-v1.json` (14-source contract).
- `scripts/validate_what_if_source_contract.py`, `scripts/source_adapters/what_if_forensic_brain.py`.
- `scripts/stage_what_if_forensics.py`, `scripts/promote_what_if_forensics.py`, `scripts/query_what_if_forensics.py` and the existing intelligence consumer/tests.
- `docs/WHAT_IF_FORENSIC_SOURCE_CONTRACT.md`, `docs/WHAT_IF_INTEGRATION_WORKFLOW.md`, repository safety audit, Architecture/Phases/provenance/registry/catalog documentation and existing schemas.

PR #36 contains research authorities linked by the new documents, but no required new What If runtime/schema implementation. Archive-only integration requires no registry/source promotion, new observation index or production-engine changes. All eight MASTER tables match active release hashes and byte lengths. Source index/map match main contract artifact hashes; contract/index/map contain matching 14 IDs, with 12 VERIFIED and two UNRESOLVED. These checks do not authenticate media anew.

The 34 relative links in the two new docs would have eight unavailable occurrences, seven distinct targets:
- `research/finance-economics-intelligence/FINANCE_WEEKEND_HANDOFF_2026-10-23.md`
- `research/finance-economics-intelligence/FINANCE_WRITER_OWNERSHIP.md`
- `research/finance-economics-intelligence/METHODS.md`
- `research/finance-economics-intelligence/README.md`
- `research/finance-economics-intelligence/RESUME_HERE.md`
- `research/visual-forensics/README.md`
- `research/visual-forensics/methodology/README.md`

All seven were independently located in GitHub's non-truncated recursive Finance-commit tree and their blob IDs equal local Git. Proposed repair: replace only these relative destinations with `https://github.com/ghilmanITM360/youtube-intelligence-os/blob/1adb8129f689207552f0838414e5823e4255bde1/<path>`, explicitly treating them as historical external authorities until separately integrated. The visual index appears in both documents. Keep remaining relative links and historical snapshot wording. Future context updates should record the newly authorized branch/base and source-to-new-commit mapping without rewriting prior snapshots. No Finance files need be copied. Broken-link repair and context refresh need explicit next-stage authorization.

Per-video references retain their original relative locations inside the archive; original media, historical absolute paths and non-integrated legacy references remain dependencies, as recorded in prior batch receipts. Experiments remain separate, with rejected/provisional results unchanged. No archive commit changes active indexes, source joins, training data or adapters. Archive presence is not automatic consumer activation. Existing consumers require configured external corpus/media and validated ignored staging/catalog/runtime; their availability is distinct from adding research to main.

## Options

| Dimension | A — independent main-based archive branch | B — stack against Finance | C — wait for Finance |
|---|---|---|---|
| Proposed main change | 397 exact research additions + two docs + README; narrow doc link/context adjustments | Eventually same archive delta, after Finance acceptance; never merge topic directly to current main | No immediate change; recompute delta after Finance integration |
| Finance exposure | Zero inherited commits in new branch ancestry; seven pinned historical links only | Five-commit comparison is clean now, but base is unapproved Finance history | Finance acceptance/ownership becomes prerequisite |
| Code/schema | Already in main; seven doc targets need adjustment | All linked authorities present on base | Depends on eventual main tree |
| History | New commit IDs; preserve original branch/receipts and record source mapping | Existing five IDs retained; no rewrite needed | Published originals retained; squash/rebase of Finance could require new integration strategy |
| Ownership | Separate Machine A archive integration authorization; no Finance ownership transfer | Finance owner coordination/review sequence required | Finance owner reconciliation required first |
| Validation | Fresh hashes, links, exact main diff, local regressions and independent retrieval | Same plus stacked-base/ref verification | All checks repeated after base changes |
| Complexity/risk | Bounded doc repair; real patch/test execution still pending | Low immediate diff complexity, higher long-term coupling/reviewer confusion | Lowest immediate mutation risk; indefinite delay and changing-base risk |
| Reversibility/folder | Additive new branch in same checkout; originals untouched | Preserve branch; PR changes need approval | No working-folder change |

B cleanly isolates the 400-path delta **only** with base `research/finance-economics-intelligence` at `1adb...`; review Finance PR #36 first, then archive delta, then revalidate final main comparison. It delays main integration but not existing GitHub archival availability. C also preserves published research safely while waiting, yet adds no missing runtime prerequisite and makes archival progress depend on separate ownership/research acceptance. Neither is preferred over bounded A.

## Validation, blockers and portability boundary

Fresh focused local regression: **35 passed in 0.95s**, using no pytest cache or bytecode writes. Exact command is in receipt. These run in the current checkout against runtime/data/test files identical to main; ignored local evidence may participate. They are **not** an execution test of an actual main-based tree. No branch creation or cherry-pick was attempted; Git-level application/conflict resolution remains NOT_EXECUTED. Hosted CI returned no runs for current HEAD: **NOT_VERIFIED**, not PASS.

New-tree acceptance must verify all 397 SHA-256 values against original committed blobs and prior source/publication receipts, 8,221,384 bytes, all links, schemas/manifests, unchanged historical defects/statuses, unchanged 14-source contract, experiment isolation and the exact main-base diff. No need to regenerate or promote source data. Source-contract media authentication requires separately available external media; do not replace it with synthetic test success.

Repository integration readiness is conditional on authorization, actual patch application, doc repair and fresh validation. Binary portability remains **BLOCKED / NOT_VERIFIED**: frozen release ZIP missing; `0921.mp4`, nine PNGs and narration MP3 absent at recorded paths; external original MP4/audio/frames, CapCut/fonts/runtime dependencies; unproven CF gray.npy regeneration; remote LFS and independent binary restoration unverified. Two source identities remain unresolved and twelve historical CSV row-width defects remain preserved. Do not alter these while integrating. No new binary/global-source audit was performed.

## Next separately authorizable execution step

Authorize one bounded archive-integration stage on proposed branch **`codex/what-if-archive-main-integration`**, confirmed absent locally and remotely during this review:

1. Fresh resource/ref/session checks and explicit exclusive Machine A writer ownership. Preserve Machine B work and protected sessions. Stop on unexplained ref movement or dirty tracked state; do not stash/clean others' work.
2. Explicitly authorize creating/switching that branch in the one canonical checkout from revalidated main `08e719...` (or stop and review any newer main). No worktree/clone workaround.
3. Apply only the five exact authorized commits above, in order, retaining original branch/commits unchanged. Record old-to-new SHA and parent mapping. Do not copy the full topic tree or inherited README footer. No automatic conflict workaround or scope expansion.
4. Separately authorized documentation-only follow-up: seven pinned targets/eight occurrences and a dated new-branch context clarification. Research bytes must remain exact. Preserve original authority documents and historical snapshots.
5. Validate the actual candidate tree: 399 additions plus README modification, 400 total paths, zero changes outside the two research roots/two docs/README, no Finance/forensic files inherited; verify source/staged/commit SHA-256, contract/table checks, link checks, focused regressions and full diff. Treat external-data-dependent checks as BLOCKED when absent. Historical whitespace/CSV defects need explicit bounded baseline handling, never silent repair.
6. If explicitly authorized, normal push and independent exact-commit retrieval/hash verification; report hosted CI separately. A future draft PR must target main and describe only this archive/documentation delta. **PR creation and any merge require separate explicit authorization; neither is granted by this review.**

Recovery plan: original five commits, branch and remote receipts remain immutable recovery anchors. Stop on any discrepancy and retain partial candidate commits plus external handoff. No hard reset, force-push, branch deletion, stash mutation or automatic rollback. If candidate is rejected, leave it preserved for owner review; later reversal of accepted changes would need an explicitly reviewed revert, not history rewrite. Recheck checkout availability before any voluntary branch return; never switch another owner's session.

## Verification receipt, resources and handoff

Associated `ANCESTRY_INTEGRATION_VERIFICATION.json` contains full 134/5/139 commit lists, exact path/status sets, 397 committed-file hashes/sizes, master/contract checks, all 34 doc links, remote dependency blobs, ref/PR snapshot, baseline/final status and stash, existing publication receipt hashes and test command. Its SHA-256 is **373f3419c239d23d7d34497941cb78d5e63bc31445ecfc4ab35661827f49ba2e**. Prior batch and documentation receipts were read, not modified. This review did not re-retrieve every previously published research file; earlier exact retrieval receipts remain the publication evidence.

Resource snapshot: five-hour usage 44% → 49%; weekly 13% → 13%; zero paid credits and none spent/reset. Context adequate; no compaction or media decoding. Start disk 13,170,916 KiB available (about 12.6 GiB); end disk 13,158,428 KiB available; only bounded external report/receipt written by this review. No distributed-lock or fresh Machine B owner confirmation claimed.

**Stop here.** Await explicit Option A execution, documentation adjustment and publication scope authorization. Finance/PR #36, Video 003, protected forensic work, binary preservation and production implementation remain separate and untouched.
