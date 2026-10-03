"""Build the canonical thumbnail universe (thumbnail-universe.csv/json) from the merged repository.

Rows: one per image-bearing evidence item. Video thumbnails carry Thumbnail_ID = THB-<sha256>.
Non-thumbnail images (screenshots, support frames, document images) get Asset_ID only until triage
overlays (asset-triage.csv, screenshot-thumbnail-register.csv) prove otherwise.
Perceptual / visual-family assignment is applied from visual-family-register.csv when present.
"""
import csv, json, sqlite3, hashlib
from collections import defaultdict, Counter
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REG = sqlite3.connect(ROOT / 'data/catalog/youtube_channel_registry.db')
INV = sqlite3.connect(ROOT / 'data/catalog/youtube_inventory.db')
# INFERENCE channel-scope niche labels (assigned from channel names and top titles; not platform data)
NICHE = {}
SENIOR = {'UCMJxAeBJ0d1JC937de1eZ0Q', 'UCQIzqH7QZ9viBYpOFqgSXMg', 'UCFpxvukIqCAUA7YizI-q9Dw', 'UCAYG0fzUyxv6OevH88qA45w', 'UC356D-NzdnznBOftTpYoBLw',
          'UCQcBYZxFW7YwNMU8-DsT3Uw', 'UCFuGMi0idGeyXl6wYK9hg7Q', 'UCXZi5JVeuTluazF-fYqQgNA'}
FINANCE = {'UCXzNNA2ngRpRiWvyA7eGd6w', 'UCTcOboZIhgrKHMDm-oTlTOg', 'UCkqzov98m_7niJOXwbRQgBA', 'UCxoC2voi0vPg2hwqgfjdhYw', 'UC6AwWrRKNrwt83CMJqeTUzw',
           'UCAKBDBaY1dP7OdZkGPiDnug', 'UCFvEZUMNoAVjSoSB8NrV7yw', 'UCDglfjh__GM2RFM1oAL3a6A', 'UC5ZSqmk7PKry99xdiRDrc0A', 'UCCEwJbv7D1CYzxdKYYOH6AA',
           'UCP9RPj_BG0vit2TNM7LuRxA', 'UC14Fb2zWTEZklONPXFbLrTQ', 'UC9m3w-9L_Bt34x02IQXQ5kg', 'UC1GwXFBhh1fiLLuZxs8VRXA'}
ROLEPLAY = {'UC96yqt8xjtShTpgdoIo0Lqg', 'UC0L9hD7HMwWU7xuU5HRA6Iw', 'UCeVwhrEnYjCNdaDr47x4dSw', 'UCNO35SZS-e3f1hLIDon_mag', 'UCm1yxl_4qMbStLHpHQu6xWg', 'UCJgTBuO9fbNvgL_IS8pqtqg'}
ANCIENT = {'UC53wkzZ3aXyeH9-eIgi17WA', 'UCK8TbMQGDbB94EOR3aGJo3Q', 'UCaS30yIIV6y2zqSnHGdIGMQ', 'UCcWtWryYdHHiNWfZGSROl1A', 'UCmYG4TVuzHphjTrP3YKYGYQ',
           'UCpgrEMx8diLrw7YNQ6r3uUw', 'UCxyQ6jK98CCOsy-gwV8QaFA', 'UChGF6aMxELhXOKg2EDDLYNg', 'UCS3iXffTKXrhKWGXaPckb8A', 'UC9ibMPcwu9pesqKEyzlut7w',
           'UCFKmBxFC3dOkUv1GirzTjww', 'UChFs6t9iB1yv0X8fuKtNIvA'}
for c, lab in [(SENIOR, 'SENIOR_HEALTH'), (FINANCE, 'FINANCE_POV_EXPLAINER'), (ROLEPLAY, 'HISTORY_ROLEPLAY_POV'), (ANCIENT, 'ANCIENT_HUMANS_ANIMAL_SURVIVAL_EXPLAINER')]:
    for x in c: NICHE[x] = lab
NICHE['UCQTcmLiL5_HMUnO1GRwCdjQ'] = 'FITNESS_HEALTH'
FIELDS = ['Thumbnail_ID', 'Asset_ID', 'Video_ID', 'Channel_ID', 'Channel_Name', 'Dataset_IDs', 'Format', 'Title',
          'Published_At', 'Niche_Label', 'Internal_Channel_ID', 'Internal_Video_ID', 'Source_Type', 'Source_Path', 'Source_URL', 'Source_Observation_Date', 'SHA256', 'Width',
          'Height', 'Aspect_Ratio', 'Evidence_Class', 'Mapping_Confidence', 'Inspection_Status', 'Creative_Version_ID',
          'Creative_Temporal_Alignment', 'Exact_Duplicate_Group', 'Visual_Family_ID', 'Recovery_Status', 'Notes']


