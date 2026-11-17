"""Build 02_SEVEN_CHANNEL_SOURCE_INVENTORY.csv and 03_VISUAL_ANALYSIS_COVERAGE.csv from verified evidence.

Usage: python3 -I build_ledger.py <run_dir> <ALL_VIDEOS.csv>
Inputs (all in <run_dir>/work, copied from Git objects / Machine B files this run):
  raw_inventory.csv                         this run's hash+ffprobe pass over 454 MP4s
  machineA_CF_SOURCE_MEDIA_INVENTORY@090f84b3.csv, machineA_CF_STATUS@090f84b3.json
  CE_SOURCE_VERIFICATION@fce81670.json, what-if-forensic-source-v1@main.json
Statuses follow the task vocabulary; nothing is marked complete without a named receipt.
"""
import csv, json, os, sys
from collections import defaultdict

run = sys.argv[1]
W = os.path.join(run, "work")
inv = list(csv.DictReader(open(os.path.join(W, "raw_inventory.csv"), encoding="utf-8")))
cfa = {r["SHA256"]: r for r in csv.DictReader(open(os.path.join(W, "machineA_CF_SOURCE_MEDIA_INVENTORY@090f84b3.csv"), encoding="utf-8"))}
st = json.load(open(os.path.join(W, "machineA_CF_STATUS@090f84b3.json")))
ce = {s["actual_sha256"]: s["video_id"] for s in json.load(open(os.path.join(W, "CE_SOURCE_VERIFICATION@fce81670.json")))["sources"]}
wi = {s["canonical_youtube_video_id"]: s for s in json.load(open(os.path.join(W, "what-if-forensic-source-v1@main.json")))["sources"] if s["canonical_youtube_video_id"]}

CF_DONE = {v["video_id"]: v for v in st["videos_complete"]}
CF_LF = set(st["queue_prior_partial_16"])
CF_GIT = "origin/research/casually-finance-editing-forensics@090f84b3"
CODEX_CF = "origin/codex/casually-finance-forensic-research@043b85bf"
CODEX_CE = "origin/codex/casual-economics-forensic-research@fce81670"
WI_ROOT = "/Users/ghilmanislam360/GhilmanProjects/video data of what if/video_forensics_output"
PILOTS = {"DZG89lilGr0": "PrimateEconomics", "95UrFFVrwJU": "MonkeBiznis",
          "HERcUJ6fIlw": "PrimitiveEducation", "uPQcyookL0Y": "BarelyEvolved"}

