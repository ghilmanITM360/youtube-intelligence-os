-- Controlled Apify YouTube acquisition (additive only).
-- Reuses the Phase 1 catalog and append-only snapshot model. Raw Actor payloads
-- remain in Apify; this catalog stores normalized facts, hashes, and provenance.

PRAGMA foreign_keys = ON;

ALTER TABLE video_snapshots ADD COLUMN description TEXT;
ALTER TABLE video_snapshots ADD COLUMN video_type TEXT;

ALTER TABLE transcripts ADD COLUMN transcript_format TEXT;
ALTER TABLE transcripts ADD COLUMN transcript_source TEXT NOT NULL DEFAULT 'SUPPLIED_ARCHIVE';
ALTER TABLE transcripts ADD COLUMN canonical_reference TEXT;

CREATE TABLE apify_source_runs (
    apify_source_run_id          TEXT PRIMARY KEY,
    registration_run_id          TEXT NOT NULL UNIQUE REFERENCES ingestion_runs(run_id),
    dataset_id                   TEXT NOT NULL REFERENCES datasets(dataset_id),

    actor_name                   TEXT NOT NULL,
    actor_id                     TEXT NOT NULL,
    actor_run_id                 TEXT NOT NULL UNIQUE,
    actor_build_id               TEXT,
    actor_build_number           TEXT,
    actor_build_version          TEXT,

    started_at                   TEXT NOT NULL,
    finished_at                  TEXT,
    observed_at                  TEXT NOT NULL,
    input_json                   TEXT NOT NULL,
    result_record_count          INTEGER NOT NULL,
    run_status                   TEXT NOT NULL,
    run_cost_usd                 REAL,
    channel_url                  TEXT NOT NULL,
    transcript_configuration_json TEXT NOT NULL,
    default_dataset_id           TEXT,
    run_console_url              TEXT,

    source                       TEXT NOT NULL CHECK (source = 'APIFY'),
    extraction_provider          TEXT NOT NULL CHECK (extraction_provider = 'streamers/youtube-scraper'),
    created_at                   TEXT NOT NULL,
    notes                        TEXT
);

CREATE INDEX idx_apify_source_runs_dataset ON apify_source_runs(dataset_id);

CREATE TABLE channel_dataset_links (
    channel_id          TEXT NOT NULL REFERENCES channels(channel_id),
    dataset_id          TEXT NOT NULL REFERENCES datasets(dataset_id),
    relationship_type   TEXT NOT NULL CHECK (relationship_type IN (
        'CREATED_FROM', 'IDENTITY_EVIDENCE', 'STRUCTURED_OBSERVATION'
    )),
    source_locator      TEXT NOT NULL,
    evidence_layer      TEXT NOT NULL,
    created_at          TEXT NOT NULL,
    notes               TEXT,
    PRIMARY KEY (channel_id, dataset_id, relationship_type)
);

INSERT OR IGNORE INTO channel_dataset_links
    (channel_id, dataset_id, relationship_type, source_locator, evidence_layer, created_at, notes)
SELECT channel_id, created_from_dataset_id, 'CREATED_FROM',
       'channels.created_from_dataset_id', 'EXTRACTED_FACT', created_at, NULL
FROM channels;

CREATE TABLE apify_result_records (
    apify_result_record_id  TEXT PRIMARY KEY,
    apify_source_run_id     TEXT NOT NULL REFERENCES apify_source_runs(apify_source_run_id),
    video_id                TEXT NOT NULL REFERENCES videos(video_id),
    record_index            INTEGER NOT NULL,
    raw_record_sha256       TEXT NOT NULL,
    observed_at             TEXT NOT NULL,
    created_at              TEXT NOT NULL,
    UNIQUE (apify_source_run_id, video_id),
    UNIQUE (apify_source_run_id, record_index)
);

CREATE INDEX idx_apify_result_records_video ON apify_result_records(video_id);

CREATE TABLE thumbnail_evidence (
    thumbnail_evidence_id   TEXT PRIMARY KEY,
    video_id                TEXT NOT NULL REFERENCES videos(video_id),
    dataset_id              TEXT NOT NULL REFERENCES datasets(dataset_id),
    registration_run_id     TEXT NOT NULL REFERENCES ingestion_runs(run_id),
    apify_source_run_id     TEXT NOT NULL REFERENCES apify_source_runs(apify_source_run_id),
    thumbnail_url           TEXT NOT NULL,
    source                  TEXT NOT NULL CHECK (source = 'APIFY'),
    extraction_provider     TEXT NOT NULL CHECK (extraction_provider = 'streamers/youtube-scraper'),
    extraction_method       TEXT NOT NULL,
    observed_at             TEXT NOT NULL,
    created_at              TEXT NOT NULL,
    UNIQUE (video_id, apify_source_run_id, thumbnail_url)
);

CREATE INDEX idx_thumbnail_evidence_video ON thumbnail_evidence(video_id);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (5, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Controlled Apify YouTube acquisition: run/record provenance, channel-dataset identity links, descriptions, transcript references, and thumbnail evidence.');
