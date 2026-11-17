#!/usr/bin/env python3
"""Targeted state-frame extraction for xkcd / Primitive Education / Barely Evolved asset libraries (local only).
usage: python3 -I extract_states.py <xkcd|pe|be> [video_id ...]
One decode pass per chunk of 40 representative frames; MP4 SHA-256 verified first; PTS cross-checked (showinfo).
Rep frame per state = start + min(3, frames-1) (same convention as the Casual Finance library). No source edits."""
import csv, glob, hashlib, json, os, re, subprocess, sys, tempfile
H = os.path.expanduser("~/YIOS-local-audits")

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def rate(s):
    m = re.search(r"(\d+)/(\d+)", str(s)); return int(m[1]) / int(m[2]) if m else 24.0

def t0_of(s):
    m = re.search(r"start_time['\"]?: ['\"]?([\d.]+)", str(s)); return float(m[1]) if m else 0.0

def preset_wi(campaign):  # xkcd / primitive-education: videos/<id>/{source_manifest.json,tables/state_ledger.csv}
    for d in sorted(glob.glob(f"{H}/{campaign}/videos/*/")):
        if not os.path.exists(d + "tables/state_ledger.csv"): continue
        m = json.load(open(d + "source_manifest.json"))["source"]
        rows = [dict(id=r["seg"], vs=r["visual_state_id"], start=int(r["start_frame"]), end=int(r["end_frame"]),
                     cls=r["event_class"], label=r["description"], text="") for r in csv.DictReader(open(d + "tables/state_ledger.csv"))]
        g = {}
        try: g = json.load(open(d + "quality_gate.json"))
        except Exception: pass
        yield dict(video_id=m["video_id"], src=m["file_path"], sha=m["sha256"], fps=rate(m["frame_rate_avg"]),
                   t0=t0_of(m.get("video_streams", "")), rows=rows, status=g.get("final_video_status", ""),
                   vfr=m.get("vfr_status", ""), root=f"{H}/{campaign}/asset_library")

def preset_be():
    root = f"{H}/barely-evolved/asset_library"
    for w, csvp, idc in (("2026-11-02-uPQcyookL0Y", "tables/states_v6_draft.csv", "state_v4"),
                         ("2026-11-03-GNaBxt_zIRA", "tables/states_v1.csv", "state"),
                         ("2026-11-03-mNLNb-Z4T0M", "tables/states_v1.csv", "state")):
        d = f"{H}/barely-evolved/{w}-deep-ct-scan/"; m = json.load(open(d + "source_manifest.json"))
        rows = [dict(id=r[idc], vs="", start=int(r["start"]), end=int(r["end"]), cls=r.get("kind", ""),
                     label=f"entry={r.get('entry','')}; see workspace tables for descriptions", text="") for r in csv.DictReader(open(d + csvp))]
        yield dict(video_id=m["video_id"], src=m["source_path"], sha=m["sha256"], fps=rate(m["video"]["fps"] if isinstance(m["video"], dict) else m["video"]),
                   t0=0.0, rows=rows, status="BE_FINAL_STATE_TABLE:" + csvp, vfr="30000/1001 (29.97)", root=root)

def run(c):
    vid, root = c["video_id"], c["root"]
    if sha(c["src"]) != c["sha"]: print(f"SHA_MISMATCH {vid}"); return
    by = {}
    for r in c["rows"]:
        n = r["start"] + min(3, r["end"] - r["start"]); r["rep"] = n; by.setdefault(n, []).append(r)
    frames = sorted(by); out = f"{root}/{vid}/states"; os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(f"{out}/{f}") if f.startswith("_seq") else None
    pts, seq = {}, {}
    for ci in range(0, len(frames), 40):
        ch = frames[ci:ci + 40]
        fs = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False)
        fs.write("select='" + "+".join(f"eq(n\\,{n})" for n in ch) + "',showinfo"); fs.close()
        p = subprocess.run(["ffmpeg", "-v", "info", "-nostdin", "-i", c["src"], "-an", "-/filter:v", fs.name, "-fps_mode", "passthrough",
                            "-q:v", "2", "-y", f"{out}/_seq{ci:05d}_%05d.jpg"], capture_output=True, text=True)
        os.remove(fs.name)
        pl = [float(m[1]) for l in p.stderr.splitlines() if "Parsed_showinfo" in l for m in [re.search(r" pts_time:([\d.]+)", l)] if m]
        got = sorted(f for f in os.listdir(out) if f.startswith(f"_seq{ci:05d}_"))
        if len(got) != len(ch) or len(pl) != len(ch):
            print(f"COUNT_MISMATCH {vid} chunk {ci}: want {len(ch)} got {len(got)}/{len(pl)} (frames beyond end?)"); return
        for n, fn, t in zip(ch, got, pl): pts[n] = t; seq[n] = fn
    idx, bad = [], 0
    for n in frames:
        t = pts[n]; ok = abs(t - (c["t0"] + n / c["fps"])) < 0.5 / c["fps"]; bad += not ok
        r0 = by[n][0]; new = f"{out}/{r0['id']}_f{n:06d}_t{t:.3f}.jpg"; os.replace(f"{out}/{seq[n]}", new)
        for r in by[n]:
            idx.append(dict(file="states/" + os.path.basename(new), video_id=vid, state_id=r["id"], visual_state_id=r["vs"], frame_index=n,
                            source_pts_s=t, pts_check="OK" if ok else "MISMATCH", event_class=r["cls"], what_changed=r["label"],
                            ledger_status=c["status"], vfr_note=c["vfr"], mp4_sha256=c["sha"], image_sha256=sha(new)))
    with open(f"{root}/{vid}/states_index.csv", "w", newline="") as f:
        w = csv.DictWriter(f, list(idx[0])); w.writeheader(); w.writerows(idx)
    print(f"{vid} fps={c['fps']:.4f} states={len(c['rows'])} frames={len(frames)} pts_mismatch={bad}")

kind, only = sys.argv[1], set(sys.argv[2:])
for c in (preset_be() if kind == "be" else preset_wi({"xkcd": "xkcd-whatif", "pe": "primitive-education"}[kind])):
    if not only or c["video_id"] in only: run(c)
