# Branch Inventory

Measured 2026-11-17 after a non-destructive `git fetch origin --tags` (no prune). Baseline: `origin/main` @ `e96f7f8f` (2026-11-17, 208 commits).
Repository: `origin` = `github.com/ghilmanITM360/youtube-intelligence-os` (single remote, no submodules, not shallow, 421 commits reachable from the current HEAD).

**Coverage: 75 distinct branch names** (37 local, 67 on origin). 21 are fully contained in `origin/main`. Every branch below has a section in `INDIVIDUAL_BRANCH_AUDIT.md`.

Columns: **Loc** L=local, R=origin. **vs main** = commits ahead/behind `origin/main`. **Files** = files changed since merge-base. **CI** = latest GitHub Actions run on that branch name. Ahead/behind uses the origin ref when it exists, else the local ref.

Other refs: tag `audit-backup/pre-sync-2026-11-11`; `stash@{0}` (on research/senior-health-complete-local-sync, mirrored by the two `preservation/*` branches); 10 linked worktrees (see BRANCH_COMPARISON.md); 45 PRs (23 open, 1 closed, 21 merged). CI workflow: `.github/workflows/validate.yml` (PR + push to main).

| # | Branch | Loc | Group | Tip | Date | vs main | Files | Merged | PR | CI | Nearest parent branch | Recommendation |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| 1 | `main` | LR | Baseline | `e96f7f8f` | 2026-11-17 | +0/-0 | 0 | yes |  | success (2026-11-17) |  | Fast-forward local main (`git pull --ff-only`). |
| 2 | `cleanup/yios-phase2-batch1` | R | Casually Finance lineage | `34a79e46` | 2026-11-10 | +243/-6 | 6947 | no |  | no run | research/casually-finance-consolidated (+1) | Integrate: rebase docs onto main, keep evidence on pinned branch. |
| 3 | `codex/casually-finance-forensic-research` | LR | Casually Finance lineage | `043b85bf` | 2026-10-13 | +54/-6 | 2257 | no | #21 OPEN | no run |  | Close #21 in favour of consolidated branch. |
| 4 | `codex/casually-finance-knowledge-navigation` | R | Casually Finance lineage | `f4dc5d14` | 2026-10-28 | +1/-6 | 5 | no |  | no run |  | Delete after consolidated lands. |
| 5 | `research/casual-finance-inventory-scoped` | R | Casually Finance lineage | `4e7c4260` | 2026-11-06 | +1/-6 | 10 | no | #47 OPEN | success (2026-11-06) |  | Close #47 and #37 together. |
| 6 | `research/casually-finance-consolidated` | R | Casually Finance lineage | `9a4023af` | 2026-11-09 | +242/-6 | 6736 | no |  | no run | research/casually-finance-video-inventory (+156) | Keep as pinned evidence branch. |
| 7 | `research/casually-finance-success-playbook` | LR | Casually Finance lineage | `fb1e56d0` | 2026-10-13 | +57/-6 | 2420 | no | #28 OPEN | no run |  | Close #28 into consolidated. |
| 8 | `research/casually-finance-video-inventory` | LR | Casually Finance lineage | `1adfdeb9` | 2026-10-19 | +86/-6 | 880 | no | #37 OPEN | failure (2026-10-19) |  | Close #37 (superseded by #47 + consolidated). |
| 9 | `data/ds-000011-supplement-2026-11-11` | LR | Data | `97eef476` | 2026-11-11 | +1/-3 | 7 | no |  | no run |  | Register via ledger, then merge. |
| 10 | `recovery/local-research-reconciliation-2026-10-12` | LR | Docs | `0fdf5a2d` | 2026-10-12 | +2/-6 | 20 | no | #22 OPEN | no run |  | Merge #22 (docs only). |
| 11 | `data/finance-economics-complete-2026-11-11` | R | Finance | `3a3f1aee` | 2026-11-16 | +91/-3 | 1219 | no |  | no run |  | Decide DB policy; open a PR. |
| 12 | `candidate/finance-integration-2026-11-02` | L | Finance lineage | `f115285b` | 2026-11-02 | +209/-6 | 2249 | no |  | no run | codex/finance-machine-a-owner-directed (+15) | Delete after #36/#45 land (fully contained). |
| 13 | `claude/finance-audits-machine-b-0044ae` | L | Finance lineage | `223f4498` | 2026-10-30 | +150/-6 | 1401 | no |  | no run |  | Delete after #36/#45 land. |
| 14 | `codex/finance-machine-a-owner-directed` | R | Finance lineage | `9c6f42fb` | 2026-11-02 | +194/-6 | 1798 | no |  | no run | claude/finance-audits-machine-b-0044ae (+44) | Delete after #36/#45 land. |
| 15 | `fix/finance-audit-validators` | R | Finance lineage | `5d487623` | 2026-11-06 | +215/-6 | 2257 | no | #45 OPEN | success (2026-11-06) | candidate/finance-integration-2026-11-02 (+6) | Highest-value merge: land after #36 or retarget. |
| 16 | `repair/second-machine-post-audit-2026-11-02` | L | Finance lineage | `cd2160f9` | 2026-11-02 | +151/-6 | 1405 | no |  | no run | claude/finance-audits-machine-b-0044ae (+1) | Delete after #36/#45 land. |
| 17 | `research/finance-economics-intelligence` | LR | Finance lineage | `2b6ccea5` | 2026-11-11 | +210/-3 | 2249 | no | #36 OPEN | failure (2026-11-11) | candidate/finance-integration-2026-11-02 (+4) | Fix DB allowlist (take #45 approach), then merge #36. |
| 18 | `research/senior-health-reports-2026-11-11` | LR | Finance lineage | `27987f2b` | 2026-11-11 | +215/-3 | 2306 | no |  | no run | research/finance-economics-intelligence (+5) | Drop 90f9cd22; split Senior Health commits onto main. |
| 19 | `chore/full-local-data-sync-and-senior-health-acquisition` | LR | Merged | `f3c56353` | 2026-09-25 | +0/-79 | 0 | yes | #4 MERGED #1 MERGED | no run |  | Delete (fully in main). |
| 20 | `claude/second-machine-audit-repair-ef17c5` | L | Merged | `08e71926` | 2026-10-11 | +0/-6 | 0 | yes |  | no run |  | Delete. |
| 21 | `claude/statins-senior-health-db38aa` | L | Merged | `fd029485` | 2026-11-10 | +0/-3 | 0 | yes |  | no run |  | Delete worktree + branch. |
| 22 | `codex/remaining-work-audit-2026-10-11` | R | Merged | `6338efe2` | 2026-10-11 | +0/-7 | 0 | yes | #18 MERGED | no run |  | Delete. |
| 23 | `codex/transcript-pending-registration` | R | Merged | `ec171641` | 2026-10-11 | +0/-17 | 0 | yes | #17 MERGED | no run |  | Delete. |
| 24 | `codex/what-if-normalized-staging` | LR | Merged | `fe284619` | 2026-10-09 | +0/-37 | 0 | yes | #10 MERGED | no run |  | Delete. |
| 25 | `codex/what-if-promotion` | LR | Merged | `aff815ef` | 2026-10-09 | +0/-34 | 0 | yes | #11 MERGED | no run |  | Delete. |
| 26 | `codex/what-if-readonly-adapter` | LR | Merged | `58c7a12b` | 2026-10-09 | +0/-39 | 0 | yes | #9 MERGED | no run |  | Delete. |
| 27 | `codex/what-if-source-contract` | LR | Merged | `be4969c7` | 2026-10-09 | +0/-41 | 0 | yes | #8 MERGED | no run |  | Delete. |
| 28 | `docs/yios-consolidation-index` | R | Merged | `efd3dc0a` | 2026-11-10 | +0/-4 | 0 | yes | #48 MERGED | success (2026-11-09) |  | Delete. |
| 29 | `feat/ai-slop-gate` | LR | Merged | `5b481bc9` | 2026-11-17 | +0/-1 | 0 | yes | #51 MERGED | success (2026-11-17) |  | Delete. |
| 30 | `integration/packaging-forensics-validated-subset-2026-10-11` | R | Merged | `ce82c0a8` | 2026-10-11 | +0/-19 | 0 | yes | #19 MERGED | no run |  | Delete. |
| 31 | `integration/repository-consolidation-2026-09-25` | R | Merged | `73816f1e` | 2026-09-26 | +0/-65 | 0 | yes | #5 MERGED | no run |  | Delete. |
| 32 | `integration/repository-superset-2026-09-23` | R | Merged | `0930dfe3` | 2026-09-23 | +0/-98 | 0 | yes |  | no run |  | Delete. |
| 33 | `integration/yios-current-canonical-2026-10-03` | R | Merged | `c1c3bb88` | 2026-10-04 | +0/-43 | 0 | yes | #7 MERGED | no run |  | Delete. |
| 34 | `research/senior-health-acquisition-phase-2` | R | Merged | `373bf37e` | 2026-09-29 | +0/-53 | 0 | yes |  | no run |  | Delete. |
| 35 | `research/senior-health-complete-local-sync` | LR | Merged | `0cbabf50` | 2026-10-02 | +0/-77 | 0 | yes | #3 MERGED | no run |  | Delete (stash@{0} was made on it). |
| 36 | `research/senior-health-data-expansion-2026-09-28` | LR | Merged | `814a0279` | 2026-09-28 | +0/-58 | 0 | yes | #6 MERGED | no run |  | Delete. |
| 37 | `research/senior-health-forensic-v2` | R | Merged | `206d67bc` | 2026-09-25 | +0/-81 | 0 | yes | #2 MERGED | no run |  | Delete. |
| 38 | `research/senior-health-metadata` | L | Merged | `fd029485` | 2026-11-10 | +0/-3 | 0 | yes |  | no run |  | Commit the untracked worktree files to a branch. |
| 39 | `codex/casual-economics-forensic-research` | LR | Metadata/forensics | `fce81670` | 2026-10-14 | +20/-6 | 477 | no | #25 OPEN | success (2026-10-14) |  | Review code diff separately, then merge (#25). |
| 40 | `research/barely-evolved-metadata` | LR | Metadata/forensics | `c4212c90` | 2026-10-20 | +1/-6 | 24 | no | #43 OPEN | failure (2026-10-20) |  | Re-run CI, merge #43. |
| 41 | `research/monkey-explains-1999-metadata` | LR | Metadata/forensics | `f176aa28` | 2026-10-20 | +1/-6 | 18 | no | #38 OPEN | failure (2026-10-20) |  | Re-run CI, merge #38. |
| 42 | `research/youtube-12-channel-metadata` | LR | Metadata/forensics | `967ea707` | 2026-10-20 | +2/-6 | 262 | no | #39 OPEN | failure (2026-10-20) |  | Re-run CI, merge #39. |
| 43 | `codex/packaging-rollup-repair-2026-10-11` | R | Packaging | `9ce62de2` | 2026-10-11 | +50/-42 | 295 | no |  | no run |  | Delete after descendant decision. |
| 44 | `planning/deferred-legacy-thumbnail-research` | LR | Packaging | `9e7be191` | 2026-10-12 | +1/-6 | 1 | no | #24 OPEN | no run |  | Merge #24 (docs only). |
| 45 | `research/thumbnail-forensics-complete-2026-10-04` | LR | Packaging | `6c6e8900` | 2026-10-11 | +71/-42 | 304 | no |  | no run | codex/packaging-rollup-repair-2026-10-11 (+21) | Open PR after stash decision. |
| 46 | `preservation/stash0-tracked-delta-2026-11-11` | L | Preservation | `ac51465b` | 2026-10-13 | +3/-77 | 1 | no |  | no run | preservation/stash0-untracked-LOCAL-ONLY-2026-11-11 (+133) | Keep until owner reviews; then drop with stash. |
| 47 | `preservation/stash0-untracked-LOCAL-ONLY-2026-11-11` | L | Preservation | `2d0e6e97` | 2026-10-13 | +1/-208 | 7309 | no |  | no run |  | Owner decision: back up off-device before anything else. |
| 48 | `dr-rehan-test-videos` | R | Production | `8daa1c83` | 2026-10-13 | +1/-6 | 62 | no | #26 OPEN | no run |  | Owner decision: keep as production archive or move to media store (#26). |
| 49 | `production/dr-rehan-diabetes-heart-warning-assets` | R | Production | `c867af8e` | 2026-10-15 | +12/-6 | 473 | no | #32 OPEN | success (2026-10-15) |  | Archive as production record; merge only manifests. |
| 50 | `production/finance-short-01-keyframe` | LR | Production | `315e76d5` | 2026-10-13 | +11/-6 | 598 | no | #29 CLOSED | success (2026-10-13) |  | Keep branch; reopen when audio arrives. |
| 51 | `production/finance-short-02-assets` | R | Production | `30e0ef2f` | 2026-10-14 | +14/-6 | 504 | no | #30 OPEN | success (2026-10-14) |  | Archive as production record. |
| 52 | `production/senior-health-casually-finance-three-videos` | R | Production | `65caa889` | 2026-10-16 | +15/-6 | 1030 | no | #34 OPEN | success (2026-10-15) |  | Archive as production record. |
| 53 | `claude/dr-rehan-seniors-health-data-5db7ab` | LR | Senior Health | `05456d7a` | 2026-11-16 | +3/-3 | 53 | no |  | no run |  | Review raw files, then merge via PR. |
| 54 | `data/exercise-apify-2026-11-14` | R | Senior Health | `23e6864d` | 2026-11-16 | +64/-3 | 174 | no |  | no run | research/senior-health-apify-2026-11-11 (+1) | Decide DB policy (LFS/allowlist or external), then merge with #50. |
| 55 | `docs/dr-rehan-recording-pack-2026-11-17` | R | Senior Health | `8aac2523` | 2026-11-17 | +1/-3 | 11 | no |  | no run |  | Run slop gate, open PR. |
| 56 | `research/senior-health-apify-2026-11-11` | R | Senior Health | `9b23e061` | 2026-11-16 | +63/-3 | 163 | no | #50 OPEN | failure (2026-11-15) |  | Decide DB policy; merge with exercise branch. |
| 57 | `consolidation/selected-folders-2026-11-11` | LR | Senior Health/docs | `89e3aa6d` | 2026-11-11 | +2/-3 | 148 | no | #49 OPEN | success (2026-11-11) |  | Merge #49. |
| 58 | `backup/decode-15cbe9f-original` | R | Stale | `15cbe9f0` | 2026-09-28 | +1/-59 | 13 | no |  | no run |  | Archive (keep ref, do not merge). |
| 59 | `fix/repository-health-remediation-2026-09-21` | R | Stale | `11ad082b` | 2026-09-21 | +4/-125 | 38 | no |  | no run |  | Archive. |
| 60 | `ui/v1` | LR | Stale | `0412932a` | 2026-09-11 | +1/-149 | 2 | no |  | no run |  | Archive; it is the prior UI plan this audit supersedes. |
| 61 | `yios-test/34df1220de934163b910f7d4c737bcf1/checkpoint` | R | Test refs | `43aff9d3` | 2026-10-30 | n/a (orphan) | 5603 | no |  | no run |  | Delete after owner confirmation. |
| 62 | `yios-test/34df1220de934163b910f7d4c737bcf1/claims/finance/TEST0000001` | R | Test refs | `5ef9694a` | 2026-10-30 | n/a (orphan) | 5602 | no |  | no run |  | Delete after owner confirmation. |
| 63 | `yios-test/34df1220de934163b910f7d4c737bcf1/claims/finance/TEST0000002` | R | Test refs | `abb9a7b4` | 2026-10-30 | n/a (orphan) | 5602 | no |  | no run |  | Delete after owner confirmation. |
| 64 | `codex/register-verified-transcript-pending-what-if` | R | Tooling | `e9b56960` | 2026-10-11 | +1/-6 | 17 | no | #20 OPEN | no run |  | Re-apply on current main via script, then close #20. |
| 65 | `codex/yios-dual-machine-coordination` | LR | Tooling | `205fc7eb` | 2026-10-30 | +151/-6 | 1417 | no |  | no run | claude/finance-audits-machine-b-0044ae (+1) | Extract the tooling commit onto main if two-Mac work continues; otherwise archive. |
| 66 | `feat/registry-reviewed-workbooks` | R | Tooling | `264e9ebf` | 2026-11-06 | +2/-6 | 13 | no | #46 OPEN | success (2026-11-06) |  | Fix the recorded validator failure, then merge #46. |
| 67 | `feat/slop-gate-alerts` | LR | Tooling | `58f9b62c` | 2026-11-17 | +1/-0 | 5 | no | #52 OPEN | success (2026-11-17) |  | Merge #52. |
| 68 | `research/local-channel-media-library` | LR | Tooling | `78e8fd2d` | 2026-10-21 | +5/-6 | 19 | no | #41 OPEN | failure (2026-10-21) |  | Re-run CI, merge #41. Needed by any UI that shows media. |
| 69 | `claude/determined-darwin-v0gl6n` | R | Visual forensics | `e0e2cbcc` | 2026-11-02 | +1/-6 | 5 | no |  | no run |  | Delete after Barely Evolved branch lands. |
| 70 | `codex/what-if-archive-main-integration` | R | Visual forensics | `f345abde` | 2026-10-28 | +7/-6 | 405 | no | #44 OPEN | failure (2026-10-28) |  | Pick one master plan; merge #44 after re-running CI. |
| 71 | `research/barely-evolved-visual-forensics` | R | Visual forensics | `3e587c75` | 2026-11-06 | +48/-6 | 1000 | no |  | no run | claude/determined-darwin-v0gl6n (+47) | Open PR or keep as pinned evidence branch. |
| 72 | `research/casually-finance-editing-forensics` | R | Visual forensics | `05e8635b` | 2026-11-15 | +94/-6 | 3073 | no |  | no run |  | Keep as evidence branch; merge after CF consolidation. |
| 73 | `research/primitive-education-visual-forensics` | R | Visual forensics | `ff2ff896` | 2026-11-06 | +15/-6 | 842 | no |  | no run |  | Keep as evidence branch. |
| 74 | `research/what-if-brain-preservation-batch1` | R | Visual forensics | `abdcf8e0` | 2026-10-25 | +139/-6 | 1736 | no |  | no run |  | Reconcile with #44; merge one. |
| 75 | `research/xkcd-whatif-visual-forensics` | R | Visual forensics | `3c6145cc` | 2026-11-06 | +19/-6 | 1600 | no |  | no run |  | Keep as pinned evidence branch. |

## Counts by group

| Group | Branches |
|---|---:|
| Baseline | 1 |
| Casually Finance lineage | 7 |
| Data | 1 |
| Docs | 1 |
| Finance | 1 |
| Finance lineage | 7 |
| Merged | 20 |
| Metadata/forensics | 4 |
| Packaging | 3 |
| Preservation | 2 |
| Production | 5 |
| Senior Health | 4 |
| Senior Health/docs | 1 |
| Stale | 3 |
| Test refs | 3 |
| Tooling | 5 |
| Visual forensics | 7 |

## Limitations

- Author is `ghilmankhan` on every tip except `claude/determined-darwin-v0gl6n` (`Claude`); authorship does not distinguish human from agent commits.
- CI "failure" with no failed step (barely-evolved, monkey-explains, youtube-12, local-media-library, casually-finance-video-inventory, what-if-archive) means the job failed before any step ran. Cause not verified (runner, quota or LFS are candidates).
- Per-branch test suites were **not** executed locally; build status comes only from CI.
- Ahead counts on stacked branches overlap heavily; use "Nearest parent" and BRANCH_COMPARISON.md for exclusive work.
