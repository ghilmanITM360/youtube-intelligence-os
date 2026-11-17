"""Seal stable completed outputs, private-index commit, normal push, fetched readback.

Run only after root has observed its independent worker terminal.
No branch checkout, shared-index update, force or protection bypass.
"""
from pathlib import Path
import os,json,csv,hashlib,subprocess,datetime
P=Path(__file__).parent
REPO=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
PARENT='9c2685f13c14450a5e30066c526e246f311bb3a7'
BRANCH='refs/heads/research/casually-finance-editing-forensics'
PREFIX='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/'
REL='research/continuation_20261105_EP0002/'
def git(*args,input=None,env=None):return subprocess.check_output(['git','-C',str(REPO),*args],input=input,env=env)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):(P/n).write_text(json.dumps(d,indent=2)+'\n')
def snapshot():return {'head':git('rev-parse','HEAD').decode().strip(),'index':sha(REPO/'.git/index'),'status':git('status','--porcelain=v1').decode(),'stashes':git('stash','list','--format=%H %gd').decode()}
assert json.loads((P/'worker_terminal_receipt.json').read_text())['this_run_reviewers_terminal'] is True
checks=['independent_QA_report.json','independent_QA_selection_supplement.json','independent_QA_article_additions.json','independent_QA_early_objects.json','independent_QA_middle_objects_and_cursor.json','independent_QA_later_objects.json']
for f in checks:assert (P/f).is_file() and json.loads((P/f).read_text())
rows=list(csv.DictReader((P/'visual_event_ledger_v25.csv').open()))
assert len(rows)==len({r['event_id'] for r in rows})==948
assert sum(r['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for r in rows)==633
part=list(csv.DictReader((P/'frame_partition_v7.csv').open()));assert sum(int(x['n_frames']) for x in part)==19862
assert all(int(a['end'])+1==int(b['start']) for a,b in zip(part,part[1:]))
idx=json.loads((P/'integrated_production_interval_index_v8.json').read_text());assert idx['missing_state_ids']==[] and len(idx['prior_draft_span_extended_intervals_remaining'])==151
media=[f for f in P.rglob('*') if f.is_file() and f.suffix.lower() in {'.png','.jpg','.mkv','.mp4'}]
with (P/'EXTERNAL_MEDIA_SHA256.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['local_path','bytes','sha256'])
 for x in sorted(media):w.writerow([str(x),x.stat().st_size,sha(x)])
before=snapshot();remote=git('ls-remote','origin',BRANCH).decode().split()[0]
assert remote==PARENT,'Remote advanced; preserve checkpoint and reconcile; no push'
git('fetch','--no-write-fetch-head','--no-tags','origin',BRANCH)
excluded={'owner-token.private','publication_private.index'}
textfiles=[f for f in P.rglob('*') if f.is_file() and f.name not in excluded and f.suffix.lower() in {'.json','.csv','.md','.py','.txt'}]
seal={str(f.relative_to(P)):sha(f) for f in sorted(textfiles)}
save('CHECKPOINT_SEAL.json',{'channel':'Casual Finance','video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66','parent':PARENT,'root':str(P),'reviewers_terminal':True,'files':seal,'media_in_git':False})
textfiles.append(P/'CHECKPOINT_SEAL.json')
index=P/'publication_private.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index));git('read-tree',PARENT,env=env);mapping={}
for f in sorted(textfiles):
 target=PREFIX+REL+str(f.relative_to(P));blob=git('hash-object','-w','--stdin',input=f.read_bytes()).decode().strip();git('update-index','--add','--cacheinfo','100644',blob,target,env=env);mapping[target]={'source':str(f),'sha256':sha(f),'blob':blob}
for f in ['QUALITY_GATE.json','EXTERNAL_EVIDENCE_MANIFEST.json']:
 target=PREFIX+f;blob=git('hash-object','-w','--stdin',input=(P/f).read_bytes()).decode().strip();git('update-index','--add','--cacheinfo','100644',blob,target,env=env);mapping[target]={'source':str(P/f),'sha256':sha(P/f),'blob':blob}
tree=git('write-tree',env=env).decode().strip();paths=git('diff','--name-only',PARENT,tree).decode().splitlines();assert paths and all(x.startswith(PREFIX)for x in paths)
(P/'exact_scoped_diff.patch').write_bytes(git('diff','--no-ext-diff',PARENT,tree));(P/'exact_scoped_paths.txt').write_text('\n'.join(paths)+'\n')
assert all(sha(P/f)==h for f,h in seal.items())
assert git('ls-remote','origin',BRANCH).decode().split()[0]==PARENT,'Remote changed before commit'
commit=git('commit-tree',tree,'-p',PARENT,input=b'Casual Finance Video006: resolve 79 timing rows and 28 missing spec mappings\n\n74 exact timing rows plus 5 continuous fragments; 633 candidate-only remain. Original bounded 28-frame attempt02 independent pass; failed attempt01 retained. Audio0/AV blocked/CT incomplete. Text-only evidence closure.\n').decode().strip()
save('prepared_checkpoint.json',{'parent':PARENT,'commit':commit,'tree':tree,'mapping':mapping,'paths':paths})
# Dependency-aware bundle; recovery ref lives inside bundle only, no new repository refs.
header=f'# v2 git bundle\n-{PARENT} Required published Video006 checkpoint V\n{commit} refs/recovery/Casual-Finance-Video006-continuation\n\n'.encode()
pack=git('pack-objects','--stdout','--revs',input=(commit+'\n^'+PARENT+'\n').encode());bundle=P/'Casual-Finance-Video006-continuation.bundle';bundle.write_bytes(header+pack)
verify=subprocess.run(['git','-C',str(REPO),'bundle','verify',str(bundle)],capture_output=True,text=True);save('bundle_verification.json',{'exit_code':verify.returncode,'stdout':verify.stdout,'stderr':verify.stderr,'sha256':sha(bundle)});assert verify.returncode==0
result=subprocess.run(['git','-C',str(REPO),'push','origin',commit+':'+BRANCH],capture_output=True,text=True)
remote_after=git('ls-remote','origin',BRANCH).decode().split()[0]
receipt={'channel':'Casual Finance','video_id':'xtqbRt94TTw','parent_sha':PARENT,'local_commit_sha':commit,'tree_sha':tree,'remote_sha':remote_after,'operation':'normal git push origin '+commit+':'+BRANCH,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'source_root':str(P),'dependency_bundle':str(bundle),'bundle_sha256':sha(bundle),'mapping_files':len(mapping),'media_uploaded':False}
if result.returncode==0:
 assert remote_after==commit
 git('fetch','--no-write-fetch-head','--no-tags','origin',BRANCH)
 for path,x in mapping.items():assert hashlib.sha256(git('show',remote_after+':'+path)).hexdigest()==x['sha256'],path
 receipt['all_fetched_blob_readbacks']='PASS'
else:receipt['publication_status']='LOCAL_VALIDATED_COMMIT_AND_BUNDLE_PRESERVED;BOUNDED_ERROR_INVESTIGATION_REQUIRED'
assert snapshot()==before,'Unrelated checkout/index/stash changed; preserve and inspect'
receipt['checkout_index_stashes_preserved']=True;save('publication-receipt.json',receipt)
print(json.dumps({k:v for k,v in receipt.items()if k not in ['stdout','stderr']},indent=2));print(result.stderr)
