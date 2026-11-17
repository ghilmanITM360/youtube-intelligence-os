# Per-stream latest seal vs remote bytes (content-addressed via tree oid; direct blob read when local changed since seal).
import subprocess,hashlib,json,sys
from pathlib import Path
repo=str(Path.home()/'workprojects/youtube-intelligence-os');A=Path.home()/'YIOS-local-audits'
def tree(ref):return {l.split('\t')[1]:l.split()[2] for l in subprocess.check_output(['git','ls-tree','-r',ref],cwd=repo,text=True).splitlines()}
def gb(b):return hashlib.sha1(b'blob %d\0'%len(b)+b).hexdigest()
def check(name,ref,seal,prefix,base):
    T=tree(ref);ok=via=0;bad=[];nf=[]
    lines=Path(seal).read_text().splitlines()
    for l in lines:
        h,f=l.split(None,1);f=f.lstrip('*')
        rel=str(Path(f).relative_to(base)) if f.startswith('/') and Path(f).is_relative_to(base) else (None if f.startswith('/') else f.removeprefix('./'))
        rp=prefix+rel if rel else None
        if rp not in T:nf.append(f);continue
        lf=Path(base)/rel
        if lf.exists():
            b=lf.read_bytes()
            if hashlib.sha256(b).hexdigest()==h:
                if gb(b)==T[rp]:ok+=1
                else:bad.append(f)
                continue
        d=subprocess.run(['git','cat-file','blob',T[rp]],cwd=repo,capture_output=True).stdout;via+=1
        if hashlib.sha256(d).hexdigest()!=h:bad.append(f)
    print(f'{name}: entries {len(lines)} local+oid {ok} blob_read {via} not_on_remote {len(nf)} mismatch {len(bad)}',nf[:6],bad[:6])
    return {'name':name,'entries':len(lines),'ok':ok,'blob':via,'not_on_remote':nf,'mismatch':bad}
R=[];PE=A/'primitive-education';XK=A/'xkcd-whatif';EP=A/'Casual-Finance-Video006-EP0002-20261105T184819Z'
R.append(check('PE-I','origin/research/primitive-education-visual-forensics',PE/'campaign/EVIDENCE_SHA256SUMS_I.txt','research/visual-forensics/channels/UCsuQtyrMiUPdHUQ8WaqsFvQ/',PE))
R.append(check('XK-P','origin/research/xkcd-whatif-visual-forensics',XK/'campaign/EVIDENCE_SHA256SUMS_P.txt','research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/',XK))
pre='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/research/continuation_20261105_EP0002/'
s=sorted(EP.glob('EVIDENCE_SHA256SUMS*'),key=lambda p:p.stat().st_mtime);print('CF seals',[x.name for x in s][-3:])
if s:R.append(check('CF-W4','origin/research/casually-finance-editing-forensics',s[-1],pre,EP))
json.dump(R,open(Path(sys.argv[0]).parent/'seal_verify.json','w'),indent=1)
