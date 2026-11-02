"""Freeze the historical-reanalysis population from the live accepted ledger (idempotent; never downgrades a ledger status).
Usage: python reanalysis/build_population.py   (run from repo root or anywhere)"""
import csv, glob, hashlib, json, pathlib, sqlite3, subprocess
H = pathlib.Path(__file__).resolve().parent; R = H.parent; ROOT = R.parents[1]
LEDGER = H / 'REANALYSIS_CAMPAIGN_LEDGER.csv'; FROZEN = H / 'REANALYSIS_POPULATION_v1.json'
rows = [json.loads(l) for l in open(R / 'VIDEO_AUDIT_966.jsonl')]
accepted = [r for r in rows if all(v == 'COMPLETE_LIMITED_EVIDENCE' for v in r['statuses'].values())]
queue = {q['video_id']: q for q in csv.DictReader(open(R / 'FINANCE_CONTINUATION_QUEUE.csv'))}
pk = {}
for f in sorted(glob.glob(str(R / 'audit-batches/*.json'))):
    n = pathlib.Path(f).name
    if n.endswith(('_VALIDATION.json', '_RECEIPTS.json')): continue
    try: d = json.load(open(f))
    except Exception: continue
    for rv in d.get('reviews', []) if isinstance(d, dict) else []:
        v = (rv.get('identity') or {}).get('video_id') or rv.get('Video_ID') or rv.get('video_id')
        if v: pk.setdefault(v, []).append(n)
con = sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
tc = {v: n for v, n in con.execute('select youtube_video_id, length(transcript_text) from transcripts')}
old = {r['video_id']: r for r in csv.DictReader(open(LEDGER))} if LEDGER.exists() else {}
base_sha = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
out = []
for r in sorted(accepted, key=lambda r: r['Video_ID']):
    v = r['Video_ID']; q = queue.get(v, {}); chars = tc.get(v) or 0
    st = old.get(v, {}).get('campaign_status') or ('PENDING' if chars else 'EVIDENCE_BLOCKED')
    out.append({'video_id': v, 'channel_id': r['Channel_ID'], 'channel_name': q.get('channel_name', ''), 'population': q.get('population', ''), 'original_batch': r['batch_id'],
                'packet_files': '|'.join(pk.get(v, [])), 'original_row_sha256': hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest(),
                'transcript_chars': chars, 'thumbnail_status': q.get('thumbnail_status', ''), 'k01_tier': q.get('performance_tier', ''), 'lifetime_rate_ratio': q.get('lifetime_rate_ratio', ''),
                'age_days': q.get('age_days', ''), 'campaign_status': st, 'block_reason': '' if chars else 'NO_TRANSCRIPT_IN_REGISTRY',
                'reanalysis_file': old.get(v, {}).get('reanalysis_file', '')})
with open(LEDGER, 'w', newline='') as f:
    w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
if not FROZEN.exists():
    ids = sorted(o['video_id'] for o in out)
    json.dump({'population_version': 'v1', 'frozen_utc': __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(), 'baseline_commit': base_sha, 'branch': 'research/finance-economics-intelligence',
               'population_sha256': hashlib.sha256('\n'.join(ids).encode()).hexdigest(), 'video_ids': ids,
               'definition': 'Accepted = VIDEO_AUDIT_966.jsonl row with all six statuses COMPLETE_LIMITED_EVIDENCE. Videos accepted later enter via the delta queue (build_population.py adds them as PENDING; baseline ids stay frozen).',
               'registered_universe': 1612, 'not_accepted_excluded': 1612 - len(ids)}, open(FROZEN, 'w'), indent=1)
fz = json.load(open(FROZEN)); delta = sorted(set(o['video_id'] for o in out) - set(fz['video_ids']))
import collections
print('accepted', len(out), 'unique', len({o['video_id'] for o in out}), 'delta', len(delta), 'hash', fz['population_sha256'][:12])
print(collections.Counter(o['campaign_status'] for o in out), collections.Counter(o['k01_tier'] for o in out), collections.Counter(bool(o['packet_files']) for o in out), collections.Counter(o['population'] for o in out))
