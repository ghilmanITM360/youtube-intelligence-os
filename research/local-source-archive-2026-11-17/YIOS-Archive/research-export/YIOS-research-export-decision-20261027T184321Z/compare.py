import pathlib,json,csv,subprocess,hashlib,collections,os,sqlite3,re
O=pathlib.Path(__file__).parent;E=O/'evidence';repo=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');R=pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21')
os.environ['GIT_NO_LAZY_FETCH']='1'
os.environ['GIT_NO_REPLACE_OBJECTS']='1'
os.environ['GIT_TERMINAL_PROMPT']='0'
def git(*a):return subprocess.run(['git','-c','remote.origin.promisor=false',*a],cwd=repo,capture_output=True,timeout=15)
sources=json.loads((E/'embedded_source_index.json').read_text());paths={s['source_path'] for s in sources}
live=[l.split() for l in (E/'live_remote_heads.txt').read_text().splitlines()];trees={};fail=[];blob_candidates=collections.defaultdict(list)
refs=[('HEAD',git('rev-parse','HEAD').stdout.decode().strip(),False)]+[(r,h,True) for h,r in live]
for ref,commit,published in refs:
 if commit in trees:
  for p,oid in trees[commit].items():blob_candidates[p].append((oid,ref,commit,published))
  continue
 z=git('ls-tree','-rz',commit)
 if z.returncode:fail.append({'ref':ref,'commit':commit,'error':z.stderr.decode()[:400]});continue
 tree={}
 for line in z.stdout.split(b'\0'):
  if not line:continue
  meta,path=line.split(b'\t',1);mode,typ,oid=meta.decode().split();path=path.decode(errors='replace')
  if typ=='blob' and path in paths:tree[path]=oid;blob_candidates[path].append((oid,ref,commit,published))
 trees[commit]=tree
# Hash only candidate Git blobs, bounded 768 MB. Preserve read failures explicitly.
oids=set(o for vals in blob_candidates.values() for o,*_ in vals);proc=subprocess.Popen(['git','-c','remote.origin.promisor=false','cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],cwd=repo,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
data=proc.communicate(('\n'.join(oids)+'\n').encode())[0];sizes={}
for line in data.decode().splitlines():
 z=line.split()
 if len(z)==3 and z[1]=='blob':sizes[z[0]]=int(z[2])
hashes={};total=0;errors=[];proc=subprocess.Popen(['git','-c','remote.origin.promisor=false','cat-file','--batch'],cwd=repo,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for oid,size in sorted(sizes.items(),key=lambda z:z[1]):
 if size>25_000_000 or total+size>768_000_000:continue
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();header=proc.stdout.readline().split()
 if len(header)!=3:errors.append(oid);continue
 b=proc.stdout.read(int(header[2]));proc.stdout.read(1);hashes[oid]=hashlib.sha256(b).hexdigest();total+=len(b)
proc.stdin.close();proc.wait()
# Earlier complete local census is evidence, not fresh re-census. Confirm stat identity before reusing hash.
prior=list(csv.DictReader(open('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')));byhash=collections.defaultdict(list);prior_target={}
for r in prior:
 if r['root_directory']==str(R):prior_target[r['relative_path']]=r
 if r['machine_a_sha256']:byhash[r['machine_a_sha256']].append(r)
rows=[]
for s in sources:
 p=s['source_path'];sha=s['source_sha256'];cand=blob_candidates.get(p,[]);matches=[x for x in cand if hashes.get(x[0])==sha];published=[x for x in matches if x[3]];current=[x for x in matches if x[1]=='HEAD'];local=[]
 for r in byhash.get(sha,[]):
  ap=pathlib.Path(r['absolute_path'])
  if not str(ap).startswith(str(repo)+'/'):continue
  try:
   st=ap.lstat();stable=st.st_size==int(r['machine_a_size']) and abs(st.st_mtime_ns-int(r['mtime_ns']))<100
   if stable:local.append(str(ap))
  except OSError:pass
 status='EXACT MATCH' if matches or local else 'UNKNOWN'
 rec='ALREADY_IN_REPO_EXACT' if matches or local else 'NEEDS_FURTHER_VERIFICATION'
 rows.append(dict(source_id=s['source_id'],source_path=p,source_sha256=sha,export_records=s['records'],record_kinds=json.dumps(s['kinds']),local_yios='YES' if local or current else 'UNKNOWN',local_counterpart=';'.join(local[:3]),git_history='YES' if matches else 'UNKNOWN',published_github='YES' if published else 'UNKNOWN',git_blob=matches[0][0] if matches else '',git_ref=matches[0][1] if matches else '',git_commit=matches[0][2] if matches else '',remote_ref=published[0][1] if published else '',remote_commit=published[0][2] if published else '',comparison=status,primary_recommendation=rec,evidence='Full source SHA256 equals Git blob SHA256' if matches else 'Prior source SHA256 + current size/mtime identity, not fresh payload read' if local else 'No exact match within bounded available published trees; absence not proved',cleanup='DO_NOT_DELETE' if not published else 'UNKNOWN_PRESERVE'))
fields=list(rows[0]);
with (O/'EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(E/'git_tree_comparison.json').write_text(json.dumps(dict(live_branches=len(live),distinct_trees=len(trees),tree_failures=fail,candidate_blobs=len(oids),hashed_blobs=len(hashes),hashed_bytes=total,hash_errors=errors,counts={k:dict(collections.Counter(r[k] for r in rows)) for k in ['local_yios','git_history','published_github','comparison']},limits='Only source-path candidates in HEAD and locally available live published branch-tip trees; no all-history completeness claim; <=25MB per blob <=768MB total'),indent=2))
(E/'git_blob_sha256.json').write_text(json.dumps(hashes));print((E/'git_tree_comparison.json').read_text()[:3500])
