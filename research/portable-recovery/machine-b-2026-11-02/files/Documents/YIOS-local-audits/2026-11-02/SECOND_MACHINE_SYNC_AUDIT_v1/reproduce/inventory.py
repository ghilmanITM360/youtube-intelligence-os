from audit import *
import sqlite3, zipfile

def category(rel):
 s=rel.lower();ext=Path(s).suffix
 if any(x in Path(rel).parts for x in ['.venv','node_modules','__pycache__','.pytest_cache','.ruff_cache','.cache','youtube_intelligence_os.egg-info']):return 'runtime_cache_dependencies'
 if Path(rel).name in ['.env'] or '.env.' in Path(rel).name:return 'private_configuration_metadata_only'
 if ext in ['.mp4','.mov','.webm','.mkv','.m4v']:return 'source_video'
 if ext in ['.wav','.mp3','.m4a','.flac','.aac','.ogg']:return 'audio'
 if ext in ['.jpg','.jpeg','.png','.webp','.gif']:
  if 'thumb' in s or 'audit-batches/' in s:return 'thumbnail_images'
  if any(x in s for x in ['sheet','contact','montage']):return 'contact_sheets'
  if any(x in s for x in ['frame','evidence','forensic']):return 'frames_and_visual_evidence'
  return 'other_images'
 if ext in ['.srt','.vtt'] or ('transcript' in s and ext in ['.txt','.zip']):return 'transcripts_subtitles_archives'
 if ext in ['.xlsx','.xls']:return 'workbooks'
 if ext=='.inspect.ndjson':return 'inspection_sidecars'
 if s.endswith('.inspect.ndjson'):return 'inspection_sidecars'
 if any(x in s for x in ['receipt','witness','sources.','source_register','evidence_manifest','checksum','sha256','source_media_inventory']):return 'source_receipts_witnesses_hashes'
 if any(x in s for x in ['calc','calculation']):return 'calculations'
 if any(x in s for x in ['shard','reviewer','original_response','agents/']):return 'reviewer_shards_responses'
 if any(x in s for x in ['state','scene','shot','event','composition','motion','measurement','metrics','objective']):return 'measurement_state_scene_event_ledgers'
 if 'production' in s or 'storyboard' in s or 'blueprint' in s or 'asset_plan' in s:return 'production_intelligence'
 if ext=='.jsonl':return 'jsonl_datasets'
 if ext=='.json':return 'json_datasets_manifests'
 if ext=='.csv':return 'csv_projections'
 if ext in ['.db','.sqlite','.sqlite3']:return 'sqlite_catalogs'
 if ext in ['.py','.js','.mjs','.ts','.sh']:
  return 'tests_validators' if any(x in s for x in ['test','validat','check']) else 'source_code'
 if any(x in s for x in ['prompt','automation','schedule']):return 'prompts_schedulers'
 if ext in ['.md','.pdf','.docx','.txt']:return 'owner_reports_handoffs_documentation'
 if ext in ['.zip','.tar','.gz','.bundle','.patch']:return 'archives_recovery'
 return 'other'

