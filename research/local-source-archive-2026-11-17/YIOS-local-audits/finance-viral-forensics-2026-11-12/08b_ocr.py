import subprocess,os,pandas as pd,cv2,concurrent.futures as cf,tempfile
ids=[f[:-4] for f in os.listdir('thumbs') if f.endswith('.jpg')]
def ocr(vid):
    im=cv2.imread(f'thumbs/{vid}.jpg')
    if im is None: return dict(video_id=vid,th_text_words=None,th_text_chars=None)
    im=cv2.resize(im,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC); p=f'/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/16863ac4-a0b4-4921-bd1f-90593160b8af/scratchpad/ocr/{vid}.png'; cv2.imwrite(p,im)
    r=subprocess.run(['tesseract',p,'-','--psm','11','tsv'],capture_output=True); os.remove(p)
    W=[]; 
    for ln in r.stdout.decode('utf-8','replace').splitlines()[1:]:
        c=ln.split('\t')
        if len(c)>=12 and c[11].strip() and float(c[10])>=60 and len(c[11].strip())>=2: W.append(c[11].strip())
    return dict(video_id=vid,th_text_words=len(W),th_text_chars=sum(map(len,W)),th_text='|'.join(W)[:200])
with cf.ThreadPoolExecutor(6) as ex: R=list(ex.map(ocr,ids))
pd.DataFrame(R).to_csv('out/thumbnail_ocr.csv',index=False); print(len(R))
