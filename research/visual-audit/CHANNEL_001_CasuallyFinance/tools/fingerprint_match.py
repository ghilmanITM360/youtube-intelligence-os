"""Fingerprint every file (8 frames, 16x28 grey) and match ID-less files to ID'd ones. Usage (from channel dir): fingerprint_match.py OUT.csv"""
import csv,os,subprocess,sys,numpy as np
from multiprocessing import Pool
D=os.path.expanduser('~/workprojects/videos in mp3/CasuallyFinance')
inv=list(csv.DictReader(open('01_DATA_INVENTORY.csv')))
def fp(r):
    f=os.path.join(D,r['file_name']);d=float(r['duration_s']);fr=[]
    for q in np.linspace(.05,.95,8):
        p=subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-ss',f'{d*q:.2f}','-i',f,'-frames:v','1','-vf','scale=16:28','-pix_fmt','gray','-f','rawvideo','-'],capture_output=True)
        a=np.frombuffer(p.stdout,np.uint8)
        fr.append(a.astype(float) if a.size==448 else np.zeros(448))
    return np.array(fr)
if __name__=='__main__':
    with Pool(6) as P: F=P.map(fp,inv)
    key=lambda r:r['video_id'] or 'FILE-'+r['sha256'][:8]
    def dist(a,b):
        return float(np.mean(np.abs(a-b))) # mean abs grey diff over 8 frames
    rows=[]
    for i,r in enumerate(inv):
        if r['video_id']:continue
        best=min(((dist(F[i],F[j]),j) for j,s in enumerate(inv) if j!=i and abs(float(s['duration_s'])-float(r['duration_s']))<4),default=(None,None))
        d,j=best
        rows.append(dict(file=r['file_name'],key=key(r),dur=round(float(r['duration_s']),1),res=r['width']+'x'+r['height'],best_match=(key(inv[j])+' | '+inv[j]['file_name'][:60]) if j is not None else '',match_dur=round(float(inv[j]['duration_s']),1) if j is not None else '',grey_diff=round(d,2) if d is not None else ''))
    w=csv.DictWriter(open(sys.argv[1],'w',newline=''),list(rows[0]));w.writeheader();w.writerows(rows)
