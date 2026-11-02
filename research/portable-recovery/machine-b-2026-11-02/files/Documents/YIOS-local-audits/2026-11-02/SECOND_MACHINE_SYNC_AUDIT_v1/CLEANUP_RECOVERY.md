# Cleanup and recovery ledger

The before checkpoint was made and verified before any exact-file cleanup. It records all HEADs/upstreams/refs/reflogs/worktrees, staged/unstaged binary-capable patches, ignored/nonignored untracked path lists, unfinished-operation checks, stash identities/contents and local writer/resource snapshots. There were no tracked or nonignored untracked changes to discard. No local branch commit was endangered, so a redundant large Git bundle was not created.

| Exact path | Classification/action | Original bytes | Recovery |
| --- | --- | --- | --- |
| /Users/ghilmanislam360/Documents/youtube-intelligence-os/.git/refs/.DS_Store | Unused local modification / REMOVED_EXACT_FILE | 6148 | /Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-02/SECOND_MACHINE_SYNC_AUDIT_v1/recovery/cleanup/.git/refs/.DS_Store.gz |
| /Users/ghilmanislam360/Documents/youtube-intelligence-os/research/finance-economics-intelligence/FINANCE_966_VIDEO_INTELLIGENCE.xlsx.inspect.ndjson | Superseded scratch / REMOVED_EXACT_FILE | 9773812 | /Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-02/SECOND_MACHINE_SYNC_AUDIT_v1/recovery/cleanup/research/finance-economics-intelligence/FINANCE_966_VIDEO_INTELLIGENCE.xlsx.inspect.ndjson.gz |
| /Users/ghilmanislam360/Documents/youtube-intelligence-os/research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx.inspect.ndjson | Redundant generated output / REMOVED_EXACT_FILE | 34251823 | /Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-02/SECOND_MACHINE_SYNC_AUDIT_v1/recovery/cleanup/research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx.inspect.ndjson.gz |

The two workbook `.inspect.ndjson` files are tool inspection exports, explicitly ignored. Their first records identify workbook inspection data; no tracked script/doc dependency and no open-file user was found. The retired966workbook's export is superseded; the current workbook remains intact and was independently checked. The Finder file under `.git/refs` is invalid Git-ref metadata; initial fsck's only errors were badRefName/badRefContent on that path. It is not a branch or research artifact. Exact gzip copies were created, decompressed and SHA256 verified before removal, and checked again afterward. Final Git integrity passes.

Gross logical removal 44,031,783 bytes (41.99 MiB; 0.041 GiB). Compressed recovery 3,883,529 bytes (3.70 MiB; 0.004 GiB). Net logical savings before other audit reports 40,148,254 bytes (38.29 MiB; 0.037 GiB). APFS physical free-space changes cannot be attributed on an active volume. Other audit output consumes space and independent Git packing changed object layout; neither is disguised as additional owner cleanup savings.

## Preserved material

All raw evidence, private configuration, registered frozen sources, stashes, local/remote branches,7Codex recovery refs, worktrees, original media, external archives, old catalogs and unknown research were retained. No blanket reset/clean/removal, stash pop/clear, auto-commit or research publication occurred. `local_path_classifications.csv` lists every ignored/untracked checkpoint path with reason/action; runtime support is retained, ignored raw evidence is preserved, unknown consumers are not declared unused.

Stash `ac51465b33be2d25d1a18749b1301cda778e33e5` contains a14-insertion/11-deletion tracked thumbnail completion-ledger edit and2,267untracked files totaling843,095,575bytes. The untracked tree has577exact remote-tip blob matches and2,265bounded local/external hash matches; an additional394,924,525byteArchive.zip matches its external original. The910,451bytefinance-short-experiment-01.zip has no exact local/remote container match established and remains preserved. Archive compression/container differences need not mean new research, so it is not counted as an independent dataset. Full item paths/blob IDs/SHA256/matching locations are in `stash_contents.csv`.

A newly generated full binary stash export would duplicate over1GBof retained evidence. It was replaced by a compact tracked-only patch, complete untracked object/hash inventory, unchanged stash ref and exact original Git object locators. The tracked patch passes `git apply --cached --check` against a disposable index at stash parent. No source/stash object was removed. The before recovery manifest was regenerated and verified after this audit-artifact compaction; the removed newly generated export is not counted as owner cleanup. Large evidence originals remain in place.

## Recovery instructions

Check `RECOVERY_MANIFEST.json` and `RECOVERY_VERIFIED.json`. Each removed path has its original SHA256 and gzip path in `cleanup_ledger.csv`. Decompress into a new staging filename, verify SHA256against the ledger, then inspect. Do not overwrite a differing original; the Finder Git-ref metadata should remain outside `.git/refs` because reinserting it reproduces the known integrity error.

For the retained stash, inspect without popping:

```sh
git show ac51465b33be2d25d1a18749b1301cda778e33e5^3:finance-short-experiment-01.zip > /private/tmp/yios-preserved-finance-short-experiment-01.zip
git diff ac51465b33be2d25d1a18749b1301cda778e33e5^1 ac51465b33be2d25d1a18749b1301cda778e33e5 -- docs/research/thumbnail-forensics-2026-10-02/completion-ledger.csv
```

Use a fresh staging path if the example destination already exists. This checkpoint is sufficient to reverse the performed cleanup and identify/preserve unchanged local work; it is not an off-device full repository disaster backup.
