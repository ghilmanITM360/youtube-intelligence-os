"""CH001 novel NS6: family C dense document/chart montage (original art, no source pixels). Targets from gate.py on 3132dfa8:
full-height (rows 125-1915), ~0.79 s/state, dark-ink share ~0.42, continuous drift motion, #FDFDFD canvas. Usage: render_novel4.py OUT_DIR"""
import os, random, subprocess, sys
from PIL import Image, ImageDraw
W, H, FPS, N = 1080, 1920, 30, 600
BG = (253, 253, 253)
def card(d, x, y, w, h, rnd, kind):
    d.rectangle([x, y, x + w, y + h], fill=(245, 245, 240), outline=(30, 30, 30), width=5)
    if kind == 0:   # text document: header block + ruled lines
        d.rectangle([x + 20, y + 20, x + w * .6, y + 60], fill=(20, 20, 20))
        for i in range(int((h - 100) / 26)): d.rectangle([x + 20, y + 80 + i * 26, x + 20 + rnd.uniform(.4, .95) * (w - 40), y + 85 + i * 26], fill=(60, 60, 60))
    elif kind == 1:  # bar chart
        for i in range(6): bh = rnd.uniform(.2, .9) * (h - 60); d.rectangle([x + 20 + i * (w - 40) / 6, y + h - 20 - bh, x + 20 + (i + .7) * (w - 40) / 6, y + h - 20], fill=(85, 85, 85))
    else:            # coin stack
        for i in range(5): d.ellipse([x + w * .2, y + h - 60 - i * 40, x + w * .8, y + h - 20 - i * 40], fill=(50, 50, 50), outline=(10, 10, 10), width=4)
def frame(f):
    s = f // 24                      # new composition every 0.8 s
    rnd = random.Random(s * 7919); im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    for i in range(rnd.randint(5, 8)):
        w, h = rnd.randint(260, 520), rnd.randint(260, 620); x, y = rnd.randint(0, W - w), rnd.randint(130, H - h - 10)
        dx, dy = rnd.uniform(-1, 1) * 0.12 * (f % 24), rnd.uniform(-1, 1) * 0.12 * (f % 24)   # continuous drift inside the beat
        card(d, x + dx, y + dy, w, h, random.Random(s * 31 + i), rnd.randint(0, 2))
    return im
if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    p = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '14', os.path.join(out, 'NS6_dense_montage.mp4')], stdin=subprocess.PIPE)
    for f in range(N): p.stdin.write(frame(f).tobytes())
    p.stdin.close(); p.wait(); print('NS6', N, 'frames')
