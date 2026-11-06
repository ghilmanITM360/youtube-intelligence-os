from pathlib import Path
import json,csv,hashlib,subprocess,sys
from PIL import Image
import PIL
import numpy as np
P=Path(__file__).parent;B=P.parent/'Casual-Finance-Video006-native2-20261106';R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def get(n):return json.loads((P/n).read_text())
def save(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
req=get('CURRENT_REQUIREMENTS.json');a=list(csv.DictReader((B/'visual_event_ledger_v39.csv').open()));b=list(csv.DictReader((P/'visual_event_ledger_v43.csv').open()));assert len(a)==len(b)==948;assert [r['event_id']for r in a]==[r['event_id']for r in b];assert len({r['event_id']for r in b})==948
cat='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET';before=[r['event_id']for r in a if r['timing_precision']==cat];after=[r['event_id']for r in b if r['timing_precision']==cat];assert len(before)==572 and len(after)==562;assert set(before)-set(after)==set(req['resolved_row_ids']);assert not set(after)-set(before)
changed=[x['event_id']for x,y in zip(a,b)if x!=y];assert set(changed)==set(req['resolved_row_ids']+['EP0029','EP0032','G005.01','G006.01']),changed
q=get('CURRENT_NATIVE_QUEUE_v19.json');assert q['count']==562 and q['items']==[r for r in b if r['timing_precision']==cat]
o=get('OPEN_REQUIREMENTS.json');assert o['strict_candidate_only_rows']==562 and o['extended_spans_pending']==143;assert [r['event_id']for r in o['outside_category_unknown_full_timing']]==['SUB101','SUB151'];assert o['outside_category_unknown_full_timing']==json.loads((B/'OPEN_REQUIREMENTS.json').read_text())['outside_category_unknown_full_timing'];assert any('P3' in r['status']for r in o['additional_open_details']);assert any('cursor' in r['requirement']and r['status'].startswith('OPEN')for r in o['additional_open_details'])
c=get('EXTENDED_SPAN_CLASSIFICATION_v3.json');assert c['total_input']==151 and c['classified_new']==6 and c['classified_shared_parameterized']==2 and c['unassessed_not_closed']==143;assert sum(r['classification']=='UNASSESSED_NOT_CLOSED'for r in c['rows'])==143
idx=get('integrated_production_interval_index_v11.json');assert idx['interval_rows']==627 and len(idx['rows'])==627 and idx['extended_span_remaining_count']==143 and len(idx['prior_draft_span_extended_intervals_remaining'])==143
assert set(idx['prior_draft_span_extended_intervals_remaining'])=={r['interval_id']for r in c['rows']if r['classification']=='UNASSESSED_NOT_CLOSED'}
for eid in ['G005.01','G006.01']:
 r=next(r for r in idx['rows']if r['interval_id']==eid);assert r['interval_parameters_verified']and 'BOUNDED_INDEPENDENT_QA_PASS'in r['production_status']
freeze=get('FREEZE_RECEIPT.json');assert freeze['criteria_sha256']==sha(P/'ACCEPTANCE_FROZEN.json')and freeze['spec_sha256']==sha(P/'ORIGINAL_SPAN_SPEC.json');assert get('ORIGINAL_VALIDATION_attempt02.json')['status']=='PASS'and all(get('ORIGINAL_VALIDATION_attempt02.json')['checks'].values());assert get('COLD_START_EXECUTION.json')['status']=='PASS'and get('COLD_START_EXECUTION.json')['matching_PNGs']==48;assert get('RENDER_OUTPUTS.json')['status']=='PASS'
manifest=get('original_attempt02/render_manifest.json');assert len(manifest)==48
for m in manifest:
 f=P/'original_attempt02'/m['system']/f"f{m['frame']:05}.png";assert sha(f)==m['sha256'];assert sha(P/'cold_package/output'/m['system']/f"f{m['frame']:05}.png")==m['sha256']
pins=[]
for n in ['QA_source_batch1.json','QA_batch2_production.json']:
 qa=get(n);assert qa['status'].startswith('PASS'),qa['status'];pinlist=qa.get('input_pins',[]);assert pinlist,'missingQAinputpins'
 for x in pinlist:assert sha(Path(x['path']))==x['sha256'],x['path'];pins.append(x)
assert get('EVIDENCE_RECONCILIATION.json')['defects'][0]['status']=='INVALID_SUPERSEDED_RETAINED'
source=get('SOURCE_VERIFICATION.json');assert sha(Path(source['path']))==source['sha256']=='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66'
assert req['actual_listening_seconds']==0 and req['ASR_undetermined']==21 and req['ASR_potential_flags']==7 and req['full_AV']=='BLOCKED'and req['CT_SCAN_COMPLETE']is False and req['complete_videos']==0
assert get('WHOLE_VIDEO_COLD_START_PACKAGE_v3.json')['status']=='PREREQUISITES_INCOMPLETE';assert get('WORKER_TERMINAL_RECEIPT.json')['all_this_run_workers_terminal']is True
# Validate exact priorreceiptcopy bytes, no current-commit receipt inclusion.
for x in get('PRIOR_RECEIPT_VALIDATION.json')['files']:assert sha(P/'prior_publication_receipts'/x['file'])==x['sha256']
font=Path(get('ORIGINAL_SPAN_SPEC.json')['font']);save('DEPENDENCY_CLOSURE.json',{'source_path':source['path'],'source_sha256':source['sha256'],'source_bytes':source['bytes'],'source_media_in_git':False,'native_evidence_inventory':'EXTERNAL_MEDIA_SHA256.csv generated before seal','render_package':get('COLD_START_EXECUTION.json'),'python':sys.version,'Pillow':PIL.__version__,'font_path':str(font),'font_sha256':sha(font),'render_inputs':['ORIGINAL_SPAN_SPEC.json','render_original_attempt02.py','ACCEPTANCE_FROZEN.json'],'qa_input_pin_count':len(pins),'all_QA_inputs_rehashed':True,'parent':'efeacb0f7adebf57d20f55733947ea5dbb57c26c','recovery':'Text-onlybundle requires publishedparent and durable external source/native/render media; exactlocators/hashes preserved. No rawmedia transportedthroughGit.'})
for x in P.rglob('*.json'):json.loads(x.read_text())
entry=get('ENTRY_STATE.json');git=lambda *a:subprocess.check_output(['git','-C',str(R),*a]).decode();assert git('rev-parse','HEAD').strip()==entry['canonical_head'];assert sha(R/'.git/index')==entry['index_sha256'];assert git('status','--porcelain=v1')==entry['status'];assert git('stash','list','--format=%H %gd')==entry['stashes'];assert git('rev-parse','refs/heads/research/casually-finance-editing-forensics').strip()==entry['local_research_ref']
save('FINAL_VALIDATION.json',{'channel':'Casual Finance','video_id':'xtqbRt94TTw','status':'PASS','948IDs_order_preserved':True,'strict_timing_before':572,'resolved_rows':req['resolved_row_ids'],'remaining':562,'exact_or_reconciled_phase_rows':6,'continuous_fragments':3,'no_meaningful_visible_event':1,'other_components_and_specrow_metadata':4,'changed_ledger_rows_total':len(changed),'extended_spans':[145,2,143],'outside_unknowns_open':2,'qa_input_pins_rehashed':len(pins),'bounded_original_coldstart_frames':48,'prior_receipts_included':8,'source_rehashed':True,'canonical_index_stash_state_preserved':True,'failed_artifacts_and_attempts_preserved':True,'audio0_AVblocked_CTfalse':True,'whole_video':'NOT_RUN_PREREQUISITES_INCOMPLETE'});print('FINAL_VALIDATION PASS',len(changed),'changedrows',len(pins),'QAinputpins;48coldmatches;562timing143spans')
