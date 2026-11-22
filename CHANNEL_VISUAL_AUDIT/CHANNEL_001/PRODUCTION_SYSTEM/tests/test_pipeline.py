"""Regression tests: python3 -m unittest discover -s tests -v   (run from PRODUCTION_SYSTEM). Synthetic PNGs only; touches temp dirs."""
import json, os, shutil, sys, tempfile, unittest
from unittest import mock
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pipeline as P, render_scene as R
from PIL import Image, ImageDraw

SCHEMA = os.path.join(P.HERE, 'asset_schema.json')
META = lambda ids: {i: dict(author='codex', generator='g', provenance='p', source='s') for i in ids}


def png(path, size, draw=None, mode='RGBA'):
    im = Image.new(mode, size, (0, 0, 0, 0) if mode == 'RGBA' else (255, 255, 255))
    if draw: draw(ImageDraw.Draw(im))
    im.save(path); return path


def thick_line(p0, p1, w=40): return lambda d: d.line([p0, p1], fill=(14, 14, 14, 255), width=w)


class Base(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(); self.st = os.path.join(self.root, 'stage'); os.makedirs(self.st)
        shutil.copy(SCHEMA, self.root); self.addCleanup(shutil.rmtree, self.root)

    def meta(self, ids): json.dump(META(ids), open(os.path.join(self.root, 'staging_meta.json'), 'w'))

    def val(self, ids=None):
        self.meta(ids or [os.path.splitext(f)[0].replace('_draft', '') for f in os.listdir(self.st)])
        rep = P.validate([self.st], P.load_meta(self.root), self.root); return {r['id']: r for r in rep['files']}, rep


class Validation(Base):
    def test_thin_valid_limbs_accepted(self):
        # 40px-wide arm in a 2048 canvas = ~0.5% coverage: the old 25% rule rejected this
        png(f'{self.st}/rig_arm_left_down_draft.png', (2048, 2048), thick_line((1000, 168), (850, 900)))
        png(f'{self.st}/rig_arm_right_down_draft.png', (2048, 2048), thick_line((1050, 168), (1200, 900)))
        png(f'{self.st}/rig_torso_draft.png', (2048, 2048), lambda d: d.line([(1024, 10), (1024, 1050)], fill=(14, 14, 14, 255), width=30))
        png(f'{self.st}/rig_legs_draft.png', (2048, 2048), lambda d: (d.line([(1024, 1030), (900, 1790)], fill=(14, 14, 14, 255), width=30), d.line([(1024, 1030), (1150, 1790)], fill=(14, 14, 14, 255), width=30)))
        r, _ = self.val()
        for i, x in r.items(): self.assertEqual(x['status'], 'PASS', (i, x['errors']))
        self.assertLess(r['rig_arm_left_down']['metrics']['bbox_frac'], .25)

    def test_transparent_padding_allowed_for_illustration(self):
        png(f'{self.st}/prop_dollar_sign.png', (1024, 1536), lambda d: d.ellipse((100, 200, 900, 1300), fill=(30, 160, 60, 255)))
        r, _ = self.val(); self.assertEqual(r['prop_dollar_sign']['status'], 'PASS', r['prop_dollar_sign']['errors'])

    def test_illustration_tiny_subject_rejected(self):
        png(f'{self.st}/prop_qcircle.png', (1024, 1024), lambda d: d.ellipse((480, 480, 560, 560), fill=(0, 0, 0, 255)))
        r, _ = self.val(); self.assertEqual(r['prop_qcircle']['status'], 'FAIL')

    def test_malformed_files(self):
        good = png(f'{self.st}/prop_qcircle.png', (1024, 1024), lambda d: d.ellipse((60, 60, 960, 960), fill=(0, 0, 0, 255)))
        data = open(good, 'rb').read()
        open(f'{self.st}/prop_dollar_sign.png', 'wb').write(data[:len(data) // 2])           # truncated
        open(f'{self.st}/prop_chart_screen.png', 'wb').write(b'not a png at all')            # not PNG
        png(f'{self.st}/prop_moneybag_pair.png', (1024, 1024), None, mode='RGB')              # wrong mode
        png(f'{self.st}/char_master_sheet.png', (2048, 2048), None)                           # empty
        png(f'{self.st}/char_body_down.png', (2048, 2048), lambda d: d.rectangle((0, 0, 2047, 2047), fill=(0, 0, 0, 255)))  # fully opaque
        r, _ = self.val()
        for i in ('prop_dollar_sign', 'prop_chart_screen', 'prop_moneybag_pair', 'char_master_sheet', 'char_body_down'): self.assertEqual(r[i]['status'], 'FAIL', i)
        self.assertIn('corrupt', r['prop_dollar_sign']['errors'][0]); self.assertIn('signature', r['prop_chart_screen']['errors'][0])
        self.assertIn('RGBA', r['prop_moneybag_pair']['errors'][0]); self.assertIn('empty', r['char_master_sheet']['errors'][0])
        self.assertTrue(any('transparency' in e for e in r['char_body_down']['errors']))
        self.assertEqual(r['prop_qcircle']['status'], 'PASS')

    def test_missing_assets_reported(self):
        png(f'{self.st}/prop_qcircle.png', (1024, 1024), lambda d: d.ellipse((60, 60, 960, 960), fill=(0, 0, 0, 255)))
        _, rep = self.val(); m = rep['summary']['missing']
        self.assertIn('rig_arm_left_up', m); self.assertIn('char_head_sweat', m); self.assertNotIn('prop_qcircle', m); self.assertEqual(rep['summary']['batch'], 'INCOMPLETE')

    def test_incorrect_variant_and_unknown_id(self):
        d = lambda x: x.ellipse((60, 60, 960, 960), fill=(0, 0, 0, 255))
        png(f'{self.st}/char_head_angry.png', (1024, 1024), d); png(f'{self.st}/mystery_asset.png', (1024, 1024), d); png(f'{self.st}/rig_arm_left_wave.png', (2048, 2048), d)
        r, _ = self.val()
        self.assertIn('incorrect variant', r['char_head_angry']['errors'][0]); self.assertIn('unknown asset id', r['mystery_asset']['errors'][0]); self.assertIn('incorrect variant', r['rig_arm_left_wave']['errors'][0])

    def test_duplicate_ids(self):
        d = lambda x: x.ellipse((60, 60, 960, 960), fill=(0, 0, 0, 255))
        png(f'{self.st}/prop_qcircle.png', (1024, 1024), d); png(f'{self.st}/prop_qcircle_draft.png', (1024, 1024), d)
        r, rep = self.val(['prop_qcircle']); self.assertEqual(rep['summary']['duplicates'], ['prop_qcircle'])
        self.assertTrue(all(x['status'] == 'FAIL' for x in rep['files']))

    def test_rig_anatomy(self):
        png(f'{self.st}/rig_arm_left_down.png', (2048, 2048), thick_line((1400, 168), (1500, 900)))   # wrong side
        png(f'{self.st}/rig_arm_right_down.png', (2048, 2048), thick_line((1500, 600), (1600, 1200)))  # detached from shoulder
        png(f'{self.st}/rig_legs.png', (2048, 2048), thick_line((1024, 300), (1024, 500)))            # not at hip, too short
        r, _ = self.val()
        self.assertTrue(any('wrong side' in e for e in r['rig_arm_left_down']['errors']))
        self.assertTrue(any('shoulder anchor' in e for e in r['rig_arm_right_down']['errors']))
        self.assertTrue(any('hip' in e for e in r['rig_legs']['errors']))

    def test_clipped_limb_rejected(self):
        png(f'{self.st}/rig_arm_right_up.png', (2048, 2048), thick_line((1050, 168), (1200, -300)))   # exits top edge
        r, _ = self.val(); self.assertTrue(any('top canvas edge' in e for e in r['rig_arm_right_up']['errors']))

    def test_wrong_canvas_and_missing_metadata(self):
        png(f'{self.st}/rig_arm_left_down.png', (1024, 1024), thick_line((500, 84), (420, 450)))
        r, _ = self.val(); self.assertTrue(any('canvas' in e for e in r['rig_arm_left_down']['errors']))
        png(f'{self.st}/prop_qcircle.png', (1024, 1024), lambda d: d.ellipse((60, 60, 960, 960), fill=(0, 0, 0, 255)))
        json.dump({}, open(os.path.join(self.root, 'staging_meta.json'), 'w'))
        rep = P.validate([self.st], {}, self.root); q = [x for x in rep['files'] if x['id'] == 'prop_qcircle'][0]
        self.assertTrue(any('metadata' in e for e in q['errors']))

    def test_earth_overlay_registration(self):
        png(f'{self.st}/prop_earth_body.png', (2048, 2048), lambda d: d.ellipse((430, 430, 1620, 1620), fill=(20, 40, 120, 200)))
        png(f'{self.st}/prop_earth_face_neutral.png', (2048, 2048), lambda d: d.ellipse((800, 900, 1200, 1100), fill=(255, 255, 255, 255)))
        png(f'{self.st}/prop_earth_face_sweat.png', (2048, 2048), lambda d: d.ellipse((1800, 900, 2000, 1100), fill=(255, 255, 255, 255)))  # off the globe
        r, _ = self.val(); self.assertEqual(r['prop_earth_face_neutral']['status'], 'PASS', r['prop_earth_face_neutral']['errors'])
        self.assertTrue(any('not inside globe' in e for e in r['prop_earth_face_sweat']['errors']))


class Registry(Base):
    def setUp(self):
        super().setUp()
        self.f = png(f'{self.st}/prop_qcircle.png', (1024, 1024), lambda d: d.ellipse((60, 60, 960, 960), fill=(0, 0, 0, 255)))
        self.meta(['prop_qcircle']); json.dump([dict(id='legacy_x', file='assets/x.png')], open(os.path.join(self.root, 'asset_registry.json'), 'w'))
        self.sha = P.sha256(self.f)

    def reg(self): return json.load(open(os.path.join(self.root, 'asset_registry.json')))

    def review(self, verdict='PASS', reviewer='fresh-vision-agent', sha=None): P.record_review('prop_qcircle', sha or self.sha, verdict, reviewer, 'looked at it at animation size', self.root)

    def test_dry_run_changes_nothing(self):
        before = open(os.path.join(self.root, 'asset_registry.json')).read(); self.review()
        ok, msgs, new = P.approve(['prop_qcircle'], [self.st], dry_run=True, root=self.root)
        self.assertTrue(ok); self.assertEqual(open(os.path.join(self.root, 'asset_registry.json')).read(), before)
        self.assertFalse(os.path.exists(os.path.join(self.root, 'approved'))); self.assertFalse(os.path.exists(os.path.join(self.root, 'registry_backups')))

    def test_no_review_no_registration(self):
        ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertFalse(ok); self.assertIn('no independent review', msgs[0]); self.assertEqual(len(self.reg()), 1)

    def test_self_review_refused_and_non_pass_blocks(self):
        with self.assertRaises(ValueError): self.review(reviewer='codex')
        with self.assertRaises(ValueError): self.review(reviewer='same-agent review')
        self.review('PARTIAL'); ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertFalse(ok); self.assertIn('PASS required', msgs[0])

    def test_review_bound_to_file_hash(self):
        self.review(sha='0' * 64); ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertFalse(ok); self.assertIn('sha mismatch', msgs[0])

    def test_approve_then_resolve_and_verify(self):
        self.review(); ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertTrue(ok, msgs)
        e = [r for r in self.reg() if r['id'] == 'prop_qcircle'][0]; self.assertEqual(e['status'], 'approved'); self.assertEqual(P.verify(self.root), [])
        self.assertEqual(R.resolve('asset:prop_qcircle', self.root), e['file']); self.assertEqual(R.resolve('plain/path.png', self.root), 'plain/path.png')
        self.assertEqual(R.resolve('asset:legacy_x', self.root), 'assets/x.png')
        with open(os.path.join(self.root, e['file']), 'ab') as f: f.write(b'x')
        self.assertTrue(P.verify(self.root))   # tamper detected

    def test_variant_syntax_and_unapproved_never_resolves(self):
        reg = self.reg() + [dict(id='char_head_worried', file='approved/h.png', status='approved'), dict(id='char_head_happy', file='staging/h.png', status='candidate'), dict(id='char_head_sweat', file='old.png', status='superseded')]
        json.dump(reg, open(os.path.join(self.root, 'asset_registry.json'), 'w'))
        self.assertEqual(R.resolve('asset:char_head/worried', self.root), 'approved/h.png')
        for bad in ('asset:char_head/happy', 'asset:char_head/sweat', 'asset:nothing'):
            with self.assertRaises(KeyError): R.resolve(bad, self.root)

    def test_no_silent_replace_needs_supersede(self):
        self.review(); P.approve(['prop_qcircle'], [self.st], root=self.root)
        png(self.f, (1024, 1024), lambda d: d.ellipse((100, 100, 900, 900), fill=(9, 9, 9, 255))); new = P.sha256(self.f)
        ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertFalse(ok)   # unreviewed candidate
        self.review(sha=new); ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertFalse(ok); self.assertIn('--supersede', msgs[0])
        ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], supersede=True, root=self.root); self.assertTrue(ok, msgs)
        st = {r['sha256'][:8]: r['status'] for r in self.reg() if r['id'] == 'prop_qcircle'}; self.assertEqual(st[new[:8]], 'approved'); self.assertEqual(st[self.sha[:8]], 'superseded')

    def test_rollback_restores_and_is_reversible(self):
        orig = open(os.path.join(self.root, 'asset_registry.json')).read(); self.review(); P.approve(['prop_qcircle'], [self.st], root=self.root)
        self.assertEqual(len(self.reg()), 2); t, cur = P.rollback(root=self.root)
        self.assertEqual(open(os.path.join(self.root, 'asset_registry.json')).read().strip(), json.dumps(json.loads(orig), indent=1).strip())
        P.rollback(to=cur, root=self.root); self.assertEqual(len(self.reg()), 2)   # undo the rollback

    def test_atomic_when_registry_swap_fails(self):
        self.review(); before = open(os.path.join(self.root, 'asset_registry.json')).read(); real = os.replace
        def boom(a, b):
            if b.endswith('asset_registry.json'): raise OSError('disk full')
            return real(a, b)
        with mock.patch.object(P.os, 'replace', boom): ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root)
        self.assertFalse(ok); self.assertIn('registry unchanged', msgs[0]); self.assertEqual(open(os.path.join(self.root, 'asset_registry.json')).read(), before)
        self.assertEqual([f for f in os.listdir(self.root) if '.tmp' in f], [])
        ok, msgs, _ = P.approve(['prop_qcircle'], [self.st], root=self.root); self.assertTrue(ok, msgs)   # recoverable: retry works

    def test_all_or_nothing(self):
        png(f'{self.st}/prop_dollar_sign.png', (1024, 1536), None); self.meta(['prop_qcircle', 'prop_dollar_sign']); self.review()
        ok, msgs, _ = P.approve(['prop_qcircle', 'prop_dollar_sign'], [self.st], root=self.root); self.assertFalse(ok); self.assertEqual(len(self.reg()), 1)


