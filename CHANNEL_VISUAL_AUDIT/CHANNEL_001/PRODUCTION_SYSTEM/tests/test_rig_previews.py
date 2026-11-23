"""Engineering tests on the ACTUAL staged rig/earth previews (read-only). PASS here = mechanically sound, NOT artistic approval.
python3 -W ignore -m unittest tests.test_rig_previews -v"""
import json, os, sys, unittest
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import render_scene as R
from PIL import Image, ImageFilter
QA = os.path.join(R.HERE, 'assets_codex', 'qa')
W, H = 1080, 1920


def spec(n): return json.load(open(os.path.join(QA, n)))


def layer_mask(el, t):
    """screen-space alpha mask (H,W) of one element at time t, via the real renderer path"""
    r = R.render_element(el, t, t)
    if r is None: return np.zeros((H, W), bool), None
    img, cx, cy = r; base = Image.new('RGBA', (W, H), (0, 0, 0, 0)); R.paste_clip(base, img, cx, cy)
    return np.asarray(base.getchannel('A')) > 8, base


def touches(a, b, px=3):
    d = Image.fromarray((a * 255).astype('uint8')).filter(ImageFilter.MaxFilter(2 * px + 1))
    return bool(((np.asarray(d) > 0) & b).any())


def bbox(m):
    ys, xs = np.nonzero(m); return (xs.min(), ys.min(), xs.max(), ys.max()) if len(xs) else None


@unittest.skipUnless(os.path.exists(os.path.join(QA, 'character_rig_preview.json')), 'staging preview absent')
class CharacterRig(unittest.TestCase):
    SPEC = 'character_rig_preview.json'

    @classmethod
    def setUpClass(cls):
        cls.s = spec(cls.SPEC); cls.els = {e['id']: e for e in cls.s['shots'][0]['elements']}
        cls.times = [p['t'] for p in cls.els['arm_left']['poses']]; cls.pose = ['down', 'shrug', 'up', 'point', 'hips']

    def m(self, i, t): return layer_mask(self.els[i], t)[0]

    def test_layer_order(self):
        L = {i: e['layer'] for i, e in self.els.items()}; self.assertTrue(L['legs'] < L['arm_left'] == L['arm_right'] < L['torso'] < L['head'], L)

    def test_head_neck_alignment(self):
        t = 0.0; head, torso = self.m('head', t), self.m('torso', t); hb, tb = bbox(head), bbox(torso)
        self.assertTrue(touches(head, torso, 3), 'head and torso do not meet at the neck: head %s torso %s' % (hb, tb))
        neck_x = (hb[0] + hb[2]) / 2; self.assertLess(abs(neck_x - (tb[0] + tb[2]) / 2), 8, 'head/neck x offset')

    def test_hips_alignment(self):
        legs, torso = self.m('legs', 0), self.m('torso', 0); self.assertTrue(touches(legs, torso, 3), 'legs do not meet torso at hip')
        lb, tb = bbox(legs), bbox(torso); self.assertLess(abs((lb[0] + lb[2]) / 2 - (tb[0] + tb[2]) / 2), 8)

    def test_shoulder_pivots_and_arm_switching(self):
        for side in ('arm_left', 'arm_right'):
            for k, t in enumerate(self.times):
                a, torso = self.m(side, t + .01), self.m('torso', 0)
                self.assertTrue(a.any(), '%s %s empty' % (side, self.pose[k])); self.assertTrue(touches(a, torso, 3), '%s %s detached from torso at the shoulder' % (side, self.pose[k]))
            sets = {self.els[side]['poses'][k]['asset'] for k in range(5)}; self.assertEqual(len(sets), 5, 'pose switching must use 5 distinct arm layers')

    def test_left_right_sides(self):
        for k, t in enumerate(self.times):
            l, r = bbox(self.m('arm_left', t + .01)), bbox(self.m('arm_right', t + .01)); self.assertLess((l[0] + l[2]) / 2, (r[0] + r[2]) / 2, self.pose[k])

    @unittest.expectedFailure  # KNOWN ART DEFECT (rig_arm_right_up exits top of canvas); unexpected success = Codex fixed it, remove this marker
    def test_no_clipping_inside_frame_and_canvas(self):
        for side in ('arm_left', 'arm_right'):
            for k, p in enumerate(self.els[side]['poses']):
                a = np.asarray(Image.open(os.path.join(R.HERE, p['asset'])).getchannel('A')) > 8
                self.assertFalse(a[0].any(), '%s %s: arm content on top canvas row (clipped by canvas)' % (side, self.pose[k]))

    def test_alpha_edges_no_halo(self):
        for i in ('legs', 'torso', 'arm_left'):
            im = np.asarray(Image.open(os.path.join(R.HERE, self.els[i]['asset'])).convert('RGBA')).astype(float); a = im[..., 3]
            e = (a > 20) & (a < 235); self.assertGreater(e.sum(), 50, i + ': no anti-aliased edge at all (hard edges)')
            self.assertLess(im[..., :3][e].mean(), 90, i + ': bright halo/fringe on edge pixels')

    def test_expression_switching_changes_only_face(self):
        poses = self.els['head']['poses']; base = np.asarray(Image.open(os.path.join(R.HERE, poses[0]['asset'])).convert('RGBA')).astype(int)
        bb = bbox(base[..., 3] > 8)
        for p in poses[1:]:
            o = np.asarray(Image.open(os.path.join(R.HERE, p['asset'])).convert('RGBA')).astype(int)
            self.assertTrue((o[..., 3] == base[..., 3]).all(), 'alpha differs between expressions')
            d = np.abs(o - base).sum(-1) > 30; self.assertTrue(d.any(), p['asset'] + ' identical to neutral'); db = bbox(d)
            fw, fh = bb[2] - bb[0], bb[3] - bb[1]
            self.assertTrue(db[1] > bb[1] + .3 * fh and db[3] < bb[3] - .05 * fh and db[0] > bb[0] + .15 * fw and db[2] < bb[2] - .15 * fw, '%s: edits leak outside face zone %s' % (p['asset'], db))

    def test_pose_transition_is_a_clean_cut_on_the_scheduled_frame(self):
        el = self.els['arm_left']; t = el['poses'][1]['t']; f = int(round(t * 30))
        a, b, c = [layer_mask(el, x / 30)[0] for x in (f - 1, f, f + 1)]
        self.assertTrue((a != b).any() and (b == c).all(), 'arm pose did not switch exactly on frame %d' % f)


