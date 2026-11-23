# Extract candle bodies (x, top, bottom, colour) from ref f1212 (no arrow/label) -> candles.json (data shape only; own style when rendered)
import json,sys
import numpy as np
from PIL import Image
im=np.array(Image.open(sys.argv[1]).convert('RGB')).astype(int)
r,g,b=im[...,0],im[...,1],im[...,2]
red=(r>150)&(g<110)&(b<110)&(r-g>70); grn=(g>100)&(g-r>40)&(g-b>-10)&(r<110)
sub=slice(740,1180); xs0,xs1=235,800
cols=[]
for x in range(xs0,xs1):
    for nm,m in (('r',red),('g',grn)):
        ys=np.where(m[sub,x])[0]
        if len(ys): cols.append((x,nm,int(ys.min())+740,int(ys.max())+740,len(ys)))
# group contiguous columns of same colour with overlapping y
runs=[]
for x,nm,t,bm,n in cols:
    for rn in runs:
        if rn['c']==nm and x-rn['x1']<=1 and not(bm<rn['t']-3 or t>rn['b']+3): rn['x1']=x; rn['t']=min(rn['t'],t); rn['b']=max(rn['b'],bm); rn['n']+=n; break
    else: runs.append(dict(c=nm,x0=x,x1=x,t=t,b=bm,n=n))
runs=[q for q in runs if q['n']>=6]
runs.sort(key=lambda q:q['x0'])
print(len(runs)); json.dump(runs,open('candles.json','w'))
print(runs[:5],runs[-3:])
