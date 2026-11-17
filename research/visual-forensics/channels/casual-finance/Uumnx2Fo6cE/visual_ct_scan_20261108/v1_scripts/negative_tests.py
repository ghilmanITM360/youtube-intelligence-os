# Deliberate mutations against a temporary copy (hard-linked big files, copied small files); each must make the validator FAIL.
import os, shutil, subprocess, json, re, sys, tempfile
import pandas as pd
SRC='/Users/ghilmankhan/YIOS-local-audits/2026-10-24-Uumnx2Fo6cE-deep-ct-scan/'
PY='/Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python'
tmp=tempfile.mkdtemp(prefix='negtest_')+'/c/'
os.makedirs(tmp)
for f in os.listdir(SRC):
    if f in ('agents','frames','asr','audio','native','qa'): continue
    p=SRC+f
    if f=='boundary_sheets': os.makedirs(tmp+f); [os.link(p+'/'+g,tmp+f+'/'+g) for g in os.listdir(p)]
    elif os.path.isdir(p): shutil.copytree(p,tmp+f)
    else: shutil.copy(p,tmp+f)
os.makedirs(tmp+'frames/ep_stable')
for g in os.listdir(SRC+'frames/ep_stable'): os.link(SRC+'frames/ep_stable/'+g,tmp+'frames/ep_stable/'+g)
def run(): 
    r=subprocess.run([PY,SRC+'v1_scripts/validate_outputs.py',tmp],capture_output=True,text=True); return r.returncode,[l for l in r.stdout.splitlines() if l.startswith('FAIL')]
def snap(files): return {f:open(tmp+f,'rb').read() for f in files}
def restore(s): [open(tmp+f,'wb').write(b) for f,b in s.items()]
base_rc,_=run(); results=[dict(test='baseline_unmutated',expected='PASS',got='PASS' if base_rc==0 else 'FAIL',caught=base_rc==0)]
def mut(name,files,fn,expect):
    s=snap(files); fn(); rc,fails=run(); restore(s)
    hit=[f for f in fails if expect in f]
    results.append(dict(test=name,expected_failure=expect,validator_failed=rc!=0,named_check_failed=bool(hit),caught=rc!=0 and bool(hit),failures=[f[:90] for f in fails][:3]))
def csvmut(f,fn):
    def _():
        d=pd.read_csv(tmp+f).fillna(''); d=fn(d); d.to_csv(tmp+f,index=False)
    return _
mut('delete_a_state_row',['VISUAL_STATES.csv'],csvmut('VISUAL_STATES.csv',lambda d:d.drop(index=100)),'timeline_fully_covered_once')
mut('shift_a_state_frame_boundary',['VISUAL_STATES.csv'],csvmut('VISUAL_STATES.csv',lambda d:d.assign(end_frame=[x+5 if i==50 else x for i,x in enumerate(d.end_frame)])),'timeline_fully_covered_once')
mut('timestamp_mismatch',['VISUAL_STATES.csv'],csvmut('VISUAL_STATES.csv',lambda d:d.assign(pts_start=[x+0.5 if i==10 else x for i,x in enumerate(d.pts_start)])),'state_pts_match_frames')
mut('duplicate_state_id',['VISUAL_STATES.csv'],csvmut('VISUAL_STATES.csv',lambda d:d.assign(state_id=['S0001' if i==2 else x for i,x in enumerate(d.state_id)])),'state_ids_unique')
mut('duplicate_boundary_event_id',['BOUNDARY_VERIFICATION.csv'],csvmut('BOUNDARY_VERIFICATION.csv',lambda d:d.assign(event_id=['EP0001' if i==5 else x for i,x in enumerate(d.event_id)])),'event_ids_unique_boundary')
mut('remove_boundary_evidence_row',['BOUNDARY_VERIFICATION.csv'],csvmut('BOUNDARY_VERIFICATION.csv',lambda d:d.drop(index=200)),'all_episodes_have_boundary_record')
mut('missing_evidence_sheet_reference',['BOUNDARY_VERIFICATION.csv'],csvmut('BOUNDARY_VERIFICATION.csv',lambda d:d.assign(evidence_sheet=['boundary_sheets/bsheet_999.jpg#row0' if i==3 else x for i,x in enumerate(d.evidence_sheet)])),'boundary_sheets_exist')
mut('drop_intra_state_event',['INTRA_STATE_EVENTS.csv'],csvmut('INTRA_STATE_EVENTS.csv',lambda d:d.drop(index=d[d.tier=='MAIN_THRESHOLD'].index[7])),'every_micro_episode_has_intra_event')
mut('intra_event_wrong_parent',['INTRA_STATE_EVENTS.csv'],csvmut('INTRA_STATE_EVENTS.csv',lambda d:d.assign(parent_state=['S0400' if i==3 else x for i,x in enumerate(d.parent_state)])),'intra_frames_inside_parent')
mut('claim_verified_shot',['BOUNDARY_VERIFICATION.csv'],csvmut('BOUNDARY_VERIFICATION.csv',lambda d:d.assign(label_shot=['VERIFIED_SHOT_BOUNDARY' if i==9 else x for i,x in enumerate(d.label_shot)])),'no_boundary_labelled_verified_shot')
mut('high_confidence_on_unreadable_text',['VISUAL_STATES.csv'],csvmut('VISUAL_STATES.csv',lambda d:d.assign(confidence=['HIGH' if (i==20) else x for i,x in enumerate(d.confidence)],unreadable_text=['tiny body text' if i==20 else x for i,x in enumerate(d.unreadable_text)])),'no_HIGH_confidence_with_unreadable_text')
def brand():
    j=json.load(open(tmp+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json')); j[30]['ORIGINAL_PRODUCTION_INSTRUCTIONS']['image_generation_prompt']+=' in the style of Casual Finance with the Redfin logo'; json.dump(j,open(tmp+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json','w'))
