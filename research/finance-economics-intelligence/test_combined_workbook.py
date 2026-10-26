import json
import subprocess
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BOOK = ROOT / "FINANCE_1612_COMBINED_INTELLIGENCE.xlsx"
class CombinedWorkbookContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(subprocess.check_output(["python3", ROOT / "build_combined_workbook_data.py"], text=True))

    def test_population_and_completion(self):
        rows = self.payload["all_videos"]
        self.assertEqual(1612, len(rows))
        self.assertEqual(1612, len({r["video_id"] for r in rows}))
        self.assertEqual(455, sum(r["audit_status"] == "DEEP_AUDIT_COMPLETE" for r in rows))
        self.assertEqual(
            "DEEP_AUDIT_COMPLETE",
            next(r["audit_status"] for r in rows if r["video_id"] == "Rd40d0XZLpQ"),
        )
        self.assertEqual(
            "DEEP_AUDIT_COMPLETE",
            next(r["audit_status"] for r in rows if r["video_id"] == "RgaTGzeFcPQ"),
        )
        target = next(r for r in rows if r["video_id"] == "RmJKnJkUgxA")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_RmJKnJkUgxA.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "S0xwBH_fAn0")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_S0xwBH_fAn0.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "SJLyXAGbBLk")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_SJLyXAGbBLk.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "SLFcypMv6I0")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_SLFcypMv6I0.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "SU-3ZcgmCJ4")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_SU-3ZcgmCJ4.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "S_8SLGjLrBM")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_S_8SLGjLrBM.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "Sb0HUHNxF2I")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_Sb0HUHNxF2I.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "SlyosXgW__4")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_SlyosXgW__4.jpg",
            target["local_media_status"],
        )
        target = next(r for r in rows if r["video_id"] == "SsHQ-TtXhRQ")
        self.assertEqual("DEEP_AUDIT_COMPLETE", target["audit_status"])
        self.assertEqual("AVAILABLE", target["thumbnail_status"])
        self.assertEqual(
            "research/finance-economics-intelligence/audit-batches/NICK_SsHQ-TtXhRQ.jpg",
            target["local_media_status"],
        )
        self.assertFalse(any(r["audit_status"] == "DEEP_AUDIT_COMPLETE" and r["population_layer"] != "FROZEN_ORIGINAL_966" for r in rows))
        self.assertFalse(any(r["audit_status"] == "DEEP_AUDIT_COMPLETE" and r["blocker"] for r in rows))

    def test_layers_channels_and_detail(self):
        self.assertEqual({"FROZEN_ORIGINAL_966": 966, "EXPANSION_12_CHANNEL_197": 197, "EXPANSION_MONKEY_63": 63, "REPOSITORY_RECONCILIATION_2026_10_21": 386}, self.payload["summary"]["layers"])
        self.assertEqual(42, len(self.payload["channels"]))
        self.assertEqual(966, len(self.payload["details"]))
        self.assertTrue(all(all(k in r for k in ("title_research", "thumbnail_research", "script_research", "topic_research", "performance_research", "virality_research")) for r in self.payload["details"]))
        authoritative = [json.loads(line) for line in (ROOT / "VIDEO_AUDIT_966.jsonl").read_text().splitlines()]
        projected = {r["video_id"]: r for r in self.payload["details"]}
        self.assertEqual({r["Video_ID"] for r in authoritative}, set(projected))
        for source in authoritative:
            detail = projected[source["Video_ID"]]
            self.assertEqual(source["statuses"], detail["statuses"])
            for section in ("title", "thumbnail", "script", "topic", "performance", "virality", "event", "private_metrics"):
                self.assertEqual(source[section], detail[f"{section}_research"] if section != "private_metrics" else detail[section])

    def test_single_current_excel_deliverable(self):
        self.assertEqual([BOOK], sorted(ROOT.glob("FINANCE_*_INTELLIGENCE.xlsx")))
        self.assertEqual([ROOT / "build_workbook_1612.mjs"], sorted(ROOT.glob("build_workbook_*.mjs")))

    def test_exported_workbook_shape(self):
        self.assertTrue(BOOK.exists())
        with zipfile.ZipFile(BOOK) as z:
            workbook_xml = z.read("xl/workbook.xml").decode()
            for name in ("Combined Dashboard", "All Finance Videos", "Channel Directory", "Detailed Research"):
                self.assertIn(f'name="{name}"', workbook_xml)
            table_xml = "\n".join(z.read(name).decode() for name in z.namelist()
                                  if name.startswith("xl/tables/table") and name.endswith(".xml"))
            self.assertIn('ref="A4:AG1616"', table_xml)
            self.assertIn('ref="A4:G46"', table_xml)
            self.assertIn('ref="A4:X970"', table_xml)


if __name__ == "__main__":
    unittest.main()
