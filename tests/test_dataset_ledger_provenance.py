import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_dataset_ledgers as v  # noqa: E402

DATASETS = [
    "DS-000020", "DS-000021", "DS-000022", "DS-000023", "DS-000024",
    "DS-000025", "DS-000027", "DS-000028", "DS-000030",
]


class LedgerPathSafetyTests(unittest.TestCase):
    def test_no_ledger_path_escapes_repository(self):
        for dataset_id in DATASETS:
            for row in v.load_ledger_rows(dataset_id):
                self.assertTrue(
                    v.resolves_within_repo(row["repository_relative_path"]),
                    "{} {} escapes the repository".format(dataset_id, row["artifact_id"]),
                )

    def test_absolute_and_dotdot_paths_are_rejected(self):
        self.assertFalse(v.resolves_within_repo("/etc/passwd"))
        self.assertFalse(v.resolves_within_repo("../../etc/passwd"))
        self.assertFalse(v.resolves_within_repo("data/manifests/../../../etc/passwd"))

    def test_duplicate_path_segments_are_rejected(self):
        self.assertTrue(v.has_duplicate_segment(
            "data/raw/channel-data/DS-000023/apify/RUN123/apify/RUN123/file.json"
        ))
        self.assertTrue(v.has_duplicate_segment("a/a/b"))
        self.assertFalse(v.has_duplicate_segment("data/raw/channel-data/DS-000023/apify/RUN123/file.json"))

    def test_ds_000023_f001_path_corrected_and_clean(self):
        rows = v.load_ledger_rows("DS-000023")
        row = next(r for r in rows if r["artifact_id"] == "DS-000023-F001")
        self.assertEqual(
            "data/raw/channel-data/DS-000023/apify/YlTuIQD7ejSlxe2Ox/youtube_actor_raw.json",
            row["repository_relative_path"],
        )
        self.assertFalse(v.has_duplicate_segment(row["repository_relative_path"]))
        self.assertEqual([], v.validate_row("DS-000023", row))


class LedgerChecksumTests(unittest.TestCase):
    def test_all_csv_ledger_datasets_are_clean(self):
        for dataset_id in DATASETS:
            problems = v.validate_dataset(dataset_id)
            self.assertEqual({}, problems, "{} has unresolved ledger issues".format(dataset_id))

    def test_default_datasets_cover_every_known_csv_ledger(self):
        self.assertEqual(set(DATASETS), set(v.DEFAULT_DATASETS))

    def test_historical_pinned_rows_are_checked_against_their_recorded_commit(self):
        # Every pinned row's ledger hash must reconcile against the git blob
        # at its recorded commit, not against current working-tree bytes —
        # these files (packaging scripts, tests, docs) have legitimately
        # changed since the dataset was packaged.
        self.assertGreater(len(v.KNOWN_HISTORICAL_SNAPSHOTS), 0)
        for (dataset_id, artifact_id), commit in v.KNOWN_HISTORICAL_SNAPSHOTS.items():
            rows = v.load_ledger_rows(dataset_id)
            row = next(r for r in rows if r["artifact_id"] == artifact_id)
            blob_sha = v.sha256_git_blob(commit, row["repository_relative_path"])
            self.assertEqual(
                row["sha256"], blob_sha,
                "{} {} does not reconcile against pinned commit {}".format(dataset_id, artifact_id, commit),
            )

    def test_immutable_raw_rows_not_pinned_match_current_bytes(self):
        checked = 0
        for dataset_id in DATASETS:
            for row in v.load_ledger_rows(dataset_id):
                if row["raw_or_derived_classification"] != "RAW":
                    continue
                if (dataset_id, row["artifact_id"]) in v.KNOWN_HISTORICAL_SNAPSHOTS:
                    continue
                self.assertEqual([], v.validate_row(dataset_id, row))
                checked += 1
        self.assertGreater(checked, 0)


class LedgerRowValidationUnitTests(unittest.TestCase):
    def test_validate_row_flags_size_and_sha_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "data" / "raw" / "sample.json"
            target.parent.mkdir(parents=True)
            target.write_text("hello", encoding="utf-8")
            row = {
                "artifact_id": "X-1",
                "repository_relative_path": "data/raw/sample.json",
                "size_bytes": "999",
                "sha256": "0" * 64,
                "raw_or_derived_classification": "RAW",
            }
            issues = v.validate_row("DS-TEST", row, root=root)
            self.assertIn("SIZE_MISMATCH", issues)
            self.assertIn("SHA_MISMATCH", issues)

    def test_validate_row_flags_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = {
                "artifact_id": "X-2",
                "repository_relative_path": "data/raw/missing.json",
                "size_bytes": "1",
                "sha256": "0" * 64,
                "raw_or_derived_classification": "RAW",
            }
            self.assertEqual(["FILE_MISSING"], v.validate_row("DS-TEST", row, root=root))

    def test_validate_row_flags_path_escape_before_any_disk_access(self):
        row = {
            "artifact_id": "X-3",
            "repository_relative_path": "../outside.json",
            "size_bytes": "1",
            "sha256": "0" * 64,
            "raw_or_derived_classification": "RAW",
        }
        self.assertEqual(["PATH_ESCAPES_REPO"], v.validate_row("DS-TEST", row))


if __name__ == "__main__":
    unittest.main()
