#!/usr/bin/env python3
"""Download only thumbnail URLs already registered for one canonical channel."""

import argparse
import hashlib
import io
import json
import mimetypes
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, UnidentifiedImageError

from report_common import REPO_ROOT, connect


CURRENT_STATE = "CURRENT_REMOTE_SNAPSHOT"


def sha256_bytes(body):
    return hashlib.sha256(body).hexdigest()


def require_registered_url(url, registered_urls):
    if url not in registered_urls:
        raise ValueError("URL is not registered canonical evidence")
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("registered thumbnail URL must use HTTPS")
    return url


def require_safe_redirect(original_url, target_url, registered_hosts):
    target = urllib.parse.urlparse(target_url)
    if target.scheme != "https" or target.hostname not in registered_hosts:
        raise ValueError("unsafe redirect from {} to {}".format(original_url, target_url))
    return target_url


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, original_url, registered_hosts, chain):
        self.original_url = original_url
        self.registered_hosts = registered_hosts
        self.chain = chain

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        require_safe_redirect(self.original_url, newurl, self.registered_hosts)
        self.chain.append({"http_status": code, "url": newurl})
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def validate_image(body, content_type):
    mime = (content_type or "").split(";", 1)[0].strip().lower()
    if not mime.startswith("image/"):
        raise ValueError("unexpected image MIME: {}".format(mime or "missing"))
    if not body:
        raise ValueError("empty image response")
    if body.lstrip().lower().startswith((b"<!doctype html", b"<html")):
        raise ValueError("invalid image: HTML response")
    try:
        with Image.open(io.BytesIO(body)) as image:
            image.verify()
        with Image.open(io.BytesIO(body)) as image:
            width, height = image.size
            image_format = image.format
    except (UnidentifiedImageError, OSError, SyntaxError) as error:
        raise ValueError("invalid image: {}".format(error)) from error
    if width <= 0 or height <= 0:
        raise ValueError("invalid image dimensions")
    return {
        "width": width,
        "height": height,
        "aspect_ratio": round(width / height, 6),
        "image_format": image_format,
        "mime_type": mime,
        "byte_size": len(body),
        "sha256": sha256_bytes(body),
    }


def store_image(body, content_type, raw_dir, known_hashes):
    metadata = validate_image(body, content_type)
    digest = metadata["sha256"]
    extension = mimetypes.guess_extension(metadata["mime_type"]) or ".img"
    if extension == ".jpe":
        extension = ".jpg"
    path = Path(raw_dir) / digest[:2] / (digest + extension)
    duplicate = digest in known_hashes
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    return {
        **metadata,
        "binary_status": "EXACT_DUPLICATE_BINARY" if duplicate else "NEW_BINARY",
        "local_path": str(path),
    }


def evidence_state(requested=CURRENT_STATE, historical_proof=False):
    allowed = {"HISTORICAL_BINARY_VERIFIED", CURRENT_STATE, "TEMPORAL_MATCH_UNKNOWN"}
    if requested not in allowed:
        raise ValueError("invalid evidence state")
    if requested == "HISTORICAL_BINARY_VERIFIED" and not historical_proof:
        raise ValueError("historical evidence requires proof")
    return requested


def failed_snapshot(video_id, url, result, error, **fields):
    return {
        "video_id": video_id,
        "original_registered_url": url,
        "result": result,
        "error": error,
        "visual_features": None,
        "evidence_state": CURRENT_STATE,
        "temporal_alignment_state": "TEMPORAL_ALIGNMENT_UNKNOWN",
        **fields,
    }


def load_registered(conn, channel_id):
    rows = conn.execute(
        """WITH latest_thumbnails AS (
               SELECT te.*,
                      ROW_NUMBER() OVER (
                        PARTITION BY te.video_id ORDER BY te.observed_at DESC, te.thumbnail_evidence_id DESC
                      ) AS rank
               FROM thumbnail_evidence te
               JOIN videos v ON v.video_id = te.video_id
               WHERE v.channel_id = ? AND te.thumbnail_url IS NOT NULL
           ), latest_titles AS (
               SELECT vs.*,
                      ROW_NUMBER() OVER (
                        PARTITION BY vs.video_id ORDER BY vs.observed_at DESC, vs.video_snapshot_id DESC
                      ) AS rank
               FROM video_snapshots vs
               JOIN videos v ON v.video_id = vs.video_id
               WHERE v.channel_id = ?
           )
           SELECT s.video_id, COALESCE(t.dataset_id, s.dataset_id) AS dataset_id,
                  COALESCE(t.thumbnail_url, s.thumbnail_url) AS thumbnail_url,
                  COALESCE(t.observed_at, s.observed_at) AS url_recorded_at,
                  s.title, s.observed_at AS title_observed_at, s.video_type
           FROM latest_titles s
           LEFT JOIN latest_thumbnails t ON t.video_id = s.video_id AND t.rank = 1
           WHERE s.rank = 1 AND COALESCE(t.thumbnail_url, s.thumbnail_url) IS NOT NULL
           ORDER BY s.video_id""",
        (channel_id, channel_id),
    ).fetchall()
    return [
        {
            **dict(row),
            "format": "SHORTS" if (row["video_type"] or "").lower() == "shorts" else "LONG_FORM",
        }
        for row in rows
    ]


