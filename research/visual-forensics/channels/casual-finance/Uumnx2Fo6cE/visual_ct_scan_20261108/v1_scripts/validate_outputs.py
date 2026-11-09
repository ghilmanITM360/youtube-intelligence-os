# Substantive validator for Uumnx2Fo6cE package. usage: validate_outputs.py ROOT [--source] -> writes ROOT/VALIDATION_RESULTS.json, exit 1 on any failure
import sys, os, json, re, hashlib, subprocess
import pandas as pd, numpy as np
ROOT=sys.argv[1].rstrip('/')+'/'; CHECK_SOURCE='--source' in sys.argv
SRC="/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/The New American Housing Crisis Has Landed.mp4"
R=[]
def chk(name,ok,detail=''): R.append(dict(check=name,status='PASS' if ok else 'FAIL',detail=str(detail)[:400]))
def rd(f): return pd.read_csv(ROOT+f).fillna('')
N=22097; FPS=24
man=json.load(open(ROOT+'SOURCE_IDENTITY_AND_MANIFEST.json'))
if CHECK_SOURCE:
    h=hashlib.sha256(open(SRC,'rb').read()).hexdigest(); chk('source_sha256_recomputed_matches_manifest',h==man['source_sha256'],h)
chk('manifest_sha_matches_registered',man['registered_manifest_comparison']['registered_sha256']==man['source_sha256'] and man['registered_manifest_comparison']['sha_match'] is True)
chk('manifest_frame_count',man['video']['frames_decoded']==N)
M=rd('FULL_FRAME_MEASUREMENTS.csv')
chk('measurements_row_count',len(M)==N,len(M)); chk('frame_index_contiguous',(M.frame.values==np.arange(len(M))).all())
chk('pts_cfr_24',np.allclose(M.pts_time.values,(np.arange(len(M))+1)/FPS,atol=2e-6),'max dev %.2e'%np.abs(M.pts_time.values-(np.arange(len(M))+1)/FPS).max())
V=rd('VISUAL_STATES.csv'); B=rd('BOUNDARY_VERIFICATION.csv'); I=rd('INTRA_STATE_EVENTS.csv'); MO=rd('MOTION_INTERVALS.csv'); E=rd('tables/episodes_classified.csv')
# unique ids
chk('state_ids_unique',V.state_id.is_unique); chk('event_ids_unique_boundary',B.event_id.is_unique); chk('event_ids_unique_intra',I.event_id.is_unique); chk('motion_ids_unique',MO.motion_id.is_unique)
# timeline coverage: states + transition-motion intervals tile [0,N-1] exactly
cov=np.zeros(N,int)
for r in V.itertuples(): cov[int(r.start_frame):int(r.end_frame)+1]+=1
tm=B[B.kind=='STATE_TRANSITION_MOTION']
for r in tm.itertuples(): cov[int(r.start_frame):int(r.end_frame)+1]+=1
chk('timeline_fully_covered_once',(cov==1).all(),f'uncovered={int((cov==0).sum())} overlap={int((cov>1).sum())}')
chk('states_ordered',(V.start_frame.values[1:]>V.end_frame.values[:-1]).all() and V.start_frame.iloc[0]==0 and V.end_frame.iloc[-1]==N-1)
chk('state_frame_counts',(V.end_frame-V.start_frame+1==V.n_frames).all())
chk('state_pts_match_frames',np.allclose(V.pts_start.values,(V.start_frame.values+1)/FPS,atol=2e-4) and np.allclose(V.pts_end.values,(V.end_frame.values+1)/FPS,atol=2e-4))
chk('state_duration',np.allclose(V.duration_s.values,V.n_frames.values/FPS,atol=2e-4))
# boundary evidence
main=B[~B.event_id.str.startswith('SUB')]
chk('all_episodes_have_boundary_record',set(main.event_id)==set(f'EP{e:04d}' for e in E.ep),f'{len(main)} vs {len(E)}')
chk('boundary_verdicts_valid',B.verdict.isin(['CONFIRMED','RECLASSIFIED','CODEC_ARTIFACT','UNVERIFIED']).all())
chk('boundary_has_native_frames_ref',(B.frames_viewed!='').all() and (B.evidence_sheet!='').all())
sheets=set(B.evidence_sheet.str.split('#').str[0]); miss=[s for s in sheets if not os.path.exists(ROOT+s)]
chk('boundary_sheets_exist',len(miss)==0,miss[:3]); chk('boundary_sheet_count',len([s for s in sheets if s.startswith('boundary_sheets/')])==90)
chk('boundary_frames_in_range',((B.start_frame.astype(int)>=0)&(B.end_frame.astype(int)<N)&(B.end_frame.astype(int)>=B.start_frame.astype(int))).all())
chk('boundary_pts_match',np.allclose(B.pts_start.astype(float).values,(B.start_frame.astype(int).values+1)/FPS,atol=2e-4))
chk('reviewer_description_present_and_nongeneric',(B.reviewer_description.str.split().str.len()>=6).all(),f'short={int((B.reviewer_description.str.split().str.len()<6).sum())}')
# shot-count honesty
shots=rd('tables/shots_inferred.csv'); chk('shots_labelled_inferred',shots.label.str.contains('INFERRED').all())
chk('no_boundary_labelled_verified_shot',not B.label_shot.str.contains('VERIFIED_SHOT',na=False).any())
# intra-state events
chk('intra_parent_state_valid',I.parent_state.isin(V.state_id).all(),f'bad={int((~I.parent_state.isin(V.state_id)).sum())}')
vs=V.set_index('state_id'); inside=[(vs.loc[r.parent_state,'start_frame']<=r.start_frame<=vs.loc[r.parent_state,'end_frame']) for r in I.itertuples() if r.parent_state in vs.index]
chk('intra_frames_inside_parent',all(inside),f'bad={inside.count(False)}')
micro_eps=set(f'EP{e:04d}' for e in E[E.kind=='MICRO_EVENT'].ep); chk('every_micro_episode_has_intra_event',micro_eps<=set(I.source_episode),f'missing={len(micro_eps-set(I.source_episode))}')
chk('subthreshold_events_present',(I.tier=='SUBTHRESHOLD').sum()==42)
chk('intra_event_descriptions',(I.description.str.split().str.len()>=6).all())
# motion
chk('motion_covers_all_n_ge3_episodes',set(MO.source_episode)==set(f'EP{e:04d}' for e in E[E.n>=3].ep))
chk('motion_duration',np.allclose(MO.duration_s.astype(float).values,MO.n_frames.astype(int).values/FPS,atol=2e-3))
chk('motion_neighbors_valid',MO.state_before.isin(set(V.state_id)|{''}).all() and MO.state_after.isin(set(V.state_id)|{''}).all())
# text honesty
hi_unread=V[(V.confidence=='HIGH')&(V.unreadable_text!='')]; chk('no_HIGH_confidence_with_unreadable_text',len(hi_unread)==0,f'{len(hi_unread)}')
chk('confidence_values',V.confidence.isin(['HIGH','MEDIUM','LOW']).all())
# reconstruction
spec=json.load(open(ROOT+'PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json'))
chk('spec_count_equals_states',len(spec)==len(V) and [s['state_id'] for s in spec]==list(V.state_id))
bad=[s['state_id'] for s,v in zip(spec,V.itertuples()) if s['SOURCE_FORENSIC_DESCRIPTION']['frames']!=[int(v.start_frame),int(v.end_frame)] or not os.path.exists(ROOT+s['SOURCE_FORENSIC_DESCRIPTION']['evidence_image'])]
chk('spec_source_grounding',len(bad)==0,bad[:5])
BRAND=re.compile(r'\b(dave|casual finance|casually finance|redfin|yahoo|lennar|census|zillow|nahb|fannie|freddie|ground news|trump|biden|harris|griner)\b',re.I)
chk('no_brand_or_person_names_in_original_instructions',not any(BRAND.search(s['ORIGINAL_PRODUCTION_INSTRUCTIONS']['image_generation_prompt']+' '+s['ORIGINAL_PRODUCTION_INSTRUCTIONS']['build']) for s in spec),[s['state_id'] for s in spec if BRAND.search(s['ORIGINAL_PRODUCTION_INSTRUCTIONS']['image_generation_prompt']+' '+s['ORIGINAL_PRODUCTION_INSTRUCTIONS']['build'])][:5])
chk('prompt_min_length',(V.prompt.str.split().str.len()>=8).all(),f'short={int((V.prompt.str.split().str.len()<8).sum())}')
chk('recon_min_length',(V.recon.str.len()>=30).all(),f'short={int((V.recon.str.len()<30).sum())}')
chk('objects_nongeneric',((V.objects.str.split().str.len()>=6)|V.objects.str.contains('blank',case=False)).all(),f'short={int((V.objects.str.split().str.len()<6).sum())}')
# generic duplication: exact duplicate prompts allowed only inside consecutive animation series (<=1.5 s)
dups=V[V.prompt.duplicated(keep=False)]; uncited=[r.state_id for r in dups.itertuples() if r.duration_s>1.5]
chk('exact_duplicate_prompts_only_short_series',len(uncited)==0,f'dups={len(dups)} long_dups={uncited[:5]}')
tok=[set(re.findall(r'[a-z]+',p.lower())) for p in V.prompt]; hi=0
for i in range(len(tok)-1):
    s=len(tok[i]&tok[i+1])/max(1,len(tok[i]|tok[i+1]))
    if s>0.9 and V.duration_s.iloc[i]>1.5 and V.duration_s.iloc[i+1]>1.5: hi+=1
