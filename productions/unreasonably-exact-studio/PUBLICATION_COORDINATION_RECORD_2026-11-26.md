# Publication coordination record: 26 November 2026

**Writer:** Claude, on Machine B. The owner directed it in the Claude Code chat to consolidate and publish the Unreasonably Exact production system, with a stated preference for a dedicated production branch.

## Checks before writing

- **Canonical checkout:** `/Users/ghilmanislam360/Documents/youtube-intelligence-os`.
  - It was on `research/what-if-channel-strategy-2026-11-18` at `5ee988ce`, equal to origin after `git fetch`.
  - Its only change was one pre-existing untracked workbook (`research/consolidation/XKCD_WHATIF_COMPLETE_DATA_WORKBOOK_2026-11-24.xlsx`). It was left untouched and was not committed.
- **Existing worktree:** `.claude/worktrees/yios-canonical` on `feat/yios-canonical-data-2026-11-17`. Not touched, and no new worktree was created (AGENTS.md permanent worktree rule).
- **Remote refs:** there were no `refs/heads/production/*`, no `refs/heads/yios/claims/*` and no `refs/heads/yios/integration/*` (only the unrelated `yios-test/…` finance test claims). No competing writer claim was found.
- **Machine A:** its unpublished local state cannot be seen from Machine B.

## Branch decision

- **Created:** `production/unreasonably-exact-studio`, from `origin/research/what-if-channel-strategy-2026-11-18` at `5ee988ce`.
- **Reasons:**
  1. It is the owner's stated preference.
  2. A production system (engine, tools, asset library, playbooks) is a different kind of content from the channel strategy research, and keeping it on its own branch avoids mixing review histories.
  3. A new branch cannot conflict with another writer's work on the channel branch.
- **Integration:** the channel branch is unchanged. Any merge back is a separate, owner-approved step; nothing is merged automatically.

## Publication method

- A normal commit and a normal push, with no force.
- The pre-commit AI-slop gate ran through the installed hook.
- Static checks from `.github/workflows/validate.yml` were run locally on the changed paths (see the commit message).
- Large media, unlicensed audio and credentials are excluded (`REPOSITORY_README.md`).
- The owner's authorization covers publication only. It is not a scientific, editorial or licensing approval of anything in this folder.
