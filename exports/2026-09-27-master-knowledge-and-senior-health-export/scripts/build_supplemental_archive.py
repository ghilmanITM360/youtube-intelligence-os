#!/usr/bin/env python3
"""Builds the self-contained supplemental data archive: real transcript text (portable,
relative-path references, not absolute paths on the original dev machine), full DS-000018
tab text, full DS-000031 corpus, full DS-000011 source text, downloaded thumbnail images
that already exist in the repo, and a manifest with sha256 for every copied file.

Read-only against data/ and docs/. Contents are staged in a system temporary directory
(removed on success or failure) and only the finished ZIP is written into the export
folder. An existing ZIP is never overwritten; pass a new --out path instead.
"""
import argparse
import hashlib
import json
import os
import shutil
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
EXPORT_DIR = Path(__file__).resolve().parents[1]
MASTER = json.loads((EXPORT_DIR / "master_data.json").read_text())
ARCHIVE_NAME = "supplemental-data-archive"
DEFAULT_OUT = EXPORT_DIR / "SUPPLEMENTAL-DATA-ARCHIVE.zip"
FIXED_ZIP_TIME = (2026, 9, 27, 0, 0, 0)
ARCHIVE = None  # staging directory, set by build() to a fresh temporary path

CHANNEL_SLUG = {
    "UCFpxvukIqCAUA7YizI-q9Dw": "better-health-while-aging",
    "UCQIzqH7QZ9viBYpOFqgSXMg": "own-channel-dr-rehan",
    "UCFuGMi0idGeyXl6wYK9hg7Q": "doctor-thomas",
    "UCMJxAeBJ0d1JC937de1eZ0Q": "dr-okoro",
    "UC356D-NzdnznBOftTpYoBLw": "dr-ares-senior",
    "UCQcBYZxFW7YwNMU8-DsT3Uw": "dr-elias-senior-health",
    "UCAYG0fzUyxv6OevH88qA45w": "senior-health-hub",
    "UCXZi5JVeuTluazF-fYqQgNA": "dr-aliza-wright",
}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_locator(locator):
    """locator is either 'path/to/file.txt' or 'path/to/archive.zip::member/path.txt'."""
    if "::" in locator:
        zip_part, member = locator.split("::", 1)
        with zipfile.ZipFile(REPO / zip_part) as z:
            return z.read(member)
    return (REPO / locator).read_bytes()


def build_transcripts():
    out_dir = ARCHIVE / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    videos_by_channel = MASTER["senior_health_videos_by_channel"]
    for cid, vids in videos_by_channel.items():
        slug = CHANNEL_SLUG[cid]
        (out_dir / slug).mkdir(parents=True, exist_ok=True)
        for v in vids:
            vid = v["youtube_video_id"]
            for t in v["transcripts"]:
                entry = {
                    "canonical_channel_id": cid,
                    "channel_slug": slug,
                    "youtube_video_id": vid,
                    "transcript_id": t["transcript_id"],
                    "dataset_id": t["dataset_id"],
                    "language": t["language"],
                    "caption_type": t["caption_type"],
                    "is_placeholder": bool(t["is_placeholder"]),
                    "word_count": t["word_count"],
                }
                if t["is_placeholder"]:
                    entry["status"] = "UNAVAILABLE"
                    entry["unavailable_reason"] = t.get("unavailable_reason")
                    manifest.append(entry)
                    continue
                try:
                    data = read_locator(t["evidence_locator"])
                except (FileNotFoundError, KeyError) as e:
                    entry["status"] = "SOURCE_DATA_UNREADABLE"
                    entry["error"] = str(e)
                    manifest.append(entry)
                    continue
                sha = sha256_bytes(data)
                sha_match = (sha == t.get("transcript_sha256"))
                out_path = out_dir / slug / f"{vid}.txt"
                out_path.write_bytes(data)
                entry["status"] = "COPIED"
                entry["archive_relative_path"] = str(out_path.relative_to(ARCHIVE))
                entry["sha256"] = sha
                entry["sha256_matches_catalog"] = sha_match
                entry["byte_size"] = len(data)
                manifest.append(entry)
    return manifest


def build_ds000018_tabs():
    out_dir = ARCHIVE / "ds-000018-full-tabs"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for t in MASTER["DS-000018"]["tabs"]:
        text = t.get("full_text")
        if not text:
            manifest.append({"tab_index": t["index"], "title": t["title"], "status": "MISSING"})
            continue
        fname = Path(t["snapshot_member"]).name
        out_path = out_dir / fname
        out_path.write_text(text, encoding="utf-8")
        manifest.append({
            "tab_index": t["index"], "title": t["title"],
            "archive_relative_path": str(out_path.relative_to(ARCHIVE)),
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "status": "COPIED",
        })
    return manifest


