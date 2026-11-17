# Episode discovery: groups active frames (global OR localized high-contrast) into episodes; classifies each.
import pandas as pd, numpy as np, json
d=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv')
n=len(d)
fr=d.changed_frac_thr10_320.values; p6=d.px_diff_ge6.values; p12=d.px_diff_ge12.values; p150=d.px_diff_ge150.values
mx=d.max_abs_diff.values; ef=d.edge_fraction.values; bb=d.bbox_area.values; pict=d.pict.values
GLOBAL=fr>=0.002
codec=(pict=='I')&(ef>=0.85)&(p150<34)&(mx<130)&(fr<0.02)
LOCAL=(p12>=675)&(p150>=90)&~codec    # localized contrast change at full-res
act=(GLOBAL|LOCAL)&~codec
# episodes with gap <=2 frames
eps=[];s=None;last=None
for i in range(1,n):
    if act[i]:
        if s is not None and i-last<=3: last=i
        else:
            if s is not None: eps.append((s,last))
            s=i;last=i
if s is not None: eps.append((s,last))
rows=[]
for k,(a,b) in enumerate(eps,1):
    seg=slice(a,b+1);L=b-a+1
    peak=float(fr[seg].max());tot=float(fr[seg].sum());mxb=int(bb[seg].max());pk150=int(p150[seg].max())
    if L<=2:
        if peak>=0.60: cl='HARD_REPLACE_FULL'
        elif peak>=0.15: cl='LARGE_PARTIAL_REPLACE'
        elif peak>=0.02: cl='PARTIAL_OR_ADDITIVE'
        else: cl='SMALL_LOCAL_CHANGE'
    else:
        if peak>=0.15 and tot/L>=0.05: cl='GLOBAL_MOTION_OR_TRANSITION'
        elif tot/L>=0.01: cl='REGIONAL_ANIMATION'
        else: cl='LOCAL_ANIMATION'
    rows.append(dict(ep=k,start=a,end=b,n=L,pts_start=float(d.pts_time[a]),pts_end=float(d.pts_time[b]),peak_frac=round(peak,4),mean_frac=round(tot/L,4),peak_n150=pk150,max_bbox=mxb,cls=cl,has_I=bool((pict[seg]=='I').any())))
E=pd.DataFrame(rows);E.to_csv('tables/episodes_v2.csv',index=False)
print(len(E),'episodes');print(E.cls.value_counts());print('codec-flagged I frames',int(codec.sum()),'of',int((pict=='I').sum()))
print(E.groupby('cls').n.describe()[['mean','max']])
