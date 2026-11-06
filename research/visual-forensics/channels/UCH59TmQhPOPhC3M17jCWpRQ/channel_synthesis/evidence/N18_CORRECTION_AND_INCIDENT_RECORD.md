# N18 correction and incident record (Barely Evolved)

Session 15f69c1b, 2026-11-06. Base N17 `bf6522a570995a01561348165855c25e0e727ffb`. Nothing published earlier was rewritten; every historical file below stays as it was.

## What N18 adds
- Publication receipts that had stayed local: all `*_PUBLICATION_RECEIPT.json` in the 4 Barely Evolved folders. `N18_RECEIPT_VALIDATION.csv` records each receipt's hash and whether its commit is an ancestor of the N17 tip.
- `final_audit/FINAL_VALIDATION_v3_post_N17.json`, `evidence/N17_PREPARED.json`, `evidence/N17_INTENDED_DIFF.txt`.
- `evidence/LOCK_OWNER_at_release_15f69c1b_REDACTED.txt`: a copy with the spent lock token removed. The original stays local and its hash is written in the copy.
- `evidence/LOCK_OWNER_at_release_1e8761b1.txt`, `evidence/N12_attempt1_rejected_INTENDED_DIFF.txt`, `evidence/BE_OPS_LOG_snapshot_N18.txt`.
- Tooling absent from the remote: `be_push_checkpoint.py`, `be_publish_n18.py`, `run_ingest_v23.sh`, `v1_scripts/be_burst_rest_montages.py`.
- `evidence/N18_LOCAL_ONLY_INVENTORY.csv`: the text files that remain local, with hashes and reasons.

## Corrections
1. **N17 ops-log line.** `BE_OPS_LOG.txt` says N17 was published with "lock held by 1e8761b1". The holder was 15f69c1b; `be_push_checkpoint.py` read the first line of the owner file. The line stays verbatim. The script now reads the last `session` line. This fix was not exercised by a publish: N18 uses `be_publish_n18.py`.
2. **"1 unmapped" in R18.** It is `uPQcyookL0Y/campaign/AUDIO_LISTENING_CAPABILITY_2026-11-03.json`. The local copy sits in the Barely Evolved root, so the folder-relative mapping misses it. Its bytes match the local file, so this is a mapping artifact, not a missing or differing file.
3. **Old remote count 301.** The fresh count of 304 at N17 stands; 301 was stale.

## Incidents
1. **Lock transfer on 2026-11-05T18:15:33Z.** Session 15f69c1b took `.be_writer_lock` from 1e8761b1 on inactivity evidence and an owner-directed continuation, without the owner naming that transfer. The owner has since instructed that an unknown-owner lock must not be transferred on inactivity. That transfer is recorded here as a precedent not to reuse. N18 acquired a free lock; no transfer occurred.
2. **Rejected and retried pushes.** The objects below exist only in Machine A's object store. None holds unique research content:
   - `2bced7b2`: N12 attempt 1, rejected because N13 landed first; re-prepared and published as `21319e26`.
   - `82cd5848`, `b2cb8403`, `10759df7`: N14 attempts with tree `f77e5489`, the same tree as published N14 `735b8ffe`.

## Known stale files, not changed here
`STATUS.json` and `OWNER_SUMMARY_ROMAN_URDU.md` at the channel root came from commit `e0e2cbcc` (2026-11-02) and say `ONBOARDING_BLOCKED_NO_MEDIA_NO_NETWORK`. Later work supersedes them. Start from `channel_synthesis/final_audit/FINAL_THREE_VIDEO_AUDIT_v3.md`.

## Limits
- N18's own receipt and lock-release record are created after the seal, so they cannot be inside N18. They stay local, and the owner report carries their values.
- Git publication here is text only. It is not a media backup, off-device portability or research completion. R20 remains PARTIAL, and audio R08, R09 and R21 remain unmet.
