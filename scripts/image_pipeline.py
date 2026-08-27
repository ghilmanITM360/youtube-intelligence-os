#!/usr/bin/env python3
"""Layer-1 image integrity + perceptual-hash helper (Phase 1C).

Standalone by design: the only script in this repo that needs Pillow, so it
is the only one that must run under the isolated `.venv/bin/python3`
(`docs/TOOLS_INSTALLED.md`) rather than the system `python3`. Never modifies
the source image. Prints one JSON object to stdout; non-zero exit + a
one-line error on stderr if the image cannot be opened/validated.
"""
import json
import sys

from PIL import Image, ExifTags


def _exif_dict(img):
    try:
        raw = img.getexif()
    except Exception:
        return {}
    if not raw:
        return {}
    out = {}
    for tag_id, value in raw.items():
        tag = ExifTags.TAGS.get(tag_id, str(tag_id))
        if isinstance(value, bytes):
            value = value.decode("utf-8", errors="replace")
        try:
            json.dumps(value)
        except TypeError:
            value = str(value)
        out[tag] = value
    return out


def dhash(img, hash_size=8):
    """Deterministic difference-hash (Pillow-only, no extra dependency).
    Returns a hex string; Hamming distance between two hashes approximates
    perceptual similarity. ponytail: coarse (8x8) — swap for a maintained
    perceptual-hash package if false-positive clustering becomes a problem.
    """
    small = img.convert("L").resize((hash_size + 1, hash_size), Image.LANCZOS)
    pixels = list(small.getdata())
    bits = []
    for row in range(hash_size):
        row_start = row * (hash_size + 1)
        for col in range(hash_size):
            bits.append(pixels[row_start + col] > pixels[row_start + col + 1])
    value = 0
    for bit in bits:
        value = (value << 1) | (1 if bit else 0)
    return "{:0{}x}".format(value, hash_size * hash_size // 4)


def inspect(path):
    with Image.open(path) as img:
        img.load()  # force full decode -> validates the file, not just the header
        width, height = img.size
        result = {
            "width_px": width,
            "height_px": height,
            "color_mode": img.mode,
            "image_format": img.format,
            "orientation": "LANDSCAPE" if width > height else ("PORTRAIT" if height > width else "SQUARE"),
            "exif": _exif_dict(img),
            "dhash": dhash(img),
            "dhash_algorithm": "dhash8x8",
        }
    return result


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--batch":
        # One warm process for many images (avoids per-image subprocess
        # startup cost at batch scale) — one path per stdin line, one JSON
        # object per stdout line, in the same order. A per-image failure is
        # reported inline and does not abort the batch.
        for line in sys.stdin:
            path = line.rstrip("\n")
            if not path:
                continue
            try:
                result = inspect(path)
                result["path"] = path
            except Exception as exc:  # noqa: BLE001
                result = {"path": path, "error": str(exc)}
            print(json.dumps(result))
        return

    if len(sys.argv) != 2:
        print("usage: image_pipeline.py <path> | image_pipeline.py --batch (paths on stdin)", file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    try:
        result = inspect(path)
    except Exception as exc:  # noqa: BLE001 - report, never crash the caller silently
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
