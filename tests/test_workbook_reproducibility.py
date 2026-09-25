"""Regression guard for the 2026-09-25 workbook-reproducibility defects.

History: build_v3_workbook.py had 3 hardcoded absolute /tmp paths (not
portable outside the original session's scratch checkout), and — separately —
its copy of sheets 11/12/25/26/27/29 from the V2 source workbook carried
forward the fabricated GT-20 Google Trends claim (mean_90d_after=16.7/20)
that was later retracted (STAGE2-CORRECTION-LEDGER.md NC-03) and hand-patched
only on the committed .xlsx, never in the script that builds it. Sheet
39_V3_BREAKOUT_INVENTORY was missing the 9 Case-13 (Better Health While
Aging) rows for the same reason. Re-running the script from a stale copy
would have silently regenerated a workbook with the disproven claim and a
smaller breakout inventory than what is actually canonical.
"""
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
V3_DIR = REPO_ROOT / "docs/research/senior-health-2026-09-25/forensic-v3"
SCRIPT = V3_DIR / "scripts/build_v3_workbook.py"
COMMITTED_WORKBOOK = V3_DIR / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx"


@unittest.skipUnless(SCRIPT.exists(), "V3 workbook build script not present in this checkout")
class WorkbookScriptPortabilityTest(unittest.TestCase):
    def test_no_hardcoded_tmp_paths(self):
        text = SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn("/tmp/", text, "build_v3_workbook.py must not hardcode a scratch /tmp path")


@unittest.skipUnless(
    SCRIPT.exists() and COMMITTED_WORKBOOK.exists(),
    "V3 workbook build script or committed workbook not present in this checkout",
)
class WorkbookRegenerationMatchesCommittedTest(unittest.TestCase):
    """Regenerating the workbook from repo-relative inputs must reproduce the
    committed authoritative workbook's cell content exactly, including the
    withdrawn-GT-20 correction and the full Case-13 breakout inventory."""

    @classmethod
    def setUpClass(cls):
        import tempfile

        cls.tmpdir = tempfile.mkdtemp(prefix="v3-workbook-repro-")
        dst = Path(cls.tmpdir) / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx"
        env = {"V3_WORKBOOK_DST": str(dst)}
        import os

        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=str(SCRIPT.parent),
            env={**os.environ, **env},
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            raise RuntimeError(f"build_v3_workbook.py failed: {result.stderr}")
        cls.fresh_path = dst

    def test_regenerated_workbook_matches_committed_sheet_content(self):
        from openpyxl import load_workbook

        wb_committed = load_workbook(str(COMMITTED_WORKBOOK), data_only=True)
        wb_fresh = load_workbook(str(self.fresh_path), data_only=True)
        self.assertEqual(wb_committed.sheetnames, wb_fresh.sheetnames)
        for name in wb_committed.sheetnames:
            rows_committed = list(wb_committed[name].iter_rows(values_only=True))
            rows_fresh = list(wb_fresh[name].iter_rows(values_only=True))
            self.assertEqual(
                rows_committed, rows_fresh,
                f"sheet {name!r} differs between the regenerated and committed workbook",
            )

    def test_regenerated_workbook_does_not_contain_fabricated_gt20_claim(self):
        from openpyxl import load_workbook

        wb_fresh = load_workbook(str(self.fresh_path), data_only=True)
        ws = wb_fresh["12_TREND_ATTRIBUTION"]
        for row in ws.iter_rows(values_only=True):
            if row and row[0] == "GT-20":
                self.assertNotIn(16.7, row, "fabricated GT-20 mean_90d_after=16.7 must not reappear")
                self.assertNotIn(20, row[4:], "fabricated GT-20 mean_90d_after=20 must not reappear")


if __name__ == "__main__":
    unittest.main()
