import pandas as pd, numpy as np, re, json
W=pd.read_csv('asr/words_small_en.csv'); B=pd.read_csv('BOUNDARY_VERIFICATION.csv').fillna('')
V=pd.read_csv('VISUAL_STATES.csv').fillna('')
starts=W.start.values; words=W.word.values
b=B[B.kind=='STATE_BOUNDARY'].copy()
rows=[]
for r in b.itertuples():
    t=r.pts_start; i=np.argmin(np.abs(starts-t)); lag=t-starts[i]  # visual time minus word onset (+ = visual after word)
    ctx=' '.join(words[max(0,i-3):i+4])
    num=bool(re.search(r'\d|percent|million|billion|trillion|%|\$',ctx))
    rows.append(dict(event_id=r.event_id,visual_time_s=t,nearest_word=words[i],word_onset_s=round(float(starts[i]),2),lag_s=round(float(lag),3),abs_lag_s=round(abs(float(lag)),3),context_unverified=ctx,numeric_context=num,
        final_type=r.final_type,visual_desc=r.reviewer_description[:160],asr_status='ASR_ONLY_NOT_AUDIO_VERIFIED',timing_label='MEASURED_OFFSET_TO_ASR_WORD_ONSET',intent_label='NOT_CLAIMED'))
A=pd.DataFrame(rows);A.to_csv('audio_visual_alignment.csv',index=False)
lag=A.lag_s.values;al=A.abs_lag_s.values
st={'events':len(A),'median_lag_s':round(float(np.median(lag)),3),'mean_lag_s':round(float(lag.mean()),3),'p10':round(float(np.percentile(lag,10)),3),'p90':round(float(np.percentile(lag,90)),3),
 'within_0.10s':int((al<=0.10).sum()),'within_0.25s':int((al<=0.25).sum()),'within_0.50s':int((al<=0.50).sum()),'beyond_0.5s':int((al>0.5).sum()),
 'visual_before_word_onset':int((lag<-0.04).sum()),'visual_after_word_onset':int((lag>0.04).sum()),'numeric_context_events':int(A.numeric_context.sum()),
 'numeric_context_median_abs_lag':round(float(np.median(A[A.numeric_context].abs_lag_s)),3)}
# chance baseline: random times
rng=np.random.default_rng(1);rt=rng.uniform(0,913,5000);rl=np.array([np.min(np.abs(starts-t)) for t in rt])
st['chance_median_abs_lag_to_nearest_word_s']=round(float(np.median(rl)),3);st['chance_within_0.10s_pct']=round(float((rl<=0.10).mean()*100),1);st['observed_within_0.10s_pct']=round(st['within_0.10s']/len(A)*100,1)
# speech vs silence at boundaries: any word active
# pause detection
gaps=starts[1:]-W.end.values[:-1];st['asr_pauses_gt_1s']=int((gaps>1).sum())
json.dump(st,open('asr/alignment_stats.json','w'),indent=1);print(st)
