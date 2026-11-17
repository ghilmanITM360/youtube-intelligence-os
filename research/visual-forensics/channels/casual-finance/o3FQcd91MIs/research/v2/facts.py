import csv,json,statistics as S
fr=list(csv.DictReader(open('v2/frame_metrics_fullres.csv')));fm=list(csv.DictReader(open('tables/frame_metrics.csv')))
bv=list(csv.DictReader(open('v2/boundary_verification.csv')));mi=list(csv.DictReader(open('v2/intra_state_events.csv')))
ob=json.load(open('v2/state_objective.json'));al=list(csv.DictReader(open('v2/audio_visual_alignment_v2.csv')))
ep=json.load(open('tables/episodes.json'))
evf=set()
for e in bv:
    for k in range(int(e['change_start_frame'])-1,int(e['change_end_frame'])+2): evf.add(k)
I=[int(x['frame']) for x in fr if x['pict']=='I'];per=[i for i in I if i not in evf and i>0]
perblip=[i for i in per if int(fr[i]['px_diff_ge6'])>0]
pe=[float(fr[i]['edge_fraction']) for i in perblip]
evb=[(int(e['change_start_frame']),int(e['change_end_frame'])) for e in bv]
unm=[e for e in ep if not any(abs(e['start_frame']-a)<=1 and abs(e['end_frame']-b)<=1 for a,b in evb)]
micro_frames={int(m['frame']) for m in mi}
codec=[e for e in unm if e['start_frame'] not in micro_frames]
L=[float(r['lead_lag_seconds']) for r in al]
pts_ok=all(abs(float(fm[i]['pts_time'])-(i+1)/30)<1e-5 for i in range(len(fm)))
F=dict(total_frames=len(fm),pts_equals_index_plus1_over_30=pts_ok,
 boundary_events=len(bv),single_frame_boundaries=sum(1 for e in bv if e['change_frames']=='1'),black_dip_events=sum(1 for e in bv if e['classification'].startswith('BLACK_DIP')),
 black_dip_frames=[7233,7234],black_dip_pts=[round(7234/30,4),round(7235/30,4)],
 intra_state_events=len(mi),content_change_events=len(bv)+len(mi),states=len(ob),stable_composition_intervals=len(ob)+len(mi),shots=len({s['shot_id'] for s in csv.DictReader(open('visual_states.csv'))}),
 measured_episodes=len(ep),episodes_matching_boundaries=len(ep)-len(unm),episodes_unmatched=len(unm),codec_episodes=len(codec),
 iframes_total=len(I),periodic_iframes_outside_events=len(per),periodic_iframes_with_pixel_diff=len(perblip),periodic_edge_fraction_median=round(S.median(pe),3),
 periodic_max_abs_diff_max=max(int(fr[i]['max_abs_diff']) for i in per),micro_event_max_abs_diff_min=min(int(m['max_abs_diff']) for m in mi),
 classification_counts={c:sum(1 for e in bv if e['classification']==c) for c in sorted({e['classification'] for e in bv})},
 asr_events=len(al),asr_median_lag=round(S.median(L),3),asr_within_0p2=sum(abs(x)<=0.2 for x in L),asr_outside_0p2=sum(abs(x)>0.2 for x in L),
 asr_outside_both_runs=sum(1 for r in al if r['asr_agreement'].startswith('BOTH_OUTSIDE')),asr_outliers_disagree=sum(1 for r in al if r['outside_0p2_small_en']=='True' and r['asr_agreement'].startswith('ASR_DISAGREE')),
 state_frames_total=sum(v['n_frames'] for v in ob.values()),
 min_state_frames=min(v['n_frames'] for v in ob.values()),median_state_s=round(S.median(v['dur_s'] for v in ob.values()),3))
json.dump(F,open('v2/key_facts.json','w'),indent=1);print(json.dumps(F,indent=1))
