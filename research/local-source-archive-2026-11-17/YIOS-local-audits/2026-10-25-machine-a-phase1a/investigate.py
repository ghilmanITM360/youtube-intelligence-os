from pathlib import Path
import os,json,csv,gzip,hashlib,subprocess,ast,struct,collections,datetime
OUT=Path(__file__).parent; OLD=OUT.parent/'2026-10-25-machine-a-phase0'; REPO=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os'); WHAT=REPO.parent/'video data of what if'; CF=REPO.parent/'yio-cf-editing-forensics-local-evidence'
env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','GIT_NO_LAZY_FETCH':'1','GIT_TERMINAL_PROMPT':'0'}
def dump(n,v): (OUT/n).write_text(json.dumps(v,indent=2))
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO,env=env)
hashcache={};readbytes=0
def sha(p):
 global readbytes
 p=Path(p);st=p.stat();key=str(p)
 if key in hashcache and hashcache[key]['stat']==[st.st_size,st.st_mtime_ns,st.st_ino]:return hashcache[key]['sha256']
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk);readbytes+=len(chunk)
 st2=p.stat();assert (st.st_size,st.st_mtime_ns,st.st_ino)==(st2.st_size,st2.st_mtime_ns,st2.st_ino)
 hashcache[key]={'sha256':h.hexdigest(),'stat':[st.st_size,st.st_mtime_ns,st.st_ino]};return h.hexdigest()
# preserve checkpoint seal verification and baseline only stat, never mutate source.
seal=[]
for line in (OLD/'SHA256SUMS').read_text().splitlines():
 expected,rel=line.split('  ',1);actual=sha(OLD/rel);seal.append({'file':rel,'expected':expected,'actual':actual,'status':'PASS' if actual==expected else 'MISMATCH'})
dump('phase0-seal-verification.json',seal)
with gzip.open(OLD/'classified-files.csv.gz','rt') as f: oldrows=list(csv.DictReader(f))
baseline={};changes=[]
for r in oldrows:
 p=Path(r['path'])
 try:
  s=p.stat();baseline[str(p)]=[s.st_size,s.st_mtime_ns,s.st_ino]
  if baseline[str(p)]!=[int(r['bytes']),int(r['mtime_ns']),int(r['inode'])]:changes.append(str(p))
 except OSError as e:changes.append({'path':str(p),'error':str(e)})
dump('source-metadata-baseline.json',baseline);dump('changes-since-phase0.json',changes)
# current live branch tip trees, exact blob comparison without lazy fetch.
snap=json.loads((OUT/'live-snapshot.json').read_text());refs={l.split()[1]:l.split()[0] for l in snap['receipts']['live-refs']['stdout'].splitlines() if 'refs/heads/' in l}
blobs=collections.defaultdict(list);coverage=[]
for ref,tip in refs.items():
 try:
  data=git('ls-tree','-rz',tip)
  for e in data.split(b'\0'):
   if not e:continue
   meta,name=e.split(b'\t',1);mode,typ,oid=meta.split()
   if typ==b'blob':blobs[oid.decode()].append({'ref':ref,'tip':tip,'path':name.decode()})
  coverage.append({'ref':ref,'sha':tip,'status':'READABLE'})
 except subprocess.CalledProcessError:coverage.append({'ref':ref,'sha':tip,'status':'UNREADABLE'})
