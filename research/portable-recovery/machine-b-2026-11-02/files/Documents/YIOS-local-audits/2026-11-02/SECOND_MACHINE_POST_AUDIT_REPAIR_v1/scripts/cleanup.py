from audit import *
import gzip
def main():
 targets=[(ROOT/'.git/refs/.DS_Store','Unused local modification','Finder metadata in Git refs is not a valid Git reference; git fsck reports only badRefName/badRefContent for this exact file.'),
 (ROOT/'research/finance-economics-intelligence/FINANCE_966_VIDEO_INTELLIGENCE.xlsx.inspect.ndjson','Superseded scratch','Ignored workbook inspection export; source workbook retired; existing handoff identifies retired inspection sidecar; no script/document dependency and no open file user.'),
 (ROOT/'research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx.inspect.ndjson','Redundant generated output','Ignored workbook inspection export, not an acceptance ledger or source; current canonical workbook retained and independently checked; no script/document dependency and no open file user.')]
 ledger=[]
 assert read('RECOVERY_VERIFIED.json')['verified']
 # Preflight every target and recovery copy before the first deletion.
 for p,classification,reason in targets:
  assert p.is_file() and not p.is_symlink()
  if p.name!='.DS_Store':
   assert not git('ls-files','--error-unmatch',str(p.relative_to(ROOT)))
   dep=run(['git','grep','-l','-F',p.name,'--','scripts','research','docs','tests'])
   assert dep['code']==1,(p,dep)
   opened=run(['lsof','-nP',str(p)]);assert opened['code']==1 and not opened['stdout'],opened
   with p.open() as f:assert json.loads(next(f))['kind'] in ['workbook','workbook-overview','overview']
  digest=sha(p);st=p.stat();dst=OUT/'recovery/cleanup'/str(p.relative_to(ROOT))
  dst=Path(str(dst)+'.gz');dst.parent.mkdir(parents=True,exist_ok=True)
  with p.open('rb') as src,gzip.open(dst,'wb',compresslevel=9) as dest:shutil.copyfileobj(src,dest)
  with gzip.open(dst,'rb') as f:assert hashlib.sha256(f.read()).hexdigest()==digest
  ledger.append({'path':str(p),'classification':classification,'reason':reason,'action':'READY_TO_REMOVE','original_bytes':st.st_size,'original_allocated_bytes':st.st_blocks*512,'sha256':digest,'recovery':str(dst),'recovery_compressed_bytes':dst.stat().st_size,'recovery_verified':True})
 write('cleanup_ledger.json',ledger)
 for row in ledger:
  p=Path(row['path']);assert sha(p)==row['sha256'];p.unlink();assert not p.exists();row['action']='REMOVED_EXACT_FILE';row['at']=now();write('cleanup_ledger.json',ledger)
 csvout('cleanup_ledger.csv',ledger)
 write('cleanup_summary.json',{'removed_paths':len(ledger),'gross_logical_bytes_removed':sum(r['original_bytes'] for r in ledger),'recovery_compressed_bytes':sum(r['recovery_compressed_bytes'] for r in ledger),'net_logical_bytes_reclaimed_before_other_audit_outputs':sum(r['original_bytes']-r['recovery_compressed_bytes'] for r in ledger),'physical_free_space_delta':'NOT_ATTRIBUTABLE_ON_ACTIVE_APFS_VOLUME','raw_evidence_deleted':False,'tracked_research_changed':False})
 print(json.dumps(read('cleanup_summary.json'),indent=2))
 write('validation/git-fsck-after-cleanup.json',run(['git','fsck','--full','--no-dangling'],timeout=300))
if __name__=='__main__':main()
