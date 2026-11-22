"""Same metrics as 21_ (rising edge >0.02 of pixels changed; still = <=0.002) for ID-less files, keyed by sha8. Usage: profile_idless.py OUT.csv"""
import csv,os,subprocess,sys,numpy as np
from multiprocessing import Pool
D=os.path.expanduser('~/workprojects/videos in mp3/CasuallyFinance')
rows=[r for r in csv.DictReader(open('01_DATA_INVENTORY.csv')) if not r['video_id']]
def run(r):
    W=240;H=int(round(W*int(r['height'])/int(r['width'])/2)*2)
    p=subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-i',os.path.join(D,r['file_name']),'-vf',f'scale={W}:{H}','-pix_fmt','gray','-f','rawvideo','-'],capture_output=True)
    a=np.frombuffer(p.stdout,np.uint8);a=a[:len(a)//(W*H)*W*H].reshape(-1,H,W).astype(np.int16)
    s=(np.abs(np.diff(a,axis=0))>16).mean(axis=(1,2));on=s>0.02;d=float(r['duration_s'])
    return dict(key='FILE-'+r['sha256'][:8],file=r['file_name'],orientation=r['orientation'],duration_s=round(d,1),change_events_per_min=round((on[1:]&~on[:-1]).sum()/d*60,1),mean_changed_pct=round(s.mean()*100,2),still_frames_pct=round((s<=0.002).mean()*100,1))
if __name__=='__main__':
    with Pool(6) as P: out=P.map(run,rows)
    w=csv.DictWriter(open(sys.argv[1],'w',newline=''),list(out[0]));w.writeheader();w.writerows(out)
