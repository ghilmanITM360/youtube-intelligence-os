# Implementation Roadmap

Effort: S ≤ 1 day, M 2-5 days, L 1-2 weeks (agent-assisted). Priority: **C** Critical, **H** High, **M** Medium, **O** Optional. **Gate 0:** the owner authorizes V2 Explorer work and AGENTS.md rule 12 is amended to scope it. Stages 1-2 are useful even without Gate 0; stages 3-7 need it.

## Stage 1: Repository and architecture foundation

| ID | Task | Pri | Source branch | Deps | Effort | Approach | Deliverable | Risks | Acceptance | Tests |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | Back up local-only evidence off-device | C | `preservation/stash0-untracked-LOCAL-ONLY`, `~/YIOS-local-audits` | external drive (owner) | S | copy + checksum | verified copy | none; owner hardware blocked (START_HERE) | sha256 match | checksum diff |
| 1.2 | Commit untracked work | C | working tree, yios-senior-health worktree | — | S | branch + commit | 2 branches | — | `git status` clean | — |
| 1.3 | Drop duplicate gate commit, fast-forward main | H | current branch | — | S | reset local branch to origin (owner-approved) | clean branch | losing work if misidentified | 90f9cd22 content ⊂ main | diff check |
| 1.4 | Merge low-risk PRs | H | #52, #49, #24, #22; rerun CI then #38 #39 #43 #41 | — | S | GitHub merge | merged PRs | — | CI green | CI |
| 1.5 | Land finance CI gates | C | #45 | #36 or replay | M | retarget/replay 6 commits | gates in CI | AGENTS.md conflict | CI fails when a reference annex is removed | `test_ci_workflow_gates.py` |
| 1.6 | Decide and implement the DB policy (builder + manifest) | C | #36, #50, finance-complete | — | M | commit builders, gitignore DBs, add hash manifest + validator | policy doc + validator | rebuild nondeterminism | builder reproduces recorded hashes | new validator test |
| 1.7 | Unstack Senior Health from the finance lineage | H | current branch, #50 | 1.6 | M | cherry-pick exclusive commits to a branch off main | clean SH PR | missed commits | `git cherry` shows all accounted for | CI |
| 1.8 | Archive stale, delete merged and orphan refs | M | 26 refs | owner OK | S | tag then delete | ~25 live branches | deleting unique work | each deleted tip contained elsewhere or tagged | containment script |
| 1.9 | Small code fixes A5, D2, package layout | M | main | — | S | refactor | PR | ledger-pinned files (D3) need re-pin | pytest green | pytest |

## Stage 2: Data architecture

| ID | Task | Pri | Deps | Effort | Approach | Deliverable | Acceptance | Tests |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Read-model schema | C | 1.6 | S | SQL file + doc | `schemas/read_model/001.sql` | covers every screen field | schema test |
| 2.2 | `build_read_model.py` (dedupe, crosswalk, normalized type, snapshots, source precedence) | C | 2.1 | L | stdlib sqlite3, read sources `mode=ro` | builder + `build_meta` | 10,553 unique videos at current data; 0 rows without a source; enum-only `video_type` | invariant tests |
| 2.3 | Flatten intelligence artifacts + plans into `insight` / `plan` | H | 2.2 | M | parse JSON envelopes | tables | every insight has evidence_layer + as_of | fixture tests |
| 2.4 | Workstream + evidence map + seal import | H | 2.2 | S | parse consolidation CSVs | `workstream` tables | numbers match START_HERE | snapshot test |
| 2.5 | API contract (OpenAPI doc) | H | 2.2 | S | write the contract first | `docs/api/read-api.yaml` | reviewed by owner | contract tests later |
| 2.6 | M0 spike: Datasette on read model | M | 2.2 | S | `uvx datasette yios_read.db --host 127.0.0.1` | demo | owner can browse/search | manual |

## Stage 3: Design foundation

| ID | Task | Pri | Effort | Deliverable | Acceptance |
|---|---|---|---|---|---|
| 3.1 | Validate personas/journeys with the owner (30-min review of USER_RESEARCH) | H | S | updated personas | owner sign-off |
| 3.2 | Tokens + validated palette (light/dark) | H | S | `tokens.css`, validator output | dataviz validator PASS both modes |
| 3.3 | Wireframes for S1, S4, S5, S7 (clickable HTML prototype on real read-model data) | H | M | prototype | owner completes the 4-click task |
| 3.4 | Component kitchen sink | M | M | page | all components in light/dark/forced-colors |

## Stage 4: Core experience (M1, read-only)

| ID | Task | Pri | Effort | Acceptance | Tests |
|---|---|---|---|---|---|
| 4.1 | Read API (GET-only, localhost) | C | M | all M1 endpoints; responses carry `as_of`, `sources`, `evidence_layer` | contract tests |
| 4.2 | App shell, routing, URL state, search | C | M | deep links reproduce views | Playwright |
| 4.3 | Home, Niches, Channels list | C | M | S1-S3 acceptance | Playwright + axe |
| 4.4 | Channel page (Overview, Videos, Intelligence, Plans tabs) | C | L | S4 acceptance | Playwright + axe |
| 4.5 | Video page (no forensics) + provenance drawer | C | M | ≤ 2 clicks to source | Playwright |
| 4.6 | Plan document + Plans index + export MD/PDF | H | M | "not framework-guided" label works | snapshot |

## Stage 5: Visualization (M2)

| ID | Task | Pri | Effort | Acceptance |
|---|---|---|---|---|
| 5.1 | Chart wrapper (Plot) with tooltip, keyboard, table toggle | H | M | every chart passes axe; table toggle |
| 5.2 | Strip plot + brush cross-filter (V5) | H | M | brush filters table |
| 5.3 | Coverage heatmap (V8), Compare small multiples + dumbbell (V10) | H | M | no dual axis; fixed entity colors |
| 5.4 | Workstreams pages (V13-V14), Knowledge (V18), Evidence Library (V19-V20), System (V21-V22) | M | L | S9-S12 acceptance |
| 5.5 | Forensics timeline (V15) with media library | M | M | local-only media message when absent |

## Stage 6: Advanced (M3, each needs a separate owner OK)

| ID | Task | Pri | Effort | Note |
|---|---|---|---|---|
| 6.1 | Review queue "mark reviewed" (append-only review store) | M | M | CANONICAL_MUTATION tier; reviewer + date recorded |
| 6.2 | Dry-run refresh trigger | O | S | SAFE_DERIVED tier |
| 6.3 | "Copy agent prompt" with entity IDs | O | S | no LLM calls from the app |
| 6.4 | My Channel (first-party) | O | M | only after a real export exists; local-only |
| 6.5 | Remote/phone access | O | M | requires an auth + privacy decision first |

## Stage 7: Validation and optimization

Functional + regression (pytest, contract, Playwright on every PR); cross-device (desktop, iPad width, 375-px phone); accessibility (axe 0 serious, keyboard walk-through, screen-reader spot check with VoiceOver); performance (FCP < 1 s, strip plot with 6k points < 100 ms interaction); usability (owner completes 5 core tasks unaided); production readiness (`uv run` one-command start on both Macs, stale-build banner verified).

## Quick wins vs large changes

- **Quick (≤ 1 day each):** 1.1, 1.2, 1.3, 1.4, 1.8, 1.9, 2.6, 3.2.
- **Large:** 1.6 DB policy, 2.2 read-model builder, 4.4 channel page, 5.4 secondary screens.
