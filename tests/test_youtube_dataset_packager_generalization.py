import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPO_ROOT / "scripts" / "package_youtube_channel_dataset.mjs"
LEGACY_GENERATOR = REPO_ROOT / "scripts" / "package_five_channel_youtube_dataset.mjs"


class YouTubeDatasetPackagerGeneralizationTests(unittest.TestCase):
    def run_config_validation(self, config):
        with tempfile.TemporaryDirectory() as directory:
            config_path = Path(directory) / "config.json"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            return subprocess.run(
                ["node", str(GENERATOR), "--config", str(config_path), "--validate-config-only"],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

    def test_accepts_any_channel_count_and_derives_deterministic_names(self):
        config = {
            "datasetId": "DS-TEST",
            "datasetName": "Test YouTube Dataset",
            "collectionDate": "2026-09-12",
            "actor": "streamers/youtube-scraper",
            "run": {"id": "run1", "datasetId": "dataset1", "status": "SUCCEEDED"},
            "channels": [
                {"name": "Alpha Channel", "handle": "@alpha", "channelId": "UCalpha", "expectedCount": 2},
                {"name": "Beta & Co.", "handle": "@beta", "channelId": "UCbeta", "expectedCount": 3},
            ],
        }
        result = self.run_config_validation(config)
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output["channelCount"], 2)
        self.assertEqual(output["totalExpectedVideos"], 5)
        self.assertEqual(output["channels"][0]["slug"], "alpha-channel")
        self.assertEqual(output["channels"][0]["workbook"], "AlphaChannel_Master_Data.xlsx")
        self.assertEqual(output["channels"][1]["zip"], "BetaCo_Transcripts_3_Videos.zip")

    def test_rejects_duplicate_channel_ids(self):
        config = {
            "datasetId": "DS-TEST",
            "datasetName": "Test YouTube Dataset",
            "collectionDate": "2026-09-12",
            "actor": "streamers/youtube-scraper",
            "run": {"id": "run1", "datasetId": "dataset1", "status": "SUCCEEDED"},
            "channels": [
                {"name": "Alpha", "handle": "@alpha", "channelId": "UCsame", "expectedCount": 1},
                {"name": "Beta", "handle": "@beta", "channelId": "UCsame", "expectedCount": 1},
            ],
        }
        result = self.run_config_validation(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate channel ID", result.stderr)

    def test_csv_serialization_strips_line_end_whitespace_without_changing_content(self):
        result = subprocess.run(
            ["node", str(GENERATOR), "--normalize-csv-value", "first  \nsecond\t\nthird"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.rstrip("\n"), '"first\nsecond\nthird"')

    def test_recovery_can_add_a_proven_missing_video(self):
        config = {
            "datasetId": "DS-TEST",
            "datasetName": "Test YouTube Dataset",
            "collectionDate": "2026-09-13",
            "actor": "streamers/youtube-scraper",
            "run": {"id": "run1", "datasetId": "dataset1", "status": "SUCCEEDED"},
            "channels": [
                {"name": "Alpha", "handle": "@alpha", "channelId": "UCalpha", "expectedCount": 2},
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = root / "config.json"
            raw_path = root / "raw.json"
            recovery_path = root / "recovery.json"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            raw_path.write_text(json.dumps([{"id": "aaaaaaaaaaa", "title": "A"}]), encoding="utf-8")
            recovery_path.write_text(json.dumps([{"id": "bbbbbbbbbbb", "title": "B"}]), encoding="utf-8")
            result = subprocess.run(
                [
                    "node", str(GENERATOR), "--config", str(config_path),
                    "--raw-json", str(raw_path), "--recovery-raw-json", str(recovery_path),
                    "--validate-record-merge-only",
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output["mergedVideoCount"], 2)
        self.assertEqual(output["recoveryAddedVideoIds"], ["bbbbbbbbbbb"])

    def test_ds000020_reproduction_generator_stays_byte_identical(self):
        digest = hashlib.sha256(LEGACY_GENERATOR.read_bytes()).hexdigest()
        self.assertEqual(digest, "f8ae62c98f693d4cf396557c71bc5c9f9803d8bb36a8ee65fe5affca45e66994")


if __name__ == "__main__":
    unittest.main()
