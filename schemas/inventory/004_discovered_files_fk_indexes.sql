-- Phase 1C follow-up (additive only). Adds indexes on the two
-- discovered_files foreign-key columns that 003 left unindexed
-- (duplicate_of_discovered_file_id is self-referencing; source_file_id
-- references source_files). Without these, SQLite's foreign-key
-- enforcement on DELETE FROM discovered_files degrades to an O(n^2) table
-- scan per deleted row — observed directly during batch-rebuild testing on
-- a ~46,000-row table, which never completed in reasonable time. Indexing
-- both columns is required, not merely a performance nicety, before this
-- table can be safely mutated at real batch scale.

CREATE INDEX idx_discovered_files_dup_of ON discovered_files(duplicate_of_discovered_file_id);
CREATE INDEX idx_discovered_files_source_file ON discovered_files(source_file_id);

INSERT INTO schema_meta (schema_version, applied_at, description) VALUES
    (4, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), 'Index discovered_files.duplicate_of_discovered_file_id and discovered_files.source_file_id — required for FK-checked DELETEs to complete at batch scale.');
