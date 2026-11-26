"""Contact sheet of a video at given times (labelled). usage: contact_sheet.py VIDEO OUT.jpg COLS t1 t2 ..."""
import subprocess, sys, io
from PIL import Image, ImageDraw, ImageFont
v, out, cols, ts = sys.argv[1], sys.argv[2], int(sys.argv[3]), [float(x) for x in sys.argv[4:]]
W, H = 270, 480; f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 22)
rows = -(-len(ts) // cols); sheet = Image.new('RGB', (cols * W, rows * H))
for i, t in enumerate(ts):
    png = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t), '-i', v, '-frames:v', '1', '-vf', 'scale=%d:%d' % (W, H), '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True, check=True).stdout
    im = Image.open(io.BytesIO(png)).convert('RGB'); d = ImageDraw.Draw(im); d.text((6, 4), '%.2f' % t, font=f, fill=(255, 230, 0), stroke_width=2, stroke_fill=(0, 0, 0))
    sheet.paste(im, ((i % cols) * W, (i // cols) * H))
sheet.save(out, quality=88); print(out, sheet.size)
