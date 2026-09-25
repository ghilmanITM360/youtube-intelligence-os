import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from video_type_classification import classify_video_type, REGULAR, SHORT, STREAM, UNKNOWN  # noqa: E402


class VideoTypeClassificationTest(unittest.TestCase):
    def test_regular_raw_values(self):
        for raw in ("video", "regular video", "regular", "Video", "REGULAR VIDEO"):
            self.assertEqual(classify_video_type(raw), REGULAR, raw)

    def test_short_raw_values(self):
        for raw in ("short", "shorts", "Short", "SHORTS"):
            self.assertEqual(classify_video_type(raw), SHORT, raw)

    def test_stream_raw_values(self):
        for raw in ("live", "livestream", "stream", "streams", "Stream"):
            self.assertEqual(classify_video_type(raw), STREAM, raw)

    def test_unknown_raw_values(self):
        for raw in (None, "", "  ", "podcast_clip", "unrecognized"):
            self.assertEqual(classify_video_type(raw), UNKNOWN, repr(raw))


class MasterInventoryVideoTypeCoverageTest(unittest.TestCase):
    """Every acquired-channel video must classify to a known bucket.

    Regression guard for the 2026-09-25 defect where 'regular video' and
    'Short' silently fell into repo_other because the report compared raw
    values against only {'video', 'shorts'} instead of a normalized set.
    """

    def test_no_nonempty_raw_value_falls_through_to_unknown(self):
        """Every non-empty raw video_type currently in the registry must map
        to REGULAR/SHORT/STREAM — only a truly missing value may be UNKNOWN.
        """
        import sqlite3

        db_path = REPO_ROOT / "data/catalog/youtube_channel_registry.db"
        if not db_path.exists():
            self.skipTest("registry database not present in this checkout")
        conn = sqlite3.connect(str(db_path))
        try:
            raw_values = {row[0] for row in conn.execute(
                "SELECT DISTINCT video_type FROM videos WHERE video_type IS NOT NULL AND video_type != ''"
            )}
        finally:
            conn.close()
        for raw in raw_values:
            self.assertNotEqual(
                classify_video_type(raw), UNKNOWN,
                f"raw video_type {raw!r} classified UNKNOWN — "
                "add it to video_type_classification.py if it is a real category",
            )


if __name__ == "__main__":
    unittest.main()
