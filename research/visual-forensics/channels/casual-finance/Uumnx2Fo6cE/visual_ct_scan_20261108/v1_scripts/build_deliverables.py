import pandas as pd, numpy as np, json, re, os
os.chdir('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-Uumnx2Fo6cE-deep-ct-scan')
V=pd.read_csv('VISUAL_STATES.csv').fillna('');B=pd.read_csv('BOUNDARY_VERIFICATION.csv').fillna('');M=pd.read_csv('MOTION_INTERVALS.csv').fillna('');I=pd.read_csv('INTRA_STATE_EVENTS.csv').fillna('')
A=pd.read_csv('audio_visual_alignment.csv').fillna('');st=json.load(open('asr/alignment_stats.json'));ss=json.load(open('asr/sentence_alignment_stats.json'))
# --- shots (INFERRED) ---
sh=V.groupby('shot_id_inferred').agg(first_state=('state_id','first'),last_state=('state_id','last'),n_states=('state_id','count'),start_frame=('start_frame','min'),end_frame=('end_frame','max'),pts_start=('pts_start','min'),pts_end=('pts_end','max')).reset_index()
sh['duration_s']=((sh.end_frame-sh.start_frame+1)/24).round(3);sh['label']='INFERRED (reviewer-defined: whole subject/scene replaced); NOT verified fact'
sh.to_csv('tables/shots_inferred.csv',index=False)
cand=B[(B.shot_boundary_inferred.isin(['YES','AMBIGUOUS']))][['event_id','kind','start_frame','pts_start','final_type','shot_boundary_inferred','confidence','evidence_sheet']].copy()
cand['source']='REVIEWER_FLAG';sd=pd.read_csv('tables/scenedetect_content20.csv').iloc[1:]
sdc=pd.DataFrame(dict(event_id=['SD%03d'%k for k in sd.scene],kind='SCENEDETECT_CONTENT20',start_frame=sd.start_frame,pts_start=sd.start_s,final_type='',shot_boundary_inferred='CANDIDATE_ONLY',confidence='',evidence_sheet='',source='PYSCENEDETECT_0.7.2'))
pd.concat([cand,sdc]).sort_values('start_frame').to_csv('SHOT_CANDIDATES.csv',index=False)
# --- state-by-state md ---
L=['# STATE-BY-STATE VISUAL FORENSICS — Uumnx2Fo6cE','',f'{len(V)} visual states (stable composition intervals between state-changing events). Frames are 0-based decode indices; PTS=(i+1)/24 s. SOURCE_FORENSIC_DESCRIPTION only; original-production text is in PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json and ORIGINAL_RECONSTRUCTION_BLUEPRINT.md.','',
 'Labels: OBSERVED = seen in decoded frames (tiles 640x360 / 256x144 — small text not guaranteed readable); INFERRED = reviewer interpretation; narration = ASR_ONLY_NOT_AUDIO_VERIFIED. Every state was reviewed twice (first pass + independent second pass).','']
ev_by=I.groupby('parent_state').apply(lambda d:'; '.join(f"{r.event_id} ({r.type}, f{r.start_frame}) {r.description}" for r in d.itertuples())).to_dict()
for r in V.itertuples():
    L+= [f'## {r.state_id} — f{r.start_frame}-{r.end_frame} ({r.pts_start:.3f}-{r.pts_end:.3f} s, {r.n_frames} frames, {r.duration_s:.2f} s) — shot {r.shot_id_inferred} (inferred) — {r.family}',
     f'- **Evidence:** {r.evidence_image}; entry {r.entry_episode or "start of video"}, exit {r.exit_episode or "end of video"}; second review: {r.second_review_match}',
     f'- **Objects/placement (OBSERVED):** {r.objects}',f'- **Background:** {r.background}',f'- **Illustration:** {r.illustration}',f'- **Typography:** {r.typography}',
     f'- **Readable text:** {r.readable_text or "none"}',f'- **Unreadable/uncertain text:** {r.unreadable_text or "none flagged"}',
     f'- **Palette (MEASURED, top-5 k-means of representative frame):** {r.palette_measured}',f'- **Hierarchy:** {r.hierarchy}',f'- **Camera/motion:** {r.camera_motion}; **entry/exit:** {r.entry_exit}',
     f'- **Narration (ASR, unverified):** {r.asr_text_unverified or "—"}',f'- **Story function (INFERRED):** {r.story_function}',f'- **Continuity:** {r.continuity}',
     f'- **Confidence:** {r.confidence}; **evidence split:** {r.evidence}']
    if r.state_id in ev_by: L.append(f'- **Intra-state events:** {ev_by[r.state_id]}')
    if r.intra_motion: L.append(f'- **Intra-state motion intervals:** {r.intra_motion}')
    L.append('')