@unittest.skipUnless(os.path.exists(os.path.join(QA, 'earth_preview.json')), 'staging preview absent')
class EarthRig(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.els = {e['id']: e for e in spec('earth_preview.json')['shots'][0]['elements']}

    def test_face_inside_and_centred_on_globe(self):
        body, face = layer_mask(self.els['body'], 1.5)[0], layer_mask(self.els['face'], 1.5)[0]; b, f = bbox(body), bbox(face)
        self.assertTrue(b[0] <= f[0] and f[2] <= b[2] and b[1] <= f[1] and f[3] <= b[3], 'face outside globe')
        self.assertLess(abs((f[0] + f[2]) / 2 - (b[0] + b[2]) / 2), .05 * (b[2] - b[0]), 'face off-centre horizontally')

    def test_sweat_variant_registers_with_neutral(self):
        n = bbox(np.asarray(Image.open(os.path.join(QA, 'earth_draft/earth_face_neutral_draft.png')).getchannel('A')) > 8); s = bbox(np.asarray(Image.open(os.path.join(QA, 'earth_draft/earth_face_sweat_draft.png')).getchannel('A')) > 8)
        self.assertLess(abs((n[0] + n[2]) / 2 - (s[0] + s[2]) / 2), 80); self.assertLess(abs(n[3] - s[3]), 80)

    def test_flames_hidden_then_overlay_globe_bottom(self):
        fl = self.els['flames']; self.assertFalse(layer_mask(fl, 1.0)[0].any(), 'flames visible before their cue')
        f = layer_mask(fl, 2.6)[0]; b = bbox(layer_mask(self.els['body'], 2.6)[0]); fb = bbox(f)
        self.assertTrue(fb[1] < b[3] < fb[3], 'flames do not straddle the globe bottom edge'); self.assertGreaterEqual(fb[0], b[0] - 30); self.assertLessEqual(fb[2], b[2] + 30)


@unittest.skipUnless(os.path.exists(os.path.join(QA, 'character_correction_preview.json')), 'correction preview absent')
class CorrectedCharacterRig(CharacterRig):
    """Same mechanical checks on the corrected (contract v2) rig; no expected failures remain (arm no longer clipped)."""
    SPEC = 'character_correction_preview.json'

    def test_no_clipping_inside_frame_and_canvas(self):
        for side in ('arm_left', 'arm_right'):
            for k, p in enumerate(self.els[side]['poses']):
                a = np.asarray(Image.open(os.path.join(R.HERE, p['asset'])).getchannel('A')) > 8
                self.assertFalse(a[0].any() or a[-1].any() or a[:, 0].any() or a[:, -1].any(), '%s %s clipped by canvas' % (side, self.pose[k]))
                m = self.m(side, self.els[side]['poses'][k]['t'] + .01); b = bbox(m); self.assertTrue(b[0] > 0 and b[1] > 0 and b[2] < W - 1 and b[3] < H - 1, '%s %s clipped by frame' % (side, self.pose[k]))

    def test_arm_pose_layers_are_pairwise_distinct_per_side(self):
        for side in ('arm_left', 'arm_right'):
            hs = [__import__('hashlib').sha256(open(os.path.join(R.HERE, p['asset']), 'rb').read()).hexdigest() for p in self.els[side]['poses']]
            self.assertEqual(len(set(hs)), 5, side + ' has byte-identical pose layers')


@unittest.skipUnless(os.path.exists(os.path.join(QA, 'character_independent_arm_preview.json')), 'independent-arm preview absent')
class IndependentArmPreview(unittest.TestCase):
    def test_left_and_right_arm_switch_at_different_times(self):
        els = {e['id']: e for e in spec('character_independent_arm_preview.json')['shots'][0]['elements']}
        tl, tr = [p['t'] for p in els['arm_left']['poses']], [p['t'] for p in els['arm_right']['poses']]
        self.assertNotEqual(tl, tr); self.assertTrue(set(tl[1:]).isdisjoint(tr[1:]), 'arms switch on the same frames: not independent')
        f = int(round(tl[1] * 30)); l0, l1 = layer_mask(els['arm_left'], (f - 1) / 30)[0], layer_mask(els['arm_left'], f / 30)[0]
        r0, r1 = layer_mask(els['arm_right'], (f - 1) / 30)[0], layer_mask(els['arm_right'], f / 30)[0]
        self.assertTrue((l0 != l1).any(), 'left arm did not change'); self.assertTrue((r0 == r1).all(), 'right arm changed with the left')


@unittest.skipUnless(os.path.exists(os.path.join(QA, 'earth_correction_preview.json')), 'correction preview absent')
class CorrectedEarth(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.els = {e['id']: e for e in spec('earth_correction_preview.json')['shots'][0]['elements']}

    def test_layer_order_and_shared_placement(self):
        self.assertEqual([self.els[i]['layer'] for i in ('body', 'face', 'flame_left', 'flame_right')], [0, 1, 2, 3])
        self.assertEqual({(e['x'], e['y'], e['scale']) for e in self.els.values()}, {(540, 960, 0.32)}, 'layers must share one origin/scale')

    def test_face_inside_globe_and_sweat_registers(self):
        b = bbox(layer_mask(self.els['body'], 1.5)[0])
        for t in (0.5, 1.5):
            f = bbox(layer_mask(self.els['face'], t)[0]); self.assertTrue(b[0] <= f[0] and f[2] <= b[2] and b[1] <= f[1] and f[3] <= b[3], 'face outside globe at t=%s' % t)
        n, sw = [bbox(layer_mask(self.els['face'], t)[0]) for t in (0.5, 1.5)]; self.assertLess(abs((n[0] + n[2]) / 2 - (sw[0] + sw[2]) / 2), 40); self.assertLess(abs(n[3] - sw[3]), 40)

    def test_side_flames_on_their_own_sides_and_overlap_globe(self):
        b = bbox(layer_mask(self.els['body'], 2.6)[0]); cx = (b[0] + b[2]) / 2
        l, r = bbox(layer_mask(self.els['flame_left'], 2.6)[0]), bbox(layer_mask(self.els['flame_right'], 2.6)[0])
        self.assertLess((l[0] + l[2]) / 2, cx); self.assertGreater((r[0] + r[2]) / 2, cx)
        for fb in (l, r): self.assertTrue(fb[0] < b[2] and fb[2] > b[0] and fb[1] < b[3] and fb[3] > b[1], 'flame detached from globe')
        self.assertLess(l[0], b[0]); self.assertGreater(r[2], b[2])
        self.assertFalse(layer_mask(self.els['flame_left'], 1.0)[0].any(), 'flames visible before their cue')


if __name__ == '__main__': unittest.main()
