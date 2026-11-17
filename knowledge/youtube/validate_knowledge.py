#!/usr/bin/env python3
"""Read-only verification of the saved knowledge catalog; does not rediscover files."""
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'knowledge/youtube'


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def main():
    rows = list(csv.DictReader((BASE / 'SOURCE_CATALOG.csv').open()))
    by_id = {row['Source_ID']: row for row in rows}
    errors = []
    if len(by_id) != len(rows):
        errors.append('duplicate source IDs')
    checked = 0
    for row in rows:
        if row['Availability'] == 'LOCAL_AVAILABLE':
            path = Path(row['Original_Path_or_URL'])
            if not path.is_absolute():
                path = ROOT / path
            if not path.is_file():
                errors.append('missing local source: ' + row['Source_ID'])
            elif digest(path) != row['SHA256_if_local']:
                errors.append('changed local checksum: ' + row['Source_ID'])
            checked += 1
        duplicate = row['Duplicate_Of']
        if duplicate:
            other = by_id.get(duplicate)
            if not other or other['SHA256_if_local'] != row['SHA256_if_local']:
                errors.append('invalid duplicate reference: ' + row['Source_ID'])
            elif other['Duplicate_Of']:
                errors.append('non-root duplicate reference: ' + row['Source_ID'])
    branches = list(csv.DictReader((BASE / 'BRANCH_SOURCE_INDEX.csv').open()))
    blobs = sorted({r['Git_Blob'] for r in branches})
    result = subprocess.check_output(['git', 'cat-file', '--batch-check'],
                                     input=('\n'.join(blobs) + '\n').encode(), cwd=ROOT)
    if any(b' missing' in line for line in result.splitlines()):
        errors.append('missing Git source object')
    documents = list(BASE.glob('*.md')) + list((ROOT / 'research/finance-economics-intelligence').glob('*.md')) + [ROOT / 'docs/research/README.md']
    for doc in documents:
        for target in re.findall(r'\]\(([^\n]+?)\)', doc.read_text()):
            if target.startswith(('https:', 'http:', '#')):
                continue
            path = target.split('#')[0]
            if path and not (doc.parent / path).exists():
                errors.append('broken link: ' + str(doc.relative_to(ROOT)) + ' -> ' + path)
    scope = subprocess.check_output(['git', 'diff', '--name-only', '08e719264e31ecd82de24f8eeb8f065c08359fe5'], cwd=ROOT).decode().splitlines()
    if any(not p.startswith(('knowledge/youtube/', 'research/finance-economics-intelligence/', 'docs/research/README.md')) for p in scope):
        errors.append('tracked changes outside intended scope')
    print(json.dumps({'local_hashes_checked': checked, 'source_rows': len(rows),
                      'git_blobs_resolve': len(blobs), 'markdown_documents': len(documents),
                      'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
