# Post-review normalisation (idempotent): confidence rule + enrich terse recon with measured timing/entry/objects
import pandas as pd
V=pd.read_csv('VISUAL_STATES.csv').fillna('');B=pd.read_csv('BOUNDARY_VERIFICATION.csv').fillna('').set_index('event_id')
n1=n2=0
for i,r in V.iterrows():
    if r.confidence=='HIGH' and r.unreadable_text!='': V.at[i,'confidence']='MEDIUM';n1+=1
    if len(r.recon)<60 and 'Timing:' not in r.recon:
        ent=B.loc[r.entry_episode] if r.entry_episode in B.index else None
        entry=f"enters by {ent.final_type.lower().replace('_',' ')} ({ent.reviewer_description.rstrip('.')})" if ent is not None else 'is the opening state'
        V.at[i,'recon']=f"{r.recon.rstrip('.')}. Timing: hold {int(r.n_frames)} frames ({r.duration_s:.2f} s at 24 fps); the state {entry}. Compose with original assets: {r.objects[:220].rstrip('.')}."
        n2+=1
V.to_csv('VISUAL_STATES.csv',index=False);print('confidence downgraded',n1,'recon enriched',n2)
