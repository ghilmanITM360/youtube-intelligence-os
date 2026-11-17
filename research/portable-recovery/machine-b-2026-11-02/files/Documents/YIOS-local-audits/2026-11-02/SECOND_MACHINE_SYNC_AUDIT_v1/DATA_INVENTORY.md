# Measured data inventory

The pre-cleanup filesystem census contains24,144file entries across34bounded scopes, logical 18,064,260,968 bytes (17227.42 MiB; 16.824 GiB). It includes shared Git only once, excludes this new audit package, and excludes the nested Claude worktree from the parent count. This is a logical/allocated-block census, not deduplicated APFS physical extents. After cleanup and background Git packing, `location_totals_after.csv` provides measured updated scope totals. All originals were retained except the three exact disposable paths in the cleanup ledger.

## Primary checkout files before cleanup

| Category | Files | Actual logical bytes | Unique hashes / hashed files |
| --- | --- | --- | --- |
| owner_reports_handoffs_documentation | 332 | 13879016 | 332 / 332 |
| other | 82 | 426639 | 74 / 82 |
| production_intelligence | 14 | 1572434 | 14 / 14 |
| json_datasets_manifests | 824 | 141918379 | 803 / 824 |
| private_configuration_metadata_only | 1 | 103 | 0 / 0 |
| csv_projections | 143 | 109481756 | 142 / 143 |
| measurement_state_scene_event_ledgers | 99 | 8913813 | 99 / 99 |
| source_receipts_witnesses_hashes | 231 | 1837234 | 231 / 231 |
| source_code | 146 | 2413893 | 146 / 146 |
| tests_validators | 67 | 587836 | 67 / 67 |
| prompts_schedulers | 7 | 1512484 | 7 / 7 |
| reviewer_shards_responses | 79 | 2696749 | 78 / 79 |
| inspection_sidecars | 2 | 44025635 | 2 / 2 |
| jsonl_datasets | 8 | 12416876 | 8 / 8 |
| workbooks | 66 | 21222042 | 60 / 66 |
| runtime_cache_dependencies | 1469 | 50833742 | 0 / 0 |
| thumbnail_images | 646 | 99190981 | 646 / 646 |
| frames_and_visual_evidence | 1130 | 113309370 | 1130 / 1130 |
| archives_recovery | 73 | 18297896 | 73 / 73 |
| sqlite_catalogs | 4 | 193765376 | 2 / 3 |
| transcripts_subtitles_archives | 562 | 31434719 | 554 / 562 |
| other_images | 122 | 565729336 | 122 / 122 |
| contact_sheets | 57 | 28852864 | 57 / 57 |
| audio | 7 | 78133250 | 7 / 7 |

Hash census excludes runtime/cache/dependency files and secrets, and is bounded at64MiB per file; separately registered large source and media hashes were checked beyond that bound. Across the census there are5,266identical-content groups within that bound, including repeated checkouts, source/extracted copies, projections and external preservation. A byte match does not make two observations independent. `identical_content_groups.csv` contains exact paths/hashes. Two inspection sidecars in the table have since been removed with verified recovery copies.

## Logical populations and acceptance

| Population | Videos / files | Accepted or structural | Partial / blocked / pending |
| --- | --- | --- | --- |
| Canonical Finance | 1612 | 461 limited;0 full | 16 /17 /1,118 |
| Separate published Machine A Finance | 1612 | 554 limited;0 full | 16 /17 /1,025 |
| Canonical registry | 2,303 videos;75 channel identities | Metadata/source registry, not audit acceptance | 2,291 real transcripts;12 placeholders;33 datasets |
| CT001–005 | 5 source videos | 2 visual-only;0 full AV | 3 partial;all human-AV signoff blocked |
| Older PR21 Casually Finance | 18 selected | 16 structural source packages | 2 selected sources absent;overlap with later CT cases |
| Casual Economics sampled corpus | 11 | 11 structural;0 deep/AV | Optional listening/independent claim QA remains |
| Private local media | 456 files | 456 hash matches | 389 high-confidence IDs;67 unresolved mappings |
| 12-channel public metadata | 445 | 12 channels,metadata only | No deep-audit acceptance inferred |
| MonkeyExplains1999 | 76 | 121raw minus45members-only | Finance uses63selected expansion records |
| BarelyEvolved | 4 | Metadata snapshot | 3local media files separately registered |

Finance disposition priority is explicit and mutually exclusive: all six dimensions complete → accepted; otherwise any missing-source block → blocked; otherwise authored complete/IN_PROGRESS → partial; remaining → pending. Baseline performance classification alone does not count as authored partial research. Original966and expansion646are disjoint by the registered universe, while branch versions and multiple projections are not added. Existing partial `TFtBWn9CWOU` is retained. Canonical Nick Invests has363registered originals and194fully completed limited-evidence records; supplementary 2026-10-23 reports are older snapshots.

