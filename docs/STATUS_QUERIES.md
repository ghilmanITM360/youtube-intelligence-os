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
| `scripts/report_channel_coverage.py` | Which channels are in the system? Which have scripts/transcripts? Which only have screenshots? Which have packaging-style / editing-style evidence? |
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
- **Which channels have packaging-style evidence?**
  `python3 scripts/report_channel_coverage.py` — Packaging Evidence column.
- **Which channels have editing-style evidence?**
  `python3 scripts/report_channel_coverage.py` — Editing Evidence column (Decision 016: requires real
  moving-image/frame evidence, never inferred from a screenshot).
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
  structured registration). Only exists for datasets that went through Phase 1B structured
  registration (currently DS-000001).
- **Screenshot/visual packaging coverage** — `visual_assets` + `entity_classifications.packaging_style`.
  Screenshot evidence can support a packaging/thumbnail-style claim; it can never support an
  editing-style claim (Decision 016).
- **Editing-style evidence** — `entity_classifications.editing_style`, which stays `UNKNOWN` unless
  real moving-image/frame evidence exists (forensic-video frame clusters, shot manifests). As of
  this writing, the forensic-video datasets that *do* have that evidence (DS-000012–DS-000016) have
  no `entity_classifications` row at all yet — a real gap the corpus-status report surfaces, not a
  false "no evidence" claim.
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
- **Tier B — `DATASET_EVIDENCED_COMPETITOR`**: no `channels` row exists. The display name is
  derived by stripping the literal `" — Competitor Channel Screenshots"` suffix off that
  dataset's own recorded `dataset_name` — it is a label of convenience for this report, not a
  registered channel identity (no `channel_id`, no YouTube channel ID, no video/transcript
  linkage). Never merge Tier A and Tier B rows or treat a Tier B name as if it had a `channel_id`.

## Agent query example

```bash
python3 scripts/report_dataset_matrix.py --json | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print(d['dataset_ids_by_content_domain'].get('HEALTH', []))"
```

## Regenerating

These scripts always reflect the *current* catalog state — there is nothing to regenerate other
than re-running them after new ingestion/classification work lands. They never write to the
database or to `data/manifests/`.
