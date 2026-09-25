import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_legacy_dataset_manifests as v  # noqa: E402


class LegacyDatasetManifestTests(unittest.TestCase):
    def test_all_23_legacy_datasets_have_verifiable_evidence(self):
        for dataset_id in v.DEFAULT_DATASETS:
            rows = v.validate_dataset(dataset_id)
            self.assertTrue(rows, "{} has no parseable manifest rows".format(dataset_id))
            bad = [r for r in rows if r[1] not in ("OK", "NOT_COPIED_BY_POLICY")]
            self.assertEqual([], bad, "{} has unverifiable rows: {}".format(dataset_id, bad))

    def test_exactly_23_legacy_dataset_ids(self):
        self.assertEqual(23, len(v.DEFAULT_DATASETS))


if __name__ == "__main__":
    unittest.main()
