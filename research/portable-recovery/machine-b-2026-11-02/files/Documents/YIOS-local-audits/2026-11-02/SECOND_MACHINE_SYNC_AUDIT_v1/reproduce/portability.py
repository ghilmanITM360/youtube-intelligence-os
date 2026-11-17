from audit import *
from data_audit import tree,blob
import io
def main():
 rows=read('branch_matrix.json');ref='origin/research/casually-finance-editing-forensics';ts=tree(ref)
 ts += [t for t in tree('origin/research/finance-economics-intelligence') if t['path'].startswith('research/visual-forensics/channels/casual-finance/')]
 by={t['path']:t for t in ts}
 hashes=defaultdict(list)
 for r in csv.DictReader((OUT/'file_hashes_bounded.csv').open()):hashes[r['sha256']].append({'path':r['path'],'bytes':int(r['bytes'])})
 for r in csv.DictReader((OUT/'media_integrity.csv').open()):
  if r['status']=='MATCH':hashes[r['expected_sha256']].append({'path':r['path'],'bytes':int(r['actual_bytes'])})
 portable=[];external=[];videos=[];texts={};hcache={}
 def bsha(t):
  if t['blob'] not in hcache:hcache[t['blob']]=hashlib.sha256(blob(t['blob'])).hexdigest()
  return hcache[t['blob']]
 for t in ts:
  p=t['path']
  if 'research/visual-forensics/channels/casual-finance/' not in p or not p.endswith('/EXTERNAL_EVIDENCE_MANIFEST.json'):continue
  d=json.loads(blob(t['blob']));root=p.rsplit('/',1)[0];vid=root.rsplit('/',1)[1]
  ref='origin/research/finance-economics-intelligence' if vid in ['o3FQcd91MIs','Uumnx2Fo6cE'] else 'origin/research/casually-finance-editing-forensics'
  pm=by.get(root+'/PORTABLE_MANIFEST.json');pd=json.loads(blob(pm['blob'])) if pm else {}
  gatepath=root+'/QUALITY_GATE.json'
  if gatepath not in by:gatepath=root+'/research/QUALITY_GATE.json'
  if gatepath not in by:gatepath=root+'/research/v2/quality_gate_v2.json'
  gate=json.loads(blob(by[gatepath]['blob'])) if gatepath in by else {}
  workspace=d.get('external_root_machine_A') or d.get('external_private_evidence',{}).get('workspace') or pd.get('external_root_machine_A')
  source=d.get('source_mp4',{})
  srcsha=d.get('source_sha256') or source.get('sha256') or pd.get('source_sha256')
  srcpath=source.get('local_path') or pd.get('source_mp4',{}).get('historical_path_machine_A')
  if not srcpath and d.get('source_filename'):srcpath=d.get('local_path_machine_A','')+d['source_filename']
  srcsize=d.get('size_bytes') or source.get('bytes') or pd.get('source_bytes')
  found=hashes.get(srcsha,[])
  external.append({'video_id':vid,'kind':'SOURCE_MP4','source_path_machine_a':srcpath or 'UNKNOWN','expected_sha256':srcsha,'expected_bytes':srcsize,'actual_matching_locations':found,'presence':'PRESENT_ELSEWHERE_VERIFIED_BY_HASH' if found else 'REFERENCED_MACHINE_A_NOT_LOCATED','purpose':'Exact source bytes for reproducible visual measurement; do not redownload if existing hash-matching copy suffices','manifest':p})
  listed=0;missing=0;knownbytes=0
  for f in d.get('files',[]):
   found=hashes.get(f.get('sha256'),[]);listed+=1;missing+=not bool(found);knownbytes+=f.get('bytes',0)
   external.append({'video_id':vid,'kind':'EXCLUDED_EVIDENCE','source_path_machine_a':str(Path(workspace or 'UNKNOWN')/f['path']),'expected_sha256':f.get('sha256'),'expected_bytes':f.get('bytes'),'actual_matching_locations':found,'presence':'PRESENT_ELSEWHERE_VERIFIED_BY_HASH' if found else 'REFERENCED_MACHINE_A_NOT_LOCATED','purpose':'Frames/audio/arrays required to independently verify published visual observations','manifest':p})
  # Latest checksum entries per path, including earlier scopes when later manifests cover only derived tables.
  sums=[x for x in ts if x['path'].startswith(root+'/research/') and re.search(r'/(?:EVIDENCE_SHA256SUMS|SHA256SUMS)',x['path']) and x['bytes']<1_000_000]
  expected={}
  for s in sorted(sums,key=lambda x:x['path']):
   for line in blob(s['blob']).decode(errors='replace').splitlines():
    m=re.match(r'^([a-f0-9]{64})\s+\*?(.+)$',line)
    if not m:continue
    rel=m[2].removeprefix('./');expected[(rel,m[1])]=s['path']
  # Keep separate expected versions when historical checksum scopes disagree.
  for (rel,h),manifest in expected.items():
   gitpath=root+'/research/'+rel
   if gitpath in by:continue
   if any(e['video_id']==vid and e.get('expected_sha256')==h for e in external):continue
   found=hashes.get(h,[])
   external.append({'video_id':vid,'kind':'EXTERNAL_CHECKSUM_ENTRY','source_path_machine_a':str(Path(workspace or 'UNKNOWN_WORKSPACE')/rel),'expected_sha256':h,'expected_bytes':found[0]['bytes'] if found else None,'actual_matching_locations':found,'presence':'PRESENT_ELSEWHERE_VERIFIED_BY_HASH' if found else 'REFERENCED_MACHINE_A_NOT_LOCATED','purpose':'Checkpoint-scoped external evidence; unknown sizes must be measured at source','manifest':manifest})
  # Verify published Git package members directly against Git bytes, not local checkout paths.
  for f in pd.get('files',[]):
   gp=root+'/'+f['path'];obj=by.get(gp);actual=bsha(obj) if obj else None
   portable.append({'video_id':vid,'ref':ref,'path':gp,'expected_sha256':f['sha256'],'actual_git_sha256':actual,'bytes':obj['bytes'] if obj else None,'status':'MATCH' if actual==f['sha256'] else ('MISSING' if not obj else 'MISMATCH'),'checked_out_here':(ROOT/gp).exists()})
  videos.append({'video_id':vid,'ref':ref,'source_path_machine_a':srcpath,'source_sha256':srcsha,'source_bytes':srcsize,'source_bytes_here':bool(found) if False else bool(hashes.get(srcsha)),'source_matching_paths':hashes.get(srcsha,[]),'workspace_machine_a':workspace,'manifest_external_file_entries':listed,'manifest_external_known_bytes':knownbytes,'manifest_external_entries_not_located':missing,'quality_gate_path':gatepath,'quality_gate':gate,'portable_contract':pd.get('contract'),'git_package_files':sum(x['path'].startswith(root+'/') for x in ts),'git_package_blob_bytes':sum(x['bytes'] for x in ts if x['path'].startswith(root+'/')),'workspace_resolution_note':'Exact published path where given; UNKNOWN_WORKSPACE means no authoritative root established.'})
 write('visual_packages.json',videos);csvout('visual_portable_hashes.csv',portable)
 csvout('machine_a_transfer_requirements.csv',external);write('machine_a_transfer_requirements.json',external)
 # Search every branch-tip filename plus text references for Video006; absence is scoped evidence.
 hits=[];unique_text={}
 for r in rows:
  if r['kind']!='remote':continue
  treefile=OUT/r['tree_index']
  for t in csv.DictReader(treefile.open()):
   if 'xtqbRt94TTw' in t['path']:hits.append({'ref':r['ref'],'path':t['path'],'kind':'FILENAME'})
   if Path(t['path']).suffix in ['.md','.json','.csv','.jsonl','.txt','.py'] and int(t['git_blob_bytes'])<2_000_000:
    unique_text.setdefault(t['blob'],{'refs':set(),'paths':set()});unique_text[t['blob']]['refs'].add(r['ref']);unique_text[t['blob']]['paths'].add(t['path'])
 absrefs=[];claims=[];gates=[];secrets=[]
 spec=importlib.util.spec_from_file_location('scan',ROOT/'scripts/scan_tracked_secrets.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 for b,meta in unique_text.items():
  raw=blob(b);s=raw.decode(errors='replace')
  if 'xtqbRt94TTw' in s:hits.append({'refs':sorted(meta['refs']),'paths':sorted(meta['paths']),'kind':'TEXT_REFERENCE'})
  for typ,pat in mod.PATTERNS.items():
   if pat.search(raw):secrets.append({'type':typ,'paths':sorted(meta['paths']),'refs':sorted(meta['refs']),'values':'REDACTED_NOT_RECORDED'})
  matches=Counter(re.findall(r'/Users/[^/\s\"\'`<>]+/',s))
  if matches:absrefs.append({'blob':b,'paths':sorted(meta['paths']),'refs':sorted(meta['refs']),'machine_path_prefix_occurrences':dict(matches)})
  candidates=[p for p in meta['paths'] if p.endswith('.json')]
  if not candidates:continue
  try:d=json.loads(s)
  except Exception:continue
  if not isinstance(d,dict):continue
  arr={k:len(v) for k,v in d.items() if isinstance(v,list)}
  scalars={k:v for k,v in d.items() if isinstance(v,(str,bool,int,float,type(None))) and (any(x in k.lower() for x in ['status','valid','pass','fail','count','complete','check','accepted','partial','blocked','pending']) or k in ['batch_id','video_id','Video_ID','checkpoint'])}
  if arr or scalars:claims.append({'blob':b,'paths':sorted(meta['paths']),'refs':sorted(meta['refs']),'array_record_counts':arr,'declarations':scalars})
  if any(re.search(r'validat|gate|status|checkpoint',p,re.I) for p in candidates):gates.append({'blob':b,'paths':sorted(meta['paths']),'refs':sorted(meta['refs']),'declarations':scalars,'array_counts':arr,'authority':'PUBLISHED_DECLARATION_NOT_A_FRESH_VALIDATION'})
 csvout('absolute_machine_path_references.csv',absrefs);csvout('json_schema_record_counts.csv',claims);write('published_validation_declarations.json',gates)
 package_hits=[h for h in hits if any('research/visual-forensics/channels/casual-finance/xtqbRt94TTw/' in p for p in h.get('paths',[h.get('path','')]))]
 write('video006_remote_search.json',{'video_id':'xtqbRt94TTw','branch_tips_searched':46,'filename_hits_and_bounded_text_hits':hits,'published_ct_scan_package_hits':package_hits,'text_limit_bytes':2_000_000,'conclusion':'NO_PUBLISHED_CT_SCAN_PACKAGE_LOCATED' if not package_hits else 'SEE_PACKAGE_HITS','historical_only':'Owner reports Checkpoint B, first-pass shards 1 and 3 structurally passed, eight pending; current Machine A files/processes not inspected','transfer_required':'Preserve and transfer entire unpublished Video006 workspace, source manifest, checksum manifests, original reviewer responses and input shards, frames/audio. Match source MP4 via local media registry first. Authoritative unpublished-workspace path/hash/size UNKNOWN until Machine A supplies its local manifest.'})
 write('branch_tip_secret_scan.json',{'unique_text_blobs_scanned':len(unique_text),'limit_bytes':2_000_000,'patterns':list(mod.PATTERNS),'findings':secrets,'scope':'All remote branch tip text candidates; not exhaustive historical or binary scan; root full tracked scan separately executed; no secret values printed.'})
 write('portability_summary.json',{'visual_packages':len(videos),'portable_entries_match':sum(r['status']=='MATCH' for r in portable),'portable_entries_mismatch':sum(r['status']!='MATCH' for r in portable),'external_checksum_entries':len(external),'external_entries_present_by_hash':sum(r['presence']=='PRESENT_ELSEWHERE_VERIFIED_BY_HASH' for r in external),'abs_path_blob_versions':len(absrefs),'secret_findings':len(secrets),'video006_hits':len(hits)})
 print(json.dumps(read('portability_summary.json'),indent=2))
if __name__=='__main__':
 import importlib.util
 main()
