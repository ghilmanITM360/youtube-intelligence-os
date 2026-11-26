#!/usr/bin/env python3
"""Single entry point: render the code-only proof clips P07-P13 into ROOT/renders/proofs/<id>/ and write PROOF_REPORT.md.

  ~/.venvs/uepipe/bin/python animation/render_proofs.py                 # all proofs, 540x960 @30 fps, + reports
  ~/.venvs/uepipe/bin/python animation/render_proofs.py P11 P12         # selected proofs
  ~/.venvs/uepipe/bin/python animation/render_proofs.py --scale 1.0     # final 1080x1920 (proof folder gets *_1080 suffix)
  ~/.venvs/uepipe/bin/python animation/render_proofs.py --still P07 4.0 /tmp/f.png   # one frame (any scale)
  ~/.venvs/uepipe/bin/python animation/render_proofs.py --selftest      # unit checks of the primitives
"""
import argparse, importlib, os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'renders', 'proofs')
PROOFS = {'OPEN': 'opening', 'P01': 'p01', 'P02': 'p02', 'P03': 'p03', 'P04': 'p04', 'P05': 'p05', 'P06': 'p06', 'P07': 'p07', 'P08': 'p08', 'P09': 'p09', 'P10': 'p10', 'P11': 'p11', 'P12': 'p12', 'P13': 'p13'}

def load(pid): return importlib.import_module('proofs.' + PROOFS[pid])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ids', nargs='*'); ap.add_argument('--scale', type=float, default=0.5)
    ap.add_argument('--fps', type=int, default=30); ap.add_argument('--workers', type=int, default=None)
    ap.add_argument('--still', nargs=3, metavar=('ID', 'ANIM_T', 'PNG')); ap.add_argument('--clip', type=int, default=0, help='which clip of the proof for --still')
    ap.add_argument('--selftest', action='store_true'); ap.add_argument('--no-report', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        import selftest; return selftest.run()
    from uemotion import video
    if a.still:
        pid, t, png = a.still; spec = load(pid).specs()[a.clip]
        video.render_frame(spec, int(round(float(t) * a.fps)), a.scale, a.fps).save(png); print('wrote', png); return
    import report
    for pid in (a.ids or list(PROOFS)):
        mod = load(pid); out = os.path.join(OUT, pid if a.scale == 0.5 else pid + '_%d' % int(1080 * a.scale))
        os.makedirs(out, exist_ok=True); results = {}
        for spec in mod.specs():
            print('rendering', spec.name, flush=True); results[spec.name] = video.render_clip(spec, out, a.scale, a.fps, a.workers)
        checks = mod.check_all(out, results) if mod.check_all.__code__.co_argcount == 2 else mod.check_all(out)
        if not a.no_report: report.write(pid, mod, out, results, checks, a)
if __name__ == '__main__': main()
