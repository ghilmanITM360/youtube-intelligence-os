"""Lens audit: per-asset measurements vs xkcd What-If lens (white plate, one line weight, anchors). Read-only."""
import csv, sys
from pathlib import Path
import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).parent))
from normalize import mint_bbox, MINT_H, MINT_TOP, AXIS
ROOT = Path(__file__).resolve().parents[2]
out = []
for r in csv.DictReader((ROOT/'assets/qa/review_selection.csv').open()):
    p = ROOT/r['filename']
    if not p.is_file(): out.append([r['asset_id'], 'MISSING']); continue
    im = Image.open(p); a = np.array(im.convert('RGBA')).astype(int)
    ink = (a[...,3] > 40) & (a[...,:3].sum(-1) < 600)
    nonwhite = ink.mean()
    ys, xs = np.nonzero(ink) if ink.any() else (np.array([0]), np.array([0]))
    row = dict(id=r['asset_id'], size=f'{im.size[0]}x{im.size[1]}', mode=im.mode, ink_pct=round(100*nonwhite,2),
               bbox=f'{xs.min()},{ys.min()},{xs.max()},{ys.max()}')
    if r['asset_id'][:5] in ('CHR-P','CHR-V','CHR-X') and im.mode == 'RGBA':
        try:
            x0,y0,x1,y1 = mint_bbox(im); row.update(head_h=y1-y0, head_top=y0, head_cx=round((x0+x1)/2))
            if r['asset_id'][4] in 'PV': row['feet_y']=int(ys.max()); row['shift_to_1102']=1102-int(ys.max())
            row['head_scale_needed']=round(MINT_H/(y1-y0),3)
        except Exception as e: row['head_err']=str(e)[:40]
    out.append(row)
keys = ['id','size','mode','ink_pct','bbox','head_h','head_top','head_cx','feet_y','shift_to_1102','head_scale_needed']
w = csv.DictWriter((ROOT/'assets/qa/audit_lens.csv').open('w'), keys, extrasaction='ignore'); w.writeheader()
for o in out:
    if isinstance(o, dict): w.writerow(o); print(' '.join(f'{k}={o.get(k)}' for k in keys if o.get(k) is not None))