chk('adjacent_near_duplicate_prompts_lt_3pct',hi<=0.03*len(V),f'{hi}')
# audio claims
asr=open(ROOT+'ASR_VISUAL_ALIGNMENT.md').read(); chk('asr_doc_declares_unverified','ASR_ONLY_NOT_AUDIO_VERIFIED' in asr and 'NOT_COMPLETED' in asr)
A=rd('audio_visual_alignment.csv'); chk('alignment_rows_all_asr_only',(A.asr_status=='ASR_ONLY_NOT_AUDIO_VERIFIED').all() and len(A)==len(B[B.kind=='STATE_BOUNDARY']))
chk('states_asr_status',(V.asr_status=='ASR_ONLY_NOT_AUDIO_VERIFIED').all())
alltext=''.join(open(ROOT+f).read() for f in ['ASR_VISUAL_ALIGNMENT.md','VISUAL_NARRATIVE_AND_ATTENTION_ANALYSIS.md','VISUAL_QUALITY_SCORECARD.md'] if os.path.exists(ROOT+f))
chk('no_audio_verified_or_retention_claims',not re.search(r'((?<!not )(?<!NOT_)audio[- ]verified|FULL_AV_SIGNOFF_COMPLETE|retention (rose|increased|was \d))',alltext.replace('NOT_AUDIO_VERIFIED','')),'')
# contradictions: key counts in docs
kf=json.load(open(ROOT+'key_facts.json'))
chk('key_facts_match_tables',kf['states']==len(V) and kf['intra_events']==len(I) and kf['motion_intervals_total']==len(MO) and kf['episodes']==len(E) and kf['frames']==len(M))
for f,needles in [('OWNER_SUMMARY_ROMAN_URDU.md',[str(len(V)),str(len(I)),str(N)]),('CONTINUATION_HANDOFF.md',[str(len(V)),str(N)]),('ART_DIRECTION_AND_DESIGN_DNA.md',[str(len(V)),str(len(I))])]:
    if os.path.exists(ROOT+f):
        t=open(ROOT+f).read().replace(',',''); chk(f'doc_counts_consistent:{f}',all(n in t for n in needles),[n for n in needles if n not in t])
