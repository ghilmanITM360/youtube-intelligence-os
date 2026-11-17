#!/usr/bin/env python3
"""xkcd clone-readiness P1: per-video coverage table + library verification (read-only on sources/ledgers).
usage: python3 -I coverage_audit.py   -> writes <lib>/_channel/coverage_by_video.csv and prints verification JSON.
Inputs: library_manifest.csv, <vid>/states_index.csv, videos/<vid>/{source_manifest,quality_gate}.json,
census/census.csv, campaign/short_long_text_reuse_population.csv. Nothing is upgraded; statuses copied verbatim."""
import csv, glob, hashlib, json, os, random, collections
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); LIB = f"{H}/asset_library"
def sha(p):
    h = hashlib.sha256(); f = open(p, "rb")
    for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
cen = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/census/census.csv"))}
reuse = {r["short"]: r for r in csv.DictReader(open(f"{H}/campaign/short_long_text_reuse_population.csv"))}
man = list(csv.DictReader(open(f"{LIB}/library_manifest.csv")))
lib_ids = {m["video_id"] for m in man}
rows, allst = [], []
for m in man:
    v = m["video_id"]; st = list(csv.DictReader(open(f"{LIB}/{v}/states_index.csv"))); allst += st
    sm = json.load(open(f"{H}/videos/{v}/source_manifest.json"))["source"]
    g = json.load(open(f"{H}/videos/{v}/quality_gate.json"))
    un = g.get("review_scope", {}).get("unreviewed_or_unverified_intervals", []) or []
    gates = g.get("gates", {})
    c = cen.get(v, {}); fmt = c.get("format_class", "UNKNOWN"); ru = reuse.get(v)
    parent = "UNKNOWN_NO_CAPTION_TEXT" if ru and ru["text_source"] == "none" else ru["best_long"] if ru and ru["relation"].startswith("TEXT_EXCERPT") else ("STANDALONE" if ru else ("" if fmt == "LONG_FORM" else "NOT_IN_REUSE_TABLE"))
    rows.append(dict(video_id=v, format=fmt, resolution=sm.get("resolution"), fps=sm.get("frame_rate_avg"), duration_s=f"{float(sm['duration_seconds']):.1f}",
        decoded_frames=sm.get("decoded_frames"), publish=c.get("publish_datetime", "")[:10], ledger_states=m["states"], frames_saved=m["frames_saved"],
        pts_check_ok=m["pts_check_ok"], status=g.get("final_video_status"), ct_scan_complete=g.get("ct_scan_complete"), full_av_signoff=g.get("full_av_signoff"),
        unviewed_intervals=len(un), unviewed_frames=sum(int(x.get("unviewed_frames", 0)) for x in un),
        gate_fails_or_partials=";".join(f"{k}={s}" for k, s in gates.items() if s != "PASS"),
        parent_long=parent, parent_reuse_coverage=ru["coverage_by_6word_blocks"] if ru else "", parent_in_library=(parent in lib_ids) if parent not in ("", "STANDALONE", "NOT_IN_REUSE_TABLE", "UNKNOWN_NO_CAPTION_TEXT") else "",
        reviewer=g.get("reviewer", "")))
with open(f"{LIB}/_channel/coverage_by_video.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
random.seed(20261108); pick = random.sample(allst, 3)
chk = [dict(file=f"{p['video_id']}/{p['file']}", recorded=p["image_sha256"][:16], actual=sha(f"{LIB}/{p['video_id']}/{p['file']}")[:16]) for p in pick]
for c in chk: c["match"] = c["recorded"] == c["actual"]
jpgs = sum(len(glob.glob(f"{LIB}/{m['video_id']}/states/*.jpg")) for m in man)
print(json.dumps(dict(videos=len(man), states_rows=len(allst), state_jpgs_on_disk=jpgs, manifest_frames=sum(int(m["frames_saved"]) for m in man),
    pts_check=collections.Counter(s["pts_check"] for s in allst), unique_frames=len(os.listdir(f"{LIB}/_channel/unique_frames")),
    formats=collections.Counter(r["format"] for r in rows), statuses=collections.Counter(r["status"] for r in rows),
    ct_true=sum(1 for r in rows if r["ct_scan_complete"]), av_true=sum(1 for r in rows if r["full_av_signoff"]),
    sha_spotcheck=chk), indent=1, default=str))
