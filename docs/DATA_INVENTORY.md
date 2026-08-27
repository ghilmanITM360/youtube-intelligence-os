# Data Inventory

Every supplied dataset will eventually receive a durable inventory record. Markdown documents and files under `data/manifests/` are sufficient for Phase 1; no database is being introduced.

## Planned record fields

```text
Dataset ID
Dataset Name
Original File Name
Original Path
File Type
Semantic Class
Description
Source
Associated Channel
Associated Competitor
Associated Video
Date Received
File Count
Approximate Size
SHA-256
Duplicate Status
Processing Status
Notes
```

Records should preserve enough provenance to trace every derived artifact to the exact supplied source. Unknown values should remain explicitly unknown rather than inferred without evidence.

## Duplicate detection rule

Future ingestion must calculate a cryptographic hash, preferably SHA-256, for each supplied file. Hashes allow differently named files with identical bytes to be detected without relying on filenames or extensions.

Inventory work must eventually distinguish:

- exact duplicate;
- probable duplicate;
- different revision; and
- genuinely new dataset.

SHA-256 can establish byte-for-byte identity, but probable duplicates and revisions require additional evidence. Phase 1 establishes the rule and manifest location only; it does not include a sophisticated deduplication engine.

## Dataset-level index

Phase 1A (Decision 012) adds a local SQLite catalog (`data/catalog/youtube_inventory.db`) as a machine-readable index alongside these manifests; see `data/catalog/README.md`. This section stays the dataset-level index — full per-file detail lives in each dataset's manifest, not here.

| Dataset ID | Name | Discovery ID | Semantic Class | Status | Manifest |
|---|---|---|---|---|---|
| DS-000001 | Matty Invests & Mr. Finance Competitor Dataset | DISC-002 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000001.md`](../data/manifests/DS-000001.md) |
