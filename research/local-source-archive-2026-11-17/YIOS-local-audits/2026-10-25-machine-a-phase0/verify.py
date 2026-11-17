import os,json,csv,gzip,hashlib,re,collections
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');H=Path('/Users/ghilmankhan')
rows=list(csv.DictReader(gzip.open(O/'files.csv.gz','rt')))
by={x['path']:x for x in rows};cache={};read=0;BUDGET=1024**3;checks=[]
def h(p,large=False):
 global read
 p=Path(p);s=p.stat();k=str(p)
 if k in cache:return cache[k]
 if s.st_size>32*1024**2 and not large:return None
 if read+s.st_size>BUDGET:return None
 st=p.stat();sha=hashlib.sha256();git=hashlib.sha1();git.update(('blob '+str(s.st_size)+'\0').encode())
 with p.open('rb') as f:
  while True:
   b=f.read(1024**2)
   if not b:break
   sha.update(b);git.update(b)
 en=p.stat();read+=s.st_size
 cache[k]={'sha256':sha.hexdigest(),'git_blob_sha1':git.hexdigest(),'bytes':s.st_size,'stable_during_read':(st.st_mtime_ns,st.st_size,st.st_ino)==(en.st_mtime_ns,en.st_size,en.st_ino)}
 return cache[k]
def check(m,p,expected):
 p=Path(p)
 if 'offline-map' in str(p).lower():return
 status='MISSING';actual=None
 try:
  if p.is_file():
   v=h(p)
   if v:actual=v['sha256'];status='PASS' if actual==expected.lower() else 'MISMATCH'
   else:status='DEFERRED_SIZE_OR_BUDGET'
 except Exception as ex:status='ERROR:'+str(ex)
 checks.append({'manifest':str(m),'file':str(p),'expected':expected,'actual':actual,'status':status})
# Explicit current external manifests first.
for m in (R/'research/visual-forensics').rglob('EXTERNAL_EVIDENCE_MANIFEST.json'):
 j=json.loads(m.read_text());root=Path(j['external_root_machine_A'])
 for x in j['files']:check(m,root/x['path'],x['sha256'])
for root in [H/'workprojects/video data of what if/production_intelligence_brain',H/'workprojects/video data of what if/releases/production_intelligence_brain-v1.0.0']:
 m=root/'RELEASE_MANIFEST.json';j=json.loads(m.read_text())
 for x in j['files']:check(m,root/x['relative_path'],x['sha256'])
# Full validation of plain checksum manifests subject to one shared bounded read budget.
ms=[]
for x in rows:
 p=Path(x['path']);n=p.name.lower()
 if x['category'] in ['dependencies-cache','git-internals']:continue
 if 'sha256' in n or n.endswith('.sha256'):ms.append(p)
for m in sorted(ms,key=lambda p:(0 if 'NICK_170' in str(p) or 'checkpoint4' in p.name or 'install-candidate' in str(p) else 1,str(p))):
 try:txt=m.read_text()
 except (UnicodeError,OSError):continue
 for line in txt.splitlines():
  z=re.match(r'^([a-fA-F0-9]{64})\s+\*?(.+)$',line)
  if z:
   raw=z[2];p=Path(raw).expanduser()
   if not p.is_absolute():p=m.parent/p
   check(m,p,z[1])
# What If source media is 165MB total. No decoding.
for x in rows:
 if '/video data of what if/videos/' in x['path'] and x['extension']=='.mp4':h(x['path'],True)
# Three specific forensic source files referenced in portable manifests and partial handoff.
sources=[]
for m in (R/'research/visual-forensics').rglob('PORTABLE_MANIFEST.json'):
 j=json.loads(m.read_text());sources.append((m,Path(j['source_mp4']['historical_path_machine_A']),j['source_sha256']))
a=H/'YIOS-local-audits/2026-10-24-5umJ63d3rzQ-deep-ct-scan'
sources.append((a/'CONTINUATION_HANDOFF.md',H/'Downloads/videos in mp3/CasuallyFinance/Brace For Impact. - Casual Finance (720p, h264).mp4','b07b2a4b55e2b83d717b8cb6e4ac7dcbb44726bf595356d0288617183cfa5bc5'))
for m,p,e in sources:check(m,p,e)
# Installed skill + candidate + Git snapshot.
skills=[H/'.claude/skills/visual-ct-scan',R/'.claude/skills/visual-ct-scan',R/'research/visual-forensics/methodology/visual-ct-scan-skill-snapshot',H/'workprojects/yios-visual-forensics-install-candidate-2026-10-24/repo-overlay/.claude/skills/visual-ct-scan']
skillsets={str(root):{str(p.relative_to(root)):h(p) for p in root.rglob('*') if p.is_file() and not p.is_symlink()} if root.exists() else None for root in skills}
(O/'skill-comparison.json').write_text(json.dumps(skillsets,indent=2))
# Hash bounded meaningful small files, prioritize size collisions across folder trees.
sizes=collections.Counter(int(x['bytes']) for x in rows if x['category'] not in ['dependencies-cache','git-internals'])
candidates=[x for x in rows if x['category'] not in ['dependencies-cache','git-internals','os-metadata'] and int(x['bytes'])<=8*1024**2]
candidates.sort(key=lambda x:(sizes[int(x['bytes'])]<2,0 if 'video data of what if' in x['root'] else 1,int(x['bytes'])))
for x in candidates:
 if read>=BUDGET:break
 h(x['path'])
(O/'hashes.json').write_text(json.dumps(cache,indent=2))
with (O/'manifest-checks.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(checks[0]));w.writeheader();w.writerows(checks)
groups=collections.defaultdict(list)
for p,x in cache.items():groups[x['sha256']].append(p)
dups=[{'sha256':sha,'bytes_each':cache[ps[0]]['bytes'],'paths':ps} for sha,ps in groups.items() if len(ps)>1]
(O/'duplicate-groups.json').write_text(json.dumps(dups,indent=2))
summary={str(m):dict(collections.Counter(x['status'] for x in checks if x['manifest']==str(m))) for m in sorted(set(x['manifest'] for x in checks))}
(O/'manifest-summary.json').write_text(json.dumps(summary,indent=2))
# Live remote tree content identity: native Git blob identity, no LFS materialization claims.
trees={}
for n in ['live_head_tree','live_main_tree']:
 j=json.loads((O/(n+'.txt')).read_text());assert not j.get('truncated');trees[n]=collections.defaultdict(list)
 for x in j['tree']:
  if x['type']=='blob':trees[n][x['sha']].append(x['path'])
publication=[]
for p,x in cache.items():
 if p not in by:continue
 publication.append({'path':p,'sha256':x['sha256'],'bytes':x['bytes'],'finance_live_paths':trees['live_head_tree'].get(x['git_blob_sha1'],[]),'main_live_paths':trees['live_main_tree'].get(x['git_blob_sha1'],[])})
(O/'publication-matches.json').write_text(json.dumps(publication,indent=2))
print(json.dumps({'read_bytes':read,'hashed_files':len(cache),'duplicate_groups':len(dups),'manifest_counts':dict(collections.Counter(x['status'] for x in checks)),'manifest_files':len(summary),'unstable_reads':sum(not x['stable_during_read'] for x in cache.values())},indent=2))
print('PRIORITY_MANIFESTS')
for m,v in summary.items():
 if any(z in m for z in ['EXTERNAL_EVIDENCE','RELEASE_MANIFEST','checkpoint4','NICK_170','install-candidate','CONTINUATION_HANDOFF.md']):print(m,v)
