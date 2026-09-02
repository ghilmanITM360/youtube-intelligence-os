-- Phase 2 batch classification: one active value per content dimension.

PRAGMA foreign_keys = ON;

CREATE UNIQUE INDEX uq_content_classifications_active_dimension
    ON content_classifications(video_id, classification_dimension)
    WHERE classification_status IN ('PROPOSED', 'VERIFIED');

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (9, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Prevent duplicate or conflicting active content classifications per video and dimension.');
