# Reconstruct, from published Git manifests only, the set of hashes CT/forensic evidence depends on, and compare with local disk and mirror.
import subprocess,os,re,csv,collections,json
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');M=A+'/scratch/remote_mirror.git';env=dict(os.environ,GIT_NO_LAZY_FETCH='1')
g=lambda *a:subprocess.run(['git','-C',M,*a],capture_output=True,env=env).stdout
pat=re.compile(r'(EVIDENCE_SHA256SUMS|EXTERNAL_EVIDENCE_MANIFEST|PORTABLE_MANIFEST|SHA256SUMS|MANIFEST_SHA256|FILE_CHECKSUMS)',re.I)
rx=re.compile(rb'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])')
refs=sorted(set(g('for-each-ref','--format=%(objectname)','refs/heads').decode().split()))
seen={};scope=collections.defaultdict(set)
for r in refs:
  for l in g('ls-tree','-r',r).decode(errors='replace').splitlines():
    meta,p=l.split('\t',1);b=meta.split()[2]
    if pat.search(os.path.basename(p)) and b not in seen and 'portable-recovery' not in p:
      seen[b]=p
      d=g('cat-file','blob',b)
      if d.startswith(b'version https://git-lfs') or len(d)>40_000_000:continue
      for h in set(rx.findall(d)):
        scope[h.decode()].add(p)
print('manifest blobs',len(seen),'distinct hashes',len(scope))
mir=set(l.split('\t')[0] for l in open(A+'/raw/hash/mirror_blob_sha256.tsv',errors='replace'))
idx=set(l.split('\t')[0] for l in open(A+'/raw/hash/index.tsv',errors='replace'))
c=collections.Counter();vid=collections.defaultdict(collections.Counter)
w=csv.writer(open(A+'/raw/5767/published_manifest_hash_comparison.csv','w',newline=''));w.writerow(['sha256','on_machine_a_disk','in_remote_mirror','n_manifests','first_manifest'])
rv=re.compile(r'/([A-Za-z0-9_-]{11})/')
for h,ps in sorted(scope.items()):
  k=('L' if h in idx else '-')+('R' if h in mir else '-');c[k]+=1
  fp=sorted(ps)[0];w.writerow([h,int(h in idx),int(h in mir),len(ps),fp])
  m=rv.search(fp);vid[m.group(1) if m else os.path.dirname(fp)[:50]][k]+=1
print('L=disk R=remote',c)
for v,x in sorted(vid.items(),key=lambda kv:-sum(kv[1].values()))[:25]:print(v,dict(x))
