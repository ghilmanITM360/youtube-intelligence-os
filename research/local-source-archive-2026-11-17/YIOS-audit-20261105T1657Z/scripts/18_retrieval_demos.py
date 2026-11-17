import sqlite3,json,csv,sys,subprocess,os,re
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');X=A+'/scratch/tests/research_finance-economics-intelligence';M=A+'/scratch/remote_mirror.git'
env=dict(os.environ,GIT_NO_LAZY_FETCH='1')
reg=sqlite3.connect(f'file:{X}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True);kb=sqlite3.connect(f'file:{X}/data/knowledge/reference_knowledge.db?mode=ro',uri=True)
g=lambda *a:subprocess.run(['git','-C',M,*a],capture_output=True,text=True,env=env,errors='replace').stdout
out={}
print([r[1] for r in reg.execute('pragma table_info(channels)')][:14]);print([r[0] for r in reg.execute("select name from sqlite_master where type='table' and name not like '%fts%'")])
print([r[1] for r in reg.execute('pragma table_info(transcripts)')][:14])
nm=[c for c in [r[1] for r in reg.execute('pragma table_info(channels)')] if 'name' in c or 'title' in c][0]
idc=[c for c in [r[1] for r in reg.execute('pragma table_info(channels)')] if 'canonical' in c or c.endswith('channel_id')][0]
rows=reg.execute(f"select c.{idc},c.{nm},count(v.youtube_video_id) from channels c left join videos v on v.canonical_channel_id=c.{idc} where lower(c.{nm}) like '%casual%' or lower(c.{nm}) like '%primitive%' or lower(c.{nm}) like '%barely%' or lower(c.{nm}) like '%what if%' or lower(c.{nm}) like '%xkcd%' group by 1").fetchall()
out['Q1_channel_and_videos']=rows
vid='xtqbRt94TTw'
v=reg.execute('select youtube_video_id,canonical_channel_id,title,published_at,duration_seconds,video_type,views from videos where youtube_video_id=?',(vid,)).fetchone()
t=reg.execute('select length(transcript_text),substr(transcript_text,1,80) from transcripts where youtube_video_id=?',(vid,)).fetchone()
out['Q2_video']={'video':v,'transcript_chars_head':t,'remote_paths':g('ls-tree','--name-only','refs/audit-now/cf-forensics',f'research/visual-forensics/channels/casual-finance/{vid}/').split(),'source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66'}
fi=g('ls-tree','-r','--name-only','refs/heads/research/finance-economics-intelligence','research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl')
kb_cols=[r[1] for r in kb.execute('pragma table_info(ref_rule)')];va=[r[1] for r in kb.execute('pragma table_info(ref_video_assessment)')];print(kb_cols,va)
rule='FR-TITLE-02'
out['Q3_rule']=kb.execute('select * from ref_rule where rule_id=?',(rule,)).fetchone()
out['Q3_exact_witnesses']=kb.execute(f'select * from ref_video_assessment where rule_id=? limit 3',(rule,)).fetchall()
out['Q3_counts']=kb.execute('select count(*),count(distinct video_id) from ref_video_assessment where rule_id=?',(rule,)).fetchone()
out['Q3_fts']=kb.execute("select rowid,substr(snippet(ref_section_fts,-1,'[',']','…',12),1,160) from ref_section_fts where ref_section_fts match 'hook' limit 2").fetchall()
vp=f'research/visual-forensics/channels/casual-finance/{vid}/research/production_v1/'
pr=g('ls-tree','--name-only','refs/audit-now/cf-forensics',vp).split()
csvp=[p for p in pr if 'per_state_production_spec' in p][-1]
lines=g('show','refs/audit-now/cf-forensics:'+csvp).splitlines()
out['Q4_production_spec']={'file':csvp,'rows':len(lines)-1,'header':lines[0][:220],'first':lines[1][:220]}
tests=g('grep','-l','-i','production_spec\\|production spec','refs/heads/research/finance-economics-intelligence','--','tests').split()
out['Q4_tests']=tests[:5]
ql=g('ls-tree','-r','--name-only','refs/audit-now/cf-forensics',f'research/visual-forensics/channels/casual-finance/{vid}/research/continuation_20261105_EP0002/').split()
qp=sorted([p for p in ql if re.search(r'CURRENT_NATIVE_QUEUE',p)])
out['Q5_next_task_video006']={'queues':qp[-3:],'owner_handoff_next':'SUB010 -> EP0018 -> SUB011 -> EP0019 ...  (OWNER_HANDOFF.md, local; queue v5 at 5e497970)'}
led=g('show','refs/heads/research/finance-economics-intelligence:research/finance-economics-intelligence/reanalysis/REANALYSIS_CAMPAIGN_LEDGER.csv')
r=list(csv.DictReader(led.splitlines()));keys=list(r[0].keys());print(keys)
sc=[k for k in keys if 'status' in k.lower() or 'state' in k.lower()];print(sc)
import collections
out['Q5_finance_ledger_counts']={k:dict(collections.Counter(x[k] for x in r)) for k in sc}
out['Q5_next_finance']=[x['video_id'] for x in r if 'PENDING' in ' '.join(x[k] for k in sc)][:3]
json.dump(out,open(A+'/raw/db/retrieval_demos.json','w'),indent=1,default=str,ensure_ascii=False)
print(json.dumps(out,indent=0,default=str,ensure_ascii=False)[:5500])
