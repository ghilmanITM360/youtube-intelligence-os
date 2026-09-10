-- Supplied channel exports can carry thumbnail references and transcript timing
-- quality without a retained direct Apify run.

PRAGMA foreign_keys = ON;

ALTER TABLE video_snapshots ADD COLUMN thumbnail_url TEXT;
ALTER TABLE transcripts ADD COLUMN timing_quality TEXT CHECK (
    timing_quality IN ('EXACT_TIMESTAMPED', 'SEGMENT_TIMESTAMPED', 'POSITIONAL_ONLY', 'INSUFFICIENT_TIMING')
);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (10, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Register supplied thumbnail references and transcript timing quality without fabricating an acquisition run.');
