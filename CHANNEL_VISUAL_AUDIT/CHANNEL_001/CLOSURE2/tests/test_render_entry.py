"""Regression tests through the ordinary proof entry point with disposable fixtures."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from contextlib import ExitStack
import unittest
from unittest.mock import patch

from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
PROOF = ROOT / 'productions/doc-animation-proof-01'
ENTRY = PROOF / 'build_proof.py'


def by_id(rows, value):
    return next(row for row in rows if row['id'] == value)


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


class BuildEntry(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.folder = Path(directory.name)
        self.output = self.folder / 'out'
        for name in ('claims.json', 'scenes.json', 'doc_spec.json', 'render_plan.json'):
            shutil.copyfile(PROOF / name, self.folder / name)
        capture = Path(read(PROOF / 'doc_spec.json')['source']['file'])
        (self.folder / capture.parent).mkdir(parents=True)
        shutil.copyfile(PROOF / capture, self.folder / capture)

    def edit(self, name, change):
        path = self.folder / f'{name}.json'
        value = read(path)
        change(value)
        path.write_text(json.dumps(value), encoding='utf-8')

    def cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(ENTRY), '--input-dir', str(self.folder),
             '--output-dir', str(self.output), *arguments],
            capture_output=True, text=True, timeout=30,
        )

    def assert_blocked(self, field):
        # Use a rendering mode, so a missed gate would actually reach renderer output.
        result = self.cli('--still', '2,8.6,25,35,45.8,51,58')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(field, result.stdout + result.stderr)
        self.assertFalse(self.output.exists())

    def test_rejected_claim_left_in_rendered_annotation(self):
        self.edit('claims', lambda d: by_id(d['claims'], 'C4').update(status='REJECTED'))
        self.edit('scenes', lambda d: by_id(d['scenes'], 'P2_doc').update(
            claim_ids=['C1', 'C2', 'C3'], on_screen_text=['5 percent', 'Once a year']))
        self.assert_blocked('document.annotations.E5: claim C4 is REJECTED')

    def test_unknown_annotation(self):
        self.edit('doc_spec', lambda d: by_id(d['annotations'], 'E5').update(claim_id='C_UNKNOWN'))
        self.assert_blocked('document.annotations.E5: unknown claim C_UNKNOWN')

    def test_unverified_claim_on_actual_path(self):
        self.edit('claims', lambda d: by_id(d['claims'], 'C4').update(status='UNVERIFIED'))
        self.assert_blocked('document.annotations.E5: claim C4 is UNVERIFIED')

    def test_different_capture(self):
        spec = read(self.folder / 'doc_spec.json')
        path = self.folder / spec['source']['file']
        with Image.open(path) as image:
            replacement = Image.new('RGB', image.size, 'white')
        replacement.save(path)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        self.edit('doc_spec', lambda d: d['source'].update(sha256=digest))
        self.assert_blocked('document.source.file')

    def test_different_marked_region(self):
        self.edit('doc_spec', lambda d: by_id(d['annotations'], 'E5')['rect'].__setitem__(0, 515))
        self.assert_blocked('document.annotations.E5 (claim C4)')

    def test_qualification_disappears_from_actual_crop(self):
        self.edit('doc_spec', lambda d: d['required_context'].pop(1))
        self.assert_blocked('document (capture, crop, context and annotation order)')

    def test_qualification_disappears_from_actual_planned_voice(self):
        def remove_qualification(plan):
            for clause in plan['planned_clauses']:
                clause['text'] = clause['text'].replace('once a year', 'indefinitely')
        self.edit('render_plan', remove_qualification)
        self.assert_blocked('render.planned_clauses')

    def test_unlabelled_hypothetical(self):
        self.edit('render_plan', lambda d: by_id(d['scenes'], 'P3_setup')['items'].pop(0))
        self.assert_blocked('claim H1 needs its on-screen label from scene entry')

    def test_wrong_unit(self):
        self.edit('render_plan', lambda d: by_id(d['scenes'], 'P3_setup')['items'][2]['args'].__setitem__(0, '$1,000 at $5 a year'))
        self.assert_blocked('render.scenes.P3_setup.items[2]')

    def test_wrong_period(self):
        self.edit('render_plan', lambda d: by_id(d['scenes'], 'P3_setup')['items'][3]['args'].__setitem__(0, 'Interest added once a year, for 3 months'))
        self.assert_blocked('render.scenes.P3_setup.items[3]')

    def test_wrong_denominator(self):
        self.edit('render_plan', lambda d: by_id(d['scenes'], 'P3_setup')['items'][2]['args'].__setitem__(0, '$1,000 at 5% per $100 of household income'))
        self.assert_blocked('render.scenes.P3_setup.items[2]')

    def test_altered_quote(self):
        self.edit('doc_spec', lambda d: by_id(d['annotations'], 'E_def1').update(passage='Compound interest is a guaranteed profit'))
        self.assert_blocked('document.annotations.E_def1.passage')

    def test_conflicting_comparison_geometry(self):
        self.edit('render_plan', lambda d: by_id(d['scenes'], 'P5_compare')['items'][3]['args'].__setitem__(3, 999))
        self.assert_blocked('render.scenes.P5_compare.items[3]')

    def test_same_claim_cannot_license_conflicting_copy(self):
        def replace_operand(plan):
            items = by_id(plan['scenes'], 'P5_compare')['items']
            item = next(item for item in items if item['args'][0] == '$157.63')
            item['args'][0] = '$150.00'
        self.edit('render_plan', replace_operand)
        self.assert_blocked('render.scenes.P5_compare.items[')

    def test_claim_free_cannot_add_unreviewed_copy(self):
        self.edit('render_plan', lambda d: by_id(d['scenes'], 'P1')['items'][1]['args'].__setitem__(0, 'Returns are guaranteed'))
        self.assert_blocked('render.scenes.P1.items[1]')

    def test_valid_check_and_all_scene_stills(self):
        result = self.cli('--check')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(self.output.exists())
        result = self.cli('--still', '2,8.6,21,30.5,35,45.8,51,58')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        stills = list((self.output / 'stills').glob('*.png'))
        self.assertEqual(len(stills), 8)
        for path in stills:
            with Image.open(path) as image:
                self.assertEqual(image.size, (1920, 1080))
                image.load()
                self.assertNotEqual(image.getextrema()[0][0], image.getextrema()[0][1])
        self.assertIn('render_plan_sha256', read(self.output / 'timing_track.json'))

    def test_same_plan_reaches_backend_through_main(self):
        module_spec = importlib.util.spec_from_file_location('proof_entry', ENTRY)
        entry = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(entry)
        import v1r4_render as backend

        bound = entry.claim_gate.authorize_render
        validated = []
        delivered = []
        names = entry.claim_gate.RENDER_OPS - {'document'}

        def authorize(register, storyboard, plan, spec, capture):
            validated.append((entry.claim_gate.payload_bytes(plan), entry.claim_gate.payload_bytes(spec), capture))
            report = bound(register, storyboard, plan, spec, capture)
            (self.folder / spec['source']['file']).write_bytes(b'changed after preflight')
            return report

        def record_operation(name):
            def record(*args, **kwargs):
                delivered.append(dict(op=name, args=args, kwargs=kwargs))
                return [] if name == 'source' else object()
            return record

        def deliver_document(spec, start, directory):
            self.assertEqual((Path(directory) / spec['source']['file']).read_bytes(), validated[0][2])
            return object()

        with ExitStack() as stack:
            stack.enter_context(patch.object(entry.claim_gate, 'authorize_render', side_effect=authorize))
            for name in names:
                stack.enter_context(patch.object(backend, name, side_effect=record_operation(name)))
            document = stack.enter_context(patch('doc_scene.document_item', side_effect=deliver_document))
            stack.enter_context(patch.object(entry, 'render_proof'))
            code = entry.main(['--input-dir', str(self.folder), '--output-dir', str(self.output)])
        self.assertEqual(code, 0)
        approved = json.loads(validated[0][0])
        expected = [
            {key: value for key, value in item.items() if key != 'claim_ids'}
            for scene in approved['scenes'] for item in scene['items'] if item['op'] != 'document'
        ]
        self.assertEqual(entry.claim_gate.payload_bytes(delivered), entry.claim_gate.payload_bytes(expected))
        document.assert_called_once()
        self.assertEqual(entry.claim_gate.payload_bytes(document.call_args.args[0]), validated[0][1])
        self.assertEqual(document.call_args.args[1], approved['scenes'][1]['start'])
