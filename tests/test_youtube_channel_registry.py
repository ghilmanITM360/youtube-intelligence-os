import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_AUTHORITY = (
    ROOT
    / "data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json"
)


class RawChannelAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(RAW_AUTHORITY.read_text(encoding="utf-8"))
        cls.rows = cls.data["submissions"]

    def test_required_control_totals_and_order(self):
        self.assertEqual(67, len(self.rows))
        self.assertEqual(47, sum(row["batch"] == "A" for row in self.rows))
        self.assertEqual(20, sum(row["batch"] == "B" for row in self.rows))
        self.assertEqual(list(range(1, 68)), [row["global_row"] for row in self.rows])
        self.assertEqual(list(range(1, 48)), [row["batch_row"] for row in self.rows[:47]])
        self.assertEqual(list(range(1, 21)), [row["batch_row"] for row in self.rows[47:]])

    def test_payload_hash_and_normalized_urls(self):
        payload = "\n".join(row["original_url"] for row in self.rows) + "\n"
        self.assertEqual(
            "b8f72bfee5d3c8edc206dd4a28d4f31470b9f24a1305044548a1dc78ebd90296",
            hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        )
        self.assertEqual(63, len({row["normalized_url"] for row in self.rows}))

    def test_exact_duplicates_reference_prior_identical_rows(self):
        duplicates = [row for row in self.rows if row["is_exact_duplicate"]]
        self.assertEqual([18, 23, 47, 64], [row["global_row"] for row in duplicates])
        self.assertEqual([13, 22, 45, 53], [row["duplicate_of_global_row"] for row in duplicates])
        by_number = {row["global_row"]: row for row in self.rows}
        for row in duplicates:
            target = by_number[row["duplicate_of_global_row"]]
            self.assertLess(target["global_row"], row["global_row"])
            self.assertEqual(target["original_url"], row["original_url"])

    def test_required_submission_fields(self):
        required = {
            "global_row",
            "batch",
            "batch_row",
            "original_url",
            "normalized_url",
            "is_exact_duplicate",
            "duplicate_of_global_row",
            "canonical_channel_id",
            "identity_status",
            "evidence_source",
            "verified_at",
        }
        for row in self.rows:
            self.assertEqual(required, set(row))


class RegistryModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from scripts.build_youtube_channel_registry import build_model

        cls.model = build_model(ROOT)

    def test_canonical_id_deduplication_and_alias_preservation(self):
        channels = self.model["channels"]
        target_channels = [row for row in channels if row["target_group"] != "OUTSIDE_TARGET"]
        self.assertEqual(63, len(target_channels))
        self.assertEqual(len(channels), len({row["canonical_channel_id"] for row in channels}))
        self.assertEqual(67, len(self.model["submissions"]))
        self.assertTrue(all(row["canonical_channel_id"] for row in self.model["submissions"]))
        self.assertEqual(
            [row["original_url"] for row in RawChannelAuthorityTests.rows],
            [row["original_url"] for row in self.model["submissions"]],
        )

    def test_completed_status_requires_package_or_catalog_evidence(self):
        for channel in self.model["channels"]:
            if channel["status"] in {"COMPLETE", "COMPLETE_WITH_LIMITATIONS"}:
                self.assertGreater(channel["video_count"], 0)
                self.assertTrue(channel["dataset_ids"])
            if channel["status"] == "IDENTITY_VERIFIED_DATA_NOT_EXTRACTED":
                self.assertEqual(0, channel["video_count"])
                self.assertEqual("", channel["completed_tick"])

    def test_tp_dossier_is_outside_targets(self):
        row = next(row for row in self.model["channels"] if row["current_handle"] == "@TPDossierYT")
        self.assertEqual("OUTSIDE_TARGET", row["target_group"])
        self.assertFalse(any(s["canonical_channel_id"] == row["canonical_channel_id"] for s in self.model["submissions"]))

    def test_screenshot_only_subjects_are_not_canonical_channels(self):
        self.assertEqual(7, len(self.model["subjects"]))
        self.assertTrue(all(row["canonical_channel_id"] is None for row in self.model["subjects"]))

    def test_package_control_totals(self):
        package = self.model["controls"]["package_layer"]
        self.assertEqual(35, package["channels"])
        self.assertEqual(1601, package["unique_videos"])
        self.assertEqual(1591, package["real_transcripts"])
        self.assertEqual(10, package["placeholders"])
        self.assertEqual(14, package["missing_descriptions"])

    def test_source_groups_and_independent_data_layer_statuses(self):
        channels = self.model["channels"]
        self.assertEqual(
            {"STANDARD_PACKAGE": 35, "HISTORICAL_CATALOG": 5, "IDENTITY_ONLY": 29},
            {
                group: sum(row["source_group"] == group for row in channels)
                for group in ("STANDARD_PACKAGE", "HISTORICAL_CATALOG", "IDENTITY_ONLY")
            },
        )
        required = {
            "identity_status",
            "extraction_status",
            "package_status",
            "video_metadata_status",
            "description_status",
            "transcript_status",
            "thumbnail_metadata_status",
            "visual_asset_status",
            "forensic_video_status",
            "intelligence_status",
            "first_party_analytics_status",
        }
        for channel in channels:
            self.assertTrue(required.issubset(channel))
            self.assertEqual("VERIFIED", channel["identity_status"])
            self.assertEqual("SCHEMA_READY_NO_DATA", channel["first_party_analytics_status"])
            if channel["source_group"] == "IDENTITY_ONLY":
                self.assertEqual("NOT_EXTRACTED", channel["extraction_status"])
                self.assertEqual("NO_PACKAGE", channel["package_status"])
                self.assertEqual("NONE", channel["transcript_status"])
            elif channel["source_group"] == "STANDARD_PACKAGE":
                self.assertEqual("STANDARD_PACKAGE", channel["package_status"])
                self.assertTrue(channel["workbook_path"].endswith(".xlsx"))
                self.assertTrue(channel["transcript_zip_path"].endswith(".zip"))
            else:
                self.assertEqual("HISTORICAL_FORMAT", channel["package_status"])

    def test_visual_evidence_is_not_inferred_from_transcripts(self):
        channels = {row["canonical_channel_id"]: row for row in self.model["channels"]}
        xkcd = channels["UC6IxnFzHofFJ5X2PycSMsww"]
        self.assertEqual("FORENSIC_VIDEO_EVIDENCE", xkcd["visual_asset_status"])
        self.assertEqual(107, xkcd["visual_coverage"]["keyframe_count"])
        self.assertEqual(3, xkcd["visual_coverage"]["registered_source_video_count"])
        self.assertEqual(107, xkcd["visual_coverage"]["timestamped_visual_observation_count"])
        self.assertEqual(
            {"UCXZi5JVeuTluazF-fYqQgNA", "UC6IxnFzHofFJ5X2PycSMsww", "UCQcBYZxFW7YwNMU8-DsT3Uw"},
            {
                identifier
                for identifier, row in channels.items()
                if row["visual_asset_status"] in {"THUMBNAIL_EVIDENCE", "FORENSIC_VIDEO_EVIDENCE"}
            },
        )
        self.assertEqual(
            {"UCkqzov98m_7niJOXwbRQgBA", "UC6AwWrRKNrwt83CMJqeTUzw"},
            {
                identifier
                for identifier, row in channels.items()
                if row["thumbnail_metadata_status"] == "NONE" and row["source_group"] == "HISTORICAL_CATALOG"
            },
        )
        self.assertEqual(7, len(self.model["subjects"]))
        self.assertTrue(all(row["visual_evidence_level"] == "SCREENSHOT_ONLY_UNMAPPED" for row in self.model["subjects"]))

    def test_eight_capabilities_preserve_input_output_distinction(self):
        coverage = self.model["intelligence_coverage"]
        self.assertEqual(8, len(self.model["intelligence_capabilities"]))
        self.assertEqual(69 * 8, len(coverage))
        self.assertTrue(
            all(
                {
                    "capability_id",
                    "canonical_channel_id",
                    "status",
                    "input_data_available",
                    "generated_artifact_available",
                    "evidence_path",
                    "limitation_reason",
                    "last_verified_at",
                }
                == set(row)
                for row in coverage
            )
        )
        package_ready = [
            row
            for row in coverage
            if row["capability_id"] == "TOPIC_OPPORTUNITY"
            and row["status"] == "DATA_READY"
        ]
        self.assertEqual(35, len(package_ready))
        self.assertTrue(all(row["input_data_available"] and not row["generated_artifact_available"] for row in package_ready))
        editing = [row for row in coverage if row["capability_id"] == "EDITING_VISUAL" and row["generated_artifact_available"]]
        self.assertEqual(["UC6IxnFzHofFJ5X2PycSMsww"], [row["canonical_channel_id"] for row in editing])
        first_party = [row for row in coverage if row["capability_id"] == "FIRST_PARTY_ANALYTICS"]
        self.assertEqual(69, len(first_party))
        self.assertTrue(all(row["status"] == "DATA_READY" and not row["input_data_available"] for row in first_party))


