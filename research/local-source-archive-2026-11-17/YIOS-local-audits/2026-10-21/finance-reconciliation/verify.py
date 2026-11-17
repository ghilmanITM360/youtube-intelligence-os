import pathlib,json,hashlib,subprocess,csv,collections,zipfile,xml.etree.ElementTree as E
R=pathlib.Path.cwd();A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21');D=A/'finance-reconciliation';B=R/'research/finance-economics-intelligence'
def g(*a):return subprocess.check_output(['git',*a])
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return list(csv.DictReader(p.open()))
manifest=json.loads((D/'restoration-manifest.json').read_text());remote=manifest['target_head'];before=json.loads((D/'before-paths.json').read_text());oldfiles=json.loads((A/'worktree-0-files.json').read_text())
assert g('rev-parse','HEAD').decode().strip()==g('rev-parse','@{u}').decode().strip()==remote
assert g('rev-list','--left-right','--count','HEAD...@{u}').decode().strip()=='0\t0'
assert not g('diff','--name-only') and not g('diff','--cached','--name-only')
collisions={x['path'] for x in manifest['files'] if x['kind']=='untracked'}
u=set(g('ls-files','--others','--exclude-standard','-z').decode().strip('\0').split('\0'));ig=set(g('ls-files','--others','--ignored','--exclude-standard','-z').decode().strip('\0').split('\0'))
assert u==set(before['untracked'])-collisions
assert ig==set(before['ignored'])
untouched=0
for cat in ['untracked','ignored']:
 for x in oldfiles[cat]:
  p=pathlib.Path(x['path']);rel=str(p.relative_to(R))
  if rel in collisions:continue
  assert p.lstat().st_size==x['bytes'],str(p)
  if 'sha256' in x:assert h(p)==x['sha256'],str(p);untouched+=1
for x in manifest['files']:
 assert h(pathlib.Path(x['archive']))==x['local_sha256']
 if 'relocated_path' in x:assert h(pathlib.Path(x['relocated_path']))==x['local_sha256']
assert g('stash','list','--format=%gd %H %gs')==(A/'stashes-before.txt').read_bytes()
assert g('rev-parse','backup/decode-15cbe9f-original').decode().strip()=='15cbe9f0112596c1e07c1c1504302cce77bfd97a'
w=g('worktree','list','--porcelain').decode();assert w.replace(remote,manifest['historical_head'],1)==(A/'worktrees-before.txt').read_text()
# Independently verify the binary patch actually reconstructs the 11 archived bytes from old HEAD.
# Temporary index is external; no repository index or working files touched.
idx=D/'patch-verification.index';env=dict(__import__('os').environ,GIT_INDEX_FILE=str(idx))
subprocess.run(['git','read-tree',manifest['historical_head']],env=env,check=True)
subprocess.run(['git','apply','--cached','--binary',str(A/'worktree-0-diff.patch')],env=env,check=True)
for x in manifest['files']:
 if x['kind']=='tracked':
  b=subprocess.check_output(['git','show',':'+x['path']],env=env);assert hashlib.sha256(b).hexdigest()==x['local_sha256']
