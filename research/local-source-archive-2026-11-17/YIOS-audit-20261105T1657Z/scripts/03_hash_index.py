#!/usr/bin/python3 -I
# Read-only SHA-256 index of YIOS roots. Never opens dataless files (would trigger iCloud download).
# Skips vendored dirs by name and records the skip. Per-file open/read is bounded by SIGALRM.
import os,hashlib,signal,sys,time,stat
H=os.path.expanduser('~'); OUT=H+'/YIOS-audit-20261105T1657Z/raw/hash/'
ROOTS=['YIOS-Archive','YIOS-local-audits','Documents/yios-private-backups','Documents/Codex','yios-git-recovery','workprojects/yios-recovery-status','finance-work-machine-a','Downloads/videos in mp3','Downloads/CasuallyFinance-Forensic-Research','workprojects/yio-cf-editing-forensics-local-evidence','workprojects/video data of what if','workprojects/dr rehan video','workprojects/youtube-intelligence-os','workprojects/yios-finance-machine-a','.codex/worktrees/finance-short-01']
SKIPD={'.git','node_modules','site-packages','__pycache__','.venv','visual-ct-scan-venv'}
SF_DATALESS=0x40000000
class TO(Exception):pass
def al(*a): raise TO()
signal.signal(signal.SIGALRM,al)
idx=open(OUT+'index.tsv','w'); skip=open(OUT+'skipped.tsv','w'); st=open(OUT+'status.txt','w')
print('start',time.strftime('%FT%TZ',time.gmtime()),file=st,flush=True)
n=b=0
for r in ROOTS:
    root=os.path.join(H,r)
    if not os.path.exists(root): print('ABSENT_ROOT',root,sep='\t',file=skip); continue
    for dp,dn,fn in os.walk(root):
        for d in list(dn):
            if d in SKIPD: print('SKIP_DIR',os.path.join(dp,d),sep='\t',file=skip); dn.remove(d)
        for f in fn:
            if f=='.DS_Store': continue
            p=os.path.join(dp,f)
            try:
                s=os.lstat(p)
                if not stat.S_ISREG(s.st_mode): print('NOT_REGULAR',p,sep='\t',file=skip); continue
                if s.st_flags&SF_DATALESS: print('DATALESS',s.st_size,p,sep='\t',file=skip); continue
                h=hashlib.sha256()
                signal.alarm(max(60,s.st_size//(20<<20)))
                with open(p,'rb') as fh:
                    while True:
                        c=fh.read(1<<20)
                        if not c: break
                        h.update(c)
                signal.alarm(0)
                print(h.hexdigest(),s.st_size,int(s.st_mtime),p,sep='\t',file=idx); n+=1; b+=s.st_size
            except TO: print('TIMEOUT',p,sep='\t',file=skip); skip.flush()
            except OSError as e: signal.alarm(0); print('ERR',e.errno,p,sep='\t',file=skip)
    print(r,n,b,time.strftime('%FT%TZ',time.gmtime()),file=st,flush=True)
print('done',n,b,time.strftime('%FT%TZ',time.gmtime()),file=st,flush=True)
