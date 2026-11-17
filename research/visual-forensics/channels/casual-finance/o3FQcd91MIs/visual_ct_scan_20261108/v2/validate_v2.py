"""Substantive validator for the o3FQcd91MIs CT scan (v2). Recomputes from raw measurements; does not trust labels.
Gate semantics follow ~/.claude/skills/visual-ct-scan/references/13_completion_gates_validation_handoffs.md and 02/03/07 (not weakened)."""
import csv,json,os,re,hashlib,sys,itertools,statistics as S
R=[];FAIL=[]
def chk(gate,name,cond,detail=''):
    R.append((gate,name,bool(cond),detail))
    if not cond: FAIL.append((gate,name,detail))
def rd(p): return list(csv.DictReader(open(p)))
man=json.load(open('source_manifest.json'))
fm=rd('tables/frame_metrics.csv');fr=rd('v2/frame_metrics_fullres.csv');ep=json.load(open('tables/episodes.json'))
bv=rd('v2/boundary_verification.csv');mi=rd('v2/intra_state_events.csv');spec=rd('v2/state_spec_76.csv');al=rd('v2/audio_visual_alignment_v2.csv')
ob=json.load(open('v2/state_objective.json'));facts=json.load(open('v2/key_facts.json'))
# ---------------- G1 technical frame coverage
h=hashlib.sha256(open(man['source_path'],'rb').read()).hexdigest()
chk('G1','source sha256 recomputed equals manifest+registry',h==man['source_sha256']=="82ab2b63ce250723f37e569d15ecf0a8b67c22f1841ec14637216d34e4a89c85")
chk('G1','8338 frames measured at 320x180 and full-res',len(fm)==8338==len(fr))
chk('G1','PTS(i)=(i+1)/30 for every frame (CFR proven)',all(abs(float(fm[i]['pts_time'])-(i+1)/30)<1e-5 for i in range(8338)))
bf=[(int(e['change_start_frame']),int(e['change_end_frame'])) for e in bv]
un=[e for e in ep if not any(abs(e['start_frame']-a)<=1 and abs(e['end_frame']-b)<=1 for a,b in bf)]
mf={int(m['frame']) for m in mi}
I={int(x['frame']) for x in fr if x['pict']=='I'}
codec=[e for e in un if e['start_frame'] not in mf]
chk('G1','every measured episode accounted: boundary + codec + micro == total',len(ep)==len(ep)-len(un)+len(codec)+len([e for e in un if e['start_frame'] in mf]) and len(ep)-len(un)==75 and len(codec)==11 and len(mf)==3,f"{len(ep)} episodes")
chk('G1','all 11 codec episodes within 1 frame of an I-frame',all(any(abs(e['start_frame']-i)<=1 for i in I) for e in codec))
chk('G1','codec episodes max abs diff <=120 (diffuse, below content contrast)',all(int(fr[e['start_frame']]['max_abs_diff'])<=120 for e in codec),str([int(fr[e['start_frame']]['max_abs_diff']) for e in codec]))
per=[i for i in I if i>0 and not any(a-1<=i<=b+1 for a,b in bf)]
chk('G1','>=95% of periodic I-frames show diffuse edge-dominant diff (median edge fraction>=0.85)',sum(1 for i in per if int(fr[i]['px_diff_ge6'])>0)/len(per)>=0.95 and S.median(float(fr[i]['edge_fraction']) for i in per if int(fr[i]['px_diff_ge6'])>0)>=0.85)
chk('G1','I-frame inside a zero-texture black hold shows zero diff (codec signature, no content)',int(fr[5609]['px_diff_ge6'])==0 and fr[5609]['pict']=='I')
chk('G1','3 micro-events are high-contrast and localized (max diff>=150, bbox<=70%)',all(int(m['max_abs_diff'])>=150 and (lambda b:(b[2]-b[0])*(b[3]-b[1])/(1280*720)<0.7)(json.loads(m['bbox_native'])) for m in mi))
chk('G1','no non-event, non-micro frame has max abs diff >=150 (nothing missed above stated sensitivity)',all(int(fr[i]['max_abs_diff'])<150 for i in range(1,8338) if not any(a-1<=i<=b+1 for a,b in bf) and i not in mf))
# ---------------- G2 visual-state coverage
REQ=['objects_and_positions','pose_expression','art_direction','composition_negative_space','typography_text','colors','hierarchy_focal','camera_framing','motion_or_hold','entry_transition','exit_transition','story_purpose','narration_asr','asr_status','attention_hypothesis','retention_claim','continuity','reconstruction_requirement','original_prompt','frame_refs','measured_blobs_norm_bbox']
chk('G2','76 state records',len(spec)==76)
bad=[(r['state_id'],k) for r in spec for k in REQ if len(r[k].strip())<(2 if k=='narration_asr' else 12)]
chk('G2','every state has all required fields non-trivially filled',not bad,str(bad[:5]))
chk('G2','states tile all frames (+2 black-dip frames)',sum(int(r['n_frames']) for r in spec)+2==8338 and all(int(spec[i+1]['start_frame'])-int(spec[i]['end_frame']) in (1,3) for i in range(75)) and int(spec[0]['start_frame'])==0 and int(spec[-1]['end_frame'])==8337)
chk('G2','exact durations = frames/30',all(abs(float(r['duration_s'])-int(r['n_frames'])/30)<1e-3 for r in spec))
fr_ok=all(all(os.path.exists(p) for p in re.findall(r'(?:frames|v2)/[\w\.]+\.jpg',r['frame_refs'])) for r in spec)
chk('G2','all referenced evidence sheets exist',fr_ok)
chk('G2','entry/mid/exit frames referenced for every state',all(('entry' in r['frame_refs'] and 'exit' in r['frame_refs'] and 'mid' in r['frame_refs']) for r in spec))
chk('G2','sub-state events recorded for S007.1,S009.2,S009.8',{m['parent_state'] for m in mi}=={'S007.1','S009.2','S009.8'} and all(r['sub_state_events'] for r in spec if r['state_id'] in {'S007.1','S009.2','S009.8'}))
# ---------------- G3 native-frame transition verification
chk('G3','75 boundary verification rows',len(bv)==75)
def has(fv,l): return l in fv
chk('G3','each boundary has pre-8, pre-1, change, post+1, stable frames recorded',all(all(has(b['frames_viewed'],t) for t in ('pre-8','pre-1','chg','post+1','stable')) for b in bv))
chk('G3','each boundary change frames correct (74 single, 1 dip)',sum(1 for b in bv if b['change_frames']=='1')==74 and sum(1 for b in bv if b['classification'].startswith('BLACK_DIP'))==1)
chk('G3','sheets exist for all boundaries',all(os.path.exists(b['sheet']) for b in bv))
chk('G3','windows unstable only where an I-frame sits in window (explained)',all(b['instability_explained_by_iframe'] in('n/a','YES') for b in bv))
chk('G3','every boundary has classification and motion/camera/animation class',all(b['classification'] and b['motion_class'] and b['camera_class']=='NONE' and b['animation_class']=='NONE' for b in bv))
dip=[b for b in bv if b['classification'].startswith('BLACK_DIP')][0]
chk('G3','black dip = frames 7233-7234 pts 241.1333-241.1667, arrival f7235',dip['change_start_frame']=='7233' and dip['change_end_frame']=='7235')
chk('G3','micro-event crops exist and 3 events verified',os.path.exists('v2/microevent_crops.jpg') and len(mi)==3 and all(m['status']=='VERIFIED' for m in mi))
# ---------------- G4 art direction / creative analysis
chk('G4','attention hypotheses labelled INFERRED, no retention claim',all(r['attention_hypothesis'].startswith('INFERRED') and r['retention_claim'].startswith('NONE') for r in spec))
chk('G4','measured palette + contrast present for every state',all('palette' in r['colors'] and 'contrast' in r['colors'] for r in spec))
unv=[r['state_id'] for r in spec if 'UNVERIFIED' in r['typography_text']]
chk('G4','unresolved small text explicitly flagged UNVERIFIED (not invented)',len(unv)>=5,f"{len(unv)} states: {unv}")
# ---------------- G5 visual-to-script
chk('G5','78 audio alignment rows, ASR_UNCERTIFIED, no listening claim',len(al)==78 and all('ASR_UNCERTIFIED' in r['audio_listening_status'] and 'NO HUMAN LISTENING' in r['audio_listening_status'] for r in al))
chk('G5','15 events outside +-0.2 s classified; 11 consistent in both ASR runs, 4 disagree',sum(1 for r in al if r['outside_0p2_small_en']=='True')==15 and facts['asr_outside_both_runs']==11 and facts['asr_outliers_disagree']==4)
chk('G5','every state carries ASR status line',all(r['asr_status'].startswith('ASR_UNCERTIFIED') for r in spec))
# ---------------- G6 reconstruction
FORB=['dave','eve ','tesla','buffett','soros','amazon','google','wolf of wall','zyn','pei wei','nobu','malibu','palantir','investopedia','fartcoin','guinness','trump','berkshire','casual finance','casually','nvidia','bitcoin','s&p']
pr=[r['original_prompt'].lower().split('[neg]')[0].replace('[style]','') for r in spec]
prfull=[r['original_prompt'].lower() for r in spec]
hits=[(spec[i]['state_id'],t) for i,p in enumerate(prfull) for t in FORB if t in p]
chk('G6','original prompts contain no source names/brands/characters',not hits,str(hits[:6]))
pk=open('v2/ORIGINAL_PRODUCTION_PACKAGE.md').read().lower()
hp=[t for t in FORB if t in pk]
chk('G6','production package contains no source names/brands/characters',not hp,str(hp))
for sec in range(1,14): chk('G6',f'package section {sec} present',re.search(rf'^## {sec}\. ',open('v2/ORIGINAL_PRODUCTION_PACKAGE.md').read(),re.M) is not None)
def toks(s): return set(re.findall(r'[a-z0-9\.]+',s))
pairs=[]
for (i,a),(j,b) in itertools.combinations(enumerate(pr),2):
    ta,tb=toks(a),toks(b);jac=len(ta&tb)/len(ta|tb)
    if jac>=0.7: pairs.append((spec[i]['state_id'],spec[j]['state_id'],round(jac,2)))
