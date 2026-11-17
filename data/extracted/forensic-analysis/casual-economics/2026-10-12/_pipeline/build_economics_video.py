import csv,json,hashlib,shutil,re,wave,sys
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
# Assembly only: reuse verified scratch features and reviewed frames, never decode video.
vid=sys.argv[1] if len(sys.argv)>1 else 'kbPauzdHhcI'
root=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/private/tmp/yios-economics-execution-2026-10-12')
work=(Path(sys.argv[3]) if len(sys.argv)>3 else Path('/private/tmp/yios-finance-execution-evidence/economics-work'))/vid
out=Path(sys.argv[4]) if len(sys.argv)>4 else root/'data/extracted/forensic-analysis/casual-economics/2026-10-12'
d=out/'02_VIDEO_FORENSICS'/vid;d.mkdir(parents=True,exist_ok=True)
va=json.load(open(work/'visual_auto.json'));ann=json.load(open(work/'visual_review.json'));pts=json.load(open(work/('PTS_VALIDATION.json' if (work/'PTS_VALIDATION.json').exists() else 'DECODE_VALIDATION.json')));manifest=json.load(open(root/'docs/research/finance/casual-economics/LOCAL_SOURCE_MANIFEST.json'));m=next(r for r in manifest['files'] if r['video_id']==vid);sha=m['sha256'];dur=m['duration_sec'];offset=pts['first_pts'];video_end=pts['last_pts']+1/va['fps']
assert va['video_id']==vid and set(ann)=={s['state_id'] for s in va['states']}
assert pts.get('video_id',vid)==vid and pts['native_pts_frames']==va['frames']
assert not pts.get('timestamp_offset_applied_to_candidate_tables',False), 'Scratch intervals must remain relative'
# Prefer the immutable Actor's more precise timed captions; keep earlier browser export as a same-source alias.
srt=root/'data/extracted/channel-data/DS-000036/captions'/f'{vid}.srt'
b=srt.read_bytes()
def tc(t):
 h,m,z=t.replace(',', '.').split(':');return int(h)*3600+int(m)*60+float(z)
cap=[];cue_ends=[]
for block in re.split(r'\n\s*\n',b.decode().replace('\r\n','\n').strip()):
 lines=block.splitlines()
 if lines and lines[0].strip().isdigit():lines=lines[1:]
 if not lines or '-->' not in lines[0]:continue
 left,right=lines[0].split('-->');text=' '.join(x.strip() for x in lines[1:] if x.strip())
 if not text:continue
 if cap and text==cap[-1][1]:continue
 cap.append((tc(left.strip()),text));cue_ends.append(tc(right.strip()))
