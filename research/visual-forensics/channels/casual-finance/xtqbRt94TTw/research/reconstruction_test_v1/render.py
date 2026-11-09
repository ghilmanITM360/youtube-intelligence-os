import pathlib,json,subprocess,hashlib,cv2,numpy as np
D=pathlib.Path(__file__).resolve().parent;S=json.loads((D/'SPEC.json').read_text());W,H=S['width'],S['height'];out=D/'original_timing_test.mp4';assert not out.exists()
base=np.full((H,W,3),S['background_bgr'],np.uint8);ink=tuple(S['ink_bgr']);accent=tuple(S['accent_bgr'])
for k,(x,y) in enumerate(S['character_centers']):
 cv2.rectangle(base,(x-84,y-74),(x+84,y+74),ink,-1);cv2.circle(base,(x-30,y-12),9,(245,245,245),-1);cv2.circle(base,(x+30,y-12),9,(245,245,245),-1);cv2.line(base,(x-24,y+28),(x+24,y+28),accent,8);cv2.rectangle(base,(x-70,y+90),(x+70,y+224),accent if k%2==0 else (155,125,75),-1)
cv2.ellipse(base,tuple(S['table']['center']),tuple(S['table']['axes']),0,0,360,(170,185,200),-1);cv2.ellipse(base,tuple(S['table']['center']),tuple(S['table']['axes']),0,0,360,ink,8)
p=subprocess.Popen(['/opt/homebrew/bin/ffmpeg','-v','error','-n','-f','rawvideo','-pixel_format','bgr24','-video_size',f'{W}x{H}','-framerate','24','-i','pipe:0','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',str(out)],stdin=subprocess.PIPE)
for f in range(S['frames']):
 image=base.copy();label=next(x['label'] for x in S['bubble_states'] if x['start']<=f<=x['end'])
 if label:
  center=(1240,245) if f<53 else (680,245);cv2.ellipse(image,center,(260,110),0,0,360,(255,255,255),-1);cv2.ellipse(image,center,(260,110),0,0,360,ink,6);cv2.putText(image,label,(center[0]-145,center[1]+22),cv2.FONT_HERSHEY_DUPLEX,1.9,accent,3,cv2.LINE_AA)
 p.stdin.write(image.tobytes())
p.stdin.close();assert p.wait()==0
cap=cv2.VideoCapture(str(out));saved=[];n=0;decoded=[]
while True:
 ok,im=cap.read()
 if not ok:break
 decoded.append(im)
 if n in (0,35,36,52,53,74):
  q=D/f'check_f{n:03}.png';cv2.imwrite(str(q),im);saved.append(dict(frame=n,path=str(q),sha256=hashlib.sha256(q.read_bytes()).hexdigest()))
 n+=1
cap.release();assert n==75
# Compare retained anchors with tolerance for codec transform noise; check exact schedule change frames.
roi=lambda im:im[450:1000,120:1800]
diff=[float(np.mean(cv2.absdiff(roi(decoded[0]),roi(x)))) for x in decoded];assert max(diff)<1.0,max(diff)
assert np.mean(cv2.absdiff(decoded[0],decoded[35]))<1;assert np.mean(cv2.absdiff(decoded[35][:450],decoded[36][:450]))>2;assert np.mean(cv2.absdiff(decoded[36],decoded[52]))<1;assert np.mean(cv2.absdiff(decoded[52][:450],decoded[53][:450]))>2;assert np.mean(cv2.absdiff(decoded[53],decoded[74]))<1
(D/'render_validation.json').write_text(json.dumps({'frames_decoded':n,'resolution':[W,H],'fps':24,'duration_s':n/24,'schedule_checks':'PASS','static_anchor_mean_abs_diff_max':max(diff),'rendered_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'rendered_path':str(out),'visual_review':'PENDING_ACTUAL_IMAGE_READS','audio':'INTENTIONALLY_SILENT_ORIGINAL_TEST_NOT_SOURCE_LISTENING','checkpoint_frames':saved},indent=2));print('rendered75frames; schedule+anchorsPASS; visualreview pending')
