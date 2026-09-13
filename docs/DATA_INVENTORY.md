# Data Inventory

Every supplied dataset receives a durable inventory record. The active local SQLite catalog (`data/catalog/youtube_inventory.db`, schema v10) is the machine-readable index alongside Markdown documents and files under `data/manifests/`; durable manifests currently describe 24 registered datasets across the canonical channel corpus. The local SQLite catalog remains regenerable and may lag newly committed manifests until its next controlled rebuild.

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
| DS-000001 | Matty Invests & Mr. Finance Competitor Dataset | DISC-002 | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000001.md`](../data/manifests/DS-000001.md) |
| DS-000002 | "7 Things Wealthy Retirees Stopped Buying to Stay Rich" — Forensic Video Reconstruction | BATCH-000001 | C — Forensic Video Intelligence | INGESTED | [`data/manifests/DS-000002.md`](../data/manifests/DS-000002.md) |
| DS-000003 | Doctor Thomas — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000003.md`](../data/manifests/DS-000003.md) |
| DS-000004 | Dr. Adewale — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000004.md`](../data/manifests/DS-000004.md) |
| DS-000005 | Dr. Okoro — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000005.md`](../data/manifests/DS-000005.md) |
| DS-000006 | Dr. Aliza Wright / Advice — Competitor Channel Screenshots + linked Apify structured acquisition | BATCH-000001 + APIFYRUN-000001 | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000006.md`](../data/manifests/DS-000006.md) |
| DS-000007 | Dr. Waterling — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000007.md`](../data/manifests/DS-000007.md) |
| DS-000008 | The Senior Health Podcast — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000008.md`](../data/manifests/DS-000008.md) |
| DS-000009 | Senior Health Hub — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000009.md`](../data/manifests/DS-000009.md) |
| DS-000010 | The Health Educator — Competitor Channel Screenshots | BATCH-000001 | B — Competitor Evidence | INGESTED | [`data/manifests/DS-000010.md`](../data/manifests/DS-000010.md) |
| DS-000011 | All Training Data of YouTube — Global Knowledge Corpus | BATCH-000001 | A — Global YouTube Knowledge | INGESTED | [`data/manifests/DS-000011.md`](../data/manifests/DS-000011.md) |
| DS-000012 | Sunset Video Forensic Reconstruction — Case 1 | BATCH-000001 | C — Forensic Video Intelligence | INGESTED | [`data/manifests/DS-000012.md`](../data/manifests/DS-000012.md) |
| DS-000013 | Moon/Electron Physics Video Forensic Reconstruction | BATCH-000001 | C — Forensic Video Intelligence | INGESTED | [`data/manifests/DS-000013.md`](../data/manifests/DS-000013.md) |
| DS-000014 | "Weird and Worrying Questions" Video Forensic Reconstruction | BATCH-000001 | C — Forensic Video Intelligence | INGESTED | [`data/manifests/DS-000014.md`](../data/manifests/DS-000014.md) |
| DS-000015 | Sunset Video Forensic Reconstruction — Case 2 (possible revision of Case 1, unresolved) | BATCH-000001 | C — Forensic Video Intelligence | INGESTED | [`data/manifests/DS-000015.md`](../data/manifests/DS-000015.md) |
| DS-000016 | Retiree Daily-Routines Video Forensic Reconstruction | BATCH-000001 | C — Forensic Video Intelligence | INGESTED | [`data/manifests/DS-000016.md`](../data/manifests/DS-000016.md) |
| DS-000017 | xkcd's What If? — Apify Channel Acquisition | APIFY_YOUTUBE_CHANNEL | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000017.md`](../data/manifests/DS-000017.md) |
| DS-000018 | 2026 Algorithm Update — Multi-Tab Creator Research Corpus | CLOUD_DOCUMENT_EXPORT | A — Global YouTube Knowledge | STRUCTURED_REGISTERED | [`data/manifests/DS-000018.md`](../data/manifests/DS-000018.md) |
| DS-000019 | Dr. Elias Senior Health — Supplied Canonical Channel Export | EXTERNAL_FILES | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000019.md`](../data/manifests/DS-000019.md) |
| DS-000020 | Five-Channel YouTube Apify Dataset Packages | APIFY_YOUTUBE_CHANNEL | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000020.md`](../data/manifests/DS-000020.md) |
| DS-000021 | Eleven-Channel YouTube Apify Dataset Packages | APIFY_YOUTUBE_CHANNEL | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000021.md`](../data/manifests/DS-000021.md) |
| DS-000022 | Seven User-Provided YouTube Channel Packages | USER_PROVIDED_EXPORTS | B — Competitor Evidence | VALIDATED_SOURCE_PACKAGE | [`data/manifests/DS-000022.md`](../data/manifests/DS-000022.md) |
| DS-000023 | Funded Master Channel Extraction — Batch 1 | APIFY_YOUTUBE_CHANNEL | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000023.md`](../data/manifests/DS-000023.md) |
| DS-000024 | Funded Master Channel Extraction — Batch 2 | APIFY_YOUTUBE_CHANNEL | B — Competitor Evidence | STRUCTURED_REGISTERED | [`data/manifests/DS-000024.md`](../data/manifests/DS-000024.md) |

Status progression: `INGESTED` (Phase 1A — raw files preserved and cataloged) → `STRUCTURED_REGISTERED` (Phase 1B — channels/videos/snapshots/transcripts registered with field provenance, `docs/DECISIONS.md` Decisions 014–015). No competitor intelligence analysis has been performed at either stage.

DS-000002 through DS-000016 were registered in Phase 1C (`docs/Phases.md`) as part of bulk multi-source ingestion `BATCH-000001` — see `data/manifests/batches/BATCH-000001.md` for the full 12-root discovery/disposition record and `data/manifests/batches/BATCH-000001_FILES.csv` for the complete per-file coverage ledger (45,774 entries, 100% disposition coverage). One additional item discovered in that batch — a stray, accidentally-mixed-in unrelated video's frames inside the Codex archive, containing an identifiable real person — was deliberately held (`HOLD` disposition) rather than registered as a dataset; it is cataloged only in the discovered-files ledger, per `docs/Security.md`.
