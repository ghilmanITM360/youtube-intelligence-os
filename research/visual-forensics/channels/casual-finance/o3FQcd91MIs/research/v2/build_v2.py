import csv,json,bisect,sys,os
sys.path.insert(0,'v2')
from state_authoring_a import A
from state_authoring_b import B
from state_authoring_c import C
AUTH={**A,**B,**C}
VID='o3FQcd91MIs'
st=list(csv.DictReader(open('visual_states.csv')))
ev=list(csv.DictReader(open('visual_event_ledger.csv')))
obj=json.load(open('v2/state_objective.json'))
bw=list(csv.DictReader(open('v2/boundary_windows.csv')))
pers={r[0]:r[3] for r in json.load(open('v2/shot_persistence.json'))}
fr=list(csv.DictReader(open('v2/frame_metrics_fullres.csv')))
asr=json.load(open('audio/o3FQ_16k.json'))
W=[(x['start'],x['end'],x['word'].strip(),x.get('probability',0)) for s in asr['segments'] for x in s['words']]
Ifr={int(r['frame']) for r in fr if r['pict']=='I'}
micro=json.load(open('v2/microevents.json'))
FAM={"F1":"Intro/pose-on-canvas","F2":"Pose + prop","F3":"Hand-drawn chart doodle","F4":"Text-only card","F5":"Evidence/UI card","F6":"Photo insert","F7":"Time-skip / split","F8":"Black beat","F9":"Full-bleed scene","F10":"Gag prop alone","F11":"End card"}
STYLE=("flat 2D hand-drawn marker doodle, near-white #FCFCFC canvas, thick slightly wobbly black outline, solid flat colour fills, no shading, no gradients, "
       "oversized round-head stick-figure characters with dot eyes and a single-line mouth, large empty negative space, 16:9, delivered as transparent PNG layers")
NEG="no photorealism, no shading, no 3D, no logos of real brands, no copyrighted characters, no text unless specified"
def sheet_ev(k): return (k-1)//7+1 if k<=63 else (10 if k<=69 else 11)
def lag(sid):  # words
    a=obj[sid]['start_pts'];b=obj[sid]['end_pts']
    ws=[w for w in W if a-0.05<=w[0]<b]
    return ' '.join(w[2] for w in ws),(round(sum(w[3] for w in ws)/len(ws),3) if ws else None),sum(1 for w in ws if w[3]<0.5)
# ---- boundary verification
evmap={e['event_id']:e for e in ev}
bvrows=[]
for i,(e,w) in enumerate(zip(ev,bw),1):
    a,b=int(e['start_frame']),int(e['end_frame'])
    bef=obj[e['before_state']];aft=obj[e['after_state']]
    bg_b=bef['bg'];bg_a=aft['bg']
    p=float(pers[e['event_id']])
    ibl=[k for k in range(a-8,b+11) if k in Ifr]
    n=b-a+1
    if n==3: cls='BLACK_DIP_2F_THEN_REPLACE'
    elif aft['bg'] in('#110f10','#100f0f','#111010') or (aft['fg_fraction']==0.0): cls='BLACK_HOLD_ENTRY'
    elif bef['fg_fraction']==0.0: cls='BLACK_HOLD_EXIT'
    elif p>=0.9: cls='ADDITIVE_ELEMENT_ENTRY (existing content unchanged)'
    elif p>=0.3: cls='PARTIAL_REPLACE (some content persists)'
    else: cls='FULL_COMPOSITION_REPLACE (hard cut)'
    shotb=st[i-1]['shot_id']!=st[i]['shot_id']
    unstable=not(w['pre_window_stable']=='True' and w['post_window_stable']=='True')
    bvrows.append(dict(event_id=e['event_id'],before_state=e['before_state'],after_state=e['after_state'],
      change_start_frame=a,change_end_frame=b,change_start_pts=round((a+1)/30,4),change_end_pts=round((b+1)/30,4),change_frames=n if n!=3 else '2 black + 1 arrival',
      frames_viewed=w['frames_viewed'],sheet=f"v2/boundary_sheet_{sheet_ev(i):02d}.jpg",
      classification=cls,motion_class='NONE (no interpolated frames before/after; hard replace)' if n==1 else 'NONE (2 black frames then new scene)',
      camera_class='NONE',animation_class='NONE',pixel_persistence_before_to_after=p,
      shot_boundary_flag=shotb,pre_window_stable=w['pre_window_stable'],post_window_stable=w['post_window_stable'],
      iframe_in_window=';'.join(map(str,ibl)) if ibl else '',instability_explained_by_iframe='YES' if (unstable and ibl) else ('n/a' if not unstable else 'NO'),
      verification='VIEWED_NATIVE_FRAMES(pre-8,pre-1,change,post+1,stable+10); MEASURED'))
