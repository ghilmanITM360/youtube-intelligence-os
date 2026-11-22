"""Adapter: Codex nested rig_anchors.json -> flat schema the renderer reads. Copies PNGs untouched into v1r4_assets/rig/ (sha256 verified).
  python3 tools/v1r4_rig_adapter.py            build + self-test (15 pairings)"""
import json, os, shutil, hashlib, itertools, sys
from PIL import Image
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = HERE + '/codex_art/v2_rig/provisional_family'; OUT = HERE + '/v1r4_assets/rig'
FIX = SRC + '/targeted_correction_20261121'  # approved corrections overlay the base family, file by file
BODIES = ('down', 'shrug', 'point'); HEADS = ('neutral', 'smile', 'worried', 'surprised', 'smirk')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()

def flatten(nested, sizes):
    out = {}
    for b in BODIES: out['rig_body_%s.png' % b] = dict(neck=nested['bodies'][b]['neck'], size=sizes['rig_body_%s.png' % b])
    for h in HEADS: out['rig_head_%s.png' % h] = dict(chin=nested['heads'][h]['chin'], size=sizes['rig_head_%s.png' % h])
    return out

def build():
    os.makedirs(OUT, exist_ok=True); sizes = {}
    for f in ['rig_body_%s.png' % b for b in BODIES] + ['rig_head_%s.png' % h for h in HEADS]:
        src = FIX + '/' + f if os.path.exists(FIX + '/' + f) else SRC + '/' + f
        shutil.copy2(src, OUT + '/' + f); assert sha(src) == sha(OUT + '/' + f), f
        sizes[f] = list(Image.open(OUT + '/' + f).size)
    flat = flatten(json.load(open(SRC + '/rig_anchors.json')), sizes)
    json.dump(flat, open(OUT + '/rig_anchors.json', 'w'), indent=1); return flat

def test(flat):
    """every head x body: chin lands on neck within 6 px; head centre-x vs torso centre-x; neck anchor inside body alpha; chin inside head alpha"""
    res = []
    for b, h in itertools.product(BODIES, HEADS):
        B = Image.open('%s/rig_body_%s.png' % (OUT, b)); H = Image.open('%s/rig_head_%s.png' % (OUT, h))
        nk = flat['rig_body_%s.png' % b]['neck']; ch = flat['rig_head_%s.png' % h]['chin']
        assert tuple(B.size) == tuple(flat['rig_body_%s.png' % b]['size']) and tuple(H.size) == tuple(flat['rig_head_%s.png' % h]['size'])
        # placed head origin = neck - chin; chin pixel lands exactly on neck pixel by construction -> measure artwork centres instead
        hb = H.getchannel('A').getbbox(); head_cx = (hb[0] + hb[2]) / 2 - ch[0]      # head art centre relative to chin x
        import numpy as np; a = np.array(B)[..., :3].astype(int); m = (abs(a - (91, 107, 58)).sum(2) < 30); m[:nk[1] + 60] = 0; m[nk[1] + 400:] = 0  # olive torso pixels only
        xs = np.where(m.any(0))[0]; torso_cx = (xs.min() + xs.max()) / 2 - nk[0]
        neck_ok = B.getpixel((nk[0], nk[1] + 40))[3] > 0; chin_ok = H.getpixel((ch[0], ch[1] - 5))[3] > 0
        res.append((b, h, round(head_cx, 1), round(torso_cx, 1), neck_ok, chin_ok))
    bad = [r for r in res if abs(r[2] - r[3]) > 6 or not r[4] or not r[5]]
    return res, bad

if __name__ == '__main__':
    flat = build(); res, bad = test(flat)
    for r in res: print(r)
    print('flat keys', len(flat), 'point neck', flat['rig_body_point.png']['neck'], 'FAIL' if bad else 'PASS 15/15', bad)
    sys.exit(1 if bad else 0)
