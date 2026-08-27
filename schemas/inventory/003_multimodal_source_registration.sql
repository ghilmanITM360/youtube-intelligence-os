-- Phase 1C — Recursive Multi-Source & Multimodal Ingestion (additive only).
-- Adds: a batch layer correlating many source roots, a complete per-file
-- discovery ledger (so every encountered filesystem item gets an explicit
-- disposition), image-specific evidence tables, and generic classification /
-- document tables. Does not touch any table shipped in 001 or 002.

PRAGMA foreign_keys = ON;

-- One row per bulk ingestion batch (e.g. BATCH-000001), correlating many
-- independently-verified source roots under one durable identity.
CREATE TABLE source_batches (
    batch_id        TEXT PRIMARY KEY,
    batch_name      TEXT NOT NULL,
    started_at      TEXT NOT NULL,
    completed_at    TEXT,
    status          TEXT NOT NULL CHECK (status IN ('STARTED', 'COMPLETED', 'PARTIAL', 'FAILED')),
    root_count      INTEGER NOT NULL,
    tool_version    TEXT NOT NULL,
    notes           TEXT
);

-- One row per source root supplied to a batch (e.g. the 12 root paths).
-- Independent of dataset assignment: a root may map to zero, one, or many
-- logical datasets (see discovered_files.dataset_id).
CREATE TABLE batch_roots (
    batch_root_id       TEXT PRIMARY KEY,
    batch_id            TEXT NOT NULL REFERENCES source_batches(batch_id),
    root_index          INTEGER NOT NULL,
    supplied_path        TEXT NOT NULL,
    canonical_path        TEXT,
    exists_at_discovery    INTEGER NOT NULL CHECK (exists_at_discovery IN (0, 1)),
    root_type               TEXT,
    file_count                INTEGER,
    dir_count                  INTEGER,
    symlink_count                INTEGER,
    total_size_bytes               INTEGER,
    observed_at                     TEXT NOT NULL,
    notes                            TEXT,
    UNIQUE (batch_id, root_index)
);

-- The complete recursive census. EVERY filesystem item encountered inside an
-- authorized source root gets exactly one row here, with an explicit
-- disposition — this is what "nothing may be silently skipped" is checked
-- against (TOTAL_DISCOVERED_FILES == count of non-null disposition rows).
-- dataset_id is nullable: a NOISE/TOOLING/UNSUPPORTED item is never forced
-- into a dataset just to satisfy a foreign key.
CREATE TABLE discovered_files (
    discovered_file_id   TEXT PRIMARY KEY,
    batch_id              TEXT NOT NULL REFERENCES source_batches(batch_id),
    batch_root_id          TEXT NOT NULL REFERENCES batch_roots(batch_root_id),

    entry_type               TEXT NOT NULL CHECK (entry_type IN ('FILE', 'DIR', 'SYMLINK', 'OTHER')),
    absolute_path              TEXT NOT NULL,
    relative_path                TEXT NOT NULL,

    extension                     TEXT,
    mime_type                      TEXT,
    size_bytes                      INTEGER,
    sha256                           TEXT,

    dataset_id                       TEXT REFERENCES datasets(dataset_id),
    source_file_id                    TEXT REFERENCES source_files(file_id),

    disposition                        TEXT NOT NULL CHECK (disposition IN (
        'INGEST', 'REFERENCE_ONLY', 'ALREADY_INGESTED', 'EXACT_DUPLICATE',
        'NEAR_DUPLICATE', 'REVISION', 'SUPPORTING_EVIDENCE', 'SUPERSEDED',
        'NOISE', 'TOOLING', 'UNSUPPORTED', 'UNSAFE', 'HOLD'
    )),
    disposition_reason                  TEXT NOT NULL,
    duplicate_of_discovered_file_id       TEXT REFERENCES discovered_files(discovered_file_id),

    processing_status                      TEXT NOT NULL DEFAULT 'RECORDED',
    created_at                              TEXT NOT NULL,
    notes                                     TEXT
);

CREATE INDEX idx_discovered_files_batch ON discovered_files(batch_id);
CREATE INDEX idx_discovered_files_root ON discovered_files(batch_root_id);
CREATE INDEX idx_discovered_files_sha256 ON discovered_files(sha256);
CREATE INDEX idx_discovered_files_dataset ON discovered_files(dataset_id);
CREATE INDEX idx_discovered_files_disposition ON discovered_files(disposition);

