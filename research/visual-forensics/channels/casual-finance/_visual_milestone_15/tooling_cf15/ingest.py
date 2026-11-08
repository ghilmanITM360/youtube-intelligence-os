# usage: ingest.py SRC WS VIDEO_ID  -> WS/source_manifest.json  (read-only on SRC)
import sys, json, hashlib, subprocess, os, datetime
src, ws, vid = sys.argv[1:4]
os.makedirs(f'{ws}/tables', exist_ok=True)
h = hashlib.sha256()
with open(src, 'rb') as f:
    for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
pr = json.loads(subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',src], capture_output=True, text=True).stdout)
fr = subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','frame=best_effort_timestamp_time,pict_type,key_frame','-of','csv=p=0',src], capture_output=True, text=True).stdout.split()
pts = [float(l.split(',')[1]) for l in fr]; pict = [l.split(',')[2] for l in fr]  # ffprobe csv order: key_frame,pts,pict_type
d = [round(b - a, 5) for a, b in zip(pts, pts[1:])]
v = next(s for s in pr['streams'] if s['codec_type'] == 'video'); a = [s for s in pr['streams'] if s['codec_type'] == 'audio']
m = dict(video_id=vid, source_path=src, source_sha256=h.hexdigest(), bytes=os.path.getsize(src), ffprobe_version=subprocess.run(['ffprobe','-version'],capture_output=True,text=True).stdout.split('\n')[0],
  container=pr['format'].get('format_name'), container_duration=pr['format'].get('duration'), video=dict(codec=v['codec_name'], w=v['width'], h=v['height'], pix_fmt=v.get('pix_fmt'), avg_frame_rate=v['avg_frame_rate'], r_frame_rate=v['r_frame_rate'], time_base=v['time_base'], start_time=v.get('start_time'), nb_frames_header=v.get('nb_frames'), duration=v.get('duration'), rotation=[s for s in v.get('side_data_list',[])]),
  audio=[dict(codec=x['codec_name'], channels=x['channels'], sample_rate=x['sample_rate'], start_time=x.get('start_time'), duration=x.get('duration')) for x in a],
  decoded_frames_pts_listed=len(pts), pts_first=pts[0], pts_last=pts[-1], pts_monotonic=all(x > 0 for x in d), frame_delta_min=min(d), frame_delta_max=max(d), frame_delta_distinct=sorted(set(d))[:8],
  cfr_assessment='CFR' if max(d) - min(d) < 0.002 else 'VFR_OR_JITTER', iframes=sum(p == 'I' for p in pict), iframe_indices=[i for i, p in enumerate(pict) if p == 'I'],
  recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), reader='Claude Sonnet 5.5 (Machine A)', status='MEASURED')
json.dump(m, open(f'{ws}/source_manifest.json', 'w'), indent=1)
json.dump(pts, open(f'{ws}/tables/pts.json', 'w'))
print(vid, m['source_sha256'][:16], 'frames', len(pts), m['cfr_assessment'], 'dt', m['frame_delta_distinct'][:3], 'I-frames', m['iframes'])
