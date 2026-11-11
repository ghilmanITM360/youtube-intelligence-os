# usage: python3 -I build_outputs.py   (run inside this folder). Builds per-channel files + SQLite DB from raw/ datasets.
import json, os, csv, sqlite3, hashlib, collections
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, 'raw')
RUNS = {'run1_QSwBSjJff8yJXnnNK': dict(run_id='QSwBSjJff8yJXnnNK', started='2026-11-11T21:43:10', max_results=50, cap=4.3, usd=1.840, note='21 channels, regular videos, limit 50 each'),
        'run2_ffSoyEykFOE9HdWax': dict(run_id='ffSoyEykFOE9HdWax', started='2026-11-11T21:55:51', max_results=200, cap=1.0, usd=0.564, note='top-up: Dr. Waterling + Vital Years Wellness, limit 200')}
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
db = os.path.join(H, 'senior_health_apify.db')
if os.path.exists(db): os.remove(db)
c = sqlite3.connect(db)
c.executescript('''
CREATE TABLE runs(run_id TEXT PRIMARY KEY, actor TEXT, build TEXT, started_utc TEXT, max_results_per_url INT, max_cost_usd REAL, charged_usd REAL, rows INT, raw_file TEXT, raw_sha256 TEXT, note TEXT);
CREATE TABLE channels(channel_id TEXT PRIMARY KEY, channel_name TEXT, handle TEXT, url TEXT, subscribers INT, channel_total_videos INT, channel_total_views INT, joined TEXT, description TEXT, videos_captured INT, coverage TEXT, first_run_id TEXT);
CREATE TABLE videos(video_id TEXT PRIMARY KEY, channel_id TEXT REFERENCES channels, title TEXT, url TEXT, published_utc TEXT, views INT, likes INT, comments INT, duration TEXT, description TEXT, hashtags TEXT, thumbnail_url TEXT, is_members_only INT, type TEXT, run_id TEXT REFERENCES runs, raw_json TEXT);
CREATE INDEX ix_v_ch ON videos(channel_id);
''')
toint = lambda x: int(x) if str(x).lstrip('-').isdigit() else None
vids = {}
for key, meta in RUNS.items():
    p = os.path.join(R, key + '_dataset.json'); rows = json.load(open(p))
    c.execute('INSERT INTO runs VALUES(?,?,?,?,?,?,?,?,?,?,?)', (meta['run_id'], 'streamers/youtube-scraper', '0.0.332', meta['started'], meta['max_results'], meta['cap'], meta['usd'], len(rows), 'raw/' + key + '_dataset.json', sha(p), meta['note']))
    for r in rows: vids[r['id']] = (r, meta['run_id'])  # later run wins (superset of the 50 newest)
chs = {}
for vid, (r, rid) in vids.items():
    cid = r['channelId']; chs.setdefault(cid, []).append((r, rid))
for cid, lst in chs.items():
    r0 = lst[0][0]; n = len(lst); tot = toint(r0.get('channelTotalVideos'))
    cov = 'COMPLETE' if tot is not None and n >= tot else ('PARTIAL' if tot else 'UNKNOWN')
    c.execute('INSERT INTO channels VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (cid, r0['channelName'], r0.get('channelUsername'), r0['channelUrl'], toint(r0.get('numberOfSubscribers')), tot, toint(r0.get('channelTotalViews')), r0.get('channelJoinedDate'), r0.get('channelDescription'), n, cov, lst[0][1]))
    for r, rid in lst:
        c.execute('INSERT INTO videos VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (r['id'], cid, r['title'], r['url'], r['date'], toint(r.get('viewCount')), toint(r.get('likes')), toint(r.get('commentsCount')), r.get('duration'), r.get('text'), json.dumps(r.get('hashtags')), r.get('thumbnailUrl'), int(bool(r.get('isMembersOnly'))), r.get('type'), rid, json.dumps(r, ensure_ascii=False)))
    d = os.path.join(H, 'channels', ''.join(ch if ch.isalnum() else '_' for ch in r0['channelName']).strip('_') + '_' + cid[:8]); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'VIDEO_MASTER.jsonl'), 'w') as f:
        for r, _ in sorted(lst, key=lambda x: x[0]['date'], reverse=True): f.write(json.dumps(r, ensure_ascii=False) + '\n')
c.commit()
with open(os.path.join(H, 'CHANNEL_STATUS.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['channel_id', 'channel_name', 'handle', 'subscribers', 'channel_total_videos', 'videos_captured', 'coverage'])
    for row in c.execute('select channel_id,channel_name,handle,subscribers,channel_total_videos,videos_captured,coverage from channels order by videos_captured desc'): w.writerow(row)
print(c.execute('select count(*),sum(videos_captured) from channels').fetchone(), c.execute('select count(*) from videos').fetchone(), c.execute('select coverage,count(*) from channels group by 1').fetchall())
