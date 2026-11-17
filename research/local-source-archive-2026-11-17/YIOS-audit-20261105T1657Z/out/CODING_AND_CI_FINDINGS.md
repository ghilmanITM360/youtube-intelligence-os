# YIOS coding and CI findings

Audit is read-only, so nothing here was fixed or published. Code references are at PR #36 tip `f115285ba230fd9a8d8923dff1e5d477f8247d80` unless stated. Proofs ran on a scratch copy: `scripts/16_validator_proofs.py`, output `raw/code/validator_proofs.json`.

## Test results: local and hosted are separate

| Ref | Local, Python 3.12.14, network denied, source roots write-denied | Hosted, last run seen |
|---|---|---|
| `main` `08e71926` | 460 passed, 1 skipped; ledgers exit 0 | success, 2026-10-10 |
| Finance PR #36 `f115285b` | 462 passed, 1 skipped; ledgers exit 0; `validate_audit_966` exit 0; `check-all` OK; 5 framework tests pass | FAILURE, run 41448066128 |
| Knowledge Navigation `f4dc5d14` | 460 passed, 1 skipped; ledgers exit 0 | no open PR run seen |

FRESH. Logs: `raw/tests/full_with_git/`, `raw/tests/targeted/`.

The first local run showed 2 or 3 failed tests. That came from this audit's harness: the export had no `.git`, so provenance tests could not read history. Those failures are not project defects. A second defect in my script (`git ls-tree -- '*.db'` does not glob) left its allowlist listing empty; it was redone with `ls-tree -r | grep`.

Local PASS does not reproduce the hosted environment: Python differs (3.12.14 here, 3.12.15 hosted), this ran on macOS, and the allowlist step is a shell step outside pytest.

## Findings

### C1. Finance PR #36 hosted failure: exact cause known
- FRESH: all steps pass, then `.github/workflows/validate.yml:59-60` fails with `Unapproved tracked database(s): data/knowledge/reference_knowledge.db`.
- The allowlist has `youtube_inventory.db` and `youtube_channel_registry.db` only.
- 7 runs fail from `0df91c58`; runs pass through `78871b87`.
- Root cause: a tracked DB was added without updating the allowlist. The DB is tracked on purpose: `AGENTS.md` and `PORTABLE_SYNC_MANIFEST.json` both describe it as tracked.
- Targeted fix: add one `-e 'data/knowledge/reference_knowledge.db'` at line 59. Owner decides, since it approves a binary DB in Git.

### C2. Ready allowlist patch: not found on Machine A or remote
Searched, all with 0 hits:
- `validate.yml` content at all 104 mirror refs and 95 local refs.
- Git history of `validate.yml` with `-G reference_knowledge`, both stores.
- `*.yml`, `*.yaml`, `*.patch`, `*.diff` under workprojects, `.codex/worktrees`, YIOS-local-audits, YIOS-Archive, private backups, finance-work-machine-a.
- Claude and Codex session logs.
- Machine B `repair_commit.patch` inside PR #36.

Status: **no branch, path or integration state can be named from here.** If it exists it is unpublished, and Machine B is UNKNOWN.

### C3. Other failing PRs: cause unknown
PRs #37, #38, #39, #41, #43, #44 show failure, and `gh run view --log-failed` returned `log not found`. C1 is not assigned to them. HISTORICAL lead only: Machine B's Nov 2 report records a billing annotation on run 41053016403 for `223f4498`. That is one run on another head, so it does not explain these either. 10 other open PRs show old success.

### C4. Reference comparison gate checks existence only
- `reference_comparison.py` `check_coverage()`: `not (...).exists()`. Its docstring and `AGENTS.md:42` say a "validating" comparison is required.
- Proof: corrupting `NICK_281_REFERENCE_COMPARISON.json`, then replacing it with `{}`, still gave `check_coverage() == []`. Direct `validate()` on the corrupted file reported 6 errors.
- Real data: the 3 current comparison files do validate, by test. The gate is weak; no bad file was found.
- Targeted fix: call `validate()` inside that loop. It is already called for reanalysis rows two lines below.

