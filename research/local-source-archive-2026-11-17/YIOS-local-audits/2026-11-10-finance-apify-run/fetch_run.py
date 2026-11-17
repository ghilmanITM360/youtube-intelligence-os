# usage: python3 -I fetch_run.py <label> <run_id> <expected_channel_id>
# Fetches public-by-ID run + dataset (no token), saves raw, prints reconciliation line.
import json, sys, urllib.request, os, hashlib
label, rid, exp = sys.argv[1:4]
D = os.path.expanduser('~/YIOS-local-audits/2026-11-10-finance-apify-run/raw')
get = lambda u: urllib.request.urlopen(u, timeout=60).read()
run = json.loads(get(f'https://api.apify.com/v2/actor-runs/{rid}'))['data']
if run['status'] in ('READY', 'RUNNING'): print('STATUS', run['status']); sys.exit(2)
ds = get(f"https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items?format=json&clean=false")
rows = json.loads(ds)
for name, blob in ((f'{label}_{rid}_run.json', json.dumps(run, indent=1).encode()), (f'{label}_{rid}_dataset.json', ds)):
    open(os.path.join(D, name), 'wb').write(blob)
ids = [r.get('id') for r in rows]
bad = [r.get('id') for r in rows if (r.get('channelId') or (r.get('aboutChannelInfo') or {}).get('channelId')) != exp]
types = {}
for r in rows: types[r.get('type')] = types.get(r.get('type'), 0) + 1
print(json.dumps({'label': label, 'run_id': rid, 'status': run['status'], 'build': run.get('buildNumber'),
  'usd': run.get('usageTotalUsd'), 'max_usd': (run.get('options') or {}).get('maxTotalChargeUsd'),
  'charged_events': run.get('chargedEventCounts'), 'rows': len(rows), 'unique_ids': len(set(ids)),
  'types': types, 'channel_mismatch': bad, 'members_only': sum(1 for r in rows if r.get('isMembersOnly')),
  'with_subtitles': sum(1 for r in rows if r.get('subtitles')), 'dataset_id': run['defaultDatasetId']}))
