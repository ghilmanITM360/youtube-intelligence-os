"""Build screenshot-thumbnail-register.csv from the OCR/mapping output plus manual visual review.

Manual review (2026-10-04, crop vs current thumbnail side by side) of the 7 tiles whose title matched but whose
perceptual distance was >12 or whose mapping stayed ambiguous:
  same creative (crop framing differs):  SS-005 T04, SS-087 T01, SS-106 T02, SS-106 T03
  creative CHANGED (title match, art differs): SS-087 T03  (screenshot shows CLEAN VESSELS WHILE YOU SLEEP; current art is DO THIS BRAIN VESSELS)
  not a thumbnail:                        SS-001 T03 (blank panel)
  mapping stays AMBIGUOUS:                SS-106 T01 (real thumbnail; title only 0.895 similar to one registry title, no visual match)
Screenshot-only tiles (channels with no registry rows) are deduplicated by pHash<=6 over overlapping scroll positions.
"""
import csv, json, glob, re
from pathlib import Path
import imagehash
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SAME = {('SS-005', 'T04'), ('SS-087', 'T01'), ('SS-106', 'T02'), ('SS-106', 'T03')}
CHANGED = {('SS-087', 'T03')}
NOT_TILE = {('SS-001', 'T03')}
HANDLE_LABEL = {'@Dr.Adewale': 'Dr. Adewale', '@Mr.Greendude': 'Dr. Waterling', '@theseniorhealthpodcast': 'The Senior Health Podcast',
                '@TheHealthEducator05': 'The Health Educator', '@DrThomasSeniorHealthTips': 'Doctor Thomas', '@drmarcusokoro': 'Dr. Okoro',
                '@Dr.AlizaWrightAdvice': 'Dr. Aliza Wright | Advice', '@Health.Hub.Senior': 'Senior Health Hub'}


def handles():
    out = {}
    for f in glob.glob(str(HERE / 'screenshot-transcriptions/part-*.json')):
        for s in json.load(open(f)):
            h = s.get('handle_visible') or ''
            for k in HANDLE_LABEL:
                if h.startswith(k): out[s['screenshot_id']] = k
    return out


def rhash(path):
    im = Image.open(ROOT / path).convert('RGB'); w, h = im.size
    return imagehash.phash(im.crop((int(w * .03), int(h * .03), int(w * .97), int(h * .82))))


if __name__ == '__main__':
    hm = handles()
    rows = list(csv.DictReader((HERE / 'screenshot-tile-ocr.csv').open()))
    out = []
    for r in rows:
        key = (r['Screenshot_Source_ID'], r['Tile'])
        st = r['Match_Status']
        m = re.search(r'Screenshot (\d{4}-\d{2}-\d{2})', r['Screenshot_Path'])
        d = m.group(1) if m else ''
        h = hm.get(r['Screenshot_Source_ID'], '')
        if key in NOT_TILE or st == 'NOT_A_VIDEO_TILE': status, rel = 'NOT_A_THUMBNAIL', ''
        elif st.startswith('MATCHED'):
            status = 'MAPPED_TO_REGISTRY_VIDEO'
            rel = 'CREATIVE_CHANGED_VERIFIED' if key in CHANGED else 'SAME_CREATIVE_AS_CURRENT' if key in SAME or (r['Visual_Distance_To_Current'] and int(r['Visual_Distance_To_Current']) <= 12) else 'NO_CURRENT_IMAGE_SCREENSHOT_IS_ONLY_EVIDENCE' if not r['Visual_Distance_To_Current'] else 'UNREVIEWED'
        elif st == 'AMBIGUOUS_MAPPING': status, rel = 'AMBIGUOUS_MAPPING', ''
        else: status, rel = 'SCREENSHOT_ONLY_NOT_IN_REGISTRY', ''
        out.append(dict(Screenshot_Source_ID=r['Screenshot_Source_ID'], Tile=r['Tile'], Screenshot_Path=r['Screenshot_Path'], Screenshot_SHA256=r['Screenshot_SHA256'],
                        X=r['X'], Y=r['Y'], W=r['W'], H=r['H'], Crop_Path=r['Crop_Path'], Crop_SHA256=r['Crop_SHA256'], Screenshot_Observation_Date=d,
                        Channel_Handle=h, Channel_Label=HANDLE_LABEL.get(h, ''), OCR_Title=r['OCR_Title'], OCR_Views=r['OCR_Views'], OCR_Age=r['OCR_Age'],
                        Mapping_Status=status, Video_ID=r['Video_ID'] if status == 'MAPPED_TO_REGISTRY_VIDEO' else '', Twin_Registry_Video_ID=r['Twin_Registry_Video_ID'],
                        Match_Score=r['Match_Score'], Visual_Distance_To_Current=r['Visual_Distance_To_Current'], Creative_Relation=rel, Cluster_ID='', Canonical_In_Cluster=''))
    # cluster unmapped (screenshot-only / ambiguous) tiles across overlapping scrolls
    idx = [i for i, o in enumerate(out) if o['Mapping_Status'] in ('SCREENSHOT_ONLY_NOT_IN_REGISTRY', 'AMBIGUOUS_MAPPING')]
    hs = {i: rhash(out[i]['Crop_Path']) for i in idx}
    par = {i: i for i in idx}
    def f(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for a in idx:
        for b in idx:
            if a < b and out[a]['Channel_Handle'] == out[b]['Channel_Handle'] and hs[a] - hs[b] <= 6: par[f(a)] = f(b)
    members = {}
    for i in idx: members.setdefault(f(i), []).append(i)
    for n, (root, mem) in enumerate(sorted(members.items(), key=lambda kv: min(kv[1])), 1):
        for j, i in enumerate(sorted(mem)):
            out[i]['Cluster_ID'] = f'SSU-{n:03d}'; out[i]['Canonical_In_Cluster'] = 'Y' if j == 0 else 'N'
    # mapped tiles: one canonical observation per (video, screenshot date)
    seen = set()
    for o in out:
        if o['Mapping_Status'] == 'MAPPED_TO_REGISTRY_VIDEO':
            k = (o['Video_ID'], o['Screenshot_Observation_Date'])
            o['Canonical_In_Cluster'] = 'N' if k in seen else 'Y'; seen.add(k)
    with (HERE / 'screenshot-thumbnail-register.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(out[0])); w.writeheader(); w.writerows(out)
    from collections import Counter
    print(len(out), Counter(o['Mapping_Status'] for o in out), 'unique screenshot-only clusters', len({o['Cluster_ID'] for o in out if o['Cluster_ID']}),
          'mapped videos', len({o['Video_ID'] for o in out if o['Video_ID']}), Counter(o['Creative_Relation'] for o in out if o['Creative_Relation']))
