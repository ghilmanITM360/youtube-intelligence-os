import csv
import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "expansion-monkey-explains-1999-2026-10-21"


def rows(name):
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


class MonkeyExpansionContract(unittest.TestCase):
    def test_public_source_and_format_split(self):
        source = rows("FULL_CHANNEL_SOURCE.csv")
        self.assertEqual(len(source), 76)
        self.assertEqual(len({row["video_id"] for row in source}), 76)
        self.assertEqual(sum(row["video_type"] == "REGULAR" for row in source), 61)
        self.assertEqual(sum(row["video_type"] == "SHORT" for row in source), 15)
        self.assertTrue(all(row["availability_status"] == "PUBLIC_ACCESSIBLE_AT_RETRIEVAL" for row in source))

    def test_every_public_video_classified_and_reconciled(self):
        source = rows("FULL_CHANNEL_SOURCE.csv")
        crosswalk = rows("FINANCE_INCLUSION_CROSSWALK.csv")
        master = rows("FINANCE_EXPANSION_MASTER.csv")
        self.assertEqual({row["video_id"] for row in source}, {row["video_id"] for row in crosswalk})
        self.assertEqual({row["video_id"] for row in master}, {row["video_id"] for row in crosswalk if row["expansion_disposition"] == "INCLUDE_UNIQUE_EXPANSION"})
        self.assertTrue(all(row["analysis_completion"] == "METADATA_ONLY_NOT_DEEP_AUDITED" for row in master))

    def test_population_contract(self):
        validation = json.loads((ROOT / "EXPANSION_VALIDATION.json").read_text())
        self.assertEqual(validation["status"], "PASS")
        self.assertEqual(validation["frozen_original_unique_ids"], 966)
        self.assertEqual(validation["existing_expansion_unique_ids"], 197)
        self.assertEqual(validation["prior_population_duplicates"], 0)
        self.assertEqual(validation["combined_unique_research_population"], 966 + 197 + validation["unique_finance_additions"])
        self.assertTrue(all(validation["checks"].values()))

    def test_checksums(self):
        checksums = json.loads((ROOT / "FILE_CHECKSUMS_SHA256.json").read_text())
        for name, expected in checksums.items():
            self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), expected)


if __name__ == "__main__":
    unittest.main()
