# Duplicate and relationship register

Exact-byte duplicate groups are recorded by SHA256 and `Duplicate_Of` in [SOURCE_CATALOG.csv](SOURCE_CATALOG.csv). [Recovery counts](RECOVERY_COUNTS.json) gives file counts, not independent-observation counts. [Archive members](ARCHIVE_MEMBER_INDEX.csv) compare member hashes against physical sources without extracting or rewriting originals.

| Family | Decision | Basis |
|---|---|---|
| DS-000011 `Hook (1).pdf` and `Hook guide.pdf` | Same extracted text; different container bytes | Both yielded 77,308 characters; equal full text independently verified using pdftotext. Treat as one semantic source family. |
| Original training folder / training ZIP variants / raw canonical copies | Compare exact file and archive-member hashes | Source catalog and archive index; preserve all historical containers. |
| DS-000018 snapshot / cloud 2026 Algorithm Update / algorithm reports | One underlying collection with snapshots and interpretations | [DS-000018 manifest](../../data/manifests/DS-000018.md); live cloud revision equivalence is not certified. |
| DS-000031 text / structured claims / training-knowledge rollups | Source and derivative interpretations | [DS-000031 manifest](../../data/manifests/DS-000031.md). |
| DS-000012 / DS-000015 | SAME_SOURCE_INDEPENDENT_ANALYSIS, historical registered relationship | [Catalog documentation](../../data/catalog/README.md). Independent analyses are not independent source videos. |
| Finance forensic corpus / success playbook / Word, Excel and Drive exports | Reused video corpus and report family | [Finance inventory](../../research/finance-economics-intelligence/EXISTING_DATA_INVENTORY.csv), [Drive review](DRIVE_REVIEW.md). Do not add 206 uploads to another 206 for the same snapshot. |
| Finance thumbnail original / 160px / 320px versions | Derived visual variants | [Local thumbnail index](../../research/finance-economics-intelligence/LOCAL_THUMBNAIL_INDEX.csv); file count is not independent-thumbnail count. |
| Registry / legacy inventory database / channel workbooks | Overlapping projections | Count unique YouTube video IDs from the chosen scope, not database rows added together. |

No exhaustive semantic deduplication of all 128 cloud candidates or every historical PDF version is claimed. Same title is only a duplicate candidate; different bytes can contain the same text, and similar wording can share an upstream source. Resolve the family before treating it as corroboration.
