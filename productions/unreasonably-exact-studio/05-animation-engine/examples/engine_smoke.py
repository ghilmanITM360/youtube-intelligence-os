import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uemotion import tokens as T, space as S, stopwatch as SW
from uemotion.video import ClipSpec, render_frame
from uemotion.camera import starfield
def scene(cv, ctx):
    S.draw_sphere(cv, (540, 1300), 330, 'earth'); S.draw_sphere(cv, (800, 420), 110, 'moon')
    SW.draw_stopwatch(cv, (300, 520), value=1.28, full=3.0); S.disclosure(cv, 'Not to scale', (60, 150), 1.0, 'lm')
    return {}
S.preload_real()
spec = ClipSpec('SMOKE', 'engine_smoke', 0.0, 1.0, scene, captions=False, audio=False)
render_frame(spec, 0, 0.5, 30).save(sys.argv[1]); print('ok', sys.argv[1])
