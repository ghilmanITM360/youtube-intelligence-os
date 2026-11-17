import os,csv,collections
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');H=os.path.expanduser('~')+'/'
mir={}
for l in open(A+'/raw/hash/mirror_blob_sha256.tsv',errors='replace'):
    f=l.rstrip('\n').split('\t');mir.setdefault(f[0],f[2])
rows=[l.rstrip('\n').split('\t') for l in open(A+'/raw/hash/index.tsv',errors='replace')]
def root(p):
    q=p.replace(H,'');s=q.split('/')
    if s[0]=='YIOS-local-audits': return '/'.join(s[:2])
    if s[0]=='YIOS-Archive': return '/'.join(s[:2])
    if s[0]=='Documents': return '/'.join(s[:2])
    if s[0]=='Downloads':return '/'.join(s[:3]) if s[1]=='videos in mp3' else '/'.join(s[:2])
    if s[0]=='workprojects':return '/'.join(s[:2])
    return s[0]
c=collections.defaultdict(lambda:[0,0,0,0,set(),set()])
allu={};uro=set();
for h,sz,_,p in (r[:4] for r in rows if len(r)>=4):
    sz=int(sz) if sz.isdigit() else 0;k=root(p);x=c[k]
    if h in mir: x[0]+=1;x[1]+=sz;x[4].add(h)
    else: x[2]+=1;x[3]+=sz;x[5].add(h)
    allu[h]=sz
w=csv.writer(open(A+'/raw/hash/local_classes_by_root.csv','w',newline=''));w.writerow('root files_in_remote bytes_in_remote files_not_in_remote bytes_not_in_remote unique_not_in_remote_hashes'.split())
for k,x in sorted(c.items(),key=lambda kv:-kv[1][3]):w.writerow([k,x[0],x[1],x[2],x[3],len(x[5])])
tot=sum(allu.values());lo=sum(s for h,s in allu.items() if h not in mir)
print('unique_hashes',len(allu),'logical_unique_bytes',tot,'unique_not_in_remote',sum(1 for h in allu if h not in mir),'bytes',lo)
for k,x in sorted(c.items(),key=lambda kv:-kv[1][3])[:26]:print(k,x[0],x[2],round(x[3]/1e6,1),'MB')
