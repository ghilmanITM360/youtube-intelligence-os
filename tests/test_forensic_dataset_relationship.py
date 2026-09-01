"""Focused regression test for the proven sunset-video dataset relationship."""
import hashlib
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import classify_forensic_dataset_relationship as classifier  # noqa: E402
import inventory_catalog as ic  # noqa: E402


class Args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ForensicDatasetRelationshipTest(unittest.TestCase):
    def test_records_relationship_idempotently_without_merging_datasets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db_path = root / "catalog.db"
            ic.cmd_init(Args(db_path=str(db_path)))
            reports = {}
            for dataset_id, content in (("DS-000012", b"case one"), ("DS-000015", b"case two")):
                path = root / (dataset_id + ".md")
                path.write_bytes(content)
                reports[dataset_id] = (path, hashlib.sha256(content).hexdigest())

            conn = sqlite3.connect(str(db_path))
            now = "2026-09-01T00:00:00.000Z"
            with conn:
                for index, dataset_id in enumerate(classifier.EXPECTED_DATASETS, 1):
                    conn.execute(
                        "INSERT INTO datasets (dataset_id,dataset_name,semantic_class,description,source_type,"
                        "ingestion_mode,status,discovered_as,date_received,created_at,updated_at,notes) "
                        "VALUES (?,?,'C',NULL,'EXTERNAL_FOLDER','SELECTIVE_COPY','INGESTED',?,?,?,?,NULL)",
                        (dataset_id, "Independent case {}".format(index), "CASE{}".format(index), now, now, now),
                    )
                    run_id = "RUN-{:06d}".format(index)
                    conn.execute(
                        "INSERT INTO ingestion_runs (run_id,dataset_id,started_at,completed_at,status,"
                        "source_file_count,archive_member_count,total_size_bytes,errors_count,verification_status,"
                        "tool_version,notes,run_type) VALUES (?,?,?,?,'COMPLETED',1,0,?,0,'VERIFIED','test',NULL,'FILE_INGESTION')",
                        (run_id, dataset_id, now, now, reports[dataset_id][0].stat().st_size),
                    )
                    conn.execute(
                        "INSERT INTO source_files (file_id,dataset_id,ingestion_run_id,parent_file_id,storage_kind,"
                        "file_role,original_filename,original_path,relative_path,canonical_path,archive_member_path,"
                        "extension,mime_type,size_bytes,sha256,semantic_class,evidence_layer,is_copied,is_archive_member,"
                        "processing_status,verification_status,created_at,notes) "
                        "VALUES (?,?,?,NULL,'PHYSICAL_FILE','SUPPORTING_EVIDENCE',?,?,?,?,NULL,'.md','text/markdown',"
                        "?,?,'C','RAW_SOURCE',1,0,'CATALOGED','VERIFIED',?,NULL)",
                        ("FILE-{:06d}".format(index), dataset_id, run_id, reports[dataset_id][0].name,
                         str(reports[dataset_id][0]), reports[dataset_id][0].name, str(reports[dataset_id][0]),
                         reports[dataset_id][0].stat().st_size, reports[dataset_id][1], now),
                    )
            before = conn.execute("SELECT dataset_id,dataset_name FROM datasets ORDER BY dataset_id").fetchall()
            source_owners = conn.execute("SELECT file_id,dataset_id FROM source_files ORDER BY file_id").fetchall()
            conn.close()

            source_hash = "9" * 64
            manifest = {
                "forensic_relationships": [
                    {"dataset_id": dataset_id, "youtube_video_id": "rGZ6TsXvi8E", "source_sha256": source_hash,
                     "status": "PROVEN"}
                    for dataset_id in classifier.EXPECTED_DATASETS
                ],
                "forensic_dataset_relationships": [{
                    "relationship_id": "DSREL-000001",
                    "dataset_ids": list(classifier.EXPECTED_DATASETS),
                    "relationship_type": "SAME_SOURCE_INDEPENDENT_ANALYSIS",
                    "confidence": "HIGH",
                    "status": "PROVEN",
                    "youtube_video_id": "rGZ6TsXvi8E",
                    "source_sha256": source_hash,
                    "source_locator": "fixture.json#forensic_dataset_relationships[0]",
                    "evidence": "same immutable source; distinct analyses",
                    "notes": "Datasets remain independent.",
                    "canonical_reports": [
                        {"dataset_id": dataset_id, "relative_path": reports[dataset_id][0].name,
                         "sha256": reports[dataset_id][1]}
                        for dataset_id in classifier.EXPECTED_DATASETS
                    ],
                }],
            }
            manifest_path = root / "fixture.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            first = classifier.record_relationship(db_path, manifest_path)
            second = classifier.record_relationship(db_path, manifest_path)
            self.assertEqual(first["relationship_id"], second["relationship_id"])
            conn = sqlite3.connect(str(db_path))
            relationship = conn.execute(
                "SELECT relationship_type,confidence,status,from_dataset_id,to_dataset_id "
                "FROM dataset_relationships"
            ).fetchall()
            self.assertEqual(relationship, [(
                "SAME_SOURCE_INDEPENDENT_ANALYSIS", "HIGH", "PROVEN", "DS-000012", "DS-000015"
            )])
            self.assertEqual(conn.execute("SELECT dataset_id,dataset_name FROM datasets ORDER BY dataset_id").fetchall(), before)
            self.assertEqual(conn.execute("SELECT file_id,dataset_id FROM source_files ORDER BY file_id").fetchall(), source_owners)
            conn.close()


if __name__ == "__main__":
    unittest.main()
