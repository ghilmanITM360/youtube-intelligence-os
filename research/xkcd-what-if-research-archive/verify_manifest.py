"""Verify this archive against MANIFEST.csv (sha256 + size) and check that no unlisted file exists.
usage (from repo root, any checkout of the branch):  python3 -I research/xkcd-what-if-research-archive/verify_manifest.py"""
import csv, hashlib, os, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(os.path.dirname(here))
rows = [r for r in csv.DictReader(open(here + '/MANIFEST.csv')) if r['status'] in ('INCLUDED', 'GENERATED')]
bad = 0; listed = set()
for r in rows:
    p = os.path.join(root, r['repo_path']); listed.add(os.path.normpath(p))
    if not os.path.isfile(p): print('MISSING', r['repo_path']); bad += 1; continue
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    if h != r['sha256'] or os.path.getsize(p) != int(r['size_bytes']): print('MISMATCH', r['repo_path']); bad += 1
skip = {os.path.normpath(here + '/MANIFEST.csv'), os.path.normpath(here + '/MANIFEST.json')}
extra = [os.path.join(dp, f) for dp, _, fs in os.walk(here) for f in fs if os.path.normpath(os.path.join(dp, f)) not in listed | skip]
for e in extra: print('UNLISTED', e); bad += 1
print(len(rows), 'files checked;', 'OK' if not bad else str(bad) + ' problems'); sys.exit(1 if bad else 0)
