#!/usr/bin/env python3
"""SLOT 07 V3 (V2 frozen in roughcut_v2.py, V1 in roughcut_v1.py): the whole 95.39 s V2 narration as one continuous film, assembled from the proof scenes + gap scenes.
One scene dispatches on narration time: each segment's scene gets its OWN clocks (anim/model time exactly as in its proof),
so every timing check made in a proof still holds in the cut. Crossfades are rendered (both scenes drawn, mixed), not faked.
Captions are drawn once for the whole film. Audio: the V2 master narration (read only), padded with silence to the end.

  ~/.venvs/uepipe/bin/python animation/roughcut.py            # 540x960 review render -> renders/roughcut/
  ~/.venvs/uepipe/bin/python animation/roughcut.py --still 33.0 /tmp/f.png
"""
import argparse, os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); ROOT = os.path.dirname(HERE)
from uemotion import tokens as T, space as S
from uemotion.timeline import ClockSet
from uemotion.video import ClipSpec, render_clip, render_frame
from uemotion.narration import MASTER_WAV, MASTER_DURATION
import render_proofs as RP
from proofs import gaps as G, opening as OP, common as K
from uemotion.easing import smoothstep, seg
S.INLINE_DISCLOSURES = False          # V3: no pills from the scenes; the film draws each necessary disclosure once, below

DUR = 96.0
# (start, end, source, crossfade-in seconds). source = proof id (its first clip unless 'ID:k') or a gap scene.
CUT = [(0.00, 9.70, 'P03', 0.0), (9.70, 11.47, G.g05, 0.45), (11.47, 17.55, 'P11', 0.30), (17.55, 26.20, 'P08', 0.25),
       (26.20, 38.03, G.g12, 0.35), (38.03, 40.08, 'P13', 0.30), (40.08, 44.30, 'P06', 0.30), (44.30, 51.01, 'P13', 0.35), (51.01, 60.44, G.g22, 0.40), (60.44, 63.53, 'P09', 0.30),
       (63.53, 65.55, 'P10', 0.30), (65.55, 67.45, 'P09', 0.30), (67.45, 70.95, G.g29, 0.35), (70.95, 75.04, 'P10', 0.35), (75.04, 81.62, G.g30, 0.35), (81.62, 88.09, 'P12', 0.30), (88.09, DUR, G.g37, 0.40)]

# V3 disclosure table: (start, end, text, xy, anchor). One small sentence-case note when a model sequence begins, attached to the
# object where that helps (slowed playback sits under the stopwatch). Audit: renders/roughcut_v3/ON_SCREEN_TEXT_AUDIT.csv
SWX, SWY = K.SW_C[0], K.SW_C[1] + K.SW_R + 128
DISCLOSURES = [
    (OP.T_LAUNCH + 0.15, OP.T_ARRIVE + 0.45, 'Real speed', (60, 150), 'lm'),
    (11.75, 15.2, 'Not to scale', (60, 150), 'lm'),
    (13.75, 17.3, 'Slowed down', (SWX, SWY), 'mm'),
    (22.0, 25.9, 'Slowed down', (SWX, SWY), 'mm'),
    (45.95, 48.6, 'Simplified diagram', (60, 150), 'lm'),
    (G.SCH1, 60.3, 'Not to scale', (60, 150), 'lm'),
    (60.75, 63.4, 'Simulated data', (60, 150), 'lm'),
    (67.6, 70.85, 'Effect greatly exaggerated', (60, 150), 'lm'),
    (71.15, 73.6, 'Simulated data', (60, 150), 'lm'),
    (78.5, 81.2, 'Not to scale', (60, 150), 'lm'),
    (G.N_HANG + 0.5, G.N_EACH + 0.4, 'Orbit simplified', (60, 150), 'lm')]
def draw_disclosures(cv, n):
    for a, b, txt, xy, anc in DISCLOSURES:
        al = smoothstep(seg(n, a, a + 0.3)) * (1 - smoothstep(seg(n, b - 0.3, b)))
        if al > 0: S.disclosure(cv, txt, xy, al, anc)

def _resolve():
    segs = []
    for a, b, src, xf in CUT:
        if callable(src): spec = ClipSpec('GAP', src.__name__, a, b - a, src); name = 'gap:' + src.__name__
        else:
            pid, k = (src.split(':') + ['0'])[:2]; spec = RP.load(pid).specs()[int(k)]; name = '%s (%s)' % (pid, spec.name)
        segs.append(dict(a=a, b=b, spec=spec, xf=xf, name=name, clocks=ClockSet(spec.n0, spec.model)))
    return segs
SEGS = None

def _draw(cv, seg, n, ctx):
    sub = seg['clocks'].at(n - seg['spec'].n0, frame=ctx.frame, fps=ctx.fps, scale=ctx.scale)
    seg['spec'].scene(cv, sub)

def scene(cv, ctx):
    global SEGS
    if SEGS is None: SEGS = _resolve()
    n = ctx.n
    i = max(k for k, s in enumerate(SEGS) if n >= s['a'] - 1e-9) if n >= 0 else 0
    cur = SEGS[i]
    if i > 0 and cur['xf'] > 0 and n < cur['a'] + cur['xf']:       # crossfade from the previous segment (it keeps running)
        _draw(cv, SEGS[i - 1], n, ctx)
        with cv.group((n - cur['a']) / cur['xf']): _draw(cv, cur, n, ctx)
    else: _draw(cv, cur, n, ctx)
    draw_disclosures(cv, n)
    return {}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--still', nargs=2); ap.add_argument('--range', nargs=2, type=float, help='re-render a frame-aligned patch [a, b) for splicing'); ap.add_argument('--scale', type=float, default=0.5); a = ap.parse_args()
    S.preload_real()
    spec = ClipSpec('CUT', 'SLOT07_V3_clean', 0.0, DUR, scene, captions=False,      # V2: captions are burned in a separate pass (tools/captions_v2.py)
                    audio=False, blur=(3, 0.5),
                    cues={'%02d_%s' % (k, (c[2] if isinstance(c[2], str) else c[2].__name__)): c[0] + 0.6 for k, c in enumerate(CUT)})
    if a.range:
        r0, r1 = a.range; pspec = ClipSpec('CUT', 'PATCH_%06.2f_%06.2f' % (r0, r1), r0, r1 - r0, scene, captions=False, audio=False, blur=(3, 0.5))
        print(render_clip(pspec, os.path.join(ROOT, 'renders', 'roughcut_v3', 'patches'), a.scale, 30)['mp4']); return
    if a.still:
        render_frame(spec, int(round(float(a.still[0]) * 30)), a.scale, 30).save(a.still[1]); print('wrote', a.still[1]); return
    out = os.path.join(ROOT, 'renders', 'roughcut_v3'); res = render_clip(spec, out, a.scale, 30)
    final = os.path.join(out, 'SLOT07_V3_clean_with_narration.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', res['mp4'], '-i', MASTER_WAV, '-filter_complex', '[1:a]apad=whole_dur=%.3f[a]' % DUR,
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', '%.3f' % DUR, final], check=True)
    print('wrote', final, 'frames', res['frames'], 'diff max %.1f' % res['diff_max'])

if __name__ == '__main__': main()
