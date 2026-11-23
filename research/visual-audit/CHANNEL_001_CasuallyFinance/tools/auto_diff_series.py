"""Per-frame changed-pixel fraction for every CasuallyFinance MP4 (480px gray). Usage: auto_diff_series.py OUTDIR [ID ...]"""
import csv,os,subprocess,sys,numpy as np
from multiprocessing import Pool
D=os.path.expanduser('~/workprojects/videos in mp3/CasuallyFinance')
out=sys.argv[1];os.makedirs(out,exist_ok=True)
inv={r['video_id']:r for r in csv.DictReader(open('01_DATA_INVENTORY.csv'))}
def run(v):
    f=os.path.join(D,inv[v]['file_name']);o=f'{out}/{v}.npy'
    if os.path.exists(o):return v
    W=240;H=int(round(W*int(inv[v]['height'])/int(inv[v]['width'])/2)*2)
    p=subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-i',f,'-vf',f'scale={W}:{H}','-pix_fmt','gray','-f','rawvideo','-'],capture_output=True)
    a=np.frombuffer(p.stdout,np.uint8);a=a[:len(a)//(W*H)*W*H].reshape(-1,H,W).astype(np.int16)
    np.save(o,(np.abs(np.diff(a,axis=0))>16).mean(axis=(1,2)).astype(np.float32));return v
if __name__=='__main__':
    ids=sys.argv[2:] or list(inv)
    with Pool(6) as P:
        for v in P.imap_unordered(run,ids):print(v,flush=True)
