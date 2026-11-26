"""Phase 14 (F14): recompute SHA-256 of every media file in the inventory (read-only) and compare with the stored value; also report file-size, ffprobe duration drift not rechecked.
usage: python3 -I scripts/phase14_hash_verify.py"""
import csv, hashlib, os, json, collections
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = [r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv')) if r['local_media_path']]
out = []
for r in rows:
    p = r['local_media_path']
    if not os.path.exists(p): out.append(dict(video_id=r['video_id'], status='PATH_MISSING', stored=r['sha256'], recomputed='', size=''))
    else:
        h = hashlib.sha256()
        with open(p, 'rb') as f:
            for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
        out.append(dict(video_id=r['video_id'], status='MATCH' if h.hexdigest() == r['sha256'] else 'MISMATCH', stored=r['sha256'], recomputed=h.hexdigest(), size=os.path.getsize(p)))
w = csv.DictWriter(open(A + '/14_HASH_VERIFY_88.csv', 'w', newline=''), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
c = collections.Counter(o['status'] for o in out); dup = collections.Counter(o['recomputed'] for o in out if o['recomputed'])
print(json.dumps(dict(rows_with_path=len(out), **c, distinct_hashes=len(dup), duplicate_hash_groups=sum(1 for v in dup.values() if v > 1))))
