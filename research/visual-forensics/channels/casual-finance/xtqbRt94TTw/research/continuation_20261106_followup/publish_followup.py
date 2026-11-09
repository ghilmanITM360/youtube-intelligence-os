"""Owner-claimed Video006 publication only. Private index, mandatory final-tree gate,
normal push, bounded timeout, dependency bundle, fetched byte readback.
Run once after independent QA worker terminal; no retry loops or history changes.
"""
from pathlib import Path
import os,subprocess,json,hashlib,csv,datetime
from publication_preflight import check_tree,TEXT_SUFFIXES
P=Path(__file__).parent;REPO=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
PARENT='5e4979705f871c37f0ab3d2a52dce44c9c90e876';BRANCH='refs/heads/research/casually-finance-editing-forensics'
PREFIX='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/';REL='research/continuation_20261106_followup/'
def git(*args,input=None,env=None):return subprocess.check_output(['git','-C',str(REPO),*args],input=input,env=env)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,value):(P/name).write_text(json.dumps(value,indent=2)+'\n')
def snap():return {'canonical_head':git('rev-parse','HEAD').decode().strip(),'index_sha256':sha(REPO/'.git/index'),'status':git('status','--porcelain=v1').decode(),'stashes':git('stash','list','--format=%H %gd').decode(),'local_research_ref':git('rev-parse',BRANCH).decode().strip()}
entry=json.loads((P/'ENTRY_STATE.json').read_text());before=snap();assert all(before[k]==entry[k]for k in before),'Canonical state changed; stop without overwriting'
token=os.environ['VF_OWNER_TOKEN'];subprocess.run(['/Users/ghilmankhan/YIOS-local-audits/vf_lock.sh','heartbeat',token],check=True,capture_output=True)
terminal=json.loads((P/'WORKER_TERMINAL_RECEIPT.json').read_text());assert terminal['all_this_run_workers_terminal']is True
qa=json.loads((P/'independent_QA_followup.json').read_text());assert qa['status']=='PASS_BOUNDED_AFTER_SEPARATE_PRODUCTION_REPAIR'
assert json.loads((P/'CURRENT_REQUIREMENTS.json').read_text())['candidate_only_current']==610
assert json.loads((P/'PRODUCTION_VALIDATION_attempt02_reconciled.json').read_text())['status']=='PASS'
remote=git('ls-remote','origin',BRANCH).decode().split()[0];assert remote==PARENT,'Remote advanced; reconcile first'
# Hash media for external preservation; never add those bytes to index.
media=[x for x in P.rglob('*')if x.is_file()and x.suffix.lower()in{'.jpg','.jpeg','.png','.mp4','.mkv','.mp3','.wav'}]
with(P/'EXTERNAL_MEDIA_SHA256.csv').open('w',newline='')as f:
 w=csv.writer(f);w.writerow(['absolute_local_path','bytes','sha256'])
 for x in sorted(media):w.writerow([str(x),x.stat().st_size,sha(x)])
excluded={'publication_receipt.json','POST_PUBLICATION_HANDOFF.md','LOCK_RELEASE.json','prepared_checkpoint.json','CHECKPOINT_SEAL.json','bundle_verification.json','PREFLIGHT_BEFORE_COMMIT.json','PREFLIGHT_BEFORE_PUSH.json','exact_scoped_paths.txt','ENTRY_STATE_after.json'}
files=sorted(x for x in P.rglob('*')if x.is_file()and x.suffix.lower()in TEXT_SUFFIXES and x.name not in excluded)
sealed={str(x.relative_to(P)):sha(x)for x in files};save('CHECKPOINT_SEAL.json',{'channel':'Casual Finance','video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66','parent':PARENT,'workers_terminal':True,'files':sealed,'new_media_in_git':False,'inherited_media_defects':'MEDIA_DEFECT.json'})
files.append(P/'CHECKPOINT_SEAL.json')
index=P/'publication_private.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index));git('read-tree',PARENT,env=env);mapping={}
def put(path,source):
 data=source.read_bytes();blob=git('hash-object','-w','--stdin',input=data).decode().strip();git('update-index','--add','--cacheinfo','100644',blob,path,env=env);mapping[path]={'source':str(source),'sha256':hashlib.sha256(data).hexdigest(),'blob':blob}
