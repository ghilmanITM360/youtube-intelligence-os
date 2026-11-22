"""Frame-by-frame comparison of a rendered reconstruction MP4 against the source for chosen shots (playback scale, art region only, captions excluded).
Per frame: ink coverage both ways (3px tol), mean abs colour diff in union-of-ink bbox, and exact-frame-change timeline (render vs source change frames)."""
import json, os, subprocess, sys
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_sprite_vs_source as V
SPAN = {1: (0, 98), 2: (99, 153), 3: (154, 253), 4: (254, 365), 5: (366, 439), 6: (440, 476), 7: (477, 510), 8: (511, 540), 9: (541, 630), 10: (631, 663), 11: (664, 706), 12: (707, 729), 13: (730, 779), 14: (780, 824), 15: (825, 849), 16: (850, 1046), 17: (1047, 1104), 18: (1105, 1159), 19: (1160, 1191), 20: (1192, 1288), 21: (1289, 1460), 22: (1461, 1659)}
def raw(path, a, b, box):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    cmd = ['ffmpeg', '-v', 'error', '-i', path, '-vf', 'select=between(n\\,%d\\,%d),crop=%d:%d:%d:%d' % (a, b, w, h, x0, y0), '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    return np.frombuffer(subprocess.check_output(cmd), np.uint8).reshape(-1, h, w, 3)
def compare(render, shot, box=(0, 650, 1080, 1290), tag=None, outdir=None, sheet_frames=None):
    a, b = SPAN[shot]; S = raw(V.SRC, a, b, box); R = raw(render, a, b, box); n = min(len(S), len(R)); rows = []
    for i in range(n):
        sg = np.array(Image.fromarray(S[i]).convert('L')) < 110; rg = np.array(Image.fromarray(R[i]).convert('L')) < 110
        sd, rd = V.dil(sg), V.dil(rg)
        rows.append((float((sg & rd).sum() / max(1, sg.sum())), float((rg & sd).sum() / max(1, rg.sum())), float(np.abs(S[i].astype(int) - R[i].astype(int)).mean())))
    r = np.array(rows)
    # change timelines (frames where ink pattern changes by >50 px) in each
    def changes(X):
        g = [np.array(Image.fromarray(x).convert('L')) < 110 for x in X]; return [a + i for i in range(1, len(g)) if int((g[i] ^ g[i - 1]).sum()) > 50]
    cs, cr = changes(S[:n]), changes(R[:n])
    res = dict(shot='SH%03d' % shot, frames=n, src_ink_covered_by_render_mean=round(r[:, 0].mean(), 3), src_ink_covered_min=round(r[:, 0].min(), 3), render_ink_on_source_mean=round(r[:, 1].mean(), 3), render_ink_on_source_min=round(r[:, 1].min(), 3),
               mean_abs_rgb_diff=round(r[:, 2].mean(), 2), max_abs_rgb_diff=round(r[:, 2].max(), 2), source_change_frames=cs[:40], render_change_frames=cr[:40])
    if outdir:
        os.makedirs(outdir, exist_ok=True)
        picks = sheet_frames or [a, (a + b) // 2, b]; tiles = []
        for f in picks:
            i = f - a
            if i >= n: continue
            sg = np.array(Image.fromarray(S[i]).convert('L')) < 110; rg = np.array(Image.fromarray(R[i]).convert('L')) < 110
            d = np.full(S[i].shape, 255, 'uint8'); d[sg & ~rg] = (230, 40, 40); d[rg & ~sg] = (40, 80, 230); d[rg & sg] = 0
            tiles.append(np.concatenate([S[i], R[i], d], 1))
        Image.fromarray(np.concatenate(tiles, 0)).resize((1620, int(1620 * sum(t.shape[0] for t in tiles) / tiles[0].shape[1]))).save(os.path.join(outdir, 'cmp_%s.png' % (tag or 'SH%03d' % shot)))
    return res
if __name__ == '__main__':
    render = sys.argv[1]; shots = [int(x) for x in sys.argv[2].split(',')]; outdir = sys.argv[3]
    res = [compare(render, s, outdir=outdir) for s in shots]; json.dump(res, open(os.path.join(outdir, 'render_vs_source.json'), 'w'), indent=1)
    for r in res: print({k: v for k, v in r.items() if 'frames' not in k or k == 'frames'}, 'src chg', r['source_change_frames'][:12], 'render chg', r['render_change_frames'][:12])
