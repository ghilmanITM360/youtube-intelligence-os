"""Caption collision check. For every caption cue (start, middle, end), render the picture and the caption overlay,
dilate the caption boxes by 6 px, and count picture pixels inside that zone that belong to the science graphics
(weight orange, drag teal, net violet, velocity blue, graph ink). Also reports caption box top/bottom on 1080x1920.
  .venv/bin/python tools/caption_qa.py   -> qa/caption_qa.csv (status FLAG if > 40 graphic pixels under a caption)
"""
import csv, io, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
ns = {'__file__': str(Path(__file__).with_name('v15.py')), '__name__': 'capqa'}
exec(open(Path(__file__).with_name('v15.py')).read(), ns)
import numpy as np
from PIL import Image, ImageFilter
ROOT = ns['ROOT']; rgb = ns['rgb']
PAL = np.array([[c * 255 for c in rgb(h)] for h in (ns['WEIGHT'], ns['DRAG'], ns['NET'], ns['VEL'])])
def arr(surf):
    b = io.BytesIO(); surf.write_to_png(b); b.seek(0); return Image.open(b).convert('RGBA')
rows = []
for i, q in enumerate(ns['CUES']):
    for tag, t in (('start', q['start'] + .1), ('mid', (q['start'] + q['end']) / 2), ('end', q['end'] - .1)):
        cap = arr(ns['caption_surface'](t)).getchannel('A')
        if not cap.getbbox(): continue
        x0, y0, x1, y1 = cap.getbbox()
        zone = np.array(cap.point(lambda a: 255 if a > 10 else 0).filter(ImageFilter.MaxFilter(13))) > 0
        pic = np.array(arr(ns['frame_surface'](t)).convert('RGB')).astype(float)
        d = np.min(np.linalg.norm(pic[:, :, None, :] - PAL[None, None], axis=3), axis=2)
        hits = int(((d < 38) & zone).sum())
        rows.append(dict(cue=i + 1, text=q['text'], when=tag, t=round(t, 2), box_top_px=y0, box_bottom_px=y1,
                         bottom_margin_px=1920 - y1, graphic_px_under_caption=hits, status='FLAG' if hits > 40 else 'ok'))
with open(ROOT / 'qa/caption_qa.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
flags = [r for r in rows if r['status'] == 'FLAG']
print(f"{len(rows)} samples over {len(ns['CUES'])} cues; box bottom range {min(r['box_bottom_px'] for r in rows)}-{max(r['box_bottom_px'] for r in rows)} px; "
      f"min bottom margin {min(r['bottom_margin_px'] for r in rows)} px; flags {len(flags)}")
for r in flags: print('FLAG', r['cue'], r['t'], r['graphic_px_under_caption'], r['text'])
