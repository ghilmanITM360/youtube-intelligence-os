import unittest

from forensic_metrics import frame_time_from_name, select_separated_peaks


class ForensicMetricsTests(unittest.TestCase):
    def test_frame_time_uses_integer_millisecond_suffix(self):
        self.assertEqual(frame_time_from_name("frame_0012375ms.jpg"), 12.375)

    def test_peak_selection_keeps_strongest_candidate_within_gap(self):
        times = [1.00, 1.08, 1.50, 2.00]
        scores = [0.40, 0.90, 0.50, 0.60]
        self.assertEqual(
            select_separated_peaks(times, scores, min_gap=0.20, limit=3),
            [1, 2, 3],
        )


if __name__ == "__main__":
    unittest.main()
