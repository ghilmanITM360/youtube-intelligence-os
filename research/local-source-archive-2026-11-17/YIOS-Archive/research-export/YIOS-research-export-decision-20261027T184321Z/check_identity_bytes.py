import pathlib,csv,collections,subprocess,os,json
O=pathlib.Path(__file__).parent;rows=list(csv.DictReader((O/'EXPORT_IDENTITY_REGISTRY_COMPARISON.csv').open()));groups=collections.defaultdict(list)
for r in rows:
 if r['in_current_registry']=='NO' and r['published_blob']:groups[r['published_blob']].append(r)
env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_NO_REPLACE_OBJECTS='1',GIT_TERMINAL_PROMPT='0');proc=subprocess.Popen(['git','-c','remote.origin.promisor=false','cat-file','--batch'],cwd='/Users/ghilmankhan/workprojects/youtube-intelligence-os',env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE);total=0
for oid,rs in groups.items():
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();h=proc.stdout.readline().split();b=proc.stdout.read(int(h[2]));proc.stdout.read(1);total+=len(b)
 for r in rs:r['identity_in_published_blob_bytes']='YES' if r['identity'].encode() in b else 'NO'
proc.stdin.close();proc.wait()
for r in rows:r.setdefault('identity_in_published_blob_bytes','NOT_TESTED_ALREADY_IN_REGISTRY')
with (O/'EXPORT_IDENTITY_REGISTRY_COMPARISON.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
res=dict(blobs=len(groups),bytes_read=total,results={t:dict(collections.Counter(r['identity_in_published_blob_bytes'] for r in rows if r['type']==t and r['in_current_registry']=='NO')) for t in ['video','channel']},limitation='Exact identity string occurrence in source blob, not complete structured row semantic equivalence or completed research verification');(O/'evidence/published_identity_byte_proof.json').write_text(json.dumps(res,indent=2));print(res)
