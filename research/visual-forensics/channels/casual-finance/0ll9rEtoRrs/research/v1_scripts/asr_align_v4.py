import csv,json,random,bisect,statistics as st
S=sorted(csv.DictReader(open('integrated_v4/reviewed_states_v4.csv')),key=lambda s:int(s['start']))
T=list(csv.DictReader(open('phaseB/historical_asr/SENTENCES.csv')))
FPS=24
ss=[int(s['start'])/FPS for s in S]; se=[(int(s['end'])+1)/FPS for s in S]
rows=[]
for t in T:
    a,b=float(t['start_sec']),float(t['end_sec'])
    ov=[(s['id'],round(min(b,e)-max(a,x),2)) for s,x,e in zip(S,ss,se) if min(b,e)>max(a,x)]
    gap=round((b-a)-sum(o for _,o in ov),2)
    first=ov[0][0] if ov else ''
    rows.append(dict(sentence_id=t['sentence_id'],start_sec=a,end_sec=b,text=t['text'],n_states_overlapping=len(ov),states=' '.join(i for i,_ in ov),dominant_state=max(ov,key=lambda x:x[1])[0] if ov else '',unowned_overlap_sec=max(gap,0),has_number=t['has_number'],is_question=t['is_question'],min_word_prob=t['min_word_prob'],alignment_basis='ASR_WHISPER_BASE_TIME_OVERLAP_NOT_HUMAN_LISTENED'))
w=csv.DictWriter(open('phaseB/asr_sentence_to_state_v4.csv','w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
# does a state start fall near a sentence start? vs shuffled baseline
starts=sorted(ss); tol=0.25
def hit(sent_starts):
    return sum(1 for x in sent_starts if starts[max(bisect.bisect_left(starts,x)-1,0):bisect.bisect_left(starts,x)+1] and min(abs(x-y) for y in starts[max(bisect.bisect_left(starts,x)-1,0):bisect.bisect_left(starts,x)+1])<=tol)/len(sent_starts)
obs=hit([float(t['start_sec']) for t in T])
random.seed(1);L=24298/FPS
base=[hit([random.uniform(0,L) for _ in T]) for _ in range(500)]
res=dict(sentences=len(T),states=len(S),tol_sec=tol,sentence_start_within_tol_of_state_start=round(obs,3),shuffled_baseline_mean=round(st.mean(base),3),baseline_p95=round(sorted(base)[474],3),
 sentences_overlapping_gt1_state=sum(1 for r in rows if r['n_states_overlapping']>1),median_states_per_sentence=st.median(r['n_states_overlapping'] for r in rows),
 sentences_with_number=sum(r['has_number']=='True' for r in rows),total_asr_words=sum(int(t['word_count']) for t in T),asr_engine='WHISPER_BASE_WORD_TIMESTAMPS (historical 2026-10-12 pass)',listened='NO')
json.dump(res,open('phaseB/asr_alignment_stats_v4.json','w'),indent=1);print(res)
