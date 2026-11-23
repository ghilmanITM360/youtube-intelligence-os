"""One-command family gate: python3 gate.py FILE.mp4 [FILE2 ...]
Per video (6 fps, 216 px wide): s/state (ink-mask IoU<0.80), dark-ink share, bottom-caption rows (dark ink 65-80% H),
content rows, green/orange panel hit. Same code for refs and renders, so numbers are comparable. Numeric only."""
import subprocess, sys, numpy as np, os
def gate(p):
    W = 216; H = 384
    pr = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-i', p, '-vf', f'fps=6,scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    n = W * H * 3; fs = []
    while True:
        b = pr.stdout.read(n)
        if len(b) < n: break
        fs.append(np.frombuffer(b, np.uint8).reshape(H, W, 3).astype(np.int16))
    F = np.array(fs); N = len(F)
    ink = np.abs(F - 253).sum(-1) > 60; st, anc = 1, 0
    for i in range(1, N):
        u = (ink[anc] | ink[i]).sum()
        if (ink[anc] & ink[i]).sum() / u < 0.80 if u else False: st += 1; anc = i
    dark = F.max(-1) < 70
    dark_share = dark.sum() / max(1, ink.sum())
    rows = ink.mean(axis=(0, 2)); act = np.where(rows > 0.01)[0]
    cap = dark[:, int(H * .65):int(H * .80)].mean() > 0.002
    rgb = F.reshape(-1, 3)
    grn = (np.abs(rgb - [48, 144, 80]).sum(-1) < 60).mean(); org = (np.abs(rgb - [240, 144, 16]).sum(-1) < 60).mean()
    return dict(file=os.path.basename(p)[:34], dur=round(N / 6, 1), s_per_state=round(N / 6 / st, 2), states=st, dark_share=round(float(dark_share), 2),
                caption=bool(cap), rows=(int(act.min() * 1920 / H), int(act.max() * 1920 / H)) if len(act) else None, green=round(float(grn), 3), orange=round(float(org), 3))
if __name__ == '__main__':
    for p in sys.argv[1:]: print(gate(p), flush=True)
