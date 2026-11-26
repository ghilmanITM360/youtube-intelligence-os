"""V3 review aid: render film frames straight from the scene code (no video) into one labelled sheet.
usage: v3_stills.py OUT.jpg COLS t1 t2 ...   (scale 0.25: 270x480 tiles)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'animation'))
from PIL import Image, ImageDraw, ImageFont
import roughcut as RC
from uemotion import space as S
from uemotion.video import ClipSpec, render_frame
out, cols, ts = sys.argv[1], int(sys.argv[2]), [float(x) for x in sys.argv[3:]]
S.preload_real(); spec = ClipSpec('CUT', 'stills', 0.0, RC.DUR, RC.scene, captions=False, audio=False)
f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 22); W, H = 270, 480
rows = -(-len(ts) // cols); sheet = Image.new('RGB', (cols * W, rows * H))
for i, t in enumerate(ts):
    im = render_frame(spec, int(round(t * 30)), 0.25, 30).convert('RGB').resize((W, H)); d = ImageDraw.Draw(im)
    d.text((6, 4), '%.2f' % t, font=f, fill=(255, 230, 0), stroke_width=2, stroke_fill=(0, 0, 0)); sheet.paste(im, ((i % cols) * W, (i // cols) * H))
sheet.save(out, quality=88); print(out)
