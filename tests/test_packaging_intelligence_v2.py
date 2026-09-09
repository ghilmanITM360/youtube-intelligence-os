import json
import unittest
from pathlib import Path


class PackagingIntelligenceV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        cls.payload = json.loads((
            root / "data/intelligence/channels/CH-000004/packaging-intelligence-2026-09-09-v2.json"
        ).read_text(encoding="utf-8"))
        cls.pilot = json.loads((
            root / "data/intelligence/channels/CH-000004/packaging-intelligence-pilot-2026-09-09.json"
        ).read_text(encoding="utf-8"))

    def test_all_visual_evidence_is_accounted_for_and_temporally_bounded(self):
        payload = self.payload
        self.assertEqual(payload["thumbnail_evidence"]["registered_urls"], 83)
        self.assertEqual(payload["thumbnail_evidence"]["successful_images"], 83)
        self.assertEqual(len(payload["visual_features"]), 83)
        self.assertTrue(all(row["interpretation_state"] == "AI_INTERPRETATION" for row in payload["visual_features"]))
        self.assertEqual(payload["temporal_alignment"]["verified_historical_pairs"], 0)
        self.assertEqual(payload["temporal_alignment"]["temporally_uncertain_pairs"], 83)

    def test_formats_archetypes_and_packages_stay_separate_and_traceable(self):
        payload = self.payload
        self.assertEqual(payload["thumbnail_evidence"]["format_counts"], {"LONG_FORM": 43, "SHORTS": 40})
        self.assertEqual(len(payload["provisional_archetype_revalidation"]), 4)
        package_rows = payload["package_revalidation"]
        original_package_ids = {
            package["package_id"]
            for opportunity in self.pilot["opportunity_packages"]
            for package in opportunity["recommended_test_set"]
        }
        self.assertEqual(len(package_rows), 15)
        self.assertEqual({row["package_id"] for row in package_rows}, original_package_ids)
        self.assertTrue(all(row["generation_state"] == "HYPOTHESIS_FOR_TESTING" for row in package_rows))
        canonical = {row["video_id"] for row in payload["visual_features"]}
        self.assertTrue(all(set(row["supporting_video_ids"]) <= canonical for row in package_rows))

    def test_no_private_metric_or_prediction_fields(self):
        forbidden = {
            "algorithm_score", "algorithm_package_score", "ctr", "ctr_score",
            "guaranteed_winner", "predicted_ctr", "predicted_winner", "success_probability",
        }

        def keys(value):
            found = set()
            if isinstance(value, dict):
                for key, child in value.items():
                    found.add(key.lower())
                    found.update(keys(child))
            elif isinstance(value, list):
                for child in value:
                    found.update(keys(child))
            return found

        self.assertTrue(forbidden.isdisjoint(keys(self.payload)))


if __name__ == "__main__":
    unittest.main()
