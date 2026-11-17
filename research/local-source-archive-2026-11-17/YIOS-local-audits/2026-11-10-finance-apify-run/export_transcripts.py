# usage: python3 -I export_transcripts.py  -> transcripts/export/{TRANSCRIPT_INDEX.csv,TRANSCRIPTS_ALL.jsonl}
# One record per video_id. Caption (COMPLETE) preferred; local Whisper only where no validated caption exists.
import csv, json, os, re, hashlib
B = os.path.dirname(os.path.abspath(__file__)); os.chdir(B)
TS = re.compile(r'^\[(\d+\.\d{3}) --> (\d+\.\d{3})\] (.+)$')
def segs(p):
    L = open(p).read().splitlines(); out = [TS.match(x) for x in L[1:]]
    assert L and L[0].startswith('# video_id=') and out and all(out), p
    return [dict(start=float(m[1]), end=float(m[2]), text=m[3]) for m in out]
cov = list(csv.DictReader(open('TRANSCRIPT_COVERAGE.csv')))
wh = {r['video_id']: r for r in csv.DictReader(open('transcripts/WHISPER_SUPPLEMENT.csv'))}
os.makedirs('transcripts/export', exist_ok=True)
idx, n = [], 0
with open('transcripts/export/TRANSCRIPTS_ALL.jsonl', 'w') as J:
    for r in cov:
        vid = r['video_id']
        if r['status'] == 'COMPLETE': src, track, p = r['source'], r['track'], r['transcript_path']
        elif vid in wh: src, track, p = wh[vid]['source'], 'whisper_' + wh[vid]['model'], wh[vid]['transcript_path']
        else:
            idx.append(dict(video_id=vid, channel_id=r['channel_id'], channel_slug=r['channel_slug'], title=r['title'], status=r['status'], source='', reason=r['reason'])); continue
        s = segs(p); n += 1
        J.write(json.dumps(dict(video_id=vid, channel_id=r['channel_id'], channel_slug=r['channel_slug'], title=r['title'], source=src, track=track,
                                machine_transcribed=src.startswith('local_whisper'), transcript_path=p, segments=s), ensure_ascii=False) + '\n')
        idx.append(dict(video_id=vid, channel_id=r['channel_id'], channel_slug=r['channel_slug'], title=r['title'], status='DELIVERED', source=src, track=track,
                        segments=len(s), words=sum(len(x['text'].split()) for x in s), last_end_s=s[-1]['end'], duration_s=r['duration_s'], transcript_path=p, reason=r['reason'] if r['status'] != 'COMPLETE' and vid in wh else ''))
F = ['video_id', 'channel_id', 'channel_slug', 'title', 'status', 'source', 'track', 'segments', 'words', 'last_end_s', 'duration_s', 'transcript_path', 'reason']
with open('transcripts/export/TRANSCRIPT_INDEX.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, F); w.writeheader(); w.writerows(idx)
assert len({x['video_id'] for x in idx}) == len(idx) == len(cov)
print('delivered', n, 'of', len(cov))
