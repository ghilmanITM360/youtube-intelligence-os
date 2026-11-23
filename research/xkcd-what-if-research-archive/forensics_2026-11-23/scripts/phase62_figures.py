"""Phase 6.2 character proportion proxy: stick-figure candidates = tall ink components (dilated 3x) whose top third contains one filled-hole disk (head ring; circularity>0.8, diameter 30-260 px).
Measures head diameter, figure height (component bbox), ratio, stroke. Candidates are drawn on an overlay sheet and ONLY those confirmed by eye are used for statements.
usage: uv run --no-project --with numpy --with pillow --with scipy --with scikit-image python scripts/phase62_figures.py"""
import csv, os, numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = list(csv.DictReader(open(A + '/06_STYLE_MEASUREMENTS_125.csv')))
out = []; tiles = []
for r in R:
    a = np.asarray(Image.open(A + '/' + r['frame_ref']).convert('RGB')).astype(np.int16); H, W, _ = a.shape
    bg = np.array([int(x) for x in r['bg_rgb'].split(',')]); nonbg = np.abs(a - bg).sum(2) > 60; mx = a.max(2); mn = a.min(2); sat = (mx - mn) / np.maximum(mx, 1); lum = a @ np.array([.299, .587, .114])
    ink = nonbg & (sat < .25) & ((lum > 150) if int(r['dark_bg']) else (lum < 110))
    ink = ndi.binary_closing(ink, iterations=1)
    filled = ndi.binary_fill_holes(ink); holes = filled & ~ink
    hl, nh = ndi.label(holes); comp, nc = ndi.label(ndi.binary_dilation(ink, iterations=3))
    found = []
    for i, sl in enumerate(ndi.find_objects(hl), 1):
        if sl is None: continue
        hh, ww = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start; area = (hl[sl] == i).sum()
        d = (hh + ww) / 2
        if not (22 <= d <= 240) or abs(hh - ww) > 0.25 * d or area < 0.7 * np.pi / 4 * hh * ww: continue
        cy, cx = (sl[0].start + sl[0].stop) // 2, (sl[1].start + sl[1].stop) // 2; cid = comp[cy, cx] or comp[sl[0].start, cx]
        if cid == 0: continue
        cs = ndi.find_objects((comp == cid).astype(int))[0]; fh, fw = cs[0].stop - cs[0].start, cs[1].stop - cs[1].start
        if fh > 1.5 * fw and fh < 0.97 * H and fh / d > 2.5 and cy < cs[0].start + 0.35 * fh and fh / d < 14:
            found.append((d, fh, fw, cs, (cy, cx)))
    # keep the largest candidate per distinct component
    seen = set(); keep = []
    for f in sorted(found, key=lambda x: -x[0]):
        k = (f[3][0].start, f[3][1].start)
        if k in seen: continue
        seen.add(k); keep.append(f)
    for d, fh, fw, cs, c in keep:
        out.append(dict(video_id=r['video_id'], t_s=r['t_s'], fmt=r['fmt'], head_diam_px=round(d, 1), figure_height_px=fh, figure_width_px=fw, height_over_head=round(fh / d, 2), frame_ref=r['frame_ref']))
    if keep and len(tiles) < 24:
        im = Image.open(A + '/' + r['frame_ref']).convert('RGB'); dr = ImageDraw.Draw(im)
        for d, fh, fw, cs, c in keep: dr.rectangle([cs[1].start, cs[0].start, cs[1].stop, cs[0].stop], outline=(255, 0, 255), width=4); dr.ellipse([c[1] - d / 2, c[0] - d / 2, c[1] + d / 2, c[0] + d / 2], outline=(0, 200, 255), width=4)
        s = 340 / im.width; tiles.append((im.resize((340, int(im.height * s))), f"{r['video_id']} {r['t_s']}"))
w = csv.DictWriter(open(A + '/06_FIGURE_CANDIDATES.csv', 'w', newline=''), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print(len(out), 'candidates in', len({(o['video_id'], o['t_s']) for o in out}), 'frames')
cols = 4; rows_ = (len(tiles) + cols - 1) // cols; Hh = max(t.height for t, _ in tiles) + 12
sh = Image.new('RGB', (340 * cols, Hh * rows_), 'white'); d = ImageDraw.Draw(sh)
for i, (t, c) in enumerate(tiles): x, y = (i % cols) * 340, (i // cols) * Hh; sh.paste(t, (x, y + 12)); d.text((x + 2, y), c, fill='black')
sh.save(A + '/phase62_style/figure_candidates_sheet.jpg', quality=85)
