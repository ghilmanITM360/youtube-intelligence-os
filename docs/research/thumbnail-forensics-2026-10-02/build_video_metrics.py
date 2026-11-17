"""Join canonical video metrics to thumbnails by exact YouTube video ID (public metrics only) and classify cohorts.

Metric_Observation_Date: exact `video_snapshots.observed_at` when the inventory DB holds one (667 videos); otherwise the
dataset manifest's `Date Ingested` (a conservative upper bound on when the numbers were observed; flagged).
Performance classes are channel- and format-normalised and age-matched; they describe lifetime public views, NOT thumbnail quality.
Private first-party Studio metrics are deliberately absent from this public-metric file.
"""
import csv, re, sqlite3
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REG = sqlite3.connect(ROOT / 'data/catalog/youtube_channel_registry.db')
INV = sqlite3.connect(ROOT / 'data/catalog/youtube_inventory.db')


def ds_date(ds):
    t = (ROOT / f'data/manifests/{ds}.md').read_text()
    m = re.search(r'Date Ingested:\s*(\d{4}-\d{2}-\d{2})', t) or re.search(r'(20\d{2}-\d{2}-\d{2})', t)
    return m.group(1) if m else ''


def parse(d):
    try: return datetime.fromisoformat(d.replace('Z', '+00:00')[:19]).replace(tzinfo=timezone.utc)
    except Exception: return None


snap = {}
for yv, obs in INV.execute('select v.youtube_video_id, max(s.observed_at) from video_snapshots s join videos v using(video_id) group by 1'): snap[yv] = obs
dsets = {v: d for d, v in REG.execute('select dataset_id,youtube_video_id from dataset_videos')}
dd = {d: ds_date(d) for d in set(dsets.values())}
U = {r['Video_ID']: r for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID'] and r['Evidence_Class'] in ('REGISTERED_LOCAL_THUMBNAIL', 'CURRENT_PUBLIC_THUMBNAIL')}
rows = []
for vid, ch, title, pub, vt, views, likes, comments in REG.execute('select youtube_video_id,canonical_channel_id,title,published_at,video_type,views,likes,comments from videos'):
    obs, src = (snap[vid], 'INVENTORY_VIDEO_SNAPSHOT_EXACT') if vid in snap else (dd[dsets[vid]], 'DATASET_MANIFEST_DATE_INGESTED_UPPER_BOUND')
    po, oo = parse(pub), parse(obs)
    age = round((oo - po).total_seconds() / 86400, 1) if po and oo and oo >= po else ''
    u = U.get(vid, {})
    rows.append(dict(Video_ID=vid, Channel_ID=ch, Dataset_ID=dsets[vid], Format=u.get('Format', ''), Title=title, Published_At=pub if po else '', Metric_Observation_Date=obs[:10], Metric_Date_Source=src,
                     Public_Views=views if views is not None else '', Likes=likes, Comments=comments, Video_Age_Days=age,
                     Views_Per_Day=round(views / max(age, 1), 2) if age != '' and views is not None else '', Thumbnail_ID=u.get('Thumbnail_ID', ''),
                     Creative_Temporal_Alignment=u.get('Creative_Temporal_Alignment', 'UNKNOWN')))
# cohorts: channel x format, age-matched percentile
by = {}
for r in rows: by.setdefault((r['Channel_ID'], r['Format']), []).append(r)
for k, g in by.items():
    ok = [r for r in g if r['Public_Views'] != '' and r['Video_Age_Days'] != '']
    for r in g:
        r['Cohort_Size'] = len(ok); r['Perf_Percentile_Age_Matched'] = ''; r['Performance_Class'] = 'INSUFFICIENT_COHORT'
        r['Performance_Method'] = 'age-matched views percentile within channel x format (nearest 12 by video age)'
        if r not in ok or len(ok) < 8: continue
        peers = sorted((p for p in ok if p is not r), key=lambda p: abs(p['Video_Age_Days'] - r['Video_Age_Days']))[:12]
        pv = np.array([p['Public_Views'] for p in peers])
        pct = float((pv < r['Public_Views']).mean() + 0.5 * (pv == r['Public_Views']).mean())
        r['Perf_Percentile_Age_Matched'] = round(pct, 3)
        r['Performance_Class'] = 'HIGH' if pct >= 0.75 else 'LOW' if pct <= 0.25 else 'MIDDLE'
with (HERE / 'video-metrics.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows), Counter(r['Performance_Class'] for r in rows), Counter(r['Metric_Date_Source'] for r in rows))
