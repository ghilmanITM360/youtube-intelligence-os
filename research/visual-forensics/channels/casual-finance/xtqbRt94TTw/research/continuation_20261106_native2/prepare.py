from pathlib import Path
import subprocess,json,hashlib,shutil,datetime
P=Path(__file__).parent;B=Path('/Users/ghilmankhan/YIOS-local-audits/Casual-Finance-Video006-followup-20261106T0330Z');R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
def git(*a):return subprocess.check_output(['git','-C',str(R),*a])
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
s={'canonical_head':git('rev-parse','HEAD').decode().strip(),'index_sha256':sha(R/'.git/index'),'status':git('status','--porcelain=v1').decode(),'stashes':git('stash','list','--format=%H %gd').decode(),'local_research_ref':git('rev-parse','refs/heads/research/casually-finance-editing-forensics').decode().strip(),'remote':git('ls-remote','origin','refs/heads/research/casually-finance-editing-forensics').decode().split()[0]};assert s['remote']=='f8665fee2465f015978fbd9cda6bfdc43409feb5';save('ENTRY_STATE.json',s)
for f in ['CURRENT_REQUIREMENTS.json','CURRENT_NATIVE_QUEUE_v8.json','visual_event_ledger_v32.csv','integrated_production_interval_index_v9.json','MEDIA_DEFECT.json']:
 prefix='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/research/continuation_20261106_followup/'
 assert git('show',s['remote']+':'+prefix+f)==(B/f).read_bytes(),f
source=Path(json.loads((B/'SOURCE_VERIFICATION.json').read_text())['path']);h=sha(source);assert h=='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66';save('SOURCE_VERIFICATION.json',{'channel':'Casual Finance','video_id':'xtqbRt94TTw','path':str(source),'bytes':source.stat().st_size,'sha256':h,'native_fps':24,'frame_pts':'(n+1)/24','baseline_remote':s['remote'],'readback_baseline_files':5})
print(s);print('SOURCE HASH PASS')
