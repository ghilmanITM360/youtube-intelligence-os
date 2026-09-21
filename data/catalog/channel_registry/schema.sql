PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS registry_metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS channels (
  canonical_channel_id TEXT PRIMARY KEY,
  channel_name TEXT NOT NULL,
  current_handle TEXT,
  canonical_url TEXT NOT NULL UNIQUE,
  source_group TEXT NOT NULL CHECK (source_group IN ('STANDARD_PACKAGE','HISTORICAL_CATALOG','IDENTITY_ONLY')),
  target_group TEXT NOT NULL CHECK (target_group IN ('ORIGINAL_TARGET','ADDED_TARGET','OUTSIDE_TARGET')),
  status TEXT NOT NULL CHECK (status IN (
    'COMPLETE','COMPLETE_WITH_LIMITATIONS','PARTIAL',
    'IDENTITY_VERIFIED_DATA_NOT_EXTRACTED','PENDING_IDENTITY_RESOLUTION',
    'UNAVAILABLE_OR_DELETED'
  )),
  completed_tick TEXT NOT NULL CHECK (completed_tick IN ('','✓')),
  identity_status TEXT NOT NULL CHECK (identity_status IN ('VERIFIED','UNRESOLVED','UNAVAILABLE')),
  extraction_status TEXT NOT NULL CHECK (extraction_status IN ('COMPLETE','COMPLETE_WITH_LIMITATIONS','PARTIAL','NOT_EXTRACTED')),
  package_status TEXT NOT NULL CHECK (package_status IN ('STANDARD_PACKAGE','HISTORICAL_FORMAT','NO_PACKAGE')),
  video_metadata_status TEXT NOT NULL CHECK (video_metadata_status IN ('COMPLETE','COMPLETE_WITH_LIMITATIONS','PARTIAL','NONE')),
  description_status TEXT NOT NULL CHECK (description_status IN ('COMPLETE','PARTIAL','NONE')),
  transcript_status TEXT NOT NULL CHECK (transcript_status IN ('COMPLETE_REAL','COMPLETE_WITH_PLACEHOLDERS','PARTIAL','NONE')),
  thumbnail_metadata_status TEXT NOT NULL CHECK (thumbnail_metadata_status IN ('COMPLETE','PARTIAL','NONE')),
  visual_asset_status TEXT NOT NULL CHECK (visual_asset_status IN ('NONE','THUMBNAIL_URL_ONLY','THUMBNAIL_EVIDENCE','FORENSIC_VIDEO_EVIDENCE')),
  forensic_video_status TEXT NOT NULL CHECK (forensic_video_status IN ('AVAILABLE_WITH_LIMITATIONS','NOT_AVAILABLE')),
  intelligence_status TEXT NOT NULL CHECK (intelligence_status IN ('VALIDATED','AVAILABLE','PARTIAL','DATA_READY','NOT_AVAILABLE','NOT_APPLICABLE')),
  first_party_analytics_status TEXT NOT NULL CHECK (first_party_analytics_status IN ('INGESTED','SCHEMA_READY_NO_DATA','NOT_CONFIGURED')),
  identity_verified_at TEXT,
  identity_evidence_source TEXT NOT NULL,
  handle_unavailable_reason TEXT,
  limitations TEXT
);

CREATE TABLE IF NOT EXISTS channel_data_layers (
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  layer_name TEXT NOT NULL CHECK (layer_name IN (
    'identity_status','extraction_status','package_status','video_metadata_status',
    'description_status','transcript_status','thumbnail_metadata_status',
    'visual_asset_status','forensic_video_status','intelligence_status',
    'first_party_analytics_status'
  )),
  status TEXT NOT NULL,
  evidence_path TEXT NOT NULL,
  limitation_reason TEXT,
  last_verified_at TEXT NOT NULL,
  PRIMARY KEY(canonical_channel_id,layer_name)
);