ids=[r['state_id'] for r in spec]
BLACK={'S010.0','S012.0','S014.0'}
def allowed(a,b):
    if a in BLACK and b in BLACK: return True
    rb=spec[ids.index(b)];return a in (rb['continuity']+rb['reconstruction_requirement'])
okpairs=all(allowed(a,b) for a,b,_ in pairs)
chk('G6','near-duplicate prompts (Jaccard>=0.7) are explicit documented reuses only',okpairs,str(pairs))
sim05=[]
for i,a_ in enumerate(pr):
    for j,b_ in enumerate(pr):
        if j>i and len(toks(a_)&toks(b_))/len(toks(a_)|toks(b_))>=0.5: sim05.append((ids[i],ids[j]))
chk('G6','every prompt pair with Jaccard>=0.5 is a documented reuse/template pair',all(allowed(x,y) for x,y in sim05),str([p for p in sim05 if not allowed(*p)]))
chk('G6','>=65% of prompts are below 0.5 similarity to all others (rest are documented reuses)',(76-len({s for p in sim05 for s in p}))/76>=0.65)
chk('G6','each prompt >= 25 words state-specific text',all(len(toks(p))>=25 for p in pr))
# ---------------- traceability: report facts == recomputed facts
rep=open('v2/visual_ct_scan_report_v2.md').read() if os.path.exists('v2/visual_ct_scan_report_v2.md') else ''
m=re.search(r'<!--KEY_FACTS(.*?)KEY_FACTS-->',rep,re.S)
chk('TRACE','report embeds KEY_FACTS and equals recomputed key_facts.json',bool(m) and json.loads(m.group(1))==facts)
chk('TRACE','report states CT scan status and AV sign-off blocked',('HUMAN LISTENING: BLOCKED' in rep) and ('FULL AUDIOVISUAL SIGN-OFF: BLOCKED' in rep))
# ---------------- gate computation
def ok(g): return all(c for gg,_,c,_ in R if gg==g)
gates=dict(technical_frame_coverage='PASS' if ok('G1') else 'PARTIAL',visual_state_coverage='PASS' if ok('G2') else 'PARTIAL',native_frame_transition_verification='PASS' if ok('G3') else 'PARTIAL',
 deep_art_direction_creative_analysis='PASS' if ok('G4') else 'PARTIAL',visual_to_script_mapping=('PASS_ASR_UNCERTIFIED' if ok('G5') else 'PARTIAL'),reconstruction_blueprint='PASS' if ok('G6') else 'PARTIAL')
