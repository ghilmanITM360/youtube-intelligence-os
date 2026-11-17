# YIOS Machine A audit and synchronization — 2026-10-21

Verdict: **MACHINE_A_PARTIALLY_SYNCED_BLOCKED**. All eligible local branches synchronized: 22 already aligned, 2 fast-forwarded, 1 dirty Finance branch blocked, 1 intentional backup branch without upstream preserved. No diverged branches. Two registered worktrees retained; none retired.

## Machine identity and scope

- Host: `ghilmankhan` Git author identity; operating host `Ghilmans-Laptop.local`, login `ghilmankhan`. Canonical cwd/top-level: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`.
- Origin fetch/push: `https://github.com/ghilmanITM360/youtube-intelligence-os.git`. Authenticated active GitHub CLI account: `ghilmanITM360`; HTTPS access verified by authenticated fetch and API reads. Tokens not stored in this report.
- Main worktree branch: `research/finance-economics-intelligence`; before/after HEAD `aea737320ad127e9783ab02912694c38c87b7c49`; upstream `origin/research/finance-economics-intelligence`.
- Common Git directory: `/Users/ghilmankhan/workprojects/youtube-intelligence-os/.git`; linked forensic worktree uses the same common directory. Not an independent clone. Repository is not shallow; it is a promisor partial clone (`blob:none`).
- Disk preflight: 40 GiB available; later observation 37 GiB before removal of redundant audit archive. No large source/media transfer performed.
- Initial live usage: five-hour 24%, weekly 40%; later 31%/41%. No context warning observed; exact context utilization unavailable. Paid balance 0; no paid runs or reset credits used.
- One agent. No new worktrees, branches, clones, commits, PRs, pushes, merges, rebases, resets, cleaning, stash application/drop, source edits, or retirement of another writer.
- No submodules reported; no Git locks found; no unrelated active Git mutation process found in preflight. Local Codex app server active; other listed project chats not loaded. Desktop process absence does not revoke documented Claude ownership or prove Machine B inactivity.

## A. Before / after local branches

All SHAs below are full commit IDs. Ahead/behind is against the fetched, verified upstream. PR owner refers to GitHub author, not checkout availability. Ref-only replica synchronization of two unoccupied branches did not claim research/production ownership.

