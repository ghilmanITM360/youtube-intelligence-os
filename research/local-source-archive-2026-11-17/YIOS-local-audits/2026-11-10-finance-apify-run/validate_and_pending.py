# usage: python3 -I validate_and_pending.py  -> validates every COMPLETE caption row, rewrites transcripts/PENDING_IDS.txt from export index
import csv, hashlib, re, collections, sys
pat = re.compile(r'^\[\d{5}\.\d{3} --> \d{5}\.\d{3}\] .+$')
bad = []
for r in csv.DictReader(open('TRANSCRIPT_COVERAGE.csv')):
    if r['status'] != 'COMPLETE': continue
    L = open(r['transcript_path']).read().splitlines()
    ok = (L[0].startswith(f"# video_id={r['video_id']} ") and len(L) - 1 == int(r['segments']) and all(pat.match(x) for x in L[1:])
          and hashlib.sha256(open(r['raw_path'], 'rb').read()).hexdigest() == r['raw_sha256'])
    if not ok: bad.append(r['video_id'])
idx = list(csv.DictReader(open('transcripts/export/TRANSCRIPT_INDEX.csv')))
p = [r['video_id'] for r in idx if r['status'] in ('QUEUED', 'RETRYABLE')]
open('transcripts/PENDING_IDS.txt', 'w').write('\n'.join(p) + '\n')
print('validation_failures', bad, '| index', dict(collections.Counter(r['status'] for r in idx)), '| pending', len(p))
sys.exit(1 if bad else 0)
