import json
import sqlite3
import unittest
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
        self.assertEqual(69, self.workbook["All Channels"].max_row - 4)
        self.assertEqual(29, self.workbook["Pending Channels"].max_row - 4)
        self.assertEqual(67, self.workbook["Submitted URLs"].max_row - 4)
        self.assertEqual(552, self.workbook["Intelligence Coverage"].max_row - 4)
        self.assertEqual(
            [row["canonical_channel_id"] for row in self.model["channels"]],
            [
                self.workbook["All Channels"].cell(row=index, column=1).value
                for index in range(5, 74)
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
            [(visual.cell(row, 1).value, visual.cell(row, 6).value, visual.cell(row, 10).value) for row in range(77, 84)],
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
                for row in range(5, 557)
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
                for row in range(5, 30)
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


if __name__ == "__main__":
    unittest.main()
