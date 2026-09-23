import hashlib
import json
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_AUTHORITY = (
    ROOT
    / "data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json"
)


class GeneratedAtTests(unittest.TestCase):
    def test_generated_at_is_actual_build_time_not_verified_at(self):
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        import build_youtube_channel_registry as builder

        stamp = builder._generated_at()
        self.assertNotEqual(stamp, builder.VERIFIED_AT)
        self.assertRegex(stamp, r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


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


class DatasetInventoryTests(unittest.TestCase):
    def test_registered_dataset_inventory_includes_ds_000027_without_requiring_ds_000026(self):
        from scripts.build_youtube_channel_registry import _dataset_records

        dataset_ids = [row["dataset_id"] for row in _dataset_records(ROOT)]
        self.assertIn("DS-000027", dataset_ids)
        self.assertNotIn("DS-000026", dataset_ids)


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

    def test_inventory_acquisition_promotes_resolved_screenshot_subject(self):
        from scripts.build_youtube_channel_registry import inventory_only_channels

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog = root / "data/catalog"
            catalog.mkdir(parents=True)
            connection = sqlite3.connect(catalog / "youtube_inventory.db")
            connection.executescript(
                """
                CREATE TABLE channels (
                    channel_id TEXT PRIMARY KEY, youtube_channel_id TEXT, handle TEXT,
                    display_name TEXT NOT NULL, channel_url TEXT, created_from_dataset_id TEXT NOT NULL
                );
                CREATE TABLE channel_dataset_links (
                    channel_id TEXT, dataset_id TEXT, relationship_type TEXT
                );
                CREATE TABLE videos (
                    video_id TEXT PRIMARY KEY, youtube_video_id TEXT, channel_id TEXT,
                    created_from_dataset_id TEXT
                );
                CREATE TABLE video_snapshots (
                    video_id TEXT, description TEXT, thumbnail_url TEXT, video_type TEXT
                );
                CREATE TABLE transcripts (
                    video_id TEXT, dataset_id TEXT, availability_status TEXT
                );
                """
            )
            connection.execute(
                "INSERT INTO channels VALUES (?,?,?,?,?,?)",
                ("CH-000006", "UC0000000000000000000000", "@acquired", "Acquired Channel",
                 "https://www.youtube.com/channel/UC0000000000000000000000", "DS-000028"),
            )
            connection.execute("INSERT INTO channel_dataset_links VALUES (?,?,?)", ("CH-000006", "DS-000028", "STRUCTURED_OBSERVATION"))
            for index in range(2):
                video_id = f"video-{index}"
                connection.execute("INSERT INTO videos VALUES (?,?,?,?)", (video_id, video_id, "CH-000006", "DS-000028"))
                connection.execute("INSERT INTO video_snapshots VALUES (?,?,?,?)", (video_id, "description", "thumbnail", "video"))
                connection.execute("INSERT INTO transcripts VALUES (?,?,?)", (video_id, "DS-000028", "AVAILABLE"))
            connection.commit()
            connection.close()

            rows = inventory_only_channels(root, set())

        self.assertEqual(1, len(rows))
        self.assertEqual("UC0000000000000000000000", rows[0]["canonical_channel_id"])
        self.assertEqual(["DS-000028"], rows[0]["dataset_ids"])
        self.assertEqual(2, rows[0]["video_count"])
        self.assertEqual(2, rows[0]["real_transcripts"])

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
        self.assertEqual(5, len(self.model["subjects"]))
        self.assertTrue(all(row["canonical_channel_id"] is None for row in self.model["subjects"]))

    def test_package_control_totals(self):
        package = self.model["controls"]["package_layer"]
        self.assertEqual(37, package["channels"])
        self.assertEqual(1702, package["unique_videos"])
        self.assertEqual(1692, package["real_transcripts"])
        self.assertEqual(10, package["placeholders"])
        self.assertEqual(14, package["missing_descriptions"])

    def test_source_groups_and_independent_data_layer_statuses(self):
        channels = self.model["channels"]
        self.assertEqual(
            {"STANDARD_PACKAGE": 37, "HISTORICAL_CATALOG": 6, "IDENTITY_ONLY": 29},
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
            {"UCkqzov98m_7niJOXwbRQgBA", "UC6AwWrRKNrwt83CMJqeTUzw", "UCFuGMi0idGeyXl6wYK9hg7Q"},
            {
                identifier
                for identifier, row in channels.items()
                if row["thumbnail_metadata_status"] == "NONE" and row["source_group"] == "HISTORICAL_CATALOG"
            },
        )
        self.assertEqual(5, len(self.model["subjects"]))
        self.assertTrue(all(row["visual_evidence_level"] == "SCREENSHOT_ONLY_UNMAPPED" for row in self.model["subjects"]))

    def test_eight_capabilities_preserve_input_output_distinction(self):
        coverage = self.model["intelligence_coverage"]
        self.assertEqual(8, len(self.model["intelligence_capabilities"]))
        self.assertEqual(72 * 8, len(coverage))
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
        self.assertEqual(37, len(package_ready))
        self.assertTrue(all(row["input_data_available"] and not row["generated_artifact_available"] for row in package_ready))
        editing = [row for row in coverage if row["capability_id"] == "EDITING_VISUAL" and row["generated_artifact_available"]]
        self.assertEqual(["UC6IxnFzHofFJ5X2PycSMsww"], [row["canonical_channel_id"] for row in editing])
        first_party = [row for row in coverage if row["capability_id"] == "FIRST_PARTY_ANALYTICS"]
        self.assertEqual(72, len(first_party))
        self.assertTrue(all(row["status"] == "DATA_READY" and not row["input_data_available"] for row in first_party))


class HistoricalRecordsNoSubtitleTests(unittest.TestCase):
    def _build_inventory_db(self, directory):
        catalog = Path(directory) / "data/catalog"
        catalog.mkdir(parents=True)
        connection = sqlite3.connect(catalog / "youtube_inventory.db")
        connection.executescript(
            """
            CREATE TABLE channels (channel_id TEXT PRIMARY KEY, youtube_channel_id TEXT);
            CREATE TABLE videos (
                video_id TEXT PRIMARY KEY, youtube_video_id TEXT, channel_id TEXT,
                canonical_url TEXT, created_from_dataset_id TEXT
            );
            CREATE TABLE video_snapshots (
                video_id TEXT, dataset_id TEXT, title TEXT, published_at TEXT,
                duration_seconds INTEGER, video_type TEXT, views INTEGER, likes INTEGER,
                comments INTEGER, description TEXT, thumbnail_url TEXT
            );
            CREATE TABLE transcripts (
                video_id TEXT, dataset_id TEXT, availability_status TEXT, caption_type TEXT,
                language TEXT, word_count INTEGER, canonical_reference TEXT,
                transcript_sha256 TEXT, notes TEXT, archive_member_file_id TEXT
            );
            CREATE TABLE source_files (file_id TEXT PRIMARY KEY, archive_member_path TEXT);
            """
        )
        connection.execute("INSERT INTO channels VALUES (?,?)", ("CH-1", "UCTESTCHANNEL00000000001"))
        connection.execute(
            "INSERT INTO videos VALUES (?,?,?,?,?)",
            ("no-subtitle-video", "no-subtitle-video", "CH-1", "https://youtube.com/watch?v=no-subtitle-video", "DS-000029"),
        )
        connection.execute(
            "INSERT INTO video_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            ("no-subtitle-video", "DS-000029", "No Subtitle Video", "2026-01-01", 300, "video", 100, 10, 1, "A real description", "https://img/thumb.jpg"),
        )
        connection.execute("INSERT INTO source_files VALUES (?,?)", ("FILE-MANIFEST", None))
        connection.execute(
            "INSERT INTO transcripts VALUES (?,?,?,?,?,?,?,?,?,?)",
            ("no-subtitle-video", "DS-000029", "UNAVAILABLE", None, None, None, None, None, None, "FILE-MANIFEST"),
        )
        connection.commit()
        connection.close()

    def test_no_subtitle_and_no_archive_produces_explicit_gap_not_crash(self):
        from scripts.build_youtube_channel_registry import _historical_records

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._build_inventory_db(directory)
            videos, transcripts, memberships = _historical_records(root)

        self.assertEqual(1, len(videos))
        self.assertEqual("no-subtitle-video", videos[0]["youtube_video_id"])
        self.assertEqual("A real description", videos[0]["description"])
        self.assertEqual(1, len(transcripts))
        transcript = transcripts[0]
        self.assertEqual(1, transcript["is_placeholder"])
        self.assertEqual("", transcript["transcript_text"])
        self.assertIsNotNone(transcript["unavailable_reason"])
        self.assertIsNotNone(transcript["evidence_locator"])
        self.assertEqual(1, len(memberships))

    def test_normal_transcript_with_canonical_reference_still_works(self):
        from scripts.build_youtube_channel_registry import _historical_records

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._build_inventory_db(directory)
            transcript_file = root / "transcript.txt"
            transcript_file.write_text("Real transcript body.", encoding="utf-8")
            connection = sqlite3.connect(root / "data/catalog/youtube_inventory.db")
            connection.execute(
                "UPDATE transcripts SET canonical_reference=?, availability_status='AVAILABLE' WHERE video_id='no-subtitle-video'",
                ("transcript.txt",),
            )
            connection.commit()
            connection.close()

            videos, transcripts, memberships = _historical_records(root)

        self.assertEqual(1, len(transcripts))
        self.assertEqual(0, transcripts[0]["is_placeholder"])
        self.assertEqual("Real transcript body.", transcripts[0]["transcript_text"])
        self.assertEqual("transcript.txt", transcripts[0]["evidence_locator"])


class RegistryDatabaseTests(unittest.TestCase):
    def test_inventory_only_acquisition_channel_rebuilds_with_multiple_runs(self):
        from scripts.build_youtube_channel_registry import build_database

        acquired_id = "UC0000000000000000000000"
        existing_id = "UC1111111111111111111111"
        model = {
            "controls": {},
            "channels": [
                {
                    "canonical_channel_id": existing_id,
                    "channel_name": "Existing Channel",
                    "current_handle": "@existing",
                    "canonical_url": f"https://www.youtube.com/channel/{existing_id}",
                    "source_group": "IDENTITY_ONLY",
                    "target_group": "ORIGINAL_TARGET",
                    "status": "IDENTITY_VERIFIED_DATA_NOT_EXTRACTED",
                    "completed_tick": "",
                    "identity_status": "VERIFIED",
                    "extraction_status": "NOT_EXTRACTED",
                    "package_status": "NO_PACKAGE",
                    "video_metadata_status": "NONE",
                    "description_status": "NONE",
                    "transcript_status": "NONE",
                    "thumbnail_metadata_status": "NONE",
                    "visual_asset_status": "NONE",
                    "forensic_video_status": "NOT_AVAILABLE",
                    "intelligence_status": "NOT_AVAILABLE",
                    "first_party_analytics_status": "SCHEMA_READY_NO_DATA",
                    "verified_at": "2026-09-22",
                    "identity_evidence_source": "fixture",
                    "handle_unavailable_reason": None,
                    "limitations": [],
                    "dataset_ids": [],
                    "primary_dataset_id": None,
                    "video_count": 0,
                    "regular_videos": 0,
                    "shorts": 0,
                    "livestreams": 0,
                    "descriptions": 0,
                    "real_transcripts": 0,
                    "placeholders": 0,
                    "missing_transcripts": 0,
                    "workbook_path": None,
                    "transcript_zip_path": None,
                    "layer_evidence": {},
                    "visual_coverage": {
                        "thumbnail_url_count": 0,
                        "downloaded_thumbnail_count": 0,
                        "screenshot_count": 0,
                        "keyframe_count": 0,
                        "registered_source_video_count": 0,
                        "timestamped_visual_observation_count": 0,
                        "visual_evidence_level": "NONE",
                        "editing_visual_intelligence_status": "NOT_AVAILABLE",
                        "evidence_path": "fixture",
                        "limitation_reason": "fixture",
                    },
                },
                {
                    "canonical_channel_id": acquired_id,
                    "channel_name": "Acquired Channel",
                    "current_handle": "@acquired",
                    "canonical_url": f"https://www.youtube.com/channel/{acquired_id}",
                    "source_group": "HISTORICAL_CATALOG",
                    "target_group": "OUTSIDE_TARGET",
                    "status": "COMPLETE",
                    "completed_tick": "✓",
                    "identity_status": "VERIFIED",
                    "extraction_status": "COMPLETE",
                    "package_status": "HISTORICAL_FORMAT",
                    "video_metadata_status": "COMPLETE",
                    "description_status": "COMPLETE",
                    "transcript_status": "COMPLETE_REAL",
                    "thumbnail_metadata_status": "COMPLETE",
                    "visual_asset_status": "THUMBNAIL_URL_ONLY",
                    "forensic_video_status": "NOT_AVAILABLE",
                    "intelligence_status": "DATA_READY",
                    "first_party_analytics_status": "SCHEMA_READY_NO_DATA",
                    "verified_at": "2026-09-22",
                    "identity_evidence_source": "fixture",
                    "handle_unavailable_reason": None,
                    "limitations": [],
                    "dataset_ids": ["DS-000028"],
                    "primary_dataset_id": "DS-000028",
                    "video_count": 1,
                    "regular_videos": 1,
                    "shorts": 0,
                    "livestreams": 0,
                    "descriptions": 1,
                    "real_transcripts": 1,
                    "placeholders": 0,
                    "missing_transcripts": 0,
                    "workbook_path": None,
                    "transcript_zip_path": None,
                    "layer_evidence": {},
                    "visual_coverage": {
                        "thumbnail_url_count": 1,
                        "downloaded_thumbnail_count": 0,
                        "screenshot_count": 0,
                        "keyframe_count": 0,
                        "registered_source_video_count": 0,
                        "timestamped_visual_observation_count": 0,
                        "visual_evidence_level": "THUMBNAIL_URL_ONLY",
                        "editing_visual_intelligence_status": "NOT_AVAILABLE",
                        "evidence_path": "fixture",
                        "limitation_reason": "fixture",
                    },
                },
            ],
            "subjects": [],
            "submissions": [],
            "intelligence_capabilities": [{"capability_id": "TOPIC_OPPORTUNITY", "capability_name": "Topic"}],
            "intelligence_coverage": [{
                "canonical_channel_id": acquired_id,
                "capability_id": "TOPIC_OPPORTUNITY",
                "status": "DATA_READY",
                "input_data_available": True,
                "generated_artifact_available": False,
                "evidence_path": "fixture",
                "limitation_reason": None,
                "last_verified_at": "2026-09-22",
            }],
        }
        video = {
            "youtube_video_id": "video-1", "canonical_channel_id": acquired_id,
            "canonical_url": "https://www.youtube.com/watch?v=video-1", "title": "Video",
            "published_at": None, "duration_seconds": 60, "video_type": "video",
            "views": 1, "likes": 1, "comments": 0, "description": "Description",
            "description_unavailable_reason": None, "thumbnail_url": "https://example/thumbnail.jpg",
            "raw_json": None,
        }
        transcript = {
            "youtube_video_id": "video-1", "dataset_id": "DS-000028", "transcript_text": "Transcript",
            "word_count": 1, "language": "en", "caption_type": "AUTO_GENERATED",
            "is_placeholder": 0, "unavailable_reason": None, "evidence_locator": "fixture",
            "transcript_sha256": hashlib.sha256(b"Transcript").hexdigest(),
        }
        runs = [
            {"actor_run_id": run_id, "actor_dataset_id": run_id + "-dataset", "dataset_id": "DS-000028",
             "actor_name": "streamers/youtube-scraper", "evidence_path": "fixture", "run_status": "SUCCEEDED", "raw_json": None}
            for run_id in ("control-run", "full-run")
        ]
        records = ([video], [transcript], [{"dataset_id": "DS-000028", "youtube_video_id": "video-1", "evidence_locator": "fixture"}], runs)
        datasets = [{"dataset_id": "DS-000028", "dataset_name": "Acquisition", "manifest_path": "fixture", "evidence_scope": None, "limitations": None}]

        with tempfile.TemporaryDirectory() as directory, \
             patch("scripts.build_youtube_channel_registry._all_records", return_value=records), \
             patch("scripts.build_youtube_channel_registry._dataset_records", return_value=datasets), \
             patch("scripts.build_youtube_channel_registry._artifact_records", return_value=[]):
            root = Path(directory)
            schema = root / "data/catalog/channel_registry"
            schema.mkdir(parents=True)
            (schema / "schema.sql").write_text((ROOT / "data/catalog/channel_registry/schema.sql").read_text())
            (root / "data/catalog/youtube_inventory.db").write_bytes(b"fixture")
            authority = root / "data/raw/channel-targets"
            authority.mkdir(parents=True)
            (authority / "user-supplied-youtube-channels-2026-09-14.json").write_text(
                json.dumps({"controls": {"ordered_payload_sha256": "fixture"}})
            )
            path = root / "registry.db"
            build_database(root, path, model)
            connection = sqlite3.connect(path)
            try:
                self.assertEqual([], connection.execute("PRAGMA foreign_key_check").fetchall())
                self.assertEqual(1, connection.execute("SELECT count(*) FROM videos").fetchone()[0])
                self.assertEqual(2, connection.execute("SELECT count(*) FROM actor_runs").fetchone()[0])
                self.assertEqual("DATA_READY", connection.execute("SELECT status FROM intelligence_coverage").fetchone()[0])
            finally:
                connection.close()
            model["channels"] = [row for row in model["channels"] if row["canonical_channel_id"] == acquired_id]
            build_database(root, path, model)
            connection = sqlite3.connect(path)
            try:
                self.assertEqual(1, connection.execute("SELECT count(*) FROM channels").fetchone()[0])
            finally:
                connection.close()

    def test_invalid_orphan_video_is_rejected(self):
        from scripts.build_youtube_channel_registry import build_database

        orphan = {
            "youtube_video_id": "orphan", "canonical_channel_id": "UC9999999999999999999999",
            "canonical_url": "https://www.youtube.com/watch?v=orphan", "title": "Orphan",
            "published_at": None, "duration_seconds": None, "video_type": "video",
            "views": None, "likes": None, "comments": None, "description": None,
            "description_unavailable_reason": "missing", "thumbnail_url": None, "raw_json": None,
        }
        model = {"channels": [], "subjects": [], "submissions": [], "intelligence_capabilities": [], "intelligence_coverage": []}
        datasets = [{"dataset_id": "DS-000028", "dataset_name": "Acquisition", "manifest_path": "fixture", "evidence_scope": None, "limitations": None}]
        with tempfile.TemporaryDirectory() as directory, \
             patch("scripts.build_youtube_channel_registry._all_records", return_value=([orphan], [], [], [])), \
             patch("scripts.build_youtube_channel_registry._dataset_records", return_value=datasets), \
             patch("scripts.build_youtube_channel_registry._artifact_records", return_value=[]):
            root = Path(directory)
            schema = root / "data/catalog/channel_registry"
            schema.mkdir(parents=True)
            (schema / "schema.sql").write_text((ROOT / "data/catalog/channel_registry/schema.sql").read_text())
            with self.assertRaisesRegex(ValueError, "video orphan references missing channel"):
                build_database(root, root / "registry.db", model)

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
                self.assertEqual(2027, connection.execute("SELECT count(*) FROM videos").fetchone()[0])
                self.assertEqual(2015, connection.execute("SELECT count(*) FROM transcripts WHERE is_placeholder = 0").fetchone()[0])
                self.assertEqual(12, connection.execute("SELECT count(*) FROM transcripts WHERE is_placeholder = 1").fetchone()[0])
                self.assertEqual(15, connection.execute("SELECT count(*) FROM videos WHERE description IS NULL").fetchone()[0])
                self.assertEqual(37, connection.execute("SELECT count(*) FROM channels WHERE source_group='STANDARD_PACKAGE'").fetchone()[0])
                self.assertEqual(6, connection.execute("SELECT count(*) FROM channels WHERE source_group='HISTORICAL_CATALOG'").fetchone()[0])
                self.assertEqual(29, connection.execute("SELECT count(*) FROM channels WHERE source_group='IDENTITY_ONLY'").fetchone()[0])
                self.assertEqual(72 * 11, connection.execute("SELECT count(*) FROM channel_data_layers").fetchone()[0])
                self.assertEqual(72, connection.execute("SELECT count(*) FROM visual_coverage").fetchone()[0])
                self.assertEqual(72 * 8, connection.execute("SELECT count(*) FROM intelligence_coverage").fetchone()[0])
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
        self.assertEqual(72, result["controls"]["canonical_channels"])
        self.assertEqual(63, result["controls"]["target_channels"])
        self.assertEqual(43, result["controls"]["channels_with_video_data"])
        self.assertEqual(29, result["controls"]["identity_only_channels"])
        self.assertEqual(37, result["controls"]["standard_packages"])
        self.assertEqual(6, result["controls"]["historical_channels"])
        self.assertEqual(576, result["controls"]["intelligence_coverage_rows"])


if __name__ == "__main__":
    unittest.main()
