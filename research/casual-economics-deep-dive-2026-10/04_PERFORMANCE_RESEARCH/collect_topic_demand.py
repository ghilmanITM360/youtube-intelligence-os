"""Cross-topic relative demand: 5-term comparisons anchored on 'great depression', YouTube search and web, worldwide, 2022-01-01..2026-10-13 (stdlib).
Writes TOPIC_DEMAND.csv and TOPIC_DEMAND_RAW.json. Values are 0-100 normalized within each comparison; the shared anchor allows rough cross-group scaling."""
import csv, http.cookiejar, json, statistics, time, urllib.parse, urllib.request
from pathlib import Path
OUT = Path(__file__).parent; RANGE = '2022-01-01 2026-10-13'
GROUPS = [['great depression', '2008 financial crisis', 'the big short', 'japan lost decade', 'roman empire'],
          ['great depression', 'switzerland economy', 'dubai history', 'greece debt crisis', 'norway economy'],
          ['great depression', 'lee kuan yew']]
jar = http.cookiejar.CookieJar(); op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
op.addheaders = [('User-Agent', 'Mozilla/5.0'), ('Accept-Language', 'en-US')]; op.open('https://trends.google.com/trends/?geo=US').read()
def get(url):
    for i in range(4):
        try: return json.loads(op.open(url, timeout=30).read().decode()[5:].lstrip("'\n,"))
        except Exception as e: err = e; time.sleep(10*(i+1))
    raise err
raw, rows = {}, []
for prop in ['youtube', '']:
    for g in GROUPS:
        req = {'comparisonItem': [{'keyword': k, 'geo': '', 'time': RANGE} for k in g], 'category': 0, 'property': prop}
        ex = get('https://trends.google.com/trends/api/explore?hl=en-US&tz=0&req=' + urllib.parse.quote(json.dumps(req)))
        w = next(x for x in ex['widgets'] if x['id'] == 'TIMESERIES'); time.sleep(2)
        d = get('https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=0&req=' + urllib.parse.quote(json.dumps(w['request'])) + '&token=' + w['token'])
        tl = d['default']['timelineData']; raw[f"{prop or 'web'}|{'+'.join(g)}"] = tl
        means = {k: statistics.mean(p['value'][i] for p in tl) for i, k in enumerate(g)}
        for k in g:
            rows.append(dict(property=prop or 'web', geo='WORLDWIDE', range=RANGE, group='+'.join(g), term=k, mean_interest=round(means[k], 2),
                             relative_to_great_depression=round(means[k]/means['great depression'], 3) if means['great depression'] else ''))
        print(prop or 'web', {k: round(v, 1) for k, v in means.items()}, flush=True); time.sleep(4)
(OUT/'TOPIC_DEMAND_RAW.json').write_text(json.dumps(raw) + '\n')
with (OUT/'TOPIC_DEMAND.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n'); w.writeheader(); w.writerows(rows)
