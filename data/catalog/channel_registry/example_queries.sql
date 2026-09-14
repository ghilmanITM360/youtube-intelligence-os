-- 1. Target channels with complete extraction status
SELECT channel_name,canonical_url,extraction_status,package_status
FROM channels
WHERE target_group<>'OUTSIDE_TARGET' AND extraction_status='COMPLETE'
ORDER BY channel_name;

-- 2. Target channels awaiting extraction
SELECT channel_name,canonical_channel_id,canonical_url,target_group
FROM channels
WHERE target_group<>'OUTSIDE_TARGET' AND extraction_status='NOT_EXTRACTED'
ORDER BY target_group,channel_name;

-- 3. Standard-package channels
SELECT channel_name,canonical_channel_id,package_status
FROM channels WHERE source_group='STANDARD_PACKAGE' ORDER BY channel_name;

-- 4. Historical-format channels
SELECT channel_name,c.canonical_channel_id,group_concat(dc.dataset_id) AS dataset_ids
FROM channels c JOIN dataset_channels dc USING(canonical_channel_id)
WHERE source_group='HISTORICAL_CATALOG'
GROUP BY c.canonical_channel_id ORDER BY channel_name;

-- 5. Channels with real transcripts
SELECT channel_name,real_transcript_count,transcript_status
FROM v_channel_status WHERE real_transcript_count>0 ORDER BY channel_name;

-- 6. Channels with transcript placeholders
SELECT channel_name,placeholder_count,transcript_status
FROM v_channel_status WHERE placeholder_count>0 ORDER BY channel_name;

-- 7. Channels with missing descriptions
SELECT channel_name,missing_description_count,description_status
FROM v_channel_status WHERE missing_description_count>0 ORDER BY channel_name;

-- 8. Channels having only thumbnail URLs, not downloaded evidence
SELECT c.channel_name,v.thumbnail_url_count,v.downloaded_thumbnail_count,v.visual_evidence_level
FROM channels c JOIN visual_coverage v USING(canonical_channel_id)
WHERE v.visual_evidence_level='THUMBNAIL_URL_ONLY' ORDER BY c.channel_name;

-- 9. Channels having downloaded thumbnail evidence
SELECT c.channel_name,v.downloaded_thumbnail_count,v.evidence_path
FROM channels c JOIN visual_coverage v USING(canonical_channel_id)
WHERE v.downloaded_thumbnail_count>0 ORDER BY c.channel_name;

-- 10. Channels having forensic video evidence
SELECT c.channel_name,c.canonical_channel_id,v.keyframe_count,v.registered_source_video_count,
       v.timestamped_visual_observation_count,v.evidence_path,v.limitation_reason
FROM channels c JOIN visual_coverage v USING(canonical_channel_id)
WHERE v.visual_evidence_level='FORENSIC_VIDEO_EVIDENCE';

-- 11. Screenshot-only unmapped subjects
SELECT subject_name,subject_id,evidence_source,limitation
FROM non_channel_subjects ORDER BY subject_id;

-- 12. Channels with each generated intelligence capability
SELECT cap.capability_name,c.channel_name,ic.status,ic.evidence_path
FROM intelligence_coverage ic
JOIN intelligence_capabilities cap USING(capability_id)
JOIN channels c USING(canonical_channel_id)
WHERE ic.generated_artifact_available=1
ORDER BY cap.capability_id,c.channel_name;

-- 13. Capability input exists but output is not generated
SELECT cap.capability_name,c.channel_name,ic.status,ic.evidence_path,ic.limitation_reason
FROM intelligence_coverage ic
JOIN intelligence_capabilities cap USING(capability_id)
JOIN channels c USING(canonical_channel_id)
WHERE ic.input_data_available=1 AND ic.generated_artifact_available=0
ORDER BY cap.capability_id,c.channel_name;

-- 14. First-party Analytics status; public metrics are not first-party Analytics
SELECT first_party_analytics_status,count(*) AS channel_count
FROM channels GROUP BY first_party_analytics_status;

-- 15. All data gaps for one channel
SELECT * FROM v_channel_data_gaps
WHERE canonical_channel_id=:channel_id ORDER BY field_name;

-- 16a. Transcript full-text search when registry_metadata.fts5_enabled='1'
SELECT t.youtube_video_id,v.title,snippet(transcript_fts,0,'[',']',' … ',12) AS match
FROM transcript_fts
JOIN transcripts t ON t.transcript_id=transcript_fts.rowid
JOIN videos v USING(youtube_video_id)
WHERE transcript_fts MATCH :phrase LIMIT 50;

-- 16b. Standard-SQL fallback when FTS5 is unavailable
SELECT t.youtube_video_id,v.title
FROM transcripts t JOIN videos v USING(youtube_video_id)
WHERE lower(t.transcript_text) LIKE '%' || lower(:phrase) || '%' LIMIT 50;

-- 17. Original-44 versus additional-19 progress
SELECT 'ORIGINAL_TARGET' AS target_group,extraction_status,count(*) AS channels
FROM channels WHERE target_group='ORIGINAL_TARGET' GROUP BY extraction_status
UNION ALL
SELECT 'ADDED_TARGET',extraction_status,count(*)
FROM channels WHERE target_group='ADDED_TARGET' GROUP BY extraction_status
ORDER BY target_group,extraction_status;

-- Alias audit for one canonical channel
SELECT global_row,batch,batch_row,original_url,is_exact_duplicate,duplicate_of_global_row
FROM submissions WHERE canonical_channel_id=:channel_id ORDER BY global_row;