CREATE TABLE IF NOT EXISTS submissions (
  global_row INTEGER PRIMARY KEY,
  batch TEXT NOT NULL CHECK (batch IN ('A','B')),
  batch_row INTEGER NOT NULL,
  original_url TEXT NOT NULL,
  normalized_url TEXT NOT NULL,
  is_exact_duplicate INTEGER NOT NULL CHECK (is_exact_duplicate IN (0,1)),
  duplicate_of_global_row INTEGER REFERENCES submissions(global_row),
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  identity_status TEXT NOT NULL,
  evidence_source TEXT NOT NULL,
  verified_at TEXT,
  UNIQUE(batch,batch_row)
);

CREATE TABLE IF NOT EXISTS channel_aliases (
  alias_id INTEGER PRIMARY KEY,
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  alias_url TEXT NOT NULL,
  alias_kind TEXT NOT NULL,
  submission_global_row INTEGER REFERENCES submissions(global_row),
  UNIQUE(canonical_channel_id,alias_url,submission_global_row)
);

CREATE TABLE IF NOT EXISTS identity_evidence (
  evidence_id INTEGER PRIMARY KEY,
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  source_type TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  verified_at TEXT,
  observed_name TEXT,
  observed_handle TEXT,
  raw_json TEXT,
  UNIQUE(canonical_channel_id,source_type,source_locator)
);

CREATE TABLE IF NOT EXISTS datasets (
  dataset_id TEXT PRIMARY KEY,
  dataset_name TEXT NOT NULL,
  manifest_path TEXT NOT NULL,
  evidence_scope TEXT,
  limitations TEXT
);

CREATE TABLE IF NOT EXISTS dataset_channels (
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  relationship TEXT NOT NULL,
  PRIMARY KEY(dataset_id,canonical_channel_id,relationship)
);

CREATE TABLE IF NOT EXISTS actor_runs (
  actor_run_id TEXT PRIMARY KEY,
  actor_dataset_id TEXT,
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  actor_name TEXT,
  evidence_path TEXT,
  run_status TEXT,
  raw_json TEXT
);

CREATE TABLE IF NOT EXISTS videos (
  youtube_video_id TEXT PRIMARY KEY,
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  canonical_url TEXT NOT NULL,
  title TEXT,
  published_at TEXT,
  duration_seconds INTEGER,
  video_type TEXT,
  views INTEGER,
  likes INTEGER,
  comments INTEGER,
  description TEXT,
  description_unavailable_reason TEXT,
  thumbnail_url TEXT,
  raw_json TEXT
);

CREATE TABLE IF NOT EXISTS dataset_videos (
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  youtube_video_id TEXT NOT NULL REFERENCES videos(youtube_video_id),
  evidence_locator TEXT,
  PRIMARY KEY(dataset_id,youtube_video_id)
);

CREATE TABLE IF NOT EXISTS transcripts (
  transcript_id INTEGER PRIMARY KEY,
  youtube_video_id TEXT NOT NULL REFERENCES videos(youtube_video_id),
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  transcript_text TEXT,
  word_count INTEGER,
  language TEXT,
  caption_type TEXT,
  is_placeholder INTEGER NOT NULL CHECK (is_placeholder IN (0,1)),
  unavailable_reason TEXT,
  evidence_locator TEXT NOT NULL,
  transcript_sha256 TEXT,
  UNIQUE(youtube_video_id,dataset_id)
);

CREATE TABLE IF NOT EXISTS subtitle_tracks (
  subtitle_track_id INTEGER PRIMARY KEY,
  youtube_video_id TEXT NOT NULL REFERENCES videos(youtube_video_id),
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  language TEXT,
  track_type TEXT,
  raw_json TEXT,
  UNIQUE(youtube_video_id,dataset_id,language,track_type)
);

CREATE TABLE IF NOT EXISTS artifacts (
  artifact_id INTEGER PRIMARY KEY,
  dataset_id TEXT REFERENCES datasets(dataset_id),
  canonical_channel_id TEXT REFERENCES channels(canonical_channel_id),
  artifact_type TEXT NOT NULL,
  repository_path TEXT NOT NULL,
  sha256 TEXT,
  availability_status TEXT NOT NULL,
  unavailable_reason TEXT,
  UNIQUE(dataset_id,canonical_channel_id,artifact_type,repository_path)
);

