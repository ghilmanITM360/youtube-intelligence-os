# YIOS GitHub Publication Status — 2026-11-11

Repository: `ghilmanITM360/youtube-intelligence-os`. Local commit ≠ published; each line below was checked with `git ls-remote`.

| Ref | Commit | Remote | Note |
|---|---|---|---|
| `research/finance-economics-intelligence` | 2b6ccea5 | VERIFIED (ff push, no force) | the 4 ahead commits |
| `consolidation/selected-folders-2026-11-11` | ceca7d19 (+ this status doc) | VERIFIED | PR #49 |
| `data/ds-000011-supplement-2026-11-11` | 97eef476 | pushed earlier, no PR | 5 training files |

PR: https://github.com/ghilmanITM360/youtube-intelligence-os/pull/49 (base `main`, not merged; review needed).
Validation: `tests/test_dataset_ledger_provenance.py` 11 passed; CSV/JSON load checks OK; secret scan of committed sources: no tokens.

## NOT on GitHub
- Stash untracked half (1,729 files, 757 MB): local refs only (two zips exceed 100 MB).
- Raw MP4s (4.2 GB) and preserved evidence: git-ignored by repo policy.
- `~/YIOS-local-audits` unique content (12.6 GB).
- Pre-existing uncommitted changes in the active worktree (not part of this work).

## LFS
Registry DB payload fetched from the GitHub LFS server and hash-matched (39e7a28b…). Other LFS objects: not checked.