mut('brand_name_in_original_prompt',['PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json'],brand,'no_brand_or_person_names')
def spec_frames():
    j=json.load(open(tmp+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json')); j[40]['SOURCE_FORENSIC_DESCRIPTION']['frames']=[1,2]; json.dump(j,open(tmp+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json','w'))
mut('spec_wrong_source_frames',['PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json'],spec_frames,'spec_source_grounding')
def spec_drop():
    j=json.load(open(tmp+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json')); j.pop(60); json.dump(j,open(tmp+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json','w'))
mut('missing_reconstruction_record',['PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json'],spec_drop,'spec_count_equals_states')
mut('generic_copied_description',['VISUAL_STATES.csv'],csvmut('VISUAL_STATES.csv',lambda d:d.assign(objects=['ok' if i==15 else x for i,x in enumerate(d.objects)])),'objects_nongeneric')
def dupprompt():
    d=pd.read_csv(tmp+'VISUAL_STATES.csv').fillna(''); idx=d[d.duration_s>3].index[:6]; d.loc[idx,'prompt']='a flat hand drawn house on a plain white background with a presenter at the right side pointing'; d.to_csv(tmp+'VISUAL_STATES.csv',index=False)
mut('copied_prompt_on_long_states',['VISUAL_STATES.csv'],dupprompt,'exact_duplicate_prompts_only_short_series')
def asrclaim():
    t=open(tmp+'ASR_VISUAL_ALIGNMENT.md').read().replace('ASR_ONLY_NOT_AUDIO_VERIFIED','VERIFIED').replace('NOT_COMPLETED','COMPLETED'); open(tmp+'ASR_VISUAL_ALIGNMENT.md','w').write(t)
mut('unjustified_audio_verified_claim',['ASR_VISUAL_ALIGNMENT.md'],asrclaim,'asr_doc_declares_unverified')
def keyfacts():
    k=json.load(open(tmp+'key_facts.json')); k['states']=500; json.dump(k,open(tmp+'key_facts.json','w'))
mut('report_count_contradiction',['key_facts.json'],keyfacts,'key_facts_match_tables')
def doccount():
    t=open(tmp+'OWNER_SUMMARY_ROMAN_URDU.md').read().replace('507','499'); open(tmp+'OWNER_SUMMARY_ROMAN_URDU.md','w').write(t)
mut('summary_contradicts_ledger',['OWNER_SUMMARY_ROMAN_URDU.md'],doccount,'doc_counts_consistent')
def manifest():
    m=json.load(open(tmp+'SOURCE_IDENTITY_AND_MANIFEST.json')); m['video']['frames_decoded']=22000; json.dump(m,open(tmp+'SOURCE_IDENTITY_AND_MANIFEST.json','w'))
mut('manifest_frame_count_wrong',['SOURCE_IDENTITY_AND_MANIFEST.json'],manifest,'manifest_frame_count')
def meas():
    d=pd.read_csv(tmp+'FULL_FRAME_MEASUREMENTS.csv'); d.at[500,'pts_time']=d.at[500,'pts_time']+0.01; d.to_csv(tmp+'FULL_FRAME_MEASUREMENTS.csv',index=False)
mut('measurement_pts_corrupted',['FULL_FRAME_MEASUREMENTS.csv'],meas,'pts_cfr_24')
mut('motion_interval_dropped',['MOTION_INTERVALS.csv'],csvmut('MOTION_INTERVALS.csv',lambda d:d.drop(index=20)),'motion_covers_all_n_ge3_episodes')
os.remove(tmp+'STATE_BY_STATE_VISUAL_FORENSICS.md'); rc,f=run(); results.append(dict(test='deleted_required_deliverable',expected_failure='required_deliverables',validator_failed=rc!=0,named_check_failed=any('required_deliverables' in x for x in f),caught=rc!=0 and any('required_deliverables' in x for x in f),failures=f[:2]))
caught=sum(1 for r in results if r['caught']);n=len(results)
out=dict(note='Mutations applied to a temporary copy; original outputs untouched.',total_tests=n,caught=caught,all_caught=caught==n,results=results)
json.dump(out,open(SRC+'tables/negative_tests.json','w'),indent=1);print(caught,'/',n,'caught'); [print('MISSED',r) for r in results if not r['caught']]
shutil.rmtree(os.path.dirname(tmp.rstrip('/')))