| Branch | Previous SHA | Final SHA | Upstream | Ahead/behind | Outcome | Relevant PR |
|---|---|---|---|---|---|---|
| backup/decode-15cbe9f-original | 15cbe9f0112596c1e07c1c1504302cce77bfd97a | 15cbe9f0112596c1e07c1c1504302cce77bfd97a | none | N/A | NO_UPSTREAM_PRESERVED | none found |
| chore/full-local-data-sync-and-senior-health-acquisition | 1a46d84c16d2b4409f7f87d908b0e44f894b1b0b | f3c5635347c843c16796c3fe2a9af0799c2ffd8e | origin/chore/full-local-data-sync-and-senior-health-acquisition | 0/0 | FAST_FORWARDED | #4 MERGED (@ghilmanITM360); #1 MERGED (@ghilmanITM360) |
| codex/casual-economics-forensic-research | fce81670bd2d6f29db6ef515732238fa3c5f09e3 | fce81670bd2d6f29db6ef515732238fa3c5f09e3 | origin/codex/casual-economics-forensic-research | 0/0 | ALREADY_SYNCED | #25 OPEN (@ghilmanITM360) |
| codex/casually-finance-forensic-research | 043b85bf58f84fb6a1c8981d54e3b233faa6a928 | 043b85bf58f84fb6a1c8981d54e3b233faa6a928 | origin/codex/casually-finance-forensic-research | 0/0 | ALREADY_SYNCED | #21 OPEN (@ghilmanITM360) |
| codex/ds-000027-dr-ares | 25110136c61ac0cc8bb124a1cacd3aa5fae8a840 | 08e719264e31ecd82de24f8eeb8f065c08359fe5 | origin/main | 0/0 | FAST_FORWARDED | none found |
| codex/packaging-rollup-repair-2026-10-11 | 9ce62de2365975ccece5e096c050e1ed1bcba622 | 9ce62de2365975ccece5e096c050e1ed1bcba622 | origin/codex/packaging-rollup-repair-2026-10-11 | 0/0 | ALREADY_SYNCED | none found |
| codex/register-verified-transcript-pending-what-if | e9b56960f6c6bcbb07d5dd0475eaf4572a657a25 | e9b56960f6c6bcbb07d5dd0475eaf4572a657a25 | origin/codex/register-verified-transcript-pending-what-if | 0/0 | ALREADY_SYNCED | #20 OPEN (@ghilmanITM360) |
| codex/remaining-work-audit-2026-10-11 | 6338efe21a8f83cbf4cac31f15779a8ae31fb69a | 6338efe21a8f83cbf4cac31f15779a8ae31fb69a | origin/codex/remaining-work-audit-2026-10-11 | 0/0 | ALREADY_SYNCED | #18 MERGED (@ghilmanITM360) |
| codex/transcript-pending-registration | ec17164134bf051252b7160a53d3e7a2529ca533 | ec17164134bf051252b7160a53d3e7a2529ca533 | origin/codex/transcript-pending-registration | 0/0 | ALREADY_SYNCED | #17 MERGED (@ghilmanITM360) |
| dr-rehan-test-videos | 8daa1c831834ff30f2b72180a2e233b566b36468 | 8daa1c831834ff30f2b72180a2e233b566b36468 | origin/dr-rehan-test-videos | 0/0 | ALREADY_SYNCED | #26 OPEN (@ghilmanITM360) |
| fix/repository-health-remediation-2026-09-21 | 11ad082bec7cd7dcd21ab16cde388f76c867e004 | 11ad082bec7cd7dcd21ab16cde388f76c867e004 | origin/fix/repository-health-remediation-2026-09-21 | 0/0 | ALREADY_SYNCED | none found |
| integration/packaging-forensics-validated-subset-2026-10-11 | ce82c0a871b756b829f4812501eb5c81b10de279 | ce82c0a871b756b829f4812501eb5c81b10de279 | origin/integration/packaging-forensics-validated-subset-2026-10-11 | 0/0 | ALREADY_SYNCED | #19 MERGED (@ghilmanITM360) |
| integration/repository-consolidation-2026-09-25 | 73816f1e853f750300b8cee5588077ac0b3837e4 | 73816f1e853f750300b8cee5588077ac0b3837e4 | origin/integration/repository-consolidation-2026-09-25 | 0/0 | ALREADY_SYNCED | #5 MERGED (@ghilmanITM360) |
| integration/repository-superset-2026-09-23 | 0930dfe381a0578ff3201de0290f5529cc7b706a | 0930dfe381a0578ff3201de0290f5529cc7b706a | origin/integration/repository-superset-2026-09-23 | 0/0 | ALREADY_SYNCED | none found |
| integration/yios-current-canonical-2026-10-03 | c1c3bb8860b92fb3a54628da0b6e41252453f5b0 | c1c3bb8860b92fb3a54628da0b6e41252453f5b0 | origin/integration/yios-current-canonical-2026-10-03 | 0/0 | ALREADY_SYNCED | #7 MERGED (@ghilmanITM360) |
| main | 08e719264e31ecd82de24f8eeb8f065c08359fe5 | 08e719264e31ecd82de24f8eeb8f065c08359fe5 | origin/main | 0/0 | ALREADY_SYNCED | none found |
| production/dr-rehan-diabetes-heart-warning-assets | c867af8effe05a2654d936c0d8aec4274bf40bdc | c867af8effe05a2654d936c0d8aec4274bf40bdc | origin/production/dr-rehan-diabetes-heart-warning-assets | 0/0 | ALREADY_SYNCED | #32 OPEN (@ghilmanITM360) |
| production/finance-short-01-keyframe | 315e76d5f805abf9af31e3aac35087c1d7fc61d1 | 315e76d5f805abf9af31e3aac35087c1d7fc61d1 | origin/production/finance-short-01-keyframe | 0/0 | ALREADY_SYNCED | #29 CLOSED (@ghilmanITM360) |
| production/finance-short-02-assets | 30e0ef2f8c1c1abe8189ebe1feb560286db62607 | 30e0ef2f8c1c1abe8189ebe1feb560286db62607 | origin/production/finance-short-02-assets | 0/0 | ALREADY_SYNCED | #30 OPEN (@ghilmanITM360) |
| production/senior-health-casually-finance-three-videos | 65caa889a3e1b9f3a1be6fa28a31ae4f518577a1 | 65caa889a3e1b9f3a1be6fa28a31ae4f518577a1 | origin/production/senior-health-casually-finance-three-videos | 0/0 | ALREADY_SYNCED | #34 OPEN (@ghilmanITM360) |
| research/casually-finance-editing-forensics | 090f84b3292a3b6c6e94653a6ef1867726e4ebdd | 090f84b3292a3b6c6e94653a6ef1867726e4ebdd | origin/research/casually-finance-editing-forensics | 0/0 | ALREADY_SYNCED | none found |
| research/finance-economics-intelligence | aea737320ad127e9783ab02912694c38c87b7c49 | aea737320ad127e9783ab02912694c38c87b7c49 | origin/research/finance-economics-intelligence | 0/20 | BLOCKED_DIRTY_MACHINE_B_OWNED | #36 OPEN (@ghilmanITM360) |
| research/senior-health-acquisition-phase-2 | 373bf37e930bbfedefb9ae2423a3fde9a1ad151b | 373bf37e930bbfedefb9ae2423a3fde9a1ad151b | origin/research/senior-health-acquisition-phase-2 | 0/0 | ALREADY_SYNCED | none found |
| research/senior-health-data-expansion-2026-09-28 | 814a027976d8373920500600805542070429e5eb | 814a027976d8373920500600805542070429e5eb | origin/research/senior-health-data-expansion-2026-09-28 | 0/0 | ALREADY_SYNCED | #6 MERGED (@ghilmanITM360) |
| research/senior-health-forensic-v2 | 206d67bcc3ca9ada065d437d04c24dbe8d201cda | 206d67bcc3ca9ada065d437d04c24dbe8d201cda | origin/research/senior-health-forensic-v2 | 0/0 | ALREADY_SYNCED | #2 MERGED (@ghilmanITM360) |
| research/thumbnail-forensics-complete-2026-10-04 | 6c6e8900a5255d6cdba2ca0018ec0186eb8b64ed | 6c6e8900a5255d6cdba2ca0018ec0186eb8b64ed | origin/research/thumbnail-forensics-complete-2026-10-04 | 0/0 | ALREADY_SYNCED | none found |

