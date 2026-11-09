#!/usr/bin/env python3
"""Read-only inventory of the Casually Finance source media directory.

Usage: python3 -I build_source_inventory.py <source_dir> <out_dir>

Never writes to <source_dir>. Container/stream facts come from ffprobe, not the
file extension. Decode check = one full ffmpeg decode of every stream to null.
Writes SOURCE_MEDIA_INVENTORY.csv and evidence/ffprobe_raw.jsonl under <out_dir>.
"""
import csv
import hashlib
import json
import os
import subprocess
import sys
from fractions import Fraction

FIELDS = [
    "Source_ID", "Relative_Path", "Filename", "Size_Bytes", "SHA256", "Mtime_ISO",
    "Container_Format", "Has_Video", "Has_Audio", "Duration_S", "Video_Frames_Counted",
    "FPS_Avg", "FPS_R", "Width", "Height", "Display_Aspect", "Orientation",
    "Video_Codec", "Video_Profile", "Pix_Fmt", "Video_Bitrate", "Audio_Codec",
    "Audio_Channels", "Audio_Sample_Rate", "Audio_Bitrate", "Format_Title_Tag",
    "Format_Comment_Tag", "Decode_Status", "Decode_Errors", "Ext_Matches_Container",
    "Acquisition_Family", "Filename_Title_Guess",
]


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fps(s):
    try:
        v = Fraction(s)
        return round(float(v), 3)
    except Exception:
        return ""


def family(name):
    if "SnapYT.App" in name:
        return "SNAPYT_TRUNCATED_TITLE"
    if "Casual Finance (" in name:
        return "YTDL_QUALITY_TAGGED"
    return "PLAIN_TITLE"


def title_guess(name):
    stem = os.path.splitext(name)[0]
    stem = stem.replace("-SnapYT.App", "")
    for tag in (" - Casual Finance (720p, h264)", " - Casual Finance (1080p, h264)"):
        stem = stem.replace(tag, "")
    if family(name) == "SNAPYT_TRUNCATED_TITLE":
        stem = stem.replace("-", " ")
    return stem.strip()


def main(src, out):
    os.makedirs(os.path.join(out, "evidence"), exist_ok=True)
    rows, raw = [], []
    files = []
    for root, _, names in os.walk(src):
        for n in sorted(names):
            files.append(os.path.join(root, n))
    files.sort()
    for i, p in enumerate(files, 1):
        st = os.stat(p)
        pr = sh(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", p])
        try:
            info = json.loads(pr.stdout)
        except Exception:
            info = {}
        fmt = info.get("format", {})
        streams = info.get("streams", [])
        v = next((s for s in streams if s.get("codec_type") == "video"), {})
        a = next((s for s in streams if s.get("codec_type") == "audio"), {})
        cnt = sh(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                  "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", p]).stdout.strip()
        dec = sh(["ffmpeg", "-v", "error", "-i", p, "-f", "null", "-"])
        errs = " | ".join(dec.stderr.strip().splitlines()[:3])
        ext = os.path.splitext(p)[1].lower().lstrip(".")
        fnames = fmt.get("format_name", "")
        w, h = v.get("width", ""), v.get("height", "")
        tags = fmt.get("tags", {}) or {}
        rel = os.path.relpath(p, src)
        rows.append({
            "Source_ID": "CFSRC-%03d" % i, "Relative_Path": rel, "Filename": os.path.basename(p),
            "Size_Bytes": st.st_size, "SHA256": sha256(p),
            "Mtime_ISO": __import__("datetime").datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
            "Container_Format": fnames, "Has_Video": bool(v), "Has_Audio": bool(a),
            "Duration_S": round(float(fmt.get("duration", 0) or 0), 3),
            "Video_Frames_Counted": cnt, "FPS_Avg": fps(v.get("avg_frame_rate", "0/1")),
            "FPS_R": fps(v.get("r_frame_rate", "0/1")), "Width": w, "Height": h,
            "Display_Aspect": v.get("display_aspect_ratio", ""),
            "Orientation": ("portrait" if h and w and h > w else "landscape" if h and w else ""),
            "Video_Codec": v.get("codec_name", ""), "Video_Profile": v.get("profile", ""),
            "Pix_Fmt": v.get("pix_fmt", ""), "Video_Bitrate": v.get("bit_rate", ""),
            "Audio_Codec": a.get("codec_name", ""), "Audio_Channels": a.get("channels", ""),
            "Audio_Sample_Rate": a.get("sample_rate", ""), "Audio_Bitrate": a.get("bit_rate", ""),
            "Format_Title_Tag": tags.get("title", ""), "Format_Comment_Tag": tags.get("comment", ""),
            "Decode_Status": "OK" if dec.returncode == 0 and not errs else "ERRORS",
            "Decode_Errors": errs,
            "Ext_Matches_Container": (ext in fnames.split(",")) or (ext == "mp4" and "mp4" in fnames),
            "Acquisition_Family": family(os.path.basename(p)),
            "Filename_Title_Guess": title_guess(os.path.basename(p)),
        })
        raw.append({"Source_ID": rows[-1]["Source_ID"], "path": rel, "ffprobe": info})
        print("%02d/%d %s %s" % (i, len(files), rows[-1]["Decode_Status"], os.path.basename(p)[:60]), flush=True)
    with open(os.path.join(out, "SOURCE_MEDIA_INVENTORY.csv"), "w", newline="") as f:
        w_ = csv.DictWriter(f, fieldnames=FIELDS)
        w_.writeheader()
        w_.writerows(rows)
    with open(os.path.join(out, "evidence", "ffprobe_raw.jsonl"), "w") as f:
        for r in raw:
            f.write(json.dumps(r, sort_keys=True) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
