import hashlib, json, os, sys, unittest
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SP = os.path.join(H, 'shot_sprites')
class ShotSprites(unittest.TestCase):
    def test_manifest_hashes_and_review(self):
        m = json.load(open(os.path.join(SP, 'shot_sprites_manifest.json')))
        self.assertGreaterEqual(len(m['sprites']), 10)
        for n, e in m['sprites'].items():
            self.assertEqual(hashlib.sha256(open(os.path.join(SP, n + '.png'), 'rb').read()).hexdigest(), e['sha256'], n)
            self.assertIn(e['review_verdict'], ('PASS', 'PARTIAL'))
    def test_hips_validated_against_every_source_frame(self):
        v = json.load(open(os.path.join(SP, 'validation', 'hips_validation.json')))
        self.assertEqual({r['shot'] for r in v}, {'SH008', 'SH010', 'SH012', 'SH015'})
        for r in v: self.assertGreaterEqual(r['src_within3_min'], .95); self.assertGreaterEqual(r['sprite_within3_min'], .95)
    def test_earth_states_validated(self):
        v = json.load(open(os.path.join(SP, 'validation', 'earth_validation.json')))['summary']
        for s in 'AB': self.assertGreaterEqual(v[s]['src_ink_in3'], .95); self.assertGreaterEqual(v[s]['orange'], .9)
    def test_sprites_have_alpha_and_expected_size(self):
        from PIL import Image
        meta = json.load(open(os.path.join(SP, 'sprites_meta.json')))
        for n, m in meta.items():
            im = Image.open(os.path.join(SP, n + '.png')); self.assertEqual(im.mode, 'RGBA'); self.assertEqual(im.size, (m['w'], m['h']))
if __name__ == '__main__': unittest.main()
