"""Visual QA sheet: python3 cmp_frames.py REF.mp4 RENDER.mp4 OUT.jpg FRAME [FRAME..] [--crop W:H:X:Y]
Per frame: [reference | render | diff overlay (ref-only red, render-only blue, both black)] stacked vertically. JPEG so the Read tool can open it."""
import subprocess, sys, io, numpy as np
from PIL import Image
F = '/opt/homebrew/bin/ffmpeg'
def grab(p, fr, crop):
    vf = f'select=eq(n\\,{fr})' + (f',crop={crop}' if crop else '')
    b = subprocess.run([F, '-v', 'error', '-i', p, '-vf', vf, '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'bmp', '-'], capture_output=True).stdout
    return Image.open(io.BytesIO(b)).convert('RGB')
def sheet(ref, ren, out, frames, crop=None, scale=0.5):
    rows = []
    for fr in frames:
        a, b = grab(ref, fr, crop), grab(ren, fr, crop)
        ia, ib = np.abs(np.asarray(a, int) - 253).sum(-1) > 60, np.abs(np.asarray(b, int) - 253).sum(-1) > 60
        d = np.full(a.size[::-1] + (3,), 255, np.uint8); d[ia & ~ib] = (220, 30, 30); d[ib & ~ia] = (30, 60, 230); d[ia & ib] = (0, 0, 0)
        row = Image.new('RGB', (a.width * 3 + 8, a.height), 'grey'); row.paste(a, (0, 0)); row.paste(b, (a.width + 4, 0)); row.paste(Image.fromarray(d), (2 * a.width + 8, 0))
        rows.append(row.resize((int(row.width * scale), int(row.height * scale))))
    s = Image.new('RGB', (rows[0].width, sum(r.height for r in rows) + 4 * len(rows)), 'grey'); y = 0
    for r in rows: s.paste(r, (0, y)); y += r.height + 4
    s.save(out, quality=90)
if __name__ == '__main__':
    a = sys.argv[1:]; crop = None
    if '--crop' in a: i = a.index('--crop'); crop = a[i + 1]; del a[i:i + 2]
    sheet(a[0], a[1], a[2], [int(x) for x in a[3:]], crop)
