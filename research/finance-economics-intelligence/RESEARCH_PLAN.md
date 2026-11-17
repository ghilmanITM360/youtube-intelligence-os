# Finance & Economics research execution plan

**Goal:** Evidence-linked competitive intelligence and an original channel pilot, on existing PR #36.
**Architecture:** Read-only SQLite and indexed Git blobs feed research-only CSVs; explicit analyst reviews and external source records feed reports. No canonical promotion or new infrastructure.
**Tech stack:** Python standard library, Git, existing validators, public web research.
**Spec:** User's Phase 2 mission dated 2026-10-16; scope boundaries in PHASE_2_READINESS.md.

## Constraints and rulings

One primary agent; existing branch/PR only; preserve untracked work and raw evidence. No API acquisition, paid scraping, forensics, production assets or merges. User explicitly requests immediate continuous execution: no additional plan approval/delegation gate. Publication dates, collection dates and ingestion dates are separate. Do not infer Shorts solely from duration. Missing or malformed dates cannot support age adjustment.

## Review focus

Missing snapshot/date → insufficient comparison; mixed formats → separate cohorts; identical transcript text → record duplicate family; small/zero-view peer groups → insufficient data; keyword labels → provisional interpretation, not observed semantic facts.

## Batches

- [x] Verify checkout, PR and exact-head starting CI; read central knowledge.
- [x] Baseline: build CHANNEL_UNIVERSE, VIDEO_MASTER, TRANSCRIPT_COVERAGE, THUMBNAIL_COVERAGE, TITLE_FEATURES, SCRIPT_FEATURES and BASELINE_COVERAGE; verify counts, source checksums and ranking edge cases. Commit/push.
- [x] Reuse: register immutable Casually Finance and Casual Economics report/data versions, retain their distinct ranking methods and QA limits.
- [ ] Packaging/scripts: stratify by channel, format and tier; deep-read selected scripts and review feasible mobile thumbnails with Video_ID association. Publish libraries and negative examples.
- [ ] Live evidence: selectively expand Tier B/C only for gaps; verify official YouTube rules and event/Trends provenance. No search snippet treated as a full channel audit.
- [ ] Synthesis: topic/performance/cross-channel findings, gaps, transparent backlog and pilot strategy.
- [ ] QA: validate tables, unchanged evidence, relevant tests, secrets, whitespace; push exact head and inspect CI. Update resume and PR body.

## Sampling decision

All 966 canonical finance videos and all valid transcript records receive automated coverage. Deep interpretation initially targets 18 canonical videos across strong/typical/weak/insufficient groups plus the existing two research overlays; expand only for unresolved decisions. New landscape discovery capped initially at six channel leads. Thumbnail acquisition starts with a matched 18-video sample; coverage gaps remain explicit, and expansion is required where image evidence changes conclusions. No claim to audit the entire niche.

Execution ledger: baseline validated and pushed as ef02fad; CSV LF correction included next. Sample expanded from 18 to 30 to cover all 13 channels plus three Shorts. Nine full-text reads and 27 mobile image reads completed; remaining scope stays explicit. Six first-page competitors add 180 cards. Twenty-six path gaps dispositioned. Legacy metadata candidate date recorded without promoting unknown formats. One primary agent throughout.

Continuation after renewed capacity: six additional full reads (Brimm/Crayon matched tiers), 30 explicit semantic title records, and source-anchored deep script maps. Full reads now 15; remaining work unchanged except these audited increments.

Second continuation unit: Drive triage of five indexed candidates (no new independent finance evidence), and source-declared DS-000022 scrape-day recovery for 595 records. Ranking expands from 176 to 723 eligible videos with five-peer and ±1-day sensitivity. Source workbooks and catalog remain unchanged.

Final bounded script unit: full Carl/Bob reads raise full-text coverage to 17 across seven channels; conditional million-dollar reveal and internal arithmetic/scenario issues documented without adopting financial claims.

## Superseding full-population execution — 2026-10-16

The owner's 966-video instruction supersedes the sampling decision above. All 966 IDs are mandatory; the old 30-row sample is reusable evidence only. Existing canonical sources remain immutable. Execute inline on this branch/PR; no plan approval gate or new worktree.

- [x] Freeze `VIDEO_MASTER.csv` bytes and ordered identities in `audit-baseline/`; hash canonical DB, transcript coverage and source files.
- [x] Add `build_audit_966.py`, `validate_audit_966.py`, and `test_audit_966.py`. Test duplicate/substituted identities, evidence drift, false semantic completion, missing script provenance and image mismatches before implementation.
- [x] Generate 966 JSONL/CSV records and six independent status dimensions. Import prior readings with their actual scope; excerpt review is not a full-script read. Preserve unavailable private metrics.
- [ ] Process channel batches of 20–40 where possible, starting with all 28 Primate Economics videos. Read all available stored text; inspect each mapped thumbnail; attach individual narrative/virality findings and specific event linkage or explicit unresolved status.
- [x] Produce requested shared tables, reports and workbook with truthful partial coverage; no unfinished record becomes complete because an output exists.
- [ ] Recompute performance under METHODS.md, validate all joins/hashes/statuses, run research and repository checks, commit/push checkpoint, verify remote equality and exact-head CI.
- [ ] Continue stable channel/master order until no dimension remains NOT_STARTED/IN_PROGRESS. Keep source-blocked components visibly blocked. Update RESUME_HERE with the exact next ID after each checkpoint.

Implementation interface: `build_audit_966.py` reads frozen identities, current master/coverage, prior semantic/title/image tables and explicit analyst `audit-batches/*.json`; writes requested full-population tables. `validate_audit_966.py` validates without rewriting analyses. Batch files are analytical source records, never generated model-like filler. All required fields absent from older reviews stay visibly pending.

Execution checkpoint: PRIMATE_001 complete limited evidence (28 IDs); CRAYON_001 30 title/image readings, NVIDIA/Petrodollar expanded complete and 28 pending. Missing-URL acquisition stopped on HTTP 429 with 158 requests unattempted. All work remains on PR #36; current next ID AKrjI9m6fpk.
