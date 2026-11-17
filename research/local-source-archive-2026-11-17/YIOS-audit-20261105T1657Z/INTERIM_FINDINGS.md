# YIOS audit: interim findings (2026-11-05 ~18:44Z)

Not the final report. Labels: FRESH, HISTORICAL, INFERENCE, UNKNOWN.

## 1. Host identity
- FRESH: hostname `Ghilmans-Laptop.local`, user `ghilmankhan`, canonical checkout `/Users/ghilmankhan/workprojects/youtube-intelligence-os`.
- HISTORICAL coordination record `~/YIOS-Archive/TWO_MAC_HANDOFF_2026-10-29.md` names exactly that path as the Machine A checkout, and `/Users/ghilmanislam360/Documents/youtube-intelligence-os` as Machine B. Older audit `PREFLIGHT.json` and discovery `VALIDATION.json` record `machine: Ghilmans-Laptop.local`.
- Verdict: **this host is Machine A**, based on the host, user and path in those records. Folder names were not used.

## 2. Orphan `.rev` warning
File: `.git/objects/pack/pack-8d9357e755ad7b7ae3a2fa62a866d13502003c23.rev`, 21,984 bytes, created 2026-10-24 16:34:30 PKT.
- FRESH: valid RIDX header, internal checksum valid, a true permutation of 5,483 objects, and its embedded pack checksum equals the file name.
- FRESH: no `.pack` or `.idx` with that name, and none of the 20 current packs has that checksum. No copy found in the audit, archive, backup or recovery roots searched by name. No `multi-pack-index`.
- FRESH: `git fsck --full --no-dangling --no-reflogs` exit 0 with empty output.
- FRESH: `count-objects` also reports `garbage: 1`, which is this file.
- What removed the parent pack: UNKNOWN. No gc.log, and no record found.

**Verdict: cosmetic leftover of incomplete maintenance, with no integrity failure found.** The `.rev` holds offsets only and no object data.

Limit: the repo is a partial clone (`remote.origin.promisor=true`, filter `blob:none`), and fsck tolerates objects the promisor is expected to supply. `rev-list --all --missing=print` found 752 missing objects out of 28,135, across 17 refs. So local clean fsck does not prove these objects exist elsewhere. Those objects are checked against the independent mirror when it finishes.

## 3. Primitive Education scheduler
File: `out/PRIMITIVE_EDUCATION_SCHEDULER_RUNS.csv`. launchd `service inactive` timestamps match `runs` exactly (17 at 17:04Z, 20 at 18:32Z).

| Class | Of first 17 | Evidence |
|---|---|---|
| Actual research work | **0** | no scheduled run produced accepted output |
| BUSY exit | 3 | logged; one was a full worker costing $0.311 |
| Usage WAIT logged | 1 | logged |
| Usage WAIT silent | 10 | INFERENCE: no log line, and the only silent path in `pe_continue.sh` is the next-wake gate |
| Source-access failure | 2 | runs 14 and 15; both exited 0 |
| Supervised test | 1 | haiku test |

Runs 18 to 20 were 1 silent wait and 2 BUSY.

**Downloads blocker: not verified fixed.** Last scheduled-context evidence (12:54Z) is BLOCKED on all 4 held-out sources. Interactive session 85559743 could read them and did the held-out work. The 2 later BUSY runs did not test source access. TCC as the cause is still INFERENCE: the block hung in `open()`, the files are not dataless, and no matching tccd record was found in the one 10-minute window searched.

Design gap: `pe_continue.sh` checks only that the directory exists, so it starts a costly worker that then finds the files unreadable.

## 4. Exact-hash comparison
Target list of 5,767 forensic hashes: **not identified on this Mac yet**. Comparison below uses the manifests that are here.

| Target | Result |
|---|---|
| Machine B manifest identities, 1,000 unique hashes | 988 hash-verified here; 12 not found |
| Machine B media master (PR #41) | 456 rows, 455 unique hashes, all verified here |
| Oct 26 "not hash-matched" rows, 370 | **358 now verified here**; 12 not found |
| Research Export 5,373-file set | Original folder absent; rows have no content hash in the file used. Remains unresolved |

- Where the 358 were found: `yios-finance-machine-a/research/finance-economics-intelligence` 331, canonical `data/` 19 (`extracted` 16, `normalized` 1, `manifests` 1, `raw` 1), `yios-private-backups/machine-a-ownership-2026-10-20/remote-finance-records` 8.
- The 12 not found are Machine B Finance/NICK files (older `VIDEO_AUDIT_966.jsonl`, `FINANCE_1612_COMBINED_INTELLIGENCE.xlsx`, `NICK_INVESTS_CHANNEL_INTELLIGENCE` support files). Status on Machine B: UNKNOWN.
- A hash found here means same bytes here. It is not an independent backup. Nothing was copied.

## 5. Channel status seen so far (FRESH, moving)
- **Casually Finance, Video006 (`xtqbRt94TTw`):** Codex released its own lock at 17:08:40Z; this audit did not touch it. Remote is at checkpoint T `4d625184`. **U `df22c7e0` and V `9c2685f1` are local only**; the handoff records U pushes rejected by `commit_refs_rules`. 0 of 35 videos fully certified; actual listening 0 seconds; `CT_SCAN_COMPLETE=false`.
- **Primitive Education:** 15 selected videos, all `VISUAL_ANALYSIS_PARTIAL`. Held-out evaluation scored; reconstruction tests still moving; checkpoint I being published at the time of reading. Listening is `BLOCKED_CAPABILITY`.
- **Barely Evolved:** published up to N17 `bf6522a5` at 18:34Z, lock released 18:35Z. 3 deep-scan videos. The N15 hint is already stale.
- **xkcd What If:** 32 selected videos built by earlier handoff; checkpoints up to N at 17:01Z; `pop6` work followed. Its own lock `.xkcd_writer_lock` is present, heartbeat last 15:59Z. Whether it is still active: not yet checked.
- **Finance:** remote PR #36 head `f115285b`. Machine B writer per the Oct 29 handoff. Current Machine B state UNKNOWN.

## 6. Hosted CI
- FRESH, **Finance PR #36 (`f115285b`)**: ruff passes, tests 462 passed and 1 skipped; failure is the last step: `Unapproved tracked database(s): data/knowledge/reference_knowledge.db`. The allowlist in `.github/workflows/validate.yml` names only 2 DBs. Targeted fix scope: decide whether that DB should be tracked, then either add it to the allowlist or untrack it.
- 7 runs on that branch failed from `0df91c58` on; the previous runs passed through `78871b87`.
- PRs #37, #38, #39, #41, #43 and #44 also show failure, but their logs were not retrievable: `log not found`. Cause: UNKNOWN until re-run or reproduced.
- 10 of 17 open PRs show success on their last run, which is old. Hosted green is not local green.
- Main's last hosted run in the list is 2026-10-10.

## 7. Concurrent changes, not caused by this audit
- 17:08:40Z Codex released the Video006 lock.
- `.pe_writer_lock` is held by session 85559743 (heartbeat 18:30:58Z).
- Barely Evolved lock transfer 18:15Z, release 18:35Z.
- The remote received pushes during the audit (`pushed_at` 18:34:36Z).
- Pack `.pack` mtimes of 2026-11-05 17:00Z changed before this audit's fsck; cause UNKNOWN.
- This audit made no pushes, merges, fetches into the canonical repo, or lock operations.
