"""Motion review aid: N evenly spaced DECODED frames of an MP4 in one strip + per-frame mean abs difference curve.
This is a frame-sequence review, not real-time viewing; reports must say so.
usage: python tools/filmstrip.py clip.mp4 out.png [n=12]"""
import subprocess, sys, json
import numpy as np
from PIL import Image, ImageDraw
mp4, out = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
pr = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height,nb_frames,r_frame_rate', '-of', 'json', mp4]))['streams'][0]
w, h, nf = pr['width'], pr['height'], int(pr['nb_frames']); fps = eval(pr['r_frame_rate'])
raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', mp4, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'])
fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)
d = np.abs(np.diff(fr.astype(np.int16)[:, ::4, ::4], axis=0)).mean((1, 2, 3))
idx = np.linspace(0, len(fr) - 1, n).astype(int); tw = 180; th = int(h * tw / w)
S = Image.new('RGB', (tw * n, th + 90), 'white'); D = ImageDraw.Draw(S)
for k, i in enumerate(idx):
    S.paste(Image.fromarray(fr[i]).resize((tw, th)), (k * tw, 0)); D.text((k * tw + 4, th + 2), '%.2fs' % (i / fps), fill='black')
pts = [(x * tw * n / len(d), th + 88 - min(60, v * 6)) for x, v in enumerate(d)]; D.line(pts, fill='red', width=2)
S.save(out)
print('frames %d; mean step %.2f; max step %.2f at %.2fs; steps > 3x median: %d' % (len(fr), d.mean(), d.max(), (d.argmax() + 1) / fps, int((d > 3 * np.median(d) + 1).sum())))
