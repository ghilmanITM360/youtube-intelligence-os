import pathlib,csv,json,collections
O=pathlib.Path(__file__).parent;rows=list(csv.DictReader((O/'EXPORT_IDENTITY_REGISTRY_COMPARISON.csv').open()));wanted={int(r['first_line']) for r in rows};mapping={};cross={r['source_id']:r for r in csv.DictReader((O/'EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv').open())}
with open('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21/ALL_RESEARCH_FINDINGS.jsonl') as f:
 for i,line in enumerate(f,1):
  if i in wanted:x=json.loads(line);mapping[i]=cross[x['source_id']]
for r in rows:
 s=mapping[int(r['first_line'])];r['first_source_id']=s['source_id'];r['first_source_sha256']=s['source_sha256'];r['first_source_published_github']=s['published_github'];r['published_ref']=s['remote_ref'];r['published_commit']=s['remote_commit'];r['published_blob']=s['git_blob'];r['first_source_local_yios']=s['local_yios']
with (O/'EXPORT_IDENTITY_REGISTRY_COMPARISON.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
st={t:dict(collections.Counter(r['first_source_published_github'] for r in rows if r['type']==t and r['in_current_registry']=='NO')) for t in ['video','channel']};(O/'evidence/registry_absence_vs_publication.json').write_text(json.dumps(st,indent=2));print(st)
