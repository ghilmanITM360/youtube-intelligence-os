import csv,os,collections,json
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z')
mir={};
for l in open(A+'/raw/hash/mirror_blob_sha256.tsv',errors='replace'):
    f=l.rstrip('\n').split('\t');mir.setdefault(f[0],(f[2],f[4]))
idx=collections.defaultdict(list)
for l in open(A+'/raw/hash/index.tsv',errors='replace'):
    f=l.rstrip('\n').split('\t')
    if len(f)>=4: idx[f[0]].append(f[3])
rows=list(csv.DictReader(open(A+'/raw/portable/LOCAL_EVIDENCE_INVENTORY.csv',newline='')))
res=[];c=collections.Counter();cat=collections.Counter();st=collections.Counter()
uniq=collections.defaultdict(list)
for r in rows:
    if r['sha256']:uniq[r['sha256']].append(r)
u=collections.Counter()
for h,rs in uniq.items():
    k=('LOCAL_DISK' if h in idx else '')+('+' if h in idx and h in mir else '')+('REMOTE_'+mir[h][0] if h in mir else '')
    k=k or 'NOT_HERE_NOT_IN_REMOTE'
    u[k]+=1
    for r in rs:
        cat[(r['category'],k)]+=1;st[(r['status'],k)]+=1
        res.append({**r,'machine_a_result':k,'local_first':idx[h][0] if h in idx else '','remote_first':mir[h][1] if h in mir else ''})
w=csv.DictWriter(open(A+'/raw/portable/inventory_vs_machine_a.csv','w',newline=''),fieldnames=res[0].keys());w.writeheader();w.writerows(res)
print('rows',len(rows),'no_hash',sum(1 for r in rows if not r['sha256']),'unique',len(uniq));print(u)
for k,v in sorted(cat.items()):print(k,v)
print();[print(k,v) for k,v in sorted(st.items())]
miss=[r for r in res if r['machine_a_result']=='NOT_HERE_NOT_IN_REMOTE']
print('missing bytes unique',sum(int(uniq[h][0]['bytes'] or 0) for h in uniq if h not in idx and h not in mir))
print('missing sample');[print(r['category'],r['bytes'],r['machine_b_path'][:110]) for r in sorted(miss,key=lambda r:-int(r['bytes'] or 0))[:25]]
# all prior target rows vs remote as well
T=list(csv.DictReader(open(A+'/raw/hash/target_comparison.csv',newline='')))
s=collections.Counter()
for r in T:
    h=r['sha256'].replace('sha256:','')
    s[(r['source'],'LOCAL' if h in idx else 'noLOCAL','REMOTE' if h in mir else 'noREMOTE')]+=1
[print(k,v) for k,v in sorted(s.items())]
