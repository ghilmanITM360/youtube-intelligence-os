# YIOS consolidation audit (Phase 1, audit only)

- Date: 2026-11-09 (measured about 23:40 local, UTC+5). Auditor: Claude (Sonnet 5.5) in the YIOS Code session.
- Scope: GitHub repo `ghilmanITM360/youtube-intelligence-os` (private), the three local checkouts, `~/YIOS-local-audits/`, `~/Downloads/videos in mp3/`, and the YIOS folders under `~/workprojects/`.
- Rules kept: read-only. Nothing was merged, pushed, closed, renamed, moved, deleted, installed or applied. All DBs opened with `mode=ro`. One scratchpad folder was used for temporary lists; it is outside the project.
- Status words: `YES` / `NO` = verified in the stated scope. `NOT CHECKED` / `BLOCKED` = not verified, reason given. Labels: MEASURED (a command output), CITED (taken from a repo file without re-counting), INFERRED.
- Prior audit `YIOS_REPO_BRANCH_PR_WORKTREE_AUDIT_20261109.md` was used as a lead. Three of its statements are corrected here (section 9).

## 0. The ten findings that matter

1. **`main` is old.** `origin/main` = `08e719264e31ecd82de24f8eeb8f065c08359fe5` (2026-10-11, merge of PR #18). Every workstream after 10-11 lives on unmerged branches. (MEASURED, `git rev-parse`)
2. **Refs:** 87 branch refs in this clone (33 local + 54 remote-tracking, incl. `origin/main` and 3 `yios-test/*`) plus the `origin/HEAD` pointer; 54 heads on the remote (`git ls-remote --heads origin`), 3 worktrees, 1 stash, 0 tags. `.git` is 5.9 GB (4.1 GB is `.git/lfs`).
3. **PRs:** 40 listed (#1-#47; the gaps are not PRs): 19 MERGED (#1-#19), 1 CLOSED (#29), 20 OPEN. 7 open PRs have a FAILURE check on their current head SHA (#36, #37, #38, #39, #41, #43, #44). (MEASURED, `gh pr list`)
4. **The consolidated Casual Finance branch already exists on the remote.** `origin/research/casually-finance-consolidated` = `9a4023af358ad15eec24a11cc5c2818a9d0994c6` = local HEAD, and **no PR points at it.** All 7 CF text branches have identical file content inside it (blob check, section 2.3). The 4 CF production/media branches do not.
5. **Finance #36 and #45 are a stack, not two copies.** #45's base is `research/finance-economics-intelligence` (the #36 head), so the earlier "base probably not main" doubt is resolved. #45 contains #36 and Machine A. Only `codex/yios-dual-machine-coordination` (151 commits) carries work that is in no other branch.
6. **Registry:** 75 channels (46 with videos, 29 identity-only), 2,303 videos, 2,303 transcript rows, of which 2,291 are real text and 12 are placeholders. Integrity check `ok`, 0 orphans, 0 duplicate IDs. Snapshot date 2026-09-28. The same bytes (SHA-256 `39e7a28b...`) sit in 4 places.
7. **The registry does not hold Casual Finance videos (0 of 206) and holds 83 of the 91 xkcd videos.** Casual Finance (206) and most expansion channels live only on branches. The Finance universe (1,612) = 966 originals (all in the registry) + 646 expansion (not in the registry).
8. **Local MP4s: 454 files, 4.36 GB (4.06 GiB), 453 distinct SHA-256.** One exact duplicate (a Casual Finance file). Casual Finance 216 files = 206 catalog IDs + 10 extra files. One folder, `MonkeBiznis-MP4` (63 files), matches **no** channel in the registry or the Finance universe, so its channel is unresolved.
9. **Visual closure (visual-only contract; audio and AV are BLOCKED, never signed off):** Casual Finance 19 / 20 verified by the local counter. xkcd 29 closed (20 Shorts + 9 long-forms) in the local ledger. Full AV sign-off: 0 for every channel. The xkcd ledger changed today after the older notes ("0 longs"). I read it as it is now.
10. **About 25.5 GB exists on this one Mac with no verified off-device copy.** No Machine B or off-device backup destination was reachable from here, so those items are BLOCKED. Phase 2 needs an owner decision on a backup destination first.

---

## 1. Current system map

### 1.1 What YIOS does (CITED from `AGENTS.md`, `README.md`, `PROJECT_STATUS.md`, read earlier in this session)
YIOS is an evidence-first research system for YouTube channels. Core rules: the repo and its documented evidence are the source of truth; raw evidence is never modified; facts, observations and AI interpretations stay separate; no YouTube API in the competitor workflow; V1 (topic, packaging, hook/script, editing-visual, orchestrator, channel strategy) is declared complete; V2 work (UI, RAG, agents, API, automation) does not start on its own. The website (Phase 3) is not started.

### 1.2 Workstreams and where each lives

| Workstream | Goal (owner's words, condensed) | Git (branch / PR) | Local only | Authoritative source today |
|---|---|---|---|---|
| **What If** | Original science channel informed by xkcd's What If? | `research/xkcd-whatif-visual-forensics` (19 commits ahead of main, no PR); `research/what-if-brain-preservation-batch1` (139 commits, no PR); #44 `codex/what-if-archive-main-integration`; #20 | `~/YIOS-local-audits/xkcd-whatif` 7.3 GB; `~/workprojects/video data of what if` 0.7 GB; `~/Downloads/videos in mp3/xkcd Channel` 88 MP4 | Local ledger `xkcd-whatif/asset_library/_channel/ct_closure/CLOSURE_LEDGER_v1.csv`; census `xkcd-whatif/census/census.csv` |
| **Finance / economics, reference = Casual Finance** | Two new channels, niches chosen from evidence | `research/casually-finance-consolidated` (CF hub); #36 / #45 / Machine A (Finance 1,612 universe); #46 registry workbooks | `~/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104`, `CF_TRANSCRIPTS_ASR_20261109`, `~/workprojects/yio-cf-editing-forensics-local-evidence` 4.2 GB | CF: `research/casually-finance/INDEX.csv` on the consolidated branch. Finance: `research/finance-economics-intelligence/FINANCE_CONTINUATION_QUEUE.csv` on #45 |
| **Local MP4 visual analysis** | Inventory all source MP4s; CF and xkcd first | Visual text records on `research/*-visual-forensics` branches | 454 MP4, 7 folders | Section 3 below |
| **Senior Health** | Lowest priority; third-party research for an independent channel; Dr Rehan material to leave the active project in Phase 2 | Merged into main (#1-#6) plus production #34 | none verified | Registry + `docs/research/senior-health-*` on main |
| **Other channels (extra)** | Not in the owner's goal list, but present | Barely Evolved branch (48 commits), Primitive Education branch (15), Casual Economics #25, metadata PRs #38/#39/#43 | `~/YIOS-local-audits/barely-evolved` 2.0 GB, `primitive-education` 0.6 GB | Branch text + local workspaces |

### 1.3 Authoritative sources (what to trust when two things disagree)
- Code, schemas, validators, manifests: `origin/main`, then the branch that changed them (#45 is the newest validator code).
- Channel registry: `data/catalog/youtube_channel_registry.db` (Git LFS). It is a **frozen snapshot of 2026-09-28**, not a live view.
- Casual Finance: the consolidated branch (INDEX.csv); not the registry.
- Finance universe: the continuation queue on #45.
- Visual closure and AV status: local ledgers only. Nothing proves publication of closure beyond the CF 15-milestone commit (`2697d3c6`).
- Chat summaries, claude-mem and memory files are leads only (AGENTS.md rule).

---

## 2. Git, GitHub and branch evidence

### 2.1 Totals (MEASURED)
| Item | Value |
|---|---|
| `origin/main` / `main` | `08e719264e31ecd82de24f8eeb8f065c08359fe5` |
| Current HEAD | `research/casually-finance-consolidated` `9a4023af358ad15eec24a11cc5c2818a9d0994c6`, working tree clean, 242 commits ahead of main, 0 behind |
| Remote heads | 54 (`git ls-remote --heads origin`) |
| Local + remote-tracking branch refs in this clone | 87 (33 local, 54 remote-tracking) plus the `origin/HEAD` pointer |
| Worktrees | 3 (see 2.5), all clean |
| Stash | 1 (`stash@{0}`) |
| Tags | 0 |

### 2.2 PR table (state at audit time; CI = checks on the PR's current head SHA)
| PR | State | Base | Head (short) | Files | CI | Note |
|---|---|---|---|---|---|---|
| #1-#19 | MERGED | main | various | 2-2,114 | SUCCESS | merged history; their branch tips mostly still exist |
| #20 | OPEN | main | `e9b56960` | 17 | SUCCESS | What If transcript-pending registration |
| #21 | OPEN | main | `043b85bf` | 2,257 | SUCCESS | CF forensic corpus |
| #22 | OPEN | main | `0fdf5a2d` | 20 | SUCCESS | recovered research |
| #24 | OPEN draft | main | `9e7be191` | 1 | SUCCESS | plan doc |
| #25 | OPEN | main | `fce81670` | 477 | SUCCESS | Casual Economics (excluded) |
| #26 | OPEN draft | main | `8daa1c83` | 62 | SUCCESS | Dr Rehan test videos |
| #28 | OPEN draft | **`codex/casually-finance-forensic-research`** (#21 branch) | `fb1e56d0` | 163 | SUCCESS | stacked on #21 |
| #29 | CLOSED draft | main | `315e76d5` | 598 | SUCCESS | Finance Short 01 keyframes |
| #30 | OPEN draft | main | `30e0ef2f` | 504 | SUCCESS | Finance Short 02 assets |
| #32 | OPEN draft | main | `c867af8e` | 473 | SUCCESS | Dr Rehan production |
| #34 | OPEN draft | main | `65caa889` | 1,030 | SUCCESS | Senior Health three videos |
| #36 | OPEN draft | main | `f115285b` | 2,249 | **FAILURE** | Finance 966 audit (PR body stale) |
| #37 | OPEN | main | `1adfdeb9` | 880 | **FAILURE** | CF video inventory |
| #38 | OPEN draft | main | `f176aa28` | 18 | **FAILURE** | MonkeyExplains1999 metadata |
| #39 | OPEN draft | main | `967ea707` | 262 | **FAILURE** | 12-channel metadata |
| #41 | OPEN draft | main | `78e8fd2d` | 19 | **FAILURE** | local channel media library |
| #43 | OPEN draft | main | `c4212c90` | 24 | **FAILURE** | BarelyEvolved metadata |
| #44 | OPEN draft | main | `f345abde` | 405 | **FAILURE** | What If archive integration |
| #45 | OPEN draft | **`research/finance-economics-intelligence`** (#36 head) | `5d487623` | 21 | SUCCESS | validators + Finance stack tip |
| #46 | OPEN draft | main | `264e9ebf` | 13 | SUCCESS | registry reviewed workbooks |
| #47 | OPEN draft | main | `4e7c4260` | 10 | SUCCESS | CF inventory, scoped alternative |

Why the failures happened was NOT investigated here. `FINANCE_PROGRESS_CHECKPOINT.json` (CITED) records a `CI_BLOCKED_BILLING` note on a #36 run, so some failures may be billing, not code. Treat that as unverified.

### 2.3 Content overlap, by file blob (MEASURED)
Method: for each branch, `git diff --raw --no-abbrev` against its merge-base with main, then compare each changed file's blob ID with the same path in the target tree. Ancestry alone is not used.

**Casual Finance, target = `origin/research/casually-finance-consolidated`**
| Branch | Files changed vs main | Identical in consolidated | Differs | Absent |
|---|---|---|---|---|
| #21 `codex/casually-finance-forensic-research` | 2,257 | 2,257 | 0 | 0 |
| #28 `research/casually-finance-success-playbook` | 2,420 | 2,412 | **8** | 0 |
| #37 `research/casually-finance-video-inventory` | 880 | 880 | 0 | 0 |
| #47 `research/casual-finance-inventory-scoped` | 10 | 10 | 0 | 0 |
| `origin/research/casually-finance-editing-forensics` (tip `2697d3c6`) | 3,017 | 3,017 | 0 | 0 |
| `origin/codex/casually-finance-knowledge-navigation` | 5 | 5 | 0 | 0 |
| `production/finance-short-01-keyframe` | 598 | 0 | 0 | 598 |
| `production/finance-short-02-assets` | 504 | 0 | 0 | 504 |
| `production/senior-health-casually-finance-three-videos` | 1,030 | 0 | 0 | 1,030 |
| `research/local-channel-media-library` (#41) | 19 | 0 | 3 | 16 |
| `codex/casual-economics-forensic-research` (#25) | 477 | 0 | 4 | 473 |

The 8 files that differ for #28 are all under `data/extracted/forensic-analysis/casually-finance/2026-10-12/` (SCRIPT_DNA, blueprint, deep report, finalization census, QA register, validation, claim verification, new-Mac handoff). Which version is newer was **not** decided here. This must be settled before #28 is retired.

**Finance, target = `origin/fix/finance-audit-validators` (#45 tip)**
| Branch | Files changed | Identical in #45 | Differs | Absent |
|---|---|---|---|---|
| `origin/research/finance-economics-intelligence` (#36) | 2,249 | 2,236 | 13 | 0 |
| `origin/codex/finance-machine-a-owner-directed` | 1,798 | 1,775 | 23 | 0 |
| `origin/codex/yios-dual-machine-coordination` | 1,417 | 1,380 | 22 | **15** |
| `origin/feat/registry-reviewed-workbooks` (#46) | 13 | 0 | 1 | 12 |

Unique to dual-machine (absent from #45): `bin/yios`, `scripts/yios.py`, `scripts/yios_coordination.py`, `scripts/yios_integration.py`, `scripts/yios_remote_smoke.py`, `scripts/yios_workspace.py`, three `tests/test_yios_*.py`, `docs/YIOS_TWO_MAC_WORKFLOW.md`, `docs/superpowers/plans/2026-10-30-dual-machine-coordination.md`, `docs/intelligence/YIOS_CASUALLY_FINANCE_COLD_START_2026-10-30.md`, `research/coordination/CHANNELS.md` and two validation JSONs. 22 more differ (e.g. `AGENTS.md`, `.gitattributes`, Finance CSVs). #45 vs #36 differs by 21 files: CI workflow, reference-comparison code, tests, frozen-registry test, identity contract, visual crosswalk CSV, `AGENTS.md`.

Finance branch content also overlaps Casual Finance: **848 files are byte-identical between #45 and the consolidated branch** (shared CF data on two lines of work).

**Containment by commit ancestry (MEASURED, `git branch -r --contains`)**
- Machine A (`9c6f42fb`) is contained in #36 and #45. #36 is contained in #45. `claude/determined-darwin-v0gl6n` (1 commit) is contained in the Barely Evolved branch. The consolidated tip is contained only in itself.
- 15 remote branches have 0 unique commits and are fully reachable from main (see 4.2 group A).

### 2.4 Ahead / behind (vs `origin/main`, MEASURED)
Heads, ahead and behind for all 87 branch refs were measured. For the two stale local branches below, `merge-base --is-ancestor` confirms the local tip is an ancestor of its remote tip (behind 24 and 75, ahead 0), so a fast-forward would lose nothing. Items that matter:

| Ref | Head | Ahead | Behind | Remote relation |
|---|---|---|---|---|
| `research/casually-finance-consolidated` | `9a4023af` | 242 | 0 | same as remote |
| `research/casually-finance-editing-forensics` (local) | `2b10f104` | 61 | 0 | **remote is `2697d3c6` (85 ahead): local is 24 commits stale** |
| `research/finance-economics-intelligence` (local) | `1adb8129` | 134 | 0 | **remote is `f115285b` (209 ahead): local is 75 commits stale** |
| `research/thumbnail-forensics-complete-2026-10-04` | `6c6e8900` | 71 | 36 | local = remote; no PR |
| `fix/finance-audit-validators` | `5d487623` | 215 | 0 | same as remote |
| `codex/finance-machine-a-owner-directed` | `9c6f42fb` | 194 | 0 | same as remote; no PR |
| `codex/yios-dual-machine-coordination` (remote only) | `205fc7eb` | 151 | 0 | no PR |
| `research/xkcd-whatif-visual-forensics` (remote only) | `3c6145cc` | 19 | 0 | no PR |
| `research/barely-evolved-visual-forensics` (remote only) | `3e587c75` | 48 | 0 | no PR |
| `research/primitive-education-visual-forensics` (remote only) | `ff2ff896` | 15 | 0 | no PR |
| `research/what-if-brain-preservation-batch1` | `abdcf8e0` | 139 | 0 | no PR; 1,736 files vs main |
| `backup/decode-15cbe9f-original` (local only) | `15cbe9f0` | 1 | 53 | no remote copy |

### 2.5 Worktrees, stash, backup ref, claims
| Item | Path / ref | Head | State |
|---|---|---|---|
| Main checkout | `~/workprojects/youtube-intelligence-os` | `9a4023af` | clean |
| Worktree | `~/workprojects/yios-audit-fixes` | `5d487623` on `fix/finance-audit-validators` | clean (0 changes), 1.6 GB |
| Worktree | `~/workprojects/yios-finance-machine-a` | `9c6f42fb` on `codex/finance-machine-a-owner-directed` | clean, 1.4 GB |
| Stash | `stash@{0}` `5b6c3042679400b16aa1024b79058b71dade0ab9` | 2026-09-24, "checkpoint doc wip" | 1 file, 1 line changed (`docs/audits/SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md`); plus an untracked-files commit; **inspected, not applied** |
| Backup ref | `backup/decode-15cbe9f-original` `15cbe9f0112596c1e07c1c1504302cce77bfd97a` | 2026-09-28 | 1 commit, 13 files, 30,005 insertions; Decode Your Heart (Dr Rehan) recovery; **local only** |

Claims and locks (MEASURED): `vf_lock.sh status` returns `FREE` for the xkcd lock dir and for the global lock. `git ls-remote` shows only branch heads, `HEAD` and 60 `refs/pull/*` refs (no tags, no other namespaces). The three `yios-test/34df.../*` branches look like test claims (names `claims/finance/TEST000000x`, `checkpoint`) and are 202 commits behind main. I found **no** live claim on the remote. Remote refs cannot show unpushed work on another machine (see Machine B in 3.4). The owner decision of 2026-11-06 (CLAUDE.md) removed the sole-writer rules, so no exclusive claim is assumed.

### 2.6 Media inside Git (MEASURED)
| Scope | Media files | Size |
|---|---|---|
| `origin/main` tree | 7 (`.m4a` / `.wav` under `data/raw/forensic-analysis/DS-000013..16`) | 78.1 MB, derived audio |
| Consolidated tree | 38 (the 7 above + 16 LFS pointers `casually-finance/source-videos/*.mp4` of about 132 bytes each + 15 pilot render/audio files under `research/casually-finance-success-playbook/`) | 133 MB measured (pointer sizes, not video bytes) |
| `production/finance-short-01-keyframe` | 9 | 85.5 MB |
| `production/finance-short-02-assets` | 16 | 141.5 MB |
| `production/senior-health-casually-finance-three-videos` | 25 | 115.2 MB |
| `production/dr-rehan-diabetes-heart-warning-assets` | 10 | 89.4 MB |
| `dr-rehan-test-videos` | 12 | 78.1 MB |
| History, all local refs | 51 distinct media blobs | 177 MB (`rev-list --objects --all`) |

- The 16 Casual Finance source MP4s are tracked as **Git LFS pointers**. Whether the LFS objects exist on GitHub's LFS store was NOT CHECKED. The policy says never to transport raw video through GitHub; this is an owner decision (section 6).
- The production branches hold generated renders and audio, not source video, but 100 MB-class files in git remain a size risk.

---

## 3. Local disk, media and databases

### 3.1 Local survey
| Path | Size | Content | Git status | Backup |
|---|---|---|---|---|
| `~/workprojects/youtube-intelligence-os` | `.git` 5.9 GB (4.1 GB LFS) + tree | main checkout | tracked | remote = GitHub |
| `~/workprojects/yios-audit-fixes` | 1.6 GB | worktree | tracked | remote = GitHub |
| `~/workprojects/yios-finance-machine-a` | 1.4 GB | worktree | tracked | remote = GitHub |
| `~/YIOS-local-audits/` | **15 GB** | forensic workspaces, handoffs, tooling, 24 `*-deep-ct-scan` folders | not in git (outside repo) | none verified |
| `  xkcd-whatif` | 7.3 GB | census, 44-video library, 29 closures | local only | none verified |
| `  barely-evolved` | 2.0 GB | BE workspaces | local only | none verified |
| `  primitive-education` | 0.6 GB | PE census, source_media | local only | none verified |
| `  CASUALLY_FINANCE_35_VIDEO_TARGET_20261104` | 0.7 GB | CF visual-complete ledger, counter | local only | none verified |
| `  tooling` | 0.4 GB | scripts incl. venv | local only | none |
| `~/Downloads/videos in mp3/` | 4.1 GB | 454 source MP4 (+ the Kit folder, 34 non-video files) | local only | none verified |
| `~/workprojects/yio-cf-editing-forensics-local-evidence` | 4.2 GB | 38 CF video folders | local only | none verified |
| `~/workprojects/video data of what if` | 0.7 GB | What If production brain, releases | local only | none verified |
| `~/workprojects/dr rehan video` | 1.5 GB | Dr Rehan kit, `input` 358 MB, `work` 1.0 GB, `CLAUDE.md`, `.venv` | not verified | none verified |
| `~/workprojects/yios-recovery-status` | 72 MB | recovery JSON from 2026-10-12 | local only | none |
| Reference book | `~/Downloads/HumanCraft_Video_Studio_V2_Complete_Guide.pdf` | 181,440 bytes, 35 pages, SHA-256 `1b1564cfd5fe144a...` | not in git (0 `humancraft` paths on main) | none |

Total local-only data with no verified off-device copy: about **25.5 GB** (15 + 4.1 + 4.2 + 0.7 + 1.5 + 0.07). Non-YIOS projects under `~/workprojects` (NooriAquaa, dotfumes, ijtema, offline-map, speedupServices, wedding-invitations, ui-maps) were not touched or measured here.

Reference book: the file above is the only match for "HumanCraft" found within 4 levels under `~`. I confirmed name, size, page count and SHA prefix only. I did **not** read it, and I did not check that it is the book the owner means. (The 20-file reference corpus inside `reference_knowledge.db` is a different set: algorithm guides and analyzer prompts, not HumanCraft.)

### 3.2 MP4 inventory (MEASURED: SHA-256 of all 454 files; full list kept in the audit scratchpad `mp4_hashes.csv`, not saved as a second deliverable)
| Folder | Files | IDs in file name | Distinct SHA | In registry videos | Maps to |
|---|---|---|---|---|---|
| `CasuallyFinance` | 216 | 162 | 215 | 0 | Casual Finance (206 catalog IDs, see 3.3) |
| `xkcd Channel` | 88 | 88 | 88 | 83 | xkcd's What If? |
| `MonkeBiznis-MP4` | 63 | 63 | 63 | 0 | **unresolved** (not in registry; its 63 IDs do not match the 63 `MonkeyExplains` IDs in the Finance queue) |
| `PrimitiveEducation-MP4` | 44 | 44 | 44 | 0 | Primitive Education (12 of the 44 IDs are in the Finance queue) |
| `PrimateEconomics-MP4` | 29 | 29 | 29 | 28 | Primate Economics (all 29 in Finance queue) |
| `casual_economics` | 11 | 0 | 11 | 0 | Casual Economics (no IDs in names; excluded) |
| `BarelyEvolved-MP4` | 3 | 3 | 3 | 0 | Barely Evolved |
| **Total** | **454** | | **453 distinct** | | |

Duplicates: exactly one SHA-256 group (2 files): Casual Finance "Why Japan's Economy Is Awful ... (720p, h264).mp4" and its "(1).mp4" copy. No SHA is shared across folders. No ID appears twice across folders.

### 3.3 Casual Finance file vs ID reconciliation (from `CF_TRANSCRIPTS_ASR_20261109/manifest.csv`, CITED, plus the hash run above)
- 216 files. 206 catalog IDs are covered. 3 catalog IDs have two files each (different SHA, so alternate encodes): `2EZzwupIa80`, `PxgCsLSf-w4`, `rSa2aziEsAI`. 7 files do not map to a catalog ID: 5 truncated "SnapYT" names with no match, the ID `9eBM5IF_bco` (not in the catalog), and the exact-copy "(1)" file. 216 = 206 + 3 + 7.
- Probe result: 209 of 216 files pass the duration check (|delta| <= 3 s); 7 have no catalog duration (`NA`); 216 of 216 have an audio stream.
- Not re-verified today: the 7 hand-mapped names (`OVERRIDE` table in `build_manifest.py`). They rest on title words plus duration within 1 s.

### 3.4 Machine B / office computer (BLOCKED)
No authorized connection exists from this Mac: `~/.ssh` has no `config`, and `known_hosts` lists only `github.com`. Nothing on that machine could be inspected. Checks that need it, exactly:
1. `git status`, `git stash list`, `git branch -vv` in its YIOS checkout; compare any unpushed commits with the 87 branch refs here.
2. `ls` + `shasum -a 256` of its media folders; compare with section 3.2.
3. The state of its `vf_lock.sh` / claim directories and any running Claude/Codex sessions.
4. Any DB copy (`youtube_channel_registry.db`, `youtube_inventory.db`, `reference_knowledge.db`) and its SHA-256 against section 3.5.
5. The off-device backup candidate (is there a drive or cloud folder it can reach?).

### 3.5 Databases (MEASURED, all opened read-only)

| DB | Role | Bytes | SHA-256 (first 16) | Integrity | Locations |
|---|---|---|---|---|---|
| `data/catalog/youtube_channel_registry.db` | **canonical registry** (Git LFS) | 141,373,440 | `39e7a28ba592b902` | ok, FK check 0 | main checkout, `yios-audit-fixes`, `yios-finance-machine-a`, plus the frozen baseline `research/finance-economics-intelligence/audit-baseline/youtube_channel_registry.frozen.db` (identical bytes, 4 copies) |
| `data/catalog/youtube_inventory.db` | **historical catalog, input to the registry** | 52,391,936 | `277c09f64bc71678` | ok | same 3 checkouts, identical |
| `data/knowledge/reference_knowledge.db` | derived reference KB (separate file by design) | 5,062,656 | `a161871add6a7e1e` | ok | `yios-audit-fixes` only (not in the main checkout) |

**Registry (`youtube_channel_registry.db`)**
- Metadata: `generated_at` 2026-09-28T13:21:20Z; `source_payload_sha256` `b8f72bfee5d3c8edc206dd4a28d4f31470b9f24a1305044548a1dc78ebd90296`; `historical_catalog_sha256` `277c09f64bc7...` (matches the inventory DB hash above, so the registry was built from that exact inventory file).
- 20 base tables + 6 FTS shadow tables + 10 views. Rows: channels 75, videos 2,303, transcripts 2,303, dataset_videos 2,303, datasets 33, artifacts 318, subtitle_tracks 2,455, channel_data_layers 825, intelligence_coverage 600, submissions 67, availability_gaps 216, visual_coverage 75, identity_evidence 75, channel_aliases 142, `transcript_fts` 2,291.
- Keys: `channels.canonical_channel_id` (YouTube `UC...` ID) -> `videos.canonical_channel_id`; `videos.youtube_video_id` -> `transcripts.youtube_video_id`; `dataset_videos(dataset_id, youtube_video_id)`; `visual_coverage` per channel.
- Checks: orphan videos 0; orphan transcripts 0; videos without a transcript row 0; duplicate video IDs 0; transcript placeholders 12 (`is_placeholder=1`, word_count 0; Lucas Grant 10, Matty Invests 1, Doctor Thomas 1); videos missing views 10 (all Lucas Grant); missing description 17; `video_type` is inconsistent (`Short` 14, `shorts` 90, `regular video` 890, `video` 1,150, NULL 159) — a data-quality defect for any Short/long split.
- Channels: `target_group` ORIGINAL_TARGET 44, ADDED_TARGET 19, OUTSIDE_TARGET 12. Status: COMPLETE 32, COMPLETE_WITH_LIMITATIONS 14, IDENTITY_VERIFIED_DATA_NOT_EXTRACTED 29.
- Visual coverage: `FORENSIC_VIDEO_EVIDENCE` 1 channel (xkcd: 3 registered source videos, 107 keyframes), `THUMBNAIL_EVIDENCE` 2, `THUMBNAIL_URL_ONLY` 41, `NONE` 31. The registry **does not know** about the 29 xkcd closures, the 19 CF closures or the 454 local MP4s.
- Casual Finance (`UCrNfRFWnLC3tCy1TnyhVQ7g`) is `IDENTITY_VERIFIED_DATA_NOT_EXTRACTED`, ADDED_TARGET, 0 videos. Barely Evolved, Primitive Education and MonkeyExplains/Monke are **not** channels in the registry.

**Inventory DB:** 27 tables; `discovered_files` 45,774, `source_files` 6,953, `visual_assets` 5,172, `field_provenance` 12,335, `videos` 667, `channels` 10, `transcripts` 668, `datasets` 26, `ingestion_runs` 37. It is the evidence ledger of files and runs that the registry was built from.

**Reference KB:** 20 source files (the owner's algorithm/hook/analyzer guides), 1,260 sections (1,029 text extracted, 230 with unread images, 1 sparse), 33 rules, 63 constituent videos, 722 video assessments. Built by `research/finance-economics-intelligence/reference-framework/build_reference_kb.py`; the README (CITED) says it can be rebuilt with `--fresh` to a new path.

**Rebuild map (INFERRED from script source; no rebuild was run):**
| DB | Rebuildable? | Inputs |
|---|---|---|
| Registry | YES, by `scripts/build_youtube_channel_registry.py` | `data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json`, `data/manifests/YOUTUBE_CHANNEL_IDENTITY_EVIDENCE.json`, `docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv`, `youtube_inventory.db`, `data/extracted/channel-data/*/combined/*_master.csv`, `data/raw/competitors/*/dataset.json`, intelligence JSON per channel |
| Inventory DB | PARTLY, by `scripts/rebuild_inventory_catalog.py` / `inventory_catalog.py` from `data/raw` (gitignored; heavy evidence is on disk, so a clean clone cannot rebuild it) | raw datasets on disk |
| Reference KB | YES, by `build_reference_kb.py` | the 20 reference files (in a ZIP, location not verified) |

Scripts that read or write these DBs (grep of `scripts/`, tests, docs): `build_youtube_channel_registry.py`, `validate_youtube_channel_registry.py`, `inventory_catalog.py`, `rebuild_inventory_catalog.py`, `register_batch.py`, `register_supplied_channel.py`, `register_structured_source.py`, `apify_youtube_ingest.py`, `ingest_youtube_analytics.py`, `generate_batch_manifests.py`, `report_common.py`, `run_youtube_intelligence.py`, `build_youtube_channel_master_tracker.py/.mjs`, `plan_intelligence_refresh.py`, `stage_what_if_forensics.py`, `promote_what_if_forensics.py`, `query_what_if_forensics.py`; tests `test_youtube_channel_registry.py`, `test_transcript_pending_registration.py`, `test_intelligence_refresh.py`, `test_first_party_analytics.py`, `test_portable_evidence_paths.py`, others. The two validators named in the PR docs (dataset-ledger, channel-registry) pass on the consolidated branch (earlier run in this session, CITED).

**Where each kind of fact lives**
| Fact | Where |
|---|---|
| Channel identity | registry `channels`, `identity_evidence`, `channel_aliases` (75). Casual Finance / Barely Evolved / Primitive Education branch folders hold the rest |
| Video metadata | registry `videos` (2,303); branch CSVs for CF (`INDEX.csv`), Finance (`FINANCE_CONTINUATION_QUEUE.csv`, 1,612), xkcd census (91) |
| Transcripts | registry `transcripts` (2,291 real text); CF `transcripts_asr_base_20261109/` (199 ASR + 16 git); Finance transcripts inside the audit CSV/JSONL |
| Evidence references | registry `artifacts`, `dataset_videos.evidence_locator`, `transcripts.evidence_locator`; inventory `source_files`, `field_provenance` |

Audit pins: the registry pins the inventory hash (`historical_catalog_sha256`). `research/finance-economics-intelligence/audit-baseline/` holds the frozen copy and `MANIFEST.json` (CITED). The frozen registry in #45 is a Git LFS pointer of 3 lines.

---

## 4. Branch, PR and worktree decisions (proposal only; nothing was changed)

Legend: KEEP, CONSOLIDATE, ARCHIVE, REMOVE CANDIDATE, BLOCKED.

### 4.1 Decision table
| Group | Items | Decision | Evidence | Destination / dependencies |
|---|---|---|---|---|
| **Main** | `main` | KEEP | `08e71926`, code and schemas | gets the validated code only (section 5) |
| **CF hub** | `research/casually-finance-consolidated` (`9a4023af`, remote, no PR) | **KEEP** | contains all 7 CF text branches by blob | becomes the single CF branch; needs a PR decision |
| **CF absorbed** | #21 `codex/casually-finance-forensic-research` | CONSOLIDATE then ARCHIVE | 2,257 of 2,257 files identical | close only on owner OK |
| | #37 `research/casually-finance-video-inventory` (CI failing) | CONSOLIDATE then ARCHIVE | 880 of 880 identical | |
| | #47 `research/casual-finance-inventory-scoped` | CONSOLIDATE then ARCHIVE | 10 of 10 identical | |
| | `research/casually-finance-editing-forensics` (remote `2697d3c6`) | CONSOLIDATE then ARCHIVE | 3,017 of 3,017 identical; local copy is 24 commits stale | local copy: fast-forward is safe, local only |
| | `codex/casually-finance-knowledge-navigation` | CONSOLIDATE then ARCHIVE | 5 of 5 identical | |
| | #28 `research/casually-finance-success-playbook` (draft, stacked on #21) | **BLOCKED** | 2,412 of 2,420 identical, **8 differ** | compare the 8 files before retiring; retarget or close after |
| **CF production** | #29 (closed), #30, #34 `production/*` | ARCHIVE | not in consolidated; 9 to 25 media files each | decide: index only vs move; media policy |
| | #41 `research/local-channel-media-library` (CI failing) | BLOCKED | 16 of 19 files absent from consolidated | decide whether it belongs in the hub |
| **Finance stack** | #36 `research/finance-economics-intelligence` (CI failing, stale body) | CONSOLIDATE into #45 | 2,236 of 2,249 identical; #45 contains it | refresh or close; same-line work |
| | #45 `fix/finance-audit-validators` (CI success) | **KEEP** as the Finance line | tip of 215 commits; base is #36 | lands the CI-gate and validator changes |
| | `codex/finance-machine-a-owner-directed` | ARCHIVE | contained in #36 and #45; worktree `yios-finance-machine-a` | worktree stays until owner says remove |
| | `codex/yios-dual-machine-coordination` | **BLOCKED** | 15 files unique, in no other branch | owner decides: keep, port to #45, or drop |
| | #46 `feat/registry-reviewed-workbooks` | KEEP | 12 of 13 files absent from #45; independent | registry work |
| **Other channels** | `research/xkcd-whatif-visual-forensics`, `research/barely-evolved-visual-forensics`, `research/primitive-education-visual-forensics` | KEEP (no PR yet) | unique, no PR | each is one visual-forensics line; see 5.3 |
| | #44, #20, `research/what-if-brain-preservation-batch1` | KEEP / BLOCKED | 405 / 17 / 1,736 files; #44 CI failing; brain-preservation has no PR | needs a What If scoping decision |
| | #25 Casual Economics (477 files) | KEEP, excluded | out of scope per owner | |
| | #38, #39, #43 metadata PRs (CI failing) | KEEP | metadata snapshots | |
| **Senior Health** | #1-#6 merged | ARCHIVE | already in main | |
| | #34 production | ARCHIVE | lowest priority | |
| **Dr Rehan** | #26 `dr-rehan-test-videos`, #32 `production/dr-rehan-diabetes-heart-warning-assets` | **REMOVE CANDIDATE** | Dr Rehan production; no shared dependency found in code (5.5) | after owner decision |
| | `backup/decode-15cbe9f-original` (local only) | ARCHIVE (keep) | 1 commit not on any remote | do not delete before a backup |
| | `codex/ds-000027-dr-ares` (local, 0 unique) | REMOVE CANDIDATE | `08e71926`, equals main | |
| **Merged clutter** | 15 remote branches with 0 unique commits (chore/full-local-data-sync..., the 4 What If source/staging/adapter/promotion, `codex/remaining-work-audit...`, `codex/transcript-pending-registration`, 4 `integration/*`, 4 `research/senior-health-*`) and their local twins | REMOVE CANDIDATE | all commits reachable from main | delete only after owner OK; PR pages remain |
| **Old / test** | `ui/v1` (143 behind), `fix/repository-health-remediation-2026-09-21` (4 ahead), `codex/packaging-rollup-repair-2026-10-11` (50 ahead), `research/thumbnail-forensics-complete-2026-10-04` (71 ahead, no PR), `planning/deferred-legacy-thumbnail-research` (#24), `recovery/local-research-reconciliation-2026-10-12` (#22), `origin/claude/determined-darwin-v0gl6n`, 3 `yios-test/*` | ARCHIVE; `yios-test/*` REMOVE CANDIDATE | unique work only on the ones with "ahead" > 0; `yios-test` are test claim refs | owner review of the 71-commit thumbnail branch |
| **Stash** | `stash@{0}` | KEEP | untouched | do not drop |
| **Worktrees** | `yios-audit-fixes`, `yios-finance-machine-a` | KEEP | clean, owner-approved earlier | remove only with explicit approval |

### 4.2 Group A detail (15 remote heads fully in main)
chore/full-local-data-sync-and-senior-health-acquisition, codex/what-if-source-contract, codex/what-if-readonly-adapter, codex/what-if-normalized-staging, codex/what-if-promotion, codex/remaining-work-audit-2026-10-11, codex/transcript-pending-registration, integration/repository-consolidation-2026-09-25, integration/repository-superset-2026-09-23, integration/yios-current-canonical-2026-10-03, integration/packaging-forensics-validated-subset-2026-10-11, research/senior-health-acquisition-phase-2, research/senior-health-complete-local-sync, research/senior-health-data-expansion-2026-09-28, research/senior-health-forensic-v2.

### 4.3 What was NOT verified for these decisions
- No review of whether any commit message or PR comment records a decision to keep a branch for a reason.
- The 8 differing #28 files, the 22 + 13 + 23 differing Finance files, and the 6 differing/absent files for #41 were listed, not diffed line by line.
- Whether the stash's untracked-file commit holds anything not in git elsewhere.

---

## 5. Coverage by channel and video ID (the crosswalk)

### 5.1 Definitions (what "COMPLETE" means per data type)
| Data type | COMPLETE means | Count shown here is |
|---|---|---|
| Registry video | a row in `videos` (metadata present) | rows |
| Transcript row | a row in `transcripts` (may be a placeholder) | rows |
| Usable transcript | real text, `is_placeholder=0` (registry) or a non-empty ASR/git text file (CF) | text present; CF ASR is **ASR_UNCERTIFIED** (Whisper `base`, not human-checked, names unverified) |
| Local source media | an MP4 with an ID in the name, or a manifest match, ffprobe-readable | files and distinct IDs |
| Visual review | a per-video visual-forensics record exists on a branch or local workspace | records |
| Visual closure | the per-video visual-only contract/gates pass (`VISUAL_ANALYSIS_COMPLETE`, validator exit 0). No claim about sound | ledger rows |
| Full AV sign-off | a human listened and signed off audio plus visual | **0 everywhere** (audio/AV is BLOCKED by owner rule) |

### 5.2 Per-channel crosswalk (focus channels)
| Channel | ID | Niche | Expected (source) | Registry videos | Usable transcripts | Local MP4 (files / IDs) | Visual evidence | Visual closure | Missing IDs (confirmed) |
|---|---|---|---|---|---|---|---|---|---|
| **Casual Finance** | `UCrNfRFWnLC3tCy1TnyhVQ7g` | finance explainers, stick-figure style (33 long + 173 Shorts) | 206 (consolidated `INDEX.csv`; the inventory PR #37/#47 census; **not re-checked live today**) | **0** (channel is identity-only) | 206 of 206 have some text: 16 in git + 199 ASR `base` (overlap 9), all `ASR_UNCERTIFIED` | 216 / 206 catalog IDs (+ 7 unmatched files) | `INDEX.csv`: 19 videos with a visual-forensics dir, 35 with an editing-forensics dir (older depth-A/B/C, not counted) | **19 of target 20** verified by the local counter `count_complete.py` (visual-only). Published text: the 15-video milestone, commit `2697d3c6`. Per-ID match of the 19 against the 19 published dirs is NOT CHECKED | none in catalog; roster 35 targets, 16 not yet closed |
| **xkcd's What If?** | `UC6IxnFzHofFJ5X2PycSMsww` | science explainer, simple animation | **91** (census 2026-11-04T01:43Z: 45 long + 46 Shorts, `census.csv`; not re-run) | **83** | 83 of 83 real text (registry) | 88 / 88 | registry: 3 registered source videos, 107 keyframes; branch: 6 video dirs; local library 44 videos | **29 closed** = 20 Shorts + 9 long-forms (local ledger, all `VISUAL_ANALYSIS_COMPLETE`, failing gates none) | 3 with no local file: `alkJ7xScBiw` (long, acquisition blocked), `NxVdO7M2YdM` (Short), `XwJAbyn5uGY` (Short). 8 census IDs are not in the registry: `35KZm1yiyIE`, `9VG0yqq_PHM`, `NxVdO7M2YdM`, `TIDHee_Q5Gk`, `X97DDWvxaqQ`, `XwJAbyn5uGY`, `alBQCm0QpJg`, `alkJ7xScBiw` |
| **Barely Evolved** | branch dir `UCH59TmQhPOPhC3M17jCWpRQ` (identity NOT cross-checked against the registry; BE is not a registry channel) | (animation/explainer, not classified here) | NOT CHECKED (no census file found) | **not a registry channel** | NOT CHECKED | 3 / 3 | 4 video dirs on its branch; local workspaces for 3 videos | not tallied here (campaign notes say N20 published; see memory) | NOT CHECKED |
| **Primitive Education** | branch dir `UCsuQtyrMiUPdHUQ8WaqsFvQ` | (not classified) | 45 (local `source_census.csv`: 44 video + 1 audio-only) | **not a registry channel** | NOT CHECKED | 44 / 44 (+1 audio-only file, not in the 454) | 6 dirs on its branch | not tallied (on HOLD per notes) | `registry_ids_without_local` = [] per its census |
| **Primate Economics** | `UC14Fb2zWTEZklONPXFbLrTQ` | economics | 29 (Finance queue: 28 original + 1 expansion) | 28 | 28 real | 29 / 29 | thumbnail URL only | none | 1 ID is in the queue + local but not in the registry |
| **MonkeBiznis (folder)** | **unresolved** | habits / lifestyle titles | NOT CHECKED | 0 | n/a | 63 / 63 | none | none | its 63 IDs match no channel in the registry or the Finance queue; `MonkeyExplains1999` (#38, 63 videos in the queue) is a different ID set |
| **Casual Economics** | not looked up (out of scope) | | | 0 | | 11 / 0 IDs | #25: 477 files | excluded by owner | |

### 5.3 Finance universe (1,612 videos; from `FINANCE_CONTINUATION_QUEUE.csv` on #45, CITED and counted)
| Layer | Videos | Channels | In the registry? | Transcript state |
|---|---|---|---|---|
| ORIGINAL (frozen 966) | 966 | 13: Nick Invests 363, Lucas Grant 95, Matty Invests 94, Carl Invests 80, Mr. Finance 65, Bob Invests 57, Brimm. 44, Sonny Finance 39, Dark Ledger 38, Crayon Capital 30, Primate Economics 28, Money Life POV 20, Shaami Finance 13 | **YES, 966 of 966** (sum of those registry rows = 966) | 955 text, 11 placeholders in the queue (registry says 12 placeholders: not reconciled) |
| EXPANSION | 646 | 14: Casually Finance 206, Mark Invests 81, MonkeyExplains 63, Uncle John Financial 53, Economics Explained 30, How Money Works 30, Modern MBA 30, Money & Macro 30, Patrick Boyle 30, PensionCraft 30, Uncle Frank Retirement 27, Logical Money 20, Primitive Education 13, Chronofold 2 (+ 1 Primate Economics) | **NO** | 433 `NOT_REGISTERED`, 197 `UNAVAILABLE_IN_METADATA_ACQUISITION`, 16 partial |

Review progress (CITED, not recounted): `RESUME_HERE.md` and the 2026-11-02 checkpoint on #45 say **558 of 1,612 deep-audited**, 1,054 pending. Status counts in the continuation queue show 564 to 575 `COMPLETE_LIMITED_EVIDENCE` per dimension. These two figures differ and are **not reconciled**. The 2026-11-02 date means the figure may be stale; no later checkpoint was found.

What can be exported later (INFERRED from file names and columns): per-video title, thumbnail, script, topic, performance and virality statuses and metrics (`VIDEO_AUDIT_966.csv/.jsonl`, `SCRIPT_ANALYSIS_966.csv`, `TITLE_ANALYSIS_966.csv`, `THUMBNAIL_ANALYSIS_966.csv`, `TOPIC_ANALYSIS_966.csv`, `VIRALITY_INTELLIGENCE_966.csv`, `FEATURE_COMPARISONS.csv`, `FINANCE_1612_COMBINED_INTELLIGENCE.xlsx`). No export was made.

### 5.4 Registry reconciliation with the earlier numbers
| Earlier number | Verified result |
|---|---|
| 75 channels | 75 rows in `channels` (46 with videos, 29 identity-only). Groups: 44 ORIGINAL_TARGET, 19 ADDED_TARGET, 12 OUTSIDE_TARGET |
| 2,303 registry videos | 2,303 rows; 2,303 distinct IDs; 2,303 transcript rows (2,291 real + 12 placeholder) |
| 1,612 finance/economics videos | 966 originals (all in the registry) + 646 expansion (none in the registry). The "13 channels" of the earlier audit is the original layer only; the universe has 27 channels in the queue |
| 454 local MP4 | 454 files in 7 folders; 453 distinct SHA; 1 exact duplicate; mapping in 3.2 |
| Casual Finance counts | 206 catalog videos; 216 local files; 206 transcripts (ASR); 19 closed. Different numbers are different scopes (catalog vs files vs closures) |
| xkcd counts | 91 census; 83 registry; 88 local; 44 in the library; 29 closed. Same reason |

### 5.5 Finance / economics evidence support for the owner's comparisons
| Comparison | Existing data supports it? | What exists | Gap |
|---|---|---|---|
| Topic | YES, for the 966 originals; limited for expansion | topic analysis CSV, queue `topic_status` (564 done, 1,021 not started) | 646 expansion videos have no topic review |
| Packaging (title, thumbnail) | PARTIAL | title and thumbnail analysis; registry has 41 channels with thumbnail URLs only | no canonical thumbnail files for most channels; thumbnail review done for about 575 |
| Hooks and scripts | PARTIAL | script analysis, DEEP_SCRIPT_MAPS, hook counts (registry 5 VALIDATED channels) | 433 expansion videos have no transcript in the registry; CF transcripts are ASR only |
| Visual technique | **NO for finance outside Casual Finance** | CF: 19 closures, 107 xkcd keyframes | no visual evidence for the other 25 finance channels in the queue |
| Relative performance | PARTIAL, associations only | `views`, `age_days`, snapshot date, tier, ratio vs peers; registry views | views are snapshots at different dates (precision column in the audit CSV); no impressions, CTR, retention or own-channel analytics (AGENTS.md: first-party ingest is READY but no real export loaded); comparability depends on age and format. Treat all patterns as association, not cause |

---

## 6. Proposed structure (proposal; nothing built)

### 6.1 Single entry point
`README.md` stays the entry. Add one `docs/START_HERE.md` (or turn `PROJECT_STATUS.md` into it) that lists, per workstream: branch, hub folder, authoritative file, current counts, owner decisions. The counts in this audit become its first version.

### 6.2 Smallest branch layout the evidence supports
| Branch | Holds |
|---|---|
| `main` | validated code, schemas, validators, CI, docs, registry (LFS), frozen baselines, manifests |
| `research/casual-finance` (rename of the consolidated branch, or keep the name) | CF hub: `INDEX.csv`, transcripts, intelligence, visual records |
| `research/finance-economics` (the #45 line) | the 1,612 universe, audit code, reference framework |
| `research/what-if` | xkcd census, closure records, brain-preservation work (from the 3 What If branches) |
| `research/other-channels` | Barely Evolved, Primitive Education, metadata snapshots |
| short-lived `feat/*` | code changes only, deleted after merge |
`archive/` as a documented tag set, not extra branches (0 tags exist now; tags of absorbed tips cost nothing and keep SHAs).
Production and Dr Rehan material: not in the hub layout (see 6.4).

### 6.3 Folder tree (target)
```
youtube-intelligence-os/
  README.md  docs/START_HERE.md  AGENTS.md  PROJECT_STATUS.md
  scripts/  schemas/  tests/  .github/        <- main only
  data/
    catalog/   youtube_channel_registry.db (LFS) + frozen baseline
    manifests/ extracted/ (text, eligible)
    raw/       (gitignored; local path documented)
  research/
    casually-finance/         (INDEX.csv, transcripts_asr_*, script-intelligence)
    finance-economics-intelligence/
    visual-forensics/channels/<channel_id>/<video_id>/   (text only)
    what-if/  other-channels/
~/YIOS-data/  (local, documented, outside git)
    media/<channel>/*.mp4   audits/  tooling/  evidence/
```

### 6.4 What goes to the private remote, and what stays local
| Class | Remote (private GitHub) | Local path | Off-device backup |
|---|---|---|---|
| Validated code, schemas, tests, CI, docs | YES (main) | repo | GitHub itself |
| Text research (CSV/JSON/MD, transcripts, ledgers, closure records) | YES, eligible text only | repo | GitHub |
| Registry DB, frozen baseline | YES (LFS) | `data/catalog/` | GitHub LFS (**LFS store state NOT CHECKED**) |
| Source MP4 (454), keyframes, heavy forensic evidence | **NO** (never raw video through GitHub) | `~/YIOS-data/media`, `~/YIOS-local-audits` | **BLOCKED**: no destination chosen. About 25.5 GB. Needs an owner-selected drive or cloud and SHA-256 manifests |
| Machine-specific files (locks, venvs, `.DS_Store`) | NO | local | not needed |
| Production assets (renders, audio) | only small generated sets, case by case | local | BLOCKED, same as above |
| Dr Rehan / client material | leaves the active tree in Phase 2 | its own folder | BLOCKED until owner picks a backup |

---

## 7. Dr Rehan and Senior Health: removal check (nothing removed)

Dr Rehan-specific paths found (MEASURED by path match):
- **Branches:** #26 `dr-rehan-test-videos` (62 files, includes `projects/dr-rehan-test-videos/...`), #32 `production/dr-rehan-diabetes-heart-warning-assets` (473 files: exports 167, assets 149, animation_v2 93, scenes 18, reviews 8), `backup/decode-15cbe9f-original` (local), `codex/ds-000027-dr-ares`.
- **On main:** `data/raw/competitors/DS-000032/` (60 files), `data/extracted/channel-data/DS-000032/packages/decode-your-heart-dr-rehan/` (2), `docs/research/decode-your-heart-2026-09-27/` (6), `data/manifests/DS-000032.md`, `docs/audits/DECODE-YOUR-HEART-PRIVACY-CLASSIFICATION-2026-10-03.md`, `scripts/build_dr_rehan_package.py`, `scripts/build_decode_your_heart_recovery.py`, `scripts/decode_your_heart_final_diagnosis.py`, `scripts/update_decode_report.py`, `tests/test_decode_your_heart_recovery.py`.
- **Registry:** the channel "Decode Your Heart - Dr. Rehan" (`UCQIzqH7QZ9viBYpOFqgSXMg`) has 56 videos and 56 real transcripts. Dr Rehan is also named in 17 docs/audit files (Senior Health inventories, thumbnail-forensics inventory, coverage ledger) and in `scripts/build_better_health_while_aging_package.py`.
- **Local:** `~/workprojects/dr rehan video` (1.5 GB, own `CLAUDE.md`, `.venv`).

Shared-dependency findings (MEASURED by path/grep, not by running tests):
- The two production branches (#26, #32) touch only `projects/dr-rehan-*` and `productions/dr-rehan-*`; no path under `scripts/`, `tests/` or `.github/` is shared, so they look removable without breaking code. Whether the 12 and 10 media files there are referenced by anything else was not traced.
- The **research** side is entangled: the registry counts (75 channels, 2,303 videos, 56 of them Decode Your Heart), registry validators and `docs/` ledgers include Decode Your Heart. Removing it changes pinned totals and needs the registry rebuild/validators to be re-run. Its status as "Dr Rehan client" or "third-party Senior Health competitor" is not clear from the files. **Owner decision needed** (section 8.5).

Senior Health third-party research (KEEP for the independent channel): registry channels Senior Health Hub (122), Better Health While Aging (98), Dr. Okoro (66), Dr. Ares Senior (35), Dr. Aliza Wright (32), Dr. Elias (29), Doctor Thomas (22), plus the merged PRs #1-#6 and `docs/research/senior-health-*` on main. Production #34 is "Senior Health with Casual Finance style" and sits with production, not research.

---

## 8. Phase 2 cleanup order (proposal)

Each step: prerequisite, verification, rollback. Nothing starts until the owner approves.

| # | Step | Prerequisites | Verification | Rollback point |
|---|---|---|---|---|
| 0 | **Choose an off-device backup destination**; copy local evidence with SHA-256 manifests | owner picks drive/cloud; Machine B checks (3.4) done | hash compare of every copied file | originals stay untouched |
| 1 | Create tags for every branch tip planned for removal (`archive/<name>` -> full SHA) | owner OK | `git tag -l`, `git ls-remote --tags` match the tip SHAs recorded here | delete the tags |
| 2 | Fast-forward the 3 stale local branches (CF editing-forensics, Finance #36, and any other that is 100% behind its remote) | owner OK; stash and untracked kept | `rev-parse` equals remote | reflog |
| 3 | Resolve the 8 differing #28 files and the dual-machine unique work (15 files) | owner decisions 8.2, 8.4 | diff written to an audit note | none needed, read-only |
| 4 | Decide CF PR: scoped or full PR for the consolidated branch; then close #21/#37/#47/#28 only with explicit authorization | owner OK; step 3 done | PR checks green; the absorbed branches' blobs still reachable via tags | reopen PRs, tags keep tips |
| 5 | Delete the 15 merged remote branches and their local twins | tags exist (step 1); owner OK | `git branch -r --merged origin/main` list equals the deletion list | recreate from tags |
| 6 | Dr Rehan: archive #26, #32, `backup/decode-*`, then (separately) decide DS-000032 research | owner decision 8.5; backup done | validators and tests still pass after any registry change | tags + backup folder |
| 7 | Refresh or close #36; merge or rebase #45 per owner choice; keep #46 | owner OK | CI on the new head SHA | PR history |
| 8 | Move media policy: replace the 16 LFS source-video pointers and the 100 MB production media with documented local paths | owner decision 8.6 | `git ls-tree` media list shrinks as planned; LFS store checked | tags |
| 9 | Add `docs/START_HERE.md`, link the crosswalk, set branch layout | steps 1 to 8 | doc links resolve | revert the commit |

**Exact duplicate or unused code/file candidates** (only listed; the entry-point check below is NOT done):
- Byte-duplicate registry copies: 3 checkouts + frozen baseline all `39e7a28b...`. The frozen baseline is intentional (a test pins it); the two worktree copies follow from the worktrees, not from separate data.
- Exact duplicate media: 1 CF file ("Why Japan's Economy Is Awful ... (1).mp4", same SHA as the original).
- 848 files identical between #45 and the consolidated branch (CF content on two branches). That disappears when one line owns CF.
- Dr Rehan scripts and tests (section 7) are candidates only after the research-side decision.
- A real "unused code" list needs an import/entry-point trace of `scripts/` against tests, CI and docs. I did not do that trace. Classifying a script as unused from file names alone would be a guess, so none is listed.

### 8.x Owner decisions needed before Phase 2
1. **Backup destination** for the ~25.5 GB of local-only data (drive, cloud, or second Mac). Without this nothing local can be moved or removed safely.
2. **Casual Finance:** open a PR for the consolidated branch (scoped text-only, or full)? And retire #21, #37, #47, #28 and the CF editing-forensics branch after tagging? Which of the 8 differing #28 files is authoritative?
3. **CF production branches** (#29/#30/#34) and #41: index only, move into the CF hub, or archive?
4. **Finance:** keep #45 as the one Finance line and retire #36 and Machine A? What happens to the 15 files that exist only in `codex/yios-dual-machine-coordination`? Refresh or close #36 (its CI fails, its body is stale)?
5. **Dr Rehan:** does "Dr Rehan" mean only the client/production material (#26, #32, local folder), or also the Decode Your Heart competitor research (DS-000032, 56 registry videos, scripts and tests)? If both, accept that registry totals and validators change.
6. **Media in git:** accept replacing the 16 Casual Finance source-video LFS pointers (and the 100 MB-class production media) with local paths plus backup?
7. **Branches without PRs:** open PRs for xkcd, Barely Evolved, Primitive Education, brain-preservation, thumbnail-forensics, dual-machine, Machine A, or tag-and-archive them?
8. **MonkeBiznis folder (63 MP4):** which channel is it, and is it in scope?
9. **Finance niches and "two channels":** the final two niches are left to evidence; confirm that Phase 2 should not choose them.
10. **Machine B:** provide an authorized way to inspect it, or accept that its unpushed work stays unknown.

---

## 9. Corrections to the earlier audit and open caveats

- The earlier audit said the consolidated branch "has no upstream / not pushed". Today `git ls-remote` shows `refs/heads/research/casually-finance-consolidated` = `9a4023af...` on origin. Who pushed it and when is not recorded in this audit. A PR for it does not exist.
- It guessed #45's base ("probably not main"). Measured: base is `research/finance-economics-intelligence`.
- The registry/branch count notes that put xkcd closures at "20/20 Shorts, 0 longs" are stale. The ledger now lists 9 long-forms (closed 2026-11-09 between 10:01Z and 16:06Z). The "13 Finance channels" is the original layer only.
- NOT CHECKED: live YouTube counts (no network census was run), CI log reasons, LFS object presence on GitHub, content of branches beyond file-blob comparison, Barely Evolved and Primitive Education census totals, the 16 not-yet-closed CF roster videos, per-ID match of CF closures against published dirs, the HumanCraft book content, any non-YIOS project, Machine B.
- Facts that can change under you: five-hour usage was 1% at the start; xkcd and CF counts come from local ledgers that other sessions may keep editing.