def build_ds000031_corpus():
    out_dir = ARCHIVE / "ds-000031-source"
    out_dir.mkdir(parents=True, exist_ok=True)
    src = REPO / "data/raw/global-youtube-knowledge/DS-000031/creator-strategy-audience-psychology-experimentation-corpus.txt"
    data = src.read_bytes()
    out_path = out_dir / "creator-strategy-audience-psychology-experimentation-corpus.txt"
    out_path.write_bytes(data)
    return [{
        "archive_relative_path": str(out_path.relative_to(ARCHIVE)),
        "sha256": sha256_bytes(data), "byte_size": len(data), "status": "COPIED",
    }]


def build_ds000011_sources():
    out_dir = ARCHIVE / "ds-000011-full-text"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for s in MASTER["DS-000011"]["fulltext_sources"]:
        if not s.get("full_text"):
            manifest.append({"filename": s["filename"], "status": "UNREADABLE_FORMAT", "sha256": s["sha256"]})
            continue
        out_path = out_dir / (s["filename"] + ".txt")
        out_path.write_text(s["full_text"], encoding="utf-8")
        manifest.append({
            "filename": s["filename"],
            "duplicate_of": s["duplicate_of"],
            "archive_relative_path": str(out_path.relative_to(ARCHIVE)),
            "original_sha256": s["sha256"],
            "status": "COPIED",
        })
    return manifest


def build_thumbnails():
    out_dir = ARCHIVE / "downloaded-thumbnails"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    videos_by_channel = MASTER["senior_health_videos_by_channel"]
    for cid, vids in videos_by_channel.items():
        slug = CHANNEL_SLUG[cid]
        for v in vids:
            lp = v.get("downloaded_thumbnail_local_path")
            if not lp:
                continue
            src = REPO / lp
            if not src.exists():
                manifest.append({"youtube_video_id": v["youtube_video_id"], "status": "SOURCE_PATH_MISSING", "recorded_path": lp})
                continue
            (out_dir / slug).mkdir(parents=True, exist_ok=True)
            ext = src.suffix
            out_path = out_dir / slug / f"{v['youtube_video_id']}{ext}"
            shutil.copyfile(src, out_path)
            manifest.append({
                "youtube_video_id": v["youtube_video_id"], "channel_slug": slug,
                "archive_relative_path": str(out_path.relative_to(ARCHIVE)),
                "original_repo_path": lp, "status": "COPIED",
            })
    return manifest


def write_zip(staging, out):
    """Write staging/ into out with sorted names and fixed timestamps, so reruns are byte-identical."""
    tmp = out.with_name(out.name + ".partial")
    try:
        with zipfile.ZipFile(tmp, "x", zipfile.ZIP_DEFLATED) as z:
            for path in sorted(p for p in staging.rglob("*") if p.is_file()):
                info = zipfile.ZipInfo(f"{ARCHIVE_NAME}/{path.relative_to(staging).as_posix()}", FIXED_ZIP_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, path.read_bytes())
        os.link(tmp, out)  # fails instead of replacing if out appeared meanwhile
    finally:
        tmp.unlink(missing_ok=True)


def build(out):
    global ARCHIVE
    out = Path(out)
    if out.exists():
        raise FileExistsError(f"{out} already exists; refusing to overwrite. Pass a new --out path.")
    with tempfile.TemporaryDirectory(prefix="supplemental-archive-") as tmp:
        ARCHIVE = Path(tmp) / ARCHIVE_NAME
        ARCHIVE.mkdir()
        summary = populate()
        write_zip(ARCHIVE, out)
    ARCHIVE = None
    return summary


def populate():
    manifest = {
        "generated_at": "2026-09-27",
        "note": "Self-contained supplemental data archive. All paths below are relative to this "
                "manifest's own directory. No source file under data/ or docs/ was modified to build this.",
        "transcripts": build_transcripts(),
        "ds_000018_full_tabs": build_ds000018_tabs(),
        "ds_000031_source_corpus": build_ds000031_corpus(),
        "ds_000011_full_text_sources": build_ds000011_sources(),
        "downloaded_thumbnails": build_thumbnails(),
    }
    manifest["summary"] = {
        "transcripts_copied": sum(1 for m in manifest["transcripts"] if m["status"] == "COPIED"),
        "transcripts_unavailable": sum(1 for m in manifest["transcripts"] if m["status"] == "UNAVAILABLE"),
        "transcripts_unreadable": sum(1 for m in manifest["transcripts"] if m["status"] not in ("COPIED", "UNAVAILABLE")),
        "transcripts_sha256_mismatch": sum(1 for m in manifest["transcripts"] if m["status"] == "COPIED" and not m.get("sha256_matches_catalog")),
        "ds18_tabs_copied": sum(1 for m in manifest["ds_000018_full_tabs"] if m["status"] == "COPIED"),
        "ds11_sources_copied": sum(1 for m in manifest["ds_000011_full_text_sources"] if m["status"] == "COPIED"),
        "thumbnails_copied": sum(1 for m in manifest["downloaded_thumbnails"] if m["status"] == "COPIED"),
    }
    (ARCHIVE / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    return manifest["summary"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    print(json.dumps(build(parser.parse_args().out), indent=2))


if __name__ == "__main__":
    main()
