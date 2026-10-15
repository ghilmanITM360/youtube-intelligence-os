"""V3 motion QA from the ENCODED video: decode consecutive frames of a loop-test window, crop to the character, and build
(1) a phase strip: 8 evenly spaced phases of one cycle + the frames either side of each foot contact / stroke entry and
the loop boundary; (2) a dense sequence sheet (every frame of two cycles) for frame-to-frame motion review.
python3 tools/motion_qa_v3.py MP4 T0 PERIOD "x0,y0,x1,y1" OUT_PREFIX "contact phases (comma)" """
import io, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

F = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)


def grab(mp4, t, box):
    png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.4f}", "-i", mp4, "-frames:v", "1", "-f", "image2pipe",
                          "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(png)).convert("RGB").crop(box)


def sheet(cells, cols, out):
    w, h = cells[0][1].size
    s = Image.new("RGB", (cols * w, -(-len(cells) // cols) * (h + 30)), "white")
    d = ImageDraw.Draw(s)
    for i, (lab, im) in enumerate(cells):
        x, y = i % cols * w, i // cols * (h + 30)
        s.paste(im, (x, y + 30)); d.text((x + 6, y + 4), lab, font=F, fill=(41, 42, 45))
        d.rectangle([x, y + 30, x + w - 1, y + 30 + h - 1], outline=(200, 200, 200))
    s.save(out)


mp4, t0, per, box, pre = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), tuple(map(int, sys.argv[4].split(","))), sys.argv[5]
contacts = [float(c) for c in sys.argv[6].split(",")] if len(sys.argv) > 6 else []
f = 1 / 30
cells = [(f"phase {i}/8  t={t0 + per * i / 8:.3f}", grab(mp4, t0 + per * i / 8, box)) for i in range(8)]
for c in contacts + [1.0]:
    tc = t0 + per * c
    cells += [(f"{'loop' if c == 1.0 else 'contact'} {c:.2f} {k:+d}f", grab(mp4, tc + k * f, box)) for k in (-1, 0, 1)]
sheet(cells, 8, pre + "_PHASES.png")
n = round(2 * per * 30)
sheet([(f"f{k}  {t0 + k * f:.3f}s", grab(mp4, t0 + k * f, box)) for k in range(n)], 9, pre + "_SEQUENCE.png")
print(pre + "_PHASES.png", pre + "_SEQUENCE.png")
