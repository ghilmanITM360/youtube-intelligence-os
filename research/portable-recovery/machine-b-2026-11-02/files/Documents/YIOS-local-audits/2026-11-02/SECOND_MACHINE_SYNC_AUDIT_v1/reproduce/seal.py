from audit import *
def main():
 br=run(['gh','api','--paginate','--slurp','repos/ghilmanITM360/youtube-intelligence-os/branches?per_page=100']);assert br['code']==0
 live={x['name']:x['commit']['sha'] for page in json.loads(br['stdout']) for x in page};expected={r['name']:r['sha'] for r in read('branch_matrix.json') if r['kind']=='remote'}
 assert live==expected,'Remote heads changed; audit package requires a new observation appendix'
 pr=run(['gh','pr','view','36','--repo','ghilmanITM360/youtube-intelligence-os','--json','number,state,isDraft,headRefOid,baseRefName,headRefName,mergedAt,url']);assert pr['code']==0;d=json.loads(pr['stdout']);assert d['state']=='OPEN' and d['isDraft'] and d['headRefOid']==expected['research/finance-economics-intelligence'] and d['mergedAt'] is None
 write('after/seal-live-branches.json',br);write('after/seal-pr36.json',pr)
 checks=[]
 for t in read('before/checkouts.json'):
  p=Path(t['path']);assert git('rev-parse','HEAD',cwd=p)==t['head'];assert not git('status','--porcelain=v1','--untracked-files=all',cwd=p);checks.append({'path':str(p),'sha':t['head'],'clean':True})
 assert git('rev-parse','refs/stash')==read('stash_summary.json')['sha']
 seal={'sealed_at_utc':now(),'remote_branch_count':len(live),'all_remote_heads_equal_audited_shas':True,'pr36':'OPEN_DRAFT_UNMERGED_HEAD_UNCHANGED','checkouts':checks,'stash_unchanged':True,'package_qa':read('PACKAGE_QA.json'),'limitations':'Snapshot audit, not continuous monitoring. Machine A unpublished state remains unknown.'}
 write('FINAL_SEAL.json',seal)
 md=read('audit_metadata.json');md['sealed_at_utc']=seal['sealed_at_utc'];write('audit_metadata.json',md)
 for name in ['README.md','SYNC_REPORT.md']:
  p=OUT/name;p.write_text(p.read_text()+f"\nFinal authenticated seal: `{seal['sealed_at_utc']}`. All46remote branch heads still match the audited SHAs; PR36remainsOPEN/DRAFT/unmerged at the same SHA; all3checkouts remain clean and unchanged. See `FINAL_SEAL.json`.\n")
 shutil.copy2(Path('/private/tmp/yios-sync-audit-v1/seal.py'),OUT/'reproduce/seal.py')
 manifest=[{'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(OUT.rglob('*')) if p.is_file() and p.name not in ['PACKAGE_MANIFEST_SHA256.json','PACKAGE_MANIFEST_SHA256.json.sha256']]
 write('PACKAGE_MANIFEST_SHA256.json',manifest)
 assert all(sha(OUT/r['path'])==r['sha256'] for r in manifest)
 write('PACKAGE_MANIFEST_SHA256.json.sha256',sha(OUT/'PACKAGE_MANIFEST_SHA256.json')+'  PACKAGE_MANIFEST_SHA256.json\n')
 print(json.dumps({'output':str(OUT),'sealed_at':seal['sealed_at_utc'],'manifest_files':len(manifest),'manifested_bytes':sum(r['bytes'] for r in manifest),'all_hashes_verified':True},indent=2))
if __name__=='__main__':main()
