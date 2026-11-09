import pathlib,json,hashlib,sys,collections,base64
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');name=sys.argv[1] if len(sys.argv)>1 else 'narration_visual_review_01';agent_path=sys.argv[2] if len(sys.argv)>2 else '/root/narration_review_01';D=R/'agents'/name;expected=json.loads((D/'items.json').read_text());o=json.loads((D/f'OUT_{name}.json').read_text());by={x['asr_id']:x for x in expected};ids=[x['asr_id'] for x in o['items']];pending=o['pending_asr_ids'];assert len(ids)==len(set(ids)) and set(ids).isdisjoint(pending) and set(ids)|set(pending)==set(by);assert ids==[x['asr_id'] for x in expected if x['asr_id'] in set(ids)]
labels={'LITERAL','METAPHOR','DATA','CONTRAST','HUMOR','DECORATIVE','UNDETERMINED','POTENTIAL_MISMATCH'};reads={x['path']:x for x in o['evidence_reads']};reuse={x['path']:x for x in o.get('evidence_reused_from_prior',[])}
for x in o['items']:
 assert x['relation'] in labels and x['asr_text_status']=='UNCERTIFIED' and x['actual_listening'] is False
 assert x['description'].strip();given={y['path'] for y in by[x['asr_id']]['images']};assert set(x['evidence_paths'])<=given and set(x['evidence_paths'])<=set(reads)|set(reuse)
 assert set(x['sampled_source_frames'])<={y['frame'] for y in by[x['asr_id']]['images']}
for x in reads.values():assert hashlib.sha256(pathlib.Path(x['path']).read_bytes()).hexdigest()==x['sha256'] and x['successful'] and x['witness'].strip()
logs=[]
for p in pathlib.Path('/Users/ghilmankhan/.codex/sessions/2026/11').glob('*/*.jsonl'):
 with p.open() as f:meta=json.loads(f.readline())
 if meta.get('payload',{}).get('agent_path')==agent_path:logs.append(p)
assert len(logs)==1;actual=[]
for line in logs[0].open():
 d=json.loads(line);x=d.get('payload',{})
 if x.get('type')=='custom_tool_call_output' and isinstance(x.get('output'),list):
  for b in x['output']:
   if b.get('type')=='input_image':
    u=b['image_url'];u=u.get('url') if isinstance(u,dict) else u
    if u.startswith('data:'):actual.append({'call_id':x['call_id'],'sha256':hashlib.sha256(base64.b64decode(u.split(',',1)[1])).hexdigest()})
need=collections.Counter(x['sha256'] for x in reads.values());have=collections.Counter(x['sha256'] for x in actual);assert not need-have
summary={'scope_items':len(expected),'completed':len(ids),'pending':len(pending),'unique_successful_read_receipts':len(reads),'actual_image_blocks_in_agent_log':len(actual),'image_bytehash_multiplicity_match':'PASS','relations':dict(collections.Counter(x['relation'] for x in o['items'])),'ASR_status':'UNCERTIFIED_NOT_LISTENING','actual_listening_seconds':0,'out_of_interval_items':[x['asr_id'] for x in expected if any(not p['sample_within_ASR_interval'] for p in x['images'])],'actual_returns':actual};(R/f'session_20261103/{name}_validation.json').write_text(json.dumps(summary,indent=2));print({k:v for k,v in summary.items() if k!='actual_returns'})
