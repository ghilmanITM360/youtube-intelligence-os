from audit import *
import io, sqlite3, zipfile, importlib.util

F='research/finance-economics-intelligence/'
def blob(b):return run(['git','cat-file','blob',b],raw=True)['stdout']
def tree(ref):
 out=[]
 for l in git('ls-tree','-rl',ref).splitlines():
  m,_,p=l.partition('\t');v=m.split()
  if len(v)==4 and v[1]=='blob':out.append({'path':p,'blob':v[2],'bytes':int(v[3])})
 return out
def jsonat(ref,p):return json.loads(git('show',ref+':'+p))
def finance(ref,label):
 rows=[json.loads(l) for l in git('show',ref+':'+F+'VIDEO_AUDIT_966.jsonl').splitlines()]
 vids=[r['Video_ID'] for r in rows];by={r['Video_ID']:r for r in rows};complete={'COMPLETE_EVIDENCE_BACKED','COMPLETE_LIMITED_EVIDENCE'}
 status=[]
 for r in rows:
  ss=list(r['statuses'].values())
  if all(s in complete for s in ss):s='ACCEPTED_LIMITED' if 'COMPLETE_LIMITED_EVIDENCE' in ss else 'ACCEPTED_FULL'
  elif any(s=='BLOCKED_MISSING_SOURCE' for s in ss):s='BLOCKED'
  elif any(s=='IN_PROGRESS' for s in ss) or any(s in complete for k,s in r['statuses'].items() if k!='PERFORMANCE_REVIEW'):s='PARTIAL'
  else:s='PENDING'
  status.append({'scope':label,'Video_ID':r['Video_ID'],'Channel_ID':r.get('Channel_ID'),'channel':r['identity'].get('Channel'),'batch_id':r.get('batch_id'),'overall_disposition':s,**r['statuses']})
 csvout('finance/'+label+'-record-dispositions.csv',status)
 universe=list(csv.DictReader(io.StringIO(git('show',ref+':'+F+'reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv'))))
 for row in universe:row['Video_ID']=row.get('Video_ID',row.get('video_id'))
 channels=list(csv.DictReader(io.StringIO(git('show',ref+':'+F+'reconciliation-all-repository-2026-10-21/CHANNEL_DIRECTORY.csv'))))
 result={'ref':ref,'sha':git('rev-parse',ref),'registered_original':len(rows),'original_unique_video_ids':len(set(vids)),'duplicate_original_ids':len(vids)-len(set(vids)),'universe_rows':len(universe),'unique_universe_video_ids':len({r['Video_ID'] for r in universe}),'channel_directory_rows':len(channels),'channels_in_original':len({r.get('Channel_ID') for r in rows}),'dispositions_original':dict(Counter(x['overall_disposition'] for x in status)),'coverage_by_dimension':{d:dict(Counter(r['statuses'][d] for r in rows)) for d in rows[0]['statuses']},'next_untouched_original':next(({'Video_ID':r['Video_ID'],'title':r['identity']['Title']} for r in rows if all(s=='NOT_STARTED' for k,s in r['statuses'].items() if k!='PERFORMANCE_REVIEW')),None),'source_blocked_overlapping':sum(any(s=='BLOCKED_MISSING_SOURCE' for s in r['statuses'].values()) for r in rows),'legacy_in_progress_overlapping':sum(any(s=='IN_PROGRESS' for s in r['statuses'].values()) for r in rows),'universe_csv_columns':list(universe[0]),'disposition_policy':'Mutually exclusive: all six complete -> accepted; any blocked -> blocked; any authored complete or IN_PROGRESS -> partial; baseline performance alone does not count as authored partial. Expansion 646 are separate pending metadata-only rows.'}
 for key in ['Audit_status','Audit_state','Deep_audit_status','Population_layer','population_layer','Audit_Status']:
  if key in universe[0]:result['universe_'+key]=dict(Counter(r[key] for r in universe))
 for label2,p in [('progress','FINANCE_PROGRESS_CHECKPOINT.json'),('validation','VALIDATION_966.json')]:
  d=jsonat(ref,F+p);result[label2+'_declared']={k:v for k,v in d.items() if not isinstance(v,(dict,list))}
 write('finance/'+label+'-summary.json',result)
 return result,by

