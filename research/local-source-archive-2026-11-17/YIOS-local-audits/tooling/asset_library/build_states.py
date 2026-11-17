#!/usr/bin/env python3
"""Targeted state-frame extraction for the asset library (local only, copies, no source edits).
usage: python3 -I build_states.py <workspace_dir> <asset_library_root>
Reads visual_states.csv + source_manifest.json, verifies MP4 SHA-256, decodes ONLY rep_frame of each state
in a single ffmpeg pass, cross-checks PTS with showinfo, writes states/*.jpg + states_index.csv."""
import csv, hashlib, json, os, re, subprocess, sys, tempfile

ws, root = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
OLD = not os.path.exists(f"{ws}/source_manifest.json")
man = json.load(open(f"{ws}/SOURCE_IDENTITY_AND_MANIFEST.json" if OLD else f"{ws}/source_manifest.json"))
vid, src, want = man["video_id"], man["source_path"], man["source_sha256"]
V = man["video"]
fps_s = (V.get("avg_frame_rate") or json.dumps(V)) if isinstance(V, dict) else str(V)
m = re.search(r"avg_frame_rate'?\"?: '?\"?(\d+)/(\d+)", fps_s) or re.search(r"(\d+)/(\d+)", fps_s)
fps = int(m[1]) / int(m[2]) if m else 24.0
ms = re.search(r"(?:start_time|first_pts_s)['\"]?: ['\"]?([\d.]+)", json.dumps(V) if isinstance(V, dict) else str(V))
t0 = float(ms[1]) if ms else 0.0   # first-frame PTS (e.g. 1/30 s => frame i at (i+1)/30)
print(f"{vid} fps={fps:.4f} first_pts={t0}")

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

if sha(src) != want:
    sys.exit(f"SHA_MISMATCH {vid}")
rows = list(csv.DictReader(open(f"{ws}/VISUAL_STATES.csv" if OLD else f"{ws}/visual_states.csv")))
if OLD:  # legacy schema: rep frame = start+3 clipped to state end (same convention as newer ledgers); labels from objects
    for r in rows:
        r["visual_state_id"] = r["state_id"]; r["shot_id"] = r["shot_id_inferred"]
        r["rep_frame"] = str(min(int(r["start_frame"]) + 3, int(r["end_frame"])))
        r["entering_change"] = r.get("entry_episode", ""); r["label"] = r["objects"][:160]
        r["visible_text"] = r["readable_text"]; r["asset_ids"] = r.get("family", "")
by_frame = {}
for r in rows: by_frame.setdefault(int(r["rep_frame"]), []).append(r)
frames = sorted(by_frame)
out = f"{root}/{vid}/states"
os.makedirs(out, exist_ok=True)
pts, seq_map = {}, {}
CH = 40
for ci in range(0, len(frames), CH):
    chunk = frames[ci:ci + CH]
    expr = "+".join(f"eq(n\\,{n})" for n in chunk)
    fs = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False)
    fs.write(f"select='{expr}',showinfo"); fs.close()
    pat = f"{out}/_seq{ci:05d}_%05d.jpg"
    p = subprocess.run(["ffmpeg", "-v", "info", "-nostdin", "-i", src, "-an", "-/filter:v", fs.name,
                        "-fps_mode", "passthrough", "-q:v", "2", "-y", pat], capture_output=True, text=True)
    os.remove(fs.name)
    plist = [float(mm[1]) for line in p.stderr.splitlines() if "Parsed_showinfo" in line
             for mm in [re.search(r" pts_time:([\d.]+)", line)] if mm]
    got = sorted(f for f in os.listdir(out) if f.startswith(f"_seq{ci:05d}_"))
    if len(got) != len(chunk) or len(plist) != len(chunk):
        sys.exit(f"COUNT_MISMATCH {vid} chunk {ci}: want {len(chunk)} got {len(got)}/{len(plist)}\n{p.stderr[-400:]}")
    for n, fn, t in zip(chunk, got, plist):  # Nth showinfo line == Nth selected source frame
        pts[n] = t; seq_map[n] = fn
seq = [seq_map[n] for n in frames]
idx = []
bad = 0
for fn, n in zip(seq, frames):
    exp_t = t0 + n / fps
    t = pts.get(n)
    ok = t is not None and abs(t - exp_t) < 0.5 / fps
    bad += (not ok)
    r0 = by_frame[n][0]
    new = f"{out}/{r0['visual_state_id']}_f{n:05d}_t{(t if t is not None else exp_t):.3f}.jpg"
    os.replace(f"{out}/{fn}", new)
    for r in by_frame[n]:
        idx.append({"file": f"states/{os.path.basename(new)}", "video_id": vid, "state_id": r["visual_state_id"],
                    "shot_id": r["shot_id"], "frame_index": n, "source_pts_s": t if t is not None else "",
                    "pts_check": "OK" if ok else "MISMATCH", "entering_class": (r.get("entering_class") or r.get("entering_change") or ""),
                    "what_changed": (r.get("label") or r.get("literal_description") or ""), "visible_text": r["visible_text"], "asset_ids": r["asset_ids"],
                    "mp4_sha256": want, "image_sha256": sha(new)})
cols = list(idx[0])
with open(f"{root}/{vid}/states_index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(idx)
print(f"{vid} states={len(rows)} unique_frames={len(frames)} pts_mismatch={bad} dir={out}")