class RegistryDatabaseTests(unittest.TestCase):
    def test_database_is_valid_complete_and_idempotent(self):
        from scripts.build_youtube_channel_registry import build_database, build_model

        model = build_model(ROOT)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.db"
            first = build_database(ROOT, path, model)
            second = build_database(ROOT, path, model)
            self.assertEqual(first, second)
            connection = sqlite3.connect(path)
            try:
                self.assertEqual("ok", connection.execute("PRAGMA integrity_check").fetchone()[0])
                self.assertEqual([], connection.execute("PRAGMA foreign_key_check").fetchall())
                views = {
                    row[0]
                    for row in connection.execute(
                        "SELECT name FROM sqlite_master WHERE type = 'view'"
                    )
                }
                self.assertTrue(
                    {
                        "v_channel_status",
                        "v_completed_channels",
                        "v_pending_channels",
                        "v_channel_data_gaps",
                        "v_original_target_progress",
                        "v_added_target_progress",
                        "v_dataset_summary",
                        "v_video_transcript_status",
                        "v_channel_artifacts",
                        "v_intelligence_coverage",
                    }.issubset(views)
                )
                self.assertEqual(1904, connection.execute("SELECT count(*) FROM videos").fetchone()[0])
                self.assertEqual(1893, connection.execute("SELECT count(*) FROM transcripts WHERE is_placeholder = 0").fetchone()[0])
                self.assertEqual(11, connection.execute("SELECT count(*) FROM transcripts WHERE is_placeholder = 1").fetchone()[0])
                self.assertEqual(14, connection.execute("SELECT count(*) FROM videos WHERE description IS NULL").fetchone()[0])
                self.assertEqual(35, connection.execute("SELECT count(*) FROM channels WHERE source_group='STANDARD_PACKAGE'").fetchone()[0])
                self.assertEqual(5, connection.execute("SELECT count(*) FROM channels WHERE source_group='HISTORICAL_CATALOG'").fetchone()[0])
                self.assertEqual(29, connection.execute("SELECT count(*) FROM channels WHERE source_group='IDENTITY_ONLY'").fetchone()[0])
                self.assertEqual(69 * 11, connection.execute("SELECT count(*) FROM channel_data_layers").fetchone()[0])
                self.assertEqual(69, connection.execute("SELECT count(*) FROM visual_coverage").fetchone()[0])
                self.assertEqual(69 * 8, connection.execute("SELECT count(*) FROM intelligence_coverage").fetchone()[0])
                self.assertEqual(1, connection.execute("SELECT count(*) FROM visual_coverage WHERE visual_evidence_level='FORENSIC_VIDEO_EVIDENCE'").fetchone()[0])
                self.assertEqual(
                    0,
                    connection.execute(
                        "SELECT count(*) FROM transcripts WHERE transcript_text IS NULL AND unavailable_reason IS NULL"
                    ).fetchone()[0],
                )
            finally:
                connection.close()


class RegistryValidatorTests(unittest.TestCase):
    def test_validator_proves_required_controls(self):
        from scripts.build_youtube_channel_registry import build_database, build_model
        from scripts.validate_youtube_channel_registry import validate_database

        model = build_model(ROOT)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.db"
            build_database(ROOT, path, model)
            result = validate_database(ROOT, path)
        self.assertEqual("PASS", result["status"])
        self.assertEqual(69, result["controls"]["canonical_channels"])
        self.assertEqual(63, result["controls"]["target_channels"])
        self.assertEqual(40, result["controls"]["channels_with_video_data"])
        self.assertEqual(29, result["controls"]["identity_only_channels"])
        self.assertEqual(35, result["controls"]["standard_packages"])
        self.assertEqual(5, result["controls"]["historical_channels"])
        self.assertEqual(552, result["controls"]["intelligence_coverage_rows"])


if __name__ == "__main__":
    unittest.main()
