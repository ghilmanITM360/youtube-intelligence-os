import csv,subprocess,re,json,sys,os,glob
V=os.path.expanduser('~/YIOS-local-audits/xkcd-whatif/videos')
D=os.path.expanduser('~/Downloads/videos in mp3/xkcd Channel')
REFS=[('8fADp43wJwU','High-view long'),('Z_xJ40QXu7Q','Typical long'),('9VG0yqq_PHM','Recent long'),('FkUNHhVbQ1Q','Mars long'),('2p305nzcVQE','Mars Short')]
def mp4(i): return glob.glob(f'{D}/*[[]{i}[]].mp4')[0]
def sil(f):
    r=subprocess.run(['ffmpeg','-nostdin','-i',f,'-af','silencedetect=n=-40dB:d=0.35','-f','null','-'],capture_output=True,text=True).stderr
    s=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',r)];e=[(float(a),float(b)) for a,b in re.findall(r'silence_end: ([\d.]+) \| silence_duration: ([\d.]+)',r)]
    return [(round(a-b,2),round(a,2),b) for a,b in e]
def rms(f,a,b):
    r=subprocess.run(['ffmpeg','-nostdin','-ss',str(a),'-t',str(max(b-a,0.05)),'-i',f,'-af','volumedetect','-f','null','-'],capture_output=True,text=True).stderr
    m=re.search(r'mean_volume: (-?[\d.inf]+) dB',r);return m.group(1) if m else 'NA'
rows=[];gaps=[]
for i,role in REFS:
    f=mp4(i);dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
    sh=list(csv.DictReader(open(f'{V}/{i}/shot_ledger.csv')))
    asr=list(csv.DictReader(open(f'{V}/{i}/asr/asr_small_en_segments.csv')))
    sl=sil(f)
    for a,b,d in sl: gaps.append((i,a,b,d))
    for s in sh:
        a,b=float(s['start_pts_seconds']),float(s['end_pts_seconds'])
        sp=[x for x in asr if float(x['start'])<b and float(x['end'])>a]
        txt=' / '.join(f"[{float(x['start']):.1f}-{float(x['end']):.1f}] {x['text']}" for x in sp)
        sg=[(x,y) for x,y,_ in sl if x<b and y>a]
        sound='speech(ASR)' if sp else 'no ASR speech'
        if sg: sound+='; silence '+', '.join(f'{x:.1f}-{y:.1f}' for x,y in sg)
        rows.append(dict(video_id=i,role=role,shot=s['shot_id'],t_start=a,t_end=b,
          narrator_says_ASR=txt,visible_change=f"{s['subject']} | text:{s['graphics_text']} | entr:{s['entrance']} | exit:{s['exit']} | cam:{s['camera_motion']}",
          ledger_function=s['narrative_function'],sound_measured=sound,mean_dB=rms(f,a,b),
          visual_verified=s['shot_verified'],audio_status='NOT_LISTENED (machine-measured only)'))
    print(i,len(sh),'shots',len(sl),'silences',file=sys.stderr)
w=csv.DictWriter(open('REF5_TIMELINE_ROWS.csv','w',newline=''),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
w=csv.writer(open('SILENCE_GAPS.csv','w',newline=''));w.writerow(['video_id','start','end','dur']);w.writerows(gaps)
