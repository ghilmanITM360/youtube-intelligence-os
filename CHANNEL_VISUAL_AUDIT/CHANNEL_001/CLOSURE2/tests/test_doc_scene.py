import sys, os, copy, hashlib, tempfile, unittest
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path
V1 = str(Path(__file__).resolve().parents[4] / 'productions/new-original-video-v1-rent-01')
sys.path.insert(0, V1 + '/tools')
import doc_scene as ds

TMP = tempfile.mkdtemp(); PNG = os.path.join(TMP, 'doc.png')
im = Image.new('RGB', (1000, 1400), 'white'); d = ImageDraw.Draw(im)
for i in range(30): d.text((60, 100 + i * 40), f'line {i} some words and 12.5 numbers', fill='black')
d.rectangle([70, 303, 78, 311], fill=(255, 0, 255)); im.save(PNG); SHA = hashlib.sha256(open(PNG, 'rb').read()).hexdigest()
VP = {'x': 100, 'y': 40, 'w': 1600, 'h': 900}   # 16:9
def spec():
    return {'source': {'file': 'doc.png', 'sha256': SHA, 'url': 'https://x.gov/a', 'publisher': 'Agency', 'title': 'T', 'published': '2023-01-01', 'retrieved': '2026-11-22', 'rights': 'US federal work', 'claim_ids': ['C1']},
            'viewport': VP, 'timing': {'legible_s': 0.5}, 'duration_s': 6,
            'camera': [{'t': 0, 'crop': [0, 200, 800, 450]}, {'t': 2, 'crop': [0, 200, 800, 450]}, {'t': 4, 'crop': [100, 500, 500, 281.25]}],
            'annotations': [{'id': 'A1', 'kind': 'highlight', 'mode': 'progressive', 'rect': [60, 300, 300, 20], 'start_s': 1.0, 'complete_s': 2.0, 'passage': 'line 5', 'claim_id': 'C1'},
                            {'id': 'A2', 'kind': 'ellipse', 'mode': 'instant', 'rect': [120, 540, 200, 20], 'start_s': 1.5, 'complete_s': 1.5, 'passage': 'line 11', 'claim_id': 'C1'}]}
def render(s, t): return ds.render_layer(s, t, TMP)
def yellow(img):
    a = np.array(img.convert('RGB')).astype(int); m = (a[..., 0] > 230) & (a[..., 1] > 200) & (a[..., 2] < 200) & (a[..., 2] > 40) ; return m
def red(img):
    a = np.array(img.convert('RGB')).astype(int); return (a[..., 0] > 190) & (a[..., 1] < 80) & (a[..., 2] < 80)

