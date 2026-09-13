import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from openpyxl import Workbook
from scripts.validate_supplied_channel_packages import (
    count_transcript_words,
    has_expected_video_filter,
    parse_transcript_text,
    youtube_id_from_cell,
)


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
    def test_transcript_word_count_matches_packager_unicode_tokenization(self):
        self.assertEqual(count_transcript_words("You're born—now re-enter foo_bar."), 5)

    def test_reads_video_id_from_hyperlink_formula_when_cached_value_is_diagnostic(self):
        cached = (
            "HYPERLINK is not implemented. "
            "linkLocation=https://www.youtube.com/watch?v=abcdefghijk, "
            "friendlyName=https://www.youtube.com/watch?v=abcdefghijk"
        )
        formula = (
            '=HYPERLINK("https://www.youtube.com/watch?v=abcdefghijk",'
            '"https://www.youtube.com/watch?v=abcdefghijk")'
        )

        self.assertEqual(youtube_id_from_cell(cached, formula), "abcdefghijk")

    def test_accepts_excel_table_filter_when_sheet_auto_filter_is_absent(self):
        from openpyxl.worksheet.table import Table

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "All Videos"
        sheet.append([])
        sheet.append([])
        sheet.append([])
        sheet.append(HEADERS)
        sheet.append([1, "abcdefghijk"] + [""] * 26)
        sheet.add_table(Table(displayName="VideosTable", ref="A4:AB5"))

        self.assertTrue(has_expected_video_filter(sheet, "A4:AB5"))

    def test_accepts_verified_members_only_zero_word_placeholder(self):
        text = """Channel      : Lucas Grant
Title        : Example Video
Video ID     : abcdefghijk
URL          : https://www.youtube.com/watch?v=abcdefghijk
Published    : 2026-09-12T00:00:00.000Z
Duration     : 00:01:00
Views        : None
Likes        : 10
Comments     : 1
Hashtags     : (none)
Caption type : NONE - members-only; captions unavailable
Language     : -
Word count   : 0
==============================================================================
DESCRIPTION
==============================================================================
Description

==============================================================================
TRANSCRIPT
==============================================================================
(Members-only video; unplayable without channel membership. YouTube displays 'Subtitles/closed captions unavailable'. Targeted Actor run dmUFY1GHENjMdqsB9 returned no subtitles.)
"""
        parsed = parse_transcript_text(text, "001_abcdefghijk_Example_Video.txt")
        self.assertEqual(parsed["word_count"], 0)
        self.assertTrue(parsed["placeholder"])

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
                "apify": {
                    "actor_run_id": "run-test",
                    "dataset_id": "dataset-test",
                    "raw_json": "data/raw/channel-data/DS-TEST/youtube_actor_raw.json",
                },
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
            self.assertIn("Actor run ID: `run-test`", markdown)
            self.assertIn("Apify dataset ID: `dataset-test`", markdown)
            self.assertIn("data/raw/channel-data/DS-TEST/youtube_actor_raw.json", markdown)


if __name__ == "__main__":
    unittest.main()
