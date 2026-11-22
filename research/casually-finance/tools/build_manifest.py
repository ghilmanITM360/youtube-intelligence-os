#!/usr/bin/env python3
"""Read-only: map local CF mp4 files to catalog IDs, verify duration + audio, sha256. Writes manifest.csv."""
import csv, hashlib, json, os, re, subprocess, sys, unicodedata

MEDIA = os.path.expanduser("~/Downloads/videos in mp3/CasuallyFinance")
CAT = "/private/tmp/claude-501/cat.csv"
OUT = os.path.expanduser("~/YIOS-local-audits/CF_TRANSCRIPTS_ASR_20261109/manifest.csv")
FF = "/opt/homebrew/bin/ffprobe"

def norm(s):
    s = unicodedata.normalize("NFKD", s).lower()
    s = re.sub(r"snapyt\.app|casual finance|\(720p, h264\)|\.mp4", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

cat = list(csv.DictReader(open(CAT, encoding="utf-8")))
by_id = {r["video_id"]: r for r in cat}
by_title = {}
for r in cat:
    by_title.setdefault(norm(r["title"])[:25], []).append(r)


# Reviewed 2026-11-09: truncated SnapYT filenames resolved by title words + duration (|delta|<=1 s). Evidence: manifest delta column.
OVERRIDE = {
 "Everyones-Future-Is-SnapYT.App.mp4": "7IMFHclDn8k",
 "The-Worlds-Greatest-SnapYT.App.mp4": "m8NC4L8hmeE",
 "Americas-Debt-Has-SnapYT.App.mp4": "-WJDfT-MwmY",
 "Americas-Self-Reinforcing-Debt-SnapYT.App.mp4": "-Vr8JhCIv08",
 "If-You-Dont-SnapYT.App.mp4": "xrNPr3YrWdw",
 "To Save the Economy... We\u2019re About to Break It - Casual Finance (1080p, h264).mp4": "xtqbRt94TTw",
 "MicroStrategy The Crypto Scam Hiding in Plain Sight - Casual Finance (1080p, h264).mp4": "dlBhLhn8lL0",
}

def probe(p):
    j = json.loads(subprocess.check_output([FF, "-v", "error", "-show_entries",
        "format=duration:stream=codec_type", "-of", "json", p]))
    dur = float(j["format"]["duration"])
    audio = any(s.get("codec_type") == "audio" for s in j.get("streams", []))
    return dur, audio

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

rows = []
for fn in sorted(os.listdir(MEDIA)):
    if not fn.endswith(".mp4"):
        continue
    p = os.path.join(MEDIA, fn)
    m = re.search(r"\[([A-Za-z0-9_-]{11})\]\.mp4$", fn)
    vid, how = "", "UNMATCHED"
    if m:
        vid, how = m.group(1), "ID_IN_NAME"
    dur, audio = probe(p)
    if not m:
        stem = norm(fn)
        c = [r for r in cat if norm(r["title"]).startswith(stem)] if stem else []
        if len(c) > 1:
            c = [r for r in c if abs(float(r["duration_sec"]) - dur) <= 3]
        if fn in OVERRIDE:
            vid, how = OVERRIDE[fn], "MANUAL_TITLE+DUR"
        elif len(c) == 1:
            vid, how = c[0]["video_id"], "TITLE_PREFIX+DUR"
        elif len(c) > 1:
            how = "TITLE_AMBIGUOUS"
    cd = by_id.get(vid, {}).get("duration_sec", "")
    try:
        delta = round(dur - float(cd), 2)
    except ValueError:
        delta = ""
    ok = "NA"
    if delta != "":
        ok = "OK" if abs(delta) <= 3 else "DURATION_MISMATCH"
    rows.append(dict(file=fn, video_id=vid, match=how, in_catalog=vid in by_id,
        local_dur=round(dur, 2), catalog_dur=cd, delta=delta, dur_check=ok,
        has_audio=audio, size=os.path.getsize(p), sha256=sha(p)))

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

from collections import Counter
print("files", len(rows))
print("match", Counter(r["match"] for r in rows))
print("dur_check", Counter(r["dur_check"] for r in rows))
print("no_audio", [r["file"] for r in rows if not r["has_audio"]])
ids = Counter(r["video_id"] for r in rows if r["in_catalog"])
print("catalog ids covered", len(ids), "dup ids", {k: v for k, v in ids.items() if v > 1})
print("catalog ids missing", [r["video_id"] for r in cat if r["video_id"] not in ids])
print("not-in-catalog files", [(r["file"], r["video_id"]) for r in rows if not r["in_catalog"]])
print("mismatches", [(r["file"][:50], r["video_id"], r["delta"]) for r in rows if r["dur_check"] == "DURATION_MISMATCH"])