class Doc(unittest.TestCase):
    def test_valid(self): self.assertEqual(ds.validate_spec(spec(), TMP), (1000, 1400))
    def bad(self, mut, frag):
        s = spec(); mut(s)
        with self.assertRaises(ds.SpecError) as e: ds.validate_spec(s, TMP)
        self.assertIn(frag, str(e.exception))
    def test_sha_mismatch(self): self.bad(lambda s: s['source'].update(sha256='0' * 64), 'checksum')
    def test_missing_provenance(self): self.bad(lambda s: s['source'].pop('rights'), 'source.rights')
    def test_distorting_crop(self): self.bad(lambda s: s['camera'][0].update(crop=[0, 200, 800, 300]), 'distort')
    def test_mark_before_legible(self): self.bad(lambda s: s['annotations'][0].update(start_s=0.2, complete_s=1.0), 'before the passage is legible')
    def test_geometry_outside_doc(self): self.bad(lambda s: s['annotations'][1].update(rect=[900, 540, 400, 20]), 'outside the document')
    def test_target_not_visible(self): self.bad(lambda s: s['annotations'][1].update(rect=[120, 1200, 200, 20]), 'outside the visible crop')
    def test_context_hidden_by_crop(self):
        self.bad(lambda s: s.update(required_context=[{'rect': [60, 250, 100, 20], 'why': 'unit qualifier', 'annotation': 'A1'}], camera=[{'t': 0, 'crop': [0, 280, 800, 450]}]), 'hidden by crop')
    def test_instant_mode_requires_equal_times(self): self.bad(lambda s: s['annotations'][1].update(complete_s=2.0), 'instant needs')
    def test_claim_not_in_source(self): self.bad(lambda s: s['annotations'][0].update(claim_id='C9'), 'not among source.claim_ids')
    def test_onset_frame_exact(self):
        s = spec(); fps = 24
        before = render(s, 1.5 - 1 / fps); at = render(s, 1.5)
        self.assertEqual(int(red(before).sum()), 0); self.assertGreater(int(red(at).sum()), 200)   # complete ellipse in ONE frame
    def test_progressive_is_monotone(self):
        s = spec(); n = [int(yellow(render(s, t)).sum()) for t in (1.0, 1.25, 1.5, 1.75, 2.0)]
        self.assertTrue(all(b >= a for a, b in zip(n, n[1:])) and n[-1] > n[0] * 3, n)
    def test_registration_through_zoom(self):
        s = spec(); s['annotations'][0].update(start_s=0.6, complete_s=0.7, exit_s=None); s['annotations'][0]['mode'] = 'progressive'
        r = s['annotations'][0]['rect']
        for t in (1.0, 2.0, 3.0, 3.99):   # before, during and after the camera move
            crop = ds.crop_at(s, t); (x0, y0) = ds.to_view(s, crop, (r[0], r[1])); (x1, y1) = ds.to_view(s, crop, (r[0] + r[2], r[1] + r[3]))
            m = yellow(render(s, t)); ys, xs = np.nonzero(m)
            if t >= 3.0:   # target still inside the (tighter) crop? only assert when visible
                if not (x0 >= 0 and y0 >= 0 and x1 <= VP['w'] and y1 <= VP['h']): continue
            self.assertGreater(len(xs), 100)
            cx, cy = (xs.min() + xs.max()) / 2 - VP['x'], (ys.min() + ys.max()) / 2 - VP['y']  # bbox centre (text pixels inside the mark are not yellow)
            self.assertLess(abs(cx - (x0 + x1) / 2), 6, (t, cx, (x0 + x1) / 2)); self.assertLess(abs(cy - (y0 + y1) / 2), 6, (t, cy))
    def test_image_and_annotation_share_one_transform(self):
        s = spec()
        for t in (0.5, 2.5, 3.0, 3.9):
            crop = ds.crop_at(s, t); ex, ey = ds.to_view(s, crop, (74, 307))   # where the magenta dot must land
            a = np.array(render(s, t).convert('RGB')).astype(int); m = ((a[..., 0] > 230) & (a[..., 1] > 80) & (a[..., 1] < 125) & (a[..., 2] > 125) & (a[..., 2] < 165)) | ((a[..., 0] > 200) & (a[..., 1] < 60) & (a[..., 2] > 200))  # magenta, plain or under the 43% yellow
            ys, xs = np.nonzero(m)
            if crop[0] <= 74 <= crop[0] + crop[2] and crop[1] <= 307 <= crop[1] + crop[3]:
                self.assertGreater(len(xs), 20, t); self.assertLess(abs((xs.min() + xs.max()) / 2 - VP['x'] - ex), 3, t); self.assertLess(abs((ys.min() + ys.max()) / 2 - VP['y'] - ey), 3, t)
    def test_layer_clipped_to_viewport(self):
        a = np.array(render(spec(), 1.8))[..., 3]; ys, xs = np.nonzero(a[:VP['y'] + VP['h'] + 4])
        self.assertGreaterEqual(xs.min(), VP['x'] - 2); self.assertLessEqual(xs.max(), VP['x'] + VP['w'] + 2)
    def test_event_table_is_frame_addressable(self):
        ev = dict((k, f) for k, t, f in ds.event_table(spec())); self.assertEqual(ev['A2:onset'], 36); self.assertEqual(ev['A2:complete'], 36)
    def test_integrates_with_existing_renderer_and_does_not_change_it(self):
        sys.path.insert(0, V1 + '/tools'); import v1r4_render as r
        it = ds.document_item(spec(), 10.0, TMP); self.assertEqual(it.mode, 'dyn')
        cv = Image.new('RGB', (r.W, r.H), r.BG); r.paste_pop(cv, it, 12.0)
        self.assertGreater(int(yellow(cv).sum()), 0)
        cv2 = Image.new('RGB', (r.W, r.H), r.BG); r.paste_pop(cv2, it, 9.0)   # before t0: nothing drawn
        self.assertEqual(np.array(cv2).min(), 253)

if __name__ == '__main__': unittest.main()
