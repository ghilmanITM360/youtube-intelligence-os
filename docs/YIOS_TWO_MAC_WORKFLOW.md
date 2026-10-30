# YIOS on either Mac

The tools are implemented and tested with independent clients. Production migration is **BLOCKED** until the legacy writer explicitly releases and both actual Macs pass acceptance. Machine B's Finance authority and Video003 protection remain in force. Do not start a new audit to test coordination.

## Install the same tools on each Mac

Use the existing repository and a clean implementation worktree at branch `codex/yios-dual-machine-coordination`. Preserve old worktrees, stashes, untracked/ignored media and branches. Inspect `git status --short`, `git worktree list`, `git stash list` and `git ls-remote origin` first. Fetch only the explicit implementation branch; no reset, force update, rebase or blind pull. Verify its published SHA before using it. Machine A's checkout is `/Users/ghilmankhan/workprojects/youtube-intelligence-os`; Machine B's is `/Users/ghilmanislam360/Documents/youtube-intelligence-os`.

Set an alias to the **implementation checkout's** launcher, not an older task branch:

```sh
alias yios='/absolute/path/to/implementation-checkout/bin/yios'
export YIOS_PYTHON='/absolute/path/to/python3.12'
yios setup machine-b
yios status
```

Use `machine-a` on A. `bin/yios` anchors imports to its own checkout, so it works while your current directory is an older research/task worktree. Python3.12–3.13, Git, Git LFS, and the repository's openpyxl/Pillow dependencies are required; Finance integration additionally needs Node22–24 and authenticated `gh` for PR36 verification. No extra service/database/account is introduced. No credits are redeemed or purchased.

## Status and safety

`yios status` reads the **live Finance branch**, computes ledger counts and next untouched original ID, and reports claims, local publication state, protected research, worktrees and media limits. Network errors are blockers, never evidence that a task is unclaimed. It does not silently synchronize the stale root checkout. Status's explicitly dated protected visual snapshot is not fresh reviewer certification.

Read the account meter before major work, then record those actual readings (example numbers must be replaced):

```sh
yios safety --five-hour 40 --weekly 25 --context AVAILABLE_UNMETERED --paid-credits 0
```

The CLI refuses missing/stale readings (>20minutes), five-hour>=90%, weekly>=95%, unavailable reserve, or free disk<5GiB. `AVAILABLE_UNMETERED` explicitly means an operator checked execution reserve but no context percentage was exposed. The CLI cannot read Codex/Claude subscription meters itself; supplying a number is an operator attestation, not a measured API result. Refresh this record before lengthy operations. It never purchases or redeems anything.

## Research, save, move

After migration and source recovery gates pass:

```sh
yios start finance XP-26tqGFXc --worktree /absolute/new-task-worktree
cd /absolute/new-task-worktree
# Edit research/tasks/finance/XP-26tqGFXc/CHECKPOINT.json and task artifacts.
yios save --files research/tasks/finance/XP-26tqGFXc/notes.md
yios switch-to machine-a
```

These are usage examples, **not permission to start NICK186**. `start` checks the live ledger and actual ownership first. `CHECKPOINT.json` records channel/video, source base and hashes, completed/remaining stages, continuation, media and exact artifact hashes. Keep each claim's six Finance dimensions and existing evidence qualifications. In-progress commits use PARTIAL/IN_PROGRESS; READY_FOR_INTEGRATION is a submission, never acceptance. No task writer edits the shared JSONL/CSVs/workbook.

On the receiving Mac, use the same alias, `setup`, fresh safety reading and `status`, then the same `start ... --worktree NEW_PATH`. The explicit released checkpoint is fetched and verified before resuming on a new claim-specific branch. Reverse A→B uses `switch-to machine-b`; all other steps are identical. A transfer is reserved for its named machine. Missing heartbeat/idleness is never release.

For visual work, supply `--media-manifest /private/path/media.json`. Its JSON array must contain the correct video/channel, `role: original-video`, local path, bytes, SHA256, private storage/object locator, rights/privacy, recovery status and restore procedure. `yios media manifest.json --required` verifies actual bytes. A matching local hash means LOCAL_ONLY, not tested private backup recovery. Restore the source, frames/audio and reviewer shards as required by the existing source contract. Video003 remains blocked even when its MP4 is present.

`save` accepts an explicit small-artifact allowlist under `research/tasks/<stream>/<video>/`, validates structured files/provenance, commits, normally pushes and checks the exact live SHA before updating ownership. No large MP4/audio/archives go into ordinary Git. Network/push failure leaves a reachable local commit and reports UNSYNCED. `yios recover` handles a lost acknowledgement only when token, writer, branch, checkpoint and artifact hashes exactly match the live state. It cannot adopt another writer. Inspect a genuine conflict; never overwrite it.

`yios release` releases a saved partial task without reserving a destination. A released READY_FOR_INTEGRATION submission is frozen against reacquisition, preventing a new researcher from racing canonical publication. Withdrawal/rework of a submitted packet is **not implemented**; obtain a reviewed explicit transition instead of deleting its claim ref.

## Canonical integration

After the legacy coordinator release is certified, either Mac can run:

```sh
yios integrate finance --task finance/VIDEO_ID_11 --expected-head LIVE_CANONICAL_SHA --worktree /absolute/new-integration-worktree --node /absolute/path/node
```

