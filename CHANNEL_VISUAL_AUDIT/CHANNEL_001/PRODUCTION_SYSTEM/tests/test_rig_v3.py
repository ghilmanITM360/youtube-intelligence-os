import json, os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__)); PS = os.path.dirname(HERE); sys.path.insert(0, PS)
import pipeline
PROTO = os.path.join(PS, 'rig_measurements', 'prototype')
META = {n: dict(author='t', provenance='t', generator='t', source='t') for n in ('rig_torso', 'rig_arm_left_hips', 'rig_arm_right_hips', 'rig_legs')}
class V3(unittest.TestCase):
    def test_versions_preserved(self):
        rv = json.load(open(os.path.join(PS, 'asset_schema.json')))['rig_versions']
        self.assertEqual(rv['v1']['anchors']['shoulder'], [1024, 168]); self.assertEqual(rv['v2']['anchors']['shoulder'], [1024, 454])
        self.assertEqual(rv['v3']['anchors']['neck'], rv['v2']['anchors']['neck']); self.assertEqual(rv['v3']['anchors']['hip'], rv['v2']['anchors']['hip'])
        self.assertEqual(rv['v3']['anchors']['shoulder'], [1024, 559])
    def test_measured_shoulder_fraction(self):
        d = json.load(open(os.path.join(PS, 'rig_measurements', 'hips_landmarks.json')))['derived']
        self.assertAlmostEqual(d['shoulder_frac_of_torso'], 0.289, places=2); self.assertTrue(0.47 <= d['hand_frac_A_L'] <= 0.62)
    def test_prototype_layers_pass_v3(self):
        r = pipeline.validate([os.path.join(PROTO, n + '.png') for n in META], meta=META, contract='v3')
        self.assertEqual({x['id']: x['status'] for x in r['files']}, {n: 'PASS' for n in META}, [x['errors'] for x in r['files']])
    def test_v2_hips_hand_rule_unchanged(self):
        r = pipeline.validate([os.path.join(PROTO, n + '.png') for n in ('rig_arm_left_hips', 'rig_arm_right_hips')], meta={k: META[k] for k in ('rig_arm_left_hips', 'rig_arm_right_hips')}, contract='v2')
        self.assertTrue(all(x['status'] == 'FAIL' for x in r['files']))  # v3 arms do not satisfy the old v2 shoulder anchor: contracts are not interchangeable
if __name__ == '__main__': unittest.main()
