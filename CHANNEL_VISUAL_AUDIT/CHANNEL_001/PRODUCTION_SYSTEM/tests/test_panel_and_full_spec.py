import json, os, sys, unittest
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, H)
import render_scene as R

class PanelAndFullSpec(unittest.TestCase):
    def test_panel_shapes(self):
        im = R.draw_proc(dict(type='panel', w=100, h=60, fill=(255, 0, 0), label='x'), 0); self.assertEqual(im.size, (104, 64))
        ol = R.draw_proc(dict(type='panel', w=100, h=60, fill=None, outline=(0, 0, 255), outline_w=5, shape='ellipse'), 0)
        self.assertEqual(ol.getpixel((52, 32))[3], 0)            # outline-only: centre transparent
    def test_full_progress_spec_valid_and_contiguous(self):
        spec = json.load(open(os.path.join(H, 'specs', 'same_video_full_progress.json')))
        self.assertEqual(len(spec['shots']), 22); self.assertEqual(R.validate(spec), [])
        self.assertEqual(round(spec['shots'][-1]['start'] * 30 + spec['shots'][-1]['dur'] * 30), 1660)
    def test_no_unapproved_asset_refs_in_full_spec(self):
        spec = json.load(open(os.path.join(H, 'specs', 'same_video_full_progress.json')))
        for s in spec['shots']:
            for e in s['elements']:
                if 'asset' in e: self.assertTrue(e['asset'].startswith('asset:') or (e['asset'].startswith('shot_sprites/') and e['asset'] in SPRITES), e)   # registry ids, or a shot sprite listed in the validated manifest; never staging paths
SPRITES = set()
_m = os.path.join(H, 'shot_sprites', 'shot_sprites_manifest.json')
if os.path.exists(_m): SPRITES = {'shot_sprites/' + k + '.png' for k in json.load(open(_m))['sprites']}
class Boil(unittest.TestCase):
    def test_sh018_two_state_alternation_every_10_frames(self):
        spec = json.load(open(os.path.join(H, 'specs', 'same_video_full_progress.json'))); el = spec['shots'][17]['elements'][0]
        ts = [round(p['t'] * 30) for p in el['poses']]; self.assertEqual(ts, [0, 10, 20, 30, 40, 50])
        labs = [p['asset'] for p in el['poses']]; self.assertEqual(len(set(labs)), 2); self.assertTrue(all(labs[i] != labs[i + 1] for i in range(5)))
        for p in el['poses']: self.assertFalse(set(p) & {'opacity', 'keys', 'alpha'})   # source has no fade/flicker

if __name__ == '__main__': unittest.main()