dump('live-tree-coverage.json',coverage)
# Exact proposed per-file integration list. Original content, future destinations only.
text_ext={'.md','.csv','.json','.txt','.py','.html','.sha256','.log','.lock'};plans=[]
for p in sorted(WHAT.rglob('*')):
 if not p.is_file() or p.is_symlink():continue
 rel=p.relative_to(WHAT);part=rel.parts[0]
 if p.suffix.lower() not in text_ext:continue
 if any(x in rel.parts for x in ['__pycache__']):continue
 data=p.read_bytes();h=sha(p);oid=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();matches=blobs.get(oid,[])
 action='PROPOSE_GIT_PRESERVE';dest='research/visual-forensics/channels/CH-000004/what-if-source-package/'+str(rel);role='source research / retrospective evidence';scope='WHAT_IF_REFERENCE';hold=''
 if 'legacy' in rel.parts:action='PRESERVE_EXTERNAL_DUPLICATE_OR_HISTORY';dest='';role='historical master duplicate; compare hash before integration'
 elif part=='releases':action='PROPOSE_GIT_FROZEN_SNAPSHOT';role='frozen release; retain own manifest semantics'
 elif part=='production_intelligence_brain':role='channel DNA / master facts / recipes / validation contract'
 elif part in ['generalization_tests','chair_test_stage_a','chair_test_v2_review']:
  scope='ORIGINAL_PRODUCTION_EXPERIMENT';dest='research/production-experiments/what-if-derived/'+str(rel);role='experiment / negative finding; not channel observation';hold='Preserve estimated timings, rejected status, original-character/asset provenance and local dependencies'
 if matches:action='ALREADY_EXACT_AT_LIVE_TIP_REVIEW_REFERENCE';dest=''
 if part=='videos':action='EXTERNAL_ONLY';dest=''
 plans.append({'source_path':str(p),'relative_path':str(rel),'bytes':len(data),'sha256':h,'git_blob_sha1':oid,'scope':scope,'role':role,'proposed_action':action,'proposed_repository_path':dest,'live_tip_matches':json.dumps(matches,separators=(',',':')),'gate':hold or 'Owner writer approval, provenance/rights review, no automatic promotion or source-ID join'})
