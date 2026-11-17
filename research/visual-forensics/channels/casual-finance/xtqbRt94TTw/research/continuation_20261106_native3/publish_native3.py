"""Casual Finance Video006 scoped text publication. Own v3 claim only; zero media exceptions."""
from pathlib import Path
import os,subprocess,json,hashlib,csv
from publication_preflight import check_tree,TEXT_SUFFIXES
P=Path(__file__).parent;REPO=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');PARENT='efeacb0f7adebf57d20f55733947ea5dbb57c26c';BRANCH='refs/heads/research/casually-finance-editing-forensics';PREFIX='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/';REL='research/continuation_20261106_native3/'
def git(*a,input=None,env=None):return subprocess.check_output(['git','-C',str(REPO),*a],input=input,env=env)
def sha(x):return hashlib.sha256(x.read_bytes()).hexdigest()
def save(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
def snap():return{'canonical_head':git('rev-parse','HEAD').decode().strip(),'index_sha256':sha(REPO/'.git/index'),'status':git('status','--porcelain=v1').decode(),'stashes':git('stash','list','--format=%H %gd').decode(),'local_research_ref':git('rev-parse',BRANCH).decode().strip()}
entry=json.loads((P/'ENTRY_STATE.json').read_text());before=snap();assert before==entry,'Canonicalstatechanged;do notoverwrite';subprocess.run(['/Users/ghilmankhan/YIOS-local-audits/vf_lock.sh','heartbeat',os.environ['VF_OWNER_TOKEN']],check=True,capture_output=True)
assert json.loads((P/'WORKER_TERMINAL_RECEIPT.json').read_text())['all_this_run_workers_terminal']is True
req=json.loads((P/'CURRENT_REQUIREMENTS.json').read_text());assert req['candidate_only_current']==562 and req['extended_spans_current']==143
assert json.loads((P/'FINAL_VALIDATION.json').read_text())['status']=='PASS';assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
media=[x for x in P.rglob('*')if x.is_file()and x.suffix.lower()in{'.jpg','.jpeg','.png','.mp4','.wav','.mp3','.mkv'}]
with(P/'EXTERNAL_MEDIA_SHA256.csv').open('w',newline='')as f:
 w=csv.writer(f);w.writerow(['absolute_local_path','bytes','sha256'])
 for x in sorted(media):w.writerow([str(x),x.stat().st_size,sha(x)])
excluded={'ENTRY_STATE.json','CHECKPOINT_SEAL.json','publication_receipt.json','POST_PUBLICATION_HANDOFF.md','LOCK_RELEASE.json','prepared_checkpoint.json','bundle_verification.json','PREFLIGHT_BEFORE_COMMIT.json','PREFLIGHT_BEFORE_PUSH.json','USAGE_END.json','exact_scoped_paths.txt','exact_scoped_diff.patch'}
files=sorted(x for x in P.rglob('*')if x.is_file()and x.suffix.lower()in TEXT_SUFFIXES and str(x.relative_to(P))not in excluded);sealed={str(x.relative_to(P)):sha(x)for x in files}
save('CHECKPOINT_SEAL.json',{'channel':'Casual Finance','video_id':'xtqbRt94TTw','parent':PARENT,'source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66','workers_terminal':True,'files':sealed,'new_media_in_git':False,'receipt_scope':'Prior8efeacb0f receipts included; currentcommit receipts excluded until later authorizedpublication; no selfhash'})
files.append(P/'CHECKPOINT_SEAL.json');index=P/'publication_private.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index));git('read-tree',PARENT,env=env);mapping={}
def put(path,source):
 data=source.read_bytes();blob=git('hash-object','-w','--stdin',input=data).decode().strip();git('update-index','--add','--cacheinfo','100644',blob,path,env=env);mapping[path]={'source':str(source),'sha256':hashlib.sha256(data).hexdigest(),'blob':blob}
for x in files:put(PREFIX+REL+str(x.relative_to(P)),x)
for dst,src in [('research/CURRENT_REQUIREMENTS.json','CURRENT_REQUIREMENTS.json'),('research/CURRENT_NATIVE_QUEUE.json',req['queue_file_name']),('research/CONTINUATION_HANDOFF.md','OWNER_HANDOFF.md'),('QUALITY_GATE.json','QUALITY_GATE.json')]:put(PREFIX+dst,P/src)
assert len([p for p in mapping if'/native3/'in p])==0 # actual path uses continuation_20261106_native3, not accidental alternate directory
assert all(PREFIX+REL+'prior_publication_receipts/'+n in mapping for n in ['publication_receipt.json','LOCK_RELEASE.json','PREFLIGHT_BEFORE_COMMIT.json','PREFLIGHT_BEFORE_PUSH.json','bundle_verification.json','POST_PUBLICATION_HANDOFF.md','prepared_checkpoint.json','USAGE_END.json'])
tree=git('write-tree',env=env).decode().strip();gate=check_tree(PARENT,tree,{'unexpected_media':[]});gate.update(effective_media_exceptions=0,text_only_scoped_tree=not gate['violations']);save('PREFLIGHT_BEFORE_COMMIT.json',gate);assert not gate['violations']
paths=git('diff','--name-only',PARENT,tree).decode().splitlines();assert all(x.startswith(PREFIX)for x in paths);assert not git('diff','--diff-filter=D','--name-only',PARENT,tree).decode().strip(),'No new deletions authorized or needed'
(P/'exact_scoped_paths.txt').write_text('\n'.join(paths)+'\n');(P/'exact_scoped_diff.patch').write_bytes(git('diff','--no-ext-diff',PARENT,tree));assert all(sha(P/n)==h for n,h in sealed.items());assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
message='Casual Finance Video006: close10timingrows, specifyG005/G006, publish priorreceipts\n\n572to562 strictcandidate rows;145to143extendedspans. Two additionalcomponentsoutsidecategory.48framebounded originalQA/coldstart; wholevideoNOT_RUN/audio0AVblockedCTfalse. Zero-mediaexceptions; historicalmedia bytesremain.\n'
commit=git('commit-tree',tree,'-p',PARENT,input=message.encode()).decode().strip();save('prepared_checkpoint.json',{'parent':PARENT,'commit':commit,'tree':tree,'mapping':mapping,'diff_paths':paths})
header=('# v2 git bundle\n-'+PARENT+' Required published Video006 parent\n'+commit+' refs/recovery/Casual-Finance-Video006-native3\n\n').encode();pack=git('pack-objects','--stdout','--revs',input=(commit+'\n^'+PARENT+'\n').encode());bundle=P/'Casual-Finance-Video006-native3.bundle';bundle.write_bytes(header+pack);v=subprocess.run(['git','-C',str(REPO),'bundle','verify',str(bundle)],capture_output=True,text=True);save('bundle_verification.json',{'exit_code':v.returncode,'stdout':v.stdout,'stderr':v.stderr,'sha256':sha(bundle),'requires_parent':PARENT});assert v.returncode==0
gate=check_tree(PARENT,commit,{'unexpected_media':[]});gate.update(effective_media_exceptions=0,text_only_scoped_tree=not gate['violations']);save('PREFLIGHT_BEFORE_PUSH.json',gate);assert not gate['violations'];assert all(sha(P/n)==h for n,h in sealed.items());assert snap()==before;assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
try:r=subprocess.run(['git','-C',str(REPO),'push','origin',commit+':'+BRANCH],capture_output=True,text=True,timeout=90);code=r.returncode;stdout=r.stdout;stderr=r.stderr
except subprocess.TimeoutExpired:code=124;stdout='';stderr='Normalpushtimeout90s; no automatic retry. Validatedcommit/bundlepreserved.'
remote=git('ls-remote','origin',BRANCH).decode().split()[0];receipt={'channel':'Casual Finance','video_id':'xtqbRt94TTw','parent':PARENT,'commit':commit,'tree':tree,'remote':remote,'push_exit_code':code,'stdout':stdout,'stderr':stderr,'operation':'normalgitpushorigin '+commit+':'+BRANCH,'sealed_files':len(sealed),'mapping_files':len(mapping),'new_media_published':False,'effective_media_exceptions':0,'historical_media_bytes_remain':True,'prior_receipts_included':8,'current_postpublication_receipts':'LOCAL_ONLY until later authorizedpublication','bundle_sha256':sha(bundle)}
if remote==commit:
 git('fetch','--no-write-fetch-head','--no-tags','origin',BRANCH)
 for path,m in mapping.items():assert hashlib.sha256(git('show',commit+':'+path)).hexdigest()==m['sha256'],path
 defects=json.loads((P/'MEDIA_DEFECT.json').read_text())['unexpected_media']
 for row in defects:assert subprocess.run(['git','-C',str(REPO),'cat-file','-e',commit+':'+row['path']],capture_output=True).returncode!=0
 receipt.update(fetched_byte_readbacks='PASS',prior_removed_media_readback='4ABSENT',status='PUBLISHED_PARTIAL')
else:receipt['status']='LOCAL_VALIDATED_BUNDLED;PUBLICATION_FAILED_OR_UNCONFIRMED;NO_BACKGROUND_RETRY'
assert snap()==before;assert all(sha(P/n)==h for n,h in sealed.items());receipt['canonical_checkout_index_stashes_preserved']=True;save('publication_receipt.json',receipt);print(json.dumps({k:v for k,v in receipt.items()if k not in['stdout','stderr']},indent=2))
