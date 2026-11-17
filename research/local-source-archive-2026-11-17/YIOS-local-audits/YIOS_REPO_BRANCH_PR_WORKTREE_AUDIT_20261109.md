# YIOS repo / branch / PR / worktree / local-disk audit (2026-11-09)

Status: READ-ONLY survey. Nothing was committed, pushed, merged, closed, deleted or moved. Only `git fetch origin --prune` ran (remote-tracking refs only).
Method: `git for-each-ref`, `git rev-list`, `git diff --name-only origin/main...<branch>`, `git branch -r --contains`, `git worktree list`, `gh pr list`, `du`, `ls`. All counts are MEASURED from refs at the time of the run. Containment is commit ancestry, NOT content comparison.

Anchors: repo `ghilmanITM360/youtube-intelligence-os` (PRIVATE); `origin/main` = `08e719264e31ecd82de24f8eeb8f065c08359fe5` (2026-10-11, merge of PR #18). Checked-out HEAD = `research/casually-finance-consolidated` @ `9a4023af358ad15eec24a11cc5c2818a9d0994c6` (clean, 0 unpushed commits).

## 1. Totals

| Item | Count |
|---|---|
| Local branches | 33 |
| Remote branches (origin) | 54 incl. `origin/main` (3 are `yios-test/...` refs) |
| Tags | 0 |
| Worktrees | 3 (main checkout + `yios-audit-fixes` + `yios-finance-machine-a`) |
| Stashes | 1 (`checkpoint doc wip`, on `chore/full-local-data-sync-and-senior-health-acquisition`) |
| PRs total | 40 listed (#1-#47, gaps are not PRs): 19 MERGED (#1-#19), 1 CLOSED (#29), 20 OPEN |
| `.git` size | 5.9 GB (1 garbage pack, 21 KB, harmless) |

## 2. Core purpose of the project (from README / AGENTS.md / PROJECT_STATUS.md)

YouTube Intelligence OS = an evidence-based intelligence system for multiple YouTube channels. `main` holds the code, schema, validators, manifests and documentation layer. V1 (Topic, Packaging, Hook/Script, Editing/Visual where forensics exist, Channel Strategy) is declared complete on `main`. Raw media and most heavy evidence are NOT in `main`; they live on the owner's Mac (`data/raw/` is gitignored; allowlisted exceptions only). Everything after 2026-10-11 (Casual Finance, xkcd, Barely Evolved, Primitive Education, Finance+Economics, production assets) lives on research/production branches that were never merged into `main`.

`main` structure (tracked files): `data/` ~2,640 (catalog DBs, manifests, normalized, raw allowlists) · `docs/` 458 · `scripts/` 67 · `tests/` 49 · `exports/` 16 · `schemas/` 11 · `.codex/` 12 · root docs (README, PROJECT_STATUS, AGENTS, PRODUCTION_PIPELINE).

## 3. Branch map by purpose

Legend: ahead = unique commits vs `main`; files = files changed vs `main`. "In" = another branch already contains this tip.

### A. Fully merged into main already (0 unique commits) , clutter, 15 remote branches
`codex/remaining-work-audit-2026-10-11` (PR #18) · `codex/transcript-pending-registration` (#17) · `integration/packaging-forensics-validated-subset-2026-10-11` (#19) · `codex/what-if-promotion` (#11) · `codex/what-if-normalized-staging` (#10) · `codex/what-if-readonly-adapter` (#9) · `codex/what-if-source-contract` (#8) · `integration/yios-current-canonical-2026-10-03` (#7) · `research/senior-health-complete-local-sync` (#3) · `research/senior-health-acquisition-phase-2` · `research/senior-health-data-expansion-2026-09-28` (#6) · `integration/repository-consolidation-2026-09-25` (#5) · `chore/full-local-data-sync-and-senior-health-acquisition` (#1/#4) · `research/senior-health-forensic-v2` (#2) · `integration/repository-superset-2026-09-23`.
Local twins also exist for most of these, plus `codex/ds-000027-dr-ares` (= main).
Effect: deleting them would lose no commits. NOT done; needs owner authorization.

### B. Casual Finance (CF) , owner priority
| Branch | PR | ahead / files | Notes |
|---|---|---|---|
| `research/casually-finance-consolidated` | none yet | 242 / 6,736 | Hub branch (6 CF branches merged + INDEX, 199 ASR transcripts, ASR note). Pushed 9a4023af. Local has no upstream set. Includes 31 mp4 already on origin. |
| `codex/casually-finance-forensic-research` | #21 open ready | 54 / 2,257 | Corpus + production DNA. In consolidated. |
| `research/casually-finance-success-playbook` | #28 draft (stacked on #21) | 57 / 2,420 | Playbook + pilot render. In consolidated. |
| `research/casually-finance-video-inventory` | #37 open ready (CI failing) | 86 / 880 | Mostly finance-economics files. In consolidated. |
| `research/casual-finance-inventory-scoped` | #47 draft | 1 / 10 | Scoped twin of #37. In consolidated. |
| `research/casually-finance-editing-forensics` | none | 85 / 3,017 | Visual CT forensics, 15/15 milestone at 2697d3c6. In consolidated. LOCAL copy is stale (2b10f104, behind origin by 24). |
| `codex/casually-finance-knowledge-navigation` | none | 1 / 5 | Navigation doc. In consolidated. |
| `production/finance-short-01-keyframe` | #29 CLOSED | 11 / 598 | Production assets. NOT in consolidated. |
| `production/finance-short-02-assets` | #30 draft | 14 / 504 | Production assets. NOT in consolidated. |
| `production/senior-health-casually-finance-three-videos` | #34 draft | 15 / 1,030 | Senior-health + CF review package. NOT in consolidated. |
| `research/local-channel-media-library` | #41 draft | 5 / 19 | Checksummed local media registry. NOT in consolidated. |

### C. Finance + Economics (13 channels, 966 / 1,612 videos) , separate line
| Branch | PR | ahead / files | Notes |
|---|---|---|---|
| `fix/finance-audit-validators` | #45 draft (shows 21 files, so its base is probably not `main`; not verified) | 215 / 2,257 | Superset of the two below. Worktree `yios-audit-fixes`. |
| `research/finance-economics-intelligence` | #36 draft (stale body) | 209 / 2,249 | In `fix/finance-audit-validators`. LOCAL copy is 75 behind origin. |
| `codex/finance-machine-a-owner-directed` | none | 194 / 1,798 | In both branches above. Worktree `yios-finance-machine-a`. |
| `codex/yios-dual-machine-coordination` | none | 151 / 1,417 | In NO other branch. Looks like an older finance line (content overlap not verified). |
| `feat/registry-reviewed-workbooks` | #46 draft | 2 / 13 | Registry importer workbooks. |

### D. Other channels, visual forensics (local-first campaigns)
| Branch | PR | ahead / files |
|---|---|---|
| `research/xkcd-whatif-visual-forensics` | none | 19 / 1,600 |
| `research/barely-evolved-visual-forensics` | none | 48 / 1,000 (contains `claude/determined-darwin-v0gl6n`) |
| `research/primitive-education-visual-forensics` | none | 15 / 842 |
| `research/barely-evolved-metadata` | #43 draft | 1 / 24 |
| `research/monkey-explains-1999-metadata` | #38 draft | 1 / 18 |
| `research/youtube-12-channel-metadata` | #39 draft | 2 / 262 |

### E. Casual Economics (excluded from CF milestones)
`codex/casual-economics-forensic-research` , PR #25 open ready , 20 / 477 , in no other branch.

### F. What If (xkcd) integration line
`codex/what-if-archive-main-integration` (#44 draft, 7 / 405) · `research/what-if-brain-preservation-batch1` (no PR, 139 / 1,736, mixed: 1,066 finance files + 545 visual-forensics + 82 production-experiments) · `codex/register-verified-transcript-pending-what-if` (#20 open, 1 / 17).

### G. Thumbnail / packaging research
`research/thumbnail-forensics-complete-2026-10-04` (no PR, 71 / 304; local is behind 36) · `codex/packaging-rollup-repair-2026-10-11` (50 / 295; contained in the thumbnail branch) · `planning/deferred-legacy-thumbnail-research` (#24 draft, 1 / 1) · `recovery/local-research-reconciliation-2026-10-12` (#22, 2 / 20).

### H. Production assets (video-making, not research)
`production/dr-rehan-diabetes-heart-warning-assets` (#32 draft, 12 / 473) · `dr-rehan-test-videos` (#26 draft, 1 / 62) · plus the three finance/senior-health ones in section B.

### I. Old / test / other
`ui/v1` (1 / 2 docs) · `fix/repository-health-remediation-2026-09-21` (4 / 38, no PR) · 3 `yios-test/...` refs (TEST claims/checkpoint, 2-5 commits each, 202 behind main) · local-only `backup/decode-15cbe9f-original` (1 commit, no upstream, content NOT inspected).

## 4. Worktrees and local state
| Path | Branch | State |
|---|---|---|
| `~/workprojects/youtube-intelligence-os` (8.1 GB) | `research/casually-finance-consolidated` | clean, 0 unpushed, 35 ignored items (venv, caches, `data/raw/first-party`, `data/staging`, `output*`) |
| `~/workprojects/yios-audit-fixes` (1.6 GB) | `fix/finance-audit-validators` | clean, in sync with origin |
| `~/workprojects/yios-finance-machine-a` (1.4 GB) | `codex/finance-machine-a-owner-directed` | clean, in sync with origin |

No worktree holds unpushed commits. One stash exists and must be preserved.

## 5. Local-only data (not in git; single Mac)
| Location | Size | What |
|---|---|---|
| `~/YIOS-local-audits/` | 12 GB | 63 entries: 24 `deep-ct-scan` video workspaces, 15 other dated folders, 5 CF Video006 folders; campaign folders `xkcd-whatif` 4.6 GB, `barely-evolved` 2.0 GB, `primitive-education` 0.6 GB, `CASUALLY_FINANCE_35_VIDEO_TARGET_20261104` 0.7 GB, `CF_TRANSCRIPTS_ASR_20261109`, `tooling` 0.4 GB, `uncommitted-backup-20261108` 0.2 GB; handoff/prompt .md files; `vf_lock.sh`. |
| `~/Downloads/videos in mp3/` | 4.1 GB | Source media: CasuallyFinance 216 mp4 (1.5 GB), casual_economics 11, MonkeBiznis 63, xkcd 88, PrimateEconomics 29, BarelyEvolved 3, PrimitiveEducation 44, plus the Visual Forensics Kit. |
| `~/workprojects/yio-cf-editing-forensics-local-evidence` | 4.2 GB | Per-video CF evidence folders (not a git checkout; relation to branch contents NOT verified). |
| `~/workprojects/video data of what if` | 0.7 GB | What If forensic outputs / production brain. |
| `~/workprojects/dr rehan video` | 1.5 GB | Dr Rehan video kit. |
| `~/workprojects/yios-recovery-status` | 72 MB | 2026-10-12 recovery/inventory JSON. |

Unrelated to YIOS (not touched): `NooriAquaa` (+worktrees), `dotfumes-*`, `ijtema-*`, `offline-map`, `speedupServices-` (+worktrees), `wedding-invitations-2026`, `ui-maps-design ideas` (~10 GB combined).

## 6. Why it feels confusing (measured causes)
1. 33 local + 54 remote branches; 15 of the remote ones are already fully in `main`.
2. Nesting: 4 CF PRs (#21, #28, #37, #47) overlap; #36 is inside #45; machine-a is inside both. The same files show up in several PRs.
3. Only `main` is canonical; all post-10-11 work is on unmerged branches, so no single branch shows the whole project.
4. Stale local copies: `research/casually-finance-editing-forensics` (-24), `research/finance-economics-intelligence` (-75), `research/thumbnail-forensics-complete-2026-10-04` (-36).
5. 8 research branches have NO PR at all (CF editing-forensics, xkcd, barely-evolved, primitive-education, what-if-brain-preservation, thumbnail-forensics, dual-machine-coordination, machine-a).
6. Heavy evidence is local-only and single-copy (about 21 GB across audits, media and evidence folders).

## 7. NOT verified (do not assume)
- Content-level overlap between branches (only ancestry was checked).
- PR base branches (#45's 21-file count suggests a non-main base).
- Whether the 24 `deep-ct-scan` folders and the evidence folder are fully published in any branch.
- Contents of `backup/decode-15cbe9f-original`, the stash, `codex/yios-dual-machine-coordination`.
- CI status per PR beyond #37 and #36 (known failing `validate`).
- Audio: still `ASR_UNCERTIFIED`; nothing here is a CT_SCAN or AV sign-off.

## 8. Decisions left to the owner (nothing started)
1. Delete or keep the 15 fully-merged remote branches (and local twins).
2. CF: open a PR for the consolidated branch (scoped vs full) and what to do with #21 / #28 / #37 / #47 (retarget #28 first).
3. CF: pull the 3 production branches and #41 into the hub, or only index them.
4. Finance: how #36 / #45 / machine-a / dual-machine-coordination relate; refresh stale PR #36 body.
5. Open a PR (or not) for the 8 PR-less research branches.
6. Off-device backup of the ~21 GB local-only evidence.
7. Fast-forward the stale local branches (safe, local-only) , needs a go-ahead.
