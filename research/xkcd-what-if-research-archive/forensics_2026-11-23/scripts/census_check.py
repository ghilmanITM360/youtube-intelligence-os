import csv,os,json,statistics as st,collections
R='/Users/ghilmanislam360/Documents/youtube-intelligence-os/'
rows=list(csv.DictReader(open(R+'research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/census/census.csv')))
print('rows',len(rows))
fc=collections.Counter(r['format_class'] for r in rows);print(fc)
for k in fc:
    v=[int(r['views_player']) for r in rows if r['format_class']==k and r['views_player'].isdigit()]
    d=[int(r['duration_s']) for r in rows if r['format_class']==k]
    print(k,'n',len(v),'sum',sum(v),'median views',st.median(v),'median dur',st.median(d),'min/max dur',min(d),max(d))
# local file availability
paths=collections.Counter();have=0;tot=0;vids_with_local=set();vids_exist=set()
for r in rows:
    lp=[p.strip() for p in r['local_paths'].split(' | ') if p.strip()]
    for p in lp:
        tot+=1
        ex=os.path.exists(p)
        paths[('exists' if ex else 'missing', p.split('/')[2] if p.startswith('/Users') else '?')]+=1
        if ex: vids_exist.add(r['video_id'])
    if lp: vids_with_local.add(r['video_id'])
print('local path entries',tot,paths)
print('videos with recorded local path',len(vids_with_local),'with existing file on THIS machine',len(vids_exist))
print('catalog_registered',collections.Counter(r['catalog_registered'] for r in rows))
print('transcript rows',collections.Counter(r['catalog_transcript_rows'] for r in rows))
no=[ (r['video_id'],r['format_class'],r['title'][:50],r['catalog_transcript_rows']) for r in rows if r['catalog_transcript_rows'] in ('0','')]
print('no transcript',len(no));[print(' ',x) for x in no]
print('latest',max(r['publish_datetime'] for r in rows))