Actual transitions:
- `chore/full-local-data-sync-and-senior-health-acquisition`: `1a46d84c16d2b4409f7f87d908b0e44f894b1b0b` → `f3c5635347c843c16796c3fe2a9af0799c2ffd8e`. Strict ancestry, no registered checkout, absence of locks, expected-old compare-and-swap update, and immediate exact new-SHA verification passed.
- `codex/ds-000027-dr-ares`: `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` → `08e719264e31ecd82de24f8eeb8f065c08359fe5`. Strict ancestry, no registered checkout, absence of locks, expected-old compare-and-swap update, and immediate exact new-SHA verification passed.

Finance prefetch cached tracking count was 0/9; authenticated fetch established actual 0/20. No remote history rewrite detected in fetch; both changed origin refs advanced normally. Same-name remote equality was not substituted for configured-upstream ancestry (`codex/ds-000027-dr-ares` intentionally tracks origin/main).

## B. Worktrees

| Path | Branch / full SHA | Status / ignored evidence | Owner | Disposition |
|---|---|---|---|---|
| /Users/ghilmankhan/workprojects/youtube-intelligence-os | research/finance-economics-intelligence / aea737320ad127e9783ab02912694c38c87b7c49 | 11 unstaged tracked modifications; 0 staged paths; 302 untracked; 2,760 ignored files | Machine B sole Finance writer; this chat coordination/audit only | KEEP canonical; BLOCKED_DIRTY |
| /Users/ghilmankhan/workprojects/yio-cf-editing-forensics | research/casually-finance-editing-forensics / 090f84b3292a3b6c6e94653a6ef1867726e4ebdd | Tracked/index/untracked clean; 1 ignored .DS_Store | Claude session 873b9a27-ba03-4183-aa61-f82d01f65998, owner-designated 2026-10-20 | KEEP protected; aligned but not released for retirement |