def main():
 remote=[r for r in read('branch_matrix.json') if r['kind']=='remote']
 trees={};objects={};textrefs=[]
 for r in remote:
  ts=trees.setdefault(r['sha'],tree(r['ref'])) if r['sha'] not in trees else trees[r['sha']]
  for t in ts:
   d=objects.setdefault(t['blob'],{'bytes':t['bytes'],'paths':set(),'refs':set()});d['paths'].add(t['path']);d['refs'].add(r['ref'])
 write('data_object_coverage.json',{'remote_branches':len(remote),'unique_tip_snapshots':len(trees),'unique_tip_blobs':len(objects),'note':'Same blob on several branches is one content version, not independent evidence.'})
 # CSV/JSONL census over unique branch-tip blobs. Status remains per-schema.
 structured=[];idsets=defaultdict(set);parse_errors=[];content_cache={}
 if (OUT/'structured_datasets.csv').exists():
  structured=list(csv.DictReader((OUT/'structured_datasets.csv').open()));parse_errors=read('structured_parse_issues.json');objects={}
 for b,d in objects.items():
  candidates=[p for p in d['paths'] if p.endswith(('.csv','.jsonl'))]
  if not candidates or d['bytes']>64*1024**2:continue
  raw=blob(b)
  try:s=raw.decode('utf-8-sig')
  except UnicodeDecodeError:continue
  path=sorted(candidates)[0];rows=[];bad=0
  try:
   if path.endswith('.csv'):rows=list(csv.DictReader(io.StringIO(s)))
   else:
    for i,l in enumerate(s.splitlines(),1):
     if not l.strip():continue
     try:v=json.loads(l);rows.append(v)
     except Exception:bad+=1
   ids=[];channels=[];statuses=Counter()
   for row in rows:
    if not isinstance(row,dict):continue
    for k in ['Video_ID','video_id','youtube_video_id','YouTube_Video_ID']:
     v=row.get(k)
     if isinstance(v,str) and re.fullmatch(r'[A-Za-z0-9_-]{11}',v):ids.append(v);break
    for k in ['Channel_ID','channel_id','youtube_channel_id']:
     v=row.get(k)
     if isinstance(v,str) and (v.startswith('UC') or v.startswith('CH-')):channels.append(v);break
    for k in ['status','Status','audit_status','overall_status','Audit_status','acceptance_status']:
     if isinstance(row.get(k),str):statuses[row[k]]+=1;break
   rec={'blob':b,'paths':sorted(d['paths']),'refs':sorted(d['refs']),'bytes':d['bytes'],'format':Path(path).suffix,'records':len(rows),'unique_video_ids':len(set(ids)),'duplicate_video_id_rows':len(ids)-len(set(ids)),'unique_channel_ids':len(set(channels)),'statuses':dict(statuses),'invalid_lines':bad,'columns':list(rows[0])[:65] if rows and isinstance(rows[0],dict) else []}
   structured.append(rec)
   for p in d['paths']:idsets[p].update(ids)
   if bad:parse_errors.append({'blob':b,'paths':sorted(d['paths']),'invalid_lines':bad})
  except Exception as e:parse_errors.append({'blob':b,'paths':sorted(d['paths']),'error':str(e)})
 csvout('structured_datasets.csv',structured);write('structured_parse_issues.json',parse_errors)
 if idsets:csvout('logical_video_ids_by_path.csv',[{'path':p,'unique_ids_across_branch_versions':len(v),'warning':'overlapping projections and version history; do not sum'} for p,v in idsets.items()])
 # Finance directly recomputed for three distinct branch roles.
 c,cb=finance('origin/research/finance-economics-intelligence','canonical')
 a,ab=finance('origin/codex/finance-machine-a-owner-directed','machine-a-published')
 co,_=finance('origin/codex/yios-dual-machine-coordination','coordination-snapshot')
 completed=lambda by:{v for v,r in by.items() if all(s in {'COMPLETE_EVIDENCE_BACKED','COMPLETE_LIMITED_EVIDENCE'} for s in r['statuses'].values())}
 write('finance/branch-comparison.json',{'canonical':c,'machine_a_published':a,'coordination':co,'extra_completed_ids_on_machine_a':sorted(completed(ab)-completed(cb)),'canonical_completed_not_on_machine_a':sorted(completed(cb)-completed(ab)),'canonical_is_ancestor_of_machine_a':run(['git','merge-base','--is-ancestor',c['sha'],a['sha']])['code']==0,'canonical_vs_machine_a_counts':git('rev-list','--left-right','--count',c['sha']+'...'+a['sha']),'machine_a_not_merged_into_canonical':True})
 # Immutable source check against actual local materialized bytes.
 frozen=jsonat('HEAD',F+'audit-baseline/MANIFEST.json');checks=[]
 for rel,expected in frozen['source_hashes'].items():
  p=ROOT/rel;actual=sha(p) if p.is_file() else None;checks.append({'path':str(p),'expected_sha256':expected,'actual_sha256':actual,'bytes':p.stat().st_size if p.exists() else None,'status':'MATCH' if actual==expected else 'MISSING_OR_MISMATCH'})
 csvout('finance/frozen_sources.csv',checks)
 # SQLite is queried strictly read-only; frozen source DB is not rebuilt.
 dbs=[]
 for p in (ROOT/'data/catalog').glob('*.db'):
  d={'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
  try:
   with sqlite3.connect(f'file:{p}?mode=ro',uri=True) as con:
    d['integrity']=con.execute('PRAGMA integrity_check').fetchall();d['foreign_key_violations']=con.execute('PRAGMA foreign_key_check').fetchall()
    tables=[t[0] for t in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    d['tables']={t:con.execute('SELECT count(*) FROM "'+t.replace('"','""')+'"').fetchone()[0] for t in tables}
    d['schema']={t:con.execute('PRAGMA table_info("'+t.replace('"','""')+'")').fetchall() for t in tables}
    if 'transcripts' in tables:
     cols=[r[1] for r in con.execute('PRAGMA table_info(transcripts)')]
     if 'transcript_text' in cols:d['nonempty_transcripts']=con.execute("SELECT count(*) FROM transcripts WHERE transcript_text IS NOT NULL AND trim(transcript_text)!=''").fetchone()[0]
  except Exception as e:d['error']=str(e)
  dbs.append(d)
 write('sqlite_inventory.json',dbs)
 # Local ZIP member availability, without extracting or copying original media.
 ziprows=[]
 files=list(csv.DictReader((OUT/'files.csv').open()))
 for row in files:
  p=Path(row['path'])
  if p.suffix.lower()!='.zip' or row['scope'] in ['shared-git-common'] or row['category']=='runtime_cache_dependencies':continue
  try:
   with zipfile.ZipFile(p) as z:
    members=[x for x in z.infolist() if not x.is_dir() and not x.filename.startswith('__MACOSX/')]
    ziprows.append({'path':str(p),'compressed_file_bytes':p.stat().st_size,'members':len(members),'member_uncompressed_bytes':sum(x.file_size for x in members),'text_members':sum(Path(x.filename).suffix in ['.txt','.srt','.vtt'] for x in members),'media_members':sum(Path(x.filename).suffix.lower() in ['.mp4','.wav','.m4a','.mp3'] for x in members),'note':'ZIP central directory readable; member CRC/full decompression not globally tested; archive members not independent source copies'})
  except Exception as e:ziprows.append({'path':str(p),'error':str(e)})
 csvout('zip_archives.csv',ziprows)
 # Validate complete 456-file local media library against the published registry.
 media=[json.loads(l) for l in git('show','origin/research/local-channel-media-library:research/media-library/SOURCE_INVENTORY.jsonl').splitlines()]
 mr=[];media_root=Path.home()/'Documents/YIOS-Media-Library'
 for r in media:
  rel=r['original_relative_path'];p=media_root/rel;expected=r['sha256'];actual=sha(p) if p.is_file() else None
  mr.append({'video_id':r.get('video_id'),'mapping_confidence':r.get('mapping_confidence'),'source_channel':r['source_channel'],'media_type':r['asset_type'],'path':str(p),'registered_original_path':r.get('external_source_path'),'registered_original_exists':Path(r.get('external_source_path','/missing')).is_file(),'expected_bytes':int(r['byte_count']),'actual_bytes':p.stat().st_size if p.exists() else None,'expected_sha256':expected,'actual_sha256':actual,'status':'MATCH' if actual==expected else 'MISSING_OR_MISMATCH'})
 csvout('media_integrity.csv',mr);write('media_integrity_summary.json',{'records':len(mr),'matches':sum(r['status']=='MATCH' for r in mr),'videos':sum(r['media_type']=='VIDEO' for r in mr),'audio':sum(r['media_type']=='AUDIO' for r in mr),'bytes':sum(r['expected_bytes'] for r in mr),'high_confidence_mappings':sum(r['mapping_confidence']=='HIGH' for r in mr),'unique_mapped_video_ids':len({r['video_id'] for r in mr if r['video_id']}),'source_folder_counts':dict(Counter(r['source_channel'] for r in mr))})
 # No evidence claims are established from a URL/manifest alone.
 write('data_audit_summary.json',{'unique_structured_blob_versions':len(structured),'parse_issue_versions':len(parse_errors),'frozen_sources_match':sum(r['status']=='MATCH' for r in checks),'frozen_sources_total':len(checks),'finance_canonical_complete':sum(v for k,v in c['dispositions_original'].items() if k.startswith('ACCEPTED')),'finance_machine_a_complete':sum(v for k,v in a['dispositions_original'].items() if k.startswith('ACCEPTED')),'media_matches':sum(r['status']=='MATCH' for r in mr)})
 print(json.dumps(read('data_audit_summary.json'),indent=2))
if __name__=='__main__':main()
