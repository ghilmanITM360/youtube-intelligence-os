-- Proven dataset-level relationships belong in the Phase 1 inventory catalog,
-- without merging, renaming, or deleting either dataset.

PRAGMA foreign_keys = ON;

CREATE TABLE dataset_relationships (
    relationship_id    TEXT PRIMARY KEY,
    from_dataset_id     TEXT NOT NULL REFERENCES datasets(dataset_id),
    to_dataset_id       TEXT NOT NULL REFERENCES datasets(dataset_id),
    relationship_type    TEXT NOT NULL CHECK (relationship_type IN (
        'SAME_SOURCE_INDEPENDENT_ANALYSIS', 'REVISION_OF',
        'DUPLICATE_DATASET', 'RELATED_BUT_UNRESOLVED'
    )),
    confidence            TEXT NOT NULL,
    status                 TEXT NOT NULL CHECK (status IN ('PROVEN', 'UNRESOLVED')),
    evidence               TEXT NOT NULL,
    source_locator         TEXT NOT NULL,
    created_at             TEXT NOT NULL,
    notes                  TEXT,
    CHECK (from_dataset_id <> to_dataset_id),
    UNIQUE (from_dataset_id, to_dataset_id, relationship_type)
);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (7, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Proven dataset-level evidence relationships without merging dataset identities.');
