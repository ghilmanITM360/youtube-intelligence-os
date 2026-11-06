#!/usr/bin/python3
# N20: scoped text publication of N20 post-seal receipts and two older lock-release receipts. Normal push only; never force.
# prepare: scan+seal+build tree via external index. push: re-verify lock+base, commit-tree, push, GitHub-API readback.
import json,sys,subprocess,hashlib,os,re,datetime,csv,base64
from pathlib import Path
BE=Path.home()/'YIOS-local-audits/barely-evolved';CS=BE/'channel_synthesis';EV=CS/'evidence';N=CS/'nonaudio_completion';repo=str(Path.home()/'workprojects/youtube-intelligence-os')
BR='research/barely-evolved-visual-forensics';REF='refs/heads/'+BR;BASE='89537b883e89b0454c5d42792263e72df0544545';GH='repos/ghilmanITM360/youtube-intelligence-os'
ROOT='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/'
F={'2026-11-02-uPQcyookL0Y-deep-ct-scan':'uPQcyookL0Y','2026-11-03-mNLNb-Z4T0M-deep-ct-scan':'mNLNb-Z4T0M','2026-11-03-GNaBxt_zIRA-deep-ct-scan':'GNaBxt_zIRA','channel_synthesis':'channel_synthesis'}
run=lambda *a,**k:subprocess.check_output(a,cwd=repo,text=True,**k).strip()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
SENS=re.compile(r'(ghp_|gho_|github_pat_|sk-[A-Za-z0-9]{16}|token=|AKIA|BEGIN .*PRIVATE|password|api[_-]?key)',re.I)
MEDIA={'.png','.jpg','.jpeg','.mp4','.wav','.index','.pyc'}
def rpath(p):
    p=Path(p)
    if p.parent==BE:return ROOT+'uPQcyookL0Y/campaign/'+p.name
    for k,v in F.items():
        if p.is_relative_to(BE/k):return ROOT+v+'/'+str(p.relative_to(BE/k))
    raise SystemExit('unmapped '+str(p))
def lock_ok():
    tok=(BE/'.be_writer_lock/token').read_text().strip();own=(BE/'.be_writer_lock/owner').read_text()
    assert 'session 15f69c1b' in own and 'token='+tok in own,'not owner'
UP=BE/"2026-11-02-uPQcyookL0Y-deep-ct-scan/evidence"
NEW=[EV/"N19_PUBLICATION_RECEIPT.json",EV/"N19_PREPARED.json",CS/"final_audit/FINAL_VALIDATION_v3_post_N19.json",UP/"M_LOCK_RELEASED.json",UP/"N_LOCK_RELEASED.json",
 BE/"be_publish_n20.py",EV/"BE_OPS_LOG_snapshot_N20.txt",EV/"N20_LOCAL_ONLY_INVENTORY.csv"]
