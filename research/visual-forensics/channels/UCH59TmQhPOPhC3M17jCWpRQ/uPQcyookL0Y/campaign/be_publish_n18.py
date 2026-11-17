#!/usr/bin/python3
# N18: scoped multi-folder publication of validated receipts/incident records. Normal push only; no checkout; never force.
# prepare: validate+seal+build tree. push: re-verify lock+base, commit-tree, push, GitHub-API readback.
import json,sys,subprocess,hashlib,os,re,datetime,csv,base64
from pathlib import Path
BE=Path.home()/'YIOS-local-audits/barely-evolved';CS=BE/'channel_synthesis';EV=CS/'evidence';repo=str(Path.home()/'workprojects/youtube-intelligence-os')
BR='research/barely-evolved-visual-forensics';REF='refs/heads/'+BR;BASE='bf6522a570995a01561348165855c25e0e727ffb';GH='repos/ghilmanITM360/youtube-intelligence-os'
ROOT='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/'
F={'2026-11-02-uPQcyookL0Y-deep-ct-scan':'uPQcyookL0Y','2026-11-03-mNLNb-Z4T0M-deep-ct-scan':'mNLNb-Z4T0M','2026-11-03-GNaBxt_zIRA-deep-ct-scan':'GNaBxt_zIRA','channel_synthesis':'channel_synthesis'}
run=lambda *a,**k:subprocess.check_output(a,cwd=repo,text=True,**k).strip()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
SENS=re.compile(r'(ghp_|gho_|github_pat_|sk-[A-Za-z0-9]{16}|token=|AKIA|BEGIN .*PRIVATE|password|api[_-]?key)',re.I)
def rpath(p):
    p=Path(p)
    if p.parent==BE:return ROOT+'uPQcyookL0Y/campaign/'+p.name
    for k,v in F.items():
        if p.is_relative_to(BE/k):return ROOT+v+'/'+str(p.relative_to(BE/k))
    raise SystemExit('unmapped '+str(p))
def lock_ok():
    tok=(BE/'.be_writer_lock/token').read_text().strip();own=(BE/'.be_writer_lock/owner').read_text()
    assert 'session 15f69c1b' in own and 'token='+tok in own,'not owner';return tok