def fmt(video_type, dur):
    t = (video_type or '').lower()
    if t in ('short', 'shorts'): return 'SHORTS'
    if t in ('video', 'regular video'): return 'LONG_FORM'
    return 'SHORTS_BY_DURATION' if dur is not None and dur <= 60 else 'LONG_FORM_BY_DURATION'


vids = {}
for vid, ch, title, pub, vt, dur, url in REG.execute(
        "select youtube_video_id,canonical_channel_id,title,published_at,video_type,duration_seconds,coalesce(thumbnail_url,'') from videos"):
    vids[vid] = dict(ch=ch, title=title, pub=pub, fmt=fmt(vt, dur), url=url)
chname = dict(REG.execute('select canonical_channel_id,channel_name from channels'))
dsets = defaultdict(list)
for d, v in REG.execute('select dataset_id,youtube_video_id from dataset_videos order by 1'): dsets[v].append(d)
assert len(vids) == 2303, len(vids)
ivmap = {y: (v, c) for v, y, c in INV.execute('select video_id,youtube_video_id,channel_id from videos')}


def base(vid):
    v = vids[vid]
    return dict(Video_ID=vid, Channel_ID=v['ch'], Channel_Name=chname.get(v['ch'], ''), Niche_Label=NICHE.get(v['ch'], 'GENERAL_EXPLAINER') + ' (INFERENCE_channel_scope)',
                Internal_Channel_ID=ivmap.get(vid, ('', ''))[1], Internal_Video_ID=ivmap.get(vid, ('', ''))[0], Dataset_IDs=';'.join(dsets[vid]),
                Format=v['fmt'], Title=v['title'], Published_At=v['pub'])


def dims(p):
    with Image.open(p) as im: return im.width, im.height


rows = []
covered = set()
# 1. registered local snapshots (tracked in git)
for m in sorted((ROOT / 'data/manifests').glob('DS-*-thumbnail-snapshot-*.json')):
    for s in json.loads(m.read_text())['snapshots']:
        vid = s['original_registered_url'].split('/vi/')[1].split('/')[0]
        rel = 'data/raw/competitors/' + s['local_path'].split('/data/raw/competitors/')[1]
        p = ROOT / rel
        assert hashlib.sha256(p.read_bytes()).hexdigest() == s['sha256'], rel
        w, h = dims(p)
        covered.add(vid)
        rows.append(dict(base(vid), Thumbnail_ID='THB-' + s['sha256'], Asset_ID='AS-' + s['sha256'], Source_Type='CURRENT_REMOTE_SNAPSHOT',
                         Source_Path=rel, Source_URL=s['original_registered_url'], Source_Observation_Date=s['retrieval_timestamp'],
                         SHA256=s['sha256'], Width=w, Height=h, Evidence_Class='REGISTERED_LOCAL_THUMBNAIL',
                         Mapping_Confidence='HASH_VERIFIED_MANIFEST', Creative_Temporal_Alignment='CURRENT_PUBLIC_ONLY',
                         Recovery_Status='RESOLVED_PRIMARY_URL', Notes='manifest ' + m.name))
# 2. zero-spend recovery
rec = json.loads((ROOT / 'data/manifests/thumbnail-recovery-2026-10-04.json').read_text())
for r in rec['results']:
    vid = r['video_id']
    if r['status'].startswith('RESOLVED'):
        p = ROOT / r['path']
        assert hashlib.sha256(p.read_bytes()).hexdigest() == r['sha256']
        covered.add(vid)
        rows.append(dict(base(vid), Thumbnail_ID='THB-' + r['sha256'], Asset_ID='AS-' + r['sha256'], Source_Type='CURRENT_PUBLIC_FETCH',
                         Source_Path=r['path'], Source_URL=r['final_url'], Source_Observation_Date=r['captured_at'], SHA256=r['sha256'],
                         Width=r['width'], Height=r['height'], Evidence_Class='CURRENT_PUBLIC_THUMBNAIL',
                         Mapping_Confidence='EXACT_VIDEO_ID_IN_URL', Creative_Temporal_Alignment='CURRENT_PUBLIC_ONLY',
                         Recovery_Status=r['status'], Notes='local-only raw image; manifest data/manifests/thumbnail-recovery-2026-10-04.json'))
    else:
        rows.append(dict(base(vid), Source_Type='NO_IMAGE', Source_URL=vids[vid]['url'], Source_Observation_Date=r['captured_at'],
                         Evidence_Class='URL_ONLY_THUMBNAIL', Mapping_Confidence='EXACT_VIDEO_ID', Inspection_Status='NO_IMAGE',
                         Creative_Temporal_Alignment='UNKNOWN', Recovery_Status=r['status'],
                         Notes='attempts: ' + ' ; '.join(r['attempts'])[:400]))
