import sqlite3,json,os,subprocess,csv
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');X=A+'/scratch/tests/research_finance-economics-intelligence'
reg=sqlite3.connect(f'file:{X}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
inv=sqlite3.connect(f'file:{X}/data/catalog/youtube_inventory.db?mode=ro',uri=True)
o=json.load(open(A+'/raw/db/retrieval_demos.json'))
print({k:(v if k.startswith('Q4') or k.startswith('Q5') else '') for k,v in o.items() if k[:2] in('Q4','Q5')})
print('registry channel name search',reg.execute("select channel_name,canonical_channel_id,(select count(*) from videos v where v.canonical_channel_id=c.canonical_channel_id) from channels c where channel_name like '%rimitive%' or channel_name like '%arely%' or channel_name like '%asual%' or channel_name like '%Nick%' or channel_name like '%xkcd%'").fetchall())
print('visual_coverage cols',[r[1] for r in reg.execute('pragma table_info(visual_coverage)')][:10],reg.execute('select count(*) from visual_coverage').fetchone())
print('avail gaps',reg.execute('select count(*) from availability_gaps').fetchone())
print('inventory tables xt',[t for (t,) in inv.execute("select name from sqlite_master where type='table'")][:30])
for t,col in (('videos','youtube_video_id'),('videos','video_id')):
    try:print(t,col,inv.execute(f'select count(*) from {t} where {col}=?',('xtqbRt94TTw',)).fetchone())
    except Exception as e:print(e)
vid='pFs8QGikczo'
q2={'video':reg.execute('select youtube_video_id,canonical_channel_id,title,published_at,views from videos where youtube_video_id=?',(vid,)).fetchone(),
'channel':reg.execute('select channel_name,current_handle from channels where canonical_channel_id=(select canonical_channel_id from videos where youtube_video_id=?)',(vid,)).fetchone(),
'transcript':reg.execute('select transcript_id,word_count,language,caption_type,is_placeholder,evidence_locator,transcript_sha256 from transcripts where youtube_video_id=?',(vid,)).fetchone()}
M=A+'/scratch/remote_mirror.git';env=dict(os.environ,GIT_NO_LAZY_FETCH='1')
d=subprocess.run(['git','-C',M,'show','refs/heads/research/finance-economics-intelligence:research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl'],capture_output=True,text=True,env=env).stdout
row=[json.loads(l) for l in d.splitlines() if json.loads(l).get('Video_ID')==vid]
q2['audit_rows']=len(row)
if row:
    r=row[0];q2['audit_keys']=sorted(r.keys());q2['statuses']={k:r[k] for k in r if k.endswith('_REVIEW') or k=='statuses'};q2['batch']=r.get('batch_id')
    q2['script_source_refs']=(r.get('script') or {}).get('source_refs',[])[:4]
o['Q2b_finance_video_full_chain']=q2
o['Q2_gap']='xtqbRt94TTw absent from registry at Finance tip; Casual Finance registry row has 0 videos; Primitive Education and Barely Evolved channels absent. Visual-forensics streams are therefore retrievable by Git path, not by registry DB.'
json.dump(o,open(A+'/raw/db/retrieval_demos.json','w'),indent=1,default=str,ensure_ascii=False)
print(json.dumps(q2,default=str,ensure_ascii=False)[:1800])
