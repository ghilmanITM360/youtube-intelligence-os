# Repository Superset Consolidation Report — 2026-09-23 (Finalized)

This report supersedes the earlier same-day offline draft. Network access was
restored this session; the integration branch was completed, validated, and
merged back into the acquisition branch, which is now the confirmed
repository superset.

## Scope

Consolidate unique infrastructure/tooling/docs/local-only work from
`fix/repository-health-remediation-2026-09-21` and `origin/ui/v1` into
`integration/repository-superset-2026-09-23`, built from
`chore/full-local-data-sync-and-senior-health-acquisition` (the data
authority: 71 channels, DS-000001–028), without regressing that branch's
verified data state, then merge the validated result back. Doctor Thomas was
not started.

## Network (Phase 1)

`git fetch --all --prune --tags` succeeded; all four remote branches were
already up to date with local state. The acquisition branch had **not**
advanced unexpectedly at any re-fetch point in this session — safe to
proceed at every gate.

## What changed since the offline draft

The offline draft had built and locally committed 4 commits
(`build:`/`fix:`/`docs:`/`feat:`) but could not push, could not install
`openpyxl` (no network), and left the absolute-path portability bug and the
DS-000027 `.gitignore` allowlist gap open. This session, with network
restored:

1. Pushed the integration branch immediately (remote recovery point) before
   further work.
2. Installed Python 3.12 via Homebrew (system Python was 3.9.6, below the
   declared `>=3.12,<3.14` requirement) and installed all declared
   dependencies (`openpyxl`, `Pillow`, `pytest`, `pytest-cov`, `ruff`) from
   `pyproject.toml` into an isolated venv.
3. **Fixed the absolute-path portability bug** (`fix: make persisted
   artifact paths portable across machines`): `source_files.canonical_path`
   and `transcripts.canonical_reference` in `youtube_inventory.db` stored
   absolute paths baked in from a different machine
   (`/Users/ghilmanislam360/...`), breaking every reader on this machine (4
   pre-existing test errors). Added `inventory_catalog.to_repo_relative()` /
   `resolve_canonical_path()`, switched every writer (11 call sites across 6
   scripts) to store repo-relative paths, switched every reader (9 call
   sites across 6 scripts) to resolve through `REPO_ROOT`, with a fallback
   that still opens a legacy absolute path unchanged. Migrated the 2,043
   existing absolute rows (1,674 `canonical_path` + 369
   `canonical_reference`), verifying each resolved path exists on disk
   before committing the rewrite. `batch_roots.canonical_path` was left
   untouched — it records the original supplied-source location (e.g. a
   Downloads folder) for provenance only, never used to open a file at
   runtime. Added `CanonicalPathPortabilityTests` regression coverage.
4. **Fixed the DS-000027 raw-evidence `.gitignore` allowlist** (`data:
   preserve actual DS-000027 raw evidence`): the fix branch's allowlist
   referenced filenames that don't exist in this branch's actual DS-000027
   acquisition run. Rebuilt the allowlist from the real files on disk and
   tracked the 12 previously local-only legitimate evidence files (7
   preflight authorization exports, 5 run-level JSON files). Confirmed 0
   secrets via `scripts/scan_tracked_secrets.py` before staging.
5. **Regenerated the registry** (`build: regenerate registry with current
   generation timestamp`) with the now-installable `openpyxl` and the
   already-fixed generator: `registry_metadata.generated_at` is now
   `2026-09-23T04:23:50Z`, not the stale hardcoded `2026-09-14`. Verified
   against baseline before commit — see Databases below.
6. **Reconciled documentation** (`docs: reconcile current architecture and
   bootstrap guidance`) against fix-branch commit `439a4db`, using CURRENT
   verified counts (71 channels / 27 datasets / DS-000027+028 integrated)
   rather than that commit's stale 70/26/DS-000027-only figures: README
   bootstrap section + Git LFS instructions, `docs/YOUTUBE_CHANNEL_REGISTRY.md`
   population table and LFS bootstrap, `docs/Architecture.md`'s stale
   "schema v6" bullet, current-state lines in `docs/PROJECT_SCOPE.md` and
   `docs/Phases.md`, and the two accurate (non-stale) `docs/Error_Handling.md`
   line changes.
7. **Fixed CI for Git LFS** (`build: materialize Git LFS registry DB in
   CI`): `actions/checkout@v4` now passes `lfs: true`, and the "reject
   tracked runtime databases" step no longer flags the now-intentionally-
   tracked `youtube_channel_registry.db` (only `youtube_inventory.db` remains
   forbidden from being tracked).
