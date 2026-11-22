"""Audio as timing reference only (internal): distance of visual-state boundaries to speech-pause edges vs random baseline. Usage: audio_sync.py KEY..."""
import an, subprocess, re, sys, numpy as np
def run(key):
    p = an.find(key); W, H = 216, 384
    pr = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-i', p, '-vf', f'fps=6,scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    fs = []
    while True:
        b = pr.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        fs.append(np.abs(np.frombuffer(b, np.uint8).reshape(H, W, 3).astype(np.int16) - 253).sum(-1) > 60)
    bd, anc = [], 0
    for i in range(1, len(fs)):
        u = (fs[anc] | fs[i]).sum()
        if u and (fs[anc] & fs[i]).sum() / u < .8: bd.append(i / 6); anc = i
    o = subprocess.run(['/opt/homebrew/bin/ffmpeg', '-i', p, '-vn', '-af', 'silencedetect=noise=-32dB:d=0.12', '-f', 'null', '-'], capture_output=True, text=True).stderr
    pts = np.array(sorted(float(x) for x in re.findall(r'silence_(?:start|end): ([\d.]+)', o))); dur = len(fs) / 6
    d = lambda x: np.abs(x[:, None] - pts[None]).min(1); b = np.array(bd); r = d(b); q = d(np.random.RandomState(0).uniform(0, dur, 5000))
    print(key, 'bounds', len(b), 'pause edges', len(pts), 'median dist real %.2f rand %.2f | within 0.2s real %.2f rand %.2f' % (np.median(r), np.median(q), (r < .2).mean(), (q < .2).mean()), flush=True)
for k in sys.argv[1:]: run(k)
