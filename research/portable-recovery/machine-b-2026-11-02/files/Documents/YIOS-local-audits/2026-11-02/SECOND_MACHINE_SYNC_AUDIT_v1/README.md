# YIOS second-machine synchronization and complete project audit — v1

Owner date: 2026-11-02 (Asia/Karachi). Generated 2026-11-02T09:22:58.804963+05:00. Machine `Users-MacBook-Pro.local`, macOS26.2/25C56, user `ghilmanislam360`. Repository authenticated as `ghilmanITM360`; private repository identity verified. All output is outside the research checkout at `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-02/SECOND_MACHINE_SYNC_AUDIT_v1`.

**Result:** all 24 local branches and all 3 existing linked checkouts already matched their own fetched upstreams. There were no staged, unstaged or nonignored untracked changes. No fast-forward would change a ref; no checked-out branch was moved. `main` is `08e719264e31ecd82de24f8eeb8f065c08359fe5`. The primary checkout is Finance, not `main`.

**Critical distinction:** canonical Finance/OPEN-DRAFT PR36 remains `223f44981ee174988574e86d5e23ae83ee60ee5d` with461/1,612 accepted limited-evidence audits. Separate published Machine A branch `9c6f42fb33e493314cced538d5c5fa599a29e6c5` has554/1,612, is44 commits beyond canonical and contains93 additional completed IDs. Its work is recovered in local Git objects, not merged into canonical/default. No push, PR36 change, ownership transfer or research integration occurred.

**Cleanup:** exactly3 proven disposable paths; gross 44,031,783 bytes (41.99 MiB; 0.041 GiB); compressed verified recovery 3,883,529 bytes (3.70 MiB; 0.004 GiB); net logical savings 40,148,254 bytes (38.29 MiB; 0.037 GiB). No raw evidence deleted. Finder metadata caused an invalid-ref Git integrity failure; removing that exact metadata file fixed it. Separate background object-layout changes were observed and verified; their space delta is not credited to cleanup.

**Research:** canonical461 accepted /16 partial /17 blocked /1,118 pending; separate Machine A554 /16 /17 /1,025. These are alternative versions of the same1,612 videos. Full-evidence completion is0, and visual/full-AV signoff is separate.

**Validation:** both canonical Finance validators,38Finance tests,2formatting tests, channel registry and final Git integrity pass. Full repository tests:459pass,1skip,1fail. Two provenance rows point to stale `.gitattributes` hashes. Workbooks agree with their JSONL at461/554 and have0 error-type cells; the universe CSV is stale at430. Hosted CI did not start because of billing. This is not an all-project-valid certification.

**Media:**456/456 registered private media files hash-match here (454videos +2audio,4.06GiB). All five published CT001–005 source MP4 hashes match local files. Most CT frame/audio/private reviewer evidence is absent. CT006 has an older published PR21 package and hash-verified source inside `Downloads/CasuallyFinance.zip`; the separately reported new CheckpointB workspace is not found in the fetched CT namespace.

## Read the package

- [Roman Urdu owner report](OWNER_REPORT_ROMAN_URDU.md)
- [Before/after synchronization](SYNC_REPORT.md)
- [Every branch](BRANCH_AUDIT.md), [complete CSV](branch_matrix.csv), [JSON](branch_matrix.json)
- [Every worktree/clone](WORKTREE_CLONE_AUDIT.md), [CSV](worktree_clone_inventory.csv)
- [Data inventory](DATA_INVENTORY.md), [typed populations](population_counts.csv), [all files](files.csv), [after location totals](location_totals_after.csv)
- [Structure and authorities](STRUCTURE_AUTHORITY_MAP.md)
- [Cleanup and recovery](CLEANUP_RECOVERY.md), [exact ledger](cleanup_ledger.csv), [local path classifications](local_path_classifications.csv), [stash contents](stash_contents.csv)
- [Fresh validation and limits](VALIDATION_REPORT.md), [raw results](validation_results.json)
- [Portability/missing evidence](PORTABILITY_MISSING_EVIDENCE.md), [exact transfer entries](machine_a_transfer_requirements.csv), [LFS presence](lfs_presence.csv)
- [Ten practical workflows](DATA_USE_GUIDE.md)
- [Prioritized unresolved issues](UNRESOLVED_ISSUES.md)

`branches/trees/` contains a complete file/blob index for every fetched branch tip; `branches/diffs/`, `branches/commits/`, `branches/cherry/` and `branches/exclusive/` show changes, history and reuse. `structured_datasets.csv` indexes1,436 unique CSV/JSONL blob versions across branches. `json_schema_record_counts.csv` indexes declared arrays; `published_validation_declarations.json` preserves historical declarations without presenting them as fresh validation. `branch_data_areas.csv` gives every branch's category counts and Git blob bytes.

## Evidence and recovery limits

The filesystem census is bounded to likely project locations, registered worktrees and discovered YIOS/media/handoff paths. Other volumes and arbitrary unrelated personal directories were not searched. Before/after snapshots have observation times; this is not an atomic disk image. Git object sizes do not include absent LFS payloads. File counts/projections are not independent video counts. APFS extent sharing is unknown. The recovery checkpoint covers the performed exact-file cleanup; large originals and the complete stash remain in place, not duplicated as a full off-device backup. Machine A's present local filesystem/processes and private cloud stores are not observable here.

Final authenticated seal: `2026-11-02T04:26:41.104089+00:00`. All46remote branch heads still match the audited SHAs; PR36remainsOPEN/DRAFT/unmerged at the same SHA; all3checkouts remain clean and unchanged. See `FINAL_SEAL.json`.
