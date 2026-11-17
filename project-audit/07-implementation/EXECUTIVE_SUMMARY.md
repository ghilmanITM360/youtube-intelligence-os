# Executive Summary: YIOS Multi-Branch Audit and Explorer Strategy

Date 2026-11-17 · Baseline `origin/main` @ `e96f7f8f` · Read-only audit: nothing was merged, pushed, deleted, migrated or written to any database. The only repository change is this new `project-audit/` folder (uncommitted).

## What the project is

YouTube Intelligence OS is a private evidence engine. It collects competitor YouTube data, records where every fact came from, analyses it in five deterministic intelligence layers, and produces content plans that separate facts from AI readings. It has **no user interface, API or server**. The owner reaches its knowledge through AI agents and generated PDF/HTML reports.

## What the audit found

1. **75 branches** (37 local, 68 remote), 45 PRs (23 open), 10 worktrees. 20 branches are fully merged; 3 are stale; 3 are orphan test refs. Two long stacked lineages (Finance ~210 commits, Casual Finance ~243) hold most unmerged work.
2. **No branch contains UI or API code.** The only frontend-like code is demo compositions and generated reports.
3. **Data is fragmented across 7 SQLite stores**, 4 of them only on branches, with **10,553 unique videos** but 12,907 rows. Three channel-ID schemes are in use, and `video_type` has 5+ spellings. This, not missing intelligence, is the main blocker for any UI.
4. **The strongest asset is honesty:** evidence layers, explicit `NOT_AVAILABLE` (56% of coverage cells), validators, hash-pinned provenance. Any UI must preserve it.
5. **Risks:** about 843 MB of evidence exists only in a local stash; about 15 GB of frames/audio are on one Mac; finance quality gates are still missing from main's CI (fixed on PR #45); 6 PRs' CI failed before any step ran; #36 and #50 fail the database allowlist.

## What to build

- **Platform:** a **local, responsive web app (the Explorer)**, desktop-first with a phone layout. Native mobile is not recommended: dense data, local-only media and private analytics all argue against it.
- **Architecture:** one new derived, rebuildable **read model** (`yios_read.db`) that dedupes all stores; a **GET-only localhost read API** that serves the UI and agents alike; a Vite/React/Observable Plot frontend. A one-day **Datasette spike** comes first to validate the read model.
- **Experience:** Home → Niches → Channels → Videos, plus Compare, Plans, Workstreams, Knowledge, Evidence and System. Every value shows its evidence layer, as-of date and a 2-click path to its source.

## Decisions needed from the owner

1. Authorize V2 Explorer work and amend AGENTS.md rule 12 (Gate 0).
2. Choose the database policy (recommended: commit builders + hash manifests, gitignore the DBs).
3. Provide off-device backup for local-only evidence.
4. Approve the merge/cleanup sequence in `01-repository-audit/BRANCH_INTEGRATION_STRATEGY.md`.

## Quality-control checklist

| Check | Status | Evidence |
|---|---|---|
| All repositories identified | ✔ | 1 remote, no submodules; 10 worktrees listed; other folders (e.g. `~/workprojects/*`) are cited in START_HERE but were not inspected |
| All local and remote branches inventoried | ✔ 75/75 | BRANCH_INVENTORY.md (generator asserts every branch is annotated) |
| Every branch individually examined | ✔ at commit/file/diff level | INDIVIDUAL_BRANCH_AUDIT.md. Line-by-line code review was limited to code-bearing branches' diffs; per-branch test suites were **not** run locally |
| Inaccessible branches documented | ✔ none inaccessible | fetch succeeded; orphan refs flagged |
| Branch differences / missing features | ✔ | BRANCH_COMPARISON.md, MASTER_FEATURE_INVENTORY.md |
| Feature inventory consolidated | ✔ 38 features | MASTER_FEATURE_INVENTORY.md |
| System modules analyzed | ✔ | SYSTEM_ARCHITECTURE.md, MODULE_DEPENDENCY_MAP.md (AST scan) |
| Data entities and relationships | ✔ 7 stores, 71 tables | DATA_DICTIONARY.md, DATABASE_RELATIONSHIPS.md |
| Every data category mapped to UI | ✔ 25 datasets | DATA_TO_UI_MAPPING.md, visualization matrix V1-V25 |
| User tasks and flows evaluated | ✔, hypothesis-level | USER_RESEARCH.md: **no owner interview yet** (task 3.1) |
| Visualization choices justified | ✔ | COMPLETE_DATA_VISUALIZATION_STRATEGY.md; palette not yet validated (task 3.2) |
| Web vs mobile compared | ✔ | PLATFORM_SELECTION_REPORT.md |
| Future architecture documented | ✔ | PROPOSED_TECHNICAL_ARCHITECTURE.md |
| Roadmap actionable and prioritized | ✔ | IMPLEMENTATION_ROADMAP.md, PRIORITY_MATRIX.md |
