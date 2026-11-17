# Read-only: any file in authorized YIOS roots whose count of distinct SHA-256 tokens (or rows) is near 5,767.
import os,re,csv,sys
rx=re.compile(rb'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])')
roots=['~/YIOS-Archive','~/Documents/yios-private-backups','~/yios-git-recovery','~/workprojects/yios-recovery-status','~/YIOS-local-audits','~/finance-work-machine-a']
hits=[];n=0;skip=0;top=[]
for r in roots:
  for dp,dn,fn in os.walk(os.path.expanduser(r)):
    dn[:]=[d for d in dn if d not in('node_modules','.venv','venv','.git','visual-ct-scan-venv','__pycache__')]
    for f in fn:
      if not f.lower().endswith(('.csv','.tsv','.txt','.jsonl','.json','.md','.sha256')) and 'SHA256' not in f.upper(): continue
      p=os.path.join(dp,f)
      try:
        s=os.stat(p)
        if s.st_flags&0x40000000 or s.st_size>200_000_000: skip+=1;continue
        b=open(p,'rb').read()
      except Exception: skip+=1;continue
      n+=1
      u=len(set(rx.findall(b)));l=b.count(b'\n')
      if 5500<=u<=6100 or 5760<=l<=5775: hits.append((u,l,s.st_size,p))
      if u>=1000: top.append((u,l,s.st_size,p))
print('files_scanned',n,'skipped',skip)
print('NEAR'); [print(*h,sep='\t') for h in sorted(hits)]
print('TOP unique sha sets >=1000'); [print(*h,sep='\t') for h in sorted(top,reverse=True)[:50]]
