# Project timeline

Audit date: 2026-10-16. Sources: `git log` (committer dates, local UTC+05:00 unless noted), `gh pr list`, `gh run list`, repository handoff files. Filesystem modification dates were not used. Commit dates prove when a commit was made, not when the underlying research was done.

## Foundation to V1 (main branch)

| Date | Event | Evidence |
|---|---|---|
| 2026-08-27 | Repository initialized (`b427956`); Phase 0, 0.5, 1A inventory catalog and DS-000001 ingest the same day | `git log --reverse` |
| 2026-09-01/02 | Legacy transcript provenance fixed; DS-000001 eligible classifications completed | `00ae52b`, `ec44b84` |
| 2026-09-08/09 | DS-000018 validation; thumbnail evidence and packaging analysis | `dcdbae2`, `e01505a` |
| 2026-09-11 | V1 capability gaps closed; V1 declared complete within evidence limits (15 commits that day) | `e29bd8f`, `3517edf`; AGENTS.md |
| 2026-09-12/13 | DS-000021 registered; DS-000025 funded channel extraction | `b69c214`, `a22c8d2` |
| 2026-09-22 to 09-26 | Senior Health acquisition and consolidation; PRs #1-#5 merged 2026-09-24/25 | gh PR list |
| 2026-10-03 | PR #7 canonical integration merged | `e43f97b` |
| 2026-10-09 | What If forensic integration PRs #8-#14 merged (source contract, adapter, staging, promotion, lifecycle, docs) | gh PR list |
| 2026-10-10 | PRs #15, #16 merged (doc entry points; identity evidence); PRs #17, #19, #18 merged 21:02-21:07 UTC | gh PR list |
| 2026-10-11 | `main` last advanced: `08e7192` at 02:07 (+05). Main CI success: 460 passed, 1 skipped. **No commit to main since.** | `git log main`; CI run on 08e7192 |

## Research and production branches (all unmerged)

| Date | Event |
|---|---|
| 2026-10-12 | PR #25 (Casual Economics), #21 (Casual Finance forensics, updated 10-13), #22 (local reconciliation), #24 + issue #23 (legacy thumbnails, deferred), #26 (Dr Rehan test videos) opened |
| 2026-10-13 | Issue #27 and PR #28 (Casually Finance playbook); PR #29 (Finance Short 01) opened and later closed unmerged |
| 2026-10-14 | PR #30 Finance Short 02 (V3 polish committed); PR #25 marked ready: head `fce8167`, 11/11 structural packages, AV sign-off 0/11 |
| 2026-10-15 | Issues #31, #33, #35; PRs #32 (Dr Rehan, through V3 upload candidate `c867af8`), #34 (three senior-health videos, V1-V3 over the day), #36 opened |

## Finance & Economics (PR #36, branch `research/finance-economics-intelligence`)

| Commit (date +05:00) | Milestone |
|---|---|
| `03a6cd0` (10-15 23:26) | Knowledge consolidation: 5,976 locators, YOUTUBE_KNOWLEDGE_READY, Phase 2 readiness |
| `ef02fad` (10-16 00:05) | Canonical baseline: 13 channels, 966 videos, coverage tables, validator, tests |
| `29532c5` (10-16 00:26) | Sampled intelligence, six-channel landscape, first RESOURCE_CHECKPOINT (93% five-hour / 41% weekly) |
| `31d6042` (10-16 07:05) | Matched script reads, 30 semantic title reviews |
| `505f032` (10-16 07:25) | Source scrape dates recovered for 595 DS-000022 records; ranking extends 176 to 723; Drive triage |
| `53db0e6` (10-16 07:27) | Scenario-arithmetic audit; second RESOURCE_CHECKPOINT (89% / 29%). CI run 38840548627 on this exact SHA: **success** (completed 02:30 UTC, 460 passed, 1 skipped) |

Note: the three later commits are timestamped 07:05-07:27 local; the 6.5-hour gap after `29532c5` is the first resource interruption followed by an explicit continuation. The PR #36 body is current; `knowledge/youtube/HANDOFF.md` still lists `03a6cd0` as a historical checkpoint.

## Production (senior health, PR #34)

V1 package committed 2026-10-15; V2 (corrected captions, claims framing) and V3 motion correction (two-leg gait, alternating crawl, red headline) committed 2026-10-15 to 2026-10-16. Swimming V3 `65caa88` on 2026-10-16 closed the three-video set. Frame-by-frame QA only; nobody has watched at playback speed.

## Interruptions and blockers

- Resource checkpoints: 2026-10-16 00:26 (93%/41%) and 07:27 (89%/29%) on the Finance branch; PR #30 earlier stopped at 96% five-hour; senior-health V3 deferred on a five-hour budget on 2026-10-15 22:31, resumed 2026-10-16 01:34.
- Resolved: DS-000022 scrape dates; the two Drive finance exports reconciled; CI on the PR #36 head.
- Unresolved: DS-000001 date/format provenance; 936 semantic reviews; emerging-channel cohort; owner approvals for every open PR; clinical review of health videos.

## Last validated checkpoint

Branch `research/finance-economics-intelligence` at `53db0e68fd7eecee9e26e0797383b779053859d7`: CI success; `validate_research.py` PASS_BOUNDED_RESEARCH_NOT_PHASE_COMPLETION; knowledge validator 0 errors; secret scan 0 findings; `git diff --check` clean (all re-run in this audit).
