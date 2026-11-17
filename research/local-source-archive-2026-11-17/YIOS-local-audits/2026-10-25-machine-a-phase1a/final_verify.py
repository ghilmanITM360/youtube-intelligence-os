from pathlib import Path
import json,hashlib,subprocess,os,datetime,csv,collections
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','GIT_NO_LAZY_FETCH':'1','GIT_TERMINAL_PROMPT':'0'};initial=json.loads((O/'live-snapshot.json').read_text())['receipts'];commands={k:initial[k]['command'] for k in ['head','branch','upstream','status','stash','worktrees','remotes','local-refs','live-refs','pr36','disk']};final={}
for n,c in commands.items():
 p=subprocess.run(c,cwd=R,capture_output=True,text=True,env=env);final[n]={'command':c,'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'same_stdout_as_initial':p.stdout==initial[n]['stdout']}
baseline=json.loads((O/'source-metadata-baseline.json').read_text());changes=[]
for name,old in baseline.items():
 p=Path(name)
 try:
  s=p.stat();new=[s.st_size,s.st_mtime_ns,s.st_ino]
  if new!=old:changes.append({'path':name,'before':old,'after':new})
 except OSError as e:changes.append({'path':name,'error':str(e)})
source_changes=[r for r in changes if '/.git/' not in r['path']];old=O.parent/'2026-10-25-machine-a-phase0';seal=[]
for line in (old/'SHA256SUMS').read_text().splitlines():
 expected,name=line.split('  ',1);actual=hashlib.sha256((old/name).read_bytes()).hexdigest();seal.append({'path':name,'status':'PASS' if expected==actual else 'FAIL'})
cap=json.loads((O/'capcut-current-dependencies.json').read_text());capchanges=[p for p,r in cap['json_hashes'].items() if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=r['sha256']]
checks={}
for n,expected in [('fresh-github-retrievals.json',5),('what-if-release-manifest-verification.json',100),('video003-checkpoint4-checks.json',1770),('skill-current-verification.json',80)]:
 d=json.loads((O/n).read_text());checks[n]={'rows':len(d),'expected_rows':expected,'statuses':dict(collections.Counter(x['status'] for x in d))};assert len(d)==expected and all(x['status']=='PASS' for x in d)
cf=json.loads((O/'cf-38-reproduction-prerequisites.json').read_text())['sets'];assert len(cf)==38 and all(x['source_check']=='PASS' and x['shape_matches_summary'] and x['header_data_bytes_consistent'] for x in cf)
assert all(x['npy_header']['descr']=='|u1' and x['npy_header']['fortran_order']==False for x in cf)
with (O/'what-if-proposed-integration.csv').open() as f:rows=list(csv.DictReader(f));assert len(rows)==457
stage=json.loads((O/'stage-index-verification.json').read_text());assert stage['index_staging_manifest_sha256_matches'] and stage['index_table_counts_match'] and all(x['status']=='PASS' for x in stage['checks'])
for key in ['head','branch','upstream','status','stash','worktrees','remotes','live-refs']:assert final[key]['same_stdout_as_initial'],key
assert not source_changes and not capchanges and all(x['status']=='PASS' for x in seal)
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'final_git_receipts':final,'restatted_paths':len(baseline),'all_metadata_changes':changes,'source_payload_metadata_changes':source_changes,'capcut_json_hash_changes':capchanges,'phase0_seal_checks':seal,'verification_counts':checks,'limitations':'Metadata comparison is sequential, not an atomic snapshot or array-payload rehash; app-managed ephemeral Git refs may change outside commands issued by this audit.'};(O/'final-preservation-verification.json').write_text(json.dumps(r,indent=2));print('source_metadata_changes',len(source_changes),'git_internal_metadata_changes',len(changes),'phase0_seals_PASS',len(seal),'git_fullrefs_same',final['local-refs']['same_stdout_as_initial'],'report_words',len((O/'CONTINUATION_REPORT.md').read_text().split()))
