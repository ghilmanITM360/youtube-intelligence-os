# YIOS audit: commands and scope

## Where everything is
- Audit directory: `/Users/ghilmankhan/YIOS-audit-20261105T1657Z/`. Scripts in `scripts/`, full command record in `COMMANDS_LOG.txt`, raw output in `raw/`, snapshots in `before/` and `after/`.
- Scratch, audit-only: `scratch/remote_mirror.git` (no alternates, no promisor), `scratch/tests/*`, `scratch/proof/`. Scratch is not in the checksum manifest because it changes and can be rebuilt; it stays on disk because cleanup was not authorized.

## Read-only rules used
- Canonical repo: `GIT_OPTIONAL_LOCKS=0`, `GIT_NO_LAZY_FETCH=1`, plus read commands only (`for-each-ref`, `log`, `show`, `status`, `ls-remote`, `rev-list --missing=print`, `fsck` with no write flags).
- Network: `ls-remote` from canonical; fetch only into the audit mirror with auto-maintenance disabled. Nonpruning.
- Tests: `sandbox-exec` denies network and writes to workprojects, YIOS-local-audits, YIOS-Archive, Downloads and Documents. Credentials unset. Scratch `.git` borrows mirror objects through alternates only inside `scratch/tests`.
- SQLite opened `mode=ro`; rebuilds only in scratch. Dataless files were not opened.

## Key steps
| Step | Script or command | Output |
|---|---|---|
| Local collection, scheduler, orphan `.rev` | `01_collect_local.sh` | `raw/orphan_rev`, `raw/primitive_scheduler`, `raw/inventory` |
| Mirror clone | `02_mirror.sh` | `raw/remote` |
| Hash index, target compare | `03_hash_index.py`, `04_hash_compare.py` | `raw/hash` |
| DB audit | `05_db_audit.py` | `raw/db` |
| Ref matrix | `06_ref_matrix.py` | `raw/refs` |
| Blob compare, LFS, first tests | `07_blob_compare.py`, `08_mechanical.sh` | `raw/blob`, `raw/lfs`, `raw/tests` |
| U in V | `09_u_in_v.py` | `raw/u_v` |
| 5,767 search | `10_find_hashset.py`, `11_subset_5767.py`, `15_published_manifest_hashes.py` | `raw/5767` |
| 12 files | `12_find_12.py` | `raw/hash/twelve_*`, `out/TWELVE_FINANCE_NICK_FILES.csv` |
| All mirror SHA-256 | `13_mirror_blob_sha256.py` | `raw/hash/mirror_blob_sha256.tsv` |
| Machine B inventory compare | `14_compare_inventory.py` | `raw/portable` |
| Validator proofs | `16_validator_proofs.py` | `raw/code/validator_proofs.json` |
| DB logical compare | `17_db_logical_compare.py` | `raw/db/*compare*`, `raw/db/registry_rebuild_*` |
| Retrieval demos | `18_retrieval_demos.py`, `20_retrieval_finance.py` | `raw/db/retrieval_demos.json` |
| Data classes | `19_data_classes.py` | `raw/hash/local_classes_by_root.csv` |

## Retrieval demos actually run (`raw/db/retrieval_demos.json`)
1. Channel and videos: Nick Invests 363, xkcd's What If? 83, Casual Finance 0.
2. Full chain for `pFs8QGikczo`: video, Nick Invests, transcript 1966 with locator and hash, `VIDEO_AUDIT_966` row batch NICK_278, 6 statuses, source refs. `xtqbRt94TTw` is absent from the DBs: reported as a gap, located by Git path instead.
3. Rule `FR-TITLE-02`: locator, 15 assessments, exact witness text.
4. Production spec: Video006 `per_state_production_spec_DRAFT_v4.csv`, 447 rows. No test references a production spec: 0 hits in `tests/`.
5. Next task: Video006 queue v5; Finance `15Gr4BAJi00`, `1CJTuLaenq8`, `1D9nBNa6jNE`.

## Scope limits
- Hash index ran at about 18:37Z on 2026-11-05: 51,729 files, 22.4 GB, 40,334 unique; 2,873 dataless not opened; 58 dirs skipped. Newer worker files are not in it.
- Unrelated repos were listed by path and not opened; only YIOS paths were read.
- Machine B, Google Drive and GitHub server internals were not inspected.
- Bytes are logical. No reclaimable estimate is given. No backup destination was tested.
