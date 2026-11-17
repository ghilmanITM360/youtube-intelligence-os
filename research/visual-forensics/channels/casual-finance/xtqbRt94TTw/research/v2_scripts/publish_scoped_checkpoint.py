"""Text-only Git-plumbing publication with private index, parent check and readback."""
import pathlib,json,subprocess,os,hashlib,sys
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
repo=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
branch='research/casually-finance-editing-forensics'
prefix='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/'
label=sys.argv[1];spec=json.loads((R/f'publication_{label}.json').read_text())
def git(*args,env=None,input=None):
    return subprocess.check_output(['git','-C',str(repo),*args],env=env,input=input)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot():
    return {'head':git('rev-parse','HEAD').decode().strip(),'index_sha256':sha(repo/'.git/index'),'status':git('status','--porcelain=v1').decode()}
before=snapshot()
parent=git('ls-remote','origin','refs/heads/'+branch).decode().split()[0]
git('fetch','--no-write-fetch-head','origin','refs/heads/'+branch)
suffix='push' if '--push' in sys.argv else 'prepare'
index=R/f'session_20261103/publication_{label}_{suffix}.index'
assert not index.exists()
env=dict(os.environ,GIT_INDEX_FILE=str(index));git('read-tree',parent,env=env);mapping={}
for src,rel in spec['files'].items():
    p=R/src;assert p.is_file()
    assert p.suffix.lower() in ('.json','.csv','.md','.py','.sh','.txt','') or p.name.startswith('EVIDENCE_SHA256SUMS_'),src
    assert not any(x in src for x in ('owner_receipt_private','audio16k','publication_'))
    target=prefix+rel
    assert target.startswith(prefix) and '..' not in pathlib.PurePosixPath(target).parts
    blob=git('hash-object','-w','--stdin',input=p.read_bytes()).decode().strip()
    git('update-index','--add','--cacheinfo','100644',blob,target,env=env)
    mapping[target]={'source':src,'sha256':sha(p),'blob':blob}
tree=git('write-tree',env=env).decode().strip()
paths=git('diff','--name-only',parent,tree).decode().splitlines()
assert paths and all(x.startswith(prefix) for x in paths)
print(git('diff','--stat',parent,tree).decode(),flush=True)
diff=git('diff','--no-ext-diff',parent,tree).decode()
(R/f'session_20261103/scoped_diff_{label}_{suffix}.txt').write_text(diff)
prepared_path=R/f'session_20261103/prepared_{label}.json'
if '--push' not in sys.argv:
    prepared_path.write_text(json.dumps(dict(parent=parent,tree=tree,mapping=mapping,before=before),indent=2))
    print('PREPARED_ONLY',parent,tree);sys.exit(0)
prepared=json.loads(prepared_path.read_text())
assert prepared['parent']==parent and prepared['tree']==tree,'Parent/tree changed; reconcile and review again'
assert git('ls-remote','origin','refs/heads/'+branch).decode().split()[0]==parent,'Remote advanced'
commit=git('commit-tree',tree,'-p',parent,input=spec['message'].encode()).decode().strip()
git('push','origin',commit+':refs/heads/'+branch)
remote=git('ls-remote','origin','refs/heads/'+branch).decode().split()[0];assert remote==commit
git('fetch','--no-write-fetch-head','origin','refs/heads/'+branch)
for path,x in mapping.items():
    assert hashlib.sha256(git('show',remote+':'+path)).hexdigest()==x['sha256'],path
assert before==snapshot(),'Unrelated checkout/index changed'
receipt=dict(checkpoint=label,parent_sha=parent,commit_sha=commit,remote_sha=remote,tree_sha=tree,readback_files=len(mapping),all_readbacks='PASS',checkout_and_index_preserved=True,source_workspace=str(R),files=mapping)
(R/f'session_20261103/publication_receipt_{label}.json').write_text(json.dumps(receipt,indent=2))
print('PUBLISHED',commit,'READBACK',len(mapping),'CHECKOUT_PRESERVED')
