# Branch → main audit (2026-11-17)

This audit was read-only. Nothing was merged, pushed or deleted. The baseline is `origin/main` at `e96f7f8f` (PR #51 merged), after `git fetch --all --prune`.

Method: ahead/behind counts via `git rev-list`; patch-equivalence via `git cherry`; containment via `merge-base --is-ancestor` across every local and `origin/*` tip; conflicts via `git merge-tree --write-tree`, run against main alone and as one cumulative merge of every leaf, smallest first. That cumulative merge was simulated in object storage only.

## Headline

- **85 refs** (local and remote). **55 distinct tips** have work that is not in main.
- **16 tips** are contained in another branch, so merging the containing branch covers them.
- That leaves **39 leaf branches** to merge or decide on: 3 are orphan test refs and 1 is already merged (`feat/ai-slop-gate`), so **35 are real**.
- In the cumulative simulation, **26 leaves merge cleanly**. **9 conflict**: 3 are stale branches that main has superseded, and 6 have small conflicts, mostly in `AGENTS.md`, `README.md` and `.gitignore`.
- **One piece of work existed only on this Mac**: `preservation/stash0-untracked-LOCAL-ONLY-2026-11-11`, with 2,267 files and about 843 MB, mostly under `docs/research/thumbnail-forensics-2026-10-02/public-current/*/thumbnail-snapshots/`.
  - **Update 2026-11-17:** it is now pushed as `preservation/stash0-pushable-2026-11-11` (`53bdb562`). That commit has the stash's tree and first two parents; its third parent is `c93c8d2c`, the untracked files without `Archive.zip`.
  - `Archive.zip` (394.9 MB, sha256 `0d82557b16e1f3a1d6162dcba13b4375a9ae615f1aa744a93d0f3675a853a76d`) is over GitHub's 100 MB limit, and it is redundant. Its 2,240 non-junk entries are byte-identical to files in the commit, its 17 root files are byte-identical in the stash's tracked tree, and its other 2,943 entries are `__MACOSX` or `.DS_Store`.
  - The original local commits (`2d0e6e97`, `ac51465b`) and `refs/preservation/stash0-2026-11-11` are unchanged.
- Untracked, uncommitted work:
  - `research/what-if-scripts/` (126 files, 1 MB) in the main checkout
  - `research/senior-health-metadata/` (35 files, 10 MB) in the `~/Documents/yios-senior-health` worktree
- The current branch's 1 unpushed commit (`90f9cd22`, the gate) is an **older version** of what PR #51 merged. It should not be pushed. Take main's version when merging.
- PR #52 (`feat/slop-gate-alerts`) is open and MERGEABLE. It was created after the fetch, so it is not counted above.

## A. Leaf branches: clean merges (26)

"Exclusive" means commits that are in no other leaf.

| Branch | Ahead | Exclusive | PR |
|---|---:|---:|---|
| origin/data/finance-economics-complete-2026-11-11 | 91 | 91 | — (`.gitignore` conflict in the cumulative run only, see C) |
| origin/data/exercise-apify-2026-11-14 | 64 | 64 | — (contains `research/senior-health-apify-2026-11-11`, #50) |
| origin/research/barely-evolved-visual-forensics | 48 | 48 | — |
| codex/casual-economics-forensic-research | 20 | 20 | #25 |
| origin/research/xkcd-whatif-visual-forensics | 19 | 19 | — |
| origin/research/primitive-education-visual-forensics | 15 | 15 | — |
| origin/production/senior-health-casually-finance-three-videos | 15 | 15 | #34 draft |
| origin/production/finance-short-02-assets | 14 | 14 | #30 draft |
| origin/production/dr-rehan-diabetes-heart-warning-assets | 12 | 12 | #32 draft |
| production/finance-short-01-keyframe | 11 | 11 | (#29 per memory) |
| origin/research/casually-finance-editing-forensics | 94 | 9 | — |
| origin/codex/what-if-archive-main-integration | 7 | 7 | #44 draft |
| research/local-channel-media-library | 5 | 5 | #41 draft |
| claude/dr-rehan-seniors-health-data-5db7ab | 3 | 3 | — |
| preservation/stash0-tracked-delta-2026-11-11 (local only, = stash@{0}) | 3 | 3 | — |
| origin/feat/registry-reviewed-workbooks | 2 | 2 | #46 draft |
| research/youtube-12-channel-metadata | 2 | 2 | #39 draft |
| recovery/local-research-reconciliation-2026-10-12 | 2 | 2 | #22 |
| consolidation/selected-folders-2026-11-11 | 2 | 2 | #49 |
| origin/dr-rehan-test-videos | 1 | 1 | #26 draft |
| origin/docs/dr-rehan-recording-pack-2026-11-17 | 1 | 1 | — |
| origin/codex/register-verified-transcript-pending-what-if | 1 | 1 | #20 |
| research/monkey-explains-1999-metadata | 1 | 1 | #38 draft |
| research/barely-evolved-metadata | 1 | 1 | #43 draft |
| planning/deferred-legacy-thumbnail-research | 1 | 1 | #24 draft |
| data/ds-000011-supplement-2026-11-11 | 1 | 1 | — |

## B. Large overlapping lineages (they share most of their commits)

| Leaf | Ahead | Exclusive | Contains | Conflict vs main |
|---|---:|---:|---|---|
| research/senior-health-reports-2026-11-11 (current) | 216 | 7 | `research/finance-economics-intelligence` (#36), `candidate/finance-integration`, `repair/second-machine-post-audit`, `codex/finance-machine-a-owner-directed` | `AGENTS.md`, `docs/policies/AI-SLOP-RISK-RULES.md`, `scripts/check_slop_risk.py`, `tests/test_check_slop_risk.py`. Main has the newer gate; keep main's gate files and keep the branch's "Reference knowledge framework" section in `AGENTS.md`. |
| origin/fix/finance-audit-validators (#45 draft) | 215 | 6 | — | `AGENTS.md` |
| origin/cleanup/yios-phase2-batch1 | 243 | 73 | `research/casually-finance-consolidated`, which contains the Casually Finance branches (#21, #28, #37, #47) | `README.md`, `docs/START_HERE.md`, `research/casually-finance/README.md`, `research/consolidation/README.md`, `research/consolidation/tools/build_phase2_batch1.py` |
| codex/yios-dual-machine-coordination | 151 | 1 | `claude/finance-audits-machine-b-0044ae` | `AGENTS.md` |
| origin/research/what-if-brain-preservation-batch1 | 139 | 5 | — | clean vs main; conflicts with the lineage above on `docs/AI_SESSION_CONTEXT.md` and `docs/YIOS_MASTER_PLAN.md` |
| research/thumbnail-forensics-complete-2026-10-04 | 71 | 71 | `codex/packaging-rollup-repair-2026-10-11` | clean vs main; conflicts with `preservation/stash0-tracked-delta` on `completion-ledger.csv` |

## C. Conflicts: stale branches that main has superseded (recommend archiving, not merging)

| Branch | Date | Behind | Evidence of supersession |
|---|---|---:|---|
| ui/v1 | 2026-09-11 | 149 | Main reworked both files in `4335eff5` "preserve remediation and UI handoff history" |
| origin/backup/decode-15cbe9f-original | 2026-09-28 | 59 | Named as a backup; main updated the same Decode files on 2026-10-04 |
| origin/fix/repository-health-remediation-2026-09-21 | 2026-09-21 | 125 | Main ported it (`811ad211` "port … from fix branch", `73816f1e` remediation results) |

Supersession is inferred from commit history, not from a line-by-line diff. Confirm before archiving.

## D. Orphan test refs (unrelated history; do not merge)

`origin/yios-test/34df1220…/checkpoint`, `…/claims/finance/TEST0000001`, `…/claims/finance/TEST0000002`. These are test claims from dual-machine coordination, with no shared history with main.

## E. Already fully in main (0 commits ahead; safe to delete after confirmation)

- Local: `chore/full-local-data-sync-and-senior-health-acquisition`, `claude/second-machine-audit-repair-ef17c5`, `claude/statins-senior-health-db38aa`, `codex/what-if-{normalized-staging,promotion,readonly-adapter,source-contract}`, `research/senior-health-complete-local-sync`, `research/senior-health-data-expansion-2026-09-28`, `research/senior-health-metadata`, `feat/ai-slop-gate`
- Remote: the same names plus `codex/remaining-work-audit-2026-10-11`, `codex/transcript-pending-registration`, `docs/yios-consolidation-index`, `integration/{packaging-forensics-validated-subset-2026-10-11,repository-consolidation-2026-09-25,repository-superset-2026-09-23,yios-current-canonical-2026-10-03}`, `research/senior-health-acquisition-phase-2`, `research/senior-health-forensic-v2`

## F. Proposed merge order (needs owner approval)

1. **Local-only first:** decide on the 843 MB preservation commit. Either push it (LFS-tracked) or record it as intentionally local. Commit or park the two untracked folders.
2. **Wave 1:** the 26 clean leaves in section A, one PR each (or one integration branch), smallest first.
3. **Wave 2:** `research/senior-health-reports-2026-11-11`, which brings the whole finance lineage. Resolve the gate conflict in main's favour and keep the reference-framework section.
4. **Wave 3:** `fix/finance-audit-validators` → `codex/yios-dual-machine-coordination` → `what-if-brain-preservation-batch1` → `cleanup/yios-phase2-batch1` → `thumbnail-forensics-complete`. Each has 1–5 small doc conflicts.
5. **Cleanup:** archive section C, delete section D, delete section E, close the PRs the merges make redundant.

Rules that still apply: AGENTS.md rule 4 (never modify raw evidence) and rule 9 (detect duplication). Several branches carry overlapping data snapshots, so run the repository validators after each wave.
