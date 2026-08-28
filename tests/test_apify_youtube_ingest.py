import copy
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import apify_youtube_ingest as ayi  # noqa: E402
import report_channel_coverage as coverage  # noqa: E402
import report_common  # noqa: E402
from inventory_catalog import CatalogError  # noqa: E402


FIXTURES = Path(__file__).parent / "fixtures" / "apify_youtube"
TS = "2026-08-27T12:11:47.105Z"


def load_fixture(name):
    return json.loads((FIXTURES / name).read_text())


class ApifyYouTubeIngestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = self.root / "catalog.db"
        conn = sqlite3.connect(str(self.db))
        conn.execute("PRAGMA foreign_keys=ON")
        for schema in sorted((REPO_ROOT / "schemas/inventory").glob("*.sql")):
            conn.executescript(schema.read_text())
        conn.execute(
            """INSERT INTO datasets
               (dataset_id, dataset_name, semantic_class, description, source_type,
                ingestion_mode, status, discovered_as, date_received, created_at,
                updated_at, notes)
               VALUES ('DS-000006', 'Dr. Aliza Wright / Advice — Competitor Channel Screenshots',
                       'B', 'fixture', 'EXTERNAL_FOLDER', 'COPY', 'INGESTED',
                       'DR_ALIZA_WRIGHT', ?, ?, ?, 'content_domain=HEALTH')""",
            (TS, TS, TS),
        )
        conn.execute(
            "INSERT INTO source_batches VALUES ('BATCH-FIXTURE','fixture',?,?,'COMPLETED',1,'fixture',NULL)",
            (TS, TS),
        )
        conn.execute(
            """INSERT INTO batch_roots
               (batch_root_id,batch_id,root_index,supplied_path,canonical_path,
                exists_at_discovery,root_type,file_count,dir_count,symlink_count,
                total_size_bytes,observed_at,notes)
               VALUES ('BROOT-FIXTURE','BATCH-FIXTURE',1,'fixture','fixture',1,'DIR',1,0,0,1,?,NULL)""",
            (TS,),
        )
        conn.execute(
            """INSERT INTO discovered_files
               (discovered_file_id,batch_id,batch_root_id,entry_type,absolute_path,
                relative_path,extension,mime_type,size_bytes,sha256,dataset_id,
                disposition,disposition_reason,processing_status,created_at)
               VALUES ('DF-FIXTURE','BATCH-FIXTURE','BROOT-FIXTURE','FILE','fixture.png',
                       'fixture.png','.png','image/png',1,?, 'DS-000006','INGEST',
                       'fixture','RECORDED',?)""",
            ("a" * 64, TS),
        )
        conn.execute(
            """INSERT INTO visual_assets
               (visual_asset_id,discovered_file_id,dataset_id,sha256,created_at)
               VALUES ('VA-FIXTURE','DF-FIXTURE','DS-000006',?,?)""",
            ("a" * 64, TS),
        )
        conn.execute(
            """INSERT INTO visual_observations
               (visual_observation_id,visual_asset_id,observation_type,
                observation_method,source_surface,extracted_text,confidence,
                structured_json,evidence_layer,observed_at,notes)
               VALUES ('VO-FIXTURE','VA-FIXTURE','SEMANTIC_INSPECTION','fixture',
                       'YOUTUBE_UI',?,1.0,?,'OBSERVATION',?,NULL)""",
            ("youtube.com/@Dr.AlizaWrightAdvice", json.dumps({
                "channel_identity": {
                    "channel_name": "Dr. Aliza Wright | Advice",
                    "handle": "@Dr.AlizaWrightAdvice",
                },
                "visual_packaging_pattern_notes": "fixture packaging evidence",
            }), TS),
        )
        conn.execute(
            """INSERT INTO entity_classifications
               (classification_id,dataset_id,target_type,target_ref,content_domain,
                editing_style,evidence_layer,source_locator,created_at)
               VALUES ('EC-FIXTURE','DS-000006','DATASET','DS-000006','HEALTH',
                       'UNKNOWN','OBSERVATION','fixture',?)""",
            (TS,),
        )
        conn.commit()
        conn.close()
        self.run = load_fixture("run_succeeded.json")
        self.with_transcript = load_fixture("video_with_transcript.json")
        self.without_transcript = load_fixture("video_without_transcript.json")
        self.actor_input = ayi.build_actor_input(
            "https://www.youtube.com/@Dr.AlizaWrightAdvice", 2
        )

    def tearDown(self):
        self.tmp.cleanup()

    def ingest(self, run=None, records=None, actor_input=None):
        return ayi.ingest_run(
            self.db,
            "DS-000006",
            "https://www.youtube.com/@Dr.AlizaWrightAdvice",
            run or copy.deepcopy(self.run),
            actor_input or copy.deepcopy(self.actor_input),
            records or [copy.deepcopy(self.with_transcript), copy.deepcopy(self.without_transcript)],
            raw_root=self.root / "raw",
            manifests_dir=self.root / "manifests",
        )

    def connect(self):
        conn = sqlite3.connect(str(self.db))
        conn.row_factory = sqlite3.Row
        return conn

    def test_apify_record_normalization(self):
        item = ayi.normalize_record(self.with_transcript, 0)
        self.assertEqual(item["duration_seconds"], 605)
        self.assertEqual(item["transcript"]["availability_status"], "AVAILABLE")
        self.assertEqual(item["transcript"]["caption_type"], "user_generated")
        self.assertEqual(item["thumbnail_urls"], [self.with_transcript["thumbnailUrl"]])

    def test_missing_transcript_is_registered_unavailable(self):
        self.ingest(records=[copy.deepcopy(self.without_transcript)])
        with self.connect() as conn:
            row = conn.execute("SELECT availability_status, transcript_source FROM transcripts").fetchone()
        self.assertEqual(tuple(row), ("UNAVAILABLE", "APIFY"))

    def test_duplicate_video_id_is_deduplicated(self):
        result = self.ingest(records=[copy.deepcopy(self.with_transcript), copy.deepcopy(self.with_transcript)])
        self.assertEqual(result["validation"]["unique_videos"], 1)
        self.assertEqual(result["validation"]["duplicate_video_ids"], ["AAAAAAAAAAA"])
        with self.connect() as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos").fetchone()[0], 1)

    def test_same_video_newer_run_appends_snapshot(self):
        self.ingest(records=[copy.deepcopy(self.with_transcript)])
        newer_run = copy.deepcopy(self.run)
        newer_run.update({"id": "fixtureRunNewer", "startedAt": "2026-08-29T10:00:00.000Z",
                          "finishedAt": "2026-08-29T10:00:10.000Z", "usageTotalUsd": 0.004})
        newer_video = copy.deepcopy(self.with_transcript)
        newer_video["viewCount"] = 250
        self.ingest(run=newer_run, records=[newer_video])
        with self.connect() as conn:
            rows = conn.execute("SELECT views FROM video_snapshots ORDER BY observed_at").fetchall()
        self.assertEqual([row[0] for row in rows], [100, 250])

    def test_identity_reconciliation_uses_exact_handle(self):
        result = self.ingest(records=[copy.deepcopy(self.with_transcript)])
        with self.connect() as conn:
            channel = conn.execute("SELECT youtube_channel_id,handle,created_from_dataset_id FROM channels").fetchone()
            links = conn.execute("SELECT relationship_type FROM channel_dataset_links WHERE channel_id=?", (result["channel_id"],)).fetchall()
        self.assertEqual(channel["handle"], "@Dr.AlizaWrightAdvice")
        self.assertEqual(channel["created_from_dataset_id"], "DS-000006")
        self.assertIn("IDENTITY_EVIDENCE", {row[0] for row in links})

    def test_screenshot_evidence_is_preserved(self):
        with self.connect() as conn:
            before = conn.execute("SELECT structured_json FROM visual_observations WHERE visual_observation_id='VO-FIXTURE'").fetchone()[0]
        self.ingest(records=[copy.deepcopy(self.with_transcript)])
        with self.connect() as conn:
            after = conn.execute("SELECT structured_json FROM visual_observations WHERE visual_observation_id='VO-FIXTURE'").fetchone()[0]
        self.assertEqual(after, before)

    def test_malformed_result_rejects_normalized_ingestion(self):
        malformed = copy.deepcopy(self.with_transcript)
        malformed.pop("title")
        with self.assertRaises(CatalogError):
            self.ingest(records=[malformed])
        with self.connect() as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos").fetchone()[0], 0)
            self.assertEqual(conn.execute("SELECT status FROM ingestion_runs").fetchone()[0], "FAILED")

    def test_failed_actor_run_is_recorded_without_entities(self):
        failed = copy.deepcopy(self.run)
        failed.update({"id": "fixtureRunFailed", "status": "FAILED", "usageTotalUsd": 0.001})
        with self.assertRaises(CatalogError):
            self.ingest(run=failed, records=[])
        with self.connect() as conn:
            self.assertEqual(conn.execute("SELECT run_status FROM apify_source_runs").fetchone()[0], "FAILED")
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos").fetchone()[0], 0)

    def test_cost_cap_enforcement(self):
        self.assertEqual(ayi.maximum_results_for_cap("0.004", "0.50"), 125)
        self.assertEqual(ayi.enforce_cost_cap(125, "0.004", "0.50"), ayi.Decimal("0.500"))
        with self.assertRaises(CatalogError):
            ayi.enforce_cost_cap(126, "0.004", "0.50")

    def test_billing_requires_all_result_events_before_final(self):
        run = copy.deepcopy(self.run)
        self.assertTrue(ayi.billing_is_final(run, 2))
        run["usageTotalUsd"] = 0.004
        run["chargedEventCounts"]["result"] = 1
        run["eventUsage"]["result"]["eventTotalUsd"] = 0.004
        self.assertFalse(ayi.billing_is_final(run, 2))

    def test_secret_values_are_not_persisted(self):
        actor_input = copy.deepcopy(self.actor_input)
        actor_input["token"] = "SECRET_SHOULD_NOT_PERSIST"
        actor_input["Authorization"] = "SECRET_SHOULD_NOT_PERSIST"
        result = self.ingest(records=[copy.deepcopy(self.with_transcript)], actor_input=actor_input)
        with self.connect() as conn:
            stored = conn.execute("SELECT input_json FROM apify_source_runs").fetchone()[0]
        manifest = Path(result["manifest_path"]).read_text()
        self.assertNotIn("SECRET_SHOULD_NOT_PERSIST", stored)
        self.assertNotIn("SECRET_SHOULD_NOT_PERSIST", manifest)

    def test_idempotent_actor_run_rerun(self):
        first = self.ingest(records=[copy.deepcopy(self.with_transcript)])
        second = self.ingest(records=[copy.deepcopy(self.with_transcript)])
        self.assertEqual(first["status"], "COMPLETED")
        self.assertEqual(second["status"], "ALREADY_INGESTED")
        with self.connect() as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM video_snapshots").fetchone()[0], 1)

    def test_field_provenance_carries_source_run_and_method(self):
        self.ingest(records=[copy.deepcopy(self.with_transcript)])
        with self.connect() as conn:
            rows = conn.execute("SELECT field_name,source_locator,extraction_method,notes FROM field_provenance").fetchall()
        names = {row["field_name"] for row in rows}
        self.assertTrue({"youtube_channel_id", "title", "description_char_count",
                         "transcript_word_count", "thumbnail_url", "availability_status"}.issubset(names))
        self.assertTrue(all(row["source_locator"].startswith("apify://") for row in rows))
        self.assertTrue(all(row["extraction_method"] == "apify_actor_record" for row in rows))
        self.assertTrue(all("source_run=APIFYRUN-" in row["notes"] for row in rows))

    def test_tier_b_upgrades_to_tier_a_without_duplicate_competitor(self):
        self.ingest(records=[copy.deepcopy(self.with_transcript)])
        with self.connect() as conn:
            payload, _ = coverage.build_report(conn)
        self.assertEqual(len(payload["registered_channels"]), 1)
        self.assertEqual(len(payload["dataset_evidenced_competitors"]), 0)
        self.assertEqual(payload["registered_channels"][0]["display_name"], "Dr. Aliza Wright | Advice")

    def test_markdown_report_escapes_channel_name_pipe(self):
        row = report_common.md_table(["Name"], [["Dr. Aliza Wright | Advice"]])[-1]
        self.assertIn("Dr. Aliza Wright \\| Advice", row)


if __name__ == "__main__":
    unittest.main()