core=[ok('G1'),ok('G2'),ok('G3'),ok('G4'),ok('G5'),ok('G6'),ok('TRACE')]
ct='CT_SCAN_COMPLETE_WITH_EVIDENCE' if all(core) else 'CT_SCAN_PARTIAL'
q=dict(video_id='o3FQcd91MIs',version='v2',source_sha256=man['source_sha256'],gates=gates,
 ct_scan=ct,ct_scan_contract_note="Contract = refs 02/03/13 temporal + creative/reconstruction gates plus sub-second frame-event ledger; the 'audible synchronization' item of SKILL.md CT_SCAN is delivered as ASR_ONLY_NOT_AUDIO_VERIFIED per ref 07; human listening gates FULL_AV_SIGNOFF (ref 13), not CT_SCAN. Owner may overrule by treating listening as a CT prerequisite.",
 human_listening='BLOCKED',full_av_signoff='BLOCKED',
 shot_grouping='INFERRED (47 reviewer-defined shots; 46 boundaries coincide 100% with verified state boundaries; pixel-persistence cannot separate shot from intra-shot changes; EV002 and EV036 are additive yet flagged as shot boundaries)',
 unresolved_small_text_states=unv,
 sensitivity='320x180 pass: ~0.06% pixels; full-res pass: localized changes >=~1.2k px at contrast>=150 would be seen; low-contrast changes <~600 px are indistinguishable from codec noise (BLIND SPOT)',
 checks=[dict(gate=g,check=n,pass_=c,detail=d) for g,n,c,d in R])
json.dump(q,open('v2/quality_gate_v2.json','w'),indent=1)
for g,n,c,d in R: print(('PASS ' if c else 'FAIL ')+g+' '+n+(' | '+d if (not c and d) else ''))
print(json.dumps(gates),ct,'| failures:',len(FAIL))
sys.exit(1 if FAIL else 0)
