#!/usr/bin/env python3
"""Build provenance manifest and labeled contact sheets for DS-000032 thumbnails."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/raw/competitors/DS-000032/dataset.json"
EVIDENCE_DIR = ROOT / "data/raw/competitors/DS-000032/public-browser-2026-09-27"
THUMB_DIR = EVIDENCE_DIR / "thumbnails"
SHEET_DIR = EVIDENCE_DIR / "contact-sheets"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    records = json.loads(DATASET.read_text(encoding="utf-8"))
    SHEET_DIR.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default(size=18)
    manifest_records = []
    items = []

    for record in sorted(records, key=lambda item: item["id"]):
        video_id = record["id"]
        path = THUMB_DIR / f"{video_id}.jpg"
        with Image.open(path) as image:
            width, height = image.size
        url = record["thumbnailUrl"]
        id_in_url = f"/vi/{video_id}/" in urlparse(url).path
        manifest_records.append(
            {
                "video_id": video_id,
                "recorded_type": record["type"],
                "source_thumbnail_url": url,
                "source_dataset": "data/raw/competitors/DS-000032/dataset.json",
                "source_observed_at": "2026-09-25T10:45:45.525Z",
                "retrieved_at": "2026-09-27",
                "retrieval_method": "direct public i.ytimg.com URL retained in DS-000032",
                "local_path": str(path.relative_to(ROOT)),
                "sha256": sha256(path),
                "width": width,
                "height": height,
                "video_id_matches_source_url": id_in_url,
                "visual_inspection_status": "PENDING",
            }
        )
        items.append((record, path))

    for batch_index in range(0, len(items), 4):
        batch = items[batch_index : batch_index + 4]
        canvas = Image.new("RGB", (1280, 820), "white")
        draw = ImageDraw.Draw(canvas)
        for index, (record, path) in enumerate(batch):
            x = (index % 2) * 640
            y = (index // 2) * 410
            with Image.open(path) as image:
                image = image.convert("RGB")
                image.thumbnail((620, 349), Image.Resampling.LANCZOS)
                canvas.paste(image, (x + 10, y + 10))
            label = f"{record['id']} | {record['type']} | {record['viewCount']} views"
            draw.rectangle((x + 10, y + 365, x + 630, y + 400), fill="white")
            draw.text((x + 14, y + 370), label, fill="black", font=font)
        page = batch_index // 4 + 1
        canvas.save(SHEET_DIR / f"sheet-{page:02d}.jpg", quality=92)

    manifest = {
        "dataset_id": "DS-000032",
        "canonical_channel_id": "UCQIzqH7QZ9viBYpOFqgSXMg",
        "observation_dates_preserved": {
            "retained_acquisition": "2026-09-25T10:45:45.525Z",
            "public_retrieval": "2026-09-27",
        },
        "image_count": len(manifest_records),
        "records": manifest_records,
    }
    (EVIDENCE_DIR / "thumbnail-recovery-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
