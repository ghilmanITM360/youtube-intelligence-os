import os,re,json,subprocess,hashlib,csv,sys
D='/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
out=[]
for f in sorted(os.listdir(D)):
    p=D+f; vid=re.search(r'\[([A-Za-z0-9_-]{11})\]',f).group(1)
    j=json.loads(subprocess.run(['ffprobe','-v','error','-print_format','json','-show_format','-show_streams',p],capture_output=True,text=True).stdout)
    v=[s for s in j['streams'] if s['codec_type']=='video'][0]; a=[s for s in j['streams'] if s['codec_type']=='audio']
    h=hashlib.sha256()
    with open(p,'rb') as fh:
        for b in iter(lambda:fh.read(1<<20),b''): h.update(b)
    fr=v.get('avg_frame_rate','0/1').split('/'); fps=round(int(fr[0])/max(int(fr[1]),1),3)
    out.append(dict(video_id=vid,path=p,size=os.path.getsize(p),sha256=h.hexdigest(),duration=float(j['format']['duration']),width=v['width'],height=v['height'],fps=fps,vcodec=v['codec_name'],bitrate=int(j['format'].get('bit_rate',0)),has_audio=bool(a),acodec=a[0]['codec_name'] if a else '',nb_frames=v.get('nb_frames','')))
w=csv.DictWriter(open('media_probe_88.csv','w'),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print(len(out))