-- Image-specific file-integrity layer (Layer 1 of the image pipeline).
-- One row per unique image identity (by sha256) actually inspected — exact
-- duplicate discovered_files rows point at the same visual_asset.
CREATE TABLE visual_assets (
    visual_asset_id     TEXT PRIMARY KEY,
    discovered_file_id   TEXT NOT NULL REFERENCES discovered_files(discovered_file_id),
    dataset_id             TEXT REFERENCES datasets(dataset_id),

    sha256                   TEXT NOT NULL,
    width_px                  INTEGER,
    height_px                  INTEGER,
    color_mode                  TEXT,
    image_format                  TEXT,
    orientation                     TEXT,
    exif_json                         TEXT,

    perceptual_hash                     TEXT,
    perceptual_hash_algorithm             TEXT,

    frame_sequence_id                       TEXT,
    frame_index                              INTEGER,
    visual_state_cluster_id                    TEXT,

    created_at                                  TEXT NOT NULL,
    notes                                         TEXT
);

CREATE INDEX idx_visual_assets_dataset ON visual_assets(dataset_id);
CREATE INDEX idx_visual_assets_phash ON visual_assets(perceptual_hash);
CREATE INDEX idx_visual_assets_cluster ON visual_assets(visual_state_cluster_id);

-- Layers 2 (OCR) and 3 (native semantic inspection) of the image pipeline.
-- Many rows per visual_asset — one per observation pass, never overwritten.
CREATE TABLE visual_observations (
    visual_observation_id   TEXT PRIMARY KEY,
    visual_asset_id           TEXT NOT NULL REFERENCES visual_assets(visual_asset_id),

    observation_type            TEXT NOT NULL CHECK (observation_type IN ('OCR', 'SEMANTIC_INSPECTION')),
    observation_method             TEXT NOT NULL,
    source_surface                   TEXT,

    extracted_text                     TEXT,
    confidence                           REAL,
    structured_json                        TEXT,

    evidence_layer                          TEXT NOT NULL,
    observed_at                              TEXT NOT NULL,
    notes                                      TEXT
);

CREATE INDEX idx_visual_observations_asset ON visual_observations(visual_asset_id);
CREATE INDEX idx_visual_observations_type ON visual_observations(observation_type);

-- Content-domain / editing-style / packaging classification, kept as
-- independent dimensions per Decision 016 (never collapsed into one field).
-- target_type + target_ref lets this cover a dataset, a channel, or a video
-- without forcing every classification through the Phase 1B channel/video
-- tables (most Phase 1C evidence has no registered channel/video identity).
CREATE TABLE entity_classifications (
    classification_id     TEXT PRIMARY KEY,
    dataset_id              TEXT NOT NULL REFERENCES datasets(dataset_id),
    target_type               TEXT NOT NULL CHECK (target_type IN ('DATASET', 'CHANNEL', 'VIDEO')),
    target_ref                  TEXT NOT NULL,

    content_domain                 TEXT,
    sub_niche                        TEXT,
    target_audience                    TEXT,
    content_format                       TEXT,
    packaging_style                        TEXT,
    thumbnail_style                          TEXT,
    presenter_style                            TEXT,
    editing_style                                TEXT NOT NULL DEFAULT 'UNKNOWN',

    evidence_layer                                  TEXT NOT NULL,
    source_locator                                    TEXT NOT NULL,
    created_at                                          TEXT NOT NULL,
    notes                                                 TEXT
);

CREATE INDEX idx_entity_classifications_dataset ON entity_classifications(dataset_id);

-- Per-document characterization for the training/reference corpus (PDF,
-- DOCX, MD, TXT, ...). One row per discovered document file.
CREATE TABLE document_records (
    document_id            TEXT PRIMARY KEY,
    discovered_file_id       TEXT NOT NULL REFERENCES discovered_files(discovered_file_id),
    dataset_id                 TEXT NOT NULL REFERENCES datasets(dataset_id),

    title                         TEXT,
    document_type                   TEXT,
    subject                           TEXT,
    knowledge_domains                  TEXT,
    evidence_type                        TEXT NOT NULL,
    authorship                             TEXT,
    ai_generated_indicators                  TEXT,
    relationship_notes                         TEXT,
    priority                                     TEXT,
    revision_status                                TEXT,

    content_read                                    INTEGER NOT NULL CHECK (content_read IN (0, 1)),
    created_at                                        TEXT NOT NULL,
    notes                                               TEXT
);

CREATE INDEX idx_document_records_dataset ON document_records(dataset_id);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (3, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Phase 1C multimodal batch registration: source_batches, batch_roots, discovered_files, visual_assets, visual_observations, entity_classifications, document_records.');