## Catalogs and packages

`youtube_channel_registry.db` is actual SQLite, frozen SHA256 `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`, not an LFS pointer. It contains75 channels,2,303 videos/transcript rows,2,291 real transcript FTS entries,33 datasets and40 standard packages. The existing registry validator passes. Its disposable rebuild has319artifact rows while the frozen DB has318; the validator's documented domain checks accept the snapshot. Do not rebuild/replace the frozen source merely to equalize that index count.

`youtube_inventory.db` is a different selected inventory:26 datasets,10 channels,667 videos,668 transcript references,6,953 source-file rows,45,774 discovered-file rows,5,172 visual assets and604 classifications. Historical discovered-file rows do not prove those45,774files are physically on this Mac. Two ignored legacy DB files are empty-schema SQLite; retained as unknown consumers. All four current DBs pass SQLite integrity; no foreign-key violations found. Schemas/counts are in `sqlite_inventory.json`.

66 tracked workbook files have60 unique content hashes (source/extracted copies are not independent datasets). `current_workbooks.csv` records every sheet's nonempty row structure. Finance has exactly one current combined workbook per branch version,1,612uniquevideo rows,42 channel rows and966 detail rows. All embedded JSON fields and six status columns compare equal to their branch's canonical JSONL. Cached dashboard counts agree at461/554;0Excel error-type cells. Native Excel recalculation was not tested. The `FINANCE_UNIVERSE.csv` identity/layer index still reports430 complete in both versions: stale status projection, not an additional authority for current acceptance.

`structured_datasets.csv` indexes1,436 unique CSV/JSONL blob versions across46branch tips, with record counts, explicit ID-key counts, duplicate-ID rows, status declarations, columns and all locations. Records with repeated IDs can be expected events/shots/search hits; duplicate-ID rows are not automatically duplicate videos. `json_schema_record_counts.csv` counts arrays without treating arbitrary JSON keys as records. One historical `channel_about.jsonl` blob has39non-JSONL lines; the raw source is preserved and no normalization claim is made.

## Claims, receipts, reviewer/state and production data

| Finance version | Structured claims / videos | Source receipt entries | Calculation receipt entries | Exact stored-ASR witnesses |
| --- | --- | --- | --- | --- |
| canonical | 801 / 200 | 808 | 206 | 397 |
| machine-a-published | 2224 / 293 | 1037 | 392 | 1820 |

Source receipt entries often repeat the same source across audits; they are not unique primary documents or a fresh verification of entailment. Older267 video claim audits are narrative text, not structured claim rows. Canonical397and separate-branch1,820 structured witnesses with exact ranges all match stored transcript bytes; other structured claims do not carry these exact range fields. Source confidence was only explicitly added in later Machine A batches; absent labels remain LEGACY_UNLABELLED, not upgraded to direct evidence. Receipts include direct inspection, snippets, recall and explicit source-unavailable limits. `finance/claims.csv`, `primary_source_receipts.csv`, `calculation_receipts.csv`, `transcript_read_receipts.csv` preserve those distinctions.

State/scene/event/composition/reviewer data exists in older PR21, Casual Economics, the38-Short editing corpus and later CT001–005 branches. CT001 has76 parent states, CT002507 states, CT003409 states/254 compositions/922 motion rows, CT004530 states/367 compositions, and CT005has its current integrated_v2/second-pass ledgers. These counts use different versions/contracts and must not be summed as independent videos. Raw reviewer outputs are claims subject to integration, not automatic acceptance. Full branch file/category/row inventories are in `branch_data_areas.csv`, `branches/trees/`, `structured_datasets.csv` and `visual_packages.json`.

Production candidates exist on Dr Rehan test/heart-warning, Finance Short01/02 and three Senior Health production branches, with scripts/storyboards/assets/audio timing/QA/manifests and some rendered candidates. They are separate from research acceptance; several are explicitly QA_BLOCKED or owner-review candidates. LFS presence is independently listed:20 locally present object versions (one current materialized source plus19 stored older versions),6 missing payload versions. No private media was downloaded or regenerated.

External YIOS recovery/preservation folders, handoffs, algorithm/creator audits, visual discovery material, transcript ZIPs, MP4s and archives are inventoried with actual paths and byte counts. ZIP central-directory members are counted separately from loose files in `zip_archives.csv`; archive copies are not added as new videos. Stash untracked content2,267files/843,095,575bytes is preserved in Git and mostly duplicated in external preservation, not copied into this audit as large media.
