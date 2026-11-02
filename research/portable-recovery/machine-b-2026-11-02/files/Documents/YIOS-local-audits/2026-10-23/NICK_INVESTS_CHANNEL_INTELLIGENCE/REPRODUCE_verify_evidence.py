import json,csv,sqlite3,hashlib,zipfile,statistics,datetime,collections
from pathlib import Path
O=Path('/private/tmp/yios-nick-channel-20261023');R=Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os');P=R/'research/finance-economics-intelligence';n=json.loads((O/'data.json').read_text());by={r['Video_ID']:r for r in n};tc={r['Video_ID']:r for r in csv.DictReader(open(P/'TRANSCRIPT_COVERAGE.csv'))};db=R/'data/catalog/youtube_channel_registry.db';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before=sha(db);c=sqlite3.connect(f'file:{db}?mode=ro',uri=True);errors=[];samples=[]
for r in n:
 vid=r['Video_ID'];ts=c.execute('select transcript_text from transcripts where youtube_video_id=? and dataset_id=?',(vid,'DS-000022')).fetchall();assert len(ts)==1;txt=ts[0][0];digest=hashlib.sha256(txt.encode()).hexdigest()
 if digest!=tc[vid]['Text_SHA256']:errors.append([vid,'db text hash'])
 loc=tc[vid]['Evidence_locator'];zp,member=loc.split('::');raw=zipfile.ZipFile(R/zp).read(member);full=raw.decode('utf-8');part=full.split('TRANSCRIPT\n'+'='*78+'\n',1)[-1]
 if part.strip()!=txt.strip(): errors.append([vid,'archive/db text mismatch'])
 if vid in json.loads((O/'sample.json').read_text()):samples.append({'video_id':vid,'canonical_text_sha256':digest,'archive_member_sha256':hashlib.sha256(raw).hexdigest(),'archive_locator':loc,'canonical_chars':len(txt),'canonical_words_whitespace':len(txt.split()),'full_archive_text_read':True,'reading_scope':'ENTIRE_ARCHIVE_MEMBER_INCLUDING_FULL_TRANSCRIPT','audit_batch':r['batch_id']})
images=[]
for r in n:
 th=r['thumbnail'];p=th.get('image_path');
 if p:
  ok=(R/p).exists() and sha(R/p)==th.get('image_sha256');images.append({'video_id':r['Video_ID'],'path':str(R/p),'sha256':sha(R/p) if (R/p).exists() else None,'registered_hash_match':ok,'inspected_this_run':r['Video_ID'] in json.loads((O/'image_sample.json').read_text()),'registered_source_url':th.get('image_source')})
  if not ok:errors.append([r['Video_ID'],'image hash'])
c.close();assert sha(db)==before
# Reproduce frozen ratios and conduct k=5, snapshot +/-1day sensitivity using parsed date membership.
def age(r,delta=0):
 try:return float(r['identity']['Age_days'])+delta
 except:return None
def ratio(r,k=10,delta=0):
 aa=age(r,delta)
 if aa is None or aa<7:return None,[]
 peers=[x for x in n if x['Video_ID']!=r['Video_ID'] and age(x,delta) is not None and age(x,delta)>=7 and .5<=age(x,delta)/aa<=2];peers=sorted(peers,key=lambda x:(abs(age(x,delta)-aa),x['Video_ID']))[:k]
 if len(peers)<5:return None,[x['Video_ID'] for x in peers]
 base=statistics.median(float(x['identity']['Views'])/age(x,delta) for x in peers);return round(float(r['identity']['Views'])/aa/base,5),[x['Video_ID'] for x in peers]
def tier(v):return 'INSUFFICIENT_DATA' if v is None else 'STRONG' if v>=2 else 'WEAK' if v<.5 else 'TYPICAL'
sens=[]
for r in n:
 frozen=r['identity'];vals={};vals['video_id']=r['Video_ID'];vals['frozen_tier']=frozen['Performance_tier'];rr,peers=ratio(r)
 if rr is not None and abs(rr-float(frozen['Lifetime_rate_ratio']))>.00002:errors.append([r['Video_ID'],'ratio mismatch',rr,frozen['Lifetime_rate_ratio']])
 for label,k,delta in [('five_peers',5,0),('snapshot_minus1',10,-1),('snapshot_plus1',10,1)]:
  v,ps=ratio(r,k,delta);vals[label+'_ratio']=v;vals[label+'_tier']=tier(v);vals[label+'_peers']='|'.join(ps)
 sens.append(vals)
with open(O/'package/PEER_COHORT_SENSITIVITY.csv','w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(sens[0]));w.writeheader();w.writerows(sens)
result={'transcript_hashes_verified':len(n),'db_unchanged':True,'archive_db_text_errors':errors,'local_image_hashes_verified':len(images),'scripts_fully_read_this_run':samples,'images':images,'sensitivity_changes':{label:sum(r['frozen_tier']!=r[label+'_tier'] for r in sens) for label in ['five_peers','snapshot_minus1','snapshot_plus1']},'db_sha256':before}
(O/'evidence_validation.json').write_text(json.dumps(result,indent=2));print({k:v for k,v in result.items() if k not in ['scripts_fully_read_this_run','images']});print(samples)
