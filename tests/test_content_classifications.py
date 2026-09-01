"""Focused regression test for the Phase 2 classification foundation."""
import sqlite3
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "schemas" / "inventory"
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


if __name__ == "__main__":
    unittest.main()
