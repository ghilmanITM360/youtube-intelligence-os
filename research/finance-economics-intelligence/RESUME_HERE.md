# Resume the full 966-video Finance and Economics audit

**Status: FULL_POPULATION_RESEARCH_IN_PROGRESS.** Existing branch `research/finance-economics-intelligence`, draft [PR #36](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/36). No new branch/worktree/PR or merge. Owner expanded scope to ALL 966, superseding the historical sample plan. Do not restart recovery or completed reviews.

## Recovery and identity

Starting verified head: `11bd3bebd746f85fba1820b1ebee457dd1a1a0a0`, same local/remote/PR, exact-head CI green at start. Latest pushed SHA/CI must be read from PR #36 and live Git, not assumed from this document. Three pre-existing untracked folders, stash and unrelated worktree preserved; never stage them.

Immutable population: `audit-baseline/VIDEO_IDS.csv`, 966 IDs across 13 channels. Exact source master bytes in `audit-baseline/VIDEO_MASTER.csv`; 26 hashes in MANIFEST.json. Do not recreate or mutate baseline. New audit JSONL is authoritative; CSVs/workbook are derived views. Batch JSON contains authored individual analysis, so regeneration needs no scratch script.

## Completed checkpoint

- CRAYON_001: **30/30 expanded reviews COMPLETE_LIMITED_EVIDENCE** (all stored transcripts read, all 30 images inspected, individual title/topic/script/virality interpretations, nine grouped and cached event-source receipts with per-video linkage and exclusions, Google Trends not attempted for these windows; no first-party metrics). Cross-video findings are in each virality record; channel-level association: reach vs like rate Spearman -0.62 and vs comment rate -0.58 (n=30, age-uncontrolled).
- PRIMATE_001: **28/28 expanded reviews COMPLETE_LIMITED_EVIDENCE**. All 13 Shorts +15 long-form. Every stored text read, every actual mapped image inspected at 320px, individual title/topic/script/virality interpretations. 22 new images, six reused; receipts and four contact sheets tracked.
- Current union: 79 distinct title readings, 54 distinct topic readings, 76 distinct visual readings, 41 distinct full-stored-text readings. Expanded rubric completion is 30. Prior excerpt-only reviews not upgraded.
- Performance revalidated 966; 179 strong, 383 typical, 161 weak, 243 insufficient. Five-peer sensitivity 598/723 agreement. Automated metadata validation is distinct from 30 bespoke virality assessments.
- Eleven missing transcripts: public watch pages returned HTTP 200 with correct titles but no captionTracks marker; no transcript recovered. See TRANSCRIPT_RECOVERY_001.json. Other legitimately published transcripts remain a recovery possibility, not exhausted. Never infer private/removed merely from failed captions.
- Google Trends attempted US Web Search, inflation/tariffs/cryptocurrency, 2025-03-01 to 2025-07-31; no series returned. Thirteen shared historical context/reference receipts; per-video chronology/exclusions preserved.
- All named population tables/reports and filterable XLSX exist as **in-progress deliverables**. 936 videos still await expanded reviews; 11 script components blocked. No all-966 completion claim.

## Exact next work

Next master-order ID: **`--nI-29Awuc`**, Lucas Grant (95 videos, first in frozen master order after the completed Primate and Crayon batches), POV: You Choose a Trade Over College. Crayon Capital is **30/30 expanded reviews COMPLETE_LIMITED_EVIDENCE** (CRAYON_001); Primate **28/28**. Expanded-complete total **58/966**; 908 outstanding. Remaining channel populations by master order: Lucas Grant 95, Matty Invests 94, Carl Invests 80, Mr. Finance 65, Bob Invests 57, Brimm. 44, Sonny Finance 39, Dark Ledger 38, Money Life POV 20, Shaami Finance 13, Nick Invests 363 (counts include IDs with legacy in-progress rows; read VIDEO_COMPLETION_MATRIX.csv for the exact IDs).

Continue remaining channels in frozen master order in batches of about 20 to 40, skipping expanded-complete IDs, until all 966 individual reviews are handled. Author per-video records directly into a new `audit-batches/<CHANNEL>_00N.json` (same shape as CRAYON_001.json: `reviews` with unique Video_IDs, statuses, title/thumbnail/topic/script/virality/event blocks), add shared event evidence once to `audit-batches/EVENT_SOURCES.json`, then run `build_audit_966.py` and the validators. For videos with INSUFFICIENT_DATA performance there is no PERFORMANCE_SENSITIVITY.csv row, so omit that source ref and keep a non-empty `peer_comparison_ids` for the title block. Remaining public thumbnail retrieval includes 159 missing canonical URL fields; never edit registry to fill research-derived fallbacks. Eleven transcript source gaps remain visibly blocked while other dimensions proceed.

The filterable XLSX (`FINANCE_966_VIDEO_INTELLIGENCE.xlsx`) has **not** been regenerated since the Primate checkpoint; regenerate it at the next larger checkpoint with the workbook builder below. The CSV/JSONL views are current.

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

Local verification: 16 research unit tests pass; 461 repository tests pass (five pre-existing fixture/Pillow warnings). Knowledge validator checks 2,732 local hashes but exits nonzero on its historical scope guard: seven existing `reports/project-status/2026-10-16/*` files lie outside its old allowlist relative to `08e7192`. These files already existed at starting HEAD. Do not delete unrelated status reports or claim this validator passed.

Live resources last checked: five-hour 29% used, weekly 35% used; context UNKNOWN. No resource stop threshold reached at that reading. Before each expensive unit check five-hour → weekly → context. Stop gates near 90%/95%; complete atomic unit, validate, commit/push and record exact next ID. This file's readings are historical, never substitute for live checks.

## Latest continuation additions

LEGACY_THUMBNAIL_RECOVERY_001: 159 IDs tracked; first request `-UdMJ-EtLDI` returned HTTP 429, 158 not attempted. New requests stopped, no retry/bypass. Do not treat these as permanently unavailable or repeat immediately. All other research can continue from local evidence.

Corrections made while finishing Crayon: the earlier thumbnail record for `xhbukTTkwJY` read the text as 'MADDOFF'; the stored image shows 'MADOFF' and the record is corrected.

Historical pushed SHAs: ad9326b and 5bc8944 (exact-head CI passed for ad9326b, run 38924569360). The Crayon completion commit follows; verify final HEAD independently. Final current SHA/CI belongs in PR #36.
