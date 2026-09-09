import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import acquire_registered_thumbnails as acquire  # noqa: E402


def png_bytes(size=(8, 6), color="white"):
    stream = io.BytesIO()
    Image.new("RGB", size, color).save(stream, format="PNG")
    return stream.getvalue()


class RegisteredThumbnailAcquisitionTests(unittest.TestCase):
    def test_accepts_only_exact_registered_urls(self):
        registered = {"https://i.ytimg.com/vi/abc/maxresdefault.jpg"}

        self.assertEqual(acquire.require_registered_url(next(iter(registered)), registered), next(iter(registered)))
        with self.assertRaisesRegex(ValueError, "not registered"):
            acquire.require_registered_url("https://i.ytimg.com/vi/other/maxresdefault.jpg", registered)

    def test_redirect_stays_https_and_on_registered_host(self):
        hosts = {"i.ytimg.com"}

        self.assertEqual(
            acquire.require_safe_redirect("https://i.ytimg.com/a", "https://i.ytimg.com/b", hosts),
            "https://i.ytimg.com/b",
        )
        for target in ("https://example.com/b", "http://i.ytimg.com/b"):
            with self.assertRaisesRegex(ValueError, "unsafe redirect"):
                acquire.require_safe_redirect("https://i.ytimg.com/a", target, hosts)

    def test_valid_image_is_decoded_and_measured(self):
        metadata = acquire.validate_image(png_bytes((8, 6)), "image/png")

        self.assertEqual(metadata["width"], 8)
        self.assertEqual(metadata["height"], 6)
        self.assertEqual(metadata["aspect_ratio"], 1.333333)
        self.assertEqual(metadata["image_format"], "PNG")

    def test_rejects_invalid_mime_html_empty_and_invalid_image(self):
        cases = [
            (png_bytes(), "text/html", "unexpected image MIME"),
            (b"<html>error</html>", "image/jpeg", "invalid image"),
            (b"", "image/png", "empty image"),
            (b"not an image", "image/jpeg", "invalid image"),
        ]
        for body, mime, message in cases:
            with self.subTest(mime=mime, body=body[:8]):
                with self.assertRaisesRegex(ValueError, message):
                    acquire.validate_image(body, mime)

    def test_sha_and_content_addressed_dedup_are_deterministic(self):
        body = png_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            first = acquire.store_image(body, "image/png", Path(tmp), set())
            second = acquire.store_image(body, "image/png", Path(tmp), {first["sha256"]})

        self.assertEqual(first["sha256"], acquire.sha256_bytes(body))
        self.assertEqual(first["sha256"], second["sha256"])
        self.assertEqual(first["binary_status"], "NEW_BINARY")
        self.assertEqual(second["binary_status"], "EXACT_DUPLICATE_BINARY")

    def test_manifest_is_deterministic_and_format_separated(self):
        rows = [
            {"video_id": "VID-2", "format": "SHORTS", "result": "DOWNLOAD_FAILED"},
            {"video_id": "VID-1", "format": "LONG_FORM", "result": "NEW_BINARY"},
        ]
        first = acquire.build_manifest("CH-X", rows, "2026-09-09T00:00:00Z")
        second = acquire.build_manifest("CH-X", list(reversed(rows)), "2026-09-09T00:00:00Z")

        self.assertEqual(acquire.render_json(first), acquire.render_json(second))
        self.assertEqual(first["format_counts"], {"LONG_FORM": 1, "SHORTS": 1})
        self.assertEqual(list(json.loads(acquire.render_json(first))), sorted(first))

    def test_current_snapshot_default_and_historical_promotion_requires_proof(self):
        self.assertEqual(acquire.evidence_state(), "CURRENT_REMOTE_SNAPSHOT")
        with self.assertRaisesRegex(ValueError, "historical evidence requires proof"):
            acquire.evidence_state("HISTORICAL_BINARY_VERIFIED")
        self.assertEqual(
            acquire.evidence_state("HISTORICAL_BINARY_VERIFIED", historical_proof=True),
            "HISTORICAL_BINARY_VERIFIED",
        )

    def test_missing_image_never_fabricates_visual_features(self):
        row = acquire.failed_snapshot("VID-1", "https://i.ytimg.com/a", "DOWNLOAD_FAILED", "timeout")

        self.assertIsNone(row["visual_features"])
        self.assertEqual(row["temporal_alignment_state"], "TEMPORAL_ALIGNMENT_UNKNOWN")


if __name__ == "__main__":
    unittest.main()
