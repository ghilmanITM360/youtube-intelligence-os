-- Phase 2 classification foundation: repeatable, provenance-linked assertions
-- about registered YouTube content. No corpus classifications are populated here.

PRAGMA foreign_keys = ON;

CREATE TABLE content_classifications (
    classification_id       TEXT PRIMARY KEY,
    video_id                TEXT NOT NULL REFERENCES videos(video_id),
    dataset_id              TEXT NOT NULL REFERENCES datasets(dataset_id),
    source_file_id          TEXT NOT NULL REFERENCES source_files(file_id),

    classification_dimension TEXT NOT NULL CHECK (
        classification_dimension IN ('CONTENT_TOPIC', 'CONTENT_FORMAT')
    ),
    classification_value    TEXT NOT NULL CHECK (length(trim(classification_value)) > 0),
    evidence_layer          TEXT NOT NULL CHECK (evidence_layer IN (
        'EXTRACTED_FACT', 'MEASURED_FACT', 'OBSERVATION',
        'AI_INTERPRETATION', 'HUMAN_INTERPRETATION'
    )),
    classification_status   TEXT NOT NULL CHECK (classification_status IN (
        'PROPOSED', 'VERIFIED', 'REJECTED', 'SUPERSEDED'
    )),

    source_locator          TEXT NOT NULL CHECK (length(trim(source_locator)) > 0),
    classification_method   TEXT NOT NULL CHECK (length(trim(classification_method)) > 0),
    method_version          TEXT,
    reproducibility_status  TEXT NOT NULL CHECK (
        reproducibility_status IN ('REPRODUCIBLE', 'NON_REPRODUCIBLE')
    ),
    created_at              TEXT NOT NULL,
    notes                   TEXT,

    CHECK (
        reproducibility_status = 'NON_REPRODUCIBLE'
        OR length(trim(method_version)) > 0
    )
);

CREATE INDEX idx_content_classifications_video
    ON content_classifications(video_id, classification_dimension);
CREATE INDEX idx_content_classifications_source
    ON content_classifications(source_file_id);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (8, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Phase 2 content classification foundation: provenance-linked topic and format assertions with evidence, status, and reproducibility metadata.');