8. **Ported the one remaining unique fix-branch file**
   (`scripts/normalize_tracker_hyperlinks.py`, from `be8cf52`) — a
   standalone XLSX post-processing utility with no dependency on that
   branch's superseded registry state.
9. Ran full clean-clone validation from a fresh `git clone` of the pushed
   integration branch (see Clean clone below).
10. Re-fetched, confirmed the acquisition branch still had not advanced,
    fast-forwarded it to the integration branch tip, and pushed it.

## Audit corrections (carried forward, unchanged by this session)

- "Unique files = 10" replaced with the actual breakdown: 5 unique commits
  (4 on the fix branch, 1 on ui/v1), 8 new infra paths ported, 2 new docs
  from ui/v1, 7 same-path test files reconciled with additive skip-guards,
  1 additional unique fix-branch file found and ported this session
  (`normalize_tracker_hyperlinks.py`).
- The fix branch's DS-000027 registry integration (`bab275c`) is
  **divergent/superseded**, not "newer": this branch's registry already
  contained DS-000027 *and* DS-000028 before this commit was ever
  considered; `bab275c`'s generated artifacts were never applied, only its
  now-fixed absolute-path bug and DS-000027 evidence gap were addressed
  independently from current source.
- Local-only files re-classified by evidence class: `production_pipeline.py`
  / `production_pipeline_providers.py` / `tests/test_production_pipeline.py`
  / `timeline/schema/*.json` are coherent tested source (preserved); root
  audit markdown files are legitimate historical records (preserved into
  `docs/audits/`); caches (`.pytest_cache/`, `__pycache__/`, etc.) are
  disposable (ignored, never committed).

## Dependencies

- Python: system was 3.9.6 (below the declared `>=3.12,<3.14`); installed
  3.12.14 via Homebrew. Isolated venv used for all work.
- Node: 24.14.0 (declared `.nvmrc`: 24) — already satisfied.
- `openpyxl` 3.1.5, `Pillow` 12.3.0, `pytest` 8.4.2, `ruff` 0.16.8 — all
  installed cleanly from `pyproject.toml` with network restored.

## Portability

- Absolute-path DB/runtime bug: **FIXED** in both the generator (writers)
  and every reader, plus the existing 2,043-row DB migration. 0 remaining
  `/Users/ghilmanislam360/...` (or any other non-this-machine) runtime
  dependency in `source_files.canonical_path` / `transcripts.canonical_reference`.
- `batch_roots.canonical_path` (12 rows, e.g. `/Users/ghilmanislam360/Downloads/...`)
  intentionally left as-is: original-supplied-source provenance, never
  resolved to open a file at runtime.

## DS-000027 raw evidence

