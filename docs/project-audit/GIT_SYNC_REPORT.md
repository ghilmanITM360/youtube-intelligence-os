# Git Sync Report — 2026-11-11

All values below were observed with git/gh commands in this session. Nothing was pushed.

| Item | Value |
|---|---|
| Repo | `/Users/ghilmanislam360/Documents/youtube-intelligence-os`, origin `https://github.com/ghilmanITM360/youtube-intelligence-os.git` (private) |
| Remote default branch | `main` (`origin/HEAD -> origin/main`) |
| Original branch / HEAD | `research/finance-economics-intelligence` @ `f115285b` |
| Tracked upstream | `origin/research/finance-economics-intelligence` @ `f115285b` (0 ahead / 0 behind) |
| Initial working tree | clean (0 modified, 0 untracked); stash `stash@{0}` (senior-health pre-switch) untouched |
| In-progress merge/rebase | none |
| Fetch | `git fetch origin --prune` OK (auth working); 6 new remote branches, 3 updated |
| `origin/main` before/after | `fd029485` (3 commits ahead of local `main` @ `08e71926`) |
| Backup | local tag `audit-backup/pre-sync-2026-11-11` -> `f115285b` (every pre-sync commit is also on the remote) |

## Actions
1. `git fetch origin main:main` — fast-forwarded local `main` `08e71926 -> fd029485` (not checked out, pure fast-forward).
2. `git merge-tree` dry run of `origin/main` into the research branch: no conflicts (20 docs/research files added, `README.md` modified).
3. `git merge --no-ff origin/main` on the research branch -> local merge commit **`2b6ccea5`** (docs-only: `docs/START_HERE.md`, `research/casually-finance/*`, `research/consolidation/*`, README). **Not pushed.**
   - The research branch is 210 commits ahead / 0 behind `origin/main`; it had never been merged with the three consolidation PRs (#46–#48 era).

## Final state
- Local branch `research/finance-economics-intelligence` @ `2b6ccea5`: 0 behind `origin/main`, **1 ahead** of its own upstream (the merge commit) plus the uncommitted audit edits listed in the roadmap/test reports.
- Remaining remote differences: none that are newer than local. Unpushed: merge commit `2b6ccea5` and audit changes.
- Undo path: `git reset --hard audit-backup/pre-sync-2026-11-11` is available **only on the owner's decision** (not run).

## Observations
- 20+ open PRs, nearly all drafts (#20–#47). #36 (this Finance branch) is draft and in-progress; the repository is run as several long-lived research branches rather than merged increments.
- Local worktrees exist at `.claude/worktrees/*` and `~/.codex/worktrees/*`; local branch `candidate/finance-integration-2026-11-02` is at the same SHA as this branch.
- `.git` is 5.4 GB (3.08 GiB pack); `data/raw` alone is 850 MB tracked.
- Finance stream is under a two-machine alternating-writer protocol (`research/finance-economics-intelligence/FINANCE_WRITER_OWNERSHIP.md`). Pushing the merge commit is a protocol decision for the owner.
