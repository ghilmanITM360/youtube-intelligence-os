import csv
import json
import unittest
from pathlib import Path

import production_pipeline as p


class ProductionPipelineTests(unittest.TestCase):
    def test_timestamp_format(self):
        self.assertEqual(p.stamp(67.42), '00:01:07,420')

    def test_semantic_warning(self):
        self.assertEqual(p.classify('If you feel unsafe or dizzy, stop.', 2, 5), 'WARNING')

    def test_real_package_contract(self):
        root = Path('output/chair-stand-safety')
        if not root.exists():
            self.skipTest('Real media fixture package absent')
        report = json.loads((root / 'qc/validation.json').read_text())
        self.assertTrue(all(report['checks'].values()))
        self.assertTrue(report['ready_for_capcut'])
        self.assertGreaterEqual(report['counts']['words'], 90)
        self.assertGreaterEqual(report['counts']['shots'], 6)
        timeline = json.loads((root / 'timeline/timeline.json').read_text())
        self.assertEqual(timeline['shots'][0]['start_sec'], 0)
        self.assertAlmostEqual(timeline['shots'][-1]['end_sec'], timeline['project']['duration_sec'], places=2)
        self.assertEqual(len(timeline['captions']), (root / 'captions/captions.srt').read_text().count(' --> '))
        with (root / 'transcript/words.csv').open() as handle:
            words = list(csv.DictReader(handle))
        self.assertTrue(all(float(w['start_sec']) < float(w['end_sec']) for w in words))
        self.assertTrue(all(float(a['end_sec']) <= float(b['start_sec']) for a,b in zip(words, words[1:])))
        actions = json.loads((root / 'capcut/CAPCUT_ACTIONS.json').read_text())['actions']
        self.assertEqual(actions, sorted(actions, key=lambda a: a['time']))
        self.assertTrue((root / 'capcut/CHATGPT_WORK_CAPCUT_PROMPT.md').exists())


if __name__ == '__main__':
    unittest.main()