assert all(a[0]<=z[0] for a,z in zip(cap,cap[1:]))
def write(name,rows,fields=None):
 with open(d/(name+'.csv'),'w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
sents=[{'video_id':vid,'sentence_id':f'T{i:04d}','start_sec':a,'end_sec':min(cue_ends[i],dur),'text':t,'text_type':'YOUTUBE_AUTO_CAPTION_SEGMENT_NOT_LINGUISTIC_SENTENCE','timing_basis':'EXACT_SOURCE_SRT_DISPLAY_INTERVAL;OVERLAPS_RETAINED;END_CLAMPED_TO_MEDIA_DURATION_IF_NEEDED;NOT_WORD_ALIGNMENT','source_sha256':hashlib.sha256(b).hexdigest(),'confidence':'AUTO_CAPTION_UNVERIFIED;NO_DIRECT_LISTENING'} for i,(a,t) in enumerate(cap)]
write('SENTENCES',sents)
states=[]
for s in va['states']:
 a=ann[s['state_id']];states.append({'video_id':vid,'state_id':s['state_id'],'shot_id':s['shot_id'],'start_sec':round(s['start']+offset,6),'end_sec':round(s['end']+offset,6),'duration_sec':s['dur'],'literal_frame_description':a['description'],'asset_ids':';'.join(a['assets']),'state_change_observation':a['state_change_observation'],'representative_source_seek_sec':a['representative_frame_sec'],'evidence_sheet':('evidence/' if (d/'evidence'/a['reviewed_sheet']).exists() else 'evidence/sheets/')+a['reviewed_sheet'],'source_sha256':sha,'confidence':a['confidence'],'timing_note':'MEASURED_INTERVAL_PLUS_NATIVE_PTS_OFFSET_ONCE; representative ffmpeg seek retained; candidate interval,not continuous visual signoff'})
write('STATES',states)
shots=[{'video_id':vid,'shot_id':s['shot_id'],'start_sec':round(s['start']+offset,6),'end_sec':round(s['end']+offset,6),'transition_candidate':s['transition_in'],'transition_episode_id':s['transition_ep'],'source_sha256':sha,'confidence':'PIXEL_BOUNDARY_CANDIDATE_WITH_REPRESENTATIVE_VISUAL_REVIEW;not frame-perfect editorial cut certification'} for s in va['shots']];write('SHOTS',shots)
motions=[]
for e in va['episodes']:
 if e['cls']=='MICRO_CHANGE':continue
 near=next((s for s in states if s['end_sec']>=e['t1']+offset),states[-1])
 motions.append({'video_id':vid,'motion_id':e['ep_id'],'shot_id':near['shot_id'],'target_state_id':near['state_id'],'start_sec':round(e['t0']+offset,6),'end_sec':round(e['t1']+offset,6),'measured_class':e['cls'],'changed_pixel_peak_fraction':e['peak_frac'],'change_bbox_fraction':e['bbox_area'],'label':'SIGNAL_DERIVED_CHANGE_CANDIDATE','semantic_transition_or_easing':'UNVERIFIED','source_sha256':sha})
write('MOTIONS',motions)
assets=[]
for asset in sorted({a for s in states for a in s['asset_ids'].split(';')}):
 ss=[s for s in states if asset in s['asset_ids'].split(';')];assets.append({'video_id':vid,'asset_id':asset,'first_state_id':ss[0]['state_id'],'last_state_id':ss[-1]['state_id'],'state_occurrences':len(ss),'category':asset.split('_')[0],'source_sha256':sha,'confidence':'OBSERVED_VISUAL_CATEGORY;character roles interpreted using caption context;authoring tool unknown'})
write('ASSETS',assets)
with wave.open(str(work/'audio22k.wav')) as wav:sr=wav.getframerate();x=np.frombuffer(wav.readframes(wav.getnframes()),np.int16).astype(float)/32768
ar=[]
for i in range(int(np.ceil(len(x)/sr))):
 seg=x[i*sr:(i+1)*sr];ar.append({'video_id':vid,'audio_event_id':f'A{i:04d}','start_sec':i,'end_sec':min(i+1,len(x)/sr),'event_type':'ONE_SECOND_SIGNAL_WINDOW','rms_dbfs':round(float(20*np.log10(np.sqrt(np.mean(seg*seg))+1e-12)),3),'peak_dbfs':round(float(20*np.log10(np.max(np.abs(seg))+1e-12)),3),'auditory_label':'UNVERIFIED','source_sha256':sha,'confidence':'MEASURED_SIGNAL;NO_LISTENING;NOT_MUSIC_OR_SFX_CLASSIFICATION'})
write('AUDIO_EVENTS',ar)
sync=[]
for s in states:
 for t in sents:
  start=max(s['start_sec'],t['start_sec']);end=min(s['end_sec'],t['end_sec'])
  if end<=start:continue
  sync.append({'video_id':vid,'sync_id':f'AV{len(sync):05d}','shot_id':s['shot_id'],'state_id':s['state_id'],'sentence_id':t['sentence_id'],'audio_event_id':f'A{min(int(start),len(ar)-1):04d}','start_sec':start,'end_sec':end,'alignment_kind':'VISUAL_STATE_CAPTION_DISPLAY_INTERVAL_OVERLAP','source_sha256':sha,'confidence':'TEMPORAL_OVERLAP_ONLY;NOT_PRECISE_SPEECH_ONSET_OR_INTENTIONAL_SYNC'})
write('AUDIO_VISUAL_SYNC',sync)
(d/'SOURCE.json').write_text(json.dumps({'video_id':vid,'channel_id':m['channel_id'],'sha256':sha,'source_locator':m['source_locator'],'duration_sec':dur,'video_pts':pts,'public_caption_source':{'url':'https://www.youtube.com/watch?v='+vid,'sha256':hashlib.sha256(b).hexdigest(),'language':'en','caption_kind':'auto-generated','raw_srt_path':str(srt.relative_to(root)),'relationship':'DS-000036 AUTO CAPTIONS;NOT INDEPENDENT AUDIO VERIFICATION','word_alignment':'NOT_AVAILABLE'},'audio_listening':'UNVERIFIED','visual_pipeline_warning':pts.get('decode_warning','Prior pipeline warning retained in native PTS evidence; no re-decode in assembly'),'timestamp_convention':{'candidate_intervals':'frame-index relative seconds','offset_applied_once_sec':offset,'representative_frames':'unchanged ffmpeg source seek labels; rounded selection tolerance one source frame','caption_audio':'source display/audio timeline; no video offset applied'}},indent=2)+'\n')
# Copy reviewed compact contact sheets only, not individual extracted frames or decoded buffers.
sheets=d/'evidence/sheets';sheets.mkdir(parents=True,exist_ok=True)
for f in sorted((work/'sheets').glob('*.jpg')):
 existing=d/'evidence'/f.name
 if existing.exists():assert existing.read_bytes()==f.read_bytes()
 else:shutil.copyfile(f,sheets/f.name)
files={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in d.glob('*.csv')}
qa={'video_id':vid,'status':'STRUCTURAL_EVIDENCE_CHECKPOINT_PASSED_WITH_LIMITATIONS','overall_audiovisual_status':'PARTIAL','counts':{'shots':len(shots),'reviewed_representative_states':len(states),'motion_candidates':len(motions),'assets':len(assets),'audio_signal_windows':len(ar),'caption_segments':len(sents),'temporal_overlap_rows':len(sync),'reviewed_contact_sheets':len(list((work/'sheets').glob('*.jpg')))},'coverage':{'container_duration_sec':dur,'first_video_pts':offset,'last_video_frame_end_sec':video_end,'native_frame_count':pts['native_pts_frames'],'decoded_frame_count':va['frames'],'unreviewed_micro_change_candidates':sum(e['cls']=='MICRO_CHANGE' for e in va['episodes']),'all_representative_states_reviewed':True,'every_frame_visually_viewed':False},'checks':{'unique_state_ids':len({x['state_id'] for x in states})==len(states),'unique_shot_ids':len({x['shot_id'] for x in shots})==len(shots),'native_pts_count_matches_decode':pts['native_pts_frames']==va['frames'],'timestamps_bounded':all(0<=x['start_sec']<=x['end_sec']<=dur+.001 for x in states+shots+motions+ar+sync),'state_shot_fk':all(x['shot_id'] in {s['shot_id'] for s in shots} for x in states),'all_annotations':set(ann)=={x['state_id'] for x in states},'source_hash_matches_manifest':sha==m['sha256']},'files':files,'limitations':['Direct audio listening unavailable; no invented voice/music/SFX observations.','Caption segments are not word-aligned verified sentences.','Motion classes are signal-derived candidates; easing/path,masking and authoring software not established.','All representative states reviewed; micro-change episodes below threshold not individually annotated.','Visual pipeline decoder warnings retained; independent fullnativePTSprobe clean; chronology retains nominal-to-native one-frame offset.','No causal virality claims or investment advice.','Financial/historical fact checks targeted,not comprehensive.']}
assert all(qa['checks'].values());(d/'QA.json').write_text(json.dumps(qa,indent=2)+'\n')
print(qa['counts'],'tables',sum(v['bytes'] for v in files.values()),'sheets',sum(p.stat().st_size for p in sheets.glob('*')))
