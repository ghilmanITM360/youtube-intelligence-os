"""Merge research/reference_fragments/*.json into research/REFERENCE_MANIFEST.csv and research/ANIMATION_EXAMPLES.csv.
Verifies every claimed file exists, recomputes sha256/size/pixel dimensions from the file on disk, and reports problems.
usage: python3 tools/merge_references.py      (exit 1 if a hard problem is found)
"""
import csv, glob, hashlib, json, os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))

def asset_ids():
    return {r['asset_id'] for r in csv.DictReader(open(os.path.join(ROOT, 'MASTER_ASSET_MANIFEST.csv')))}

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''): h.update(ch)
    return h.hexdigest()

COLS = ['ref_id', 'family', 'local_filename', 'source_url', 'source_page_url', 'source_org', 'title', 'camera_perspective', 'visible_characteristics',
        'viewed', 'asset_ids', 'scientific_relevance', 'production_influence', 'licence_status', 'licence_evidence_url', 'credit_line',
        'local_w', 'local_h', 'local_bytes', 'sha256_local', 'orig_width', 'orig_height', 'orig_bytes', 'sha256_original', 'retrieved', 'notes']
ACOLS = ['id', 'family', 'title', 'url', 'org', 'kind', 'timestamp_or_frame', 'technique', 'why_it_helps_viewers', 'application_slot07', 'review_mode', 'evidence_files']

def main():
    ids = asset_ids(); refs = []; anims = []; problems = []; warnings = []; gaps = {}
    for fn in sorted(glob.glob(os.path.join(ROOT, 'research', 'reference_fragments', '*.json'))):
        try: d = json.load(open(fn))
        except Exception as e: problems.append('%s: invalid JSON (%s)' % (os.path.basename(fn), e)); continue
        fam = d.get('family', os.path.basename(fn)[:-5])
        gaps[fam] = d.get('gaps', [])
        for r in d.get('refs', []):
            row = {c: r.get(c, '') for c in COLS}; row['family'] = fam
            if isinstance(r.get('asset_ids'), list): row['asset_ids'] = ' '.join(r['asset_ids'])
            for a in row['asset_ids'].split():
                if a not in ids: problems.append('%s: unknown asset id %s' % (r.get('ref_id'), a))
            lf = r.get('local_filename', ''); status = r.get('licence_status', '')
            if status != 'LINK_ONLY':
                p = os.path.join(ROOT, lf)
                if not lf or not os.path.isfile(p): problems.append('%s: file missing: %s' % (r.get('ref_id'), lf)); continue
                row['local_bytes'] = os.path.getsize(p); row['sha256_local'] = sha(p)
                try:
                    with Image.open(p) as im: row['local_w'], row['local_h'] = im.size
                except Exception: row['local_w'] = row['local_h'] = ''
                if not r.get('viewed'): warnings.append('%s: viewed is not true (description unverified)' % r.get('ref_id'))
                if not r.get('visible_characteristics'): problems.append('%s: no visible_characteristics' % r.get('ref_id'))
            if not (r.get('source_url') or r.get('source_page_url')): problems.append('%s: no source URL' % r.get('ref_id'))
            if not status: problems.append('%s: no licence_status' % r.get('ref_id'))
            refs.append(row)
        for e in d.get('animation_examples', []):
            row = {c: e.get(c, '') for c in ACOLS}; row['family'] = fam
            if isinstance(e.get('evidence_files'), list):
                row['evidence_files'] = ' | '.join(e['evidence_files'])
                for ef in e['evidence_files']:
                    if not os.path.exists(os.path.join(ROOT, ef)): problems.append('%s: evidence file missing: %s' % (e.get('id'), ef))
            if e.get('review_mode') in ('WATCHED', 'FRAME_SAMPLED') and not e.get('evidence_files'):
                problems.append('%s: %s without evidence files' % (e.get('id'), e.get('review_mode')))
            anims.append(row)
    seen = set()
    for r in refs:
        if r['ref_id'] in seen: problems.append('duplicate ref_id %s' % r['ref_id'])
        seen.add(r['ref_id'])
    with open(os.path.join(ROOT, 'research', 'REFERENCE_MANIFEST.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, COLS); w.writeheader(); w.writerows(refs)
    with open(os.path.join(ROOT, 'research', 'ANIMATION_EXAMPLES.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, ACOLS); w.writeheader(); w.writerows(anims)
    by = {}
    for r in refs: by.setdefault(r['family'], [0, 0]); by[r['family']][r['licence_status'] == 'LINK_ONLY'] += 1
    print('refs %d (saved/link-only per family: %s)' % (len(refs), {k: tuple(v) for k, v in by.items()}))
    print('animation examples %d; modes: %s' % (len(anims), {m: sum(1 for a in anims if a['review_mode'] == m) for m in {a['review_mode'] for a in anims}}))
    for w_ in warnings: print('WARN', w_)
    for p in problems: print('PROBLEM', p)
    return 1 if problems else 0

if __name__ == '__main__':
    sys.exit(main())
