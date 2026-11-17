# Branch Integration Strategy

Nothing here has been executed. Every merge, deletion and push is an owner decision. Order is by risk reduction first, then by value to the proposed Explorer.

## Principles

1. **Merge leaves, not ancestors.** Closing a lineage's leaf PR closes its ancestors' PRs.
2. **Unstack unrelated work.** Senior Health work on the finance lineage moves to its own branch off main (cherry-pick of the ~7 exclusive commits), so finance and health review separately (AGENTS.md rule 16).
3. **Databases need a policy before they merge.** CI allows exactly two tracked DBs. Decide one of: (a) extend the allowlist + LFS, (b) commit the *builder* and a hash manifest and rebuild locally, (c) keep DBs on pinned evidence branches. Recommendation: **(b)**, because it keeps raw evidence immutable, keeps the repo small, and lets the Explorer rebuild a read model deterministically.
4. **Evidence branches may stay unmerged** when START_HERE pins them by SHA (CF consolidated, xkcd, Barely Evolved, Primitive Education). That is a valid end state, not debt.
5. **Never take the newer version blindly.** Example: the current branch's slop gate is newer in date than main's base but older in content than PR #51.

## Ordered plan

| Step | Action | Branches / PRs | Why | Risk | Verify |
|---|---|---|---|---|---|
| 0 | Back up the local-only stash data off-device | `preservation/stash0-untracked-LOCAL-ONLY` | Only copy of ~843 MB of thumbnails | none | checksum on copy |
| 0 | Commit untracked work to branches | `research/what-if-scripts/`, `docs/audit/`, `~/Documents/yios-senior-health` untracked files | Uncommitted = unprotected | none | `git status` clean |
| 1 | Fast-forward local main; drop `90f9cd22` from the current branch | main, current | Removes the duplicate gate | low | `git log origin/main..` |
| 2 | Merge small green PRs | #52, #49, #24, #22 | CI green or docs-only | low | CI |
| 3 | Re-run CI on the "failed before any step" PRs, then merge | #38, #39, #43, #41 | Snapshot data + media library | low | CI |
| 4 | Land Finance CI gates | #45 (retarget to main after #36, or replay its 6 commits on main) | Closes debt D1: mandatory gates not in CI | medium (AGENTS.md conflict) | `tests/test_ci_workflow_gates.py` |
| 5 | Adopt the DB policy, then land the finance corpus | #36 (+ data/finance-economics-complete) | Fixes the "unapproved databases" CI failure | medium | CI + builder reproduces hash |
| 6 | Unstack Senior Health | current branch → new branch off main; #50 + data/exercise-apify; claude/dr-rehan…; docs/dr-rehan-recording-pack | Topic separation | medium | per-branch CI |
| 7 | CF lineage: rebase the docs of `cleanup/yios-phase2-batch1` onto main; keep evidence pinned | close #21, #28, #37, #47 | Avoid importing 6,947 files | medium | START_HERE links resolve |
| 8 | What If: choose one master plan | #44 vs `research/what-if-brain-preservation-batch1` | Two conflicting `YIOS_MASTER_PLAN.md` | medium (owner choice) | diff review |
| 9 | Code-review then merge | #25 (touches registry builder + Apify ingest), #46 (fix recorded validator failure), #20 (re-apply via script; it edits committed DBs) | Shared-code changes | medium | full pytest |
| 10 | Decide the dual-machine CLI | `codex/yios-dual-machine-coordination` | Extract its 1 tooling commit or archive | low | its 3 test files |
| 11 | Production branches → archive tags | #26, #29, #30, #32, #34 | Media-heavy records, not shared code | low | tag exists |
| 12 | Delete merged/orphan/stale refs | 20 merged, 3 `yios-test/*`, 3 stale (archive tag first) | Reduce noise from 75 to ~25 | low | `git branch -a` |

## What the proposed Explorer needs from this

Hard prerequisites: step 5's DB policy (the Explorer's read model must know which DBs are canonical), #41 media library (thumbnails and frames), and reference KB migration `011` on main. Everything else can stay on pinned branches. The Explorer reads them through an index, not through merges.

## Regression requirements per merge

`python -m pytest -q`, `ruff check scripts tests`, `scan_tracked_secrets.py`, `validate_dataset_ledgers`, `validate_youtube_channel_registry`, the DB integrity step, and (after step 4) the finance gates. CI already runs all of these except the finance gates.
