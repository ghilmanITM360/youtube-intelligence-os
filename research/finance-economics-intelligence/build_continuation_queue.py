#!/usr/bin/env python3
"""Recompute the Finance 1,612 continuation queue from accepted canonical records.

  build                  write FINANCE_CONTINUATION_QUEUE.csv and _SUMMARY.json
  lock acquire|release|status   single-writer lock (mkdir is atomic) in this worktree's git dir

Nothing here is taken from conversation memory: ledger, universe, master, transcript
coverage, read-only registry and git history are the only inputs.
"""
from __future__ import annotations

import csv, json, os, sqlite3, subprocess, sys, time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WT = ROOT.parents[1]
UNIVERSE = ROOT / "reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv"
DB = WT / "data/catalog/youtube_channel_registry.db"
DIMS = ("TOPIC", "TITLE", "THUMBNAIL", "SCRIPT", "PERFORMANCE", "VIRALITY")
PRESERVED_PARTIAL = {"TFtBWn9CWOU"}
# Established policy: finish the Nick Invests original queue first, then other original channels.
CHANNEL_PRIORITY = ("Nick Invests",)
LOCK = Path(subprocess.check_output(["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True).strip()) / "finance-machine-a-writer.lock"


def rows(p):
    with open(p, encoding="utf-8-sig", newline="") as h:
        return list(csv.DictReader(h))


def packet_commits():
    """First commit that added each audit-batches/*.json packet."""
    out = subprocess.check_output(["git", "log", "--reverse", "--diff-filter=A", "--name-only", "--format=@%H", "--", "audit-batches/"], cwd=ROOT, text=True)
    seen, sha = {}, ""
    for line in out.splitlines():
        if line.startswith("@"):
            sha = line[1:]
        elif line.endswith(".json"):
            seen.setdefault(Path(line).stem, sha)
    return seen


def build():
    ledger = {r["Video_ID"]: r for r in map(json.loads, (ROOT / "VIDEO_AUDIT_966.jsonl").read_text().splitlines())}
    master = {r["Video_ID"]: r for r in rows(ROOT / "VIDEO_MASTER.csv")}
    tcov = {r["Video_ID"]: r for r in rows(ROOT / "TRANSCRIPT_COVERAGE.csv")}
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    tlen = dict(con.execute("select youtube_video_id, length(transcript_text) from transcripts"))
    commits = packet_commits()
    out = []
    for u in rows(UNIVERSE):
        vid, layer = u["video_id"], u["population_layer"]
        original = layer == "FROZEN_ORIGINAL_966"
        a, m, t = ledger.get(vid), master.get(vid, {}), tcov.get(vid, {})
        st = {d: (a["statuses"][f"{d}_REVIEW"] if a else "NOT_STARTED") for d in DIMS}
        done = all(s.startswith("COMPLETE") for s in st.values())
        has_text = (t.get("Status") == "TEXT_AVAILABLE") if original else (tlen.get(vid) or 0) > 500
        if done:
            elig = "ACCEPTED"
        elif vid in PRESERVED_PARTIAL or "IN_PROGRESS" in st.values():
            elig = "DEFERRED_PRESERVED_PARTIAL"
        elif not has_text:
            elig = "BLOCKED_MISSING_SOURCE_TRANSCRIPT"
        elif original and m.get("Performance_tier") == "INSUFFICIENT_DATA":
            elig = "DEFERRED_INSUFFICIENT_PEER_BASELINE"
        else:
            elig = "ELIGIBLE"
        batch = a["batch_id"] if a and done else ""
        out.append({
            "video_id": vid, "population": "ORIGINAL" if original else "EXPANSION", "population_layer": layer,
            "channel_id": u["channel_id"], "channel_name": u["channel_name"], "accepted_batch_id": batch,
            "source_fingerprint": t.get("Text_SHA256", "") if original else "",
            "transcript_available": "YES" if has_text else "NO",
            "transcript_completeness": t.get("Status", u["transcript_status"]) if original else u["transcript_status"],
            "thumbnail_status": (a["statuses"]["THUMBNAIL_REVIEW"] if a else u["thumbnail_status"]),
            **{f"{d.lower()}_status": st[d] for d in DIMS},
            "views": m.get("Views", ""), "age_days": m.get("Age_days", ""), "metric_snapshot_date": m.get("Metric_snapshot_date", ""),
            "performance_tier": m.get("Performance_tier", ""), "lifetime_rate_ratio": m.get("Lifetime_rate_ratio", ""),
            "prior_audit_ref": a["batch_id"] if a else "",
            "eligibility": elig,
            "accepted_packet": f"audit-batches/{batch}.json" if batch and (ROOT / f"audit-batches/{batch}.json").exists() else "",
            "accepted_commit": commits.get(batch, "PRE_HISTORY_OR_LEGACY") if batch else "",
            "next_atomic_operation": "",
        })
    # Order: originals before expansion; priority channels first; then channel, video id.
    rank = lambda r: (r["population"] != "ORIGINAL", r["channel_name"] not in CHANNEL_PRIORITY, r["channel_name"], r["video_id"])
    out.sort(key=rank)
    nicks = [int(k.split("_")[1]) for k in commits if k.startswith("NICK_") and k.split("_")[1].isdigit()]
    n = max(nicks, default=0)
    for r in out:
        if r["eligibility"] == "ELIGIBLE":
            if r["channel_name"] == "Nick Invests":
                n += 1
                r["next_atomic_operation"] = f"AUDIT_SIX_DIMENSIONS_AS_NICK_{n}"
            else:
                r["next_atomic_operation"] = "AUDIT_SIX_DIMENSIONS_ASSIGN_CHANNEL_BATCH_ID_AT_START"
        elif r["eligibility"] == "BLOCKED_MISSING_SOURCE_TRANSCRIPT":
            r["next_atomic_operation"] = "ACQUIRE_AND_REGISTER_TRANSCRIPT_THEN_REQUEUE"
        elif r["eligibility"].startswith("DEFERRED"):
            r["next_atomic_operation"] = "HOLD_UNDER_DEFERRAL_RULE"
    with (ROOT / "FINANCE_CONTINUATION_QUEUE.csv").open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)
    c = Counter((r["population"], r["eligibility"]) for r in out)
    head = next((r for r in out if r["eligibility"] == "ELIGIBLE"), None)
    summary = {
        "derived_from": ["VIDEO_AUDIT_966.jsonl", "VIDEO_MASTER.csv", "TRANSCRIPT_COVERAGE.csv", str(UNIVERSE.relative_to(ROOT)), "registry transcripts (read-only)", "git history of audit-batches/"],
        "counts": {f"{p}:{e}": n for (p, e), n in sorted(c.items())},
        "original_accepted": c["ORIGINAL", "ACCEPTED"], "original_remaining": 966 - c["ORIGINAL", "ACCEPTED"],
        "expansion_accepted": c["EXPANSION", "ACCEPTED"], "expansion_remaining": 646 - c["EXPANSION", "ACCEPTED"],
        "overall_accepted": c["ORIGINAL", "ACCEPTED"] + c["EXPANSION", "ACCEPTED"],
        "eligible_now": sum(v for (p, e), v in c.items() if e == "ELIGIBLE"),
        "next": {k: head[k] for k in ("video_id", "channel_name", "next_atomic_operation")} if head else None,
    }
    (ROOT / "FINANCE_CONTINUATION_QUEUE_SUMMARY.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(json.dumps(summary, indent=1))


def lock(action, owner=""):
    if action == "acquire":
        try:
            LOCK.mkdir()
        except FileExistsError:
            sys.exit(f"LOCKED {(LOCK / 'owner').read_text() if (LOCK / 'owner').exists() else '?'}")
        (LOCK / "owner").write_text(f"{owner or 'unnamed'} pid={os.getppid()} at={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
        print("ACQUIRED", LOCK)
    elif action == "release":
        (LOCK / "owner").unlink(missing_ok=True); LOCK.rmdir(); print("RELEASED")
    else:
        print("HELD " + (LOCK / "owner").read_text() if LOCK.exists() else "FREE")


if __name__ == "__main__":
    if sys.argv[1:2] == ["lock"]:
        lock(sys.argv[2], " ".join(sys.argv[3:]))
    else:
        build()
