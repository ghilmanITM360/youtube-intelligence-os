# SHA-256 of every blob in the audit mirror (all refs incl. refreshed tips); LFS pointers recorded by OID.
import subprocess,hashlib,os,re
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');M=A+'/scratch/remote_mirror.git'
env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_OPTIONAL_LOCKS='0')
ids=subprocess.run(['git','-C',M,'rev-list','--objects','--all'],capture_output=True,text=True,env=env,errors='replace').stdout.splitlines()
first={}
for l in ids:
    s=l.split(' ',1)
    if len(s)==2 and s[0] not in first:first[s[0]]=s[1]
p=subprocess.Popen(['git','-C',M,'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,env=env)
out=open(A+'/raw/hash/mirror_blob_sha256.tsv','w');n=0
import threading
items=list(first)
def feed():
    for i in items:p.stdin.write((i+'\n').encode())
    p.stdin.close()
threading.Thread(target=feed).start()
rx=re.compile(rb'^version https://git-lfs[^\n]*\noid sha256:([0-9a-f]{64})\nsize (\d+)')
for i in items:
    h=p.stdout.readline().split()
    t=h[1];sz=int(h[2]);d=p.stdout.read(sz);p.stdout.read(1)
    if t!=b'blob':continue
    m=rx.match(d) if sz<300 else None
    if m: print(m[1].decode(),m[2].decode(),'LFS',i,first[i],sep='\t',file=out)
    else: print(hashlib.sha256(d).hexdigest(),sz,'BLOB',i,first[i],sep='\t',file=out)
    n+=1
print('blobs',n)
