"""Collect Google Trends interest-over-time around each video's publication date (stdlib only).
Writes TRENDS_RAW.json and TRENDS_WINDOWS.csv next to this file. Values are Google-normalized 0-100 within each request."""
import csv, datetime, http.cookiejar, json, statistics, time, urllib.parse, urllib.request
from pathlib import Path
OUT = Path(__file__).parent
VIDEOS = [  # video_id, publish date (YouTube publishDate, local), search term
    ('qF3ekm9Gx_E', '2025-03-19', 'great depression'), ('APlGPpM-nBo', '2025-08-26', '2008 financial crisis'),
    ('x_MZu-QF-6o', '2025-06-11', 'japan lost decade'), ('3tVMjRRXQIg', '2024-03-26', 'switzerland economy'),
    ('N9GUfsfiM4M', '2024-09-08', 'dubai history'), ('nr5dcBPACH0', '2026-03-22', 'greece debt crisis'),
    ('Iwz0fhJWN9Q', '2026-07-29', 'the big short'), ('rl6ggpS13ao', '2026-05-31', 'roman empire'),
    ('xVhMZPiIIGs', '2026-01-31', 'norway economy'), ('VTx478EUybo', '2025-11-11', 'great depression'),
    ('kbPauzdHhcI', '2026-09-19', 'lee kuan yew')]
jar = http.cookiejar.CookieJar(); op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
op.addheaders = [('User-Agent', 'Mozilla/5.0'), ('Accept-Language', 'en-US')]
op.open('https://trends.google.com/trends/?geo=US').read()
def get(url):
    for i in range(4):
        try: return json.loads(op.open(url, timeout=30).read().decode()[5:].lstrip("'\n,"))
        except Exception as e: err = e; time.sleep(10*(i+1))
    raise err
def series(term, start, end, prop):
    req = {'comparisonItem': [{'keyword': term, 'geo': '', 'time': f'{start} {end}'}], 'category': 0, 'property': prop}
    ex = get('https://trends.google.com/trends/api/explore?hl=en-US&tz=0&req=' + urllib.parse.quote(json.dumps(req)))
    w = next(x for x in ex['widgets'] if x['id'] == 'TIMESERIES'); time.sleep(2)
    d = get('https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=0&req=' + urllib.parse.quote(json.dumps(w['request'])) + '&token=' + w['token'])
    return [(datetime.datetime.fromtimestamp(int(p['time']), datetime.timezone.utc).date().isoformat(), p['value'][0]) for p in d['default']['timelineData']]
today = datetime.date(2026, 10, 13); raw = {}; rows = []
for vid, pub, term in VIDEOS:
    p = datetime.date.fromisoformat(pub); s = p - datetime.timedelta(days=90); e = min(p + datetime.timedelta(days=60), today)
    for prop in ['youtube', '']:
        pts = series(term, s, e, prop); time.sleep(3)
        raw[f'{vid}|{prop or "web"}'] = dict(term=term, geo='WORLDWIDE', property=prop or 'web', range=f'{s} {e}', points=pts)
        def avg(a, b):
            v = [x for d, x in pts if a <= (datetime.date.fromisoformat(d) - p).days <= b]
            return round(statistics.mean(v), 1) if v else ''
        peak = max(pts, key=lambda z: z[1]) if pts else ('INSUFFICIENT_DATA', '')
        rows.append(dict(video_id=vid, term=term, property=prop or 'web', geo='WORLDWIDE', range=f'{s} {e}', publish_date=pub,
                         avg_d90_to_d31=avg(-90, -31), avg_d30_to_d8=avg(-30, -8), avg_d7_to_d1=avg(-7, -1), avg_pub_week=avg(0, 6),
                         avg_d7_to_d30=avg(7, 30), avg_d31_to_d60=avg(31, 60), peak_date=peak[0], peak_value=peak[1],
                         zero_share=round(sum(x == 0 for _, x in pts)/len(pts), 2) if pts else 'NO_POINTS', retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')))
        print(rows[-1]['video_id'], rows[-1]['property'], rows[-1]['avg_d30_to_d8'], rows[-1]['avg_pub_week'], rows[-1]['peak_date'], flush=True)
(OUT/'TRENDS_RAW.json').write_text(json.dumps(raw, indent=0) + '\n')
with (OUT/'TRENDS_WINDOWS.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n'); w.writeheader(); w.writerows(rows)
