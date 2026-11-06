"""Rebuild data/manifests/VISUAL_FORENSICS_REGISTRY_CROSSWALK.csv from pinned Git sources and the committed registry.

Contract: docs/VISUAL_FORENSICS_IDENTITY_CONTRACT.md. Writes no database. Needs the pinned commits in the local object store.
"""
import csv
import io
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/manifests/VISUAL_FORENSICS_REGISTRY_CROSSWALK.csv"
FIELDS = ["youtube_channel_id", "channel_name", "video_id", "title_from_source", "in_registry", "source_commit", "source_path"]
# (channel id, canonical name, commit, path, video id column, title column)
SOURCES = [
    ("UCrNfRFWnLC3tCy1TnyhVQ7g", "Casual Finance", "1adfdeb9462023b39fa62b9a54da12ccd874ae16",
     "research/casually-finance-video-inventory/CASUALLY_FINANCE_VIDEO_INVENTORY.csv", "Video ID", "Video Title"),
    ("UC6IxnFzHofFJ5X2PycSMsww", "xkcd's What If?", "3bd92e6ac578b9699a725a96ec129f2c97b4263c",
     "research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/census/census.csv", "video_id", "title"),
    ("UCH59TmQhPOPhC3M17jCWpRQ", "Barely Evolved", "c4212c90ecd57fe9416da2948a95669050366512",
     "research/barely-evolved-metadata/VIDEO_MASTER.csv", "video_id", "title"),
    ("UCsuQtyrMiUPdHUQ8WaqsFvQ", "Primitive Education", "f3769da1",
     "research/visual-forensics/channels/UCsuQtyrMiUPdHUQ8WaqsFvQ/census/source_census.csv", None, "reg_title"),
]


def build():
    registry = sqlite3.connect(f"file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro", uri=True)
    known = {row[0]: row[1] for row in registry.execute("SELECT youtube_video_id, canonical_channel_id FROM videos")}
    rows, owner = [], {}
    for channel, name, commit, path, id_column, title_column in SOURCES:
        text = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{commit}:{path}"], text=True, encoding="utf-8")
        full_commit = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", commit], text=True).strip()
        for source in csv.DictReader(io.StringIO(text)):
            # Primitive Education's census names files, with the ID in brackets before the extension.
            video = source[id_column] if id_column else source["file"].rsplit("[", 1)[1].split("]", 1)[0]
            if owner.setdefault(video, channel) != channel:
                raise ValueError(f"{video} claimed by {owner[video]} and {channel}")
            if known.get(video, channel) != channel:
                raise ValueError(f"{video} is registered under {known[video]}, source says {channel}")
            rows.append({"youtube_channel_id": channel, "channel_name": name, "video_id": video,
                         "title_from_source": source.get(title_column, ""), "in_registry": str(video in known).lower(),
                         "source_commit": full_commit, "source_path": path})
    rows.sort(key=lambda r: (r["youtube_channel_id"], r["video_id"]))
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


if __name__ == "__main__":
    print(f"{len(build())} rows -> {OUTPUT}", file=sys.stderr)
