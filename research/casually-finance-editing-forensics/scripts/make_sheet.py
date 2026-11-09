#!/usr/bin/env python3
"""Build annotated contact sheets of NATIVE-resolution frames from a source video (read-only).

Usage:
  python3 -E make_sheet.py <video_id> <out_png> --frames 12,13,20-30 [--cols 6] [--scale 0.6]
  python3 -E make_sheet.py <video_id> <out_png> --range 0:10:0.5      # start:end:step in seconds
Frames are selected by native frame number n (0-based, as ffmpeg `select=eq(n,..)`), so the label
"f207 6.900s" is exact. Frame images are decoded once into a temp dir and deleted afterwards.
"""
import argparse
import csv
import os
import shutil
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont

RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = "/Users/ghilmankhan/Downloads/CasuallyFinance"


def source(vid):
    for r in csv.DictReader(open(os.path.join(RDIR, "SOURCE_MEDIA_INVENTORY.csv"))):
        if r["Video_ID"] == vid and r["Canonical_For_Analysis"] == "True":
            return os.path.join(SRC_DIR, r["Relative_Path"]), float(r["FPS_Avg"])
    raise SystemExit("unknown video id")


def parse_frames(spec):
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        elif part:
            out.append(int(part))
    return sorted(set(out))


def extract(src, frames, tmp):
    sel = "+".join("eq(n,%d)" % f for f in frames)
    subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf", "select='%s'" % sel, "-fps_mode", "passthrough", "-q:v", "2",
                    os.path.join(tmp, "f%05d.jpg")], check=True)
    files = sorted(os.listdir(tmp))
    assert len(files) == len(frames), "extracted %d of %d frames" % (len(files), len(frames))
    return [Image.open(os.path.join(tmp, f)).convert("RGB") for f in files]


def sheet(frames_img, labels, cols, scale, out):
    w0, h0 = frames_img[0].size
    w, h = int(w0 * scale), int(h0 * scale)
    bar = 18
    rows = (len(frames_img) + cols - 1) // cols
    font = ImageFont.load_default(size=13)
    canvas = Image.new("RGB", (cols * (w + 4), rows * (h + bar + 4)), (40, 40, 40))
    d = ImageDraw.Draw(canvas)
    for i, (im, lab) in enumerate(zip(frames_img, labels)):
        x, y = (i % cols) * (w + 4), (i // cols) * (h + bar + 4)
        d.text((x + 3, y + 2), lab, fill=(255, 255, 0), font=font)
        canvas.paste(im.resize((w, h), Image.LANCZOS), (x, y + bar))
    canvas.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vid")
    ap.add_argument("out")
    ap.add_argument("--frames")
    ap.add_argument("--range")
    ap.add_argument("--cols", type=int, default=6)
    ap.add_argument("--scale", type=float, default=0.6)
    ap.add_argument("--cell-w", type=int, default=0, help="target cell width in px (overrides --scale)")
    ap.add_argument("--crop", default="", help="normalized x0:y0:x1:y1 applied to every frame")
    a = ap.parse_args()
    src, fps = source(a.vid)
    if a.range:
        s, e, st = [float(x) for x in a.range.split(":")]
        frames, t = [], s
        while t < e - 1e-9:
            frames.append(int(round(t * fps)))
            t += st
        frames = sorted(set(frames))
    else:
        frames = parse_frames(a.frames)
    tmp = tempfile.mkdtemp()
    try:
        imgs = extract(src, frames, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if a.crop:
        x0, y0, x1, y1 = [float(v) for v in a.crop.split(":")]
        W, H = imgs[0].size
        imgs = [im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))) for im in imgs]
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    sc = (a.cell_w / imgs[0].size[0]) if a.cell_w else a.scale
    sheet(imgs, ["f%d %.3fs" % (f, f / fps) for f in frames], a.cols, sc, a.out)
    print(a.out, len(frames), "frames", imgs[0].size)


if __name__ == "__main__":
    main()