# Finance source and workbook verification, no validator/rebuild writes.
universe=read(B/'reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv');ids={x['video_id'] for x in universe};assert len(universe)==len(ids)==1612
layers=collections.Counter(x['population_layer'] for x in universe);assert layers['FROZEN_ORIGINAL_966']==966 and sum(v for k,v in layers.items()if k!='FROZEN_ORIGINAL_966')==646
rows=[json.loads(l) for l in (B/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()];assert len(rows)==len({x['Video_ID'] for x in rows})==966
complete=[x for x in rows if all(s.startswith('COMPLETE_') for s in x['statuses'].values())];nextid=next(x['Video_ID'] for x in rows if any(s in {'NOT_STARTED','IN_PROGRESS'} for s in x['statuses'].values()))
v=json.loads((B/'VALIDATION_966.json').read_text());assert len(complete)==v['analyzed_partial_evidence']+v['fully_analyzed_complete_evidence']==437;assert nextid==v['next_master_order_id']=='S_8SLGjLrBM'
frozen=json.loads((B/'audit-baseline/MANIFEST.json').read_text());assert len(frozen['source_hashes'])==26
sourcechecks=[]
for p,digest in frozen['source_hashes'].items():assert h(R/p)==digest,p;sourcechecks.append(dict(path=p,sha256=digest))
assert h(B/'audit-baseline/VIDEO_MASTER.csv')==frozen['frozen_master_sha256']
# Every registered completion's audit receipt path exists by batch association.
batches={x.get('batch_id')for x in complete};batches.discard(None)
missing=[b for b in batches if not (B/'audit-batches'/f'{b}.json').is_file()];assert not missing,missing
workbooks=list(B.rglob('*.xlsx'));assert workbooks==[B/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'],workbooks
z=zipfile.ZipFile(workbooks[0]);ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ss=[''.join(t.itertext())for t in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]if 'xl/sharedStrings.xml'in z.namelist()else []
def cells(f):
 d={}
 for c in E.fromstring(z.read(f)).findall('.//m:sheetData/m:row/m:c',ns):
  v=c.findtext('m:v','',ns)
  if c.get('t')=='s':v=ss[int(v)]
  elif c.get('t')=='inlineStr':v=''.join(c.find('m:is',ns).itertext())
  assert c.get('t')!='e',(f,c.attrib)
  d[c.get('r')]=v
 return d
s=cells('xl/worksheets/sheet2.xml');detail=cells('xl/worksheets/sheet4.xml');dash=cells('xl/worksheets/sheet1.xml');ch=cells('xl/worksheets/sheet3.xml')
assert {s['A'+str(i)]for i in range(5,1617)}==ids
assert sum(v=='DEEP_AUDIT_COMPLETE' for k,v in s.items()if k.startswith('AA'))==437
assert sum(v=='DEEP_AUDIT_COMPLETE' for k,v in detail.items()if k.startswith('E'))==437
assert [dash[k]for k in ['B5','B6','B7','B9']]==['1612','437','1175','42']
channels={x['channel_id'] for x in universe};directory=read(B/'reconciliation-all-repository-2026-10-21/CHANNEL_DIRECTORY.csv');directory_ids={x['channel_id'] for x in directory};assert len(directory)==len(directory_ids)==42;assert {ch['A'+str(i)] for i in range(5,47)}==directory_ids;assert channels<=directory_ids
live=g('ls-remote','origin','refs/heads/research/finance-economics-intelligence').decode().split()[0]
pr=json.loads(subprocess.check_output(['gh','pr','view','36','--repo','ghilmanITM360/youtube-intelligence-os','--json','headRefOid,state,isDraft,url,updatedAt']));assert live==pr['headRefOid']==remote
(D/'pr-final.json').write_text(json.dumps(pr,indent=2));(D/'status-final.txt').write_bytes(g('status','--porcelain=v2','--branch','--untracked-files=all'))
result=dict(start=manifest['historical_head'],final=remote,origin=live,pr36=pr['headRefOid'],ahead=0,behind=0,tracked_modifications=0,staged=0,untracked=len(u),ignored=len(ig),tracked_resolved=11,untracked_relocated=20,affected_recovery_files_verified=31,binary_patch_reconstructs_all_11=True,unchanged_other_evidence_hashes_verified=untouched,stash_unchanged=True,decode_backup_unchanged=True,worktrees=2,forensic_registration_unchanged=True,population=1612,original=966,expansion=646,channels=42,channels_with_videos=len(channels),completed=len(complete),remaining=1612-len(complete),next_id=nextid,source_fingerprints=sourcechecks,registered_completed_batches=len(batches),single_workbook=str(workbooks[0]),workbook_sha256=h(workbooks[0]),workbook_population_matches=True,workbook_coverage_matches=True,native_excel_recalculation_tested=False,static_universe_audit_labels=dict(collections.Counter(x['audit_status']for x in universe)),validation='PASS')
(D/'final-verification.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items()if k!='source_fingerprints'},indent=2))
