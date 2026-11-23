"""Contact sheet: python3 contact_sheet.py OUT.jpg VIDEO[:label] [VIDEO ...] --t 1,4,7,10 [--w 270]  -> one row of frames per video (JPEG, Read-tool friendly)"""
import subprocess, sys, io
from PIL import Image
F = '/opt/homebrew/bin/ffmpeg'
def frame(p, t, w):
    b = subprocess.run([F, '-v', 'error', '-ss', str(t), '-i', p, '-frames:v', '1', '-vf', f'scale={w}:-1', '-f', 'image2pipe', '-vcodec', 'bmp', '-'], capture_output=True).stdout
    try: return Image.open(io.BytesIO(b)).convert('RGB')
    except Exception: return Image.new('RGB', (w, int(w * 16 / 9)), (60, 60, 60))   # t beyond duration
if __name__ == '__main__':
    a = sys.argv[1:]; out = a[0]; w = 270
    if '--w' in a: i = a.index('--w'); w = int(a[i + 1]); del a[i:i + 2]
    i = a.index('--t'); ts = [float(x) for x in a[i + 1].split(',')]; vids = a[1:i]
    rows = [[frame(v, t, w) for t in ts] for v in vids]; h = rows[0][0].height
    s = Image.new('RGB', ((w + 4) * len(ts), (h + 4) * len(vids)), 'grey')
    for r, row in enumerate(rows):
        for c, im in enumerate(row): s.paste(im, (c * (w + 4), r * (h + 4)))
    s.save(out, quality=88)
