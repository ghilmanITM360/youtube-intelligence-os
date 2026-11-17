import json,os,subprocess,csv,hashlib,datetime
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');M=A+'/scratch/remote_mirror.git';R=os.path.expanduser('~/workprojects/youtube-intelligence-os')
env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_OPTIONAL_LOCKS='0')
g=lambda repo,*a:subprocess.run(['git','-C',repo,*a],capture_output=True,text=True,env=env,errors='replace').stdout.strip()
pin={l.split('\t')[1].strip():l.split('\t')[0] for l in open(A+'/raw/recon/ls_remote_final2.txt') if 'HEAD' not in l}
mir={l.split()[1]:l.split()[0] for l in g(M,'for-each-ref','--format=%(objectname) %(refname)','refs/heads','refs/pull').splitlines()}
T=list(csv.reader(open(A+'/out/TWELVE_FINANCE_NICK_FILES.csv')))[1:]
twelve=0
for x in T:
    d=subprocess.run(['git','-C',M,'cat-file','blob',x[6]],capture_output=True,env=env).stdout
    twelve+=hashlib.sha256(d).hexdigest()==x[0]
lfs=0
for d,_,fs in os.walk(M+'/lfs/objects'):
    for f in fs:
        h=hashlib.sha256()
        with open(os.path.join(d,f),'rb') as fh:
            for b in iter(lambda:fh.read(1<<20),b''):h.update(b)
        lfs+=h.hexdigest()==f
rows=list(csv.DictReader(open(A+'/out/PRIMITIVE_EDUCATION_SCHEDULER_RUNS.csv')))[:17]
cls={}
for r in rows:cls[r['class']]=cls.get(r['class'],0)+1
V={'generated_utc':datetime.datetime.utcnow().isoformat()+'Z',
'remote_final_pin':{'time':open(A+'/raw/recon/ls_remote_final2.time').read().strip(),'heads':sum(k.startswith('refs/heads/') for k in pin),'pulls':sum(k.startswith('refs/pull/') for k in pin),'mirror_equals_pin':pin==mir},
'mirror':{'alternates_file':os.path.exists(M+'/objects/info/alternates'),'partialclone':g(M,'config','--get','extensions.partialclone'),'promisor':g(M,'config','--get','remote.origin.promisor'),'full_fsck_status':open(A+'/raw/remote/mirror_fsck_full.status').read().strip(),'full_fsck_output_bytes':os.path.getsize(A+'/raw/remote/mirror_fsck_full.txt'),'conn_fsck_final_output_bytes':os.path.getsize(A+'/raw/remote/mirror_fsck_conn_final.txt')},
'lfs_payloads_rehashed_now_match':lfs,
'twelve_files_blob_sha256_match':twelve,
'tests_local':{n:open(f'{A}/raw/tests/full_with_git/{n}.pytest.log').read().strip().splitlines()[-1] for n in ('main','research_finance-economics-intelligence','codex_casually-finance-knowledge-navigation')},
'validator_proofs':json.load(open(A+'/raw/code/validator_proofs.json')),
'scheduler_first17':cls,
'canonical':{'head':g(R,'rev-parse','HEAD'),'untracked':g(R,'status','--porcelain').count('\n')+1,'stash':g(R,'stash','list','--format=%H'),'orphan_rev_sha256':hashlib.sha256(open(R+'/.git/objects/pack/pack-8d9357e755ad7b7ae3a2fa62a866d13502003c23.rev','rb').read()).hexdigest()},
'finance_worktree_head':g(os.path.expanduser('~/workprojects/yios-finance-machine-a'),'rev-parse','HEAD'),
'blocked':['5767_comparison: list not located','machine_b_current_state: not accessible','off_device_backup: no destination','allowlist_patch: not found here'],
'not_certified':['listening','semantic approval','production approval','worktree restore beyond 3 refs']}
json.dump(V,open(A+'/out/VALIDATION_RESULTS.json','w'),indent=1,default=str)
print(json.dumps({k:V[k] for k in('remote_final_pin','lfs_payloads_rehashed_now_match','twelve_files_blob_sha256_match','tests_local','scheduler_first17','canonical','finance_worktree_head')},indent=0)); print(V['mirror'])
