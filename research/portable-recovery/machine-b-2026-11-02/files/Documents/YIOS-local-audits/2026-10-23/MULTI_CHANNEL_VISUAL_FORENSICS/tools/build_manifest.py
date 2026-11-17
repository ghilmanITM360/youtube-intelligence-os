"""Write 08_VIDEO_SOURCE_AND_EVIDENCE_MANIFEST.json.

Usage: python3 -I build_manifest.py <run_dir> <yios_repo> <pilot_channel/video_id>...
Asserts each pilot's re-hashed source equals the inventory hash.
"""
import csv, datetime, hashlib, json, os, subprocess, sys

O, repo, pilots = sys.argv[1], sys.argv[2], sys.argv[3:]


def sh(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def first_line(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()[0]


git = lambda *a: subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True).stdout.strip()
cov = {r["video_id"]: r for r in csv.DictReader(open(os.path.join(O, "03_VISUAL_ANALYSIS_COVERAGE.csv"), encoding="utf-8"))}
out = []
for cv in pilots:
    ch, vid = cv.split("/")
    d = os.path.join(O, "evidence", ch, vid)
    files = [{"path": os.path.relpath(os.path.join(r, f), O), "sha256": sh(os.path.join(r, f)),
              "bytes": os.path.getsize(os.path.join(r, f))}
             for r, _, fs in sorted(os.walk(d)) for f in sorted(fs)]
    pr = json.load(open(os.path.join(d, "ffprobe.json")))
    v = next(s for s in pr["streams"] if s["codec_type"] == "video")
    c = cov[vid]
    rehash = open(os.path.join(d, "source.sha256")).read().strip()
    assert rehash == c["source_sha256"], vid
    out.append({
        "channel_folder": c["source_path"].split("/")[0], "video_id": vid, "title": c["title"],
        "source_path": "/Users/ghilmanislam360/Downloads/all channels videos data /" + c["source_path"],
        "source_sha256": rehash, "duration_s": pr["format"]["duration"],
        "frames_decoded": int(open(os.path.join(d, "frame_count.txt")).read()),
        "fps": v["avg_frame_rate"], "resolution": f"{v['width']}x{v['height']}", "vcodec": v["codec_name"],
        "audio_present": any(s["codec_type"] == "audio" for s in pr["streams"]),
        "cut_candidates_ge_0.30": sum(1 for _ in open(os.path.join(d, "cuts_0.30.tsv"))),
        "visual_status": c["visual_status"], "derived_files": files,
    })

m = {
    "run": "2026-10-23 MULTI_CHANNEL_VISUAL_FORENSICS (Machine B)",
    "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "host": {"user": os.environ.get("USER"), "hostname": os.uname().nodename},
    "yios_repo": {"path": repo, "branch": git("branch", "--show-current"), "head": git("rev-parse", "HEAD"),
                  "tracked_changes": git("status", "--porcelain") or "none"},
    "source_root": "/Users/ghilmanislam360/Downloads/all channels videos data /  (trailing space in folder name)",
    "tools": {"ffmpeg": first_line(["ffmpeg", "-version"]), "ffprobe": first_line(["ffprobe", "-version"]),
              "python": first_line(["python3", "--version"]),
              "scripts": {f: sh(os.path.join(O, "tools", f)) for f in sorted(os.listdir(os.path.join(O, "tools")))}},
    "git_evidence_read": {
        "cf_editing_forensics": "origin/research/casually-finance-editing-forensics@090f84b3292a3b6c6e94653a6ef1867726e4ebdd",
        "cf_codex": "origin/codex/casually-finance-forensic-research@043b85bf",
        "ce_codex": "origin/codex/casual-economics-forensic-research@fce81670",
        "what_if_manifest": "main:data/manifests/what-if-forensic-source-v1.json"},
    "work_inputs": {f: sh(os.path.join(O, "work", f)) for f in sorted(os.listdir(os.path.join(O, "work")))},
    "deliverables": {f: sh(os.path.join(O, f)) for f in sorted(os.listdir(O))
                     if f[:2].isdigit() and not f.startswith("08_")},
    "pilots": out,
    "frame_timestamp_rule": "sheet_1fps_NN.jpg tile k (row-major, 0-based) = (NN-1)*30 + k s; "
                            "dense/w_<start>-<end>_<f>fps.jpg tile k = start + k/f s",
    "limits": ["no human listening", "ASR is uncertified whisper.cpp small.en, spot-check alignment only",
               "1 fps sampling may miss sub-second overlays outside dense windows",
               "ffmpeg build has no drawtext; timestamps positional, not burned in"],
}
json.dump(m, open(os.path.join(O, "08_VIDEO_SOURCE_AND_EVIDENCE_MANIFEST.json"), "w"), indent=1, ensure_ascii=False)
print("ok", sum(len(p["derived_files"]) for p in out), "derived files;", len(m["deliverables"]), "deliverables hashed")