Before 2; after 2; safely retired 0. Neither registration is broken, detached, locked or prunable; `git worktree prune --dry-run --verbose` proposed no cleanup. No force or actual prune used. `yio-cf-editing-forensics-local-evidence` and `yios-recovery-status` are ordinary evidence directories, not registered worktrees or independent repositories.

## C. Local-only evidence and preservation

External audit root: `/Users/ghilmankhan/YIOS-local-audits/2026-10-21`. Original paths and relative structure retained in JSON manifests. All source directories remain in place.

| Evidence | Exact inventory | Preservation / verification |
|---|---|---|
| Main modified tracked files | 11 files; 25,507,607 bytes | Exact external copies plus binary unstaged patch; all SHA-256 verified |
| Main untracked evidence | 302 files; 161,801,153 bytes | Exact external copies; all SHA-256 verified; includes production, Short 02 calibration, script intelligence, NICK batches/images |
| Main ignored files | 2,760 files; 124,950,707 bytes | All inventoried and retained; 262 hashed, including relevant outputs; 237 non-cache/non-DS_Store files copied (50,427,177 bytes) and hash-verified |
| Forensic ignored file | 1 file; 6,148 bytes | Retained and SHA-256 verified |
| Casually Finance source and durable media | 54 files / 393,588,505 bytes per copy; 53 distinct hashes; 48 mapped Video IDs | All 108 source/durable paths independently rehashed against established manifest; PASS |
| Local-only commits | 4 commits absent from remote refs | 1 Decode backup commit plus stash commit and two stash parents; existing refs retained; verified local-only-commits.bundle |
| Stash | 1; 5b6c3042679400b16aa1024b79058b71dade0ab9 | IDs/count unchanged; reflogs copied; bundle verified |
| Recovery objects | fsck: 86 dangling objects (49 blobs, 37 trees); no dangling commits reported | 175 unique/reflog object graph entries preserved in verified compact pack; original Git object store untouched |

The Decode commit `15cbe9f0112596c1e07c1c1504302cce77bfd97a` is reachable only through local `backup/decode-15cbe9f-original`; no matching GitHub upstream. The stash support commits are `d114cc36771b818524da60267a77a82592fd6f65` and `e9b7c70c2ffd4ec3b7c3f9af9684597552973deb`. Do not delete these refs or archives.

Additional external evidence census (overlaps/derived copies are not additive unique evidence):

| Path | Files | Bytes | Disposition |
|---|---|---|---|
| /Users/ghilmankhan/Downloads/all training data of youtube | 15 | 6,891,874 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Downloads/dr rehan old videos | 1 | 6,148 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Downloads/CasuallyFinance | 54 | 393,588,505 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Downloads/casual_economics | 11 | 659,321,738 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research | 2033 | 1,233,825,567 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/workprojects/yios-recovery-status | 2130 | 71,424,682 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence | 392 | 4,459,400,272 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Documents/YIOS-Production-Library | 1098 | 201,342,191 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21 | 5373 | 3,710,635,920 | Retained in place; per-file inventory in audit root |
| /Users/ghilmankhan/Documents/yios-private-backups | 851 | 276,586,146 | Retained in place; per-file inventory in audit root |

Existing prior research export and preservation manifests were located, not rerun or rewritten. External frame outputs include 4,459,400,272 bytes under the forensic evidence directory. These unmoved external files were stat-inventoried, not claimed newly hash-verified. Cache/dependency contents were inventoried and retained without redundant backup. Separate independent repository markers are listed in `independent-repository-markers.json`; none modified. Nested scan of canonical checkout found only its own .git.

## D. GitHub / PR alignment