# 3. non-thumbnail image assets from the B000 inventory
ROLE = {'ACQUISITION_SCREENSHOT_PENDING_REVIEW': 'UI_OR_PREFLIGHT_IMAGE', 'FORENSIC_SUPPORT_IMAGE_PENDING_REVIEW': 'FORENSIC_SUPPORT_IMAGE',
        'SCREENSHOT_PENDING_THUMBNAIL_EXTRACTION': 'UNKNOWN_IMAGE', 'IMAGE_UNCLASSIFIED': 'UNKNOWN_IMAGE'}
tri = {}
if (HERE / 'asset-triage.csv').exists():
    tri = {r['Asset_ID']: r for r in csv.DictReader((HERE / 'asset-triage.csv').open())}
for r in csv.DictReader((HERE / 'asset-inventory.csv').open()):
    if r['role'] not in ROLE or r['decode_status'] != 'ACCESSIBLE': continue
    loc = r['location']
    cls = ROLE[r['role']]
    if '!/' in loc: cls = 'DOCUMENT_EMBEDDED_IMAGE'
    t = tri.get(r['asset_id'], {})
    rows.append(dict(Asset_ID=r['asset_id'], Source_Type='REPO_FILE' if '!/' not in loc else 'DOCUMENT_MEMBER', Source_Path=loc,
                     SHA256=r['sha256'], Width=r['width'], Height=r['height'], Evidence_Class=t.get('Evidence_Class') or cls,
                     Mapping_Confidence='NOT_MAPPED', Inspection_Status=t.get('Inspection_Status', 'NOT_INSPECTED'),
                     Creative_Temporal_Alignment='UNKNOWN', Notes=t.get('Notes', '')))
# 4. canonical videos with neither image nor recovery attempt
for vid in vids:
    if vid not in covered and not any(r.get('Video_ID') == vid for r in rows):
        rows.append(dict(base(vid), Source_Type='NO_IMAGE', Evidence_Class='URL_ONLY_THUMBNAIL', Inspection_Status='NO_IMAGE',
                         Creative_Temporal_Alignment='UNKNOWN', Recovery_Status='NOT_ATTEMPTED'))
# derived columns
for r in rows:
    try: r['Aspect_Ratio'] = round(int(r['Width']) / int(r['Height']), 4)
    except Exception: r['Aspect_Ratio'] = ''
    r.setdefault('Inspection_Status', 'NOT_INSPECTED')
    r['Inspection_Status'] = r.get('Inspection_Status') or 'NOT_INSPECTED'
    if r.get('Thumbnail_ID'):
        r['Creative_Version_ID'] = f"CV-{r['Video_ID']}-{r['SHA256'][:10]}"
grp = defaultdict(list)
for r in rows:
    if r.get('SHA256'): grp[r['SHA256']].append(r)
n = 0
for h, g in sorted(grp.items()):
    if len(g) > 1:
        n += 1
        for r in g: r['Exact_Duplicate_Group'] = f'XD-{n:04d}'
vf = {}
if (HERE / 'visual-family-register.csv').exists():
    vf = {r['Thumbnail_ID']: r['Visual_Family_ID'] for r in csv.DictReader((HERE / 'visual-family-register.csv').open())}
for r in rows:
    r['Visual_Family_ID'] = vf.get(r.get('Thumbnail_ID'), '')
    for f in FIELDS: r.setdefault(f, '')
rows.sort(key=lambda r: (r['Evidence_Class'], r['Video_ID'], r['Source_Path']))
with (HERE / 'thumbnail-universe.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, FIELDS); w.writeheader(); w.writerows(rows)
(HERE / 'thumbnail-universe.json').write_text(json.dumps(rows, indent=1))
c = Counter(r['Evidence_Class'] for r in rows)
print(len(rows), dict(c), 'dup groups', n)
print('videos with image', len({r['Video_ID'] for r in rows if r['Thumbnail_ID']}), 'of', len(vids))