Repeat `--task` for independent ready packets. Each task must be published, explicitly released and frozen READY_FOR_INTEGRATION. The checkpoint's `integration_files` is an explicit list of `{ "source": "research/tasks/.../packet.json", "destination": "research/finance-economics-intelligence/audit-batches/BATCH.json" }`. Sources must appear in the checkpoint hash manifest. Existing canonical packet names cannot be overwritten. Packets can share an older source base only if it is an ancestor, every immutable fingerprint matches and their individual canonical target rows remain unchanged.

The exclusive integration claim is separate from video claims. Integration uses a fresh isolated canonical checkout; checks exact expected HEAD, identities, already-accepted IDs, source versions and all unchanged records; calls the existing builder; independently reconciles all7CSV projections; patches only target workbook cells/derived counters; preserves package parts, styles, formulas, tables, filters, dimensions and panes; runs the full Finance suite, formatting tests and both validators. It then commits/pushes normally, verifies live branch and OPEN/DRAFT PR36, reconciles task acceptance and explicitly releases the coordinator. No native Excel recalculation or hosted CI PASS is claimed.

The current adapter supports original966 packets. The remaining646 expansion videos need their existing canonical expansion review contract extended before deep acceptance; they are not silently mapped into the966ledger. CSV headers remain frozen; JSONL-only fields are not promoted. These are explicit adapter limits, not another ledger. Existing combined-workbook tests now derive completion from the canonical ledger with a461preservation floor, avoiding a hardcoded count that would reject the next real audit.

Visual integration uses `yios integrate visual-forensics ...`. It adds reviewed new small records only under the exact existing channel/video hierarchy, rejects every collision and requires a scoped VISUAL_ONLY `ACCEPTANCE.json` with limitations/reviewers. It cannot certify listening/fullAV or replace existing001/002/003research. The protected visual coordinator remains gated pending its legacy release. The current adapter rejects Video003 even after release: integrating its existing partial continuation requires a separately reviewed adapter; this implementation does not finish that research.

Failed integration retains its claim, isolated worktree and baseline, and prints an operationID. After inspection use `yios integrate-recover ID`: an already-published exact commit can be reconciled. If canonical is still exactly the original base, `--preserve-and-release` explicitly releases the coordinator while retaining every local failed output and published input packet. Local generated outputs are not falsely described as backed up. Retry using a new worktree and fresh expected HEAD. Diverged canonical state stays blocked for manual reconciliation.

## Remote protocol and limits

Each task uses `refs/heads/yios/claims/<stream>/<video>`, and each coordinator uses `.../integration/<stream>`. Only metadata is stored there; the accepted research ledger remains canonical. Initial contenders create unique orphan commits. Every subsequent transition has exactly the inspected remote state as its single parent and fresh nonce; concurrent changes are siblings. Normal Git ref updates accept one and reject the competing divergent commit. Slots are never deleted, preventing release/recreate ABA. Ref existence alone, arbitrary fast-forward pushes and expiry leases are not treated as locks. See [Git push rules](https://git-scm.com/docs/git-push) and [GitHub reference API](https://docs.github.com/en/rest/git/refs).

This is cooperative exclusion for authorized clients. A collaborator bypassing the CLI can still push directly with their existing repository permissions; no server-side security restriction was installed. Server enforcement and actual two-Mac certification are not inferred from fixture tests. Non-production `yios-test/...` refs are labelled tests, use fake IDs, contain no accepted research and remain auditable in RELEASED state.

## Actual second-Mac acceptance and migration

Machine A is inaccessible from this session: **NOT_TESTED**. Machine B local fixture/CLI verification is not a two-Mac certification. On each actual host independently:

1. Verify implementation remote SHA, clean preserved checkout, dependencies, current usage and >5GiB disk. Run `yios status`; confirm actual Finance head/count and protected003 without starting either.
2. Run `python -m pytest tests/test_yios_coordination.py tests/test_yios_checkpoints.py tests/test_yios_integration.py -q` and `python -m scripts.yios_remote_smoke --remote origin --output /private/tmp/yios-host-acceptance.json` from the tool checkout. Non-production refs only.
3. Perform one non-production partial checkpoint A→B and B→A using the smoke receipt's refs/commits; independently compare every published artifact and restore required private source bytes against original manifests. Never create fake accepted Finance rows.
4. Publish a reviewed host acceptance JSON in an implementation/acceptance branch with `machine`, status `REAL_MAC_ACCEPTANCE_PASS`, `simulated:false`, distinct real-host `hardware_id_sha256`, `protocol_tests_pass:true`, `checkpoint_restore_pass:true`, `media_gate_pass:true`, exact test/restore receipts and limitations. A single-host simulation must not supply these actual-host attestations.
5. The authorized legacy writer finishes/publishes its checkpoint, explicitly stops writes and publishes `research/coordination/releases/finance.json` on the Finance canonical branch (visual uses `.../visual-forensics.json` on its existing protected branch). Required fields: `scope`, `state:EXPLICITLY_RELEASED_TO_YIOS_COORDINATION`, `released_by`, `checkpoint_commit`, `continuation`, `implementation_commit` and `machine_acceptance` entries for machine-a/b containing verified `branch`, `commit`, `path` for those actual-host records. The reviewed implementation and generic workbook test must already be included in that canonical history. This file is **not created by this implementation**. Human owner authorization and the prior writer's published release must be reviewed; a JSON template alone is not a release.
6. New clients verify every remote release/acceptance object and ancestry before allowing legacy claims. Video003 also requires the exact protected checkpoint, shards/reviewer dispositions and source hashes; do not infer release from this document. Keep old authority enforceable until all gates pass.

No PR21/36/44 is merged. No existing source, research corpus, backup package or stash is deleted. The next research video is selected only after implementation/migration is resolved and fresh queue/ownership checks pass.
