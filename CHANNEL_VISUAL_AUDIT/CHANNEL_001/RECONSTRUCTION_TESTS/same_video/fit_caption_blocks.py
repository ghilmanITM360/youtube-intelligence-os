import csv,json,os,re,glob,numpy as np
from PIL import Image,ImageFont,ImageDraw
WS=os.path.expanduser('~/YIOS-local-audits/2026-11-08-10nEByVLya0-deep-ct-scan/')
F=ImageFont.truetype('/System/Library/Fonts/Supplemental/Comic Sans MS Bold.ttf',58)
words=[(w['word'].strip(),w['start']) for s in json.load(open(WS+'audio/10nEByVLya0_small_en.json'))['segments'] for w in s['words']]
EV=[int(r['start_frame']) for r in csv.DictReader(open(WS+'caption_event_ledger.csv'))]
WS_=[x[1] for x in words]
d=ImageDraw.Draw(Image.new('RGB',(10,10)))
tl=lambda t:d.textlength(t,font=F)
# ref measures
ref={}
for p in glob.glob('../../FRAME_REFERENCES/10nEByVLya0/*.png'):
    f=int(re.search(r'_f(\d+)',p).group(1)); a=np.array(Image.open(p).convert('L')).astype(int)[1285:1440]<110; ys,xs=np.where(a)
    if len(xs): ref[f]=(xs.max()-xs.min(),ys.min()+1285)
def vis(f,gap,maxw,maxl):
    ev=[e for e in EV if e<=f]
    if not ev: return None
    t=ev[-1]/30+.04; idx=max([i for i,w in enumerate(WS_) if w<=t] or [-1])
    if idx<0: return None
    # blocks from start
    blocks=[[0]]; lines=[[words[0][0]]]
    for i in range(1,len(words)):
        cur=lines[-1]; new=False
        if WS_[i]-WS_[i-1]>gap: new=True
        else:
            if tl(' '.join(cur+[words[i][0]]))>maxw:
                if len(lines)>=maxl: new=True
                else: lines.append([words[i][0]]); blocks[-1].append(i); continue
        if new: blocks.append([i]); lines=[[words[i][0]]]
        else: cur.append(words[i][0]); blocks[-1].append(i)
    for b in blocks:
        if b[0]<=idx<=b[-1]: return [words[k][0] for k in b if k<=idx],[words[k][0] for k in b]
def score(gap,maxw,maxl):
    err=0;n=0
    for f,(w,top) in ref.items():
        v=vis(f,gap,maxw,maxl)
        if not v: continue
        vw,full=v
        # predicted visible width: widest visible line
        L=[[]]
        for x in full:
            if tl(' '.join(L[-1]+[x]))>maxw: L.append([x])
            else: L[-1].append(x)
        k=0;wid=0
        for ln in L:
            sh=ln[:max(0,len(vw)-k)];k+=len(ln)
            if sh: wid=max(wid,tl(' '.join(sh)))
        ptop=1297 if len(L)>1 else 1329
        err+=abs(wid-w)/ max(w,1)+(ptop!=top and abs(ptop-top)>10)*1; n+=1
    return err/n
best=[]
for gap in (.3,.4,.5,.7,1.0):
    for maxw in (760,800,860,900):
        for maxl in (1,2,3): best.append((score(gap,maxw,maxl),gap,maxw,maxl))
best.sort(); print(best[:6])
