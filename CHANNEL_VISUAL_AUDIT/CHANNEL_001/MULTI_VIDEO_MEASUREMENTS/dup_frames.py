"""Duplicate-frame census: python3 dup_frames.py VIDEO. Prints runs of motion (consecutive changing frames) and where exact dups (diff<eps) sit mod 5."""
import subprocess,sys,numpy as np
p=sys.argv[1];W,H=135,240
pr=subprocess.Popen(['/opt/homebrew/bin/ffmpeg','-v','error','-i',p,'-vf',f'scale={W}:{H}:flags=area','-f','rawvideo','-pix_fmt','gray','-'],stdout=subprocess.PIPE)
fs=[];n=W*H
while True:
    b=pr.stdout.read(n)
    if len(b)<n:break
    fs.append(np.frombuffer(b,np.uint8).astype(np.int16))
d=[0]+[int(np.abs(fs[i]-fs[i-1]).sum()) for i in range(1,len(fs))]
d=np.array(d);big=d>np.percentile(d[d>0],30) if (d>0).any() else d>0
# motion frames: diff > small noise; dup: diff <= noise while neighbours move
noise=max(50,int(np.percentile(d,10))*2+50)
mov=d>noise
dups=[i for i in range(2,len(d)-2) if not mov[i] and mov[i-1] and mov[i-2] and mov[i+1] and mov[i+2]]
print('frames',len(d),'noise',noise,'moving',int(mov.sum()),'dups-inside-motion',len(dups))
from collections import Counter
print('dup frame idx',dups[:60]);
# gaps between consecutive dups
g=[b-a for a,b in zip(dups,dups[1:])];print('gap histogram',Counter(g).most_common(6))
