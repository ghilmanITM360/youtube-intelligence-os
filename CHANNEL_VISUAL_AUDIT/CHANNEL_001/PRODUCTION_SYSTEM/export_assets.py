"""Export the existing Pillow-drawn originals to transparent PNGs + registry (asset library v0, code-drawn, LEVEL-3).
Each PNG is cropped to its alpha bbox; registry stores the anchor (centre) so scene specs place by centre."""
import importlib.util, json, os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
spec = importlib.util.spec_from_file_location('r6', os.path.join(HERE, '..', 'RECONSTRUCTION_TESTS', 'same_video', 'render_10nEByVLya0_v6.py'))
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
class TCv(R.Cv):                       # transparent canvas, same drawing API
    def __init__(s):
        s.im = Image.new('RGBA', (R.W * R.SS, (R.Y1 - R.Y0) * R.SS), (0, 0, 0, 0)); s.d = R.ImageDraw.Draw(s.im)
    def out(s): return s.im.resize((R.W, R.Y1 - R.Y0), Image.LANCZOS)
reg = []
def save(aid, fn, kind, **meta):
    c = TCv(); fn(c); im = c.out(); bb = im.getchannel('A').point(lambda a: 255 if a > 8 else 0).getbbox()
    im = im.crop(bb); im.save(os.path.join(HERE, 'assets', aid + '.png'))
    reg.append(dict(id=aid, file='assets/%s.png' % aid, type=kind, size=im.size, bbox_in_frame=[bb[0], bb[1] + R.Y0, bb[2], bb[3] + R.Y0],
                    transparent=True, provenance='original, drawn in Pillow (export_assets.py)', level=3, validation='NOT_REVIEWED', **meta))
Y = 880
save('prop_qcircle', lambda c: R.qmark(c, 540, Y, 105), 'prop')
save('prop_chart_screen', lambda c: R.chart2(c, 540, Y, 420, 330), 'prop')
save('prop_moneybag_pair', lambda c: (R.bag(c, 520, Y, 1.4), R.bag(c, 575, Y + 8, 1.4)), 'prop')
save('prop_dollar', lambda c: R.dollar(c, 540, Y), 'prop')
save('prop_earth', lambda c: R.earth(c, 540, Y, 222), 'prop')
for face in ('neutral', 'worried', 'happy'):
    for arms in ('shrug', 'down', 'up'):
        save('char_stick_%s_%s' % (face, arms), lambda c, f=face, a=arms: R.stick(c, 540, 770, f, a), 'character', character='stick_man', face=face, arms=arms)
json.dump(reg, open(os.path.join(HERE, 'asset_registry.json'), 'w'), indent=1)
print(len(reg), 'assets')
