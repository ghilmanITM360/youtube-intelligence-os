import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from openpyxl import Workbook
from scripts.validate_supplied_channel_packages import parse_transcript_text


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_supplied_channel_packages.py"
HEADERS = [
    "#", "Video ID", "Title", "Video URL", "Published (UTC)", "Date", "Day",
    "Duration", "Sec", "Views", "Likes", "Comments", "Like Rate", "Comment Rate",
    "Engagement", "Views/Day", "Transcript Words", "Words/Min", "Desc Chars",
    "Desc Links", "Hashtags", "Caption Type", "Transcript File", "Thumbnail URL",
    "Members Only", "Paid", "Comments Off", "Age Restr.",
]


class SuppliedPackageValidatorTests(unittest.TestCase):
    def test_accepts_explicit_zero_word_placeholder(self):
        text = """Channel      : Example Channel
Title        : Example Video
Video ID     : abcdefghijk
URL          : https://www.youtube.com/watch?v=abcdefghijk
Published    : 2026-09-12T00:00:00.000Z
Duration     : 00:01:00
Views        : None
Likes        : 10
Comments     : 1
Hashtags     : (none)
Caption type : NONE - not available from scraper
Language     : -
Word count   : 0
==============================================================================
DESCRIPTION
==============================================================================
Description

==============================================================================
TRANSCRIPT
==============================================================================
(No transcript available. Confirmed on two scrapes.)
"""
        parsed = parse_transcript_text(text, "001_abcdefghijk_Example_Video.txt")
        self.assertEqual(parsed["word_count"], 0)
        self.assertTrue(parsed["placeholder"])

    def test_accepts_reconciled_workbook_and_transcript_zip(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workbook_path = root / "Example_Master_Data.xlsx"
            zip_path = root / "Example_Transcripts_1_Videos.zip"
            report_path = root / "report.json"
            markdown_path = root / "report.md"
            config_path = root / "config.json"

            workbook = Workbook()
            overview = workbook.active
            overview.title = "Channel Overview"
            overview.append(["Example Channel"])
            overview.append(["Source: Apify streamers/youtube-scraper. Scraped 12 Sep 2026."])
            overview.append([])
            overview.append(["Field", "Value"])
            overview.append(["Channel Name", "Example Channel"])
            overview.append(["Handle", "@example"])
            overview.append(["Channel ID", "UCexample"])
            overview.append(["Channel URL", "https://www.youtube.com/@example"])

            videos = workbook.create_sheet("All Videos")
            videos.append(["Example Channel"])
            videos.append(["Source package"])
            videos.append([])
            videos.append(HEADERS)
            row = [
                1, "abcdefghijk", "Example Video", "https://www.youtube.com/watch?v=abcdefghijk",
                "2026-09-12 00:00:00", 46277, "Saturday", "00:01:00", 60, "N/A", 10, 1,
                0.1, 0.01, 0.11, 100, 10, 10, 11,
                0, "#example", "ASR", "001_abcdefghijk_Example_Video.txt",
                "https://i.ytimg.com/vi/abcdefghijk/hqdefault.jpg", "No", "No", "No", "No",
            ]
            videos.append(row)
            videos.freeze_panes = "D5"
            videos.auto_filter.ref = "A4:AB5"

            descriptions = workbook.create_sheet("Descriptions")
            descriptions.append(["Example Channel"])
            descriptions.append(["Source package"])
            descriptions.append([])
            descriptions.append(["#", "Video ID", "Title", "Hashtags", "Link Count", "Description Links (URLs)", "Full Description"])
            descriptions.append([1, "abcdefghijk", "Example Video", "#example", 0, "", "Description"])
            workbook.create_sheet("Verification")
            workbook.create_sheet("Analysis")
            workbook.save(workbook_path)

            transcript = """Channel      : Example Channel
Title        : Example Video
Video ID     : abcdefghijk
URL          : https://www.youtube.com/watch?v=abcdefghijk
Published    : 2026-09-12 00:00:00
Duration     : 00:01:00
Views        : 100
Likes        : 10
Comments     : 1
Hashtags     : #example
Caption type : ASR
Language     : English
Word count   : 10
==============================================================================
DESCRIPTION
==============================================================================
Description

==============================================================================
TRANSCRIPT
==============================================================================
one two three four five six seven eight nine ten
"""
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("001_abcdefghijk_Example_Video.txt", transcript)
                archive.writestr("INDEX.txt", "001_abcdefghijk_Example_Video.txt\n")

            config_path.write_text(json.dumps({
                "dataset_id": "DS-TEST",
                "packages": [{
                    "channel": "Example Channel",
                    "expected_count": 1,
                    "workbook": str(workbook_path),
                    "zip": str(zip_path),
                }],
            }), encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(VALIDATOR), "--config", str(config_path), "--report-json", str(report_path), "--report-md", str(markdown_path)],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["total_videos"], 1)
            self.assertEqual(report["total_transcript_files"], 1)
            self.assertEqual(report["total_placeholder_transcripts"], 0)
            self.assertEqual(report["packages"][0]["video_ids"], ["abcdefghijk"])
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("abcdefghijk", markdown)
            self.assertIn("Views", markdown)


if __name__ == "__main__":
    unittest.main()
