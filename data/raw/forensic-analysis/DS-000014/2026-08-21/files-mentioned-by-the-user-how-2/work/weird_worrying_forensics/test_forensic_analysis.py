import importlib
import unittest


class ForensicAnalysisContractTests(unittest.TestCase):
    def load_subject(self):
        try:
            return importlib.import_module("forensic_analysis")
        except ImportError as exc:
            self.fail(f"forensic_analysis module is missing: {exc}")

    def test_parse_frame_time_uses_millisecond_filename(self):
        """Catches parsing milliseconds as seconds or dropping the fractional part."""
        subject = self.load_subject()
        self.assertEqual(subject.parse_frame_time("frame_0005125ms.jpg"), 5.125)

    def test_parse_frame_time_rejects_non_frame_name(self):
        """Catches silently assigning a false timestamp to malformed evidence."""
        subject = self.load_subject()
        with self.assertRaises(ValueError):
            subject.parse_frame_time("overview.jpg")

    def test_select_peaks_keeps_strongest_within_minimum_distance(self):
        """Catches reporting several adjacent samples as separate cuts."""
        subject = self.load_subject()
        peaks = subject.select_peaks(
            [(0.25, 0.20), (1.00, 0.70), (1.25, 0.95), (3.00, 0.60)],
            threshold=0.50,
            minimum_distance=0.50,
        )
        self.assertEqual(peaks, [(1.25, 0.95), (3.00, 0.60)])

    def test_prompt_measurement_counts_unicode_characters_and_enforces_ceiling(self):
        """Catches byte-counting or accepting a prompt over the 500-character ceiling."""
        subject = self.load_subject()
        self.assertEqual(subject.prompt_measurement("Earth → Moon"), (12, True))
        self.assertEqual(subject.prompt_measurement("x" * 501), (501, False))

    def test_transition_marker_uses_default_font_supported_ascii(self):
        """Catches choosing a glyph that Pillow's bundled default font renders as a box."""
        subject = self.load_subject()
        self.assertTrue(hasattr(subject, "transition_marker"), "transition_marker is missing")
        self.assertEqual(subject.transition_marker(), "->")


if __name__ == "__main__":
    unittest.main()
