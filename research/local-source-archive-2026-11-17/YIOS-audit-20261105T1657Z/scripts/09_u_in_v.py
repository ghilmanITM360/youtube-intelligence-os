import subprocess,sys
R,M,U,V,names=sys.argv[1:6]
def b(repo,c,p):
    r=subprocess.run(['git','-C',repo,'rev-parse',f'{c}:{p}'],capture_output=True,text=True);return r.stdout.strip() if r.returncode==0 else None
same=diff=gone=0;rows=[]
for l in open(names):
    st,*ps=l.rstrip('\n').split('\t');p=ps[-1]
    bu=b(R,U,p);bv=b(M,V,p)
    k='SAME_IN_V' if bu==bv else ('ABSENT_IN_V' if bv is None else 'CHANGED_IN_V')
    if bu is None:k='DELETED_IN_U'
    rows.append((k,st,p,bu,bv))
from collections import Counter
print(Counter(r[0] for r in rows))
for r in rows:
    if r[0]!='SAME_IN_V':print(r)
