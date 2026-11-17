# Option A — main-based What If archive integration result

Machine A, 2026-10-25. **VERIFIED / COMMITTED / PUSHED / REMOTE_RETRIEVED.** Stopped after the authorized candidate integration. No PR or merge was created. This is repository archival integration readiness, not complete binary restoration or production-engine readiness.

## Published candidate

- Canonical checkout: `/Users/ghilmankhan/workprojects/youtube-intelligence-os` (one worktree).
- Branch: `codex/what-if-archive-main-integration`.
- Base main: `08e719264e31ecd82de24f8eeb8f065c08359fe5`.
- Final HEAD and upstream/advertised remote: `badec432bbf5610748123b3f0e0bcb9cdb25fa10`.
- [Published commit](https://github.com/ghilmanITM360/youtube-intelligence-os/commit/badec432bbf5610748123b3f0e0bcb9cdb25fa10).
- Final documentation-repair parent: `f0373a8d590af58d3c8578e0a5237a23616bd782`.

| Original source commit | New main-based commit | Changed paths |
|---|---|---:|
| `5f7afcbf16e27ed93aa37401208baa7fe6167052` | `d4111afc20443b22fba5614ef8505e46dcf7c151` | 51 |
| `b928b95d96f5903b111336c495df80227ad31f36` | `f5cf5479ff1930360799609fe3dc626fc4fe016e` | 258 |
| `1c5a2d4b222eb5b4902eab9765dbb5423f594948` | `7bea4298616edba36eaf0dd05103b30b3c97dfa4` | 82 |
| `dcbdc7d8c24d5d3ccd28bdd4fdf5e9fc90a7cf67` | `f4703d64c7668d1f6029e28d6431055dfbb2db8f` | 6 |
| `abdcf8e04c16bfc0c9495fcbd05b0c6bb64951b0` | `f0373a8d590af58d3c8578e0a5237a23616bd782` | 3 |

A sixth atomic commit, `badec432bbf5610748123b3f0e0bcb9cdb25fa10`, corrects only the two documentation files (26 insertions, eight deletions). Every replay includes `cherry picked from commit` traceability. Every new parent was verified locally and independently through GitHub's Git commit API; the first replay's parent is approved main. All cherry-picks completed cleanly, without conflicts or resolution. The original archive branch and all original commits remain unchanged locally and remotely.

## Scope and ancestry proof

Final main comparison: **400 paths = 399 additions + one README modification**. Research additions: **397 files / 8,221,384 bytes**, comprising 315 under `research/visual-forensics/channels/CH-000004/what-if-source-package/` and 82 under `research/production-experiments/what-if-derived/`. The other additions are `docs/YIOS_MASTER_PLAN.md` and `docs/AI_SESSION_CONTEXT.md`. README adds exactly two navigation lines.

There are exactly six new linear commits after main and **zero of the 134 inherited Finance-side commits** in candidate ancestry. Exact changed-path membership equals the authorized 397 research paths plus the two documents and README. No Finance files, inherited forensic package, `.gitattributes`, knowledge/status additions or Finance README footer were imported. `scripts/`, `data/`, `schemas/` and `tests/` have no changes against main. The full 1,337 inherited-path change set was not replayed; README's authorized navigation is its only overlapping path.

## Integrity and validation

- All 397 worktree and candidate committed blobs match original committed source bytes and the previously verified SHA-256 baseline; aggregate count and bytes match exactly. The receipt records every path, size and SHA-256.
- Independent GitHub retrieval fetched **all 400 changed file blobs**, not a sample: all 397 research files, both documents and README. Every retrieved byte sequence equals the local candidate; each Git blob identity and SHA-256 checked. GitHub tree was complete/non-truncated, remote branch ref checked before and after retrieval, and all six remote parents matched.
- Active RELEASE_MANIFEST: all 50 present entries match recorded bytes/hashes, including eight MASTER tables. Historical missing external distribution is not inferred from this check. Source index/map match contract artifact hashes. Contract remains 14 sources: 12 VERIFIED, two UNRESOLVED. No registration, catalog, observation-index, schema, adapter or consumer-behavior changes.
- Parsed 36 JSON files, 132 CSV files and 15 Python scripts (AST only). Twelve historical CSV-width defect files remain byte-identical. Historical research whitespace-check output matches the original source baseline exactly (52,301 output lines, including displayed source lines; this is not a count of distinct defects). See `OPTION_A_HISTORICAL_WHITESPACE.txt`. New documentation passes `git diff --check`.
- Production experiments remain in their separate root. Rejected/provisional experiments, measured/inferred distinctions, uncertainty and historical PREPARING frozen metadata are unchanged. No audio, MP4, frame or CapCut binary additions.
- Actual main-based candidate regression: **35 passed in 1.00s**. Command: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m pytest -q -p no:cacheprovider tests/test_what_if_source_contract.py tests/test_what_if_forensic_brain_adapter.py tests/test_stage_what_if_forensics.py tests/test_query_what_if_forensics.py tests/test_editing_visual_intelligence.py`. No pytest cache/bytecode written by this run. Existing ignored local evidence can participate; this is not an independent-machine restore.
- Independent read-only final reviewer found no blocking findings after checking scope, all research hashes, ancestry, README and doc repairs.
- **Hosted CI: NOT_VERIFIED.** GitHub run list for exact final HEAD returned `[]`. Local tests do not imply hosted success. Full media reconstruction, CapCut/tool execution and independent binary restore are **BLOCKED / NOT_RUN** outside this scope. JSON syntax/manifest checks and focused tests are not a claim of exhaustive schema or all-project test execution.

## Documentation corrections

Eight broken relative-link occurrences covering seven distinct authorities now use immutable GitHub URLs pinned to Finance SHA `1adb8129f689207552f0838414e5823e4255bde1`. Each authority was authenticated, actually retrieved and byte-compared with its committed blob. They are explicitly dated historical authorities, not live Finance state or locally integrated Finance evidence. The receipt lists all seven paths, blob IDs, hashes and byte sizes.

All repository-relative links resolve: README five, master plan 19, session context seven. Other valid relative links were preserved. README SHA-256 equals the reviewed main-plus-navigation result `a2c1a9206668d59362ae5799bed25e14116a2d79b1ed9593c31e2c983699a413`; no inherited Research discovery footer. Session context adds the main base, new branch and five source-to-candidate mappings without rewriting dated snapshots, and distinguishes publication, main merge and binary restoration. AGENTS.md unchanged.

## Protected state, ownership and resources

Main `08e719264e31ecd82de24f8eeb8f065c08359fe5`, Finance `1adb8129f689207552f0838414e5823e4255bde1`, forensic `090f84b3292a3b6c6e94653a6ef1867726e4ebdd` and original topic `abdcf8e04c16bfc0c9495fcbd05b0c6bb64951b0` remain unchanged locally and on origin. PR #36 remains OPEN/DRAFT, same Finance head/main base; no modifications. There is no PR for the new branch.

Tracked tree/index clean. Stash `5b6c3042679400b16aa1024b79058b71dade0ab9` unchanged. Untracked roots remain `finance-short-02-visual-calibration/`, `productions/`, `research/casually-finance-script-intelligence/`. All pre-existing untracked/ignored file size/mtime/inode snapshots unchanged. Before switch, every such path was checked against main for collisions; `git switch --no-overwrite-ignore` added a safety gate. No stash, cleanup or overwrite operation occurred.

Owner granted exclusive scoped Machine A integration authority; local process/thread checks found no competing active YIOS writer. Claude PIDs 79913/79948 absent; known Codex app helpers retained cwd. This is bounded local evidence, not a distributed lock or inspection of Machine B's unpublished disk state. Finance ownership conflict and protected forensic writer reservation remain unchanged. No further repository activity is authorized by this report.

Five-hour usage **51% → 58%**, weekly **14% → 15%**. Credits zero; none spent or reset. Context adequate, no compaction. Available disk initially 13,149,484 KiB (~12.54 GiB), final measured 10,223,904 KiB (~9.75 GiB); APFS/system availability fluctuated and this difference is not attributed to the bounded audit files. No media decoding, installation, cloud storage or binary scans. Only the authorized checkout changes and external execution evidence were written.

## Remaining preservation boundaries

Binary portability remains **BLOCKED / NOT_VERIFIED**: frozen release ZIP absent; missing `0921.mp4`, nine PNGs and narration MP3; original videos/audio/frames, CapCut project, fonts/runtime remain external. PNGs: BG_01_offwhite, CHAIR_01, STOPWATCH_OUTLINE_01, WARNING_TRIANGLE_01, PERSON_SEATED_01, PERSON_STANDING_01, UNSTEADY_ARCS_01, SCORE_CARD_EMPTY_01, DIAGNOSIS_CARD_EMPTY_01 (all `.png`). Narration: `Before_you_try_the_30-second_Educational_Science_Narration_Male.mp3`. Existing broken Downloads symlink was not modified.

CF gray.npy exact reproducibility, remote LFS restoration, bundle prerequisite availability and independent private binary restore remain unverified. Two What If source identities remain unresolved. Historical defects, absolute paths, licensing/provenance limitations and sixty held/duplicate proposal records retain prior statuses. No new global dependency investigation occurred. Original external evidence, Video 003 checkpoint 6 and all prior audit/publication receipts remain untouched; Video 003 remains partial, not resumed.

## Receipt and complete continuation handoff

`OPTION_A_EXECUTION_RECEIPT.json` SHA-256: `96a3f4d8809eae2e0fdb0d6798d195ee9b99bbab60d2a24a95bbca54472b4914`. It contains preflight, exact untracked/ignored snapshots, five mappings and parents, complete 397-file baseline, all 400 retrieved remote file hashes, six remote parents, pinned-authority retrievals, local validations and final protected refs/PR/status/resources. Reproduction/check scripts: `OPTION_A_VALIDATE.py`, `OPTION_A_REMOTE_VERIFY.py`; per-pick logs and documentation staged diff are external audit evidence, not permanent project authorities. Original review and all previous reports/receipts preserved unchanged.

**Next bounded step requires separate owner approval:** create/review an archive-only PR from `codex/what-if-archive-main-integration` to main after fresh resources, ownership, refs, 400-path scope and exact final HEAD checks. PR description should disclose six candidate commits, original mapping, 397 byte-exact research files, doc repair, zero inherited Finance ancestors, local tests, CI NOT_VERIFIED and external binary limitations. No PR or merge permission is implied here. If main moves, reassess ancestry and validations before proposing changes; do not automatically rebase or retarget.

Recovery anchors are unchanged original source branch/commits and authenticated receipts. On any later discrepancy, preserve this candidate and report exact state; do not reset, force-push, delete branches, mutate stashes or auto-switch another session. A rejected candidate can remain published pending owner decision. No automatic rollback or next batch.

**STOP — authorized integration and exact remote retrieval complete.**