with (OUT/'what-if-proposed-integration.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(plans[0]));w.writeheader();w.writerows(plans)
dump('what-if-plan-summary.json',{'files':len(plans),'bytes':sum(x['bytes'] for x in plans),'actions':dict(collections.Counter(x['proposed_action'] for x in plans)),'groups':{g:{'files':sum(x['relative_path'].split('/')[0]==g for x in plans),'bytes':sum(x['bytes'] for x in plans if x['relative_path'].split('/')[0]==g)} for g in sorted({x['relative_path'].split('/')[0] for x in plans})}})
# source contract source checks bounded 165MB, no decoding.
contract=json.loads((REPO/'data/manifests/what-if-forensic-source-v1.json').read_text());sources=[]
for s in contract['sources']:
 p=WHAT/s['relative_media_path'];a=sha(p) if p.exists() else None;sources.append({**s,'current_path':str(p),'actual_bytes':p.stat().st_size if p.exists() else None,'actual_sha256':a,'check':'PASS' if a==s['sha256'] and p.stat().st_size==s['size_bytes'] else 'FAIL'})
dump('what-if-source-contract-checks.json',sources)
# CF script inventory and summaries directly at protected tip, header-only npy inspection.
ref=refs['refs/heads/research/casually-finance-editing-forensics'];prefix='research/casually-finance-editing-forensics/'
inv=list(csv.DictReader((OUT/'protected-SOURCE_MEDIA_INVENTORY.csv').open()));rows=[]
for p in sorted(CF.glob('*/gray.npy')):
 vid=p.parent.name;candidates=[x for x in inv if x['Video_ID']==vid and x['Canonical_For_Analysis']=='True'];r=candidates[0] if len(candidates)==1 else {}
 raw=git('show',ref+':'+prefix+'videos/'+vid+'/auto/AUTO_SUMMARY.json');summary=json.loads(raw)
 with p.open('rb') as f:
  assert f.read(6)==b'\x93NUMPY';v=f.read(2);n=struct.unpack('<H' if v[0]==1 else '<I',f.read(2 if v[0]==1 else 4))[0];header=ast.literal_eval(f.read(n).decode().strip());offset=f.tell()
 source=Path('/Users/ghilmankhan/Downloads/CasuallyFinance')/r.get('Relative_Path','MISSING');a=sha(source) if source.is_file() else None
 matches=(a==r.get('SHA256')==summary['source_sha256']) if a else False
 rows.append({'video_id':vid,'gray_path':str(p),'gray_bytes':p.stat().st_size,'npy_header':header,'header_data_bytes_consistent':p.stat().st_size-offset==__import__('math').prod(header['shape']),'inventory_candidate_count':len(candidates),'source_path':str(source),'source_exists':source.is_file(),'source_bytes':source.stat().st_size if source.is_file() else None,'source_expected_sha256':r.get('SHA256'),'source_actual_sha256':a,'source_check':'PASS' if matches else ('MISSING' if not source.is_file() else 'FAIL'),'identity_method':r.get('ID_Match_Method'),'identity_confidence':r.get('ID_Confidence'),'auto_summary':summary,'shape_matches_summary':list(header['shape'])==[summary['frames_decoded'],summary['analysis_size'][1],summary['analysis_size'][0]],'reproduction_status':'NOT_EXECUTED; historical environment and independent byte identity not proven'})
dump('cf-38-reproduction-prerequisites.json',{'protected_ref':ref,'script_sha256':sha(OUT/'protected-forensic_features.py'),'source_inventory_sha256':sha(OUT/'protected-SOURCE_MEDIA_INVENTORY.csv'),'sets':rows})
# checksum path ambiguity resolution: retained historical manifests unchanged, explicit base mapping.
oldchecks=list(csv.DictReader((OLD/'manifest-checks.csv').open()));unresolved=collections.defaultdict(list)
for r in oldchecks:
 if r['status']=='MISSING':unresolved[r['manifest']].append(r)
resolved=[]
for name,rs in unresolved.items():
 manifest=Path(name)
 if 'DS-000027_RAW' in name:base=REPO
 elif name.endswith('visual-ct-scan-installed.SHA256SUMS'):base=Path('/Users/ghilmankhan/.claude/skills/visual-ct-scan')
 elif '/o3FQcd91MIs/research/' in name:base=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-o3FQcd91MIs-deep-ct-scan')
 elif '/Uumnx2Fo6cE/research/' in name:base=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-Uumnx2Fo6cE-deep-ct-scan')
 else:base=manifest.parent
 lines=[]
 for line in manifest.read_text().splitlines():
  if len(line)>66 and all(c in '0123456789abcdef' for c in line[:64].lower()):lines.append((line[:64],line[64:].strip().lstrip('*')))
 for expected,rel in lines:
  p=base/rel;actual=sha(p) if p.is_file() else None
  resolved.append({'manifest':name,'historical_relative':rel,'interpreted_base':str(base),'resolved_path':str(p),'expected_sha256':expected,'actual_sha256':actual,'status':'PASS' if expected==actual else ('MISMATCH' if actual else 'MISSING')})
# latest 003 checkpoint freshly all bytes.
v3=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-5umJ63d3rzQ-deep-ct-scan');latest=[]
for line in (v3/'EVIDENCE_SHA256SUMS_checkpoint4').read_text().splitlines():
 if not line.strip():continue
 expected,rel=line.split(maxsplit=1);p=v3/rel.strip().lstrip('*');actual=sha(p) if p.is_file() else None;latest.append({'path':str(p),'expected_sha256':expected,'actual_sha256':actual,'status':'PASS' if expected==actual else 'FAIL'})
dump('historical-base-resolution.json',resolved);dump('video003-checkpoint4-checks.json',latest)
# known external media dependencies and editable JSON paths; inspect strings, never execute project.
deps=[]
for p in [WHAT/'chair_test_stage_a/chair_test_completed_draft.json',WHAT/'chair_test_stage_a/timeline_02_before_edit.json',WHAT/'chair_test_stage_a/EDIT_PLAN.json',WHAT/'chair_test_v2_review/ASSET_MANIFEST.json']:
 data=json.loads(p.read_text())
 def walk(d,key=''):
  if isinstance(d,dict):
   for k,v in d.items():walk(v,key+'/'+k)
  elif isinstance(d,list):
   for i,v in enumerate(d):walk(v,key+'/'+str(i))
  elif isinstance(d,str) and (d.startswith('/Users/') or ':/' in d):
   q=Path(d);deps.append({'project':str(p),'json_location':key,'dependency':d,'exists_here':q.exists(),'bytes':q.stat().st_size if q.is_file() else None})
 walk(data)
link=WHAT/'chair_test_v2_review/evidence/0921.mp4';target=link.resolve();deps.append({'symlink':str(link),'target':str(target),'exists':target.is_file(),'bytes':target.stat().st_size if target.is_file() else None,'sha256':sha(target) if target.is_file() and target.stat().st_size<200_000_000 else 'NOT_HASHED'})
dump('production-dependencies.json',deps)
dump('read-hash-receipts.json',hashcache);dump('investigation-summary.json',{'hash_bytes_read':readbytes,'phase0_changes':len(changes),'whatif_planned_files':len(plans),'cf_sets':len(rows),'cf_source_checks':dict(collections.Counter(x['source_check'] for x in rows)),'cf_header_match':sum(x['shape_matches_summary'] for x in rows),'resolved_checks':dict(collections.Counter(x['status'] for x in resolved)),'v3_checks':dict(collections.Counter(x['status'] for x in latest))})
print(json.dumps(json.loads((OUT/'investigation-summary.json').read_text()),indent=2))
