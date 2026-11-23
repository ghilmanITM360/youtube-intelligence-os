"""Pixel-level (dilated ink-mask) IoU per frame between reference and a render. Stricter than bbox IoU. Usage: pixel_iou.py REF_KEY RENDER.mp4 [DIL]"""
import an, subprocess, sys, numpy as np
def load(p, W=216, H=384):
    pr = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-i', p, '-vf', f'fps=6,scale={W}:{H}:flags=area', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE); fs = []
    while True:
        b = pr.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        fs.append(np.abs(np.frombuffer(b, np.uint8).reshape(H, W, 3).astype(np.int16) - 253).sum(-1) > 60)
    return np.array(fs)
def dil(m, k):
    o = m.copy()
    for dy in range(-k, k + 1):
        for dx in range(-k, k + 1): o |= np.roll(np.roll(m, dy, 1), dx, 2)
    return o
if __name__ == '__main__':
    k = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    A, B = load(an.find(sys.argv[1])), load(sys.argv[2]); n = min(len(A), len(B)); A, B = A[:n], B[:n]
    # tolerant IoU: intersection of dilated-vs-raw both ways (precision/recall) -> F1-like
    prec = (B & dil(A, k)).sum((1, 2)) / np.maximum(1, B.sum((1, 2))); rec = (A & dil(B, k)).sum((1, 2)) / np.maximum(1, A.sum((1, 2)))
    f = 2 * prec * rec / np.maximum(1e-9, prec + rec)
    print('frames', n, 'dil', k, 'F1 median %.3f mean %.3f p10 %.3f' % (np.median(f), f.mean(), np.percentile(f, 10)))
    for lo in range(0, n, 30):
        s = f[lo:lo + 30]
        if s.mean() < .8: print('  %.1f-%.1fs F1 %.2f prec %.2f rec %.2f' % (lo / 6, (lo + 30) / 6, s.mean(), prec[lo:lo + 30].mean(), rec[lo:lo + 30].mean()))
