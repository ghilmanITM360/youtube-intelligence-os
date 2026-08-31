# Corpus Status Queries

Read-only reporting layer over the existing manifests and `data/catalog/youtube_inventory.db`.
It answers questions about what has already been ingested and classified — it does not
ingest new data, does not perform competitor strategy analysis, and does not generate
topic/title/thumbnail recommendations (same Phase 1C boundary as
`.codex/skills/multimodal-source-ingestion/SKILL.md`).

Three scripts, each supporting both consumption modes:

- **Markdown** (default): human-readable report, printed to stdout.
- **`--json`**: a single structured JSON object on stdout, for an agent to parse
  programmatically instead of scraping Markdown.

Both modes are built from the same query results in one run, so they never disagree.

| Script | Answers |
|---|---|
| `scripts/report_corpus_status.py` | What data has arrived so far? What is still missing? |
| `scripts/report_channel_coverage.py` | Which channels are in the system? Which have scripts/transcripts? Which only have screenshots? Which have packaging/editing evidence? What is each channel's newest structured snapshot and which sources support it? |
| `scripts/report_dataset_matrix.py` | Which datasets are registered? Which are forensic-video datasets? Which are health/finance/general-knowledge? |

## Question → command map

- **What data has arrived so far?**
  `python3 scripts/report_corpus_status.py` — Datasets, Source Batches, Discovered Files sections.
- **Which datasets are currently registered?**
  `python3 scripts/report_dataset_matrix.py` — one row per dataset.
- **Which channels are in the system?**
  `python3 scripts/report_channel_coverage.py` — Tier A + Tier B tables (see caveat below).
- **Which channels have scripts/transcripts?**
  `python3 scripts/report_channel_coverage.py` — "Channels with scripts/transcripts" answer line (Tier A only, currently).
- **Which channels only have screenshots?**
  `python3 scripts/report_channel_coverage.py` — "Channels with screenshots only" answer line (Tier B).
- **Which channels have thumbnail/packaging evidence?**
  `python3 scripts/report_channel_coverage.py` — Thumbnail Items/Refs and Packaging columns. A thumbnail URL
  reference is reported separately from a screenshot-supported packaging observation.
- **Which channels have editing-style evidence?**
  `python3 scripts/report_channel_coverage.py` — Editing Evidence and Related Forensics columns (Decision 016:
  requires real moving-image/frame evidence, never inferred from a screenshot, thumbnail, or transcript). A linked
  forensic dataset can establish that editing evidence exists without creating an editing-style classification.
- **What is a channel's newest structured snapshot?**
  `python3 scripts/report_channel_coverage.py` — Newest Snapshot column.
- **Which evidence came from screenshots vs Apify?**
  `python3 scripts/report_channel_coverage.py` — Sources column and Apify Provenance table; packaging evidence
  remains screenshot-derived, while video/transcript/snapshot fields carry Actor/run provenance.
- **How many regular videos, Shorts, and streams does a channel have?**
  `python3 scripts/report_channel_coverage.py` — Regular/Shorts/Streams/Unknown column, using each video's newest
  structured snapshot without overwriting older observations.
- **Which forensic datasets are strongly related to a channel?**
  `python3 scripts/report_channel_coverage.py` — Related Forensics column. A relationship is shown only when an
  exact source-download media ID is registered against a canonical channel video; topic/style similarity is not enough.
- **Which datasets are forensic-video datasets?**
  `python3 scripts/report_dataset_matrix.py` — "Forensic Video" column / Forensic-video datasets section.
- **Which datasets are health niche, finance niche, or general YouTube knowledge?**
  `python3 scripts/report_dataset_matrix.py` — "By content domain" section (`content_domain` as
  actually recorded in `entity_classifications`; a dataset with no classification row reports as
  `UNCLASSIFIED`, never guessed from its name).
- **What is still missing?**
  `python3 scripts/report_corpus_status.py` — "What is still missing" section: datasets never
  classified, `editing_style` unknown despite visual evidence, `packaging_style` missing despite
  semantic screenshot inspection, provenance text inconsistencies, unavailable transcripts.

## Coverage separated on purpose

Each report keeps these dimensions visually distinct rather than folding them into one score,
so a reader can tell *what kind* of evidence backs a claim:

- **Scripts/transcripts coverage** — `channels`/`videos`/`transcripts` tables (Decision 014/015
  structured registration). Exists only for datasets that completed structured registration.
- **Screenshot/visual packaging coverage** — `visual_assets` + `entity_classifications.packaging_style`.
  Screenshot evidence can support a packaging/thumbnail-style claim; it can never support an
  editing-style claim (Decision 016).
- **Editing-style evidence** — a recorded `entity_classifications.editing_style`, or strongly linked forensic-video
  frames/shot evidence. The report keeps an actual style classification separate from evidence availability: linked
  frames may produce `FORENSIC (unclassified)`, never a guessed style. Transcripts, thumbnails, and screenshots do
  not establish editing style.
- **Niche/domain classification** — `entity_classifications.content_domain` / `sub_niche`, reported
  verbatim; `UNCLASSIFIED` when no row exists.
- **Provenance confidence** — not a fabricated score. Each dataset's row in the dataset-matrix
  report names which evidence layer actually backs it: `field_provenance` (structured registration,
  Decision 015), `entity_classifications.evidence_layer` (screenshot observation), `document_records`
  (full-text-read documents), or forensic-video frame clustering cross-referenced against a
  canonical report (see `data/manifests/batches/BATCH-000001_VISUAL_STATE_COVERAGE.md`).
- **Gaps/unknowns** — computed each run in `report_corpus_status.py`, not a hand-maintained list, so
  it can never silently go stale as new data is classified.

## Identity-tier caveat (channel coverage)

`report_channel_coverage.py` reports two tiers that must never be treated as equivalent:

- **Tier A — `REGISTERED_CHANNEL`**: a real row in the `channels` table, with `videos`/
  `transcripts` linked to it by foreign key.
- **Tier B — `DATASET_EVIDENCED_COMPETITOR`**: no strongly linked `channels` row exists. The display name is
  derived by stripping the literal `" — Competitor Channel Screenshots"` suffix off that
  dataset's own recorded `dataset_name` — it is a label of convenience for this report, not a
  registered channel identity (no `channel_id`, no YouTube channel ID, no video/transcript
  linkage). Never merge on the name alone. Once exact handle/URL/channel-ID evidence creates a
  `channel_dataset_links` relationship, the same dataset is shown with Tier A and suppressed from Tier B.

## Agent query example

```bash
python3 scripts/report_dataset_matrix.py --json | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print(d['dataset_ids_by_content_domain'].get('HEALTH', []))"
```

## Regenerating

These scripts always reflect the *current* catalog state — there is nothing to regenerate other
than re-running them after new ingestion/classification work lands. They never write to the
database or to `data/manifests/`.