def fetch_registered(record, registered_urls, registered_hosts, raw_root, retrieved_at, known_hashes, attempts=3):
    url = require_registered_url(record["thumbnail_url"], registered_urls)
    chain = []
    opener = urllib.request.build_opener(SafeRedirectHandler(url, registered_hosts, chain))
    request = urllib.request.Request(url, headers={"User-Agent": "YouTube-Intelligence-OS/thumbnail-evidence"})
    common = {
        "format": record["format"],
        "dataset_id": record["dataset_id"],
        "url_recorded_at": record["url_recorded_at"],
        "title": record["title"],
        "title_observed_at": record["title_observed_at"],
        "retrieval_timestamp": retrieved_at,
        "acquisition_method": "DIRECT_FETCH_REGISTERED_URL",
        "redirect_chain": chain,
    }
    try:
        for attempt in range(1, attempts + 1):
            try:
                with opener.open(request, timeout=30) as response:
                    status = response.getcode()
                    final_url = response.geturl()
                    content_type = response.headers.get("Content-Type")
                    body = response.read()
                break
            except (urllib.error.URLError, TimeoutError, OSError):
                if attempt == attempts:
                    raise
                time.sleep(0.25 * attempt)
        common["attempt_count"] = attempt
        if status != 200:
            return failed_snapshot(record["video_id"], url, "DOWNLOAD_FAILED", "HTTP {}".format(status), http_status=status, final_url=final_url, **common)
        try:
            image = store_image(body, content_type, raw_root / record["dataset_id"] / "thumbnail-snapshots", known_hashes)
        except ValueError as error:
            result = "UNEXPECTED_CONTENT_TYPE" if "MIME" in str(error) else "INVALID_IMAGE"
            return failed_snapshot(record["video_id"], url, result, str(error), http_status=status, final_url=final_url, mime_type=content_type, byte_size=len(body), **common)
        known_hashes.add(image["sha256"])
        result = image.pop("binary_status")
        return {
            "video_id": record["video_id"],
            "original_registered_url": url,
            **common,
            "http_status": status,
            "final_url": final_url,
            **image,
            "result": result,
            "evidence_state": CURRENT_STATE,
            "title_snapshot_state": "CANONICAL_TITLE_SNAPSHOT",
            "thumbnail_snapshot_state": CURRENT_STATE,
            "package_snapshot_state": "CURRENT_THUMBNAIL_WITH_CANONICAL_TITLE",
            "temporal_alignment_state": "TEMPORAL_ALIGNMENT_UNKNOWN",
            "historical_performance_correlation": "TEMPORAL_ALIGNMENT_UNKNOWN",
            "visual_features": None,
        }
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as error:
        return failed_snapshot(record["video_id"], url, "DOWNLOAD_FAILED", str(error), **common)


def build_manifest(channel_id, rows, retrieved_at):
    ordered = sorted(rows, key=lambda row: row["video_id"])
    results = Counter(row["result"] for row in ordered)
    hashes = Counter(row.get("sha256") for row in ordered if row.get("sha256"))
    return {
        "schema_version": "registered-thumbnail-acquisition-1",
        "channel_id": channel_id,
        "retrieval_timestamp": retrieved_at,
        "evidence_state": CURRENT_STATE,
        "registered_urls": len(ordered),
        "attempted": len(ordered),
        "successful_images": results["NEW_BINARY"] + results["EXACT_DUPLICATE_BINARY"],
        "failed_downloads": results["DOWNLOAD_FAILED"],
        "invalid_images": results["INVALID_IMAGE"] + results["UNEXPECTED_CONTENT_TYPE"],
        "unique_hashes": len(hashes),
        "duplicate_hash_groups": sum(count > 1 for count in hashes.values()),
        "result_counts": dict(sorted(results.items())),
        "format_counts": dict(sorted(Counter(row.get("format", "UNKNOWN") for row in ordered).items())),
        "snapshots": ordered,
        "guardrails": {
            "allowlist_source": "canonical registered thumbnail references for requested channel",
            "crawl_performed": False,
            "url_discovery_performed": False,
            "youtube_api_used": False,
            "apify_called": False,
            "historical_state_asserted": False,
        },
    }


def render_json(payload):
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, indent=2) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--db")
    parser.add_argument("--output", required=True)
    parser.add_argument("--raw-root", default=str(REPO_ROOT / "data/raw/competitors"))
    parser.add_argument("--retrieved-at")
    args = parser.parse_args(argv)
    retrieved_at = args.retrieved_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    with connect(args.db) as conn:
        records = load_registered(conn, args.channel)
    urls = {row["thumbnail_url"] for row in records}
    hosts = {urllib.parse.urlparse(url).hostname for url in urls}
    known_hashes = set()
    snapshots = [
        fetch_registered(row, urls, hosts, Path(args.raw_root), retrieved_at, known_hashes)
        for row in records
    ]
    manifest = build_manifest(args.channel, snapshots, retrieved_at)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_json(manifest), encoding="utf-8")
    print(render_json({key: value for key, value in manifest.items() if key != "snapshots"}), end="")


if __name__ == "__main__":
    main()
