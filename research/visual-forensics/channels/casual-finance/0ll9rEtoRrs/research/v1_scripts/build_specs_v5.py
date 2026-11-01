import csv,json,collections
rd=lambda p:list(csv.DictReader(open(p)))
S=rd('integrated_v5/reviewed_states_v5.csv');C=rd('integrated_v5/reviewed_candidates_v5.csv');A=rd('phaseB/asr_sentence_to_state_v4.csv');CP={c['composition_id']:c for c in rd('integrated_v5/compositions_v5.csv')};U=rd('integrated_v5/unowned_intervals_v5.csv')
FAM_ASSET={'F1':'one original presenter figure (new design, 2-3 poses)','F2':'original presenter plus one original prop','F3':'3-6 original icons/props on blank canvas','F4':'licensed or self-made document/screen capture frame','F5':'original presenter beside an original or licensed data capture','F6':'original chart built from cited public data','F7':'original text card','F8':'self-made dark-UI mock capture','F9':'one original full-bleed drawn scene','F10':'original title/end card','F11':'composite of original drawings and licensed captures'}
asr=collections.defaultdict(list)
for a in A:
    for sid in a['states'].split():asr[sid].append((a['sentence_id'],a['start_sec'],a['end_sec']))
def evs(s):
    a,b=int(s['start']),int(s['end'])
    r=[c for c in C if a<=int(c['start'])<=b and c['final_type'] not in('NOT_A_CHANGE','CODEC_ARTIFACT')]
    return sorted(r,key=lambda c:int(c['start']))
gaps=[(int(u['start']),int(u['end']),u) for u in U]
out=[]
for s in S:
    e=evs(s);a,b=int(s['start']),int(s['end'])
    fid=(s['family'].split() or ['F5'])[0]; s['family']=s['family'] or 'F5 screenshot+character (assigned from own frame review)'
    seq='; '.join(f"f{c['start']}:{c['final_type']}" for c in e[:12])+(' ...' if len(e)>12 else '')
    ver=collections.Counter(c.get('smp_status','FIRST_PASS_ONLY') if c['sp_decision']=='NOT_SECOND_PASSED' else 'SECOND_PASS_'+c['sp_decision'] for c in e)
    adj=[g[2]['gap_id']+':'+(g[2]['rr_class'] or g[2]['sp_class']) for g in gaps if g[1]==a-1 or g[0]==b+1]
    unver=[]
    if s['pass']!='SECOND_PASS_VERIFIED' and s['pass'].startswith('FIRST'):unver.append('state description first-pass only')
    if s['unreadable_text']:unver.append('unreadable text: '+s['unreadable_text'][:60])
    if s['id'] in('S0466P',) or s['parent_id']:unver.append('split child; description from own frame review')
    out.append(dict(state_id=s['id'],composition_id=s['composition_id'],start_frame=a,end_frame=b,pts_start=s['pts_start'],pts_end=s['pts_end'],duration_s=s['duration_s'],family=s['family'],
      visual_purpose=s['story_function'],source_observation=(s['corr_desc'] or s['objects'])[:400],background=s['background'][:120],editable_layers_observed=s['objects'][:300],hierarchy=s['hierarchy'][:160],
      layer_entry_sequence_measured_frames=seq or 'NONE_RECORDED',motion_type=s['camera_motion'],animation_timing_basis='MEASURED_FRAME_INDEXES_ONLY; easing=UNAVAILABLE; layer_coordinates=UNAVAILABLE_UNLESS_IN_SOURCE_OBSERVATION',
      narration_sentences=' '.join(x[0] for x in asr.get(s['id'],[])),narration_basis='ASR_NOT_LISTENED' if asr.get(s['id']) else 'NONE',
      required_original_assets=FAM_ASSET.get(fid,'TO_BE_DESIGNED'),colour_values='UNAVAILABLE_NOT_SAMPLED',typeface='UNAVAILABLE_NOT_IDENTIFIED',
      reference_description_not_to_copy=s['recon'][:350],original_image_prompt_template=f"Create an ORIGINAL flat hand-drawn whiteboard-style illustration on a white canvas: {FAM_ASSET.get(fid,'new composition')}; purpose: {s['story_function'][:120]}. Use a new character design and new props; do not copy the source video's characters, screenshots or text.",
      animation_instructions='Build as separate layers; reveal them in the order given by layer_entry_sequence_measured_frames converted to your own timing; hold the final layout until the next composition.',
      adjacent_unowned_intervals=' '.join(adj),composition_absorbed_gap_ids=CP[s['composition_id']]['absorbed_gap_ids'],composition_full_span_frames=CP[s['composition_id']]['full_span_frames'],candidate_verification=json.dumps(dict(ver)),reviewer_confidence=s['confidence'],unverified_properties=' | '.join(unver) or 'NONE_RECORDED',
      evidence_paths=f"integrated_v5/reviewed_states_v5.csv#{s['id']}; source frames {a}-{b} (decode source_manifest.json source_path)"))
w=csv.DictWriter(open('production/per_state_specs_v5.csv','w',newline=''),fieldnames=out[0].keys());w.writeheader();w.writerows(out);print(len(out))
