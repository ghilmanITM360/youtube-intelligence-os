import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("analytics", Path(__file__).with_name("build_analytics.py"))
m = importlib.util.module_from_spec(spec)

class ScoringTests(unittest.TestCase):
    def test_boundaries(self):
        spec.loader.exec_module(m)
        for ratio, expected in [(4,"BREAKOUT"),(2,"TOP_PERFORMER"),(1.25,"ABOVE_BASELINE"),(1,"TYPICAL"),(.6,"BELOW_BASELINE"),(.49,"UNDERPERFORMER")]:
            self.assertEqual(m.tier(ratio), expected)

    def test_peer_pool_keeps_format_and_excludes_launch(self):
        spec.loader.exec_module(m)
        rows = [{"video_id":str(i),"format_class":"LONG_FORM","age":100+i,"vpd":100} for i in range(9)]
        rows += [{"video_id":"short","format_class":"SHORT","age":100,"vpd":900000}, {"video_id":"new","format_class":"LONG_FORM","age":2,"vpd":900000}]
        peers, mode = m.peers_for(rows[0], rows)
        self.assertEqual(len(peers),8)
        self.assertEqual(mode,"AGE_CALIPER")
        self.assertNotIn("0",[p["video_id"] for p in peers])
        self.assertNotIn("short",[p["video_id"] for p in peers])
        self.assertNotIn("new",[p["video_id"] for p in peers])

    def test_duplicate_conflict_rejected(self):
        spec.loader.exec_module(m)
        with self.assertRaises(ValueError):
            m.deduplicate([{"video_id":"x","views":"1"},{"video_id":"x","views":"2"}])
        self.assertEqual(len(m.deduplicate([{"video_id":"x"},{"video_id":"x"}])),1)

if __name__ == "__main__":
    unittest.main()