GitHub: 38 branch heads; 39 remote-tracking refs including origin/HEAD; 26 local branches. Remote-only names: `codex/what-if-normalized-staging`, `codex/what-if-promotion`, `codex/what-if-readonly-adapter`, `codex/what-if-source-contract`, `planning/deferred-legacy-thumbnail-research`, `recovery/local-research-reconciliation-2026-10-12`, `research/barely-evolved-metadata`, `research/casually-finance-success-playbook`, `research/casually-finance-video-inventory`, `research/local-channel-media-library`, `research/monkey-explains-1999-metadata`, `research/senior-health-complete-local-sync`, `research/youtube-12-channel-metadata`, `ui/v1`. No unnecessary local branches created. Full remote SHAs before/after are in github-before.txt, github-after.txt and remote-refs-after.txt. No tags reported; fetch requested tags normally without prune.

16 open PRs: 11 drafts, 5 non-drafts. All have verified matching fetched origin head SHAs and recorded base, title, update time and author in prs.json. Historical merged/closed PR associations are recorded in all-prs.json.

| PR | Title | Head branch / full SHA | Base | State | Updated UTC | Local relation | Exact-head Actions |
|---|---|---|---|---|---|---|---|
| #43 | research: add BarelyEvolved channel metadata | research/barely-evolved-metadata / c4212c90ecd57fe9416da2948a95669050366512 | main | OPEN / DRAFT | 2026-10-20T12:16:07Z | local branch absent; fetched origin matches | BILLING BLOCKED; 0 steps executed |
| #41 | Add checksummed local channel media library | research/local-channel-media-library / 78e8fd2de654b622a5b1a093851886ef138c4d6a | main | OPEN / DRAFT | 2026-10-21T04:26:42Z | local branch absent; fetched origin matches | BILLING BLOCKED; 0 steps executed |
| #39 | research: add 12-channel YouTube metadata snapshot | research/youtube-12-channel-metadata / 967ea707a0d7198754d132a978962baa96073f49 | main | OPEN / DRAFT | 2026-10-20T08:00:40Z | local branch absent; fetched origin matches | BILLING BLOCKED; 0 steps executed |
| #38 | research: add MonkeyExplains1999 metadata snapshot | research/monkey-explains-1999-metadata / f176aa2861cd93913b977e6159a4e00f4eabeacc | main | OPEN / DRAFT | 2026-10-20T06:30:34Z | local branch absent; fetched origin matches | BILLING BLOCKED; 0 steps executed |
| #37 | research: Casual Finance complete video download inventory | research/casually-finance-video-inventory / 1adfdeb9462023b39fa62b9a54da12ccd874ae16 | main | OPEN | 2026-10-19T12:10:24Z | local branch absent; fetched origin matches | BILLING BLOCKED; 0 steps executed |
| #36 | research: full 966-video Finance and Economics audit (in progress) | research/finance-economics-intelligence / d41a5774f1381a21022b70f02d206303195be3a7 | main | OPEN / DRAFT | 2026-10-21T12:32:10Z | local older: 0/20 | BILLING BLOCKED; 0 steps executed |
| #34 | Senior health: three original illustration and keyframe review packages | production/senior-health-casually-finance-three-videos / 65caa889a3e1b9f3a1be6fa28a31ae4f518577a1 | main | OPEN / DRAFT | 2026-10-15T20:43:34Z | MATCH | PASS; 16 steps executed |
| #32 | Dr Rehan: diabetes heart warning storyboard and illustrated assets | production/dr-rehan-diabetes-heart-warning-assets / c867af8effe05a2654d936c0d8aec4274bf40bdc | main | OPEN / DRAFT | 2026-10-15T12:04:35Z | MATCH | PASS; 16 steps executed |
| #30 | Finance Short 02: original reference-led illustration asset package | production/finance-short-02-assets / 30e0ef2f8c1c1abe8189ebe1feb560286db62607 | main | OPEN / DRAFT | 2026-10-14T11:19:30Z | MATCH | PASS; 16 steps executed |
| #28 | Research: Casually Finance Success & Production Playbook | research/casually-finance-success-playbook / fb1e56d03e5ad53086c74247cd2972b262d09b78 | codex/casually-finance-forensic-research | OPEN / DRAFT | 2026-10-13T06:33:36Z | local branch absent; fetched origin matches | PASS; 16 steps executed |
| #26 | Dr Rehan Test Videos | dr-rehan-test-videos / 8daa1c831834ff30f2b72180a2e233b566b36468 | main | OPEN / DRAFT | 2026-10-12T20:17:31Z | MATCH | PASS; 16 steps executed |
| #25 | research: acquire Casual Economics and begin audiovisual forensics | codex/casual-economics-forensic-research / fce81670bd2d6f29db6ef515732238fa3c5f09e3 | main | OPEN | 2026-10-14T18:40:11Z | MATCH | PASS; 16 steps executed |
| #24 | docs: plan deferred legacy thumbnail evidence reuse | planning/deferred-legacy-thumbnail-research / 9e7be191a35d012416c73c25b0a9025dca33eb1a | main | OPEN / DRAFT | 2026-10-12T08:27:17Z | local branch absent; fetched origin matches | PASS; 16 steps executed |
| #22 | Preserve recovered historical B002 research and audit local synchronization | recovery/local-research-reconciliation-2026-10-12 / 0fdf5a2dc8aa7b63f0e7f8290bede7053514efa2 | main | OPEN | 2026-10-12T08:03:15Z | local branch absent; fetched origin matches | PASS; 16 steps executed |
| #21 | research: complete Casual Finance available corpus and production DNA | codex/casually-finance-forensic-research / 043b85bf58f84fb6a1c8981d54e3b233faa6a928 | main | OPEN | 2026-10-13T04:06:08Z | MATCH | PASS; 16 steps executed |
| #20 | Register verified What If identities with transcript-pending state | codex/register-verified-transcript-pending-what-if / e9b56960f6c6bcbb07d5dd0475eaf4572a657a25 | main | OPEN | 2026-10-10T21:18:47Z | MATCH | PASS; 16 steps executed |

