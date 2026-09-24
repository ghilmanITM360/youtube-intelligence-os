# Repository remediation report — 2026-09-21

## 1. Baseline

Local `main` started at `dcfe2927eee8c9bca11ac03cf21724c59b440b6b`, one commit behind live `origin/main` (`25110136c61ac0cc8bb124a1cacd3aa5fae8a840`). No divergence. Conflicting local DS-000027 files were byte-compared with the incoming commit and backed up outside the repository before a fast-forward. `main` then matched `origin/main` at `25110136`. All changes below were made on `fix/repository-health-remediation-2026-09-21`, not on `main`.

Baseline SHA-256 checks covered DS-000027 raw evidence/manifests, the registry, tracker, and current intelligence. Final comparison found only the intended generated registry JSON and tracker XLSX changed. Raw evidence, DS-000027 manifests, and existing intelligence artifacts retained their baseline hashes.

## 2. Changes made

- Integrated DS-000027 into canonical registry, target ledgers, capability coverage, and master tracker.
- Replaced tracker `HYPERLINK()` formulas with native workbook hyperlinks; no stale cached formula errors remain.
- Added safe read-only SQLite access, a manifest-index catalog rebuild, declared Python/Node runtime contracts, clean-clone test behavior, validation CI, and a value-safe tracked-secret scan.
- Reconciled current documentation and narrow DS-000027 raw-evidence ignore rules.

## 3. DS-000027 integration

Dr. Ares Senior (`UC356D-NzdnznBOftTpYoBLw`) appears once, linked to DS-000027 and its standard package. The package contributes 35 videos, 35 descriptions, and 35 real transcripts. Topic, packaging, hook, and script inputs are ready. No Dr. Ares-generated channel intelligence was claimed or fabricated. Editing remains unavailable without registered forensic video. Strategy and unified-plan artifacts remain unavailable until their supported historical/catalog contracts are met.

## 4. Registry and count reconciliation

Registry validation passed with 70 canonical channels: 36 standard packages, five historical channels, and 29 identity-only channels. It contains 1,939 videos, 1,928 real transcripts, 11 placeholders, and 14 description gaps. Forty-one channels have video data. Generated channel-specific intelligence exists for five channels, not 69; the former 69 figure conflated input-ready capability rows with actual artifacts. The five-channel generated coverage is: topic five, packaging five, hook five, script five, unified plans five, strategy four, editing one.

## 5. Dependencies and reproducibility

`pyproject.toml` declares Python `>=3.12,<3.14`, runtime `openpyxl`/`Pillow`, and development `pytest`/`pytest-cov`/`ruff`; `.python-version` selects 3.12. `package.json`, lockfile, and `.nvmrc` declare Node >=22 <25 without inventing an npm dependency for the external bundled `@oai/artifact-tool`. README documents clone-to-validation commands. An isolated Python 3.12 environment installed `.[dev]` successfully. Historical ignored raw transcript/forensic evidence is not reconstructed in a clean clone; those tests skip with explicit reasons.

## 6. Database fixes

The invalid zero-byte local inventory DB was verified empty and replaced by a valid ignored schema-v10 manifest-index DB. This is **semantic manifest indexing, not byte-identical reconstruction** of the old operational catalog or its unavailable raw rows. The ignored registry DB was generated from tracked inputs plus available local evidence. Both databases returned `PRAGMA integrity_check = ok` and zero foreign-key violations. Reporting/validation reads use read-only SQLite URI mode and raise an actionable error for a missing/empty DB rather than creating one. The registry validator passed an idempotence check.

## 7. Tests and validation

Clean declared Python environment: 343 collected; 287 passed, 56 explicitly skipped, zero failed, zero errors, five warnings. Historical `341 passed` describes a different environment/state and is not a current result. Dataset ledgers DS-000021, DS-000022, DS-000023, DS-000024, DS-000025, and DS-000027 validated clean. Registry controls validated. `ruff check scripts tests`, tracked-secret scan (`0` findings), `git diff --check`, and `git fsck --full --strict` passed; fsck reported harmless dangling objects, not corruption.

## 8. CI status

`.github/workflows/validate.yml` now performs declared dependency installation, compile/static checks, tracked-secret scan, manifest-index and registry rebuild, provenance/registry validation, tests, and tracked-runtime-junk rejection with read-only repository permission. Local equivalent gates passed. Hosted GitHub Actions execution remains **not run/unknown** until branch publication and workflow execution; it is not claimed passing here.

## 9. Tracker fix

Generator now uses dynamic channel ranges and emits native hyperlinks. Regenerated workbook has 1,103 native hyperlinks, zero `HYPERLINK()` formulas, zero cached hyperlink errors, and automatic recalculation metadata. Workbook opened in `openpyxl`; channel 70 and Dr. Ares are represented. This avoids dependence on formula cached values in non-Excel readers.

## 10. Documentation updates

Updated README, AGENTS, Architecture, Phases, Project Scope, Error Handling, and Channel Registry docs. They now distinguish 70 canonical holdings, 41 channels with video data, 36 standard packages, 29 identity-only records, five generated-intelligence channels, input-ready versus generated coverage, one forensic-video channel, and zero ingested first-party Analytics exports. Dated historical audits remain historical.

## 11. Cleanup performed

Removed only verified noncanonical local items: the zero-byte invalid DB (replaced by a valid ignored generated DB), two ignored nested DS-000021/DS-000023 JSON copies after matching canonical hashes, `outputs/.DS_Store`, and generated Python/inspection caches. No canonical tracked raw evidence was deleted. Other ignored `outputs/` copies were preserved; proposed removal was not approved and no workaround was used.

## 12. Files deliberately preserved

Canonical raw/package/manifests, all existing intelligence, dated audits, and six pre-existing untracked local reports/proposals remain untouched. `origin/ui/v1` unique commit `0412932` contains two dated UI handoff/audit documents, no unique source; both are superseded historical context. The remote branch was not deleted. Raw-versus-package duplicate evidence remains intact for provenance.

## 13. Remaining limitations

Historical operational catalog rows and ignored transcript bodies cannot be byte-identically reconstructed from a clean clone. The rebuilt catalog is a manifest index, and historical registry fallback uses tracked canonical-fact snapshots with absent bodies clearly marked. Dr. Ares intelligence is input-ready but not generated. Tracker rebuilding requires an external bundled artifact runtime; committed tracker consumption and Python validation do not. GitHub-hosted CI has not yet run. Pre-existing untracked reports remain outside commits pending a retention decision. Other ignored output staging was preserved.

## 14. Git status

Remediation branch contains only intentional committed changes; pre-existing untracked reports/proposal remain local and uncommitted. Baseline `main` matched live `origin/main` before remediation. No merge into `main` or history rewrite occurred.

## 15. Commit list

1. `bab275c` — `feat: integrate DS-000027 into canonical registry`
2. `be8cf52` — `build: make clean-clone validation reproducible`
3. `439a4db` — `docs: reconcile registry status and bootstrap`
4. Final report commit: recorded in Git history after this report is committed.

## Final assessment

**HEALTHY WITH WARNINGS** for local reproducible validation, subject to hosted CI confirmation. No secret findings or Git object corruption. The remaining warnings are explicit evidence availability and external tracker-build tooling, not silent data-integrity failures.
