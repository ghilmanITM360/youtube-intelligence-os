"""Regression cases from the Actor's inline-caption output contract."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import apify_youtube_ingest as ingest


class InlineSrtTests(unittest.TestCase):
    def test_numeric_content_blank_and_repeated_display_cues(self):
        srt = (
            "1\n00:00:0,080 --> 00:00:4,319\nGDP was\n\n"
            "2\n00:00:1,670 --> 00:00:4,319\n \n\n"
            "3\n00:00:4,319 --> 00:00:6,400\n1955\n\n"
            "4\n00:00:4,319 --> 00:00:6,400\n1955\n\n"
        )
        result = ingest.normalize_transcript([
            {"language": "en", "type": "auto_generated", "srt": srt, "srtUrl": None}
        ])
        self.assertEqual(result["text"], "GDP was 1955")
        self.assertEqual(result["availability_status"], "AVAILABLE")
        self.assertEqual(result["format"], "srt")
        self.assertEqual(result["word_count"], 3)

    def test_empty_caption_is_unavailable(self):
        result = ingest.normalize_transcript([{"language": "en", "srt": ""}])
        self.assertEqual(result["availability_status"], "UNAVAILABLE")
        self.assertIsNone(result["word_count"])

    def test_plaintext_precedence_is_preserved(self):
        result = ingest.normalize_transcript([
            {"language": "en", "plaintext": "Original supplied text", "srt": "malformed"}
        ])
        self.assertEqual(result["text"], "Original supplied text")
        self.assertEqual(result["format"], "plaintext")

    def test_live_actor_input_uses_existing_subtitles_only(self):
        value = ingest.build_actor_input("https://www.youtube.com/@casual_economics", 11)
        self.assertEqual(value["transcriptionAndSubtitle"], "ALWAYS_SUBTITLES")
        self.assertFalse(value["aiVideoDescription"])
        self.assertFalse(value["aiVideoSummary"])


if __name__ == "__main__":
    unittest.main()
