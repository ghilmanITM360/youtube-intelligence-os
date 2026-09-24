"""Provenance and non-enforcement checks for global corpus DS-000031."""

import hashlib
import json
import sqlite3
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "data/intelligence/global/creator-strategy-knowledge-DS-000031.json"
VALIDATION = ROOT / "data/intelligence/global/creator-strategy-primary-validation-2026-09-24.json"
OLD_TRAINING = ROOT / "data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json"
NEW_TRAINING = ROOT / "data/intelligence/system/youtube-strategy-training-knowledge-2026-09-24.json"


class CreatorStrategyKnowledgeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(KNOWLEDGE.read_text(encoding="utf-8"))
        cls.raw = ROOT / cls.data["raw_path"]
        cls.lines = cls.raw.read_text(encoding="utf-8").split("\n")

    def test_raw_and_manifest(self):
        self.assertTrue((ROOT / "data/manifests/DS-000031.md").is_file())
        payload = self.raw.read_bytes()
        self.assertEqual(len(payload), self.data["raw_size_bytes"])
        self.assertEqual(payload.count(b"\n"), self.data["raw_lf_count"])
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.data["raw_sha256"])
        manifest = (ROOT / "data/manifests/DS-000031.md").read_text(encoding="utf-8")
        self.assertIn(self.data["raw_sha256"], manifest)

    def test_all_locators_and_ids(self):
        segments = {item["id"]: item for item in self.data["segments"]}
        concepts = {item["id"]: item for item in self.data["concepts"]}
        self.assertEqual(len(segments), len(self.data["segments"]))
        self.assertEqual(len(concepts), len(self.data["concepts"]))
        for segment in segments.values():
            start, end = segment["lines"]
            self.assertTrue(1 <= start <= end <= len(self.lines))
        for concept in concepts.values():
            self.assertEqual(concept["id"].startswith("CS-"), True)
            self.assertTrue(concept["name"] and concept["type"] and concept["status"] and concept["use"])
            self.assertTrue(any(segments[ref]["lines"][0] <= concept["line"] <= segments[ref]["lines"][1] for ref in concept["segments"]))
        for formula in self.data["formulas"]:
            self.assertIn(formula["text"], self.lines[formula["line"] - 1])
            self.assertIn(formula["concept"], concepts)
        for row in self.data["numeric_heuristics"]:
            self.assertIn(row["concept"], concepts)
            self.assertFalse(row["enforce"])
        for row in self.data["examples"]:
            self.assertIn(row["concept"], concepts)
            self.assertIn(row["segment"], segments)
        for row in self.data["relationships"]:
            self.assertIn(row["from"], concepts)
            self.assertIn(row["to"], concepts)

    def test_validation_is_separate_and_source_heuristics_not_rules(self):
        validation = json.loads(VALIDATION.read_text(encoding="utf-8"))
        sources = {row["id"] for row in validation["primary_sources"]}
        concepts = {row["id"] for row in self.data["concepts"]}
        self.assertEqual(validation["dataset_id"], "DS-000031")
        for row in validation["checks"]:
            self.assertIn(row["concept"], concepts)
            self.assertTrue(set(row["official_sources"]) <= sources)
        self.assertFalse(self.data["scorecard"]["platform_verified"])
        self.assertFalse(self.data["scorecard"]["enforced"])

    def test_historical_training_preserved_and_no_channel_link(self):
        old = json.loads(OLD_TRAINING.read_text(encoding="utf-8"))
        new = json.loads(NEW_TRAINING.read_text(encoding="utf-8"))
        self.assertEqual(old["rules"], new["rules"][:len(old["rules"])])
        added = new["rules"][len(old["rules"]):]
        self.assertTrue(added)
        self.assertTrue(all(row["SOURCE_ID"] == "DS-000031" for row in added))
        db = ROOT / "data/catalog/youtube_inventory.db"
        if db.is_file():
            with sqlite3.connect(f"file:{db}?mode=ro", uri=True) as conn:
                self.assertEqual(conn.execute("SELECT COUNT(*) FROM channel_dataset_links WHERE dataset_id='DS-000031'").fetchone()[0], 0)
                self.assertEqual(conn.execute("SELECT COUNT(*) FROM datasets WHERE dataset_id='DS-000031' AND semantic_class='A'").fetchone()[0], 1)

    def test_freshness_registry_tracks_new_artifacts_without_runtime_promotion(self):
        registry = json.loads((ROOT / "data/intelligence/system/intelligence-freshness-registry.json").read_text(encoding="utf-8"))
        global_rows = [row for row in registry["artifacts"] if row["ARTIFACT_TYPE"] == "GLOBAL_KNOWLEDGE"]
        self.assertEqual(len(global_rows), 3)
        self.assertTrue(all(any(self.data["raw_path"] in dep["ref"] for dep in row["SOURCE_DEPENDENCIES"]) for row in global_rows))
        runtime_training = [row for row in registry["artifacts"] if row["ARTIFACT_TYPE"] == "TRAINING_KNOWLEDGE"]
        self.assertEqual(len(runtime_training), 1)
        self.assertEqual(runtime_training[0]["PATH"], str(OLD_TRAINING.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
