from audit import *
from data_audit import blob,tree
def main():
 st=read('before/stashes.json')[0];commit=st['sha'];entries=tree(commit+'^3')
 tip_blobs=set();tip_places=defaultdict(list)
 for r in read('branch_matrix.json'):
  if r['kind']!='remote':continue
  for t in csv.DictReader((OUT/r['tree_index']).open()):
   tip_blobs.add(t['blob']);tip_places[t['blob']].append(r['name']+':'+t['path'])
 hashes=defaultdict(list)
 for r in csv.DictReader((OUT/'file_hashes_bounded.csv').open()):hashes[r['sha256']].append(r['path'])
 items=[]
 for t in entries:
  h=hashlib.sha256(blob(t['blob'])).hexdigest();matches=sorted(set(hashes.get(h,[])))
  published=tip_places.get(t['blob'],[])
  items.append({**t,'sha256':h,'stash_object_locator':commit+'^3:'+t['path'],'present_in_remote_branch_tips':bool(published),'remote_examples':published[:5],'matching_local_files':matches,'classification':'Completed but unpublished work' if not published and not matches and t['path'].endswith(('.json','.jsonl','.csv','.md')) else ('Redundant generated output' if published else 'Unknown'),'action':'PRESERVE_STASH_NO_POP_NO_CLEAR','confidence_limit':'Byte matches establish redundancy only; research acceptance/ownership not inferred.'})
 csvout('stash_contents.csv',items)
 # Retain compact tracked delta, refs, object identities and source locations.
 # Full 843 MB untracked stash tree stays in original Git objects and external preservation folders.
 beforepatch=OUT/'before/stash-0.patch';old_bytes=beforepatch.stat().st_size;old_hash=sha(beforepatch)
 rr=run(['git','diff','--binary','--full-index',commit+'^1',commit],raw=True);tracked=OUT/'before/stash-0-tracked.patch';tracked.write_bytes(rr['stdout'])
 tmpindex=OUT/'recovery/stash-verification.index';tmpindex.parent.mkdir(parents=True,exist_ok=True)
 env={**os.environ,'GIT_INDEX_FILE':str(tmpindex),'GIT_OPTIONAL_LOCKS':'0'}
 rr1=subprocess.run(['git','read-tree',commit+'^1'],cwd=ROOT,env=env,capture_output=True)
 rr2=subprocess.run(['git','apply','--cached','--check',str(tracked)],cwd=ROOT,env=env,capture_output=True)
 assert rr1.returncode==rr2.returncode==0,(rr1.stderr,rr2.stderr)
 tmpindex.unlink(missing_ok=True)
 assert git('rev-parse','refs/stash')==commit
 beforepatch.unlink()
 st['patch']=str(tracked);st['untracked_tree']=git('rev-parse',commit+'^3^{tree}');st['untracked_inventory']='stash_contents.csv';st['large_untracked_content']='Retained in original Git common object store; no stash operation or garbage collection; external matching paths inventoried.'
 write('before/stashes.json',[st])
 write('stash_summary.json',{'sha':commit,'tracked_patch_apply_check':'PASS_USING_DISPOSABLE_INDEX','tracked_delta_paths':git('diff','--name-status',commit+'^1',commit),'untracked_files':len(items),'untracked_bytes':sum(r['bytes'] for r in items),'remote_byte_matches':sum(r['present_in_remote_branch_tips'] for r in items),'external_or_checkout_hash_matches':sum(bool(r['matching_local_files']) for r in items),'neither_remote_tip_nor_bounded_local_match':sum(not r['present_in_remote_branch_tips'] and not r['matching_local_files'] for r in items),'preserved':True,'checkpoint_compaction':{'removed_newly_generated_redundant_full_stash_patch_bytes':old_bytes,'old_patch_sha256':old_hash,'reason':'Avoid duplicating 843 MB of retained source/media; exact object identities, all path hashes, tracked patch and original stash ref suffice to recover unchanged stash. This is not owner-data cleanup and is not counted as owner space reclaimed.'}})
 manifest=[{'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in (OUT/'before').rglob('*') if p.is_file()]
 write('RECOVERY_MANIFEST.json',manifest);assert all(sha(OUT/r['path'])==r['sha256'] for r in manifest)
 write('RECOVERY_VERIFIED.json',{'at':now(),'verified':True,'files':len(manifest),'stash_tracked_patch_apply_check':'PASS','stash_ref_unchanged':True,'large_stash_tree_recovery':'Original Git common directory objects; exact locator and SHA256 of every untracked stash path in stash_contents.csv; originals deliberately not duplicated. No operation endangered these objects. This is a recovery checkpoint for the performed cleanup, not a full off-device repository backup.'})
 print(json.dumps(read('stash_summary.json'),indent=2))
if __name__=='__main__':main()