class InventoryReconciliation(unittest.TestCase):
    def test_every_batch1_inventory_asset_is_covered_by_schema_families(self):
        import csv
        inv = {r['asset_id'] for r in csv.DictReader(open(os.path.join(P.HERE, 'ASSET_INVENTORY.csv'))) if r['codex_batch1'].startswith('YES')}
        cov = {d['inventory'] for d in P.load_schema()['families'].values()}; self.assertEqual(inv - cov, set(), 'inventory assets with no schema family')
        self.assertEqual(cov - inv - {'prop_dollar_sign'}, set(), 'schema inventory refs not in inventory')

    def test_schema_ids_expand_to_19_unique_staging_ids_plus_rig_layers(self):
        ids = P.expand_ids(P.load_schema()); self.assertEqual(len(ids), len(set(ids)))
        for need in ('char_head_sweat', 'rig_arm_left_hips', 'rig_arm_right_up', 'rig_torso', 'rig_legs', 'prop_earth_face_sweat', 'prop_earth_flames', 'char_body_point'): self.assertIn(need, ids)


class RendererCompat(unittest.TestCase):
    def test_existing_specs_still_validate(self):
        for s in ('same_video_SH001_002.json', 'original_ES1.json'): self.assertEqual(R.validate(json.load(open(os.path.join(P.HERE, 'specs', s)))), [], s)

    def test_validate_reports_unresolved_registry_ref(self):
        spec = dict(shots=[dict(start=0, dur=1, elements=[dict(id='a', asset='asset:does_not_exist')])]); self.assertTrue(any('unresolved' in e for e in R.validate(spec)))

    def test_render_scale_applied_for_registry_assets_only(self):
        d = tempfile.mkdtemp(); self.addCleanup(shutil.rmtree, d); json.dump([dict(id='a_big', file='x.png', status='approved', render_scale=0.25), dict(id='cand', file='y.png', status='candidate', render_scale=9)], open(d + '/asset_registry.json', 'w'))
        self.assertEqual(R.asset_scale('asset:a_big', d), .25); self.assertEqual(R.asset_scale('asset:cand', d), 1.0); self.assertEqual(R.asset_scale('assets/p.png', d), 1.0)


