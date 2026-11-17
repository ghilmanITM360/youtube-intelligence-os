"""Casual Finance Video006 claimed checkpoint: text-only, private index, scoped media deletion,
mandatory final-tree preflight twice, one normal push and byte readback. No checkout/ref changes."""
from pathlib import Path
import os,subprocess,json,hashlib,csv
from publication_preflight import check_tree,TEXT_SUFFIXES
P=Path(__file__).parent;REPO=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');PARENT='f8665fee2465f015978fbd9cda6bfdc43409feb5';BRANCH='refs/heads/research/casually-finance-editing-forensics';PREFIX='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/';REL='research/continuation_20261106_native2/'
def git(*a,input=None,env=None):return subprocess.check_output(['git','-C',str(REPO),*a],input=input,env=env)
def sha(x):return hashlib.sha256(x.read_bytes()).hexdigest()
def save(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
def snap():return{'canonical_head':git('rev-parse','HEAD').decode().strip(),'index_sha256':sha(REPO/'.git/index'),'status':git('status','--porcelain=v1').decode(),'stashes':git('stash','list','--format=%H %gd').decode(),'local_research_ref':git('rev-parse',BRANCH).decode().strip()}
entry=json.loads((P/'ENTRY_STATE.json').read_text());before=snap();assert all(before[k]==entry[k]for k in before),'Canonical state changed; do not overwrite'
subprocess.run(['/Users/ghilmankhan/YIOS-local-audits/vf_lock.sh','heartbeat',os.environ['VF_OWNER_TOKEN']],check=True,capture_output=True)
assert json.loads((P/'WORKER_TERMINAL_RECEIPT.json').read_text())['all_this_run_workers_terminal']is True
req=json.loads((P/'CURRENT_REQUIREMENTS.json').read_text());assert req['candidate_only_current']==int(os.environ['EXPECTED_PENDING'])
assert json.loads((P/'FINAL_VALIDATION.json').read_text())['status']=='PASS'
assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
media=[x for x in P.rglob('*')if x.is_file()and x.suffix.lower()in {'.jpg','.jpeg','.png','.mp4','.wav','.mp3','.mkv'}]
with(P/'EXTERNAL_MEDIA_SHA256.csv').open('w',newline='')as f:
 w=csv.writer(f);w.writerow(['absolute_local_path','bytes','sha256'])
 for x in sorted(media):w.writerow([str(x),x.stat().st_size,sha(x)])
excluded={'ENTRY_STATE.json','CHECKPOINT_SEAL.json','publication_receipt.json','POST_PUBLICATION_HANDOFF.md','LOCK_RELEASE.json','prepared_checkpoint.json','bundle_verification.json','PREFLIGHT_BEFORE_COMMIT.json','PREFLIGHT_BEFORE_PUSH.json','exact_scoped_paths.txt'}
# Exclusions are ROOT-relative; validated prior checkpoint post-publication receipts are included.
files=sorted(x for x in P.rglob('*')if x.is_file()and x.suffix.lower()in TEXT_SUFFIXES and str(x.relative_to(P))not in excluded)
sealed={str(x.relative_to(P)):sha(x)for x in files};save('CHECKPOINT_SEAL.json',{'channel':'Casual Finance','video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66','parent':PARENT,'workers_terminal':True,'files':sealed,'new_media_in_git':False,'media_removal':'MEDIA_CORRECTION.json','receipt_scope':'prior f8665fee receipts included; current-commit receipts necessarily local-only until later authorized checkpoint'})
files.append(P/'CHECKPOINT_SEAL.json');index=P/'publication_private.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index));git('read-tree',PARENT,env=env);mapping={}
def put(path,source):
 d=source.read_bytes();blob=git('hash-object','-w','--stdin',input=d).decode().strip();git('update-index','--add','--cacheinfo','100644',blob,path,env=env);mapping[path]={'source':str(source),'sha256':hashlib.sha256(d).hexdigest(),'blob':blob}
for x in files:put(PREFIX+REL+str(x.relative_to(P)),x)
for dst,src in [('research/CURRENT_REQUIREMENTS.json','CURRENT_REQUIREMENTS.json'),('research/CURRENT_NATIVE_QUEUE.json',req['queue_file_name']),('research/CONTINUATION_HANDOFF.md','OWNER_HANDOFF.md'),('QUALITY_GATE.json','QUALITY_GATE.json')]:put(PREFIX+dst,P/src)
assert all(PREFIX+REL+'prior_publication_receipts/'+n in mapping for n in ['publication_receipt.json','LOCK_RELEASE.json','PREFLIGHT_BEFORE_COMMIT.json','PREFLIGHT_BEFORE_PUSH.json','bundle_verification.json','POST_PUBLICATION_HANDOFF.md'])
correction=json.loads((P/'MEDIA_CORRECTION.json').read_text())
for r in correction['files']:
 p=Path(r['external_exact_byte_copy']);assert p.exists()and sha(p)==r['sha256']and p.stat().st_size==r['bytes'];assert hashlib.sha256(git('show',PARENT+':'+r['path'])).hexdigest()==r['sha256']
# Private-index normal removal only; source originals and history are preserved.
git('update-index','--index-info',input=''.join('0 '+'0'*40+'\t'+r['path']+'\n'for r in correction['files']).encode(),env=env)
tree=git('write-tree',env=env).decode().strip()
# Final scoped tree must now be text-only: ZERO media exceptions, rather than inherited allowances.
gate=check_tree(PARENT,tree,{'unexpected_media':[]});gate['effective_media_exceptions']=0;gate['text_only_scoped_tree']=not gate['violations'];save('PREFLIGHT_BEFORE_COMMIT.json',gate);assert not gate['violations']
paths=git('diff','--name-only',PARENT,tree).decode().splitlines();assert all(x.startswith(PREFIX)for x in paths);deletes=git('diff','--diff-filter=D','--name-only',PARENT,tree).decode().splitlines();assert sorted(deletes)==sorted(r['path']for r in correction['files'])
(P/'exact_scoped_paths.txt').write_text('\n'.join(paths)+'\n');(P/'exact_scoped_diff.patch').write_bytes(git('diff','--no-ext-diff',PARENT,tree))
assert all(sha(P/n)==h for n,h in sealed.items());assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
message=f"Casual Finance Video006: close {req['newly_resolved_timing_rows']} timing rows, specify3spans, remove4current-tree JPG violations\n\n{req['candidate_only_current']} strict candidate rows and145 extended spans remain. Prior receipts included, current receipts excluded. New original128frame bounded cold-start; audio0/AVblocked/CTfalse. Historical media bytes remain.\n"
commit=git('commit-tree',tree,'-p',PARENT,input=message.encode()).decode().strip();save('prepared_checkpoint.json',{'parent':PARENT,'commit':commit,'tree':tree,'mapping':mapping,'diff_paths':paths,'deleted_media':deletes})
header=('# v2 git bundle\n-'+PARENT+' Required published Video006 parent\n'+commit+' refs/recovery/Casual-Finance-Video006-native2\n\n').encode();pack=git('pack-objects','--stdout','--revs',input=(commit+'\n^'+PARENT+'\n').encode());bundle=P/'Casual-Finance-Video006-native2.bundle';bundle.write_bytes(header+pack);v=subprocess.run(['git','-C',str(REPO),'bundle','verify',str(bundle)],capture_output=True,text=True);save('bundle_verification.json',{'exit_code':v.returncode,'stdout':v.stdout,'stderr':v.stderr,'sha256':sha(bundle)});assert v.returncode==0
gate=check_tree(PARENT,commit,{'unexpected_media':[]});gate['effective_media_exceptions']=0;gate['text_only_scoped_tree']=not gate['violations'];save('PREFLIGHT_BEFORE_PUSH.json',gate);assert not gate['violations'];assert all(sha(P/n)==h for n,h in sealed.items());assert snap()==before;assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT
try:r=subprocess.run(['git','-C',str(REPO),'push','origin',commit+':'+BRANCH],capture_output=True,text=True,timeout=90);code=r.returncode;stdout=r.stdout;stderr=r.stderr
except subprocess.TimeoutExpired:code=124;stdout='';stderr='Normal push timeout90s; no automatic retry. Commit+bundle preserved.'
remote=git('ls-remote','origin',BRANCH).decode().split()[0];receipt={'channel':'Casual Finance','video_id':'xtqbRt94TTw','parent':PARENT,'commit':commit,'tree':tree,'remote':remote,'push_exit_code':code,'stdout':stdout,'stderr':stderr,'operation':'normal git push origin '+commit+':'+BRANCH,'sealed_files':len(sealed),'mapping_files':len(mapping),'media_removed_from_current_tree':deletes,'external_exact_byte_preservation':'4PASS','historical_media_bytes_remain':True,'new_media_published':False,'effective_media_exceptions':0,'prior_receipts_included':True,'current_commit_postpublication_receipts':'LOCAL_ONLY until later authorized publication','bundle_sha256':sha(bundle)}
if remote==commit:
 git('fetch','--no-write-fetch-head','--no-tags','origin',BRANCH)
 for path,m in mapping.items():assert hashlib.sha256(git('show',commit+':'+path)).hexdigest()==m['sha256'],path
 for r in correction['files']:assert subprocess.run(['git','-C',str(REPO),'cat-file','-e',commit+':'+r['path']],capture_output=True).returncode!=0
 receipt['fetched_byte_readbacks']='PASS';receipt['deleted_media_readback']='4ABSENT';receipt['status']='PUBLISHED_PARTIAL'
else:receipt['status']='LOCAL_VALIDATED_BUNDLED; REMOTE_PUBLICATION_FAILED_OR_UNCONFIRMED; NO_BACKGROUND_RETRY'
assert snap()==before;assert all(sha(P/n)==h for n,h in sealed.items());receipt['canonical_checkout_index_stashes_preserved']=True;save('publication_receipt.json',receipt);print(json.dumps(receipt,indent=2))
