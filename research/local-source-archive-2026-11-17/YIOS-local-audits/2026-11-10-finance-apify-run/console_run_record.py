# usage: python3 -I console_run_record.py <label> <run_id> <dataset_id> <started_utc> <finished_utc> <max_usd> <build>
# Moves ~/Downloads/<label>_<run>_dataset.json into raw/ and writes a run record built from Console page values
# (account perspicacious_computer: runs are not public by ID). Charge is derived from dataset row count x $0.004.
import json, sys, os, shutil
label, rid, dsid, st, fi, mx, build = sys.argv[1:8]; acct = sys.argv[8] if len(sys.argv) > 8 else 'perspicacious_computer'
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'raw'); name = f'{label}_{rid}_dataset.json'
src = os.path.expanduser(f'~/Downloads/{name}')
if os.path.exists(src): shutil.move(src, os.path.join(R, name))
rows = json.load(open(os.path.join(R, name)))
run = {'id': rid, 'defaultDatasetId': dsid, 'status': 'SUCCEEDED', 'buildNumber': build, 'startedAt': st, 'finishedAt': fi,
       'options': {'maxTotalChargeUsd': float(mx)}, 'chargedEventCounts': {'result': len(rows)}, 'usageTotalUsd': round(0.004 * len(rows), 3),
       'source': 'Apify Console run page (owner session, account ' + acct + '); dataset via Console signed export; not public-by-ID API'}
json.dump(run, open(os.path.join(R, f'{label}_{rid}_run.json'), 'w'), indent=1)
types = {}
for r in rows: types[r.get('type')] = types.get(r.get('type'), 0) + 1
ch = {(r.get('channelId') or (r.get('aboutChannelInfo') or {}).get('channelId')) for r in rows}
print(json.dumps({'label': label, 'rows': len(rows), 'unique_ids': len({r.get('id') for r in rows}), 'types': types, 'channels': sorted(map(str, ch)),
  'members_only': sum(1 for r in rows if r.get('isMembersOnly')), 'with_subtitles': sum(1 for r in rows if r.get('subtitles')), 'usd': run['usageTotalUsd']}))