for x in files:put(PREFIX+REL+str(x.relative_to(P)),x)
# Published current pointers; previous owner local files and historicalspecs preserved.
put(PREFIX+'research/CURRENT_REQUIREMENTS.json',P/'CURRENT_REQUIREMENTS.json')
put(PREFIX+'research/CURRENT_NATIVE_QUEUE.json',P/'CURRENT_NATIVE_QUEUE_v8.json')
put(PREFIX+'research/CONTINUATION_HANDOFF.md',P/'OWNER_HANDOFF.md')
put(PREFIX+'QUALITY_GATE.json',P/'QUALITY_GATE.json')
tree=git('write-tree',env=env).decode().strip();defects=json.loads((P/'MEDIA_DEFECT.json').read_text());gate=check_tree(PARENT,tree,defects);save('PREFLIGHT_BEFORE_COMMIT.json',gate);assert not gate['violations'],gate['violations']
paths=git('diff','--name-only',PARENT,tree).decode().splitlines();assert paths and all(x.startswith(PREFIX)for x in paths)
(P/'exact_scoped_diff.patch').write_bytes(git('diff','--no-ext-diff',PARENT,tree));(P/'exact_scoped_paths.txt').write_text('\n'.join(paths)+'\n')
assert all(sha(P/name)==h for name,h in sealed.items()),'Sealed content changed; stop'
assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
commit=git('commit-tree',tree,'-p',PARENT,input=b'Casual Finance Video006: close 17 timing rows, specify 3 spans, enforce media preflight\n\n610 candidate-only rows and148 extended spans remain; bounded original attempt02 independent QA. Source-derived historical JPG defects disclosed, no new media. Audio0; AV blocked; CT incomplete.\n').decode().strip()
save('prepared_checkpoint.json',{'parent':PARENT,'commit':commit,'tree':tree,'mapping':mapping,'diff_paths':paths})
header=('# v2 git bundle\n-'+PARENT+' Required published Video006 W4\n'+commit+' refs/recovery/Casual-Finance-Video006-followup\n\n').encode();pack=git('pack-objects','--stdout','--revs',input=(commit+'\n^'+PARENT+'\n').encode());bundle=P/'Casual-Finance-Video006-followup.bundle';bundle.write_bytes(header+pack)
bv=subprocess.run(['git','-C',str(REPO),'bundle','verify',str(bundle)],capture_output=True,text=True);save('bundle_verification.json',{'exit_code':bv.returncode,'stdout':bv.stdout,'stderr':bv.stderr,'sha256':sha(bundle)});assert bv.returncode==0
# Same content gate immediatelybefore normalpush; no historical defect silently removed.
gate=check_tree(PARENT,commit,defects);save('PREFLIGHT_BEFORE_PUSH.json',gate);assert not gate['violations']
assert all(sha(P/name)==h for name,h in sealed.items())
assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
try:
 result=subprocess.run(['git','-C',str(REPO),'push','origin',commit+':'+BRANCH],capture_output=True,text=True,timeout=90);code=result.returncode;stdout=result.stdout;stderr=result.stderr
except subprocess.TimeoutExpired:
 code=124;stdout='';stderr='Normal push timed out after90seconds; no automatic retry. Readremote first; localcommit+bundlepreserved.'
remote_after=git('ls-remote','origin',BRANCH).decode().split()[0]
receipt={'channel':'Casual Finance','video_id':'xtqbRt94TTw','parent':PARENT,'commit':commit,'tree':tree,'remote':remote_after,'push_exit_code':code,'stdout':stdout,'stderr':stderr,'operation':'normal git push origin '+commit+':'+BRANCH,'new_media_published':False,'inherited_media_violations_retained':4,'bundle_sha256':sha(bundle),'sealed_files':len(sealed),'mapping_files':len(mapping),'post_publication_receipts':'LOCAL_ONLY_UNTIL_EXPLICIT_FOLLOWUP_PUBLICATION'}
if remote_after==commit:
 git('fetch','--no-write-fetch-head','--no-tags','origin',BRANCH)
 for path,m in mapping.items():assert hashlib.sha256(git('show',commit+':'+path)).hexdigest()==m['sha256'],path
 receipt['fetched_byte_readbacks']='PASS';receipt['status']='PUBLISHED_PARTIAL'
else:receipt['status']='LOCAL_VALIDATED_AND_BUNDLED; PUBLICATION_UNCONFIRMED_OR_FAILED; NO_BACKGROUND_RETRIES'
assert snap()==before,'Canonical state changed; preserve andinspect'
receipt['canonical_checkout_index_stashes_preserved']=True;save('publication_receipt.json',receipt);print(json.dumps(receipt,indent=2))