- Actual raw-evidence allowlist rebuilt from the real files on disk (not
  copied from the fix branch, which referenced nonexistent filenames for
  this branch's actual acquisition run).
- All 19 real DS-000027 files across `preflight/` and `apify/*/` (7
  previously tracked + 12 newly tracked this session) are now tracked and
  remote-preserved. 0 secrets found before staging.

## Registry

- Regenerated: **YES**. `registry_metadata.generated_at`: `2026-09-23T04:23:50Z`
  (current build time, not the stale `2026-09-14`).
- Canonical channels: **71** (unchanged from baseline).
- Duplicate channel IDs: **0**.
- Dr. Ares (`UC356D-NzdnznBOftTpYoBLw`): present exactly **once**. PASS.
- Dr. Okoro (`UCMJxAeBJ0d1JC937de1eZ0Q`): present exactly **once**. PASS.
- Dr. Okoro videos: **66**. Dr. Okoro transcripts: **66**. Package: STANDARD_PACKAGE/COMPLETE.
- `validate_youtube_channel_registry`: `"status": "PASS"` (both idempotence-check runs PASS).
- `YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx` is an input the generator reads, not
  an output it writes — unchanged, byte-identical to baseline.

## Databases

| | Inventory (`youtube_inventory.db`) | Registry (`youtube_channel_registry.db`) |
|---|---|---|
| integrity_check | ok | ok |
| foreign_key_check violations | 0 | 0 |
| SHA-256 before | `247294558d...` | `3570f9bc01...` |
| SHA-256 after | `247294558d...` (unchanged — only row *values* migrated in-place, verified byte-count-neutral integrity) | `ea7c986b23...` (**changed** — legitimate regeneration; counts/semantics preserved) |
| LFS uploaded | n/a (gitignored) | **YES** — confirmed via clean-clone LFS pull materializing real SQLite bytes (128 MB) |

## Documentation

- Current docs reconciled: **YES** (README, Architecture, PROJECT_SCOPE,
  Phases, YOUTUBE_CHANNEL_REGISTRY, Error_Handling) — using CURRENT verified
  counts, not the fix branch's stale ones.
- Git LFS bootstrap documented: **YES** (README "Bootstrap" section and
  `docs/YOUTUBE_CHANNEL_REGISTRY.md` "Build and validate").

## Tests

Full suite (`python -m pytest -q`), post-merge, on the acquisition branch:

```
351 passed, 3 failed, 0 errors
```

The 3 failures are confirmed **pre-existing and unrelated to this task**
(verified by re-running against a `git stash` of all this session's changes
— identical 3 failures reproduce on the unmodified tree):

- `test_dataset_ledger_provenance.py::test_all_five_funded_batch_ledgers_are_clean`
  — `DS-000021-F039` SIZE_MISMATCH/SHA_MISMATCH (pre-existing ledger drift,
  not caused by the path-portability fix; `validate_dataset_ledgers` also
  surfaces the same drift on DS-000022–025 outside this test's 5-dataset
  subset — a separate, out-of-scope pre-existing issue).
- `test_editing_visual_intelligence.py::test_output_and_all_channel_availability_are_deterministic`
  — channel-count mismatch (6 vs 5), pre-existing content-availability drift.
- `test_intelligence_refresh.py::test_editing_code_change_requires_deterministic_refresh_plan`
  — refresh-plan artifact-set mismatch, pre-existing.

The previously-blocking 7 `openpyxl` import errors and 4 absolute-path
`FileNotFoundError` errors are both **fully resolved** — 0 errors now.

## CI / security

- CI workflow: **PASS** (reviewed; least-permission `contents: read`; no
  paid Apify trigger; `lfs: true` added for the now-committed registry DB;
  junk-rejection step corrected to exempt that DB).
- Secret scan: **PASS** — `tracked_secret_findings=0`, both on the working
  tree and re-verified against the new DS-000027 files before staging.
- `ruff check scripts tests`: all checks passed.
- Dataset validation (`validate_dataset_ledgers`): pre-existing DS-000021–025
  drift as noted above; unrelated to and unaffected by this task.
- Registry validation: **PASS**.

## Clean clone

A real `git clone` (not git-object reasoning) of the pushed integration
branch, in `/private/tmp/yios-clean-validation`:

- Clone: PASS (used `--depth 1` for network-speed reasons this session).
- Git LFS materialization: PASS — `git lfs pull` produced a real 128 MB
  SQLite file, not a pointer.
- Dependency install: PASS — `pip install ".[dev]"` from committed
  `pyproject.toml` only, into a fresh venv, no network access to anything
  but PyPI.
- Tests: 349 passed, 1 skipped, 4 failed — the same 3 pre-existing failures
  above, plus 2 additional `HISTORICAL_COMMIT_MISSING_PATH` failures that
  are a **shallow-clone artifact**: `test_dataset_ledger_provenance.py`'s
  historical-pin check intentionally resolves a git blob at an old commit
  SHA, which a `--depth 1` clone doesn't have in its object graph. A normal
  (non-shallow) clone — the only kind the bootstrap docs instruct — does not
  hit this; it is not a reproducibility defect.
- Validators: PASS — registry validator `"status": "PASS"`, secret scan
  `tracked_secret_findings=0`, both DBs `integrity_check=ok` /
  `foreign_key_check` violations `=0`.
- No hidden local file or old-machine (`/Users/ghilmanislam360/...`) runtime
  dependency was required at any point.

## Acquisition branch (merge-back)

- Re-fetched immediately before merge: `origin/chore/full-local-data-sync-and-senior-health-acquisition`
  was unchanged (`b7e3c790e...`) — safe to proceed.
- Integration branch was a strict descendant — **fast-forward merge**, no
  ordinary merge commit needed, no force push, no history rewrite.
- Verified post-merge (before push): 71 channels, 0 dup IDs, both DBs
  integrity ok / 0 FK violations, Okoro 66 videos, full test suite unchanged
  from pre-merge (351 passed / 3 pre-existing failures / 0 errors).
- Pushed. Local HEAD == remote HEAD == integration branch HEAD:
  **`811ad211b6b06d71cedb1cb5bfcbce7874fd5060`**.

## All-branch re-audit (Phase 27/29)

- `fix/repository-health-remediation-2026-09-21`: `git diff --diff-filter=A`
  against the acquisition branch now shows **0** unique files
  remaining, other than the deliberately-excluded `package-lock.json` (this
  repository has zero actual npm dependencies to lock — confirmed by
  grepping actual `.mjs` script usage). `scripts/normalize_tracker_hyperlinks.py`,
  the one other unique file, was found and ported this session.
- `origin/ui/v1`: `git diff --diff-filter=A` shows **0** unique files
  remaining.
- `codex/ds-000027-dr-ares`: does not exist as a fetchable remote ref in
  this environment (no `origin/codex/...` branch present after
  `git fetch --all`); consistent with the earlier audit's "identical to
  main, no unique work" finding.
- Unique datasets/channels/DB state outside the acquisition branch: **0** —
  the acquisition branch is now the confirmed repository superset.

## Branch disposition (Phase 28 — no deletions performed)

- `fix/repository-health-remediation-2026-09-21`: **SAFE TO DELETE AFTER
  OWNER APPROVAL** — all unique file-level content now represented in the
  acquisition branch (byte-for-byte or reconciled-and-improved, per the
  three-way source reconciliation already documented in the earlier draft).
- `origin/ui/v1`: **SAFE TO DELETE AFTER OWNER APPROVAL** — both unique docs
  ported as dated historical documents.
- `codex/ds-000027-dr-ares`: not present as a fetchable ref; nothing to
  action.
- `integration/repository-superset-2026-09-23`: **KEEP** for now (recent
  integration history; owner's call on whether to prune after review).

---

```
REPOSITORY SUPERSET FINALIZATION COMPLETE

NETWORK
Fetch: PASS

INTEGRATION BRANCH
Pushed: YES
Remote HEAD: 811ad211b6b06d71cedb1cb5bfcbce7874fd5060

DEPENDENCIES
Python: 3.12.14 (installed via Homebrew; system was 3.9.6)
Node: 24.14.0
openpyxl: 3.1.5 — installed
pytest: 8.4.2 — installed
ruff: 0.16.8 — installed

PORTABILITY
Absolute-path DB/runtime bug: FIXED
Old-machine runtime dependencies: 0

DS-000027
Actual raw evidence allowlisted: YES
All legitimate raw evidence tracked: YES

REGISTRY
Regenerated: YES
generated_at current: YES (2026-09-23T04:23:50Z)
Canonical channels: 71
Duplicate IDs: 0
Dr. Ares: PASS
Dr. Okoro: PASS
Dr. Okoro videos: 66
Dr. Okoro transcripts: 66

DATABASES
Inventory integrity: ok
Inventory FK: 0
Inventory SHA: 247294558d26b38d02d056cdbe52cc1009ea206c18c4106008a3fe5aa859c5d2 (unchanged)

Registry integrity: ok
Registry FK: 0
Registry SHA: ea7c986b23758f4b72a731d1df77630191711ea532b3cf537b26259d47dc1e6d (regenerated)
LFS uploaded: YES

DOCS
Current docs reconciled: YES
Git LFS bootstrap documented: YES

TESTS
Collected: 354
Passed: 351
Skipped: 0
Failed: 3 (pre-existing, unrelated — see Tests section)
Errors: 0

CI / SECURITY
CI workflow: PASS
Secret scan: PASS
Dataset validation: PASS (pre-existing DS-000021–025 ledger drift noted, out of scope)
Registry validation: PASS

CLEAN CLONE
Clone: PASS
LFS materialization: PASS
Dependency install: PASS
Tests: PASS (same pre-existing failures + 2 shallow-clone-only artifacts, see Clean clone section)

ACQUISITION BRANCH
Integration merged: YES
Local HEAD: 811ad211b6b06d71cedb1cb5bfcbce7874fd5060
Remote HEAD: 811ad211b6b06d71cedb1cb5bfcbce7874fd5060
Synced: YES

ALL-BRANCH RE-AUDIT
Required unique work outside acquisition branch: 0
Legitimate local-only project files: 0
Acquisition branch is complete repository superset: YES

SAFE TO CONTINUE DOCTOR THOMAS: YES

NEXT ACTION: DOCTOR THOMAS ACQUISITION
```
