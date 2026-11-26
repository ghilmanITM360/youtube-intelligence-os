"""Asset acceptance check for layered PNG art (PROPOSED standard; tested on V15 assets in the scratchpad).
usage: python validate_asset.py FILE [--canvas WxH] [--min-blob 400]
Reports: mode, size, alpha range, alpha bbox, RGB-under-zero-alpha pixels, semi-transparent fringe share,
and connected opaque components (stray blobs). Exit 1 on FAIL."""
import sys, json
import numpy as np
from PIL import Image
from scipy import ndimage
def check(path, canvas=None, min_blob=400):
    im = Image.open(path); res = dict(file=str(path), mode=im.mode, size=list(im.size), fail=[], warn=[])
    if im.mode != 'RGBA': res['fail'].append('not RGBA')
    a = np.asarray(im.convert('RGBA')); al = a[..., 3]
    res['alpha_range'] = [int(al.min()), int(al.max())]
    if al.max() == 0: res['fail'].append('fully transparent'); return res
    ys, xs = np.nonzero(al > 8); res['alpha_bbox_ltrb'] = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
    if canvas and list(im.size) != list(canvas): res['fail'].append(f'canvas {im.size} != {canvas}')
    hidden = int(((al == 0) & (a[..., :3].max(-1) > 0)).sum()); res['rgb_under_zero_alpha_px'] = hidden
    if hidden: res['warn'].append('non-zero RGB under zero alpha (loaders must crop by alpha, not RGB)')
    # NOTE: body alpha in generated art is often 253-254, not 255, so 'opaque' means >= 245
    semi = ((al > 8) & (al < 245)).sum() / max(1, (al > 8).sum());  res['semi_transparent_share'] = round(float(semi), 4)
    if semi > .25: res['warn'].append('large semi-transparent share: haze or soft fringe')
    lab, n = ndimage.label(al > 8); sizes = ndimage.sum(np.ones_like(al), lab, range(1, n + 1)) if n else []
    big = sorted((int(s) for s in sizes if s >= min_blob), reverse=True); small = [int(s) for s in sizes if 20 <= s < min_blob]
    res['components'] = dict(total=int(n), large=big[:6], small_20_to_min=len(small))
    if len(big) > 1 and big[-1] < .02 * big[0]: res['warn'].append(f'tiny detached component(s) {big[1:]} vs main {big[0]}: possible stray blob')
    return res
if __name__ == '__main__':
    args = sys.argv[1:]; canvas = None; mb = 400
    if '--canvas' in args: i = args.index('--canvas'); canvas = [int(x) for x in args[i + 1].split('x')]; del args[i:i + 2]
    if '--min-blob' in args: i = args.index('--min-blob'); mb = int(args[i + 1]); del args[i:i + 2]
    bad = 0
    for f in args:
        r = check(f, canvas, mb); print(json.dumps(r)); bad += bool(r['fail'])
    sys.exit(1 if bad else 0)
