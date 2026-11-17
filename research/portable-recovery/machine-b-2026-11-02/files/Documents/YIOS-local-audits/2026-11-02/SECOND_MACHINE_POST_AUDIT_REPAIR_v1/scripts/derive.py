from audit import *
from data_audit import blob
from inventory import category
def main():
 matrix=read('branch_matrix.json');files=list(csv.DictReader((OUT/'files.csv').open()));locations=read('location_totals.json');hashes=list(csv.DictReader((OUT/'file_hashes_bounded.csv').open()));hashby={r['path']:r for r in hashes};wts=[]
 for i,d in enumerate(read('before/checkouts.json')):
  after=next(x for x in read('after/checkouts.json') if x['path']==d['path']);loc=next(x for x in locations if x['path']==d['path']);other=[x for x in read('before/checkouts.json') if x['path']!=d['path']]
  same=[x['path'] for x in other if x['head']==d['head']]
  wts.append({**after,'clone_kind':'PRIMARY_CHECKOUT_SHARED_GIT_COMMON' if d['path']==str(ROOT) else 'LINKED_WORKTREE','disk_before':loc,'ignored_paths_before':len(d['ignored']),'untracked_paths_before':len(d['untracked']),'unpublished_head_commits':d['local_only_commits'],'same_head_other_locations':same,'role':'Primary Finance checkout and local evidence/runtime' if d['path']==str(ROOT) else ('Coordination implementation/testing worktree' if 'dual-machine' in d['path'] else 'Finance Claude writer-assigned worktree'),'needed_assessment':'KEEP_CANONICAL_AND_LOCAL_DEPENDENCIES' if d['path']==str(ROOT) else ('KEEP_DISTINCT_TOOLING_ROLE_SECOND_MAC_ACCEPTANCE_PENDING' if 'dual-machine' in d['path'] else 'LOGICAL_CHECKOUT_DUPLICATE_AT_SAME_HEAD_BUT_WRITER_ASSIGNMENT_UNKNOWN_KEEP'),'active_process_evidence':'No separate local YIOS research writer identified in ps/app snapshots; audit is active; other clients not excluded.','writer_locks':'No Git operation/index locks; uv.lock is dependency metadata; production distributed lease not established.','media_dependency':'Private Documents/YIOS-Media-Library; frozen catalog/ZIP sources in primary checkout. Full external CT frame/audio sets mostly missing.','physical_disk_duplication':'Logical copied files exist; no identical inode sharing detected in census; APFS clone extent sharing UNKNOWN. Shared Git common counted once.'})
 write('worktree_clone_inventory.json',wts);csvout('worktree_clone_inventory.csv',wts)
 areas=[];lfs={}
 for r in matrix:
  if r['kind']!='remote':continue
  counts=defaultdict(lambda:Counter());uniques=defaultdict(set)
  for t in csv.DictReader((OUT/r['tree_index']).open()):
   area='/'.join(t['path'].split('/')[:2]) if '/' in t['path'] else '(root)';cat=category(t['path']);key=(area,cat);counts[key]['files']+=1;counts[key]['git_blob_bytes']+=int(t['git_blob_bytes']);uniques[key].add(t['blob'])
   if int(t['git_blob_bytes'])<250 and t['path'].endswith(('.db','.mp4','.wav','.zip','.xlsx','.npy')):
    raw=blob(t['blob'])
    if raw.startswith(b'version https://git-lfs.github.com/spec/v1'):
     s=raw.decode();oid=re.search(r'oid sha256:([a-f0-9]+)',s)[1];size=int(re.search(r'size (\d+)',s)[1]);d=lfs.setdefault(oid,{'oid':oid,'expected_bytes':size,'paths':set(),'refs':set()});d['paths'].add(t['path']);d['refs'].add(r['ref'])
  for key,c in counts.items():areas.append({'ref':r['ref'],'sha':r['sha'],'area':key[0],'category':key[1],**c,'unique_git_blobs_in_category':len(uniques[key]),'availability':'Git bytes locally fetched; LFS/external media requires independent presence check; table is not physical disk usage.'})
 csvout('branch_data_areas.csv',areas)
 lr=[]
 for oid,d in lfs.items():
  obj=ROOT/'.git/lfs/objects'/oid[:2]/oid[2:4]/oid;local=[]
  for rel in d['paths']:
   p=ROOT/rel
   if p.is_file() and p.stat().st_size==d['expected_bytes'] and sha(p)==oid:local.append(str(p))
  d.update({'paths':sorted(d['paths']),'refs':sorted(d['refs']),'local_materialized_matches':local,'local_lfs_object_exists':obj.is_file(),'local_lfs_object_bytes':obj.stat().st_size if obj.is_file() else None,'presence':'MATERIALIZED_HASH_MATCH' if local else ('OBJECT_STORE_PRESENT_NOT_MATERIALIZED' if obj.is_file() else 'POINTER_ONLY_UNAVAILABLE_HERE')});lr.append(d)
 csvout('lfs_presence.csv',lr)
 # Category inventories with exact local unique content, separate from logical research IDs.
 grouped=defaultdict(list)
 for r in files:
  if r['scope']=='checkout-1':grouped[r['category']].append(r)
 metrics=[]
 for cat,rr in grouped.items():
  hh=[hashby[x['path']]['sha256'] for x in rr if x['path'] in hashby]
  metrics.append({'category':cat,'checkout':'PRIMARY_BEFORE_CLEANUP','file_count':len(rr),'actual_logical_bytes':sum(int(x['bytes']) for x in rr),'allocated_blocks_bytes':sum(int(x['allocated_bytes']) for x in rr),'unique_content_hashes_bounded':len(set(hh)),'hashed_files_bounded':len(hh),'duplicate_file_copies_bounded':len(hh)-len(set(hh)),'unique_logical_research_records':'SEE_TYPED_POPULATIONS_NOT_FILE_COUNT','accepted_partial_blocked_pending':'Only meaningful for typed research populations; see population_counts.csv','examples':[x['path'] for x in rr[:3]]})
 csvout('primary_data_inventory.csv',metrics)
 c=read('finance/canonical-summary.json');a=read('finance/machine-a-published-summary.json');pop=[]
 for d,label in [(c,'Canonical Finance PR36'),(a,'Separate published Machine A Finance')]:
  ss=d['dispositions_original'];pop.append({'population':label,'ref':d['ref'],'logical_video_ids':1612,'channel_identities':42,'channels_with_videos':27,'accepted_limited':ss['ACCEPTED_LIMITED'],'accepted_full_evidence':0,'partial':ss['PARTIAL'],'blocked':ss['BLOCKED'],'pending':ss['PENDING']+646,'method':'Exclusive priority: complete > any blocked > authored partial > pending; 646 expansion records pending. Do not add these two versions together.'})
 pop += [{'population':'Canonical channel registry','logical_video_ids':2303,'channel_identities':75,'real_transcripts':2291,'placeholder_transcripts':12,'dataset_count':33,'accepted_limited':'NOT_AN_ACCEPTANCE_LEDGER','method':'Metadata/source registry; overlapping Finance/other research projections are not additional independent videos.'},
 {'population':'Portable CT001-005 packages','logical_video_ids':5,'accepted_visual_only':2,'partial':3,'full_av_accepted':0,'blocked':'ALL_HUMAN_AV_SIGNOFF','method':'Five source videos overlap older PR21 corpus; CT006 new local checkpoint not available for counting.'},
 {'population':'Older Casually Finance PR21 selection','logical_video_ids':18,'structural_packages':16,'missing_selected_sources':2,'full_av_accepted':0,'method':'Historical published progress declarations, not16 complete independently certified reviews.'},
 {'population':'Casual Economics sampled forensic corpus','logical_video_ids':11,'structural_packages':11,'deep_forensic_complete':0,'full_av_accepted':0,'method':'Published STATUS.json distinguishes sampled/structural completion from deep/AV acceptance.'},
 {'population':'Private local media manifest','files':456,'video_files':454,'audio_files':2,'high_confidence_video_ids':389,'unresolved_file_mappings':67,'hash_matches':456,'actual_bytes':4363111708,'method':'Files are not necessarily one unique video per file; reuse exact SHA/ID crosswalk.'},
 {'population':'Twelve-channel public metadata','logical_video_ids':445,'channel_identities':12,'method':'CSV/JSONL/per-channel projections overlap; metadata is not a forensic acceptance state.'},
 {'population':'MonkeyExplains1999 public metadata','logical_video_ids':76,'raw_records':121,'members_only_excluded':45,'method':'Finance selects63 of these into its expansion; do not count as63 additional independent records beyond1,612.'},
 {'population':'BarelyEvolved public metadata','logical_video_ids':4,'method':'Metadata-only snapshot; local media registry separately contains3 files.'}]
 csvout('population_counts.csv',pop);write('population_counts.json',pop)
 # Add concrete historical validation/checkpoint locations for every ref.
 decl=read('published_validation_declarations.json')
 for r in matrix:
  ref=r['ref'] if r['kind']=='remote' else ('refs/remotes/'+r['upstream'] if r['upstream'] else r['ref'])
  candidates=[]
  for d in decl:
   if ref not in d['refs']:continue
   if d['declarations']:candidates.append({'paths':d['paths'],'declarations':d['declarations']})
  r['published_checkpoint_declarations']=candidates
 write('branch_matrix.json',matrix);csvout('branch_matrix.csv',matrix)
 write('runtime_portability.json',{'python_project':run([str(ROOT/'.venv/bin/python'),'--version']),'available_modules':{n:bool(__import__('importlib.util',fromlist=['find_spec']).find_spec(n)) for n in ['numpy','PIL','openpyxl','pytest','whisper','scenedetect']},'binaries':run(['which','node','ffmpeg','ffprobe','uv','git-lfs']),'system_python_issue':'Homebrew python3=3.14.7 outside declared >=3.12,<3.14 range; importing plistlib/XML expat failed with missing _XML_SetAllocTrackerActivationThreshold. Project .venv Python3.12.14 passed actual checks. No environment install/repair performed.','services_not_tested':['Apify credentials/network acquisition','private Drive restore','Machine A filesystem/scheduler/session','native Excel recalculation','hosted CI execution (billing blocked)']})
 print('derived worktrees',len(wts),'branch category rows',len(areas),'LFS OIDs',len(lr),'typed populations',len(pop))
if __name__=='__main__':main()
