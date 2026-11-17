#!/usr/bin/python3 -I
# Git blob id for each indexed local file, compared to all blobs in the independent mirror. Reads only.
import hashlib,os,subprocess as sp,collections,csv
H=os.path.expanduser('~');A=H+'/YIOS-audit-20261105T1657Z/';M=A+'scratch/remote_mirror.git'
p=sp.Popen(['git','-C',M,'cat-file','--batch-check=%(objecttype) %(objectname)','--batch-all-objects','--unordered'],stdout=sp.PIPE,text=True)
bl={l.split()[1] for l in p.stdout if l.startswith('blob')};print('mirror blobs',len(bl))
lfs=set()
if os.path.exists(A+'raw/lfs/oids.txt'): lfs={l.strip() for l in open(A+'raw/lfs/oids.txt')}
c=collections.Counter();by=collections.Counter()
w=csv.writer(open(A+'raw/blob/local_vs_remote.csv','w'));w.writerow(['sha256','size','blob_sha1','in_mirror','path'])
for l in open(A+'raw/hash/index.tsv',encoding='utf8',errors='surrogateescape'):
    s,z,m,f=l.rstrip('\n').split('\t',3);z=int(z)
    if s in lfs: v='LFS_OID';b=''
    else:
        h=hashlib.sha1(b'blob %d\0'%z)
        try:
            with open(f,'rb') as fh:
                while True:
                    d=fh.read(1<<20)
                    if not d:break
                    h.update(d)
        except OSError: c['read_error']+=1;continue
        b=h.hexdigest();v='BLOB' if b in bl else 'ABSENT'
    c[v]+=1;r=f.replace(H+'/','').split('/');k='/'.join(r[:2]);by[(k,v)]+=z
    w.writerow([s,z,b,v,f.encode('utf8','surrogateescape').decode('utf8','replace')])
print(c)
for k,v in sorted(by.items()):print(k[0],k[1],v)
