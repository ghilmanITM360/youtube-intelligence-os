"""Expansion-population contracts for the continuation queue and the expansion K01 baseline."""
import csv, json, unittest
from pathlib import Path

import build_continuation_queue as q
from build_baseline import compare

ROOT = Path(__file__).resolve().parent
CANDIDATES = json.loads((ROOT / "EXPANSION_TRANSCRIPT_CANDIDATES_VERIFIED.json").read_text())["videos"]
CAND_IDS = {v["video_id"] for v in CANDIDATES}
EXP_LEDGER = ROOT / "expansion-12-channel-2026-10-20/EXPANSION_AUDIT_LEDGER.jsonl"
K01 = ROOT / "EXPANSION_K01_CASUALLY_FINANCE.csv"


def queue():
    with open(ROOT / "FINANCE_CONTINUATION_QUEUE.csv", newline="", encoding="utf-8") as h:
        return list(csv.DictReader(h))


class ExpansionQueue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        q.build()
        cls.rows = queue()
        cls.by = {r["video_id"]: r for r in cls.rows}

    def test_population_is_966_plus_646(self):
        self.assertEqual(1612, len(self.by))
        pops = [r["population"] for r in self.rows]
        self.assertEqual((966, 646), (pops.count("ORIGINAL"), pops.count("EXPANSION")))

    def test_verified_candidates_are_recognized_but_not_eligible(self):
        self.assertEqual(30, len(CAND_IDS))
        for vid in CAND_IDS:
            r = self.by[vid]
            self.assertEqual("EXPANSION", r["population"])
            self.assertEqual("DEFERRED_TRANSCRIPT_VERIFIED_NOT_REGISTERED", r["eligibility"], vid)
        blocked = [r for r in self.rows if r["population"] == "EXPANSION" and r["eligibility"] == "BLOCKED_MISSING_SOURCE_TRANSCRIPT"]
        self.assertEqual(616, len(blocked))

    def test_expansion_ledger_statuses_are_read(self):
        ledger = [json.loads(l) for l in EXP_LEDGER.read_text().splitlines()]
        for a in ledger:
            r = self.by[a["video_id"]]
            for d in q.DIMS:
                self.assertEqual(a["statuses"][f"{d}_REVIEW"], r[f"{d.lower()}_status"], (a["video_id"], d))

    def test_ledgers_are_disjoint_and_accepted_counted_once(self):
        orig = {json.loads(l)["Video_ID"] for l in (ROOT / "VIDEO_AUDIT_966.jsonl").read_text().splitlines()}
        exp = {json.loads(l)["video_id"] for l in EXP_LEDGER.read_text().splitlines()}
        self.assertFalse(orig & exp)
        s = json.loads((ROOT / "FINANCE_CONTINUATION_QUEUE_SUMMARY.json").read_text())
        accepted = sum(r["eligibility"] == "ACCEPTED" for r in self.rows)
        self.assertEqual(accepted, s["overall_accepted"])
        self.assertEqual(s["original_accepted"] + s["expansion_accepted"], s["overall_accepted"])

    def test_original_tiers_unchanged(self):
        with open(ROOT / "VIDEO_MASTER.csv", newline="", encoding="utf-8-sig") as h:
            master = {r["Video_ID"]: r for r in csv.DictReader(h)}
        for r in self.rows:
            if r["population"] == "ORIGINAL":
                self.assertEqual(master[r["video_id"]]["Performance_tier"], r["performance_tier"])

    def test_regeneration_is_deterministic(self):
        before = (ROOT / "FINANCE_CONTINUATION_QUEUE.csv").read_bytes()
        q.build()
        self.assertEqual(before, (ROOT / "FINANCE_CONTINUATION_QUEUE.csv").read_bytes())


class ExpansionK01(unittest.TestCase):
    def setUp(self):
        with open(K01, newline="", encoding="utf-8") as h:
            self.rows = list(csv.DictReader(h))

    def test_one_row_per_candidate_with_stable_fingerprints(self):
        self.assertEqual(CAND_IDS, {r["video_id"] for r in self.rows})
        for v in CANDIDATES:
            shas = {c["text_sha256"] for c in v["candidates"] if c.get("kind") == "WORD_LEVEL_ASR"}
            self.assertEqual(1, len(shas), v["video_id"])

    def test_tiers_reproduce_original_k01_rule(self):
        snap = json.loads(K01.with_suffix(".json").read_text())
        vids = snap["videos"]
        by = {v["Video_ID"]: v for v in vids}
        for r in self.rows:
            tier, n, ratio, peers, basis = compare(by[r["video_id"]], vids)
            self.assertEqual((tier, str(n), str(ratio), peers, basis),
                             (r["tier"], r["peer_count"], r["ratio"], r["peer_ids"], r["basis"]), r["video_id"])
            if tier != "INSUFFICIENT_DATA":
                self.assertTrue(5 <= int(r["peer_count"]) <= 10)
                for p in peers.split("|"):  # same channel, format and snapshot only
                    self.assertEqual((by[p]["Format"], by[p]["Metric_snapshot_date"]),
                                     (by[r["video_id"]]["Format"], by[r["video_id"]]["Metric_snapshot_date"]))

    def test_insufficient_data_is_deferred_not_forced(self):
        insufficient = [r for r in self.rows if r["tier"] == "INSUFFICIENT_DATA"]
        self.assertTrue(all(r["ratio"] == "" for r in insufficient))


if __name__ == "__main__":
    unittest.main()
