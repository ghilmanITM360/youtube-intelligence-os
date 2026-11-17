# Candidate shot cuts via PySceneDetect ContentDetector(12) (candidates only; require visual confirmation). Derived from BE scenedetect_run.py with output path arg.
import sys,csv
from scenedetect import open_video,SceneManager,ContentDetector
v=open_video(sys.argv[1]);sm=SceneManager();sm.add_detector(ContentDetector(threshold=12.0,min_scene_len=1));sm.detect_scenes(v)
sc=sm.get_scene_list()
with open(sys.argv[2],'w',newline='') as f:
    w=csv.writer(f);w.writerow(['scene','start_frame','end_frame','start_s'])
    for i,(a,b) in enumerate(sc):w.writerow([i+1,a.get_frames(),b.get_frames()-1,round(a.get_seconds(),4)])
print(len(sc),'scenes')
