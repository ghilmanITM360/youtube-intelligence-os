"""Frame-by-frame review strips from the FINAL captioned MP4: 6 consecutive frames around every shot cut and
around the critical animation moments. Writes qa/frames_critical/*.png (one strip per moment) + index.csv.
  .venv/bin/python tools/frame_strips.py
"""
import csv, subprocess, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
ns = {'__file__': str(Path(__file__).with_name('v15.py')), '__name__': 'strips'}
exec(open(Path(__file__).with_name('v15.py')).read(), ns)
ROOT = ns['ROOT']; unwarp = ns['unwarp']; FPS = 24
OUT = ROOT / 'qa/frames_critical'; OUT.mkdir(parents=True, exist_ok=True)
SRC = ROOT / 'SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4'
moments = [(f'cut_{a["id"]}', unwarp(a['start'])) for a in ns['SHOT_OBJS'][1:]]
moments += [('weight_draws_on', unwarp(5.5)), ('forearm_lift', unwarp(8.45)), ('head_snap', unwarp(11.2)), ('drag_grows_E1', unwarp(19.4)),
            ('bars_equal', unwarp(43.4)), ('drag_passes_weight', unwarp(43.8)), ('lens_opens', unwarp(44.2)), ('net_arrow_on_body', unwarp(44.7)),
            ('trail_net_force', unwarp(49.55)), ('needle_drops', unwarp(55.6)), ('end_card', 109.6)]
rows = []
for name, t in moments:
    f0 = max(0, round(t * FPS) - 3)
    p = OUT / f'{name}.png'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(SRC), '-vf', f"select='between(n,{f0},{f0 + 5})',scale=270:480,tile=6x1",
                    '-frames:v', '1', '-fps_mode', 'passthrough', str(p)], check=True)
    rows.append(dict(moment=name, film_time=round(t, 3), first_frame=f0, last_frame=f0 + 5, strip=p.name))
with open(OUT / 'index.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'strips ->', OUT)