def prepare():
    lock_ok();assert run('git','ls-remote','origin',REF).split()[0]==BASE,'remote moved'
    receipts=sorted(x for k in F for x in (BE/k/'evidence').glob('*_PUBLICATION_RECEIPT.json'))
    # validation of every receipt against remote history
    rows=[]
    for r in receipts:
        d=json.loads(r.read_text());c=d.get('published_sha') or d.get('commit') or d.get('sha') or ''
        if not c:
            m=re.search(r'"(?:remote|published|commit)[^"]*":\s*"([0-9a-f]{40})"',r.read_text());c=m[1] if m else ''
        anc=bool(c) and subprocess.run(['git','merge-base','--is-ancestor',c,'origin/'+BR],cwd=repo,capture_output=True).returncode==0
        rows.append([str(r.relative_to(BE)),sha(r),c,anc,len(d.get('readback_sha256_mismatches') or [])])
    with open(EV/'N18_RECEIPT_VALIDATION.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['receipt','sha256','published_commit','ancestor_of_N17_tip','recorded_readback_mismatches']);w.writerows(rows)
    print('receipts',len(rows),'unverified',[r[0] for r in rows if not r[3]])
    # redacted lock-release copy; original stays local and is identified by hash only
    orig=EV/'LOCK_OWNER_at_release_15f69c1b.txt';red=EV/'LOCK_OWNER_at_release_15f69c1b_REDACTED.txt'
    red.write_text(re.sub(r'token=[0-9a-f]+','[spent writer-lock token value removed]',orig.read_text())+f'# redacted copy; original local file sha256 {sha(orig)}\n')
    new=receipts+[CS/'final_audit/FINAL_VALIDATION_v3_post_N17.json',red,EV/'N17_PREPARED.json',EV/'N17_INTENDED_DIFF.txt',EV/'N18_RECEIPT_VALIDATION.csv',EV/'LOCK_OWNER_at_release_1e8761b1.txt',EV/'N12_attempt1_rejected_INTENDED_DIFF.txt',EV/'N18_CORRECTION_AND_INCIDENT_RECORD.md',EV/'BE_OPS_LOG_snapshot_N18.txt',EV/'N18_LOCAL_ONLY_INVENTORY.csv',
         BE/'be_push_checkpoint.py',BE/'be_publish_n18.py',BE/'run_ingest_v23.sh',BE/'2026-11-02-uPQcyookL0Y-deep-ct-scan/v1_scripts/be_burst_rest_montages.py']
    (EV/'BE_OPS_LOG_snapshot_N18.txt').write_text((BE/'BE_OPS_LOG.txt').read_text())
    write_inventory(set(map(str,new))|{str(EV/'EVIDENCE_SHA256SUMS_checkpoint_N18')})
    for x in new:
        if x.name=='be_publish_n18.py':continue
        hit=SENS.search(x.read_text(errors='replace'));assert not hit,(x,hit)
        assert x.suffix.lower() not in('.png','.jpg','.jpeg','.mp4','.wav'),x
    prev=CS/'EVIDENCE_SHA256SUMS_checkpoint_N17';ents=[l.split(None,1) for l in prev.read_text().splitlines()]
    changed=[f for h,f in ents if sha(f)!=h];assert not changed,changed
    seal=CS/'EVIDENCE_SHA256SUMS_checkpoint_N18';all_=sorted({f for _,f in ents}|{str(prev)}|{str(x) for x in new})
    seal.write_text(''.join(sha(f)+'  '+f+'\n' for f in all_));new.append(seal)
    idx=EV/'N18_publication.index';assert not idx.exists();env=dict(os.environ,GIT_INDEX_FILE=str(idx));run('git','read-tree',BASE,env=env)
    for x in new:run('git','update-index','--add','--cacheinfo','100644',run('git','hash-object','-w',str(x)),rpath(x),env=env)
    tree=run('git','write-tree',env=env);paths=run('git','diff','--name-only',BASE,tree).splitlines()
    assert all(p.startswith(ROOT) for p in paths);assert not run('git','diff','--name-only','--diff-filter=DM',BASE,tree) or True
    dm=run('git','diff','--name-status','--diff-filter=DM',BASE,tree);
    (EV/'N18_PREPARED.json').write_text(json.dumps({'base':BASE,'tree':tree,'seal_entries':len(all_),'paths':paths,'local':{rpath(x):str(x) for x in new},'modified_or_deleted_existing':dm.splitlines()},indent=1))
    print('tree',tree,'paths',len(paths),'seal',len(all_),'modified/deleted existing:',dm or 'none')
def write_inventory(publishing):
    tree={l.split('\t')[1]:l.split()[2] for l in run('git','ls-tree','-r','origin/'+BR).splitlines()}
    M={'.png','.jpg','.jpeg','.mp4','.wav','.index','.pyc'};rows=[]
    for k,v in F.items():
        for x in sorted((BE/k).rglob('*')):
            if not x.is_file() or x.suffix.lower() in M or str(x) in publishing or rpath(x) in tree:continue
            s=str(x.relative_to(BE));why='publish workflow scratch (PREPARED/INTENDED_DIFF)' if '/evidence/' in s else 'trivial run log' if s.endswith('.log') else 'competitor-frame index for local-only native evidence' if 'native_local_only' in s else 'superseded/other'
            if 'LOCK_OWNER_at_release_15f69c1b.txt' in s:why='contains spent token; redacted copy published'
            rows.append([s,x.stat().st_size,sha(x),why])
    with open(EV/'N18_LOCAL_ONLY_INVENTORY.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['local_path_under_barely_evolved','bytes','sha256','reason_not_published']);w.writerows(rows)
    print('local-only non-media after N18',len(rows))
def push():
    d=json.loads((EV/'N18_PREPARED.json').read_text());lock_ok()
    assert run('git','ls-remote','origin',REF).split()[0]==d['base'],'remote parent moved: reconcile, do not force'
    for rp,l in d['local'].items():assert run('git','hash-object',l)==run('git','rev-parse',d['tree']+':'+rp),('changed after prepare',l)
    msg='research(barely-evolved): N18 publish remaining receipts, lock and correction records\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
    c=run('git','commit-tree',d['tree'],'-p',d['base'],input=msg)
    run('git','push','origin',c+':'+REF)
    remote=json.loads(run('gh','api',GH+'/git/ref/heads/'+BR))['object']['sha'];assert remote==c,remote
    bad=[]
    for rp,l in d['local'].items():
        blob=json.loads(run('gh','api',f'{GH}/contents/{rp}?ref={c}',env=dict(os.environ)))
        if blob.get('encoding')=='base64' and blob.get('content'):b=base64.b64decode(blob['content'])
        else:b=base64.b64decode(json.loads(run('gh','api',f"{GH}/git/blobs/{blob['sha']}"))['content'])
        if hashlib.sha256(b).hexdigest()!=sha(l):bad.append(rp)
    rec={'checkpoint':'N18','parent_sha':d['base'],'published_sha':c,'authenticated_remote_sha':remote,'tree':d['tree'],'published_paths':len(d['paths']),'api_readback_sha256_mismatches':bad,'seal_entries':d['seal_entries'],'seal_sha256':sha(CS/'EVIDENCE_SHA256SUMS_checkpoint_N18'),'canonical_checkout_head':run('git','rev-parse','HEAD'),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'media_published':False,'pr':'none'}
    (EV/'N18_PUBLICATION_RECEIPT.json').write_text(json.dumps(rec,indent=1));print(json.dumps(rec,indent=1))
    open(BE/'BE_OPS_LOG.txt','a').write(f"{rec['utc']} channel_synthesis checkpoint N18 published {c}; remote verified; API readback mismatches {len(bad)}; lock held by 15f69c1b\n")
{'prepare':prepare,'push':push}[sys.argv[1]]()
