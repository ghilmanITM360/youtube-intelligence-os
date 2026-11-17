# usage: python3 -I setup_pipeline.py
# Splits the 4 multi-channel Apify Console datasets (R1-R4) into per-channel raw dataset + run records and copies the
# 2026-11-10 normalizer/backfill scripts into ./pipeline with a PLAN for the new channels. No network, no DB.
import json, os, re, shutil, collections
B = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(B, 'raw'); P = os.path.join(B, 'pipeline')
SRC = os.path.expanduser('~/YIOS-local-audits/2026-11-10-finance-apify-run')
# run -> (file, run id, dataset id, started UTC, finished UTC, max cost, maxResults). Console shows PKT (UTC+5); converted to UTC here.
RUNS = {
 'R1': ('R1_econ_new_Ejhif25dRKVknumlx_dataset.json', 'Ejhif25dRKVknumlx', 'PIokdgghg8DOt6VtB', '2026-11-11T17:06:47.000Z', '2026-11-11T17:10:21.000Z', 0.8, 70),
 'R2': ('R2_econ_existing_7lzjT07IszJcXXByf_dataset.json', '7lzjT07IszJcXXByf', 'NCbFUX075iKoePtaA', '2026-11-11T17:12:43.000Z', '2026-11-11T17:15:57.000Z', 0.8, 60),
 'R3': ('R3_fin_small_326K8bk3f2xA2uT5B_dataset.json', '326K8bk3f2xA2uT5B', 'fsLEO1UtvYMPV07dt', '2026-11-11T17:16:57.000Z', '2026-11-11T17:29:45.000Z', 2.6, 170),
 'R4': ('R4_fin_big_DGVyhavl8Y2PCPWWh_dataset.json', 'DGVyhavl8Y2PCPWWh', 'RQg8IhClTEOM1WmdQ', '2026-11-11T17:21:23.000Z', '2026-11-11T17:25:44.000Z', 1.0, 40),
}
SLUG = lambda n: re.sub(r'[^a-z0-9]+', '', n.lower())
plan, removed = {}, []
os.makedirs(P, exist_ok=True)
for key, (fn, rid, dsid, st, fi, mx, lim) in RUNS.items():
    rows = json.load(open(os.path.join(RAW, fn)))
    by = collections.OrderedDict()
    for r in rows:
        cid = r.get('channelId') or (r.get('aboutChannelInfo') or {}).get('channelId')
        if r.get('error') == 'NO_VIDEOS': cid = re.search(r'channel/([^/]+)', r['input']).group(1); removed.append({'run': rid, 'channel_id': cid, 'row': r}); continue
        by.setdefault(cid, []).append(r)
    for cid, rs in by.items():
        name = (rs[0].get('aboutChannelInfo') or {}).get('channelName') or rs[0]['channelName']
        label = 'x_' + SLUG(name)
        json.dump(rs, open(os.path.join(RAW, f'{label}_{rid}_dataset.json'), 'w'))
        json.dump({'id': rid, 'defaultDatasetId': dsid, 'status': 'SUCCEEDED', 'buildNumber': '0.0.332', 'startedAt': st, 'finishedAt': fi,
                   'options': {'maxTotalChargeUsd': mx}, 'chargedEventCounts': {'result': len(rs)}, 'usageTotalUsd': round(0.004 * len(rs), 3),
                   'source': f'Apify Console run page (account CLAUDE Personal, owner browser session); dataset via Console signed export. Multi-channel run {key}; per-channel cost attribution = rows x $0.004.'},
                  open(os.path.join(RAW, f'{label}_{rid}_run.json'), 'w'), indent=1)
        plan[label] = (name, cid, 'X', None, [lim, 0, 0], round(0.004 * len(rs) + 0.01, 2))
json.dump(removed, open(os.path.join(B, 'UNAVAILABLE_CHANNELS.json'), 'w'), indent=1)
t = open(os.path.join(SRC, 'build_outputs.py')).read()
t = re.sub(r"PLAN = \{.*?\n\}\nPILOTS", 'PLAN = ' + json.dumps(plan, ensure_ascii=False, indent=1).replace('null', 'None') + '\nPILOTS', t, flags=re.S)
t = t.replace("ROOT = os.path.dirname(os.path.abspath(__file__))", "ROOT = os.path.dirname(os.path.abspath(__file__)); RAW_DIR = os.path.join(os.path.dirname(ROOT), 'raw')")
t = t.replace("RAW = os.path.join(ROOT, 'raw')", "RAW = RAW_DIR")
t = t.replace("'FINANCE_VIDEO_MASTER_ALL", "'NEW_VIDEO_MASTER_ALL")
open(os.path.join(P, 'build_outputs.py'), 'w').write(t)
print(len(plan), 'channels planned;', len(removed), 'unavailable:', [(x['channel_id'], x['row'].get('additionalData')) for x in removed])
