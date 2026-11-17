# Checkpoint N: clean restore and rebuild test

Base commit 7d71996317a3e55c84ada549dbd773411597697b (checkpoint M). Run by session 85559743 up to 2026-11-06T16:16Z; that session ended with its lock held. Session 58b184f1 recovered the lock on owner-death proof, reran `compare` and classified the differences. No model, reviewer or network was used by the rebuild. Weekly usage reached 99% during closure, so no cause analysis was started for the two open differences below.

## Verdict: REBUILD_EXECUTED_PARTIAL

A real rebuild ran, not only a copy and hash check. The deterministic visual pipeline reproduced. ASR did not reproduce on 2 of 15 videos, and one video's contact sheets differ. The review stage was reused, not rerun.

## Isolation and inputs

Root: the session scratchpad `restore_N` (temporary, 363 MB, not durable). Isolation is a separate `HOME`; every script resolves its workspace from it. Commands: `campaign/restore_test_N_rebuild_script.txt`, `campaign/restore_test_N_checks.txt`, `scripts/pe_restore_test.py`.

| Input | How it was obtained | Rebuilt? |
|---|---|---|
| Scripts, selection, review annotations | `git archive` of the base commit | From Git |
| 15 sources | Copied from `source_media`, SHA-256 verified | Copy and hash only |
| Local-only manifest rows | Copied from live paths, hash checked | Copy and hash only |
| `visual-ct-scan-venv`, `asr-venv` | Read-only symlink to the real paths | Not rebuilt |
| ffmpeg/ffprobe 9.0.1_1 (Homebrew), Arial Rounded Bold (system) | Host | Not rebuilt |
| ASR model | Real `~/.cache/huggingface`, `HF_HUB_OFFLINE=1` | Local cache, no network |

Test-only shims: `pe_ingest.sh` hardcodes `~/Downloads`, so its `SRCDIR` was patched in the isolated copy, and sources were symlinked under the `<title> [<id>].mp4` name it globs.

Network dependency: `pip install --no-index --dry-run --ignore-installed -r visual-ct-scan-requirements.lock` fails with `No matching distribution found for click==8.5.0`. A fresh venv needs a package index or a wheel cache; neither exists locally. A networked reinstall was not attempted.

## Results

Steps (`campaign/restore_test_N_steps.csv`): ingest, prep, native, stroke, enc_audit, build, finalize, report and gate_corrections exit 0 on 15/15; correct exit 0 on 13/13; ledger exit 0. Validate exits 1 on 15/15 (see below).

Compare (`campaign/restore_test_N_rebuild.csv`, 1,219 files): IDENTICAL 722, IDENTICAL_AFTER_PATHS 66, DIFFERENT 210, NOT_REBUILT 220, ONLY_IN_REBUILD 1.

- Byte-identical on 15/15: `shot_ledger.csv`, `visual_event_ledger.csv`, `tables/state_ledger.csv`, `reconstruction_blueprint.md`, `tables/segments_v1.csv`, annotations. Annotations are inputs copied from Git, so they prove nothing about review.
- Accepted animatics byte-identical: RT_L1 attempt 5 `bb33080b628a9a375b382380a1a1c9dce0d486e1cdbc406831a58db8910a30f9`, RT_P1 attempt 6 `372a0fb7e446e6c6cbc1622567ae1ede42054d1aeffbeb2cf0c26d325d191389`.
- Aggregates and hidden-audit recount byte-identical: `aggregate_dev_final`, `aggregate_heldout`, `hidden_audit/recount_*`.
- Publisher test: 24 passed, 0 failed (rerun at closure).

## Differences

Harmless, by inspected diff of the largest case per class:
- Timestamps, runtimes or addresses: `INGEST_DONE`, `asr_run.log`, `coverage.json`, `quality_gate.json`, `log_segment.txt`, `ebur128.txt`.
- Source path or shim: `source_path.txt`, `source_sha256.txt` (same hash), `source_manifest.json`, `visual_ct_scan_report.md`, `continuation_handoff.md`. `source_bytes` reads 175 because ingest measures the shim symlink, not the file; this is a test artifact.
- Later brief text: 7 `review_brief` files gained the read-budget clause added to the script after they were generated.
- Not rebuilt by design: `PUBLISHED`, `source_path_original.txt`, `frames/sheets_v2/*` (190).

Validate exit 1 is not a rebuild pass or a rebuild failure. `pe_validate_review.py` checks reviewer transcripts against the live paths they recorded, so in the isolated tree it reports sheets and strips never opened and writes outside the review dir. Its narration errors come from finding 1. Transcripts for all 15 reviewers exist. Live `validation.json` files were not rerun.

## Open findings

1. **ASR is not reproducible on KyBWJPaF1KI and uIG2U_1xynQ.** Measured segments and last end time, same source and model:

   | Video | Published | Rebuild | Rerun 1 | Rerun 2 |
   |---|---|---|---|---|
   | KyBWJPaF1KI | 95 / 205.54 s | 30 / 205.56 s | 13 / 205.54 s | 27 / 205.58 s |
   | uIG2U_1xynQ | 8 / 53.80 s | 14 / 49.22 s | 14 / 49.22 s | 9 / 49.38 s |

   Reruns differ from each other, so this is run-to-run variation, not drift in the restored inputs. Consequences: 2 `audio_visual_alignment.csv` files differ, and `reuse_dev.json` and `reuse_all.json` differ (for example `short_words` 119 published against 110 rebuilt). Treat ASR-derived timings and reuse shares for these videos as one sample. Cause not established. ASR is not listening, and audio gates stay BLOCKED. Segment files: `campaign/restore_test_N_asr_*.csv`.

2. **3AsDdMQr_nQ contact sheets differ.** Published 96 tiles on 8 sheets; rebuilt 100 tiles on 9. The extra tiles are hold frames 3254 and 3310 (G0089), 3369 and 3395 (G0091). `segments_v1.csv` is byte-identical and `pe_sheets.py` is unchanged since checkpoint A, so the live sheets are likely older than the current segment state, but this is an inference. G0089 and G0091 have annotations; whether the reviewer saw these four frames was not checked. Nothing live was changed.

## Publication and preservation

- M receipt: commit and remote head both 7d71996317a3e55c84ada549dbd773411597697b, 0 readback mismatches. M seal 823/823 OK inside the restored export and 0 mismatches against live files at closure.
- Manifests: 0 MISSING. 16 DRIFT_SINCE_MANIFEST rows, all expected live changes: 15 `PUBLISHED` markers and `scheduler.log`.
- Uncovered at restore time: 4 text files (M receipts and the two test scripts). This checkpoint publishes them.
- `restore_N` is temporary and can be regenerated from the commit, `source_media` and the scripts. Its key text receipts are copied into `campaign/`.
- N receipts stay local until a later checkpoint exists, by the rule in checkpoint L. No receipt-only checkpoint is planned.

## Remaining

- BLOCKED on owner: off-device destination, so no transfer has happened; listening capability, so listening, final AV signoff, narration sync and the visual-script audio side stay pending.
- Optional, after usage resets: review the 4 extra 3AsD tiles, and find the ASR variation cause. Neither was claimed closed.
- No CAMPAIGN_COMPLETE. All 15 stay VISUAL_ANALYSIS_PARTIAL. `HOLD_NO_EXECUTABLE_WORK` stays.
