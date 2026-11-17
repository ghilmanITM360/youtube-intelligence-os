"""V1-vs-V2 corrected-frame evidence: side-by-side decoded frames from the two encoded MP4s.
python3 tools/evidence_v2.py V1.mp4 V2.mp4 OUT.png "t_v1,t_v2,label" ..."""
import io, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

F = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)


def grab(mp4, t, w=360):
    png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-vf",
                          f"scale={w}:{w * 16 // 9}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(png)).convert("RGB")


v1, v2, out, rows = sys.argv[1], sys.argv[2], sys.argv[3], [r.split(",", 2) for r in sys.argv[4:]]
tw, th = 360, 640
sheet = Image.new("RGB", (2 * tw + 30, len(rows) * (th + 70)), (236, 236, 232))
d = ImageDraw.Draw(sheet)
for i, (a, b, label) in enumerate(rows):
    y = i * (th + 70)
    d.text((10, y + 8), label, font=F, fill=(41, 42, 45))
    sheet.paste(grab(v1, float(a)), (10, y + 40)); sheet.paste(grab(v2, float(b)), (tw + 20, y + 40))
    d.text((14, y + 44), f"V1 {float(a):.2f}s", font=F, fill=(200, 60, 40))
    d.text((tw + 24, y + 44), f"V2 {float(b):.2f}s", font=F, fill=(40, 120, 110))
sheet.save(out)
print(out)