with open('v2/boundary_verification.csv','w',newline='') as f:
    q=csv.DictWriter(f,fieldnames=list(bvrows[0]));q.writeheader();q.writerows(bvrows)
# ---- intra-state micro events
mrows=[]
mdesc={'3855':('S007.1','TEXT_ENTER: bold green percentage appears below the duration line','x 0.54-0.76,y 0.50'),'4417':('S009.2','ICON_ENTER: tiny stick-figure icon appears right of the equals sign','x 0.55-0.60,y 0.56-0.66'),'4916':('S009.8','TEXT_ENTER: bold word appears above the cash-pile character','x 0.57-0.66,y 0.22-0.30')}
for k,v in micro.items():
    sid,desc,pos=mdesc[k];f=int(k);x=fr[f]
    mrows.append(dict(event_id=f"EVI{len(mrows)+1:02d}",parent_state=sid,frame=f,pts=v['pts'],bbox_native=v['bbox_native'],changed_px_ge30=v['n30'],max_abs_diff=int(x['max_abs_diff']),
      event_class=desc,position=pos,transition_type='HARD_REPLACE_1F (element appears on one frame)',pict_type=x['pict'],iframe_coincident='NO' if f not in Ifr else 'YES',
      evidence='MEASURED(full-res diff, localized, max diff>=184) + VIEWED(v2/microevent_crops.jpg)',status='VERIFIED'))
with open('v2/intra_state_events.csv','w',newline='') as f:
    q=csv.DictWriter(f,fieldnames=list(mrows[0]));q.writeheader();q.writerows(mrows)
# ---- 76-state specification
ROLE={"S001.15":"two-part arrow line: short label, arrow, punchline phrase (first card of a pair)","S001.16":"second card of the pair: swap only the two text parts, arrow identical","S003.0":"the premise question, one line of ~45-60 characters","S011.0":"the premise question restated before the reveal (exact repeat of the earlier card)","S015.0":"short 'what is X?' section-header question, ~15 characters","S017.3":"'why does this matter?' pivot question, ~25 characters","S021.3":"final takeaway sentence, one line of ~40 characters","S009.5":"first follow-up question, starts with an ellipsis, sits at right-of-centre","S009.6":"second follow-up question, replaces the first and sits lower-left","S009.0":"formula build step 1: a single term near upper centre","S009.1":"formula build step 2: adds a plus sign and a second term","S009.2":"formula build step 3: adds an equals sign and a result word","S005.5":"first quoted keyword beside the seated character","S005.6":"second quoted keyword stacked under the first","S010.0":"black hold #1: spoken set-up line over a blank frame","S012.0":"black hold #2: spoken reveal set-up over a blank frame","S014.0":"black hold #3: spoken hand-off into the explainer segment","S017.1":"second handwritten line under the wordmark, plain-language gloss"}
recs=[];missing=[]
for i,s in enumerate(st):
    sid=s['visual_state_id'];o=obj[sid];au=AUTH.get(sid)
    if au is None: missing.append(sid);continue
    words,mp,low=lag(sid)
    ent=bvrows[i-1] if i>0 else None;ex=bvrows[i] if i<len(bvrows) else None
    sheetS=f"frames/state_sheet_{i//6+1:02d}.jpg"
    neg=round(1-o['fg_fraction'],4)
    subs=[]
    if 'micro_event_frame' in o: subs=[f"sub-state split at f{o['micro_event_frame']} (pts {round((o['micro_event_frame']+1)/30,4)}): see intra_state_events.csv"]
    fam=au['f']
    rec=dict(
      state_id=sid,shot_id=s['shot_id'],start_frame=o['start_frame'],end_frame=o['end_frame'],n_frames=o['n_frames'],start_pts=o['start_pts'],end_pts=o['end_pts'],duration_s=o['dur_s'],
      frame_refs=f"entry f{o['start_frame']} viewed in {('v2/boundary_sheet_%02d.jpg'%sheet_ev(i)) if ent else 'frames/first_last.jpg'}; exit f{o['end_frame']} viewed in {('v2/boundary_sheet_%02d.jpg'%sheet_ev(i+1)) if ex else 'frames/first_last.jpg'}; mid f{o['mid_frame']} viewed in {sheetS}",
      objects_and_positions=au['o'],measured_blobs_norm_bbox=(json.dumps(o['blobs']) if o['blobs'] else 'NONE (solid field; 0 content blobs measured)'),pose_expression=(au['p'] if len(au['p'])>8 else f"no character in frame ({FAM[fam]} state); subject is: {au['h']}"),art_direction=f"{FAM[fam]} ({fam}); flat marker-doodle on {o['bg']} field; third-party/UI material as rectangular cut-outs where present",
      composition_negative_space=f"non-background content {round(o['fg_fraction']*100,2)}% of pixels; negative space {round(neg*100,1)}%; content centroid {o['centroid']}",
      typography_text=f"visible_text: {s['visible_text']} | {au['t']}",colors=f"bg {o['bg']}; palette {json.dumps(o['palette'])}; max contrast vs bg {o['max_contrast_vs_bg']}:1",
      hierarchy_focal=(au['h'] if len(au['h'])>8 else 'single line of text is the whole hierarchy'),camera_framing='static frontal 2D; no camera motion (MEASURED)',motion_or_hold=f"static hold {o['n_frames']} frames; no in-state motion"+(" except sub-state element entry" if subs else ""),
      entry_transition=(f"{ent['classification']} at f{ent['change_start_frame']}-{ent['change_end_frame']} ({ent['change_start_pts']} s)" if ent else 'start of video (f0)'),
      exit_transition=(f"{ex['classification']} at f{ex['change_start_frame']}-{ex['change_end_frame']} ({ex['change_start_pts']} s)" if ex else 'end of video (f8337)'),
      story_purpose=au['u'],narration_asr=words if words else '(no ASR words starting in interval)',asr_status=f"ASR_UNCERTIFIED small.en; mean word prob {mp}; words<0.5 prob: {low}",
      attention_hypothesis='INFERRED: '+au['a'],retention_claim='NONE (no retention data; hypotheses only)',continuity=au['c'],sub_state_events=';'.join(subs),
      reconstruction_requirement=au['r'],style_family=fam,
      original_prompt=f"[STYLE] {au['g']}. Role: {ROLE.get(sid,FAM[fam])}. Layout: content blocks {len(o['blobs'])}, main block x {o['blobs'][0][0] if o['blobs'] else 0:.2f}-{o['blobs'][0][2] if o['blobs'] else 0:.2f}, y {o['blobs'][0][1] if o['blobs'] else 0:.2f}-{o['blobs'][0][3] if o['blobs'] else 0:.2f}; content covers {round(o['fg_fraction']*100,2)}% of the frame, centroid {o['centroid']}; hold {o['dur_s']} s; background {o['bg']}. [NEG] {NEG}",original_prompt_id=f"P-{sid}",
      verification_status='ENTRY/EXIT/MID FRAMES VIEWED; description OBSERVED; purpose/attention INFERRED; small-text items flagged UNVERIFIED in typography_text where marked')
    recs.append(rec)
