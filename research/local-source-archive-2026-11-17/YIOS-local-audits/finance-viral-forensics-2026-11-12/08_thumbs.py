import numpy as np,pandas as pd,cv2,os,warnings
warnings.filterwarnings('ignore')
from scipy import stats
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
v=pd.read_pickle('out/videos_feat2.pkl'); L=pd.read_pickle('out/long_classified2.pkl')
fc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
rows=[]
for vid in v.video_id:
    p=f'thumbs/{vid}.jpg'
    if not os.path.exists(p): continue
    im=cv2.imread(p)
    if im is None: continue
    im=cv2.resize(im,(320,180)); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY); hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    b,gg,r=[im[:,:,i].astype(float) for i in range(3)]; rg=r-gg; yb=.5*(r+gg)-b
    colorful=np.sqrt(rg.std()**2+yb.std()**2)+.3*np.sqrt(rg.mean()**2+yb.mean()**2)
    ed=cv2.Canny(g,100,200); 
    faces=fc.detectMultiScale(g,1.1,5,minSize=(24,24))
    # text proxy: density of strong horizontal-stroke edges in bottom/top thirds (no OCR available)
    sob=np.abs(cv2.Sobel(g,cv2.CV_32F,1,0))>150
    rows.append(dict(video_id=vid,th_brightness=g.mean(),th_contrast=g.std(),th_saturation=hsv[:,:,1].mean(),th_colorfulness=colorful,th_edge_density=(ed>0).mean(),
      th_face_count=len(faces),th_has_face=len(faces)>0,th_face_area=sum(w*h for x,y,w,h in faces)/(320*180),th_vstroke_density=sob.mean(),
      th_dark=g.mean()<70,th_bright=g.mean()>150,th_hue_med=np.median(hsv[:,:,0]),th_red_share=((hsv[:,:,0]<10)|(hsv[:,:,0]>170))[hsv[:,:,1]>100].mean() if (hsv[:,:,1]>100).any() else 0))
T=pd.DataFrame(rows).merge(pd.read_csv('out/thumbnail_ocr.csv')[['video_id','th_text_words','th_text_chars']],on='video_id',how='left'); T['th_text_le4words']=(T.th_text_words<=4)&(T.th_text_words>=1); T['th_text_gt8words']=T.th_text_words>8; T.to_csv('out/thumbnail_visual_features.csv',index=False); print(len(T))
L=L.merge(T,on='video_id',how='left')
binf=['th_has_face','th_dark','th_bright','th_text_le4words','th_text_gt8words']; cont=['th_brightness','th_contrast','th_saturation','th_colorfulness','th_edge_density','th_face_area','th_vstroke_density','th_red_share','th_text_words','th_text_chars']
out=[]
for c in binf:
    d=L.dropna(subset=[c]).copy(); d['f']=d[c].astype(float)
    if min(d.f.sum(),len(d)-d.f.sum())<30: continue
    m=smf.ols('logPI~f',d).fit(cov_type='cluster',cov_kwds={'groups':d.channel_id.astype('category').cat.codes}); pos=tot=0
    for cid,g in d.groupby('channel_id'):
        a=g[g.f==1].logPI;b=g[g.f==0].logPI
        if len(a)>=4 and len(b)>=4: tot+=1;pos+=a.mean()>b.mean()
    out.append(dict(feature=c,kind='binary',n=len(d),n_with=int(d.f.sum()),effect=np.exp(m.params['f']),ci_lo=np.exp(m.conf_int().loc['f',0]),ci_hi=np.exp(m.conf_int().loc['f',1]),p=m.pvalues['f'],ch_pos=pos,ch_tot=tot))
for c in cont:
    d=L.dropna(subset=[c]); r,p=stats.spearmanr(d[c],d.logPI); pos=tot=0
    for cid,g in d.groupby('channel_id'):
        if len(g)>=15:
            rr=stats.spearmanr(g[c],g.logPI)[0]
            if not np.isnan(rr): tot+=1;pos+=rr>0
    out.append(dict(feature=c,kind='spearman',n=len(d),effect=r,p=p,ch_pos=pos,ch_tot=tot))
O=pd.DataFrame(out); O['q_BH']=multipletests(O.p,method='fdr_bh')[1]; O.to_csv('out/thumbnail_feature_tests.csv',index=False); print(O.round(3).to_string())
# thumbnail accessibility
a=pd.read_csv('out/thumbnail_accessibility.csv') if os.path.exists('out/thumbnail_accessibility.csv') else None
L.to_pickle('out/long_classified3.pkl')