def inventory(publishing):
    tree={l.split('\t')[1] for l in run('git','ls-tree','-r','--name-only','--full-tree','origin/'+BR).splitlines() and [f'x\t{x}' for x in run('git','ls-tree','-r','--name-only','--full-tree','origin/'+BR).splitlines()]}
    rows=[]
    for k in F:
        for x in sorted((BE/k).rglob('*')):
            if not x.is_file() or x.suffix.lower() in MEDIA or str(x) in publishing or rpath(x) in tree:continue
            s=str(x.relative_to(BE));why='trivial run log' if s.endswith('.log') else 'competitor-frame index for local-only native evidence' if 'native_local_only' in s else 'publish workflow scratch (PREPARED/INTENDED_DIFF)' if '/evidence/' in s else 'superseded/other'
            if 'LOCK_OWNER_at_release_15f69c1b.txt' in s:why='contains spent token; redacted copy published'
            rows.append([s,x.stat().st_size,sha(x),why])
    with open(EV/'N20_LOCAL_ONLY_INVENTORY.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['local_path_under_barely_evolved','bytes','sha256','reason_not_published']);w.writerows(rows)
    print('local-only non-media after N20',len(rows))
def prepare():
    lock_ok();assert run('git','ls-remote','origin',REF).split()[0]==BASE,'remote moved'
    (EV/'BE_OPS_LOG_snapshot_N20.txt').write_text((BE/'BE_OPS_LOG.txt').read_text())
    seal=CS/'EVIDENCE_SHA256SUMS_checkpoint_N20';inventory({str(x) for x in NEW}|{str(seal),str(EV/'N20_PREPARED.json')})
    for x in NEW:
        if x.name!='be_publish_n20.py':
            hit=SENS.search(x.read_text(errors='replace'));assert not hit,(x,hit)
        assert x.suffix.lower() not in MEDIA,x
    prev=CS/'EVIDENCE_SHA256SUMS_checkpoint_N19';ents=[l.split(None,1) for l in prev.read_text().splitlines()]
    changed=[f for h,f in ents if sha(f)!=h];assert not changed,changed
    all_=sorted({f for _,f in ents}|{str(prev)}|{str(x) for x in NEW})
    seal.write_text(''.join(sha(f)+'  '+f+'\n' for f in all_));new=NEW+[seal]
    idx=EV/'N20_publication.index';idx.unlink(missing_ok=True);env=dict(os.environ,GIT_INDEX_FILE=str(idx));run('git','read-tree',BASE,env=env)
    for x in new:run('git','update-index','--add','--cacheinfo','100644',run('git','hash-object','-w',str(x)),rpath(x),env=env)
    tree=run('git','write-tree',env=env);paths=run('git','diff','--name-only',BASE,tree).splitlines()
    assert all(p.startswith(ROOT) for p in paths);dm=run('git','diff','--name-status','--diff-filter=DM',BASE,tree);assert not dm,dm
    (EV/'N20_PREPARED.json').write_text(json.dumps({'base':BASE,'tree':tree,'seal_entries':len(all_),'paths':paths,'local':{rpath(x):str(x) for x in new}},indent=1))
    print('tree',tree,'paths',len(paths),'seal',len(all_),'modified/deleted existing: none');print(run('git','diff','--stat',BASE,tree).splitlines()[-1])
def push():
    d=json.loads((EV/'N20_PREPARED.json').read_text());lock_ok()
    assert run('git','ls-remote','origin',REF).split()[0]==d['base'],'remote parent moved: reconcile, do not force'
    for rp,l in d['local'].items():assert run('git','hash-object',l)==run('git','rev-parse',d['tree']+':'+rp),('changed after prepare',l)
    msg='research(barely-evolved): N20 N20 receipts and lock-release records\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
    c=run('git','commit-tree',d['tree'],'-p',d['base'],input=msg);run('git','push','origin',c+':'+REF)
    remote=json.loads(run('gh','api',GH+'/git/ref/heads/'+BR))['object']['sha'];assert remote==c,remote
    bad=[]
    for rp,l in d['local'].items():
        blob=json.loads(run('gh','api',f'{GH}/contents/{rp}?ref={c}'))
        b=base64.b64decode(blob['content']) if blob.get('encoding')=='base64' and blob.get('content') else base64.b64decode(json.loads(run('gh','api',f"{GH}/git/blobs/{blob['sha']}"))['content'])
        if hashlib.sha256(b).hexdigest()!=sha(l):bad.append(rp)
    rec={'checkpoint':'N20','parent_sha':d['base'],'published_sha':c,'authenticated_remote_sha':remote,'tree':d['tree'],'published_paths':len(d['paths']),'api_readback_files':len(d['local']),'api_readback_sha256_mismatches':bad,'seal_entries':d['seal_entries'],'seal_sha256':sha(CS/'EVIDENCE_SHA256SUMS_checkpoint_N20'),'canonical_checkout_head':run('git','rev-parse','HEAD'),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'media_published':False,'pr':'none'}
    (EV/'N20_PUBLICATION_RECEIPT.json').write_text(json.dumps(rec,indent=1));print(json.dumps(rec,indent=1))
    open(BE/'BE_OPS_LOG.txt','a').write(f"{rec['utc']} channel_synthesis checkpoint N20 published {c}; remote verified; API readback mismatches {len(bad)}; lock held by 15f69c1b\n")
{'prepare':prepare,'push':push}[sys.argv[1]]()