# casual_economics IDs come only from hash match against Codex SOURCE_VERIFICATION; then re-run registry lookup
csv.field_size_limit(10**9)
reg = {r["video_id"]: r for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"))}
for r in inv:
    if r["channel_folder"] == "casual_economics" and r["sha256"] in ce:
        r["video_id"], r["id_method"] = ce[r["sha256"]], "SHA256_MATCH_CODEX_CE_VERIFICATION"
        m = reg.get(r["video_id"], {})
        r["in_yios_all_videos"] = str(bool(m))
        r["registry_channel"], r["registry_title"] = m.get("channel_name", ""), m.get("title", "")

by_id = defaultdict(list)
for r in inv:
    by_id[r["video_id"] or "UNMAPPED:" + r["sha256"]].append(r)


def pick(rows):
    # prefer the copy Machine A analysed (exact hash), else first by filename
    return next((r for r in rows if r["sha256"] in cfa), sorted(rows, key=lambda r: r["filename"])[0])


inv_rows, cov_rows = [], []
for vid, rows in sorted(by_id.items(), key=lambda kv: (kv[1][0]["channel_folder"], kv[0])):
    c = pick(rows)
    ch = c["channel_folder"]
    dur = float(c["duration_s"] or 0)
    fmt = "SHORT" if (c["orientation"] == "portrait" and dur <= 181) else "LONG_FORM"
    inv_rows.append({
        "channel_folder": ch, "video_id": vid, "id_method": c["id_method"],
        "registry_channel": c["registry_channel"], "registry_title": c["registry_title"],
        "in_yios_registry": c["in_yios_all_videos"], "canonical_filename": c["filename"],
        "canonical_sha256": c["sha256"], "size_bytes": c["size_bytes"], "duration_s": c["duration_s"],
        "width": c["width"], "height": c["height"], "fps": c["fps"], "vcodec": c["vcodec"],
        "acodec": c["acodec"], "has_audio": c["has_audio"], "orientation": c["orientation"],
        "format_class": fmt, "decode_status": c["decode_status"], "local_copies": len(rows),
        "other_copies": " | ".join(f"{r['filename']} ({r['sha256'][:12]})" for r in rows if r is not c),
    })
    status, audio, receipt, remaining, depth = "SOURCE_AVAILABLE", "NOT_STARTED", "", "full visual pass", ""
    if ch == "CasuallyFinance" and vid in CF_DONE:
        status, audio = "VISUAL_ANALYSIS_COMPLETE", "AUDIO_REVIEW_PENDING"
        depth = "Machine A depth " + CF_DONE[vid]["depth"] + " (per-event, frame-accurate Shorts procedure)"
        receipt = f"{CF_GIT}:research/casually-finance-editing-forensics/{CF_DONE[vid]['qa']}"
        remaining = "human listening / full AV sign-off; second reviewer; frame dumps exist only on Machine A"
    elif ch == "CasuallyFinance" and vid in CF_LF:
        status, audio = "STRUCTURAL_ANALYSIS_COMPLETE", "AUDIO_REVIEW_PENDING"
        depth = "Codex PASS_STRUCTURAL (sampled visual reconstruction)"
        receipt = f"{CODEX_CF}:data/extracted/forensic-analysis/casually-finance/2026-10-12/02_VIDEO_FORENSICS/{vid}/QA.json"
        remaining = "Machine A long-form procedure LF-0..LF-6 (written, not started); AV sign-off"
    elif ch == "CasuallyFinance" and vid == "turJ6VMfUjI":
        status, depth = "SAMPLED_FRAMES_ONLY", "Codex evidence/ folder only, no QA.json"
        receipt = f"{CODEX_CF}:data/extracted/forensic-analysis/casually-finance/2026-10-12/02_VIDEO_FORENSICS/turJ6VMfUjI/evidence"
        remaining = "was SOURCE_MISSING on Machine A; source now present on Machine B -> full visual pass"
    elif ch == "casual_economics" and c["id_method"].startswith("SHA256_MATCH"):
        status, audio = "STRUCTURAL_ANALYSIS_COMPLETE", "AUDIO_REVIEW_PENDING"
        depth = "Codex structural package PASS; shot census NOT_CERTIFIED; motion PARTIAL"
        receipt = f"{CODEX_CE}:research/casual-economics-deep-dive-2026-10/06_VALIDATION_AND_HANDOFF/QA_LIMITATIONS_REGISTER.md"
        remaining = "certified shot census; independent visual QA; AV sign-off 0/11"
    elif ch == "xkcd Channel" and vid in wi:
        status = "HISTORICAL_UNVERIFIED"
        depth = f"What If brain v1.0.0 claims COMPLETE_VALIDATED ({wi[vid]['source_video_id']}, {wi[vid]['identity_class']})"
        receipt = f"{WI_ROOT}/<{wi[vid]['forensic_slug']}> ; data/manifests/what-if-forensic-source-v1.json@main"
        remaining = "prior source copy hash differs from Machine B copy; audit completion contract before reuse"
    elif vid in PILOTS:
        status, audio = "VISUAL_ANALYSIS_PARTIAL", "AUDIO_REVIEW_PENDING"
        depth = "this run: full-frame scene-score pass + 1 fps full-timeline sheets + dense windows"
        receipt = f"evidence/{PILOTS[vid]}/{vid}/ ; 06_PILOT_VISUAL_ANALYSIS_REPORT.md"
        remaining = "frame-accurate event timing (sub-second overlays between 1 fps samples not certified); full script alignment beyond ASR spot-checks (ASR uncertified); listening"
    if vid.startswith("UNMAPPED:"):
        status, remaining = "IDENTITY_UNVERIFIED", "map Video ID"
    cov_rows.append({
        "channel_folder": ch, "video_id": vid, "title": c["registry_title"] or c["filename"],
        "source_path": os.path.join(ch, c["filename"]), "source_sha256": c["sha256"],
        "duration_s": c["duration_s"], "format_class": fmt, "visual_status": status,
        "audio_status": audio, "analysis_depth": depth, "evidence_receipt": receipt,
        "remaining_work": remaining,
    })

for name, rows in (("02_SEVEN_CHANNEL_SOURCE_INVENTORY.csv", inv_rows), ("03_VISUAL_ANALYSIS_COVERAGE.csv", cov_rows)):
    with open(os.path.join(run, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

# self-checks
ids = [r["video_id"] for r in inv_rows]
assert len(ids) == len(set(ids)), "duplicate Video IDs in inventory"
assert sum(r["local_copies"] for r in inv_rows) == len(inv) == 454
assert all(r["evidence_receipt"] for r in cov_rows if r["visual_status"] not in ("SOURCE_AVAILABLE", "IDENTITY_UNVERIFIED"))
summ = defaultdict(lambda: defaultdict(int))
for r in cov_rows:
    summ[r["channel_folder"]][r["visual_status"]] += 1
    summ[r["channel_folder"]]["_unique"] += 1
for ch, d in summ.items():
    print(ch, dict(d))
