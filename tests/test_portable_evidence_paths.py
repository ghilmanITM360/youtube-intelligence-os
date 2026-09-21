import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_youtube_channel_registry as registry
import report_editing_visual_intelligence as editing


class PortableEvidencePathTests(unittest.TestCase):
    def test_readonly_registry_connect_does_not_create_missing_database(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.db"
            with self.assertRaisesRegex(FileNotFoundError, "missing or empty"):
                registry.connect_readonly(missing)
            self.assertFalse(missing.exists())

    def test_historical_reference_rebases_to_selected_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = Path("data/raw/competitors/DS-000001/sample.txt")
            source = root / relative
            source.parent.mkdir(parents=True)
            source.write_text("Transcript sample", encoding="utf-8")
            row = {
                "canonical_reference": str(source), "archive_member_path": None,
                "youtube_video_id": "sample12345", "youtube_channel_id": "UCsample",
                "canonical_url": "https://youtube.com/watch?v=sample12345", "dataset_id": "DS-000001",
                "title": "Sample", "published_at": None, "duration_seconds": 10,
                "video_type": "video", "views": 1, "likes": 0, "comments": 0,
                "description": "Sample", "thumbnail_url": None,
                "availability_status": "AVAILABLE", "caption_type": None, "language": "en",
                "word_count": 2, "transcript_sha256": None, "notes": None,
            }

            class Connection:
                row_factory = None

                def execute(self, _sql):
                    return [row]

                def close(self):
                    pass

            for reference in (str(source), "/Users/legacy/youtube-intelligence-os/" + relative.as_posix()):
                row["canonical_reference"] = reference
                videos, transcripts, memberships = registry._historical_records(root, source=Connection())
                self.assertEqual(1, len(videos))
                self.assertEqual("Transcript sample", transcripts[0]["transcript_text"])
                self.assertEqual(relative.as_posix(), transcripts[0]["evidence_locator"])
                self.assertEqual(relative.as_posix(), memberships[0]["evidence_locator"])

    def test_forensic_report_and_states_resolve_in_selected_worktree_from_other_cwd(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as elsewhere:
            root = Path(directory)
            relative = Path("data/raw/forensic-analysis/DS-000013/frames")
            report = root / relative / "report.md"
            states_file = root / relative / "state_manifest.tsv"
            report.parent.mkdir(parents=True)
            report.write_text("| V01 | Sample visual |\n", encoding="utf-8")
            states_file.write_text("visual\trepresentative\nV01\t1.5\n", encoding="utf-8")
            rows = [
                {"dataset_id": "DS-000013", "original_filename": "report.md", "extension": "md",
                 "original_path": "/Users/ghilmankhan/old/report.md", "canonical_path": "/Users/ghilmankhan/old/copy.md",
                 "relative_path": "frames/report.md", "is_copied": 1, "file_id": 1, "sha256": "a"},
                {"dataset_id": "DS-000013", "original_filename": "state_manifest.tsv", "extension": "tsv",
                 "original_path": "/Users/ghilmankhan/old/state_manifest.tsv", "canonical_path": "/Users/ghilmankhan/old/copy.tsv",
                 "relative_path": "frames/state_manifest.tsv", "is_copied": 1, "file_id": 2, "sha256": "b"},
            ]
            old_cwd = Path.cwd()
            try:
                os.chdir(elsewhere)
                self.assertEqual(report.resolve(), editing._existing_path(rows[0], root))
                with patch.object(editing, "_files", return_value=rows):
                    states, report_text = editing._load_states(
                        None, {"dataset_id": "DS-000013", "forensic_report": (relative / "report.md").as_posix()}, root,
                    )
                self.assertEqual(1, len(states))
                self.assertIn("Sample visual", report_text)
                self.assertNotIn("/Users/", editing.render_json(states))
                self.assertNotIn("/private/tmp/", editing.render_json(states))
            finally:
                os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main()
