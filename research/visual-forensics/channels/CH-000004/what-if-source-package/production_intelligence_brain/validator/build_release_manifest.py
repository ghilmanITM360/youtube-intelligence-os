#!/usr/bin/env python3
"""Generate RELEASE_MANIFEST.json from the canonical files currently on disk.

Run from anywhere:

    python3 validator/build_release_manifest.py

Re-run this any time canonical files change, then re-run validate_brain.py to
confirm the manifest still matches disk.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _canonical_files import list_canonical_files  # noqa: E402

BRAIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

entries = list_canonical_files(BRAIN)

manifest = {
    'schema_version': '1.0',
    'release_version': '1.0.0',
    'generated_at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'excludes_self': True,
    'files': [
        {
            'relative_path': rel_path,
            'size_bytes': size,
            'sha256': digest,
            'category': category,
            'canonical': True,
        }
        for rel_path, category, size, digest in entries
    ],
}

out_path = os.path.join(BRAIN, 'RELEASE_MANIFEST.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)
    f.write('\n')

print(f'Wrote {out_path} with {len(entries)} canonical files.')
