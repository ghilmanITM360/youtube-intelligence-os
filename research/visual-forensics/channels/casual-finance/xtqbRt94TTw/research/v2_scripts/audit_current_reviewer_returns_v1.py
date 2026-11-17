import pathlib,json,hashlib,base64,sys,collections
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');batch=int(sys.argv[1]);name=f'gap_review_{batch:02}';o=json.loads((R/f'agents/{name}/OUT_{name}.json').read_text());logs=[]
for p in pathlib.Path('/Users/ghilmankhan/.codex/sessions/2026/11/03').glob('*.jsonl'):
 with p.open() as f:
  first=json.loads(f.readline())
 if first.get('type')=='session_meta' and first.get('payload',{}).get('agent_path')=='/root/'+name:logs.append(p)
assert len(logs)==1,logs;p=logs[0];images=[]
for l in p.open():
 d=json.loads(l);x=d.get('payload',{})
 if d.get('type')=='response_item' and x.get('type')=='custom_tool_call_output' and isinstance(x.get('output'),list):
  for b in x['output']:
   if b.get('type')=='input_image':
    u=b.get('image_url');u=u.get('url') if isinstance(u,dict) else u
    if isinstance(u,str) and u.startswith('data:'):images.append({'call_id':x['call_id'],'sha256':hashlib.sha256(base64.b64decode(u.split(',',1)[1])).hexdigest()})
returned=collections.Counter(x['sha256'] for x in images);expected=collections.Counter(x['sha256'] for x in o['evidence_reads'] if x.get('successful'));missing=expected-returned
assert not missing,dict(missing)
audit={'review':name,'rollout_log':str(p),'actual_image_blocks':len(images),'claimed_successful_reads':sum(expected.values()),'exact_bytehash_match_with_multiplicity':'PASS','method':'Actual image data URL bytehash from custom_tool_call_output input_image blocks, compared with saved image receipts; matching multiplicities required. Native means fullsize derivative actually returned, not all-frame native review.','native_vs_scaled':dict(collections.Counter(x['scale'] for x in o['evidence_reads'] if x.get('successful'))),'returns':images}
(R/f'session_20261103/{name}_tool_read_audit_v1.json').write_text(json.dumps(audit,indent=2));print(name,'PASS',len(images),'actualimageblocks',dict(audit['native_vs_scaled']))
