# Validation actually executed

Repository/source identity: canonical Finance `223f44981ee174988574e86d5e23ae83ee60ee5d`, frozen registry SHA256 `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`. Runtime `.venv/bin/python`3.12.14. Commands/working directories, UTCtimes, durations, stdout/stderr and exit codes are retained in `validation/*.json`/`.log`.

| Check | Result | Exit / seconds |
| --- | --- | --- |
| git-diff-check | PASS | 0 / 0.035 |
| git-fsck | FAIL | 8 / 46.202 |
| tracked-secret-scan | PASS | 0 / 1.85 |
| dataset-ledgers | FAIL | 1 / 0.821 |
| registry | PASS | 0 / 8.652 |
| finance-audit | PASS | 0 / 35.811 |
| finance-research | PASS | 0 / 0.879 |
| finance-tests | PASS | 0 / 1.046 |
| finance-formatting | PASS | 0 / 0.13 |
| repository-tests | FAIL | 1 / 48.687 |
| coordination-tests | PASS | 0 / 17.551 |

Initial Git fsck failed solely on `.git/refs/.DS_Store`; after exact verified cleanup it passed. A final additional fsck after newly observed Git object-layout change also passes. All3,138formerly loose object IDs still resolve, all refs/stash match, and every checkout remains clean at its original SHA. LFS object hashes are independently listed in `lfs_presence.csv`; Git fsck alone does not certify LFS bytes.

## Commands and scope

- `git diff --check`; `git fsck --full --no-dangling`.
- `.venv/bin/python scripts/scan_tracked_secrets.py`:0 findings. Additional all-branch-tip bounded text scan:0 findings; no secret values printed. Patterns/bounds are documented; this is not an exhaustive historical/binary secret audit. Private `.env` was not opened.
- `.venv/bin/python -m scripts.validate_dataset_ledgers`:DS20/21/22/23/24/25/27clean; DS28-F020andDS30-F019fail SIZE/SHA on shared`.gitattributes`. Expected627bytes/hash1970079d…; exact current hash/size and introducing history are in `validation/provenance_mismatches.json`. Raw evidence was not altered.
- `.venv/bin/python -m scripts.validate_youtube_channel_registry`:PASS,0 domain errors,0 duplicate channel/video IDs,0 null-transcript-without-reason,0 first-party ingested; disposable rebuild idempotence PASS. Original frozen source DB retained.
- Existing Finance `validate_audit_966.py` and`validate_research.py`:PASS,966identities,26frozen-source hashes, thumbnail hashes, canonical transcript hashes, statuses/CSV identity and analysis projections. Their two generated JSONreports were redirected externally with a narrowly scoped Path.write_text shim; validators themselves were unmodified. The exact shim and argv are in reproduce/ and validation/.
- `.venv/bin/python -m pytest -q -p no:cacheprovider research/finance-economics-intelligence`:38 PASS.
- `node --test test_workbook_formatting.mjs` in Finance directory:2 PASS.
- `.venv/bin/python -m pytest -q -p no:cacheprovider tests`:459 PASS,1 SKIP,1 FAIL,5 warnings. Failure is `LedgerChecksumTests::test_all_csv_ledger_datasets_are_clean`, the same two historical config fingerprint issues. It is not hidden as a green suite.
- Coordination worktree's existing `test_yios_coordination.py` and`test_yios_checkpoints.py`:17 PASS with real disposable Git fixtures. This does not migrate a protected writer or prove Machine A receiving-client acceptance.
- Independent read-only workbook reconciliation on both exact published Finance heads:1,612unique rows/42 channels/966 details, all embedded JSON and statuses agree, ZIPintegrity PASS,17formulas,0 error-type cells. Cached deep counts461/554. Native Excel recalculation NOT_TESTED.
- SQLite read-only integrity/foreign-key inspection for4local DBs:PASS.456/456 media hashes and26/26 frozen source hashes match.351published CT003/004portable member hashes match; CT001/002manifests primarily enumerate external files rather than a member list.
- Exact-range financial claim witnesses:397 canonical and1,820Machine A version matches,0mismatches among entries with those fields. No new source entailment/financial fact-check or calculation evaluation was performed.

## Hosted CI and historical assertions

Latest canonical head run41053016403/check124053485843isFAILURE with 0 steps. Fresh authenticated annotation says job did not start due failed payments/spending limit. Classification:CI_BLOCKED_BILLING, not a successful CI run and not proof code tests executed. Existing runs were not retriggered. See `latest-ci-jobs.json`/`latest-ci-annotations.json`.

Machine A's554checkpoint declares48pytest +2Node checks and existing validators; those historical run counts were not rerun as a full Machine A environment. Fresh local checks independently establish its published row counts, IDs, workbook/JSONL equality and common frozen source availability. Each other branch's published validation declarations are indexed, not presented as fresh reruns.

## Unavailable/not-run checks

Full CT visual/audio evidence-based validators are blocked by absent external frames/audio and missing numpy/Whisper/PySceneDetect in the project runtime; raw evidence was not regenerated. No new listening, source decode, reviewer wave, external-source fact-check, Apify/YouTube API, private Drive restore, V2, source ingestion or research pipeline was started. Native Excel, current Machine A filesystem/processes, historical full Git secret content and remote LFS availability for absent versions remain unverified. One passing validator cannot certify these layers.
