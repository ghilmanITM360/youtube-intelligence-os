#!/usr/bin/env python3
"""Re-hash Machine A o3FQcd91MIs/Uumnx2Fo6cE evidence. Inputs read-only. Writes rows.csv, unique_hashes.csv, summary.json next to this script."""
import collections, csv, hashlib, json, os, pathlib, sys
OUT = pathlib.Path(__file__).resolve().parent
INV = pathlib.Path(sys.argv[1])  # audit raw/portable/inventory_vs_machine_a.csv
ROOTS = {v: pathlib.Path.home() / f'YIOS-local-audits/2026-10-24-{v}-deep-ct-scan' for v in ('o3FQcd91MIs', 'Uumnx2Fo6cE')}
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
listed = {}
for r in csv.DictReader(open(INV)):
    if r['status'] == 'REFERENCED_BUT_UNAVAILABLE_ON_MACHINE_B':
        listed[r['note'].removeprefix('machine A path ')] = r
rows = []; seen = set()
for path, r in listed.items():
    seen.add(path); p = pathlib.Path(path); ok = p.is_file()
    h = sha(p) if ok else ''
    rows.append(dict(video_id=r['associated'], path=path, bytes=p.stat().st_size if ok else '', sha256=h, in_machine_b_portable_inventory='yes',
                     portable_inventory_sha256=r['sha256'], hash_matches_inventory=h == r['sha256'], exists=ok))
for vid, root in ROOTS.items():
    for d, _, names in os.walk(root):
        for n in names:
            path = str(pathlib.Path(d) / n)
            if path in seen: continue
            rows.append(dict(video_id=vid, path=path, bytes=os.path.getsize(path), sha256=sha(path), in_machine_b_portable_inventory='no',
                             portable_inventory_sha256='', hash_matches_inventory='', exists=True))
rows.sort(key=lambda r: r['path'])
with open(OUT / 'rows.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, rows[0].keys()); w.writeheader(); w.writerows(rows)
by = collections.defaultdict(list)
for r in rows:
    if r['sha256']: by[r['sha256']].append(r)
with open(OUT / 'unique_hashes.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['sha256', 'bytes', 'video_ids', 'copies', 'referenced_by_machine_b_inventory', 'first_path'])
    for h, c in sorted(by.items()):
        w.writerow([h, c[0]['bytes'], '|'.join(sorted({x['video_id'] for x in c})), len(c), any(x['in_machine_b_portable_inventory'] == 'yes' for x in c), c[0]['path']])
inv = [r for r in rows if r['in_machine_b_portable_inventory'] == 'yes']
invh = {r['sha256'] for r in inv if r['sha256']}
s = dict(inventory_rows=len(inv), inventory_rows_existing=sum(r['exists'] for r in inv), inventory_hash_mismatches=sum(r['hash_matches_inventory'] is False for r in inv),
         inventory_unique_hashes=len(invh), inventory_unique_bytes=sum(by[h][0]['bytes'] for h in invh),
         by_video={v: dict(rows=sum(r['video_id'] == v for r in inv), unique_hashes=len({r['sha256'] for r in inv if r['video_id'] == v})) for v in ROOTS},
         extra_rows_outside_inventory=len(rows) - len(inv), all_unique_hashes=len(by), all_unique_bytes=sum(c[0]['bytes'] for c in by.values()),
         recovery_count='PROVISIONAL: no join against UNAVAILABLE_UNIQUE_HASHES.csv yet')
(OUT / 'summary.json').write_text(json.dumps(s, indent=2) + '\n'); print(json.dumps(s, indent=2))
