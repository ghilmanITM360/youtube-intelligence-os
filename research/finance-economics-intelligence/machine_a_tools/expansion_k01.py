#!/usr/bin/env python3
"""Freeze the Casually Finance public-view snapshot and apply the unchanged original K01 rule
(build_baseline.compare) to the 30 verified expansion transcript candidates.

Input is a committed git object, never conversation memory. Writes
EXPANSION_K01_CASUALLY_FINANCE.json (frozen inputs + provenance) and .csv (one row per candidate).
A K01 tier is performance evidence only; it does not make a candidate eligible or accepted.
"""
import csv, hashlib, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from build_baseline import compare  # noqa: E402

SOURCE = "fb1e56d03e5ad53086c74247cd2972b262d09b78:research/casually-finance-success-playbook/VIDEO_PERFORMANCE.csv"
CHANNEL_ID = "UCrNfRFWnLC3tCy1TnyhVQ7g"
OUT = ROOT / "EXPANSION_K01_CASUALLY_FINANCE"


def main():
    raw = subprocess.check_output(["git", "show", SOURCE], cwd=ROOT)
    videos = [{"Video_ID": r["Video_ID"], "Channel_ID": CHANNEL_ID,
               "Format": "SHORTS" if r["Format"] == "SHORT" else "LONG_FORM" if r["Format"] == "LONG_FORM" else "UNKNOWN",
               "Metric_snapshot_date": r["Snapshot_Date"][:10], "Age_days": float(r["Age_Days"]), "Views": int(r["Public_Views"])}
              for r in csv.DictReader(raw.decode("utf-8-sig").splitlines())]
    by = {v["Video_ID"]: v for v in videos}
    ids = sorted(v["video_id"] for v in json.loads((ROOT / "EXPANSION_TRANSCRIPT_CANDIDATES_VERIFIED.json").read_text())["videos"])
    OUT.with_suffix(".json").write_text(json.dumps({
        "source": SOURCE, "source_sha256": hashlib.sha256(raw).hexdigest(),
        "rule": "build_baseline.compare (original K01: same channel, format and snapshot date; age ratio 0.5-2; nearest 10; >=5 peers; STRONG >=2, WEAK <0.5)",
        "limitations": "Public lifetime views at one snapshot; not CTR, retention or impressions. Snapshot differs from the original 966 snapshot (2026-09-11).",
        "videos": videos}, indent=0) + "\n")
    with OUT.with_suffix(".csv").open("w", newline="", encoding="utf-8") as h:
        w = csv.writer(h)
        w.writerow(["video_id", "format", "age_days", "views", "snapshot_date", "tier", "peer_count", "ratio", "peer_ids", "basis"])
        for vid in ids:
            v = by[vid]
            w.writerow([vid, v["Format"], v["Age_days"], v["Views"], v["Metric_snapshot_date"], *compare(v, videos)])


if __name__ == "__main__":
    main()
