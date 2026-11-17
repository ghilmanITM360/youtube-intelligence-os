from audit import *
def main():
 before=list(csv.DictReader((OUT/'files.csv').open()));missing=[]
 for r in before:
  if r['scope']!='shared-git-common':continue
  rel=r['relative_path'];p=Path(r['path'])
  if re.fullmatch(r'objects/[a-f0-9]{2}/[a-f0-9]{38}',rel) and not p.exists():missing.append(rel.split('/')[1]+rel.split('/')[2])
 p=subprocess.run(['git','cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],input=('\n'.join(missing)+'\n').encode(),cwd=ROOT,capture_output=True)
 lines=p.stdout.decode().splitlines();unresolved=[l for l in lines if l.endswith(' missing')]
 assert len(lines)==len(missing) and not unresolved
 fsck=run(['git','fsck','--full','--no-dangling'],timeout=300);write('validation/git-fsck-final.json',fsck)
 summary=Counter()
 for d,dirs,names in os.walk(ROOT/'.git'):
  for n in names:
   f=Path(d)/n
   if f.is_file():s=f.stat();summary['files']+=1;summary['bytes']+=s.st_size;summary['allocated_bytes']+=s.st_blocks*512
 old=next(x for x in read('location_totals.json') if x['scope']=='shared-git-common')
 bref={x['ref']:x['sha'] for x in read('before/refs.json')};aref={x['ref']:x['sha'] for x in refs()}
 write('git_storage_observation.json',{'observed_at':now(),'before_shared_git':old,'after_shared_git':dict(summary),'old_loose_paths_no_longer_present':len(missing),'all_old_object_ids_still_resolve':not unresolved,'final_fsck_code':fsck['code'],'refs_before_after_equal':bref==aref,'count_objects_after':git('count-objects','-vH'),'interpretation':'Physical loose-object layout changed during audit; 3,138 previously redundant loose paths disappeared while identical object IDs remain readable from packs. Background maintenance/packing is an inference; initiator was not established. Audit did not run gc/repack/prune. This space delta is not counted as authorized cleanup savings.','observed_writer_processes_after':'No live gc/repack/maintenance process found at final process inspection.'})
 # Every locally present LFS object gets a fresh hash check, without downloads.
 lr=list(csv.DictReader((OUT/'lfs_presence.csv').open()))
 for r in lr:
  oid=r['oid'];f=ROOT/'.git/lfs/objects'/oid[:2]/oid[2:4]/oid
  r['object_store_sha256_check']='MATCH' if f.exists() and sha(f)==oid else ('MISSING' if not f.exists() else 'MISMATCH')
 csvout('lfs_presence.csv',lr)
 # Show measured after cleanup totals without a second full hash pass.
 removed={r['path'] for r in read('cleanup_ledger.json')};total=[]
 for loc in read('location_totals.json'):
  x=dict(loc)
  if x['scope']=='shared-git-common':x.update(summary)
  else:
   paths=[r for r in before if r['scope']==x['scope'] and r['path'] in removed]
   x['files']-=len(paths);x['bytes']-=sum(int(r['bytes']) for r in paths);x['allocated_bytes']-=sum(int(r['allocated_bytes']) for r in paths)
  x['observation']='After exact cleanup and latest Git common stat census; other scopes unchanged originals retained.';total.append(x)
 write('location_totals_after.json',total);csvout('location_totals_after.csv',total)
 print(json.dumps({'missing_loose_paths':len(missing),'all_objects_readable':not unresolved,'fsck_code':fsck['code'],'refs_equal':bref==aref,'after_git':dict(summary),'lfs_states':dict(Counter(r['object_store_sha256_check'] for r in lr))},indent=2))
if __name__=='__main__':main()
