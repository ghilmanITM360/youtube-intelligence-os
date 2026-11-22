"""Run the real proof builder preflight with one in-memory input change per case."""
import json
import runpy
import sys
from pathlib import Path
from unittest.mock import patch

root = Path(__file__).resolve().parents[4]
builder = root / 'productions/doc-animation-proof-01/build_proof.py'
load = json.load

def claim(doc, cid):
    return next(row for row in doc['claims'] if row['id'] == cid)

def scene(doc, sid):
    return next(row for row in doc['scenes'] if row['id'] == sid)

def remove_qualification(doc):
    target = scene(doc, 'P2_doc')
    target['on_screen_text'].remove('Once a year')
    target['narration'] = target['narration'].replace(', calculated once a year', '')

cases = [
    ('baseline', '', lambda doc: None),
    ('unverified referenced', 'claims.json', lambda doc: claim(doc, 'C4').update(status='UNVERIFIED')),
    ('unknown scene id reference', 'scenes.json', lambda doc: scene(doc, 'P6_close').update(claim_ids=['C140'])),
    ('qualification missing from JSON', 'scenes.json', remove_qualification),
    ('rejected document annotation omitted from storyboard', 'scenes.json',
     lambda doc: scene(doc, 'P2_doc').update(claim_ids=['C1', 'C2', 'C3'], on_screen_text=['$1,000'])),
    ('hypothetical with same figures framed as historical fact', 'scenes.json',
     lambda doc: scene(doc, 'P4_years').update(narration='These are reported results from an actual savings account.')),
    ('wrong time period admitted via ignored digits', 'scenes.json',
     lambda doc: scene(doc, 'P5_compare').update(narration='These returns took 30 years.', ignore_numbers=[3,30])),
    ('unrelated claim licenses closing statement', 'scenes.json',
     lambda doc: scene(doc, 'P6_close').update(claim_ids=['C3'])),
    ('misquotation in scene copy', 'scenes.json',
     lambda doc: scene(doc, 'P2_doc').update(narration='The Bureau says: "Your savings earn interest only on the original deposit."')),
    ('incompatible comparison in scene copy', 'scenes.json',
     lambda doc: scene(doc, 'P5_compare').update(narration='The comparison uses simple interest after one year versus compound interest after three.')),
    ('qualification substituted outside the actual render', 'claims.json',
     lambda doc: claim(doc, 'C2').update(required_qualification='calculated once a year')),
    ('unknown doc claim declared only in document spec', 'doc_spec.json',
     lambda doc: (doc['source']['claim_ids'].append('C140'), doc['annotations'][0].update(claim_id='C140'))),
    ('wrong passage metadata in document spec', 'doc_spec.json',
     lambda doc: doc['annotations'][0].update(passage='Bureau guarantees these returns.')),
]
for name, filename, mutate in cases:
    print(f'\n{name}')
    def changed(file, *args, **kwargs):
        data = load(file, *args, **kwargs)
        if Path(file.name).name == filename:
            mutate(data)
        if name == 'rejected document annotation omitted from storyboard' and Path(file.name).name == 'claims.json':
            claim(data, 'C4').update(status='REJECTED')
        return data
    with patch.object(json, 'load', changed), patch.object(sys, 'argv', [str(builder), '--check']):
        try:
            runpy.run_path(str(builder), run_name='__main__')
        except SystemExit as result:
            print('exit:', result.code)