assert not missing,missing
with open('v2/state_spec_76.csv','w',newline='') as f:
    q=csv.DictWriter(f,fieldnames=list(recs[0]));q.writeheader();q.writerows(recs)
with open('v2/state_spec_76.md','w') as f:
    f.write("# 76-state visual specification — o3FQcd91MIs (FORENSIC description of the SOURCE)\n\nEach record separates OBSERVED/MEASURED facts from INFERRED interpretation. Prompts for the new original production are in `original_prompts.md` (no source IP). Positions in 'objects_and_positions' are approximate verbal estimates from viewed frames; `measured_blobs_norm_bbox` is the computed layout.\n\n")
    for r in recs:
        f.write(f"## {r['state_id']}  ·  {r['duration_s']} s  ·  f{r['start_frame']}–f{r['end_frame']} ({r['n_frames']} frames)  ·  pts {r['start_pts']}–{r['end_pts']}\n")
        for k in ['shot_id','frame_refs','objects_and_positions','measured_blobs_norm_bbox','pose_expression','art_direction','composition_negative_space','typography_text','colors','hierarchy_focal','camera_framing','motion_or_hold','entry_transition','exit_transition','story_purpose','narration_asr','asr_status','attention_hypothesis','retention_claim','continuity','sub_state_events','reconstruction_requirement','verification_status']:
            if r[k]: f.write(f"- **{k}**: {r[k]}\n")
        f.write("\n")
with open('v2/original_prompts.md','w') as f:
    f.write("# Original-production prompts (one per state) — NO source characters, logos, photos, brand names or script\n\n**STYLE anchor (prefix every prompt):** "+STYLE+"\n\n**Negative:** "+NEG+"\n\nPlaceholders: LEAD = your new protagonist, FOIL = your second character. Replace every 'fictional' item with your own original asset.\n\n")
    for r in recs:
        f.write(f"### {r['original_prompt_id']} ({r['style_family']}, {r['duration_s']} s hold, entry: {r['entry_transition'].split(' at ')[0]})\n{r['original_prompt'].replace('[STYLE]','').replace('[NEG]','NEG:')}\n\nReconstruction: {r['reconstruction_requirement']}\n\n")
print(len(recs),'records;',len(bvrows),'boundary rows;',len(mrows),'micro')