def main():
 before=read('before/checkouts.json');roots=[(Path(d['path']),'checkout-'+str(d['id'])) for d in before]
 for p in (Path.home()/'Documents').iterdir():
  if 'yios' in p.name.lower() and p.resolve()!=ROOT.resolve():roots.append((p,'external-'+p.name))
 for base in [Path.home()/'Downloads',Path.home()/'Desktop',Path.home()/'workprojects']:
  if base.exists():
   for p in base.iterdir():
    if re.search(r'yios|casually.?finance|casual.?economics|nick.?invests|youtube.intelligence',p.name,re.I):roots.append((p,'external-'+p.name))
 # Include configured Git common storage exactly once, independent of worktrees.
 roots.append((ROOT/'.git','shared-git-common'))
 allrows=[];summaries=[];errors=[];inode_seen={};group_stats=defaultdict(lambda:{'files':0,'bytes':0,'allocated_bytes':0,'hardlink_dedup_bytes':0,'examples':[]})
 for base,label in roots:
  subtotal=Counter();tracked=set();ignored=set();untracked=set()
  if label.startswith('checkout'):
   tracked=set(pathlist(['ls-files','-z'],base));d=next(x for x in before if x['path']==str(base));ignored=set(d['ignored']);untracked=set(d['untracked'])
  def files():
   if base.is_file():yield base;return
   for dr,dirs,names in os.walk(base,followlinks=False):
    dp=Path(dr)
    dirs[:]=[n for n in dirs if not (dp/n).resolve().is_relative_to(OUT.resolve()) and (label=='shared-git-common' or n!='.git') and not (n=='worktrees' and dp.name=='.claude') and not ((dp/n).is_symlink())]
    for n in names:yield dp/n
  for p in files():
   try:
    st=p.lstat();rel=str(p.relative_to(base)) if p!=base else p.name
    if p.is_symlink():sz=st.st_size;kind='symlink'
    else:sz=st.st_size;kind='file'
    cat='git_objects_and_metadata' if label=='shared-git-common' else category(rel)
    state='tracked' if rel in tracked else ('ignored' if rel in ignored else ('untracked' if rel in untracked else 'external_or_runtime'))
    key=(st.st_dev,st.st_ino);prior=inode_seen.get(key);inode_seen.setdefault(key,str(p))
    row={'scope':label,'root':str(base),'path':str(p),'relative_path':rel,'category':cat,'git_state':state,'kind':kind,'bytes':sz,'allocated_bytes':st.st_blocks*512,'device':st.st_dev,'inode':st.st_ino,'link_count':st.st_nlink,'same_inode_as':prior or ''}
    allrows.append(row);subtotal['files']+=1;subtotal['bytes']+=sz;subtotal['allocated_bytes']+=st.st_blocks*512
    g=group_stats[(label,cat)];g['files']+=1;g['bytes']+=sz;g['allocated_bytes']+=st.st_blocks*512
    if not prior:g['hardlink_dedup_bytes']+=sz
    if len(g['examples'])<4:g['examples'].append(str(p))
   except Exception as e:errors.append({'path':str(p),'error':type(e).__name__})
  summaries.append({'scope':label,'path':str(base),**subtotal})
 csvout('files.csv',allrows);write('location_totals.json',summaries);csvout('location_totals.csv',summaries)
 cats=[{'scope':k[0],'category':k[1],**v,'readable_GiB':round(v['bytes']/1024**3,6),'logical_records':'NOT_INFERRED_FROM_FILE_COUNT','acceptance':'NOT_APPLICABLE_OR_REQUIRES_SCHEMA'} for k,v in group_stats.items()]
 csvout('data_categories.csv',cats);write('inventory_errors.json',errors)
 csvout('media_files.csv',[r for r in allrows if r['category'] in ['source_video','audio','transcripts_subtitles_archives','thumbnail_images','contact_sheets']])
 # Exact content identities for project evidence/code, not large media/cache/Git or secret values.
 hashtable={};hashrows=[]
 for row in allrows:
  if row['kind']!='file' or row['category'] in ['git_objects_and_metadata','runtime_cache_dependencies','private_configuration_metadata_only'] or row['bytes']>64*1024**2:continue
  p=Path(row['path'])
  if p.suffix in ['.pem','.key','.p12']:continue
  try:
   k=(row['device'],row['inode']);h=hashtable.setdefault(k,sha(p)) if k not in hashtable else hashtable[k]
   hashrows.append({'path':str(p),'scope':row['scope'],'category':row['category'],'bytes':row['bytes'],'sha256':h})
  except Exception as e:errors.append({'path':str(p),'hash_error':str(e)})
 csvout('file_hashes_bounded.csv',hashrows)
 groups=defaultdict(list)
 for x in hashrows:groups[(x['sha256'],x['bytes'])].append(x['path'])
 dup=[{'sha256':k[0],'bytes_each':k[1],'copies':len(v),'paths':v,'semantics':'identical bytes; not independent evidence; APFS physical sharing UNKNOWN'} for k,v in groups.items() if len(v)>1]
 csvout('identical_content_groups.csv',dup)
 write('disk_accounting.json',{'scopes':len(roots),'file_entries':len(allrows),'logical_bytes_sum':sum(r['bytes'] for r in allrows),'inode_dedup_logical_bytes':sum(r['bytes'] for r in allrows if not r['same_inode_as']),'allocated_blocks_sum':sum(r['allocated_bytes'] for r in allrows),'apfs_clone_extent_sharing':'UNKNOWN; st_blocks and logical sums are not a proof of distinct physical allocation','shared_git_counted_once':True,'nested_claude_worktree_excluded_from_parent':True,'external_audit_package_excluded':True,'hash_bound':'64 MiB; larger originals retained, exact registered hashes checked separately','duplicate_content_groups_bounded':len(dup)})
 print(json.dumps({'locations':summaries,'errors':len(errors),'bounded_identical_groups':len(dup)},indent=2))

if __name__=='__main__':
 assert category('a.inspect.ndjson')=='inspection_sidecars'
 assert category('thumb/a.jpg')=='thumbnail_images'
 main()
