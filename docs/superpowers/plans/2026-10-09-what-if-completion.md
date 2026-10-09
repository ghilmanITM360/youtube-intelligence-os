# What If Completion Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline execution. Owner explicitly authorized implementation and routine decisions without additional design approval.

**Goal:** Complete source-fixable What If integration and publish verified changes through guarded merge commits.

**Architecture:** Preserve read-only canonical source adapter and immutable catalog history. Extend staging with a stable creation receipt, validate promoted rows before querying them, and attach compact source-backed editing guidance to production plans. Keep unknown or unregistered sources held.

**Tech Stack:** Python 3.12, SQLite, JSONL, GitHub CLI.

**Spec:** Owner completion request dated 2026-10-09 and WHAT_IF_FORENSIC_SOURCE_CONTRACT.md.

## Global Constraints

No raw source mutation, title-based identity registration, paid acquisition, independent-sample inflation, silent overwrite, or history rewrite. All evidence references retain table, row, video, release and confidence. Preserve existing snapshots and transcripts.

## Review Focus

- Tampered staged data must fail closed.
- Missing local staging must report unavailable without inventing evidence.
- Partial/malformed timing must not create false pacing metrics.
- Relocated repository/corpus must resolve relative references.
- Empty or other-channel samples must not receive What If recommendations.

### Task 1: Canonical promotion and identity evidence
- [x] Review exact PR #11 head, green CI, guarded merge and refresh.
- [x] Attempt official uploads acquisition authorization discovery; document unavailable API authorization/implementation blocker. No videos registered without evidence.
- [x] Investigate ID-less sources using independent content evidence; preserve holds without sufficient proof.

### Task 2: Durable staging lifecycle
Files: scripts/stage_what_if_forensics.py, tests/test_stage_what_if_forensics.py.
- [x] Test creation timestamp/checksum receipt, stable second run, drift rejection.
- [x] Implement durable ignored staging with generated receipt.
- [x] Verify live corpus CREATED/UNCHANGED and portable root.
- [x] Commit, push, PR, CI and guarded merge.

### Task 3: Editing evidence consumption
Files: scripts/query_what_if_forensics.py, scripts/run_youtube_intelligence.py, tests/test_query_what_if_forensics.py.
Interface: query_evidence(stage_dir, catalog_path, index_path, video_ids=None) returns compact per-video metrics, source references and hypothesis recommendations.
- [x] Add failing tests for source-backed shot pacing, all eight table coverage, held exclusion, tampering and missing-stage behavior.
- [x] Validate stage/index agreement before querying. Compute measured durations only from valid finite timing; preserve source-declared confidence and distinguish recommendations as hypotheses.
- [x] Attach relevant query output to production plan editing blueprint; keep channel sample counts separate.
- [x] Verify full suite and source-backed production output, publish and guarded merge.

### Task 4: Documentation and safety
Files: README.md, docs/Architecture.md, docs/WHAT_IF_FORENSIC_SOURCE_CONTRACT.md, docs/WHAT_IF_INTEGRATION_WORKFLOW.md, PROJECT_STATUS.md, docs/audits/WHAT_IF_REPOSITORY_SAFETY_2026-10-09.md.
- [x] Document validation, stage, diff, promotion, update, rollback and identity-refresh blocker.
- [x] Classify every pre-existing tracked media/frame/private finding without deleting required evidence or rewriting history.
- [x] Run CI-equivalent checks and final end-to-end flow; publish and guarded merge.
- [x] Verify created-branch/worktree cleanup procedure and report exact acceptance results, blockers and usage after canonical publication.

## Verified execution results

PR #11 merged as `e43e2d9312608c3143d04b74530f78083dda399c`; PR #12 as `3c2fa06efd7aa48ba1ebca968264c00cd13d6656`. PR #13 exact head `89e2acb60e976c5aeba2a4994754c0392fa1222e` passed CI and independent review before guarded merge. Final local suite: 438 passed, one skipped, five pre-existing warnings. Portable-root end-to-end reproduction: CREATED then UNCHANGED for stage and promotion; 8,327 unique accepted observations, 3,258 held, zero rejected; catalog checksum unchanged; integrity ok and zero foreign-key violations. Production example consumes 2,381 observations from four existing videos with 24 hypotheses; reviewer validated all 1,144 grouped citations. Static, secret, ledger, registry and disposable-rebuild checks pass.

Canonical registration remains externally blocked: no available YouTube Data API credential and no existing official acquisition implementation. Two verified-but-unregistered IDs and two unresolved media identities stay held. No paid fallback, source mutation, raw-media addition, private-export addition, historical-snapshot overwrite or history rewrite occurred. All historical safety findings have per-file classification; required owner decisions remain documented.