Exact-head workflow validation executed on 10 PRs; 6 failed checks did not execute validation. GitHub annotations for #36/#37/#38/#39/#41/#43 state: “The job was not started because recent account payments have failed or your spending limit needs to be increased.” No workflow reruns requested. Successful general repository CI does not prove completion or semantic validity of research.

## E. Project readiness

| Area | Verified current state | Availability / limits |
|---|---|---|
| Finance PR #36 | d41a5774f1381a21022b70f02d206303195be3a7; 1,612 unique IDs = 966 original + 197 first expansion + 63 Monkey + 386 reconciliation | Fetched Git objects available; checked-out Finance branch remains older/dirty |
| Latest audit | NICK_161 / SU-3ZcgmCJ4; 437 limited-evidence audits; 0 full-evidence audits; 529 original and 1,175 combined remaining | Independently counted six-dimension statuses in exact-head JSONL; next outstanding S_8SLGjLrBM |
| Workbook | Sole tracked current Finance Excel at PR head: FINANCE_1612_COMBINED_INTELLIGENCE.xlsx; all 1,612 IDs match universe; cached totals 437/1,175; 42 registered channels; zero error-type XML cells | SHA-256 b87869124ec31a59b8d9e640ed370f72f303cd2902f1f0ef63b47998296002a9; existing ZIP inspected read-only; not regenerated or recalculated |
| Local Finance working copy | 966 records, 430 limited-evidence completions; FINANCE_966_VIDEO_INTELLIGENCE.xlsx locally modified | Preserved historical/local evidence; combined workbook not installed into dirty checkout |
| Static Finance universe labels | 1,612 IDs correct; static audit_status labels still mark 430 complete | Current JSONL and workbook overlay reach 437. Reported as stale derived labels; no research edited |
| Finance validation metadata | Latest VALIDATION_966.json: PASS, zero errors, 26 immutable source hashes reported checked | Not rerun as a new Finance audit. RESEARCH_CHECKPOINT_VALIDATION.json is an older 30-review snapshot; not current completion evidence |
| Casually Finance forensic | Branch 090f84b3292a3b6c6e94653a6ef1867726e4ebdd aligned; checkpoint states 38/48 visual reviews, all Shorts; 10 long-form remain | Source media and external frames present; direct listening blocked per source; sole owner retained |
| Senior Health research | Acquisition, expansion and forensic branch heads match fetched GitHub; acquisition aggregate ref safely advanced 5 commits | Production #34/#32 aligned, exact-head CI executed; local authored production evidence preserved |
| Casual Economics | #25 / fce81670bd2d6f29db6ef515732238fa3c5f09e3 aligned; 11 external media files present | Sources retained; no repeated forensic research |
| Finance Shorts / thumbnail research / core | Short 02 #30 aligned; Short 01 branch preserved (#29 CLOSED); thumbnail and other local core branch heads aligned with configured upstreams | Untracked production/calibration assets remain separate from Git history; no rebuilt output |
| Machine B media | Full 4.1 GB library not imported | Machine-specific availability limitation, not missing Git history; no current Machine B filesystem inspection claimed |

