-- Phase 1B Structured Registration — migration 002 (Decisions 014, 015)
-- Additive only. Does not edit 001_initial.sql; migration history stays honest.
-- Adds: run_type on ingestion_runs, channels, channel_snapshots, videos,
-- video_snapshots, transcripts, field_provenance.

PRAGMA foreign_keys = ON;

-- Distinguish a Phase 1A file-copy run from a Phase 1B parsing run.
-- Existing rows (e.g. RUN-000001) default to FILE_INGESTION, preserving history.
ALTER TABLE ingestion_runs ADD COLUMN run_type TEXT NOT NULL DEFAULT 'FILE_INGESTION'
    CHECK (run_type IN ('FILE_INGESTION', 'STRUCTURED_REGISTRATION'));

-- One row per YouTube channel (own or competitor). Stable identity only —
-- mutable metrics live in channel_snapshots (Decision 014).
CREATE TABLE channels (
    channel_id                TEXT PRIMARY KEY,
    youtube_channel_id        TEXT UNIQUE,
    handle                    TEXT,
    display_name              TEXT NOT NULL,
    channel_url               TEXT,
    created_from_dataset_id   TEXT NOT NULL REFERENCES datasets(dataset_id),
    created_at                TEXT NOT NULL,
    updated_at                TEXT NOT NULL,
    notes                     TEXT
);

-- Point-in-time channel metrics. Never overwritten; a later ingestion of the
-- same channel appends another snapshot (Decision 014).
CREATE TABLE channel_snapshots (
    channel_snapshot_id       TEXT PRIMARY KEY,
    channel_id                TEXT NOT NULL REFERENCES channels(channel_id),
    dataset_id                TEXT NOT NULL REFERENCES datasets(dataset_id),
    registration_run_id       TEXT NOT NULL REFERENCES ingestion_runs(run_id),
    observed_at                TEXT NOT NULL,
    subscriber_count           INTEGER,
    video_count                 INTEGER,
    created_at                   TEXT NOT NULL,
    notes                         TEXT,
    UNIQUE (channel_id, dataset_id, observed_at)
);

-- One row per YouTube video, own or competitor. Stable identity only —
-- title/metrics live in video_snapshots (rule 12).
CREATE TABLE videos (
    video_id                  TEXT PRIMARY KEY,
    youtube_video_id          TEXT NOT NULL UNIQUE,
    channel_id                TEXT NOT NULL REFERENCES channels(channel_id),
    canonical_url              TEXT,
    created_from_dataset_id    TEXT NOT NULL REFERENCES datasets(dataset_id),
    created_at                  TEXT NOT NULL,
    updated_at                   TEXT NOT NULL,
    notes                         TEXT
);

-- Point-in-time video metrics, including source-computed rates (Decision 015
-- requires their origin to stay distinguishable via field_provenance).
CREATE TABLE video_snapshots (
    video_snapshot_id          TEXT PRIMARY KEY,
    video_id                   TEXT NOT NULL REFERENCES videos(video_id),
    dataset_id                  TEXT NOT NULL REFERENCES datasets(dataset_id),
    registration_run_id          TEXT NOT NULL REFERENCES ingestion_runs(run_id),

    observed_at                    TEXT NOT NULL,
    published_at                    TEXT,

    title                             TEXT,
    duration_seconds                   INTEGER,

    views                                INTEGER,
    likes                                 INTEGER,
    comments                              INTEGER,

    views_per_day                          REAL,
    engagement_rate                         REAL,

    description_char_count                   INTEGER,
    transcript_word_count                     INTEGER,

    created_at                                 TEXT NOT NULL,
    notes                                        TEXT,
    UNIQUE (video_id, dataset_id, observed_at)
);

-- One row per video's transcript registration. Never stores transcript body
-- text (rules 15, 33) — the canonical ZIP archive member remains evidence.
CREATE TABLE transcripts (
    transcript_id               TEXT PRIMARY KEY,
    video_id                    TEXT NOT NULL REFERENCES videos(video_id),
    dataset_id                   TEXT NOT NULL REFERENCES datasets(dataset_id),
    registration_run_id           TEXT NOT NULL REFERENCES ingestion_runs(run_id),

    archive_member_file_id          TEXT NOT NULL REFERENCES source_files(file_id),

    availability_status               TEXT NOT NULL CHECK (availability_status IN ('AVAILABLE', 'UNAVAILABLE')),
    caption_type                        TEXT,
    language                             TEXT,
    word_count                            INTEGER,

    transcript_sha256                      TEXT,
    description_present                     INTEGER CHECK (description_present IN (0, 1)),

    created_at                                TEXT NOT NULL,
    notes                                       TEXT,
    UNIQUE (video_id, dataset_id, registration_run_id)
);

-- Traces every meaningful structured value back to its exact source
-- location (Decision 015). Exactly one target entity must be populated.
CREATE TABLE field_provenance (
    provenance_id                TEXT PRIMARY KEY,

    dataset_id                    TEXT NOT NULL REFERENCES datasets(dataset_id),
    registration_run_id             TEXT NOT NULL REFERENCES ingestion_runs(run_id),
    source_file_id                    TEXT REFERENCES source_files(file_id),

    channel_id                          TEXT REFERENCES channels(channel_id),
    channel_snapshot_id                   TEXT REFERENCES channel_snapshots(channel_snapshot_id),
    video_id                                TEXT REFERENCES videos(video_id),
    video_snapshot_id                         TEXT REFERENCES video_snapshots(video_snapshot_id),
    transcript_id                               TEXT REFERENCES transcripts(transcript_id),

    field_name                                    TEXT NOT NULL,
    source_locator                                  TEXT NOT NULL,

    value_origin                                      TEXT NOT NULL CHECK (value_origin IN (
        'SOURCE_EXTRACTED', 'SOURCE_DECLARED', 'SOURCE_COMPUTED',
        'TRANSCRIPT_METADATA', 'ARCHIVE_OBSERVED', 'SYSTEM_VERIFIED'
    )),
    evidence_layer                                      TEXT NOT NULL,
    extraction_method                                     TEXT,

    observed_at                                             TEXT,
    created_at                                                TEXT NOT NULL,
    notes                                                       TEXT,

    CHECK (
        (CASE WHEN channel_id IS NOT NULL THEN 1 ELSE 0 END) +
        (CASE WHEN channel_snapshot_id IS NOT NULL THEN 1 ELSE 0 END) +
        (CASE WHEN video_id IS NOT NULL THEN 1 ELSE 0 END) +
        (CASE WHEN video_snapshot_id IS NOT NULL THEN 1 ELSE 0 END) +
        (CASE WHEN transcript_id IS NOT NULL THEN 1 ELSE 0 END) = 1
    )
);

CREATE INDEX idx_channel_snapshots_channel ON channel_snapshots(channel_id);
CREATE INDEX idx_videos_channel ON videos(channel_id);
CREATE INDEX idx_video_snapshots_video ON video_snapshots(video_id);
CREATE INDEX idx_transcripts_video ON transcripts(video_id);
CREATE INDEX idx_transcripts_archive_member ON transcripts(archive_member_file_id);
CREATE INDEX idx_field_provenance_dataset ON field_provenance(dataset_id);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (2, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Phase 1B structured registration: run_type on ingestion_runs, channels, channel_snapshots, videos, video_snapshots, transcripts, field_provenance.');
