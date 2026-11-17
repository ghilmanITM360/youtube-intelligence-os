"""Reuse qualified historical native observations; no source redisplay."""
from pathlib import Path
import json,csv,hashlib,base64,collections
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261105'
idx=json.loads((S/'prior_native_fullframe_receipt_index_v1.json').read_text())['frame_receipts']
frames=[3809,3810,4244,4245,4269,4270,5447,5448,6770,6771,6829,6830]
selected=[]
for n in frames:
    x=next(z for z in idx[str(n)] if z['review_ref'] in ['agents/gap_review_01/OUT_gap_review_01.json','agents/gap_review_02/OUT_gap_review_02.json'])
    assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256']
    selected.append(dict(x,source_frame=n))
expected=collections.Counter(x['sha256'] for x in selected);actual=[];logs=[]
for p in (Path.home()/'.codex/sessions').rglob('*.jsonl'):
    try:
        with p.open() as f:meta=json.loads(next(f))
    except Exception:continue
    if meta.get('payload',{}).get('agent_path') not in ['/root/gap_review_01','/root/gap_review_02']:continue
    logs.append(str(p))
    for line in p.open():
        if 'input_image' not in line:continue
        row=json.loads(line);z=row.get('payload',{})
        if z.get('type')!='custom_tool_call_output' or not isinstance(z.get('output'),list):continue
        for b in z['output']:
            if b.get('type')!='input_image':continue
            u=b.get('image_url');u=u.get('url') if isinstance(u,dict) else u
            if not isinstance(u,str) or not u.startswith('data:'):continue
            h=hashlib.sha256(base64.b64decode(u.split(',',1)[1])).hexdigest()
            if h in expected:actual.append(dict(sha256=h,call_id=z['call_id'],timestamp=row['timestamp'],rollout=str(p)))
counts=collections.Counter(x['sha256'] for x in actual)
assert not expected-counts,dict(expected-counts)
cases=[]
for id,gap,agent,natives,cut,desc in [
 ('EP0109','G035','01',[3809,3810],3810,'Existing native3809/3810 verifies history chalkboard replaced by white. Arrow/disc build begins3811 and remaining entry remains sampled.'),
 ('EP0128','G037','01',[4244,4245,4269,4270],4270,'Existing native4244/4245 verifies fragmentation onset4245, not a shot cut. Existing native4269/4270 verifies later chart cut4270 within compound4245–4328. Pan/interior stays sampled.'),
 ('EP0159','G041','01',[5447,5448],5448,'Existing native5447/5448 verifies blank transition from Fed/percent scene. Subsequent biography and speech-page entry is sampled; no invented exact slide offset.'),
 ('EP0192','G051','02',[6770,6771,6829,6830],6830,'Existing native6770/6771 verifies banknote overlay on retained scene, not full composition cut6771. Existing native6829/6830 verifies later host/chalkboard cut6830; rain interior remains sampled.')]:
    ref=f'agents/gap_review_{agent}/OUT_gap_review_{agent}.json';o=json.loads((R/ref).read_text())
    identity_ref=ref
    identity=o.get('source_sha256')
    if identity is None:
        identity_ref=f'agents/gap_review_{agent}/native_decode_receipt.json'
        decode=json.loads((R/identity_ref).read_text());identity=decode['source_sha256']
        assert all(x['path'] in decode['saved_paths'] for x in selected if x['source_frame'] in natives)
    assert identity=='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66'
    raw=next(x for x in o['items'] if x['id']==gap)
    cases.append(dict(event_id=id,qualified_prior_review_ref=ref+'#'+gap,source_identity_ref=identity_ref,native_source_frames=natives,cut_onset_frame=cut,curated_description=desc,prior_observation=raw,
                      native_receipts=[x for x in selected if x['source_frame'] in natives],new_source_image_reads=0,qualification='Reused independent historical gap reviewer observations; root curates taxonomy/provenance, not a new blind/native semantic re-view'))
out=dict(status='FOUR_PARENT_COMPOUND_RULINGS_FROM_EXISTING_NATIVE_OBSERVATIONS',cases=cases,prior_native_receipts=selected,required_return_hash_multiplicities=dict(expected),actual_historical_matching_returns=actual,
         bytehash_and_required_multiplicity='PASS',source_frame_mapping='Saved qualified source_frame/path observations and original historical whole-review return audits; identical white-frame JPEG bytes can recur, so byte identity alone is not unique frame identity.',
         rollout_logs=logs,actual_new_image_reads=0,new_qualified_cut_inventory_entries=[3810,4270,5448],existing_inventory_cut_reused=6830,
         actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
p=S/'additional_native_cut_semantic_reuse_audit_v2.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('HISTORICAL_RETURN_REUSE_PASS12source-frame receipts,4compoundrulings,3newinventoryonsets,0newimages')
