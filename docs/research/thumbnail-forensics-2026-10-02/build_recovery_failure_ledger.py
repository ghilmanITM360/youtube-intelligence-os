"""Per-Video_ID thumbnail-recovery failure ledger: separates unique failed videos, failed HTTP requests and final no-image videos."""
import csv, json, re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
m = json.loads((ROOT / 'data/manifests/thumbnail-recovery-2026-10-04.json').read_text())
uni = list(csv.DictReader((HERE / 'thumbnail-universe.csv').open()))
scr = {r['Video_ID'] for r in csv.DictReader((HERE / 'screenshot-thumbnail-register.csv').open()) if r['Mapping_Status'] == 'MAPPED_TO_REGISTRY_VIDEO'}
has_image = {r['Video_ID'] for r in uni if r['Evidence_Class'] in ('REGISTERED_LOCAL_THUMBNAIL', 'CURRENT_PUBLIC_THUMBNAIL')}
rows, codes = [], Counter()
for r in m['results']:
    if r['status'].startswith('RESOLVED'): continue
    a = [x.split('|') for x in r['attempts']]
    c = Counter(x[1] for x in a); codes.update(c)
    vid = r['video_id']
    rows.append(dict(Video_ID=vid, Recovery_Status=r['status'], Thumbnail_Variants_Tried=len(a), Failed_Thumbnail_Requests=len(a),
                     Thumbnail_HTTP_Codes=';'.join(f'{k}x{v}' for k, v in sorted(c.items())), OEmbed_HTTP=r.get('oembed_http', ''),
                     Failed_Requests_Total=len(a) + (1 if r.get('oembed_http') not in (None, 200) else 0),
                     Has_Local_Image=vid in has_image, Screenshot_Evidence=vid in scr,
                     Final_State='NO_ACCESSIBLE_IMAGE' if vid not in has_image and vid not in scr else 'IMAGE_ONLY_VIA_SCREENSHOT',
                     Captured_At=r['captured_at']))
with (HERE / 'recovery-failure-ledger.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
fin = Counter(r['Final_State'] for r in rows)
print(dict(unique_failed_videos=len(rows), failed_thumbnail_requests=sum(r['Failed_Thumbnail_Requests'] for r in rows), thumbnail_codes=dict(codes),
           oembed=dict(Counter(str(r['OEmbed_HTTP']) for r in rows)), by_status=dict(Counter(r['Recovery_Status'] for r in rows)), final=dict(fin)))
