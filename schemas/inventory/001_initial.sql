-- Phase 1 Inventory Catalog — initial schema (Decision 012)
-- Minimal, migration-friendly. Do not add tables here beyond what Phase 1
-- actually requires; see docs/Database.md §5 for what is deliberately deferred.

PRAGMA foreign_keys = ON;

-- Tracks which schema files have been applied, in order.
CREATE TABLE schema_meta (
    schema_version  INTEGER PRIMARY KEY,
    applied_at      TEXT NOT NULL,
    description     TEXT NOT NULL
);

-- One row per logical dataset (e.g. DS-000001). Never one row per file.
CREATE TABLE datasets (
    dataset_id      TEXT PRIMARY KEY,
    dataset_name    TEXT NOT NULL,
    semantic_class  TEXT NOT NULL,
    description     TEXT,
    source_type     TEXT NOT NULL,
    ingestion_mode  TEXT NOT NULL,
    status          TEXT NOT NULL,
    discovered_as   TEXT,
    date_received   TEXT NOT NULL,
    created_at      TEXT NOT NULL,
    updated_at      TEXT NOT NULL,
    notes           TEXT
);

-- One row per ingestion attempt against a dataset. Never fake COMPLETED.
-- dataset_id is nullable: an attempt that fails before a dataset record is
-- created (e.g. a hash-verification failure during the very first ingest of
-- a new Dataset ID) is still logged, with the attempted ID kept in `notes`.
CREATE TABLE ingestion_runs (
    run_id                TEXT PRIMARY KEY,
    dataset_id            TEXT REFERENCES datasets(dataset_id),
    started_at            TEXT NOT NULL,
    completed_at          TEXT,
    status                TEXT NOT NULL CHECK (status IN ('STARTED', 'COMPLETED', 'PARTIAL', 'FAILED', 'ROLLED_BACK')),
    source_file_count     INTEGER,
    archive_member_count  INTEGER,
    total_size_bytes      INTEGER,
    errors_count          INTEGER NOT NULL DEFAULT 0,
    verification_status   TEXT,
    tool_version          TEXT NOT NULL,
    notes                 TEXT
);

-- Where a dataset's source originally came from. The external path is
-- evidence, not a guarantee it will exist forever — hence the local copy.
CREATE TABLE source_locations (
    source_location_id  TEXT PRIMARY KEY,
    dataset_id           TEXT NOT NULL REFERENCES datasets(dataset_id),
    original_path        TEXT NOT NULL,
    location_type         TEXT NOT NULL,
    exists_at_ingestion   INTEGER NOT NULL CHECK (exists_at_ingestion IN (0, 1)),
    observed_at            TEXT NOT NULL,
    notes                  TEXT
);

-- The most important table: one row per physical file OR archive member.
CREATE TABLE source_files (
    file_id               TEXT PRIMARY KEY,
    dataset_id            TEXT NOT NULL REFERENCES datasets(dataset_id),
    ingestion_run_id      TEXT NOT NULL REFERENCES ingestion_runs(run_id),
    parent_file_id        TEXT REFERENCES source_files(file_id),

    storage_kind          TEXT NOT NULL CHECK (storage_kind IN ('PHYSICAL_FILE', 'ARCHIVE_MEMBER')),
    file_role             TEXT NOT NULL,

    original_filename     TEXT NOT NULL,
    original_path         TEXT NOT NULL,
    relative_path         TEXT,

    canonical_path        TEXT,
    archive_member_path   TEXT,

    extension             TEXT,
    mime_type              TEXT,

    size_bytes             INTEGER NOT NULL,
    sha256                 TEXT,

    semantic_class          TEXT,
    evidence_layer           TEXT,

    is_copied                INTEGER NOT NULL DEFAULT 0 CHECK (is_copied IN (0, 1)),
    is_archive_member         INTEGER NOT NULL DEFAULT 0 CHECK (is_archive_member IN (0, 1)),

    processing_status          TEXT NOT NULL,
    verification_status        TEXT NOT NULL,

    created_at                  TEXT NOT NULL,
    notes                        TEXT
);

CREATE INDEX idx_source_files_dataset ON source_files(dataset_id);
CREATE INDEX idx_source_files_parent ON source_files(parent_file_id);
CREATE INDEX idx_source_files_sha256 ON source_files(sha256);

-- Only relationships actually proven during ingestion. Never invented.
CREATE TABLE file_relationships (
    relationship_id    TEXT PRIMARY KEY,
    from_file_id        TEXT NOT NULL REFERENCES source_files(file_id),
    to_file_id           TEXT NOT NULL REFERENCES source_files(file_id),
    relationship_type     TEXT NOT NULL CHECK (relationship_type IN (
        'EXACT_DUPLICATE_OF', 'PROBABLE_DUPLICATE_OF', 'REVISION_OF',
        'ARCHIVE_OF', 'CONTAINS', 'DERIVED_FROM', 'SUPERSEDES', 'RELATED_TO'
    )),
    confidence             TEXT,
    evidence                TEXT,
    created_at                TEXT NOT NULL,
    notes                      TEXT
);

-- Error taxonomy per docs/Error_Handling.md. Never write secrets here.
-- dataset_id is nullable for the same reason as ingestion_runs.dataset_id.
CREATE TABLE ingestion_errors (
    error_id                 TEXT PRIMARY KEY,
    run_id                    TEXT NOT NULL REFERENCES ingestion_runs(run_id),
    dataset_id                TEXT REFERENCES datasets(dataset_id),
    file_id                    TEXT REFERENCES source_files(file_id),
    error_type                  TEXT NOT NULL,
    severity                     TEXT NOT NULL,
    message                       TEXT NOT NULL,
    retryable                      INTEGER NOT NULL CHECK (retryable IN (0, 1)),
    requires_human_review           INTEGER NOT NULL CHECK (requires_human_review IN (0, 1)),
    created_at                       TEXT NOT NULL,
    resolved_at                       TEXT,
    notes                              TEXT
);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (1, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Initial Phase 1 inventory catalog: datasets, ingestion_runs, source_locations, source_files, file_relationships, ingestion_errors.');
