import pandas as pd, numpy as np, cv2, os, json
S=pd.read_csv('tables/states_machine.csv').fillna(''); E=pd.read_csv('tables/episodes_classified.csv')
K=7; per=int(np.ceil(len(S)/K)); manifest=[]
for k in range(K):
    d=f'agents/shard_{k+1}'; os.makedirs(d+'/state_sheets',exist_ok=True)
    s=S.iloc[k*per:(k+1)*per]; f0,f1=int(s.start.iloc[0]),int(s.end.iloc[-1])
    lo=f0 if k>0 else 0; hi=int(S.iloc[(k+1)*per].start) if k<K-1 else 10**9
    ep=E[(E.start>=lo)&(E.start<hi)]
    cols=['ep','kind','cls','start','end','n','pts_start','pts_end','peak_frac','net_changed_frac','net_bbox','content_iou','sheet','sheet_row']
    ep[cols].to_csv(d+'/machine_episodes.csv',index=False)
    s[['state_id','shot_id_inferred','start','end','n_frames','pts_start','pts_end','duration_s','entry_ep','exit_ep','micro_events','motion_intervals']].to_csv(d+'/machine_states.csv',index=False)
    # state sheets 3x2 from rep images
    tiles=[]
    for r in s.itertuples():
        im=cv2.imread(r.rep_image); 
        if im is None: im=np.zeros((360,640,3),np.uint8)
        cv2.rectangle(im,(0,0),(640,22),(255,255,255),-1)
        cv2.putText(im,f"{r.state_id} f{r.start}-{r.end} {r.pts_start:.2f}-{r.pts_end:.2f}s ({r.duration_s:.2f}s)",(4,16),cv2.FONT_HERSHEY_SIMPLEX,0.55,(0,0,200),1)
        tiles.append(im)
    for j in range(0,len(tiles),6):
        c=tiles[j:j+6]
        while len(c)<6: c.append(np.full((360,640,3),200,np.uint8))
        cv2.imwrite(f'{d}/state_sheets/ss_{j//6+1:02d}.jpg',np.vstack([np.hstack(c[:3]),np.hstack(c[3:])]),[cv2.IMWRITE_JPEG_QUALITY,82])
    sheets=sorted(set(ep.sheet))
    manifest.append(dict(shard=k+1,states=[s.state_id.iloc[0],s.state_id.iloc[-1]],n_states=len(s),n_episodes=len(ep),frames=[f0,f1],boundary_sheets=sheets,n_state_sheets=(len(s)+5)//6))
    print(k+1,s.state_id.iloc[0],s.state_id.iloc[-1],len(s),len(ep),len(sheets),(len(s)+5)//6)
json.dump(manifest,open('agents/shards.json','w'),indent=1)