# required deliverables non-empty
REQ=['SOURCE_IDENTITY_AND_MANIFEST.json','FULL_FRAME_MEASUREMENTS.csv','SHOT_CANDIDATES.csv','VISUAL_STATES.csv','INTRA_STATE_EVENTS.csv','MOTION_INTERVALS.csv','BOUNDARY_VERIFICATION.csv','STATE_BY_STATE_VISUAL_FORENSICS.md','ART_DIRECTION_AND_DESIGN_DNA.md','VISUAL_NARRATIVE_AND_ATTENTION_ANALYSIS.md','ASR_VISUAL_ALIGNMENT.md','ORIGINAL_RECONSTRUCTION_BLUEPRINT.md','PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json','PRODUCTION_ASSET_AND_EDITING_PLAN.md','VISUAL_QUALITY_SCORECARD.md','CONTINUATION_HANDOFF.md','OWNER_SUMMARY_ROMAN_URDU.md']
miss=[f for f in REQ if not os.path.exists(ROOT+f) or os.path.getsize(ROOT+f)<500]; chk('required_deliverables_present_nonempty',len(miss)==0,miss)
# state md has a section per state
md=open(ROOT+'STATE_BY_STATE_VISUAL_FORENSICS.md').read() if os.path.exists(ROOT+'STATE_BY_STATE_VISUAL_FORENSICS.md') else ''; chk('state_md_section_per_state',all(f'## {s} ' in md for s in V.state_id))
res=dict(video_id='Uumnx2Fo6cE',total=len(R),passed=sum(r['status']=='PASS' for r in R),failed=sum(r['status']=='FAIL' for r in R),checks=R)
json.dump(res,open(ROOT+'VALIDATION_RESULTS.json','w'),indent=1)
print(f"{res['passed']}/{res['total']} PASS, {res['failed']} FAIL")
for r in R:
    if r['status']=='FAIL': print('FAIL',r['check'],r['detail'])
sys.exit(1 if res['failed'] else 0)