## F. Blockers

1. Main Finance branch: 0 ahead/20 behind; 11 modified tracked paths all overlap upstream changes; 20 untracked paths are now tracked upstream. All exact local files backed up. Machine B owns Finance. Do not stash/reset/restore these files or fast-forward this checkout until the owner-approved reconciliation is concrete.
2. Forensic worktree: clean and aligned, but protected sole writer session has not released it. No retirement, switch, source edit, interruption or handoff message authorized/performed.
3. Backup Decode branch has no upstream and contains unique local history. This is intentional preservation, not a branch to reset or push automatically.
4. Six exact-head Actions validations blocked before steps by GitHub billing/spending limits. No fresh CI pass claimed for these heads.
5. Finance current counts require authoritative JSONL/workbook overlay; static universe completion labels and older checkpoint validation are stale. Native Excel recalculation and underlying research semantic entailment are outside this synchronization audit.

## Validation evidence

git fsck --full exited 0: no corruption/missing-object error; 86 dangling objects archived. Partial clone promisor semantics apply: this is not a claim that every historical blob is physically materialized. All original local branch tips remain ancestors of final tips. Stash ID/count unchanged. Before/after statuses differ only in fetched ahead/behind header. All untracked/ignored path sets unchanged; all original inventoried files remain present with unchanged sizes. 576 original evidence file SHA-256 checks passed; all 313 primary preservation copies and 237 ignored-evidence copies verified. Media verification adds 108 file reads. No source data or research files removed. Focused code tests were not run: only unoccupied refs advanced; no checked-out code or research was changed.

## Exact continuation

1. Read this report and `/Users/ghilmankhan/YIOS-local-audits/2026-10-21/INITIAL_INVENTORY.md`, branches-after.json, finance-conflicts.json, final-verification.json, and archive SHA256 manifest. Recheck live resource limits and ownership before any future mutation.
2. To reconcile Finance, obtain availability and scope from Machine B owner. Compare each exact preserved local patch/file with d41a5774f1381a21022b70f02d206303195be3a7 (or its newly fetched successor); preserve original directory provenance. Resolve the 11 tracked overlaps and 20 untracked/upstream collisions without research rewriting by this coordination chat. Keep old workbook as historical evidence outside active deliverables. Only once an approved non-destructive reconciliation yields an available clean checkout may an ff-only update be attempted.
3. Keep forensic worktree and 4.46 GB frame evidence intact until designated Claude session is explicitly released by owner. Recheck source inventory, unpublished commits, ignored files and common-dir registrations before normal non-force worktree removal. Retain branch and stash.
4. Keep Decode backup ref, stash, reflog copies, bundle and compact recovery pack. Bundle requires prerequisite objects verified in this repository; do not treat it as a new standalone clone. Archive manifests support recovery without creating refs during this audit.
5. Billing owner may resolve GitHub Actions account limits. Do not rerun or spend/reset credits automatically. Fetch/read current PR head and exact-head checks after any future change.

Final verdict: **MACHINE_A_PARTIALLY_SYNCED_BLOCKED**. 24/25 upstream-configured local branches aligned; 1 dirty upstream branch blocked; 1 upstream-less backup preserved. 2 → 2 worktrees; zero retired.

Additional independent workbook row count: All Finance Videos column AA and Detailed Research column E each contain exactly 437 DEEP_AUDIT_COMPLETE records.
