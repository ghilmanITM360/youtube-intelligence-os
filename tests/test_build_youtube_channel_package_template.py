import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILDER = REPO_ROOT / "scripts" / "build_youtube_channel_package_template.py"
SHEETS = ["Channel Overview", "All Videos", "Descriptions", "Verification", "Analysis"]


class YouTubeChannelPackageTemplateTests(unittest.TestCase):
    def test_builds_content_free_template_while_preserving_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.xlsx"
            output = root / "template.xlsx"
            workbook = Workbook()
            workbook.active.title = SHEETS[0]
            for name in SHEETS[1:]:
                workbook.create_sheet(name)
            videos = workbook["All Videos"]
            videos["A1"] = "Title"
            videos["M5"] = "=1+1"
            videos["A1"].font = Font(bold=True)
            videos.merge_cells("A97:I97")
            workbook.save(source)

            result = subprocess.run(
                [sys.executable, str(BUILDER), "--source", str(source), "--output", str(output)],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            built = load_workbook(output, data_only=False)
            self.assertEqual(built.sheetnames, SHEETS)
            self.assertTrue(built["All Videos"]["A1"].font.bold)
            self.assertIn("A97:I97", {str(value) for value in built["All Videos"].merged_cells.ranges})
            self.assertFalse(any(cell.value is not None for sheet in built for row in sheet.iter_rows() for cell in row))


if __name__ == "__main__":
    unittest.main()
