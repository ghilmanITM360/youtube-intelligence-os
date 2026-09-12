import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook

from scripts.apply_youtube_transcript_recovery import (
    build_recovery_results,
    update_placeholder_archive,
    update_workbook_annotations,
)


PLACEHOLDER = """Channel      : Lucas Grant
Title        : Example
Video ID     : abcdefghijk
URL          : https://www.youtube.com/watch?v=abcdefghijk
Published    : 2026-08-24T12:15:21.000Z
Duration     : 00:22:55
Views        : None
Likes        : 89
Comments     : 0
Hashtags     : (none)
Caption type : NONE - scrape gap
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


class TranscriptRecoveryTests(unittest.TestCase):
    def test_classifies_member_only_video_when_actor_returns_no_subtitles(self):
        raw = [{
            "id": "abcdefghijk",
            "title": "Example",
            "url": "https://www.youtube.com/watch?v=abcdefghijk",
            "viewCount": None,
            "subtitles": None,
            "transcriptionUrl": None,
        }]
        live = [{
            "video_id": "abcdefghijk",
            "resolved_url": "https://www.youtube.com/watch?v=abcdefghijk",
            "availability": "MEMBERS_ONLY",
            "playable_without_membership": False,
            "captions_visible": False,
            "youtube_caption_control": "Subtitles/closed captions unavailable",
        }]

        results = build_recovery_results(raw, live, "dmUFY1GHENjMdqsB9")

        self.assertEqual(results[0]["recovery_result"], "MEMBERS_ONLY_CAPTIONS_UNAVAILABLE")
        self.assertEqual(results[0]["transcript_word_count"], 0)
        self.assertIn("members-only", results[0]["verified_reason"].lower())
        self.assertIn("No subtitles found", results[0]["actor_evidence"])

    def test_updates_placeholder_archive_and_index_with_verified_reason(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.zip"
            output = root / "output.zip"
            filename = "001_abcdefghijk_Example.txt"
            index = (
                "TRANSCRIPT PACK - Lucas Grant\n"
                "With transcript: 0\n"
                "Without transcript (view count hidden by creator, confirmed on 2 scrapes): 1\n\n"
                f"001      0 words  {filename}   [NO TRANSCRIPT - view count hidden by creator]\n"
            )
            with zipfile.ZipFile(source, "w", zipfile.ZIP_DEFLATED) as archive:
                archive.writestr(filename, PLACEHOLDER)
                archive.writestr("INDEX.txt", index)

            update_placeholder_archive(
                source,
                output,
                {"abcdefghijk": "Members-only video; captions unavailable on YouTube and Actor run dmUFY1GHENjMdqsB9."},
                "dmUFY1GHENjMdqsB9",
            )

            with zipfile.ZipFile(output) as archive:
                transcript = archive.read(filename).decode("utf-8")
                updated_index = archive.read("INDEX.txt").decode("utf-8")
                self.assertIsNone(archive.testzip())
            self.assertIn("Caption type : NONE - members-only; captions unavailable", transcript)
            self.assertIn("Members-only video; captions unavailable", transcript)
            self.assertNotIn("view count hidden by creator", transcript)
            self.assertIn("Without transcript (verified members-only; captions unavailable): 1", updated_index)
            self.assertIn("[NO TRANSCRIPT - members-only; captions unavailable]", updated_index)

    def test_updates_workbook_annotations_without_removing_formulas(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.xlsx"
            output = root / "output.xlsx"
            workbook = Workbook()
            overview = workbook.active
            overview.title = "Channel Overview"
            overview["A1"] = "10 videos returned no view count on two separate scrapes"
            videos = workbook.create_sheet("All Videos")
            videos["B4"] = "Video ID"
            videos["Q4"] = "Transcript Words"
            videos["R4"] = "Words/Min"
            videos["V4"] = "Caption Type"
            videos["Y4"] = "Members Only"
            videos["B5"] = "abcdefghijk"
            videos["Q5"] = 0
            videos["R5"] = "=IFERROR(Q5/10,0)"
            videos["V5"] = "NONE - scrape gap"
            videos["Y5"] = "No"
            workbook.create_sheet("Descriptions")
            verification = workbook.create_sheet("Verification")
            verification["A1"] = "Videos with hidden view count / no transcript available"
            verification["A2"] = "Videos with a scrape gap (no transcript / no view count)"
            workbook.create_sheet("Analysis")
            workbook.save(source)

            update_workbook_annotations(
                source,
                output,
                {"abcdefghijk"},
                "dmUFY1GHENjMdqsB9",
                "OSwKiHG3ijoDZZ1t9",
            )

            checked = load_workbook(output, data_only=False)
            try:
                self.assertEqual(checked["All Videos"]["V5"].value, "NONE - members-only; captions unavailable")
                self.assertEqual(checked["All Videos"]["Y5"].value, "Yes")
                self.assertEqual(checked["All Videos"]["R5"].value, "=IFERROR(Q5/10,0)")
                self.assertIn("members-only", checked["Channel Overview"]["A1"].value.lower())
                self.assertIn("members-only", checked["Verification"]["A1"].value.lower())
                self.assertEqual(
                    checked["Verification"]["A2"].value,
                    "Videos verified members-only with captions unavailable",
                )
            finally:
                checked.close()


if __name__ == "__main__":
    unittest.main()