open('STATE_BY_STATE_VISUAL_FORENSICS.md','w').write('\n'.join(L))
# --- per-state reconstruction JSON ---
ev_l=I.groupby('parent_state').apply(lambda d:[dict(event=r.event_id,frame=int(r.start_frame),type=r.type,observed=r.description,animation_instruction=f"Recreate as a {r.type.lower().replace('_',' ')} beat at frame offset {int(r.start_frame)-int(V[V.state_id==d.name].start_frame.iloc[0])} within the state, hard-cut (single frame) unless noted") for r in d.itertuples()]).to_dict()
out=[]
for r in V.itertuples():
    out.append(dict(state_id=r.state_id,SOURCE_FORENSIC_DESCRIPTION=dict(evidence_image=r.evidence_image,frames=[int(r.start_frame),int(r.end_frame)],pts_s=[float(r.pts_start),float(r.pts_end)],objects=r.objects,illustration=r.illustration,typography=r.typography,readable_text=r.readable_text,unreadable_text=r.unreadable_text,palette_measured=r.palette_measured,entry_episode=r.entry_episode,exit_episode=r.exit_episode,confidence=r.confidence,second_review=r.second_review_match),
      ORIGINAL_PRODUCTION_INSTRUCTIONS=dict(style_family=r.family,shot_inferred=r.shot_id_inferred,duration_frames_24fps=int(r.n_frames),build=r.recon,image_generation_prompt=r.prompt,intra_state_beats=ev_l.get(r.state_id,[]),continuity_requirement=r.continuity,rights='original assets only; no source characters, screenshots, logos, text or script')))
json.dump(out,open('PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json','w'),indent=1)
# --- ASR alignment md ---
big=B[(B.kind=='STATE_BOUNDARY')&B.measured_class.isin(['HARD_REPLACE_FULL','LARGE_PARTIAL_REPLACE'])]
num=A[A.numeric_context==True].sort_values('abs_lag_s').head(12)
T=['# ASR ↔ VISUAL ALIGNMENT — Uumnx2Fo6cE','','**Status: PROVISIONAL_ASR_ONLY. ASR_ONLY_NOT_AUDIO_VERIFIED. Nobody has listened to the audio; wording and word timing are automated (openai-whisper small.en, local). Human listening NOT_COMPLETED; full audiovisual sign-off BLOCKED.**','',
 '## Method','- Transcript: local Whisper small.en with word timestamps (3,027 words, 196 segments). Cross-check against the registered earlier base-model transcript: 2,964 words matched in sequence, median word-start difference 0.02 s (asr/asr_crosscheck.json).',
 '- Visual event time = PTS of the first changed frame of each of the 370 state-boundary events (MEASURED). Offset = visual time − nearest ASR word onset (negative = visual changes before the word).','- A timing relationship is MEASURED; any claim about editorial intention is NOT made.','',
 '## Result 1 — word-level alignment is not informative (honest null)',f'Speech is dense (~3.3 words/s), so some word onset is always near. Median |offset| {np.median(A.abs_lag_s):.3f} s; {st["within_0.10s"]}/{st["events"]} ({st["observed_within_0.10s_pct"]}%) events lie within 0.10 s of a word onset, versus {st["chance_within_0.10s_pct"]}% for random times (chance baseline, 5,000 draws). That is barely above chance, so word-level offsets must NOT be read as deliberate word-sync.',
 f'Offset distribution: median {st["median_lag_s"]} s, p10 {st["p10"]} s, p90 {st["p90"]} s; {st["visual_before_word_onset"]} events precede the nearest word onset by >0.04 s, {st["visual_after_word_onset"]} follow it.','',
 '## Result 2 — sentence-level alignment is real (MEASURED)',f'Using ASR sentence starts ({ss["sentence_starts"]}): across all state-boundary events {ss["all_within_0p25_pct"]}% fall within 0.25 s of a sentence start (chance {ss["chance_within_0p25_pct"]}%). For the {ss["big_events"]} full/large composition replacements, {ss["big_within_0p25_pct"]}% fall within 0.25 s of a sentence start versus {ss["chance_within_0p25_pct"]}% chance. Large scene changes therefore cluster at ASR sentence starts; small additive changes are spread through sentences (they follow phrases/words).','',
 '## Numerical-claim contexts',f'{st["numeric_context_events"]} state-boundary events have a digit/percent/dollar/million token within ±3 ASR words (median |offset| {st["numeric_context_median_abs_lag"]} s). Closest examples (ASR wording UNVERIFIED):','']
for r in num.itertuples(): T.append(f'- {r.event_id} @ {r.visual_time_s:.3f} s, offset {r.lag_s:+.3f} s, ASR "…{r.context_unverified}…" — visual: {r.visual_desc}')
T+=['','## Silence and pacing','- No ASR pause longer than 1 s exists (asr_pauses_gt_1s = 0): narration is continuous over the whole 913.8 s speech span; visuals change underneath continuous speech.','','## What is NOT claimed','- No human-verified wording, no audible-beat, music or sound-effect analysis (audio not listened to), no editorial-intention claim.','- Per-event rows: audio_visual_alignment.csv (370 rows); per-state ASR text: VISUAL_STATES.csv (asr_text_unverified).']
open('ASR_VISUAL_ALIGNMENT.md','w').write('\n'.join(T))
print('ok',len(sh),'shots')