CREATE TABLE IF NOT EXISTS availability_gaps (
  gap_id INTEGER PRIMARY KEY,
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  field_name TEXT NOT NULL,
  unavailable_reason TEXT NOT NULL,
  evidence_source TEXT NOT NULL,
  UNIQUE(canonical_channel_id,field_name,unavailable_reason)
);

CREATE TABLE IF NOT EXISTS intelligence_capabilities (
  capability_id TEXT PRIMARY KEY,
  capability_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS intelligence_coverage (
  canonical_channel_id TEXT NOT NULL REFERENCES channels(canonical_channel_id),
  capability_id TEXT NOT NULL REFERENCES intelligence_capabilities(capability_id),
  status TEXT NOT NULL CHECK (status IN ('VALIDATED','AVAILABLE','PARTIAL','DATA_READY','NOT_AVAILABLE','NOT_APPLICABLE')),
  input_data_available INTEGER NOT NULL CHECK (input_data_available IN (0,1)),
  generated_artifact_available INTEGER NOT NULL CHECK (generated_artifact_available IN (0,1)),
  evidence_path TEXT NOT NULL,
  limitation_reason TEXT,
  last_verified_at TEXT NOT NULL,
  PRIMARY KEY(canonical_channel_id,capability_id)
);

CREATE TABLE IF NOT EXISTS visual_coverage (
  canonical_channel_id TEXT PRIMARY KEY REFERENCES channels(canonical_channel_id),
  thumbnail_url_count INTEGER NOT NULL CHECK (thumbnail_url_count >= 0),
  downloaded_thumbnail_count INTEGER NOT NULL CHECK (downloaded_thumbnail_count >= 0),
  screenshot_count INTEGER NOT NULL CHECK (screenshot_count >= 0),
  keyframe_count INTEGER NOT NULL CHECK (keyframe_count >= 0),
  registered_source_video_count INTEGER NOT NULL CHECK (registered_source_video_count >= 0),
  timestamped_visual_observation_count INTEGER NOT NULL CHECK (timestamped_visual_observation_count >= 0),
  visual_evidence_level TEXT NOT NULL CHECK (visual_evidence_level IN ('NONE','THUMBNAIL_URL_ONLY','THUMBNAIL_EVIDENCE','FORENSIC_VIDEO_EVIDENCE')),
  editing_visual_intelligence_status TEXT NOT NULL CHECK (editing_visual_intelligence_status IN ('PARTIAL','NOT_AVAILABLE')),
  evidence_path TEXT NOT NULL,
  limitation_reason TEXT
);

CREATE TABLE IF NOT EXISTS non_channel_subjects (
  subject_id TEXT PRIMARY KEY,
  subject_name TEXT NOT NULL,
  canonical_channel_id TEXT,
  identity_status TEXT NOT NULL,
  evidence_source TEXT NOT NULL,
  limitation TEXT NOT NULL,
  CHECK (canonical_channel_id IS NULL)
);

CREATE TABLE IF NOT EXISTS subject_datasets (
  subject_id TEXT NOT NULL REFERENCES non_channel_subjects(subject_id),
  dataset_id TEXT NOT NULL REFERENCES datasets(dataset_id),
  PRIMARY KEY(subject_id,dataset_id)
);

CREATE INDEX IF NOT EXISTS idx_channels_status ON channels(status);
CREATE INDEX IF NOT EXISTS idx_videos_channel ON videos(canonical_channel_id);
CREATE INDEX IF NOT EXISTS idx_transcripts_video ON transcripts(youtube_video_id);
CREATE INDEX IF NOT EXISTS idx_artifacts_channel ON artifacts(canonical_channel_id);

CREATE VIEW IF NOT EXISTS v_channel_status AS
SELECT c.*,
       COUNT(DISTINCT v.youtube_video_id) AS video_count,
       COUNT(DISTINCT CASE WHEN t.is_placeholder=0 THEN t.youtube_video_id END) AS real_transcript_count,
       COUNT(DISTINCT CASE WHEN t.is_placeholder=1 THEN t.youtube_video_id END) AS placeholder_count,
       COUNT(DISTINCT CASE
         WHEN v.description IS NULL
          AND COALESCE(v.description_unavailable_reason,'') NOT LIKE 'Description verified present in historical coverage;%'
         THEN v.youtube_video_id END) AS missing_description_count
FROM channels c
LEFT JOIN videos v ON v.canonical_channel_id=c.canonical_channel_id
LEFT JOIN transcripts t ON t.youtube_video_id=v.youtube_video_id
GROUP BY c.canonical_channel_id;

CREATE VIEW IF NOT EXISTS v_completed_channels AS
SELECT * FROM v_channel_status WHERE status='COMPLETE';

CREATE VIEW IF NOT EXISTS v_pending_channels AS
SELECT * FROM v_channel_status
WHERE status IN ('COMPLETE_WITH_LIMITATIONS','PARTIAL','IDENTITY_VERIFIED_DATA_NOT_EXTRACTED','PENDING_IDENTITY_RESOLUTION','UNAVAILABLE_OR_DELETED');

CREATE VIEW IF NOT EXISTS v_channel_data_gaps AS
SELECT c.canonical_channel_id,c.channel_name,c.status,g.field_name,g.unavailable_reason,g.evidence_source
FROM channels c JOIN availability_gaps g USING(canonical_channel_id);

CREATE VIEW IF NOT EXISTS v_original_target_progress AS
SELECT status,COUNT(*) AS channel_count FROM channels WHERE target_group='ORIGINAL_TARGET' GROUP BY status;

CREATE VIEW IF NOT EXISTS v_added_target_progress AS
SELECT status,COUNT(*) AS channel_count FROM channels WHERE target_group='ADDED_TARGET' GROUP BY status;

CREATE VIEW IF NOT EXISTS v_dataset_summary AS
SELECT d.dataset_id,d.dataset_name,
       COUNT(DISTINCT dc.canonical_channel_id) AS channel_count,
       COUNT(DISTINCT dv.youtube_video_id) AS video_count,
       COUNT(DISTINCT CASE WHEN t.is_placeholder=0 THEN t.youtube_video_id END) AS real_transcript_count,
       COUNT(DISTINCT CASE WHEN t.is_placeholder=1 THEN t.youtube_video_id END) AS placeholder_count
FROM datasets d
LEFT JOIN dataset_channels dc ON dc.dataset_id=d.dataset_id
LEFT JOIN dataset_videos dv ON dv.dataset_id=d.dataset_id
LEFT JOIN transcripts t ON t.dataset_id=d.dataset_id AND t.youtube_video_id=dv.youtube_video_id
GROUP BY d.dataset_id;

CREATE VIEW IF NOT EXISTS v_video_transcript_status AS
SELECT v.youtube_video_id,v.canonical_channel_id,v.title,v.canonical_url,v.description,
       CASE WHEN t.transcript_id IS NULL THEN 'MISSING'
            WHEN t.is_placeholder=1 THEN 'PLACEHOLDER' ELSE 'AVAILABLE' END AS transcript_status,
       t.word_count,t.unavailable_reason,t.evidence_locator
FROM videos v LEFT JOIN transcripts t USING(youtube_video_id);

CREATE VIEW IF NOT EXISTS v_channel_artifacts AS
SELECT c.canonical_channel_id,c.channel_name,a.dataset_id,a.artifact_type,a.repository_path,a.availability_status,a.unavailable_reason
FROM channels c JOIN artifacts a USING(canonical_channel_id);

CREATE VIEW IF NOT EXISTS v_intelligence_coverage AS
SELECT c.canonical_channel_id,c.channel_name,cap.capability_id,cap.capability_name,
       COALESCE(ic.status,'NOT_AVAILABLE') AS status,
       COALESCE(ic.input_data_available,0) AS input_data_available,
       COALESCE(ic.generated_artifact_available,0) AS generated_artifact_available,
       ic.evidence_path,ic.limitation_reason,ic.last_verified_at
FROM channels c CROSS JOIN intelligence_capabilities cap
LEFT JOIN intelligence_coverage ic
  ON ic.canonical_channel_id=c.canonical_channel_id AND ic.capability_id=cap.capability_id;
