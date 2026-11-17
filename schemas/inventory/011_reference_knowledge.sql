-- Reference knowledge framework (v1): source members, locator-addressed sections, rules,
-- conflicts, platform-verification receipts and video/plan assessments. Additive only.
-- Rebuilt by research/finance-economics-intelligence/reference-framework/build_reference_kb.py.

PRAGMA foreign_keys = ON;

CREATE TABLE ref_source_member (
    member_id           TEXT PRIMARY KEY,
    filename            TEXT NOT NULL,
    sha256              TEXT NOT NULL UNIQUE,
    size_bytes          INTEGER NOT NULL,
    pages_or_chunks     INTEGER NOT NULL,
    document_id         TEXT REFERENCES document_records(document_id),
    source_id           TEXT,
    canonical_member_id TEXT REFERENCES ref_source_member(member_id),
    dedupe_group        TEXT,
    disposition         TEXT NOT NULL CHECK (disposition IN ('PROCESSED_CANONICAL','PROCESSED_ALIAS','PROCESSED_WITH_UNREAD_IMAGES','PARTIAL')),
    extraction_note     TEXT
);

CREATE TABLE ref_section (
    section_id          TEXT PRIMARY KEY,
    member_id           TEXT NOT NULL REFERENCES ref_source_member(member_id),
    locator             TEXT NOT NULL,
    ordinal             INTEGER NOT NULL,
    extraction_status   TEXT NOT NULL CHECK (extraction_status IN ('TEXT_EXTRACTED','TEXT_EXTRACTED_WITH_IMAGES_UNREAD','IMAGE_ONLY_UNRESOLVED','EMPTY_OR_SPARSE')),
    char_count          INTEGER NOT NULL,
    image_count         INTEGER NOT NULL DEFAULT 0,
    text_sha256         TEXT NOT NULL,
    raw_text            TEXT,
    UNIQUE (member_id, locator)
);
CREATE INDEX idx_ref_section_member ON ref_section(member_id);
CREATE VIRTUAL TABLE ref_section_fts USING fts5(raw_text, content='ref_section', content_rowid='rowid');

CREATE TABLE ref_constituent_video (
    cv_id        TEXT PRIMARY KEY,
    member_id    TEXT NOT NULL REFERENCES ref_source_member(member_id),
    ordinal      INTEGER NOT NULL,
    title        TEXT NOT NULL,
    start_line   INTEGER NOT NULL,
    end_line     INTEGER NOT NULL,
    UNIQUE (member_id, ordinal)
);

CREATE TABLE ref_rule (
    rule_id            TEXT NOT NULL,
    framework_version  TEXT NOT NULL,
    member_id          TEXT REFERENCES ref_source_member(member_id),
    locator            TEXT NOT NULL,
    meaning            TEXT NOT NULL,
    audit_dimension    TEXT NOT NULL,
    rule_class         TEXT NOT NULL CHECK (rule_class IN ('CREATIVE_HEURISTIC','OWNER_PREFERENCE','PLATFORM_CLAIM','EMPIRICAL_HYPOTHESIS','TOOL_SPECIFIC_PRODUCTION','DUPLICATED_OR_SUPERSEDED','NOT_APPLICABLE')),
    evidence_required  TEXT NOT NULL,
    applicability      TEXT NOT NULL,
    PRIMARY KEY (rule_id, framework_version)
);

CREATE TABLE ref_rule_conflict (
    conflict_id   TEXT PRIMARY KEY,
    rule_a        TEXT NOT NULL,
    rule_b        TEXT NOT NULL,
    framework_version TEXT NOT NULL,
    relation      TEXT NOT NULL CHECK (relation IN ('DIFFERENT_SCALE','CONTRADICTORY','SUPERSEDES','OVERLAP')),
    note          TEXT NOT NULL,
    FOREIGN KEY (rule_a, framework_version) REFERENCES ref_rule(rule_id, framework_version),
    FOREIGN KEY (rule_b, framework_version) REFERENCES ref_rule(rule_id, framework_version)
);

CREATE TABLE ref_platform_verification (
    claim_id      TEXT PRIMARY KEY,
    member_id     TEXT REFERENCES ref_source_member(member_id),
    locator       TEXT NOT NULL,
    assertion     TEXT NOT NULL,
    official_url  TEXT NOT NULL,
    verdict       TEXT NOT NULL CHECK (verdict IN ('SUPPORTED','PARTLY_SUPPORTED','CONTRADICTED_IN_PART','CONTRADICTED','UNVERIFIED_NOT_ON_OFFICIAL_PAGES')),
    evidence_note TEXT NOT NULL,
    audit_use     TEXT NOT NULL,
    accessed      TEXT NOT NULL
);

CREATE TABLE ref_analysis_run (
    run_id             TEXT PRIMARY KEY,
    framework_version  TEXT NOT NULL,
    population_hash    TEXT NOT NULL,
    base_commit        TEXT NOT NULL,
    started_at         TEXT NOT NULL,
    note               TEXT
);

CREATE TABLE ref_video_assessment (
    assessment_id  TEXT PRIMARY KEY,
    run_id         TEXT NOT NULL REFERENCES ref_analysis_run(run_id),
    video_id       TEXT NOT NULL,
    rule_id        TEXT NOT NULL,
    framework_version TEXT NOT NULL,
    judgment       TEXT NOT NULL CHECK (judgment IN ('MET','PARTLY_MET','NOT_MET','NOT_EVALUABLE','NOT_APPLICABLE','EVIDENCE_UNAVAILABLE')),
    witness_kind   TEXT,
    witness_start  INTEGER,
    witness_end    INTEGER,
    witness_text   TEXT,
    rationale      TEXT NOT NULL,
    uncertainty    TEXT NOT NULL,
    FOREIGN KEY (rule_id, framework_version) REFERENCES ref_rule(rule_id, framework_version)
);
CREATE INDEX idx_ref_assessment_video ON ref_video_assessment(video_id);

CREATE TABLE ref_plan_application (
    application_id  TEXT PRIMARY KEY,
    plan_id         TEXT NOT NULL,
    stage           TEXT NOT NULL CHECK (stage IN ('TOPIC','TITLE_THUMBNAIL','HOOK_SCRIPT','STORYBOARD_EDIT','PAYOFF_CTA','SOURCE_ACCURACY','POST_PUBLICATION')),
    rule_id         TEXT NOT NULL,
    framework_version TEXT NOT NULL,
    implementation  TEXT NOT NULL,
    exception_note  TEXT,
    FOREIGN KEY (rule_id, framework_version) REFERENCES ref_rule(rule_id, framework_version),
    UNIQUE (plan_id, stage, rule_id)
);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (11, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Reference knowledge framework v1: source members, sections with locators, rules, conflicts, platform verification, video assessments and plan applications.');
