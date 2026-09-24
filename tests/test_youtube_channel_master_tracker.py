import csv
import hashlib
import json
import re
import sqlite3
import unittest
import zipfile
from pathlib import Path

from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json"
WORKBOOK_PATH = ROOT / "data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx"


class ChannelMasterTrackerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
        cls.workbook = load_workbook(WORKBOOK_PATH, data_only=False, read_only=False)

    @classmethod
    def tearDownClass(cls):
        cls.workbook.close()

    def test_required_sheets_and_tables(self):
        self.assertEqual(
            [
                "Dashboard",
                "All Channels",
                "Pending Channels",
                "Data Coverage",
                "Visual Evidence",
                "Datasets",
                "Submitted URLs",
                "Intelligence Coverage",
                "Definitions",
            ],
            self.workbook.sheetnames,
        )
        for name in self.workbook.sheetnames[1:-1]:
            self.assertTrue(self.workbook[name].tables, name)

    def test_channel_submission_and_intelligence_rows_reconcile(self):
        self.assertEqual(len(self.model["channels"]), self.workbook["All Channels"].max_row - 4)
        self.assertEqual(29, self.workbook["Pending Channels"].max_row - 4)
        self.assertEqual(67, self.workbook["Submitted URLs"].max_row - 4)
        self.assertEqual(len(self.model["intelligence_coverage"]), self.workbook["Intelligence Coverage"].max_row - 4)
        self.assertEqual(
            [row["canonical_channel_id"] for row in self.model["channels"]],
            [
                self.workbook["All Channels"].cell(row=index, column=1).value
                for index in range(5, 5 + len(self.model["channels"]))
            ],
        )

    def test_dashboard_is_formula_driven(self):
        dashboard = self.workbook["Dashboard"]
        formulas = [
            cell.value
            for row in dashboard.iter_rows()
            for cell in row
            if isinstance(cell.value, str) and cell.value.startswith("=")
        ]
        self.assertGreaterEqual(len(formulas), 14)
        self.assertTrue(any("'All Channels'" in formula for formula in formulas))
        self.assertTrue(any("'Visual Evidence'" in formula for formula in formulas))

    def test_clickable_channel_and_evidence_links(self):
        for sheet_name, columns in {
            "All Channels": (4, 28),
            "Pending Channels": (2,),
            "Submitted URLs": (5, 6),
            "Intelligence Coverage": (8,),
        }.items():
            sheet = self.workbook[sheet_name]
            for row in range(5, sheet.max_row + 1):
                self.assertTrue(
                    any(
                        isinstance(sheet.cell(row=row, column=column).value, str)
                        and sheet.cell(row=row, column=column).value.startswith("=HYPERLINK(")
                        for column in columns
                    ),
                    f"{sheet_name} row {row}",
                )

    def test_repository_links_use_main_and_existing_files(self):
        prefix = "https://github.com/ghilmanITM360/youtube-intelligence-os/blob/main/"
        count = 0
        for sheet in self.workbook.worksheets:
            for row in sheet.iter_rows():
                for cell in row:
                    formula = cell.value
                    if not isinstance(formula, str) or not formula.startswith("=HYPERLINK("):
                        continue
                    match = re.match(r'=HYPERLINK\("([^"]+)","([^"]+)"\)', formula)
                    self.assertIsNotNone(match, (sheet.title, cell.coordinate))
                    url = match.group(1)
                    if not url.startswith("https://github.com/ghilmanITM360/youtube-intelligence-os/blob/"):
                        continue
                    self.assertTrue(url.startswith(prefix), (sheet.title, cell.coordinate, url))
                    self.assertTrue((ROOT / url[len(prefix):]).is_file(), (sheet.title, cell.coordinate, url))
                    count += 1
        self.assertGreater(count, 600)

    def test_independent_status_columns_are_present(self):
        headers = {
            self.workbook["All Channels"].cell(row=4, column=column).value
            for column in range(1, self.workbook["All Channels"].max_column + 1)
        }
        self.assertTrue(
            {
                "Identity Verified",
                "Video Data Available",
                "Extraction Status",
                "Standard Package Available",
                "Historical-Format Data Available",
                "Transcript Status",
                "Thumbnail URLs Available",
                "Downloaded Thumbnail Evidence",
                "Forensic Video Evidence",
                "Topic Intelligence",
                "Packaging Intelligence",
                "Hook Intelligence",
                "Script Intelligence",
                "Editing/Visual Intelligence",
                "Unified Orchestration",
                "Channel Strategy",
                "First-Party Analytics",
            }.issubset(headers)
        )

    def test_channel_visual_and_capability_values_reconcile(self):
        sheet = self.workbook["All Channels"]
        headers = {sheet.cell(4, column).value: column for column in range(1, sheet.max_column + 1)}
        for index, source in enumerate(self.model["channels"], start=5):
            expected_missing_descriptions = (
                0 if source["descriptions"] is None else source["video_count"] - source["descriptions"]
            )
            self.assertEqual(source["target_group"], sheet.cell(index, headers["Target Membership"]).value)
            self.assertEqual(source["extraction_status"], sheet.cell(index, headers["Extraction Status"]).value)
            self.assertEqual(source["video_count"], sheet.cell(index, headers["Saved Video Count"]).value)
            self.assertEqual(source["real_transcripts"], sheet.cell(index, headers["Real Transcripts"]).value)
            self.assertEqual(source["placeholders"], sheet.cell(index, headers["Transcript Placeholders"]).value)
            self.assertEqual(expected_missing_descriptions, sheet.cell(index, headers["Missing Descriptions"]).value)
            self.assertEqual(source["transcript_status"], sheet.cell(index, headers["Transcript Status"]).value)
            self.assertEqual(
                ", ".join(source["dataset_ids"]) or "—",
                sheet.cell(index, headers["Dataset IDs"]).value,
            )

        visual = self.workbook["Visual Evidence"]
        for index, source in enumerate(self.model["channels"], start=5):
            coverage = source["visual_coverage"]
            self.assertEqual(coverage["thumbnail_url_count"], visual.cell(index, 4).value)
            self.assertEqual(coverage["downloaded_thumbnail_count"], visual.cell(index, 5).value)
            self.assertEqual(coverage["screenshot_count"], visual.cell(index, 6).value)
            self.assertEqual(coverage["keyframe_count"], visual.cell(index, 7).value)
            self.assertEqual(coverage["registered_source_video_count"], visual.cell(index, 8).value)
            self.assertEqual(coverage["timestamped_visual_observation_count"], visual.cell(index, 9).value)
            self.assertEqual(coverage["visual_evidence_level"], visual.cell(index, 10).value)
        self.assertEqual(
            [(row["subject_name"], row["screenshot_count"], row["visual_evidence_level"]) for row in self.model["subjects"]],
            [(visual.cell(row, 1).value, visual.cell(row, 6).value, visual.cell(row, 10).value) for row in range(7 + len(self.model["channels"]), 7 + len(self.model["channels"]) + len(self.model["subjects"]))],
        )

        intelligence = self.workbook["Intelligence Coverage"]
        self.assertEqual(
            [
                (
                    row["canonical_channel_id"],
                    row["capability_id"],
                    row["status"],
                    "✓" if row["input_data_available"] else "No",
                    "✓" if row["generated_artifact_available"] else "No",
                )
                for row in self.model["intelligence_coverage"]
            ],
            [
                (
                    intelligence.cell(row, 1).value,
                    intelligence.cell(row, 3).value,
                    intelligence.cell(row, 4).value,
                    intelligence.cell(row, 5).value,
                    intelligence.cell(row, 6).value,
                )
                for row in range(5, 5 + len(self.model["intelligence_coverage"]))
            ],
        )

    def test_submissions_datasets_and_portable_links_reconcile(self):
        submitted = self.workbook["Submitted URLs"]
        self.assertEqual(
            [
                (
                    row["global_row"],
                    row["batch"],
                    row["batch_row"],
                    row["original_url"],
                    "✓" if row["is_exact_duplicate"] else "No",
                    row["duplicate_of_global_row"] if row["duplicate_of_global_row"] is not None else "—",
                    row["canonical_channel_id"],
                )
                for row in self.model["submissions"]
            ],
            [
                (
                    submitted.cell(row, 1).value,
                    submitted.cell(row, 2).value,
                    submitted.cell(row, 3).value,
                    submitted.cell(row, 4).value,
                    submitted.cell(row, 7).value,
                    submitted.cell(row, 8).value,
                    submitted.cell(row, 9).value,
                )
                for row in range(5, 72)
            ],
        )

        connection = sqlite3.connect(ROOT / "data/catalog/youtube_channel_registry.db")
        try:
            datasets = connection.execute(
                """
                SELECT d.dataset_id, count(distinct dc.canonical_channel_id),
                       count(distinct dv.youtube_video_id)
                FROM datasets d
                LEFT JOIN dataset_channels dc ON dc.dataset_id=d.dataset_id
                LEFT JOIN dataset_videos dv ON dv.dataset_id=d.dataset_id
                GROUP BY d.dataset_id ORDER BY d.dataset_id
                """
            ).fetchall()
        finally:
            connection.close()
        dataset_sheet = self.workbook["Datasets"]
        self.assertEqual(
            datasets,
            [
                (dataset_sheet.cell(row, 1).value, dataset_sheet.cell(row, 3).value, dataset_sheet.cell(row, 4).value)
                for row in range(5, dataset_sheet.max_row + 1)
            ],
        )

        formulas = [
            cell.value
            for sheet in self.workbook.worksheets
            for row in sheet.iter_rows()
            for cell in row
            if isinstance(cell.value, str) and cell.value.startswith("=")
        ]
        self.assertFalse(any("/Users/" in formula or "file://" in formula for formula in formulas))

    def test_raw_csv_json_sqlite_workbook_and_query_report_reconcile(self):
        raw = json.loads(
            (ROOT / "data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json").read_text(encoding="utf-8")
        )
        with (ROOT / "data/manifests/YOUTUBE_CHANNEL_TARGETS.csv").open(encoding="utf-8", newline="") as handle:
            csv_rows = {row["canonical_channel_id"]: row for row in csv.DictReader(handle)}
        model_rows = {row["canonical_channel_id"]: row for row in self.model["channels"]}
        target_ids = {identifier for identifier, row in model_rows.items() if row["target_group"] != "OUTSIDE_TARGET"}
        self.assertEqual(
            [row["original_url"] for row in raw["submissions"]],
            [row["original_url"] for row in self.model["submissions"]],
        )
        self.assertEqual(target_ids, {row["canonical_channel_id"] for row in self.model["submissions"]})
        self.assertEqual(set(model_rows), set(csv_rows))

        all_channels = self.workbook["All Channels"]
        all_headers = {all_channels.cell(4, column).value: column for column in range(1, all_channels.max_column + 1)}
        workbook_rows = {
            all_channels.cell(row, 1).value: row
            for row in range(5, all_channels.max_row + 1)
        }
        visual = self.workbook["Visual Evidence"]
        visual_rows = {visual.cell(row, 2).value: row for row in range(5, 5 + len(self.model["channels"]))}

        connection = sqlite3.connect(ROOT / "data/catalog/youtube_channel_registry.db")
        connection.row_factory = sqlite3.Row
        try:
            db_rows = {
                row["canonical_channel_id"]: row
                for row in connection.execute(
                    """
                    SELECT s.*,v.visual_evidence_level
                    FROM v_channel_status s JOIN visual_coverage v USING(canonical_channel_id)
                    """
                )
            }
            self.assertEqual(set(model_rows), set(db_rows))
            self.assertEqual(set(model_rows), set(workbook_rows))
            for identifier, source in model_rows.items():
                csv_row = csv_rows[identifier]
                db_row = db_rows[identifier]
                workbook_row = workbook_rows[identifier]
                visual_row = visual_rows[identifier]
                missing_descriptions = 0 if source["descriptions"] is None else source["video_count"] - source["descriptions"]
                self.assertEqual(
                    (
                        source["channel_name"], source["target_group"], source["status"], source["package_status"],
                        source["video_count"], source["real_transcripts"], source["placeholders"], source["description_status"],
                        source["visual_asset_status"], source["first_party_analytics_status"], " | ".join(source["dataset_ids"]),
                        source["workbook_path"] or "", source["transcript_zip_path"] or "",
                    ),
                    (
                        csv_row["channel_name"], csv_row["target_group"], csv_row["status"], csv_row["package_status"],
                        int(csv_row["video_count"]), int(csv_row["real_transcripts"]), int(csv_row["placeholders"]),
                        csv_row["description_status"],
                        csv_row["visual_asset_status"], csv_row["first_party_analytics_status"], csv_row["dataset_ids"],
                        csv_row["workbook_path"], csv_row["transcript_zip_path"],
                    ),
                )
                self.assertEqual(
                    (
                        source["channel_name"], source["target_group"], source["status"], source["package_status"],
                        source["video_count"], source["real_transcripts"], source["placeholders"], missing_descriptions,
                        source["visual_asset_status"], source["first_party_analytics_status"],
                    ),
                    (
                        db_row["channel_name"], db_row["target_group"], db_row["status"], db_row["package_status"],
                        db_row["video_count"], db_row["real_transcript_count"], db_row["placeholder_count"],
                        db_row["missing_description_count"], db_row["visual_evidence_level"],
                        db_row["first_party_analytics_status"],
                    ),
                )
                self.assertEqual(source["channel_name"], all_channels.cell(workbook_row, all_headers["Channel Name"]).value)
                self.assertEqual(source["target_group"], all_channels.cell(workbook_row, all_headers["Target Membership"]).value)
                self.assertEqual(source["extraction_status"], all_channels.cell(workbook_row, all_headers["Extraction Status"]).value)
                self.assertEqual(source["video_count"], all_channels.cell(workbook_row, all_headers["Saved Video Count"]).value)
                self.assertEqual(source["visual_asset_status"], visual.cell(visual_row, 10).value)
                self.assertEqual(", ".join(source["dataset_ids"]) or "—", all_channels.cell(workbook_row, all_headers["Dataset IDs"]).value)
                if source["source_group"] == "STANDARD_PACKAGE":
                    artifacts = dict(
                        connection.execute(
                            "SELECT artifact_type,repository_path FROM artifacts WHERE canonical_channel_id=? AND artifact_type IN ('WORKBOOK','TRANSCRIPT_ZIP')",
                            (identifier,),
                        )
                    )
                    self.assertEqual(source["workbook_path"], artifacts["WORKBOOK"])
                    self.assertEqual(source["transcript_zip_path"], artifacts["TRANSCRIPT_ZIP"])

            database_intelligence = {
                (row["canonical_channel_id"], row["capability_id"]): tuple(row)
                for row in connection.execute(
                    "SELECT canonical_channel_id,capability_id,status,input_data_available,generated_artifact_available,evidence_path FROM intelligence_coverage"
                )
            }
            intelligence_sheet = self.workbook["Intelligence Coverage"]
            for row_number, source in enumerate(self.model["intelligence_coverage"], start=5):
                key = (source["canonical_channel_id"], source["capability_id"])
                self.assertEqual(
                    key + (source["status"], int(source["input_data_available"]), int(source["generated_artifact_available"]), source["evidence_path"]),
                    database_intelligence[key],
                )
                self.assertEqual(key, (intelligence_sheet.cell(row_number, 1).value, intelligence_sheet.cell(row_number, 3).value))
                self.assertEqual(source["status"], intelligence_sheet.cell(row_number, 4).value)
                self.assertEqual("✓" if source["input_data_available"] else "No", intelligence_sheet.cell(row_number, 5).value)
                self.assertEqual("✓" if source["generated_artifact_available"] else "No", intelligence_sheet.cell(row_number, 6).value)

            report = (ROOT / "docs/audits/YOUTUBE_CHANNEL_REGISTRY_QUERY_RESULTS_2026-09-14.md").read_text(encoding="utf-8")
            complete = "; ".join(row[0] for row in connection.execute("SELECT channel_name FROM channels WHERE target_group<>'OUTSIDE_TARGET' AND extraction_status='COMPLETE' ORDER BY channel_name"))
            pending = "; ".join(row[0] for row in connection.execute("SELECT channel_name FROM channels WHERE target_group<>'OUTSIDE_TARGET' AND extraction_status='NOT_EXTRACTED' ORDER BY lower(channel_name)"))
            standard = "; ".join(row[0] for row in connection.execute("SELECT channel_name FROM channels WHERE source_group='STANDARD_PACKAGE' ORDER BY channel_name"))
            self.assertIn(f"26 rows: {complete}.", report)
            self.assertIn(f"29 rows: {pending}.", report)
            self.assertIn(f"37 rows: {standard}.", report)
            for text in ("Registry total: 2,116 real transcripts.", "Total: 11.", "Total: 16.", "72 channels: `SCHEMA_READY_NO_DATA`."):
                self.assertIn(text, report)
        finally:
            connection.close()

    def test_standard_transcript_archives_crc_and_database_text_reconcile(self):
        from scripts.build_youtube_channel_registry import _parse_structured_transcript

        connection = sqlite3.connect(ROOT / "data/catalog/youtube_channel_registry.db")
        errors = []
        counts = {"channels": 0, "videos": 0, "real": 0, "placeholders": 0, "over_excel_limit": 0}
        try:
            for channel in self.model["channels"]:
                if channel["source_group"] != "STANDARD_PACKAGE":
                    continue
                counts["channels"] += 1
                with zipfile.ZipFile(ROOT / channel["transcript_zip_path"]) as archive:
                    self.assertIsNone(archive.testzip(), channel["channel_name"])
                    members = [name for name in archive.namelist() if name != "INDEX.txt"]
                    self.assertEqual(channel["video_count"], len(members), channel["channel_name"])
                    self.assertEqual(len(members), len(set(members)), channel["channel_name"])
                    for member in members:
                        text = archive.read(member).decode("utf-8")
                        body, placeholder, reason = _parse_structured_transcript(text)
                        header = text.split("\n==========", 1)[0]
                        video_id = dict(re.findall(r"^([^:\n]+?)\s*:\s*(.*)$", header, re.MULTILINE)).get("Video ID")
                        row = connection.execute(
                            "SELECT transcript_text,is_placeholder,unavailable_reason,transcript_sha256 FROM transcripts WHERE youtube_video_id=?",
                            (video_id,),
                        ).fetchone()
                        if not row:
                            errors.append(f"{channel['channel_name']}: missing {video_id}")
                            continue
                        if (body, int(placeholder), hashlib.sha256(body.encode()).hexdigest()) != (row[0], row[1], row[3]):
                            errors.append(f"{channel['channel_name']}: mismatch {video_id}")
                        if placeholder and not (reason and row[2]):
                            errors.append(f"{channel['channel_name']}: missing placeholder reason {video_id}")
                        counts["videos"] += 1
                        counts["real"] += int(not placeholder)
                        counts["placeholders"] += int(placeholder)
                        counts["over_excel_limit"] += int(not placeholder and len(body) > 32_767)
        finally:
            connection.close()
        self.assertFalse(errors, errors[:10])
        self.assertEqual(
            {"channels": 37, "videos": 1758, "real": 1748, "placeholders": 10, "over_excel_limit": 33},
            counts,
        )


if __name__ == "__main__":
    unittest.main()