### C5. TITLE and THUMBNAIL witnesses accept any text
- `validate()`: `elif kind in ('TITLE','THUMBNAIL_OBSERVATION'): if not w.get('text')`.
- Proof: 3 witnesses replaced with `FABRICATED TEXT THAT IS NOT THE TITLE` gave 0 errors. The existing forged-witness test only covers transcript witnesses.
- Real data: 29 files, 57 of 57 TITLE witnesses are substrings of the registry title. 46 THUMBNAIL_OBSERVATION witnesses cannot be checked by machine.
- Targeted fix: compare TITLE text with `videos.title`. Thumbnail stays structural.

### C6. Meaningless stage implementations and exceptions pass
- `content_plan_check.py`: `if not (a.get('implementation') or a.get('exception'))`.
- Proof: the same rule on all 7 stages with `implementation: 'x'`, then `exception: '.'`, both returned no errors.
- Also unchecked: whether a rule's dimension fits the stage, whether a rule came from `retrieved`, and whether an exception has a reason.
- The validator labels itself structural-only, which is honest, but a plan like this would still get `STRUCTURALLY_VALID_NOT_SEMANTICALLY_REVIEWED`.
- Targeted fix: bind rule dimension to stage, require a rule from retrieved sections, reject trivial text.

### C7. Framework plan validation is optional, and hosted CI never runs it
- `AGENTS.md` heading says mandatory. `run_youtube_intelligence.py:831` only checks when `--framework-plan` is passed.
- `ref_plan_application` has 0 rows, so no real plan has been stored.
- Hosted workflow does not run `validate_audit_966.py` or `check-all`, and pytest `testpaths = ["tests"]` skips `reference-framework/test_reference_comparison.py`. These gates have no hosted coverage.
- Targeted fix: add those steps to the workflow; make the flag required for any run that claims a framework plan.

### C8. Runtime mismatch
- Project needs Python `>=3.12,<3.14`. System `python3` is 3.9.6, and campaign scripts call `python3 -I` (Primitive Education, xkcd What If). Impact not tested.
- Hosted run warned about the Node 20 action runtime; `.nvmrc` is 24, local Node is 24.14.0.
- Canonical `.venv` is 3.12.14.

### C9. Video006 publishing allowed media into Git
- FRESH: 4 JPG paths under `xtqbRt94TTw` at `5e497970`, count verified here. Introduced by W2, W3, W4 according to worker file `Casual-Finance-Video006-followup-20261106T0330Z/MEDIA_DEFECT.json`.
- That record says the publisher lacks a final-tree media rejection. The current Codex run says it will enforce it for its own publication. History keeps the blobs either way.

### C10. Registry cannot retrieve visual-forensics videos
- At Finance tip: Casual Finance has 0 videos, `xtqbRt94TTw` is absent, Primitive Education and Barely Evolved channels are absent. xkcd What If has 83, while its census has 91.
- These streams are retrievable by Git path, not by DB. Demo: `raw/db/retrieval_demos.json`.

### C11. Primitive Education scheduler design
`pe_continue.sh` checked only that the source directory exists, so a costly worker could start and then hang on Downloads. See `AUTOMATION_AND_OWNERSHIP.md`.

## Dangerous tests and scripts
- The full suites passed with network denied and write-denied source roots, so they need neither. Credentials were unset.
- Not run because they touch network or paid services, by name and reading: `scripts/apify_youtube_ingest.py`, `scripts/acquire_registered_thumbnails.py`, publish scripts such as `pe_publish.py`, `xk_publish.py`, `be_push_checkpoint.py`.

## Database checks
| DB | Integrity | FK errors | Logical rows | Rebuild in scratch |
|---|---|---|---|---|
| `youtube_channel_registry.db` | ok | 0 | 75 channels, 2,303 videos, 2,303 transcripts | 20 of 21 tables identical; only `registry_metadata` differs |
| `youtube_inventory.db` | ok | 0 | 667 videos, 45,774 discovered_files | partial rebuilder exercised on disposable DB, not compared |
| `reference_knowledge.db` | ok | 0 | 20 members, 1,260 sections, 33 rules, 722 assessments, inventory placeholder tables 0 | 36 of 37 tables identical; only `schema_meta` differs |

FTS shadow tables and empty placeholders are excluded from research population. Canonical DBs were not written.
