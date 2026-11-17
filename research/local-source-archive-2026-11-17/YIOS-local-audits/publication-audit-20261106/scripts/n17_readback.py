# Independent N17 readback: GitHub API tree + blobs (not local object store) vs local files and the N17 seal.
import json,subprocess,hashlib,base64,sys,re
from pathlib import Path
S=Path(sys.argv[0]).parent; R='repos/ghilmanITM360/youtube-intelligence-os'; N17='bf6522a570995a01561348165855c25e0e727ffb'; P16='16bd0cc708b45ddb2e9b70873e37dfe9ffd786aa'
gh=lambda p:json.loads(subprocess.check_output(['gh','api',p]))
BE=Path.home()/'YIOS-local-audits/barely-evolved'; CS=BE/'channel_synthesis'
ROOT='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/'
t=gh(f'{R}/git/trees/{N17}?recursive=1'); assert not t['truncated']
tree={e['path']:e for e in t['tree'] if e['type']=='blob'}
t0=gh(f'{R}/git/trees/{P16}?recursive=1'); assert not t0['truncated']
prev={e['path']:e['sha'] for e in t0['tree'] if e['type']=='blob'}
changed=sorted(p for p,e in tree.items() if prev.get(p)!=e['sha'])
removed=sorted(set(prev)-set(tree))
print('N17 changed paths',len(changed),'removed',len(removed))
prepared=json.loads((CS/'evidence/N17_PREPARED.json').read_text())
print('matches PREPARED paths',sorted(prepared['paths'])==changed)
seal={}
for l in (CS/'EVIDENCE_SHA256SUMS_checkpoint_N17').read_text().splitlines():
    h,f=l.split(None,1); seal[Path(f).resolve()]=h
rows=[]
for p in changed:
    b=base64.b64decode(gh(f"{R}/git/blobs/{tree[p]['sha']}")['content']); sh=hashlib.sha256(b).hexdigest()
    loc=CS/p.split('/channel_synthesis/',1)[1]; lh=hashlib.sha256(loc.read_bytes()).hexdigest() if loc.exists() else None
    sealed=seal.get(loc.resolve())
    rows.append(dict(path=p.split('/channel_synthesis/',1)[1],remote_sha256=sh,bytes=len(b),local_equal=lh==sh,seal_equal=(sealed==sh) if sealed else None))
json.dump(rows,open(S/'n17_readback.json','w'),indent=1)
print('local mismatches',[r['path'] for r in rows if not r['local_equal']])
print('seal mismatches',[r['path'] for r in rows if r['seal_equal'] is False])
print('not in seal',[r['path'] for r in rows if r['seal_equal'] is None])
want=['DENSE_REVIEW_LEDGER','FINAL_AUDIT_MATRIX_v3','METHOD_CHANGE_LOG','NAC_HANDOFF_N17','FINAL_THREE_VIDEO_AUDIT_v3','M3_RULE_FREEZE','BLIND_RECONCILIATION_v3','ADDENDUM_N17','R20_VERIFY']
for w in want: print(w,[ (r['path'].split('/')[-1],r['remote_sha256'][:12],r['local_equal']) for r in rows if w in r['path']])
# whole-folder mapping, for all 4 BE folders
for vid,folder in [('uPQcyookL0Y','2026-11-02-uPQcyookL0Y-deep-ct-scan'),('mNLNb-Z4T0M','2026-11-03-mNLNb-Z4T0M-deep-ct-scan'),('GNaBxt_zIRA','2026-11-03-GNaBxt_zIRA-deep-ct-scan'),('channel_synthesis','channel_synthesis')]:
    pre=ROOT+vid+'/'; rf=[(p,e) for p,e in tree.items() if p.startswith(pre)]
    un=[];mm=[]
    for p,e in rf:
        l=BE/folder/p[len(pre):]
        if not l.exists(): un.append(p);continue
        d=l.read_bytes(); gs=hashlib.sha1(b'blob %d\0'%len(d)+d).hexdigest()
        if gs!=e['sha']: mm.append(p[len(pre):])
    print(vid,'remote',len(rf),'unmapped',un,'local-differs',mm)
other=sorted({p.split('/')[4] for p in tree if p.startswith(ROOT)})
print('BE subfolders on remote',other)
print('other paths under UCH59 not in folders',[p for p in tree if p.startswith(ROOT) and p.split('/')[4] not in('uPQcyookL0Y','mNLNb-Z4T0M','GNaBxt_zIRA','channel_synthesis')][:20])
