#!/usr/bin/env python3
"""Rebuild research/casually-finance/INDEX.csv from repo files. Run from repo root. Read-only except INDEX.csv."""
import csv, os
R = "research/casually-finance"
FV = "data/extracted/forensic-analysis/casually-finance/2026-10-12/02_VIDEO_FORENSICS"
cat = list(csv.DictReader(open("data/extracted/forensic-analysis/casually-finance/2026-10-12/01_CHANNEL_METADATA/all-videos-metadata.csv", encoding="utf-8")))
man = {r["video_id"] for r in csv.DictReader(open(f"{R}/transcripts_asr_base_20261109/manifest.csv", encoding="utf-8")) if r["in_catalog"] == "True"}
cols = ["video_id","title","format","published_at","duration_sec","views","in_git_transcript","git_transcript_path","asr_base_transcript","local_media_verified","visual_forensics_dir","editing_forensics_dir"]
rows = []
for r in cat:
    i = r["video_id"]
    g = f"{FV}/{i}/TRANSCRIPT.csv"; a = f"{R}/transcripts_asr_base_20261109/{i}.txt"
    v = f"research/visual-forensics/channels/casual-finance/{i}"; e = f"research/casually-finance-editing-forensics/videos/{i}"
    rows.append(dict(video_id=i, title=r["title"], format=r["format_class"], published_at=r["published_at"][:10],
        duration_sec=r["duration_sec"], views=r["views"],
        in_git_transcript=os.path.exists(g), git_transcript_path=g if os.path.exists(g) else "",
        asr_base_transcript=a if os.path.exists(a) else "", local_media_verified=i in man,
        visual_forensics_dir=v if os.path.isdir(v) else "", editing_forensics_dir=e if os.path.isdir(e) else ""))
with open(f"{R}/INDEX.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
n = len(rows)
print("rows", n, "git", sum(r["in_git_transcript"] for r in rows), "asr", sum(bool(r["asr_base_transcript"]) for r in rows),
      "any_text", sum(r["in_git_transcript"] or bool(r["asr_base_transcript"]) for r in rows),
      "media", sum(r["local_media_verified"] for r in rows), "visual", sum(bool(r["visual_forensics_dir"]) for r in rows),
      "editing", sum(bool(r["editing_forensics_dir"]) for r in rows))
