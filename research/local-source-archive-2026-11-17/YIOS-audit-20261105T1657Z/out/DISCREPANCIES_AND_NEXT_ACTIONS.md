# YIOS discrepancies and ranked next actions

## Corrections to this audit's own earlier statements
| Earlier statement | Correct position | Evidence |
|---|---|---|
| Video006 U and V are local only | V is on remote; U commit is local only (unreachable in canonical, plus same-Mac recovery bundle), with all 28 file versions on remote | `raw/u_v/`, canonical reflog |
| V follows U | U and V are siblings on T | `git log` |
| T is latest | Latest at pin is W4 `5e497970` | `raw/recon/ls_remote_final2.txt` |
| No writer lock at 18:47Z | zsh glob artifact; `.vf_writer_lock` existed | `after/locks.txt` |
| Mirror pinned to 19:08Z ls-remote | Mirror refs matched clone start, about 18:33Z. Later recheck fetches moved 4 mirror heads as a side effect of `+refs/*:refs/*` | `raw/refs/mirror_refs.txt`, `raw/remote/mirror_refs_after_recheck_fetch.txt` |
| Local tests fail on all refs | Harness artifact; all pass with Git access | `raw/tests/full_with_git/` |
| "Usage WAIT 11" | Logged 1, separately inferred 10 | `out/PRIMITIVE_EDUCATION_SCHEDULER_RUNS.csv` |

## Discrepancies in project records
1. **Barely Evolved `STATUS.json` is stale.** Says `ONBOARDING_BLOCKED_NO_MEDIA_NO_NETWORK` while N18 and the progress matrix show 3 videos partial.
2. **Video006 `QUALITY_GATE.json` at W4** still says events V25 and next EP0014, while the queue is at v5 and SUB010 is next.
3. **`CLAUDE.md` writer rule vs handback.** See `AUTOMATION_AND_OWNERSHIP.md`.
4. **Text-only contract vs 4 JPGs** in Video006 Git paths.
5. **LFS:** fetch log says 39 objects; pointer walk and payload files both say 38; unexplained, harmless so far.
6. **Registry vs research:** Casual Finance 0 videos, xkcd What If 83 vs census 91; Primitive Education and Barely Evolved absent.
7. **Local Finance ref** `research/finance-economics-intelligence` is `1adb8129`, far behind remote `f115285b`. It is stale, not ahead.
8. **Channel name:** "Casually Finance" in your briefs, "Casual Finance" in registry and paths, for the same channel ID `UCrNfRFWnLC3tCy1TnyhVQ7g`. Casual Economics is a different stream.

## Concurrent external changes (actor UNKNOWN unless a record is cited; none by this audit)
| Time UTC | Change | Source |
|---|---|---|
| 2026-11-05 17:08:40 | Video006 lock release, label codex-v006 | lock log |
| 18:34:30 to 18:35 | Barely Evolved N17 push, lock release | BE log |
| 18:41:01 / 18:45:54 | Primitive Education lock events | PE log |
| 18:41:02 to 20:03 | Video006 lock sequence, label codex | lock log |
| 18:42:14 | Video006 V pushed; tracking ref moved "update by push" | canonical reflog |
| 19:15:58 | xkcd What If checkpoint P, lock release | progress log |
| 19:59 to 20:00 | Video006 `9d81f94d` push after V | reflog |
| 21:13 to 22:48 | Video006 scheduled lock; W1 | lock log, reflog |
| 22:07:36 | Primitive Education lock by session 85559743 | PE log |
| 2026-11-06 00:27 to 02:52 | Video006 W2, W3 | reflog, lock log |
| 03:11 to 03:15 | Video006 W4 | reflog, lock log |
| 03:18:50 | Video006 Codex lock | lock log |
| 03:26 to 03:31 | Barely Evolved N18, release | BE log |
| 03:27:41 | xkcd What If lock | lock receipt |
| 03:31 | `publication-audit-20261106` folder created by another worker; PE `HOLD_NO_EXECUTABLE_WORK` | mtimes |
| throughout | `refs/codex/turn-diffs/*` churn; origin tracking refs move "update by push" | `after/refs_diff.txt` |

## Ranked next actions

| # | Action | Who | Dependency | Why first |
|---|---|---|---|---|
| 1 | Name an off-device destination, then copy and hash-verify local-only work: Video006 workspaces, other deep-ct-scan folders, `yio-cf-editing-forensics-local-evidence`, media | Owner | None for naming; wait for worker locks before copying moving folders | 17.14 GB exists on one Mac only, as far as provable |
| 2 | Find and supply the 5,767 list | Owner | Whoever produced that number; check Machine B | Forensic comparison is BLOCKED without it |
| 3 | On Machine B, verify the 420 hashes not here or on remote, starting with `Archive.zip` 394.9 MB and `local_branches.bundle` 65 MB | Machine B session | Owner | Could be single-copy data |
| 4 | Decide `reference_knowledge.db` policy, then 1-line allowlist change | Owner, then Finance writer | Writer confirmation | Unblocks PR #36 hosted check |
| 5 | Decide fate of Video006 JPGs and add final-tree media rejection | Owner, current Video006 worker | Lock owner | Prevents more media in Git |
| 6 | Include U recovery bundle in the off-device copy (action 1). Add a local ref for U only if owner wants it | Owner | Worker not writing | Canonical copy of U is unreachable and can eventually be pruned; bundle is same-Mac only |
| 7 | Rerun logs for PRs #37-44 | Owner | Hosted minutes and billing state | Causes unknown |
| 8 | Strengthen C4, C5, C6, C7 validators | Finance writer | PR #36 writer | Gates pass on garbage |
| 9 | Prove the Primitive Education scheduler with one test when work exists | Owner | Remove HOLD deliberately | Scheduler never proved |
| 10 | Provide listening capability | Owner | Decision | Every channel's audio gate is BLOCKED |
| 11 | Confirm writer rule in `CLAUDE.md` | Owner | None | Current text conflicts with practice |
| 12 | Add visual-forensics channels to the registry | Metadata writer | Owner | Retrieval by DB fails for them |

## Resume-ready, with dependency
| Stream | Ready for | Needs |
|---|---|---|
| Casually Finance — Video006 | SUB010 onward | Current Codex lock released; never take over |
| xkcd What If | Current worker's follow-up | Its lock released; Phase 7 scope from owner |
| Barely Evolved | No lock held; open UBC items | Owner decision on scope; refresh `STATUS.json` |
| Primitive Education | Publish J by its worker | Then waits for audio or owner decisions |
| Finance | `15Gr4BAJi00`, `1CJTuLaenq8`, `1D9nBNa6jNE` | Writer confirmation; Machine B state; PR #36 not merged |
| Thumbnail research | Not ready | Owner decision; Machine B `Archive.zip` |
