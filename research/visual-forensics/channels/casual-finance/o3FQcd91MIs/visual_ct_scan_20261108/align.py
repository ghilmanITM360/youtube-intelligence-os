import json,csv,statistics as S,bisect
w=json.load(open('audio/o3FQ_16k.json'))
words=[(x['start'],x['end'],x['word'].strip(),x.get('probability',0)) for s in w['segments'] for x in s['words']]
starts=[x[0] for x in words]
ev=list(csv.DictReader(open('visual_event_ledger.csv')))
rows=[];offs=[]
for e in ev:
    t=float(e['start_pts_seconds']); i=bisect.bisect_left(starts,t)
    c=[j for j in (i-1,i) if 0<=j<len(words)]
    j=min(c,key=lambda j:abs(words[j][0]-t))
    off=round(t-words[j][0],3); offs.append(off)
    inside=any(a<=t<=b for a,b,_,_ in words[max(0,j-2):j+3])
    rel='ON_WORD_START(|lag|<=0.1s)' if abs(off)<=0.1 else ('VISUAL_BEFORE_WORD' if off<0 else ('DURING_WORD' if inside else 'AFTER_WORD_START'))
    ctx=' '.join(x[2] for x in words[max(0,j-3):j+4])
    rows.append(dict(video_id='o3FQcd91MIs',event_id=e['event_id'],audio_source='local ASR openai-whisper small.en (word timestamps)',audio_listening_status='ASR_UNCERTIFIED - NO HUMAN LISTENING',
      phrase_or_sound=f"[{words[j][2]}] …{ctx}…",audio_start_pts=round(words[j][0],3),audio_end_pts=round(words[j][1],3),visual_start_pts=t,visual_end_pts=e['end_pts_seconds'],
      lead_lag_seconds=off,timestamp_method='visual PTS (frame-exact) minus nearest ASR word start',confidence='MEDIUM (ASR word timing +/-~0.1-0.2 s; visual timing exact)',limitations=rel+'; ASR text unverified; no audio event/music/SFX claim'))
with open('audio_visual_alignment.csv','w',newline='') as f:
    q=csv.DictWriter(f,fieldnames=list(rows[0]));q.writeheader();q.writerows(rows)
a=sorted(offs);n=len(a)
print('events',n,'median lag',S.median(a),'p10',a[n//10],'p90',a[9*n//10])
print('|lag|<=0.1:',sum(abs(x)<=0.1 for x in a),'|lag|<=0.2:',sum(abs(x)<=0.2 for x in a),'visual before word >0.2:',sum(x<-0.2 for x in a))
# compare with base ASR
base=list(csv.DictReader(open('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/02_VIDEO_FORENSICS/o3FQcd91MIs/TRANSCRIPT.csv')))
print('words small.en',len(words),'base',len(base))
bs=[float(x['start_sec']) for x in base]
d=[]
for a_,b_,tx,p in words:
    j=min(range(len(bs)),key=lambda k:abs(bs[k]-a_)) if False else bisect.bisect_left(bs,a_)
    cand=[k for k in (j-1,j) if 0<=k<len(bs)]
    k=min(cand,key=lambda k:abs(bs[k]-a_));d.append(abs(bs[k]-a_))
print('word-start agreement small.en vs base: median',round(S.median(d),3),'p90',round(sorted(d)[9*len(d)//10],3))
json.dump({'text':w['text']},open('audio/small_en_text.json','w'))
print(w['text'][:400])
