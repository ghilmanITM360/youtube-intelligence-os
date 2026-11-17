# Finance and CT handoff: alternating-worker protocol (v2, 2026-11-02; NOT executed)

Supersedes v1. Owner correction: Machine A and Machine B are both read/write workers. Ownership belongs temporarily to an active task/session, not to a machine. There is no permanent sole writer. Nothing below has been executed, pushed or transferred.

## Live state (fetched 2026-11-02)
| Item | Value |
|---|---|
| Finance canonical `research/finance-economics-intelligence` | `223f4498` (461 accepted), unchanged |
| Machine A branch `codex/finance-machine-a-owner-directed` | `9c6f42fb` (554 accepted), last accepted `NICK_278`, last commit 2026-11-02 01:02 +05:00 |
| Latest live queue next unaudited | `pTyMmSZ2EVs` (`NICK_279` is not accepted at this head; re-read the queue at takeover, do not assume the ID) |
| `main` | `08e71926`, unchanged |
| Finance ownership record | Latest entry is "Owner-directed Machine A execution, 2026-10-31". It has **no published release**. Machine B's earlier entries are untouched provenance |
| Candidate (local review artifact) | `candidate/finance-integration-2026-11-02` `554a8335`, validated: full tests 462 pass/1 skip, Finance 50, Node 2. Unpushed |
| Repair commit | `cd2160f9`, unpushed, independent of ownership |

## Finance: current owner and gate
- **Current owner: Machine A task/session (owner-directed, 2026-10-31).** It has not published a release. I cannot see whether a Machine A session or scheduler is running now, and a local lock on this machine proves nothing about Machine A.
- **Gate not met:** step 5 of the incoming checklist (previous writer released the stream) is unconfirmed. This machine does read-only Finance work until it is.
- No exclusion is placed on either machine afterwards. This machine may become the next writer after verified release, sync and acceptance, and Machine A may take over again later.

### Outgoing worker (Machine A) must
1. Finish or checkpoint the current atomic operation (no half-accepted batch).
2. Validate and push the Finance branch normally. Publish the exact checkpoint: full SHA, accepted count, completed/pending IDs, ledger/workbook/JSONL hashes, and the next operation read from the live queue.
3. Preserve incomplete work with an explicit status. Name any non-Git evidence and where it can be fetched.
4. Publish a documentation-only release entry in `FINANCE_WRITER_OWNERSHIP.md` (a coordination record, not a lock), then stop canonical writes.
5. Disable or pause its own scheduled Finance runs while the handoff is open. It re-enables them after reacquiring ownership. No second scheduler is created.

### Incoming worker (this machine) steps
1. `git fetch origin`; read the newest handoff and the ownership file at the live head.
2. Preserve local work: `candidate/…`, `repair/…`, the local branch bundle, the stash (1 entry) and recovery refs stay as they are.
3. Synchronize safely: fast-forward only (the merge base equals canonical head, so no conflicts). Apply `cd2160f9`, then compare the result with candidate `554a8335`.
4. Verify evidence: re-run `scripts/reconcile_finance.py`, validators and tests. Expect 554 accepted and 462 pass/1 skip, or the new live equivalents.
5. Confirm the release entry exists and the live Machine A head matches the published checkpoint.
6. Publish acceptance (UTC time, host/user/root, SHAs, local/origin/PR #36 equality) using the existing protocol.
7. Re-fetch after acceptance. If the head moved, repeat the checks.
8. Continue from the live queue's next unaudited video. Do not redo accepted IDs.

If Machine A is still writing, keep its ownership and do independent read-only work.

### Do not
Re-audit the 93 overlap IDs, edit the frozen `FINANCE_UNIVERSE.csv`, change the two pinned `.gitattributes` ledger rows, drop the NICK_260 correction, or call any limited-evidence audit full-evidence. Do not force-push, reset or rebase.

## CT (Visual Forensics): recovered state
- Owner stream: the Machine A scheduled task `yios-visual-forensics-machine-a` and `~/YIOS-local-audits/vf_lock.sh` lock state. Not observable from this machine. This machine has no scheduled tasks (confirmed), so there is nothing here to edit and no duplicate to create.
- Published checkpoints (`research/casually-finance-editing-forensics` @ `f067ad22`, 2026-11-01 23:15 +05:00): Video 005 `-X6YzlY_8tM` is at **checkpoint J** (status `VIDEO_005_PARTIAL_STRUCTURE_SECOND_PASSED`).
- Published next operation: queue position 6, `xtqbRt94TTw`. The Video 006 handoff, checkpoint manifests and reviewer outputs are **not in Git**. They are the "checkpoint B" Machine A holds locally.
- Evidence readiness for Video 006: **not ready.** Reviewer outputs must not be rebuilt from summaries. If Machine A's checkpoint B is still current, continue from its next pending operation.
- Fetch from Machine A, over an authorized transfer path, before resuming: handoff, checkpoint manifests, shard map, `OUT_shard_*.json` and validators, the referenced source imagery, and the lock record. Then hash-verify against the manifests. The request file lists exact rows, with unmeasured sizes and hashes marked UNKNOWN: `CT_TRANSFER_REQUEST.md`, `CT_TRANSFER_REQUEST_video005_-X6YzlY_8tM.csv`, `CT_VIDEO005_CHECKPOINT_MANIFEST_ENTRIES.csv`.
- The Machine A outgoing worker publishes a release (checkpoint, SHA, pending shards, lock freed, scheduler paused). This machine then acquires the lock under the existing `vf_lock` protocol and re-reads the checkpoint.

## Scheduled-task instructions
- This machine: none registered, so nothing to change.
- Machine A's task prompts must read live ownership at start and skip when another machine is the owner. That edit has to be made on Machine A through its scheduler controls. Suggested text is in the report. No scheduler is created here.

## Independent work not blocked
The repair commit `cd2160f9` can land on canonical on its own. CI billing is separate and hosted CI stays failing until the billing owner acts.
