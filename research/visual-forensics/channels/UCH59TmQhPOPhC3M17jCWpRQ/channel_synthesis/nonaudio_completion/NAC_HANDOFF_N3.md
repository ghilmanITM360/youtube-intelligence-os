# Non-audio completion — handoff N3 (2026-11-04 ~20:55 UTC; five-hour 86%)

- **Lock:** `.be_writer_lock`, session 1e8761b1.
- **Remote:** 051800b6 (N8).
- **Listening and AV sign-off:** excluded; still BLOCKED.

## State per item

| Item | v1 uPQcyookL0Y | v2 mNLNb-Z4T0M | v3 GNaBxt_zIRA |
|---|---|---|---|
| Dense interval naming (tiles) | 282/282 | 288/288 | IN PROGRESS: check rows in `dense_review/DENSE_REVIEW_GNaBxt_zIRA_v1.csv` |
| Native-crop verification | 99/99 (54 confirmed, 45 corrected) | packs built (100 intervals, 34 sheets); review NOT DONE | not built |
| Merged ledger | `DENSE_REVIEW_LEDGER_uPQcyookL0Y.csv` | interim (100 NEEDS_CROP_NOT_DONE) | — |
| Style/full-scene RT | RT-V1-S01 PASS | S01–S03 FAIL, S04 PASS | S01, S02 FAIL, S03 PASS |
| Asset crosswalk | NOT DONE (brief and sheets ready: `crosswalk/`) | | |
| Portability | STORAGE_DESTINATION_REQUIRED | | |

## Exact next operations

1. If the v3 CSV has fewer than 280 rows, resume the reviewer from the next sheet (`BRIEF_DENSE_REVIEW.md`, VID=GNaBxt_zIRA).
2. `~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 scripts/crop_packs.py GNaBxt_zIRA`
3. Crop reviews for v2 (C001..C034) and v3 (`BRIEF_CROP_REVIEW.md`). After each, run `/usr/bin/python3 scripts/merge_dense_ledger.py <VID>`.
4. Crosswalk reviewer (`crosswalk/BRIEF_CROSSWALK.md`).
5. Close-out: FINAL_AUDIT_MATRIX_v2, gates, synthesis/manual v1.2, `be_final_validate.py`, publish, release the lock.

**Publishing.** Run from the channel_synthesis directory:
```
/usr/bin/python3 ../be_prepare_checkpoint.py NX <remote> channel_synthesis EVIDENCE_SHA256SUMS_checkpoint_N8 '["globs"]' '[]'
/usr/bin/python3 ../be_push_checkpoint.py NX "msg"
```
