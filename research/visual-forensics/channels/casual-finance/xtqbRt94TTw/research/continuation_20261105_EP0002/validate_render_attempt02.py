"""Check decoded output presence, separation, motion and stable anchors."""
from pathlib import Path
import json,subprocess
from PIL import Image
import numpy as np
P=Path(__file__).parent;R=P/'original_render_attempt02'
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',str(R/'original_timing_master.mkv')]))
arrays={n:np.array(Image.open(R/'decoded'/f'f{n:05d}.png')) for n in range(37,65)}
rows=[]
for n,a in arrays.items():
    roi=a[350:670,790:1130];bg=np.array([251,244,235]);mask=(roi!=bg).any(axis=2);ys,xs=np.where(mask)
    accent=(roi==np.array([230,110,100])).all(axis=2)
    rows.append({'frame':n,'badge_bbox':None if not len(xs) else [int(xs.min()+790),int(ys.min()+350),int(xs.max()+790),int(ys.max()+350)],'coral_pixels':int(accent.sum())})
video=next(s for s in probe['streams'] if s['codec_type']=='video')
checks={
 'exact_stream':video['width']==1920 and video['height']==1080 and video['avg_frame_rate']=='24/1' and video['nb_read_frames']=='28',
 'no_audio':not any(s['codec_type']=='audio' for s in probe['streams']),
 'first_rim39':next(r['frame'] for r in rows if r['badge_bbox'])==39,
 'first_fill40':next(r['frame'] for r in rows if r['coral_pixels'])==40,
 'first_full_separation53':next(r['frame'] for r in rows if r['badge_bbox'] and r['badge_bbox'][3]<669)==53,
 'panel_c_absent48_complete49':np.all(arrays[48][320:501,1250:1821]==np.array([251,244,235])) and np.array_equal(arrays[49][320:501,1250:1821],arrays[64][320:501,1250:1821]) and not np.array_equal(arrays[48][320:501,1250:1821],arrays[49][320:501,1250:1821]),
 'upward_until59':all(rows[n-37]['badge_bbox'][1]<rows[n-38]['badge_bbox'][1] for n in range(40,60)),
 'hold60_64':all(np.array_equal(arrays[59],arrays[n]) for n in range(60,65)),
 'fixed_lights_console':all(np.array_equal(arrays[37][670:],a[670:]) for a in arrays.values()),
 'fixed_panels_a_b':all(np.array_equal(arrays[37][80:341,100:621],a[80:341,100:621]) and np.array_equal(arrays[37][80:221,1100:1701],a[80:221,1100:1701]) for a in arrays.values())}
result={'checks':checks,'status':'PASS_INTERNAL_BOUNDED_TIMING_TRANSFER' if all(checks.values()) else 'FAIL_PRESERVED','probe':probe,'measurements':rows,'visual_checkpoint_review':'PENDING_ACTUAL_IMAGE_VIEWS','independent_signoff':'NOT_PERFORMED','whole_video_cold_start':'PENDING; this is only a bounded cold-input unit','actual_listening_seconds':0,'CT_SCAN_COMPLETE':False}
(R/'validation.json').write_text(json.dumps(result,indent=2))
print(json.dumps(checks,indent=2));assert all(checks.values())
