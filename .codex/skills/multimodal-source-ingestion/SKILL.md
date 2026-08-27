---
name: multimodal-source-ingestion
description: "Use when the user asks to ingest a folder, add a dataset, import competitor data, analyze source folders, ingest screenshots, or ingest YouTube/forensic research into this repository. Encodes this project's tested Phase 1C recursive multi-source & multimodal ingestion rules — recursive census, hash-first dedup, per-item disposition, image/document handling, provenance. A workflow tool, not a source of truth: the repository, database, and evidence remain authoritative."
---

# /multimodal-source-ingestion

Bulk-ingest one or more external source folders into this repository's Phase 1 catalog, with 100% recursive coverage and an explicit disposition for every discovered item — never a silent skip.

## Before touching anything

1. Read `AGENTS.md` and `docs/DECISIONS.md` in full. They are authoritative over this skill.
2. Confirm the repo is clean (`git status`) and on `main`.
3. Read `docs/Database.md` §5 and `data/catalog/README.md` to know the current schema version and which tables already exist — do not assume a fresh schema.
4. For every supplied root: verify it exists at the exact given path (a near-miss path is a `SourceNotFound` error, not a guess); resolve its canonical absolute path; confirm file vs. directory; get a recursive file/dir/symlink count and total size *before* deciding anything about scope.
5. If a root's contents may already be a registered dataset, re-hash its files and compare against the recorded `source_files.sha256` for that dataset — if they match, mark `ALREADY_INGESTED`, never re-register. If they differ, this is `RevisionDetected`: stop and report, never silently overwrite history.

## Phase boundary (do not cross)

Allowed: discovery, hashing, exact + perceptual deduplication, image OCR/metadata/native-vision description, document characterization, channel/video-page screenshot *observation* registration, classification (content domain, packaging style), database migration, tests.

Never in this phase: competitor strategy analysis, viral/topic analysis, title/thumbnail/script recommendations, content-gap discovery, ranking, embeddings, RAG, vectors, live web research or scraping. If asked for any of these, say the ingestion is complete and the analysis phase needs separate, explicit authorization.

## Core completeness rule

Every filesystem item (file, directory, symlink) inside an authorized root must receive exactly one explicit disposition: `INGEST`, `REFERENCE_ONLY`, `ALREADY_INGESTED`, `EXACT_DUPLICATE`, `NEAR_DUPLICATE`, `REVISION`, `SUPPORTING_EVIDENCE`, `SUPERSEDED`, `NOISE`, `TOOLING`, `UNSUPPORTED`, `UNSAFE`, or `HOLD`. At the end, assert `TOTAL_DISCOVERED_FILES == TOTAL_FILES_WITH_DISPOSITION`. If they don't match, the batch is not complete — do not report success.

A directory shared by more than one logical dataset is the single most common source of misclassification bugs in this pipeline (confirmed live during `BATCH-000001`: loose files at a shared `outputs/` root silently fell into the wrong sibling dataset via an over-broad catch-all rule). When one folder root contains more than one logical case, write an explicit per-file or per-subfolder rule for every ambiguous item — never a single catch-all covering files that actually belong to different datasets. Visually or textually confirm what a loose file actually contains before assigning it; do not infer from folder proximity alone.

Directory/tooling-noise names (`__pycache__`, `.git`, `node_modules`, `.venv`/`venv`, `site-packages`, `*-cache`, `pydeps`, `python_pkgs`, `hf-cache`, etc.) must be checked *before* dataset-prefix matching, so a cache directory nested inside an otherwise-real evidence tree is still classified as `TOOLING`/`NOISE` and not swept into evidence.

## Filename encoding gotcha

macOS screenshot filenames (and some others) use a narrow no-break space (U+202F) between the time and "AM"/"PM", not a regular space. Never hand-type a path from what a filename *looks like* — always take paths from an actual directory listing (`os.walk`, `find`, `ls`) or from prior tool output, and use those exact bytes. A hand-typed path with a regular space will silently fail to match and read as "file not found."

## Building the pipeline (once per project, reusable across batches)

- A `source_batches` + `batch_roots` + `discovered_files` layer correlates many roots under one batch ID (see `schemas/inventory/003_multimodal_source_registration.sql` — reuse it, do not recreate).
- A declarative rules module (`scripts/source_adapters/batch_rules.py`) separates the *generic* discovery/registration engine (`scripts/register_batch.py`) from *this specific batch's* dataset/disposition assignments — never hard-code one dataset's logic into dozens of functions.
- Image pipeline: Pillow (isolated `.venv/`, never the system Python) for Layer-1 metadata + a deterministic difference-hash for perceptual near-duplicate clustering; Apple Vision (`scripts/image_text_recognition.swift`) for on-device OCR. Both are read-only and never modify the source image.
- For video-frame-heavy sources (a folder full of near-duplicate consecutive frames), hash + perceptually cluster every frame for 100% file coverage, but only run native semantic inspection on cluster representatives — never redo an existing canonical forensic report that already did shot-by-shot analysis; register that report as `SUPPORTING_EVIDENCE` and spot-verify a sample against it instead.
- For every unique competitor/evidence screenshot, run OCR *and* native semantic inspection (channel identity, video card details, visual packaging) — 100% coverage of unique images, not a sample. Distinguish `YOUTUBE_UI` values from third-party overlay values (`VIDIQ_OVERLAY`, etc.) at the field level; never merge their provenance.
- Never collapse `content_domain`/`sub_niche` (niche) into `editing_style` (production grammar) or infer one from the other. `editing_style` stays `UNKNOWN` unless real moving-image evidence (frames, shot manifests, forensic reports) exists — a channel-page screenshot never justifies an editing-style claim (Decision 016).
- Full document read (not just filename/metadata) for every PDF/DOCX/MD/TXT/CSV/JSON encountered; for a suspected duplicate pair, do a real content-level comparison (e.g. `pdftotext` + `diff`), not a metadata guess.
- Copy vs. reference: copy small/medium unique evidence into `data/raw/`; for large frame-heavy trees, copy the reports/manifests/CSVs but reference (don't copy) the raw dense-frame dumps — hash-index them all the same either way. Never copy vendored tooling into canonical evidence just to inflate a coverage number.

## Before claiming done

1. Re-hash every discovered file with a recorded hash and confirm 0 mismatches, 0 missing — source roots must be provably untouched.
2. Run `PRAGMA integrity_check` (expect `ok`) and `PRAGMA foreign_key_check` (expect 0 rows) against the live catalog.
3. Run the full test suite (`python3 -m unittest discover -s tests -v`, plus `.venv/bin/python3 -m unittest discover -s tests -v` to also exercise the Pillow-dependent tests).
4. Generate durable manifests from the database itself (`scripts/generate_batch_manifests.py`), never hand-author them — a hand-written manifest drifts from what actually got registered.
5. Review `git status`/`git diff --stat` before staging: the runtime `.db`, raw payloads, and any transient scratch/state JSON must never be committed; schema, scripts, tests, docs, and manifests should be.

## When something looks wrong mid-run

If a disposition rule produces a result that visually contradicts the file's actual content (e.g. a "moon physics" dataset containing a sunset image), stop and verify directly — open the file, don't trust the folder name or a prior audit's claims. A previous session's own generated report about this same source tree is useful context for *where to look*, never a substitute for re-verifying against the live filesystem.