if __name__ == '__main__': unittest.main()


class RigContractV2(Base):
    """Versioned contracts: v1 = legacy draft anchors, v2 = corrected rig. Neither is weakened to pass the other."""
    L = (14, 14, 14, 255)

    def meta2(self, ids, contract):
        m = META(ids)
        for i in ids: m[i]['contract'] = contract
        json.dump(m, open(os.path.join(self.root, 'staging_meta.json'), 'w'))

    def run_val(self, ids, contract):
        self.meta2(ids, contract); rep = P.validate([self.st], P.load_meta(self.root), self.root); return {r['id']: r for r in rep['files']}, rep

    def arm(self, name, p0, p1): png(f'{self.st}/{name}.png', (2048, 2048), thick_line(p0, p1))

    def test_v2_arm_passes_v2_fails_v1_and_vice_versa(self):
        n = 'rig_arm_left_shrug'; self.arm(n, (1020, 440), (800, 520))           # root at v2 shoulder y=454
        self.assertEqual(self.run_val([n], 'v2')[0][n]['status'], 'PASS')
        e = self.run_val([n], 'v1')[0][n]; self.assertEqual(e['status'], 'FAIL'); self.assertTrue(any('shoulder anchor' in x for x in e['errors']))
        self.arm(n, (1020, 175), (800, 250))                                      # legacy root at y=168
        self.assertEqual(self.run_val([n], 'v1')[0][n]['status'], 'PASS')
        self.assertEqual(self.run_val([n], 'v2')[0][n]['status'], 'FAIL')

    def test_v2_torso_and_legs_anchors(self):
        png(f'{self.st}/rig_torso.png', (2048, 2048), lambda d: d.line([(1024, 320), (1024, 1222)], fill=self.L, width=30))
        png(f'{self.st}/rig_legs.png', (2048, 2048), lambda d: (d.line([(1024, 1146), (900, 1747)], fill=self.L, width=30), d.line([(1024, 1146), (1150, 1747)], fill=self.L, width=30)))
        r, _ = self.run_val(['rig_torso', 'rig_legs'], 'v2')
        for i, x in r.items(): self.assertEqual(x['status'], 'PASS', (i, x['errors']))
        for i, x in self.run_val(['rig_torso', 'rig_legs'], 'v1')[0].items(): self.assertEqual(x['status'], 'FAIL', i)

    def test_unknown_contract_rejected(self):
        self.arm('rig_arm_left_down', (1020, 440), (850, 1146))
        self.assertTrue(any('unknown contract' in e for e in self.run_val(['rig_arm_left_down'], 'v9')[0]['rig_arm_left_down']['errors']))

    def test_char_body_v2_thin_figure_ok_but_legacy_keeps_bbox_rule(self):
        def fig(d): d.line([(1024, 320), (1024, 1747)], fill=self.L, width=30); d.line([(790, 600), (1260, 600)], fill=self.L, width=30)
        png(f'{self.st}/char_body_down.png', (2048, 2048), fig)
        self.assertEqual(self.run_val(['char_body_down'], 'v2')[0]['char_body_down']['status'], 'PASS')
        e = self.run_val(['char_body_down'], 'v1')[0]['char_body_down']; self.assertEqual(e['status'], 'FAIL'); self.assertTrue(any('bbox' in x for x in e['errors']))

    def test_char_body_v2_must_touch_anchors_and_be_tall(self):
        png(f'{self.st}/char_body_down.png', (2048, 2048), lambda d: d.rectangle((900, 1500, 1150, 1700), fill=self.L))
        e = self.run_val(['char_body_down'], 'v2')[0]['char_body_down']; self.assertEqual(e['status'], 'FAIL')
        self.assertTrue(any('neck anchor' in x for x in e['errors'])); self.assertTrue(any('height' in x for x in e['errors']))

    def test_pose_pair_relationships(self):
        self.arm('rig_arm_left_up', (1020, 440), (900, 600)); self.arm('rig_arm_right_up', (1030, 440), (1150, 600))
        r, _ = self.run_val(['rig_arm_left_up', 'rig_arm_right_up'], 'v2')
        self.assertTrue(all(any('pose "up"' in e for e in x['errors']) for x in r.values()))
        self.arm('rig_arm_right_up', (1030, 440), (1100, 200))                      # raised above shoulder
        r, _ = self.run_val(['rig_arm_left_up', 'rig_arm_right_up'], 'v2')
        self.assertEqual({x['status'] for x in r.values()}, {'PASS'})                  # one raised arm suffices; other rests
        self.arm('rig_arm_left_hips', (1020, 440), (900, 700)); self.arm('rig_arm_right_hips', (1030, 440), (1150, 1000))
        r, _ = self.run_val(['rig_arm_left_hips', 'rig_arm_right_hips'], 'v2'); self.assertEqual({x['status'] for x in r.values()}, {'FAIL'})
        self.assertTrue(any('pose "hips"' in e for e in r['rig_arm_left_hips']['errors']))

    def test_flame_sides_and_contract_gate(self):
        def body(d): d.ellipse((517, 505, 1530, 1543), fill=(40, 90, 160, 255))
        png(f'{self.st}/prop_earth_body.png', (2048, 2048), body)
        png(f'{self.st}/prop_earth_flame_left.png', (2048, 2048), lambda d: d.ellipse((398, 1126, 816, 1561), fill=(240, 120, 20, 255)))
        png(f'{self.st}/prop_earth_flame_right.png', (2048, 2048), lambda d: d.ellipse((1268, 384, 1639, 792), fill=(240, 120, 20, 255)))
        ids = ['prop_earth_body', 'prop_earth_flame_left', 'prop_earth_flame_right']
        r, rep = self.run_val(ids, 'v2'); self.assertEqual({x['status'] for x in r.values()}, {'PASS'}, [x['errors'] for x in r.values()])
        for i in ids[1:]: self.assertTrue(any('requires contract' in e for e in self.run_val(ids, 'v1')[0][i]['errors']))   # legacy never silently accepts side flames
        png(f'{self.st}/prop_earth_flame_left.png', (2048, 2048), lambda d: d.ellipse((1268, 384, 1639, 792), fill=(240, 120, 20, 255)))   # left layer drawn on the right
        e = self.run_val(ids, 'v2')[0]['prop_earth_flame_left']; self.assertEqual(e['status'], 'FAIL'); self.assertTrue(any('wrong side' in x for x in e['errors']))
        png(f'{self.st}/prop_earth_flame_left.png', (2048, 2048), lambda d: d.ellipse((100, 1900, 160, 1960), fill=(240, 120, 20, 255)))   # detached from globe
        self.assertTrue(any('overlap' in x for x in self.run_val(ids, 'v2')[0]['prop_earth_flame_left']['errors']))

    def test_combined_flames_legacy_lower_edge_vs_v2_sides(self):
        png(f'{self.st}/prop_earth_body.png', (2048, 2048), lambda d: d.ellipse((517, 505, 1530, 1543), fill=(40, 90, 160, 255)))
        def both(d): d.ellipse((398, 1126, 816, 1561), fill=(240, 120, 20, 255)); d.ellipse((1268, 384, 1639, 792), fill=(240, 120, 20, 255))
        png(f'{self.st}/prop_earth_flames.png', (2048, 2048), both)
        ids = ['prop_earth_body', 'prop_earth_flames']
        self.assertEqual(self.run_val(ids, 'v2')[0]['prop_earth_flames']['status'], 'PASS')
        self.assertTrue(any('lower edge' in e for e in self.run_val(ids, 'v1')[0]['prop_earth_flames']['errors']))
        png(f'{self.st}/prop_earth_flames.png', (2048, 2048), lambda d: d.ellipse((600, 1400, 1400, 1700), fill=(240, 120, 20, 255)))   # legacy: lower-edge flames
        self.assertEqual(self.run_val(ids, 'v1')[0]['prop_earth_flames']['status'], 'PASS')

    def test_missing_ids_depend_on_contract(self):
        self.arm('rig_arm_left_down', (1020, 440), (850, 1146))
        self.meta2(['rig_arm_left_down'], 'v2')
        m1 = P.validate([self.st], P.load_meta(self.root), self.root, contract='v1')['summary']['missing']
        m2 = P.validate([self.st], P.load_meta(self.root), self.root, contract='v2')['summary']['missing']
        self.assertNotIn('prop_earth_flame_left', m1); self.assertIn('prop_earth_flame_left', m2)

    def test_registry_entry_records_contract_and_review_history_kept(self):
        self.arm('rig_arm_left_down', (1020, 440), (850, 1146)); self.arm('rig_arm_right_down', (1030, 440), (1200, 1146))
        self.meta2(['rig_arm_left_down', 'rig_arm_right_down'], 'v2')
        _, rep = self.run_val(['rig_arm_left_down', 'rig_arm_right_down'], 'v2'); sha = rep['files'][0]['sha256']
        P.record_review('rig_arm_left_down', 'a' * 64, 'PARTIAL', 'blind-reviewer', 'first', self.root)
        P.record_review('rig_arm_left_down', sha, 'PASS', 'blind-reviewer', 'second', self.root)
        self.assertTrue(os.path.exists(os.path.join(self.root, 'reviews', 'history', 'rig_arm_left_down@aaaaaaaa.json')))
        ok, msgs, new = P.approve(['rig_arm_left_down'], [self.st], root=self.root)
        self.assertTrue(ok, msgs); self.assertEqual(new[0]['contract'], 'v2'); self.assertEqual(new[0]['type'], 'rig_arm')
