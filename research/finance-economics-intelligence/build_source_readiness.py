#!/usr/bin/env python3
"""Read-only source-readiness queue for BLOCKED_MISSING_SOURCE_TRANSCRIPT rows.

Inputs: FINANCE_CONTINUATION_QUEUE.csv, TRANSCRIPT_COVERAGE.csv, registered archive members
named in Evidence_locator, and path listings of origin/* branches (no blob reads, no writes
outside this directory). Nothing is registered: a branch path is only a recovery candidate until
its blob is fetched, mapped to the video ID and fingerprinted by the authorised registry writer.
"""
import csv, json, re, subprocess, zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WT = ROOT.parents[1]
TX = re.compile(r"(transcript|caption|subtitle|\.vtt$|\.srt$)", re.I)


def rows(p):
    with open(p, encoding="utf-8-sig", newline="") as h:
        return list(csv.DictReader(h))


def main():
    q = rows(ROOT / "FINANCE_CONTINUATION_QUEUE.csv")
    blk = {r["video_id"]: r for r in q if r["eligibility"] == "BLOCKED_MISSING_SOURCE_TRANSCRIPT"}
    tc = {r["Video_ID"]: r for r in rows(ROOT / "TRANSCRIPT_COVERAGE.csv")}
    cand = {}
    branches = subprocess.check_output(["git", "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin"], cwd=WT, text=True).split()
    for b in branches:
        p = subprocess.run(["git", "ls-tree", "-r", "--name-only", b], cwd=WT, capture_output=True, text=True)
        for f in p.stdout.splitlines() if p.returncode == 0 else []:
            if TX.search(f):
                for part in f.split("/"):
                    if part in blk:
                        cand.setdefault(part, []).append(f"{b}:{f}")
    out = []
    for vid, r in blk.items():
        t = tc.get(vid, {})
        loc, note = t.get("Evidence_locator", ""), ""
        if loc and "::" in loc:
            a, _, mem = loc.partition("::")
            try:
                body = zipfile.ZipFile(WT / a).read(mem).decode("utf-8", "replace")
                note = next((l.split(":", 1)[1].strip() for l in body.splitlines() if l.startswith("Caption type")), "")
            except (KeyError, FileNotFoundError, zipfile.BadZipFile):
                note = "REGISTERED_MEMBER_UNREADABLE"
        c = sorted(cand.get(vid, []))
        if "members-only" in note.lower():
            cls, need = "MEMBERS_ONLY_CAPTIONS_UNAVAILABLE", "Owner-authorised channel membership access or creator-supplied transcript; otherwise permanently blocked"
        elif c:
            cls, need = "CANDIDATE_TRANSCRIPT_ON_ORIGIN_BRANCH", "Fetch blob read-only, map to video ID, fingerprint, then register through the authorised registry writer; not yet registered"
        elif note:
            cls, need = "REGISTERED_ARCHIVE_HAS_NO_CAPTIONS", "Authorised external caption/ASR acquisition, then register"
        else:
            cls, need = "NO_LOCAL_SOURCE_FOUND", "Authorised external caption/ASR acquisition, then register"
        out.append({"video_id": vid, "population": r["population"], "population_layer": r["population_layer"], "channel_name": r["channel_name"],
                    "readiness_class": cls, "coverage_status": t.get("Status", r["transcript_completeness"]), "registered_locator": loc,
                    "registered_caption_note": note, "candidate_count": len(c), "candidate_locators": " | ".join(c[:4]), "recovery_requirement": need})
    out.sort(key=lambda r: (r["population"] != "ORIGINAL", r["readiness_class"], r["channel_name"], r["video_id"]))
    with (ROOT / "FINANCE_SOURCE_READINESS_QUEUE.csv").open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    s = {"blocked_rows": len(out), "unique_video_ids": len({r["video_id"] for r in out}),
         "by_class": {f"{p}:{k}": n for (p, k), n in sorted(Counter((r["population"], r["readiness_class"]) for r in out).items())},
         "candidate_by_channel": dict(Counter(r["channel_name"] for r in out if r["candidate_count"])),
         "registered_transcripts_added": 0, "method": "read-only; branch path names only, no blob content trusted yet"}
    print(json.dumps(s, indent=1))


if __name__ == "__main__":
    main()
