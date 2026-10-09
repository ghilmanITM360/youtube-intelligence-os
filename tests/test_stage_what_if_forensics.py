import json
import sqlite3
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from source_adapters.what_if_forensic_brain import TABLE_IDS
from stage_what_if_forensics import StagingError, stage
from promote_what_if_forensics import promote


class StagingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.catalog = self.root / "catalog.db"
        with closing(sqlite3.connect(self.catalog)) as connection:
            connection.execute("CREATE TABLE videos (youtube_video_id TEXT, channel_id TEXT)")
            connection.execute("CREATE TABLE video_snapshots (video_snapshot_id TEXT, views INTEGER)")
            connection.execute("INSERT INTO videos VALUES ('existing001', 'CH-000004')")
            connection.execute("INSERT INTO video_snapshots VALUES ('snapshot001', 123)")
            connection.commit()
        sources = [
            {"source_video_id": "SRC01", "forensic_slug": "known", "sha256": "hash1",
             "candidate_youtube_video_id": "existing001",
             "canonical_youtube_video_id": "existing001", "mapping_status": "VERIFIED"},
            {"source_video_id": "SRC02", "forensic_slug": "new", "sha256": "hash2",
             "candidate_youtube_video_id": "newvideo001",
             "canonical_youtube_video_id": "newvideo001", "mapping_status": "VERIFIED"},
            {"source_video_id": "SRC03", "forensic_slug": "unknown", "sha256": "hash3",
             "candidate_youtube_video_id": None,
             "canonical_youtube_video_id": None, "mapping_status": "UNRESOLVED"},
        ]
        tables = {}
        for table, local_id in TABLE_IDS.items():
            tables[table] = [
                {"VIDEO_SLUG": "known", local_id: "ROW1", "START_SEC": "0.1",
                 "END_SEC": "0.2", "CONFIDENCE": ""},
                {"VIDEO_SLUG": "new", local_id: "ROW2", "START_SEC": "1.1",
                 "END_SEC": "1.2", "CONFIDENCE": "HIGH"},
                {"VIDEO_SLUG": "unknown", local_id: "ROW3", "START_SEC": "2.1",
                 "END_SEC": "2.2", "CONFIDENCE": "LOW"},
            ]
        self.brain = {"contract": {"source_release": "1.0.0",
                                   "release_manifest_sha256": "releasehash",
                                   "sources": sources}, "tables": tables}
        self.output = self.root / "stage"

    def test_second_run_is_identical_and_holds_unregistered_sources(self):
        first = stage(self.brain, self.catalog, self.output)
        second = stage(self.brain, self.catalog, self.output)
        self.assertEqual((first["status"], second["status"]), ("CREATED", "UNCHANGED"))
        manifest = first["manifest"]
        self.assertEqual(manifest["accepted_rows"], 8)
        self.assertEqual(manifest["excluded_rows"], 16)
        self.assertEqual(manifest["not_registered_sources"], 1)
        self.assertEqual(manifest["unresolved_sources"], 1)
        words = [json.loads(line) for line in
                 (self.output / "MASTER_WORDS.jsonl").read_text().splitlines()]
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0]["canonical_youtube_video_id"], "existing001")
        self.assertIsNone(words[0]["confidence"])
        self.assertEqual(words[0]["timing"], {"START_SEC": "0.1", "END_SEC": "0.2"})
        self.assertEqual(words[0]["source_table_row_number"], 2)
        with closing(sqlite3.connect(self.catalog)) as connection:
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM videos").fetchone()[0], 1)
            self.assertEqual(connection.execute("SELECT views FROM video_snapshots").fetchone()[0], 123)

    def test_changed_stage_requires_review_without_overwrite(self):
        stage(self.brain, self.catalog, self.output)
        before = (self.output / "manifest.json").read_bytes()
        self.brain["tables"]["MASTER_WORDS"][0]["START_SEC"] = "0.3"
        with self.assertRaisesRegex(StagingError, "DIFF_REQUIRES_REVIEW"):
            stage(self.brain, self.catalog, self.output)
        self.assertEqual((self.output / "manifest.json").read_bytes(), before)

    def test_promotion_is_small_idempotent_and_catalog_safe(self):
        stage(self.brain, self.catalog, self.output)
        index_path = self.root / "index.json"
        status, index = promote(self.output, self.catalog, index_path)
        self.assertEqual(status, "CREATED")
        self.assertEqual(index["video_count"], 1)
        self.assertEqual(index["observation_count"], 8)
        self.assertEqual(len(index["held_sources"]), 2)
        self.assertEqual(promote(self.output, self.catalog, index_path)[0], "UNCHANGED")
        with closing(sqlite3.connect(self.catalog)) as connection:
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM videos").fetchone()[0], 1)
            self.assertEqual(connection.execute("SELECT views FROM video_snapshots").fetchone()[0], 123)

    def test_promotion_rejects_tampered_stage(self):
        stage(self.brain, self.catalog, self.output)
        (self.output / "MASTER_WORDS.jsonl").write_text("tampered\n")
        with self.assertRaisesRegex(StagingError, "changed or missing stage table"):
            promote(self.output, self.catalog, self.root / "index.json")

    def test_promotion_rejects_changed_catalog_identity_set(self):
        stage(self.brain, self.catalog, self.output)
        with closing(sqlite3.connect(self.catalog)) as connection:
            connection.execute("INSERT INTO videos VALUES ('newvideo001', 'CH-000004')")
            connection.commit()
        with self.assertRaisesRegex(StagingError, "catalog identity set changed"):
            promote(self.output, self.catalog, self.root / "index.json")


if __name__ == "__main__":
    unittest.main()
