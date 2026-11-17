# YIOS dual-machine coordination implementation plan

**Goal:** Deliver the owner's specified CLI in the existing repository without changing accepted research or legacy ownership.
**Architecture:** Python standard library plus Git. Durable per-task remote state branches contain only coordination metadata. Each transition is a new single-parent commit built from the exact observed state; concurrent transitions diverge and normal pushes reject the loser. Slots are never deleted. Task evidence remains on separate ordinary research branches. Canonical integration has its own exclusive slot and existing Finance validators.
**Spec:** Owner's 2026-10-30 master implementation request in this chat. Explicit implementation/publication authorization supersedes an additional design approval round.

## Choices and boundaries

Atomic ref creation alone is insufficient for safe release/reacquisition. An append-only state history avoids deleted-ref ABA races. GitHub issue comments/shared JSON edits cannot provide exclusion. No lease timeout or heartbeat takeover; no force push. This is cooperative writer exclusion, not a security boundary against collaborators bypassing Git tooling. Server rules and actual second-Mac verification remain distinct gates.

Production Finance remains MACHINE_B_SOLE_WRITER_ACCEPTED; Video003 remains protected until its writer's published release. No production claims, audit acceptance, canonical rebuild, research PR merge or ownership migration is performed during implementation. Isolated fixtures exercise integration. Remote smoke tests use a clearly labelled non-production namespace.

## Tasks

- [x] Record live Finance/PR/protected branch heads, ledger counts, source hashes, worktrees/stashes and media limitations. Preserve stale root checkout.
- [x] Write failing real-Git tests for simultaneous claims, separate videos, stale states, wrong-owner release, release/reacquisition, remote failures and protected legacy gates. Implement durable coordination protocol.
- [x] Add start/save/switch/resume/status with explicit file allowlists, validation and source/media hashes, verified remote checkpoints and UNSYNCED preservation. Test two independent working contexts and push failure.
- [x] Add serialized integration from verified task checkpoints using exact canonical base, target-only assertions, existing JSONL/CSV builder, workbook structural verification and all Finance acceptance checks. Test two packets in fixtures, duplicates and stale canonical conflicts. Add bounded Visual Forensics registration preserving existing accepted records.
- [x] Add concise channel evidence navigation and media verification. Independent agent loads Casually Finance and produces an original storyboard with evidence/interpretation/adaptation separated.
- [x] Run full repository tests, Finance tests/validators, formatting tests, local two-client tests and live GitHub protocol smoke. Record exact results and limitations. Review diff, publish implementation branch normally and verify remote SHA.
- [x] Provide real second-Mac acceptance commands; mark inaccessible Machine A NOT_TESTED. Keep legacy migrations BLOCKED until actual releases and acceptance gates are met.

## Review focus

Network errors never mean an absent claim. Missing source bytes or LFS pointers never mean recovered media. No task checkpoint may change shared canonical files. A stale base cannot publish integration. Partial research cannot become accepted merely by pushing. An idle writer never implies release. No automatic reset credits, paid spending, destructive Git operations or unbounded lazy fetch.

## Recorded acceptance

See research/coordination/validation/2026-10-30-implementation-validation.json.26focused tests,38Finance tests,2formatting tests and both validators pass. Full repository:485passed,1skipped,1pre-existing provenance-checksum failure. Live GitHub isolated protocol:7checks pass. Actual two-Mac acceptance and legacy migration remain NOT_TESTED/BLOCKED. Publication is verified separately by exact remote SHA; no research acceptance is added.
