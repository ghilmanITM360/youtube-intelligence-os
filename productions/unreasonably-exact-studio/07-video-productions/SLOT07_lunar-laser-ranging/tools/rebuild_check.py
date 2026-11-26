#!/usr/bin/env python3
# usage: ~/.venvs/uepipe/bin/python tools/rebuild_check.py "$PWD" OUT_DIR TAG   (from the project root; writes only into OUT_DIR)
"""Rebuild check: render stills from the V3 scene code, compare with frames decoded from the locked clean render; log every file opened."""
import sys, os, json, subprocess, runpy
proj, out, tag = sys.argv[1], sys.argv[2], sys.argv[3]
opened = set()
def hook(ev, args):
    if ev == 'open' and isinstance(args[0], str): opened.add(os.path.realpath(args[0]))
sys.addaudithook(hook)
sys.path.insert(0, os.path.join(proj, 'animation')); os.chdir(proj)
sys.argv = ['roughcut.py']
import importlib.util
spec = importlib.util.spec_from_file_location('rc', os.path.join(proj, 'animation', 'roughcut.py')); rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
from uemotion.video import ClipSpec, render_frame
import numpy as np
from PIL import Image
rc.S.preload_real()
cspec = ClipSpec('CUT', 'SLOT07_V3_clean', 0.0, rc.DUR, rc.scene, captions=False, audio=False, blur=(3, 0.5))
times = [1.5, 3.0, 9.0, 14.0, 20.0, 30.0, 39.0, 42.0, 48.0, 55.0, 59.7, 62.0, 64.5, 69.0, 73.0, 77.0, 84.0, 90.0, 94.0]
res = []
clean = os.path.join(proj, 'renders/roughcut_v3/SLOT07_V3_clean.mp4')
for t in times:
    f = int(round(t * 30)); im = render_frame(cspec, f, 1.0, 30).convert('RGB'); p = os.path.join(out, '%s_%05d.png' % (tag, f)); im.save(p)
    ref = os.path.join(out, 'ref_%05d.png' % f)
    if not os.path.exists(ref):
        subprocess.run(['ffmpeg','-v','error','-y','-i',clean,'-vf','select=eq(n\\,%d)' % f,'-frames:v','1',ref], check=True)
    a = np.asarray(im, dtype=np.float32); b = np.asarray(Image.open(ref).convert('RGB'), dtype=np.float32)
    d = float(np.abs(a - b).mean()) if a.shape == b.shape else None
    res.append(dict(t=t, frame=f, mean_abs_diff=d)); print(t, f, d, flush=True)
json.dump(dict(results=res, opened=sorted(opened)), open(os.path.join(out, tag + '_report.json'), 'w'), indent=1)
