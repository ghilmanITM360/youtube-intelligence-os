# Resume the full 966-video Finance and Economics audit

**Status: FULL_POPULATION_RESEARCH_IN_PROGRESS.** Existing branch `research/finance-economics-intelligence`, draft [PR #36](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/36). No new branch/worktree/PR or merge. Owner expanded scope to ALL 966, superseding the historical sample plan. Do not restart recovery or completed reviews.

## Recovery and identity

Starting verified head: `11bd3bebd746f85fba1820b1ebee457dd1a1a0a0`, same local/remote/PR, exact-head CI green at start. Latest pushed SHA/CI must be read from PR #36 and live Git, not assumed from this document. Three pre-existing untracked folders, stash and unrelated worktree preserved; never stage them.

Immutable population: `audit-baseline/VIDEO_IDS.csv`, 966 IDs across 13 channels. Exact source master bytes in `audit-baseline/VIDEO_MASTER.csv`; 26 hashes in MANIFEST.json. Do not recreate or mutate baseline. New audit JSONL is authoritative; CSVs/workbook are derived views. Batch JSON contains authored individual analysis, so regeneration needs no scratch script.

## Completed checkpoint

- PRIMATE_001: **28/28 expanded reviews COMPLETE_LIMITED_EVIDENCE**. All 13 Shorts +15 long-form. Every stored text read, every actual mapped image inspected at 320px, individual title/topic/script/virality interpretations. 22 new images, six reused; receipts and four contact sheets tracked.
- Legacy union: 52 distinct title/topic semantic readings, 49 distinct visual readings, 39 distinct full-stored-text readings. Expanded rubric completion remains 28. Prior excerpt-only reviews not upgraded.
- Performance revalidated 966; 179 strong, 383 typical, 161 weak, 243 insufficient. Five-peer sensitivity 598/723 agreement. Automated metadata validation is distinct from 28 bespoke virality assessments.
- Eleven missing transcripts: public watch pages returned HTTP 200 with correct titles but no captionTracks marker; no transcript recovered. See TRANSCRIPT_RECOVERY_001.json. Other legitimately published transcripts remain a recovery possibility, not exhausted. Never infer private/removed merely from failed captions.
- Google Trends attempted US Web Search, inflation/tariffs/cryptocurrency, 2025-03-01 to 2025-07-31; no series returned. Nine shared historical event receipts; per-video chronology/exclusions preserved.
- All named population tables/reports and filterable XLSX exist as **in-progress deliverables**. 938 videos still await expanded reviews; 11 script components blocked. No all-966 completion claim.

## Exact next work

Next master-order ID: **`1GowFTjbUnk`**, Crayon Capital, NVIDIA Explained Like You're 5. Next channel batch: **all 30 Crayon Capital IDs in VIDEO_MASTER order**. Reuse its prior full reads/title/image reviews; extend to expanded rubric. Stable next-ID advances only when record statuses justify it. Primate completed channel is skipped when encountered later.

After Crayon, continue remaining channels in frozen master order, batches approximately 20–40, until all 966 individual reviews handled. Remaining public thumbnail retrieval includes 159 missing canonical URL fields; never edit registry to fill research-derived fallbacks. Recover metrics where defensible without substituting current snapshots into old cohorts. Eleven transcript source gaps remain visibly blocked while other dimensions proceed.

## Validation and rebuilding

```bash
python3 research/finance-economics-intelligence/build_baseline.py
python3 research/finance-economics-intelligence/build_comparisons.py
python3 research/finance-economics-intelligence/build_audit_966.py
python3 -m unittest discover -s research/finance-economics-intelligence -p 'test_*.py'
python3 research/finance-economics-intelligence/validate_research.py
python3 research/finance-economics-intelligence/validate_audit_966.py
.venv/bin/python -m pytest -q
python3 scripts/scan_tracked_secrets.py
git diff --check
```

Legacy VALIDATION.json reports only legacy tables; VALIDATION_966.json covers new full-population views. Research checks run explicitly; general repository CI does not automatically validate research. No CI workflow changed in this checkpoint because regenerated registry DB bytes in CI can differ from the frozen local binary hash despite equivalent source data.

Workbook builder: copy tracked build_workbook_966.mjs into a temporary directory beside a node_modules symlink to bundled dependencies, run bundled Node with absolute research directory argument. Read Spreadsheets skill for runtime paths and authoring protocol. Builder recalculates six coverage counts, mutation-tests one status, renders all three sheets, exports one XLSX. `audit-batches/workbook-*.png` are previews, not competitor evidence.

Local verification: 14 research unit tests pass; 461 repository tests pass (five pre-existing fixture/Pillow warnings). Knowledge validator checks 2,732 local hashes but exits nonzero on its historical scope guard: seven existing `reports/project-status/2026-10-16/*` files lie outside its old allowlist relative to `08e7192`. These files already existed at starting HEAD. Do not delete unrelated status reports or claim this validator passed.

Live resources last checked: five-hour 9% used, weekly 32% used; context UNKNOWN. No resource stop threshold reached at that reading. Before each expensive unit check five-hour → weekly → context. Stop gates near 90%/95%; complete atomic unit, validate, commit/push and record exact next ID. This file's readings are historical, never substitute for live checks.
