"""Focused regression tests for Phase 2 content classifications."""
import hashlib
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "schemas" / "inventory"
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import classify_content_pilot as pilot  # noqa: E402
import inventory_catalog as ic  # noqa: E402

TS = "2026-09-01T00:00:00.000Z"


class ContentClassificationTest(unittest.TestCase):
    def test_creation_provenance_and_evidence_layers(self):
        with tempfile.TemporaryDirectory() as tmp:
            conn = sqlite3.connect(str(Path(tmp) / "catalog.db"))
            conn.execute("PRAGMA foreign_keys = ON")
            for schema in sorted(SCHEMA_DIR.glob("*.sql")):
                conn.executescript(schema.read_text(encoding="utf-8"))

            conn.execute(
                "INSERT INTO datasets "
                "(dataset_id,dataset_name,semantic_class,source_type,ingestion_mode,status,"
                "date_received,created_at,updated_at) VALUES "
                "('DS-TEST','fixture','B','TEST','TEST','INGESTED',?,?,?)",
                (TS, TS, TS),
            )
            conn.execute(
                "INSERT INTO ingestion_runs "
                "(run_id,dataset_id,started_at,status,errors_count,tool_version,run_type) "
                "VALUES ('RUN-TEST','DS-TEST',?,'COMPLETED',0,'test','FILE_INGESTION')",
                (TS,),
            )
            conn.execute(
                "INSERT INTO source_files "
                "(file_id,dataset_id,ingestion_run_id,storage_kind,file_role,original_filename,"
                "original_path,size_bytes,sha256,semantic_class,evidence_layer,is_copied,"
                "is_archive_member,processing_status,verification_status,created_at) VALUES "
                "('FILE-TEST','DS-TEST','RUN-TEST','PHYSICAL_FILE','TEST','fixture.json',"
                "'fixture.json',2,?,'B','RAW_SOURCE',0,0,'CATALOGED','VERIFIED',?)",
                ("a" * 64, TS),
            )
            conn.execute(
                "INSERT INTO channels VALUES "
                "('CH-TEST','UC_TEST','@test','Fixture',NULL,'DS-TEST',?,?,NULL)",
                (TS, TS),
            )
            conn.execute(
                "INSERT INTO videos VALUES "
                "('VID-TEST','video_test','CH-TEST',NULL,'DS-TEST',?,?,NULL)",
                (TS, TS),
            )

            rows = [
                ("CC-TOPIC", "CONTENT_TOPIC", "RETIREMENT_PLANNING", "AI_INTERPRETATION", "PROPOSED", "topic-prompt", "prompt-v1"),
                ("CC-FORMAT", "CONTENT_FORMAT", "SHORT_FORM", "MEASURED_FACT", "VERIFIED", "duration-threshold", "duration-rule-v1"),
            ]
            conn.executemany(
                "INSERT INTO content_classifications "
                "(classification_id,video_id,dataset_id,source_file_id,classification_dimension,"
                "classification_value,evidence_layer,classification_status,source_locator,"
                "classification_method,method_version,reproducibility_status,created_at) "
                "VALUES (?,'VID-TEST','DS-TEST','FILE-TEST',?,?,?,?,"
                "'fixture.json#records[0]',?,?, 'REPRODUCIBLE',?)",
                [row + (TS,) for row in rows],
            )

            actual = conn.execute(
                "SELECT cc.classification_dimension,cc.classification_value,cc.evidence_layer,"
                "cc.classification_status,sf.sha256,cc.reproducibility_status "
                "FROM content_classifications cc "
                "JOIN source_files sf ON sf.file_id=cc.source_file_id "
                "WHERE cc.video_id='VID-TEST' ORDER BY cc.classification_dimension"
            ).fetchall()
            self.assertEqual(actual, [
                ("CONTENT_FORMAT", "SHORT_FORM", "MEASURED_FACT", "VERIFIED", "a" * 64, "REPRODUCIBLE"),
                ("CONTENT_TOPIC", "RETIREMENT_PLANNING", "AI_INTERPRETATION", "PROPOSED", "a" * 64, "REPRODUCIBLE"),
            ])
            self.assertEqual(conn.execute("PRAGMA foreign_key_check").fetchall(), [])
            conn.close()

    def test_pilot_vocabulary_provenance_and_idempotency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_path = root / "catalog.db"
            metadata = root / "metadata.json"
            transcript = root / "transcript.txt"
            metadata.write_text('{"duration_seconds": 1200}', encoding="utf-8")
            transcript.write_text("Evidence about blood pressure medication timing.", encoding="utf-8")

            conn = sqlite3.connect(str(db_path))
            conn.execute("PRAGMA foreign_keys = ON")
            for schema in sorted(SCHEMA_DIR.glob("*.sql")):
                conn.executescript(schema.read_text(encoding="utf-8"))
            conn.execute(
                "INSERT INTO datasets (dataset_id,dataset_name,semantic_class,source_type,ingestion_mode,status,"
                "date_received,created_at,updated_at) VALUES "
                "('DS-TEST','fixture','B','TEST','TEST','INGESTED',?,?,?)",
                (TS, TS, TS),
            )
            conn.execute(
                "INSERT INTO ingestion_runs (run_id,dataset_id,started_at,status,errors_count,tool_version,run_type) "
                "VALUES ('RUN-TEST','DS-TEST',?,'COMPLETED',0,'test','FILE_INGESTION')",
                (TS,),
            )
            for file_id, path, role in (
                ("FILE-METADATA", metadata, "STRUCTURED_METADATA"),
                ("FILE-TRANSCRIPT", transcript, "TRANSCRIPT"),
            ):
                conn.execute(
                    "INSERT INTO source_files (file_id,dataset_id,ingestion_run_id,storage_kind,file_role,"
                    "original_filename,original_path,canonical_path,size_bytes,sha256,semantic_class,evidence_layer,"
                    "is_copied,is_archive_member,processing_status,verification_status,created_at) VALUES "
                    "(?,'DS-TEST','RUN-TEST','PHYSICAL_FILE',?,?,?,?,?,?,'B','RAW_SOURCE',1,0,'CATALOGED','VERIFIED',?)",
                    (file_id, role, path.name, str(path), str(path), path.stat().st_size,
                     hashlib.sha256(path.read_bytes()).hexdigest(), TS),
                )
            conn.execute(
                "INSERT INTO channels VALUES "
                "('CH-TEST','UC_TEST','@test','Fixture',NULL,'DS-TEST',?,?,NULL)",
                (TS, TS),
            )
            conn.execute(
                "INSERT INTO videos VALUES "
                "('VID-TEST','video_test','CH-TEST',NULL,'DS-TEST',?,?,NULL)",
                (TS, TS),
            )
            conn.execute(
                "INSERT INTO video_snapshots (video_snapshot_id,video_id,dataset_id,registration_run_id,"
                "observed_at,title,duration_seconds,created_at,description,video_type) VALUES "
                "('VS-TEST','VID-TEST','DS-TEST','RUN-TEST',?,'Blood pressure timing',1200,?,"
                "'A sourced description.','video')",
                (TS, TS),
            )
            conn.execute(
                "INSERT INTO transcripts (transcript_id,video_id,dataset_id,registration_run_id,"
                "archive_member_file_id,availability_status,transcript_sha256,created_at,transcript_source,"
                "canonical_reference) VALUES "
                "('TR-TEST','VID-TEST','DS-TEST','RUN-TEST','FILE-TRANSCRIPT','AVAILABLE',?,?,"
                "'APIFY',?)",
                (hashlib.sha256(transcript.read_bytes()).hexdigest(), TS, str(transcript)),
            )
            conn.execute(
                "INSERT INTO field_provenance (provenance_id,dataset_id,registration_run_id,source_file_id,"
                "video_snapshot_id,field_name,source_locator,value_origin,evidence_layer,extraction_method,created_at) "
                "VALUES ('FP-TEST','DS-TEST','RUN-TEST','FILE-METADATA','VS-TEST','duration_seconds',"
                "'fixture.json#items[0]','SOURCE_EXTRACTED','EXTRACTED_FACT','fixture',?)",
                (TS,),
            )
            conn.commit()
            conn.close()

            item = {"video_id": "VID-TEST", "youtube_video_id": "video_test", "dataset_id": "DS-TEST",
                    "video_snapshot_id": "VS-TEST", "topic": "CARDIOVASCULAR_HEALTH"}
            with self.assertRaisesRegex(ic.CatalogError, "outside the pilot vocabulary"):
                pilot.classify_pilot(db_path, (dict(item, topic="UNCONTROLLED"),))

            conn = sqlite3.connect(str(db_path))
            conn.execute("UPDATE source_files SET verification_status='FAILED' WHERE file_id='FILE-TRANSCRIPT'")
            conn.commit()
            conn.close()
            with self.assertRaisesRegex(ic.CatalogError, "incomplete or unverified"):
                pilot.classify_pilot(db_path, (item,))

            conn = sqlite3.connect(str(db_path))
            conn.execute("UPDATE source_files SET verification_status='VERIFIED' WHERE file_id='FILE-TRANSCRIPT'")
            conn.commit()
            conn.close()
            first = pilot.classify_pilot(db_path, (item,))
            second = pilot.classify_pilot(db_path, (item,))
            self.assertEqual(first, {"items": 1, "created": 2, "classifications": 2})
            self.assertEqual(second, {"items": 1, "created": 0, "classifications": 2})

            conn = sqlite3.connect(str(db_path))
            rows = conn.execute(
                "SELECT classification_dimension,classification_value,evidence_layer,classification_status,"
                "reproducibility_status FROM content_classifications ORDER BY classification_dimension"
            ).fetchall()
            self.assertEqual(rows, [
                ("CONTENT_FORMAT", "LONG_FORM", "MEASURED_FACT", "VERIFIED", "REPRODUCIBLE"),
                ("CONTENT_TOPIC", "CARDIOVASCULAR_HEALTH", "AI_INTERPRETATION", "PROPOSED", "NON_REPRODUCIBLE"),
            ])
            self.assertEqual(conn.execute("PRAGMA foreign_key_check").fetchall(), [])
            conn.close()


if __name__ == "__main__":
    unittest.main()
