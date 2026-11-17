import pandas as pd, cv2, json, os
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-31-0ll9rEtoRrs-deep-ct-scan'
SRC="/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/The World's Safest Market Is Breaking - Casual Finance (720p, h264).mp4"
st=pd.read_csv(f'{R}/tables/states_machine.csv'); cc=pd.read_csv(f'{R}/tables/candidates_classified.csv'); sd=pd.read_csv(f'{R}/tables/scenedetect_candidates.csv')
starts=st.start.values
cuts=sd.start_frame.values[1:]
un=[int(c) for c in cuts if min(abs(starts-c))>2]
print('unmatched',len(un))
# dispute strips
need={}
for c in un:
    for f in (c-2,c,c+2): need.setdefault(max(f,0),[]).append(c)
cap=cv2.VideoCapture(SRC); i=0; got={}
while True:
    ok,fr=cap.read()
    if not ok: break
    if i in need: got[i]=cv2.resize(fr,(480,270))
    i+=1
print('decoded',i)
rows=[]
for k,c in enumerate(un,1):
    did=f'SD{k:03d}'
    strip=cv2.hconcat([got[max(c-2,0)],got[c],got[c+2]])
    cv2.putText(strip,f'{did} cut@f{c} pre-2 | cut | post+2',(8,20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    cv2.imwrite(f'{R}/disputes/{did}.jpg',strip,[cv2.IMWRITE_JPEG_QUALITY,80])
    rows.append((did,c,round((c+1)/24,4)))
dis=pd.DataFrame(rows,columns=['id','cut_frame','pts_s']); dis.to_csv(f'{R}/tables/disputes_scenedetect.csv',index=False)
# shards by frame range: 8 shards equal in candidates
cc=cc.sort_values('start').reset_index(drop=True)
N=10; per=len(cc)//N+1
for s in range(N):
    d=f'{R}/agents/shard_{s+1}'; os.makedirs(d,exist_ok=True)
    c=cc.iloc[s*per:(s+1)*per]; lo=int(c.start.min()); hi=int(c.start.max()) if s<N-1 else 10**9
    lo=0 if s==0 else lo
    sts=st[(st.start>=lo)&(st.start<=hi)]
    ds=dis[(dis.cut_frame>=lo)&(dis.cut_frame<=hi)]
    c.to_csv(f'{d}/candidates.csv',index=False); sts.to_csv(f'{d}/states.csv',index=False); ds.to_csv(f'{d}/disputes.csv',index=False)
    print(s+1,len(c),len(sts),len(ds),lo,hi)
