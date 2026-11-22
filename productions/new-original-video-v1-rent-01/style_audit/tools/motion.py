import subprocess,numpy as np,os,glob
D="/Users/ghilmankhan/workprojects/videos in mp3/CasuallyFinance/"
V1="/Users/ghilmankhan/workprojects/visual-audit-worktrees/casually-finance/productions/new-original-video-v1-rent-01/out/V1_RENT_segment_0-75s_take2.mp4"
def stat(f,label,ss=0,t=75):
    cmd=["ffmpeg","-v","error","-ss",str(ss),"-t",str(t),"-i",f,"-vf","fps=30,scale=192:108,format=gray","-f","rawvideo","-"]
    b=subprocess.run(cmd,capture_output=True).stdout; n=len(b)//(192*108)
    a=np.frombuffer(b[:n*192*108],np.uint8).reshape(n,108,192).astype(int)
    d=np.abs(np.diff(a,axis=0)).mean(axis=(1,2))
    static=(d<0.02).mean()           # exactly-still frames
    big=(d>2.0)                      # large changes (cuts / big pop-ins)
    # count events: runs of consecutive changed frames (d>0.2) separated by >=6 still frames
    ch=d>0.2; ev=0; gap=99
    for c in ch:
        if c and gap>=6: ev+=1
        gap = 0 if c else gap+1
    print(f"{label:34s} dur={n/30:5.1f}s static={static:.2f} cuts(d>2)={int(big.sum()):3d} events={ev:3d} ev/10s={ev/(n/30)*10:4.1f}")
stat(V1,"V1 RENT 0-75s")
for nm in ["Brace For Impact. - Casual Finance (720p, h264).mp4","Every Type of Investor Explained in 6 Minutes - Casual Finance (720p, h264).mp4","Something Feels Off About 2026... [Im-N3K9Pnf0].mp4","America Is Quietly Drowning in Debt [7K991LgY3tc].mp4","Crypto Is a Brilliant Scam and I Can Prove It [hbsYaLaN_F8].mp4","MicroStrategy The Crypto Scam Hiding in Plain Sight - Casual Finance (1080p, h264).mp4"]:
    stat(D+nm,nm[:34],ss=0,t=75)
