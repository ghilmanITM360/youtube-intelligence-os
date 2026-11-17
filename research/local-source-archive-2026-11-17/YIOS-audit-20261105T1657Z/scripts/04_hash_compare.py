#!/usr/bin/python3 -I
# Exact-hash comparison of target manifests against the fresh index. Read-only; writes under raw/hash.
import csv,os,re,sys,json,collections
csv.field_size_limit(10**9)
H=os.path.expanduser('~');A=H+'/YIOS-audit-20261105T1657Z/raw/hash/'
idx={}
for l in open(A+'index.tsv',encoding='utf8',errors='surrogateescape'):
    p=l.rstrip('\n').split('\t')
    idx.setdefault(p[0],[]).append((int(p[1]),p[3]))
print('index unique hashes',len(idx))
C=H+'/YIOS-Archive/recovery/YIOS-coverage-audit-20261026T220542Z/'
RX=re.compile(r'\b[0-9a-f]{64}\b')
rows=[]
def add(src,sha,size,path,cls):
    rows.append((src,sha,size,path,cls))
for r in csv.DictReader(open(C+'MACHINE_B_MANIFEST_SOURCE_IDENTITIES.csv')):
    la=r.get('logical_asset_id') or ''
    m=RX.findall(r.get('sha256') or '') or (RX.findall(la) if la.startswith('sha256:') else [])
    add('machine_b_manifest_source_identities',m[0] if m else '',r.get('bytes'),r.get('path'),r.get('category'))
for r in csv.DictReader(open(C+'MISSING_CRITICAL_ASSETS.csv')):
    la=r.get('logical_asset_id') or ''
    m=RX.findall((r.get('machine_a_sha256') or '')+' '+(r.get('recorded_source_sha256') or '')+' '+(la if la.startswith('sha256:') else ''))
    add('missing_critical_'+r['local_machine_a_presence'],m[0] if m else '',r.get('machine_a_size') or r.get('machine_b_size'),r.get('absolute_path'),r.get('classification'))
pr=H+'/Documents/yios-private-backups/machine-a-2026-10-20/machine-b-media-master-pr41.csv'
if os.path.exists(pr):
    for r in csv.DictReader(open(pr)):
        m=RX.findall(' '.join(str(v) for v in r.values()))
        add('machine_b_media_master_pr41',m[0] if m else '',r.get('bytes') or r.get('size') or r.get('size_bytes'),r.get('path') or r.get('relative_path') or r.get('filename'),'media')
w=csv.writer(open(A+'target_comparison.csv','w'));w.writerow('source sha256 size recorded_path class verdict found_count first_found_path'.split())
s=collections.Counter();u=collections.defaultdict(set)
for src,sha,size,path,cls in rows:
    if not sha: v='NO_HASH_IN_MANIFEST';f=[]
    else:
        f=idx.get(sha,[]);v='HASH_VERIFIED_HERE' if f else ('NOT_FOUND_RECORDED_PATH_EXISTS' if path and os.path.lexists(path) else 'NOT_FOUND_IN_INDEXED_SCOPE')
    s[(src,v)]+=1;u[(src,v)].add(sha)
    w.writerow([src,sha,size,path,cls,v,len(f),f[0][1] if f else ''])
for k in sorted(s):print(k[0],k[1],'rows',s[k],'unique',len(u[k]))
