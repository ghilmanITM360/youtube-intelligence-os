# Test and Validation Report — 2026-11-11

Environment: macOS arm64, `.venv` Python 3.12.14 (project requires `>=3.12,<3.14`; system `python3` is 3.14.7 and is out of range), ruff 0.16.9, pytest 8.x. No network calls beyond `git fetch`/`gh`. No paid API, Apify, or publishing action was run.

| # | Command | Result |
|---|---|---|
| 1 | `.venv/bin/python -m compileall -q scripts tests` | exit 0 |
| 2 | `.venv/bin/python -m ruff check scripts tests` (CI rule set E9,F63,F7,F82) | All checks passed |
| 3 | `.venv/bin/python scripts/scan_tracked_secrets.py` | `tracked_secret_findings=0` |
| 4 | `.venv/bin/python -m pytest -q` (baseline, before edits) | **462 passed, 1 skipped, 5 warnings, 43.85 s** |
| 5 | `python -m scripts.validate_dataset_ledgers` | every dataset reported `clean` |
| 6 | `python -m scripts.validate_youtube_channel_registry` | `"status": "PASS"` |
| 7 | SQLite read-only `PRAGMA integrity_check` + `foreign_key_check` on `youtube_inventory.db`, `youtube_channel_registry.db`, `reference_knowledge.db` | `ok`, 0 FK violations each |
| 8 | `ruff --select F401 --fix` on scripts/tests, then pytest | **1 failed** — `test_dataset_ledger_provenance::test_all_csv_ledger_datasets_are_clean` (`DS-000022-F046 SIZE_MISMATCH/SHA_MISMATCH`): that file is hash-pinned in `data/manifests/DS-000022_FILES.csv`, so my import removal changed its hash. I reverted that one file. |
| 9 | pytest after revert | **462 passed, 1 skipped** (37.73 s); ruff clean; ledger validator clean |

## Not run / limits
- Skipped test: `tests/test_production_pipeline.py:16` — real media fixture package absent.
- Not run: `scripts.build_youtube_channel_registry --write-ledgers` and `scripts.rebuild_inventory_catalog` (CI runs them; they write generated files — not run to avoid mutating tracked data). Not run: Finance validators (`validate_audit_966.py`, `content_plan_check.py`), `git lfs pull` verification beyond confirming the registry DB is readable and passes integrity.
- Not run: dependency vulnerability scan (no `pip` in the venv; `pip-audit` not installed). Dependency ranges are pinned in `pyproject.toml`/`uv.lock` but not CVE-checked.
- Not run: the app against real first-party analytics, Apify, or any live YouTube data (none exists / not authorized).
- Pytest warnings: Pillow `Image.getdata` deprecated (removed in Pillow 14, `scripts/image_pipeline.py:43`); duplicate-name ZIP fixture warning.
- Coverage % was not measured. By name matching, 17 of 65 scripts are not referenced by any test (see BUGS_AND_TECHNICAL_DEBT.md).

Confidence in current health: high for the V1 Python tooling and catalog integrity; unverified for anything touching private first-party data, media, or the Finance research gates in CI.
