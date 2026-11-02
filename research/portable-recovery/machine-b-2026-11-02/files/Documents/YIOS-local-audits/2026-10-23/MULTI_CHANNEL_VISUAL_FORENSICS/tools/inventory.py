"""Read-only inventory of the seven-channel source folder.

Usage: python3 -I inventory.py <media_root> <all_videos_csv> <cf_machineA_inventory_csv> <out_csv>
Hashes every MP4 (SHA-256, streamed), ffprobes it, and maps a Video ID by:
  1. bracketed [11-char id] in filename (yt-dlp naming)          -> FILENAME_BRACKET_ID
  2. SHA-256 equal to a row in Machine A SOURCE_MEDIA_INVENTORY   -> SHA256_MATCH_MACHINE_A
  3. otherwise IDENTITY_UNVERIFIED (title matching is reported separately, never trusted alone)
Source files are opened read-only; nothing is written next to them.
"""
import csv, hashlib, json, os, re, subprocess, sys

root, all_videos, cf_inv, out = sys.argv[1:5]
csv.field_size_limit(10**9)
ID_RE = re.compile(r"\[([A-Za-z0-9_-]{11})\]")

meta = {}
with open(all_videos, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        meta[r["video_id"]] = r
cfa = {}
with open(cf_inv, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        cfa[r["SHA256"]] = r


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", p],
                       capture_output=True, text=True)
    if r.returncode:
        return None, r.stderr.strip()[:200]
    return json.loads(r.stdout), ""


rows = []
for ch in sorted(os.listdir(root)):
    d = os.path.join(root, ch)
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if not fn.lower().endswith(".mp4"):
            continue
        p = os.path.join(d, fn)
        h = sha256(p)
        pr, err = probe(p)
        v = a = {}
        dur = ""
        if pr:
            v = next((s for s in pr["streams"] if s["codec_type"] == "video"), {})
            a = next((s for s in pr["streams"] if s["codec_type"] == "audio"), {})
            dur = pr["format"].get("duration", "")
        m = ID_RE.search(fn)
        if m:
            vid, method = m.group(1), "FILENAME_BRACKET_ID"
        elif h in cfa:
            vid, method = cfa[h]["Video_ID"], "SHA256_MATCH_MACHINE_A"
        else:
            vid, method = "", "IDENTITY_UNVERIFIED"
        md = meta.get(vid, {})
        w, ht = int(v.get("width", 0) or 0), int(v.get("height", 0) or 0)
        fr = v.get("avg_frame_rate", "0/1").split("/")
        fps = round(int(fr[0]) / int(fr[1]), 3) if len(fr) == 2 and int(fr[1]) else ""
        rows.append({
            "channel_folder": ch, "filename": fn, "size_bytes": os.path.getsize(p), "sha256": h,
            "video_id": vid, "id_method": method,
            "registry_channel": md.get("channel_name", ""), "registry_title": md.get("title", ""),
            "registry_duration": md.get("duration", ""), "registry_format": md.get("format", ""),
            "in_yios_all_videos": bool(md),
            "decode_status": "OK" if pr and v else ("NO_VIDEO_STREAM" if pr else "PROBE_FAILED:" + err),
            "duration_s": dur, "width": w, "height": ht, "fps": fps, "vcodec": v.get("codec_name", ""),
            "acodec": a.get("codec_name", ""), "has_audio": bool(a),
            "orientation": "portrait" if ht > w else ("landscape" if w > ht else "square"),
        })
        print(ch, fn[:50], method, file=sys.stderr)

# duplicate groups: same sha256 or same video_id
by_h, by_id = {}, {}
for r in rows:
    by_h.setdefault(r["sha256"], []).append(r)
    if r["video_id"]:
        by_id.setdefault(r["video_id"], []).append(r)
for r in rows:
    r["dup_same_hash"] = len(by_h[r["sha256"]]) - 1
    r["dup_same_id"] = len(by_id.get(r["video_id"], [r])) - 1
    grp = by_id.get(r["video_id"]) or by_h[r["sha256"]]
    r["canonical_copy"] = grp[0] is r  # first by sorted filename

with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(len(rows), "rows", file=sys.stderr)
