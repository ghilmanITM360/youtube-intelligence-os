import csv, json, subprocess, io, glob, collections, sys
REPO='/Users/ghilmankhan/workprojects/youtube-intelligence-os'
S='/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/622c153f-af35-4a64-8794-cbc9a7c5edf5/scratchpad'
def show(ref,p): return subprocess.run(['git','-C',REPO,'show',f'{ref}:{p}'],capture_output=True,text=True,check=True).stdout
P39='research/youtube-12-channel-metadata/channels/'
PK={'UC14Fb2zWTEZklONPXFbLrTQ':('PR #39','967ea707',P39+'primateeconomics'),
    'UCKhpM-cu2Cod-GyG6KngNYg':('PR #39','967ea707',P39+'logicalmoney72'),
    'UCcj_KU4ZN6bx6Ki68hNJWqw':('PR #39','967ea707',P39+'markbuildsus'),
    'UCLh3aiudWdnfR0QDC8aLEhQ':('PR #39','967ea707',P39+'unclefrankretirement16'),
    'UCWugleQL2wqr5N1X4o8yyLw':('PR #39','967ea707',P39+'unclejohnfinancial'),
    'UCiBGqUxeTe4AYQyRseSZaKw':('PR #38','f176aa28','research/monkey-explains-1999')}
live={}
for f in glob.glob(S+'/stageA/pages*.jsonl'):
    for l in open(f):
        d=json.loads(l)
        if d.get('channel_id'): live[d['channel_id']]=d
KEY=['title','description','publication_timestamp_utc','duration_seconds','view_count','like_count','comment_count','watch_url','thumbnail_url']
out=[]
for cid,(pr,ref,p) in PK.items():
    ev=json.loads(show(ref,p+'/CHANNEL_IDENTITY.json'))['evidence']
    rows=list(csv.DictReader(io.StringIO(show(ref,p+'/VIDEO_MASTER.csv'))))
    gaps=list(csv.DictReader(io.StringIO(show(ref,p+'/VIDEO_METADATA_GAPS.csv'))))
    acc=list(csv.DictReader(io.StringIO(show(ref,p+'/ACCESS_RESTRICTIONS.csv')))) if pr=='PR #39' else None
    assert ev['channel_id']==cid and all(r['channel_id']==cid for r in rows), cid
    types=collections.Counter(r['video_type'] for r in rows)
    avail=collections.Counter(r['availability_status'] for r in rows)
    blank={k:sum(1 for r in rows if r.get(k,'') in ('','UNKNOWN','null','None')) for k in KEY}
    caps=collections.Counter(r['captions_or_transcript_available'] for r in rows)
    ids={r['video_id'] for r in rows}
    latest=max(r['publication_timestamp_utc'] for r in rows if r['publication_timestamp_utc'])
    L=live[cid]
    samp=[s.get('video_id') for s in (L['videos_sample']+L['shorts_sample'])]
    new=[v for v in samp if v and v not in ids]
    out.append(dict(canonical_channel_id=cid,channel=ev['canonical_channel_name'],package=f"{pr} {p} @{ref}",
      id_match='PASS',snapshot_utc=ev['snapshot_timestamp_utc'],run_id=ev['source_run_id'],dataset_id=ev['source_dataset_id'],
      pkg_reported_videos=ev['reported_public_video_count'],pkg_rows=len(rows),
      by_type=';'.join(f'{k}={v}' for k,v in sorted(types.items())),by_availability=';'.join(f'{k}={v}' for k,v in sorted(avail.items())),
      latest_upload_in_pkg=latest,live_reported_videos_2026_11_09=next((h for h in L['header_meta'] if 'video' in h),'UNKNOWN'),
      live_sample_ids_not_in_pkg=len(new),live_sample_size=len([v for v in samp if v]),
      blank_counts=';'.join(f'{k}={v}' for k,v in blank.items() if v),gap_rows=len(gaps),
      caption_field=';'.join(f'{k}={v}' for k,v in caps.items()),
      gap_fields=';'.join(sorted({g['field'] for g in gaps}))[:200]))
w=csv.DictWriter(open(S+'/finecon/REUSE_VERIFICATION.csv','w',newline=''),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
for o in out: print(json.dumps(o))
