"""Actual emitted image bytes, exact order/multiplicity and request accounting."""
from pathlib import Path
import json,hashlib,base64,collections,sys,io
from PIL import Image
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
path=R/sys.argv[1];label=sys.argv[2];root_mode=len(sys.argv)>3 and sys.argv[3]=='ROOT';o=json.loads(path.read_text());m=json.loads((path.parent/'items.json').read_text())
req=m['new_view_requests'];reads=o['new_evidence_reads'];pending=o.get('pending_paths',o.get('pending_new_image_paths',[]))
assert o['source_sha256']==m['source_sha256'] and o['actual_listening_seconds']==0 and o['CT_SCAN_COMPLETE'] is False
assert len({x['path'] for x in reads})==len(reads)
assert not set(pending)&{x['path'] for x in reads}
assert set(pending)|{x['path'] for x in reads}=={x['path'] for x in req}
lookup={x['path']:x for x in req}
for x in reads:
    assert x['successful'] is True and 'NATIVE' in x['scale']
    assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256']==lookup[x['path']]['sha256']
hashes={x['sha256'] for x in req};actual=[];logs=[]
for p in (Path.home()/'.codex/sessions').rglob('*.jsonl'):
    try:
        with p.open() as f:meta=json.loads(next(f))
    except Exception:continue
    if root_mode:
        if meta.get('payload',{}).get('id')!='01a1a2b1-c283-75f3-b64f-f45a440501b1':continue
    elif meta.get('payload',{}).get('agent_path')!='/root/gap_review_03':continue
    logs.append(str(p))
    for line in p.open():
        if 'input_image' not in line:continue
        row=json.loads(line);z=row.get('payload',{})
        if row.get('timestamp','')<'2026-11-05T03:11:42' or z.get('type')!='custom_tool_call_output' or not isinstance(z.get('output'),list):continue
        for b in z['output']:
            if b.get('type')!='input_image':continue
            u=b.get('image_url');u=u.get('url') if isinstance(u,dict) else u
            if not isinstance(u,str) or not u.startswith('data:'):continue
            data=base64.b64decode(u.split(',',1)[1]);h=hashlib.sha256(data).hexdigest()
            if h in hashes:
                dims=list(Image.open(io.BytesIO(data)).size);assert dims==[1920,1080]
                actual.append(dict(call_id=z['call_id'],timestamp=row['timestamp'],sha256=h,dimensions=dims))
assert collections.Counter(x['sha256'] for x in actual)==collections.Counter(x['sha256'] for x in reads)
assert [x['sha256'] for x in actual]==[x['sha256'] for x in reads]
a=dict(saved_output=str(path.relative_to(R)),saved_output_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),rollout_logs=logs,
       requested_paths=len(req),claimed_actual_reads=len(reads),actual_native_fullframe_returns=len(actual),actual_scaled_returns=0,pending_paths=pending,
       request_accounting_and_actual_bytehash_order_multiplicity_dimensions='PASS',actual_returns=actual,
       scope='New successful tool displays, not automatically new unique source frames. Consult prior_native_fullframe_receipt_index/reuse audit before uniqueness claims. Domain-specific semantic/schema audit separately required.',
       actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
dest=R/'session_20261105'/(label+'_independent_return_audit_v1.json');assert not dest.exists();dest.write_text(json.dumps(a,indent=2)+'\n')
print('PASS',label,len(actual),'actualnative returns;',len(pending),'pending;uniqueness not inferred')
