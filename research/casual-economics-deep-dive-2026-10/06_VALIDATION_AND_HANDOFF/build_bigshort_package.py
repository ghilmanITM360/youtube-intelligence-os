from pathlib import Path
import json,csv,re,hashlib,datetime,statistics,shutil
import sys
R=Path(__file__).resolve().parents[3];W=Path(sys.argv[1]).resolve();D=R/'research/casual-economics-deep-dive-2026-10';V='Iwz0fhJWN9Q';P=D/'02_VIDEO_FORENSICS'/V;P.mkdir(parents=True,exist_ok=True)
O=R/'data/extracted/forensic-analysis/casual-economics/2026-10-12/02_VIDEO_FORENSICS'/V
source=json.loads((D/'01_SOURCE_INVENTORY'/f'{V}.json').read_text());sha=source['actual_sha256'];duration=source['actual_duration_sec'];va=json.loads((O/'visual_auto.json').read_text());pts=json.loads((O/'PTS_VALIDATION.json').read_text());offset=pts['first_pts']
def save(name,obj): (P/name).write_text(json.dumps(obj,indent=2)+'\n')
def csvwrite(name,rows):
 assert rows
 with (P/name).open('w',newline='') as f:
  z=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');z.writeheader();z.writerows(rows)
def parse_notes(name):return [x.split('|') for x in (P/'review_inputs'/name).read_text().splitlines() if x]
frames=json.loads((W/'FRAME_MANIFEST.json').read_text());notes=parse_notes('review_notes.txt');assert len(notes)==len(frames)==275
rows=[]
for s,f,(idx,desc,assets) in zip(va['states'],frames,notes):
 assert int(idx)==f['index'] and s['state_id']==f['state_id']
 rows.append(dict(video_id=V,observation_id=s['state_id'],shot_id=s['shot_id'],start_sec=round(s['start']+offset,6),end_sec=round(s['end']+offset,6),source_seek_sec=f['source_seek_sec'],observation_type='REVIEWED_REPRESENTATIVE_OF_CANDIDATE_INTERVAL',description=desc,asset_ids=assets,source_sha256=sha,frame_sha256=f['frame_sha256'],evidence_status='SCREEN_OBSERVED',interval_constancy='NOT_CERTIFIED'))
gaps=json.loads((W/'GAP_MANIFEST.json').read_text());gn=parse_notes('gap_notes.txt');assert len(gaps)==len(gn)==42
for f,(idx,desc,assets) in zip(gaps,gn):
 assert idx==f['supplement_id'];t=f['source_seek_sec'];shot=next((s['shot_id'] for s in va['shots'] if s['start']+offset<=t<s['end']+offset),'TAIL')
 rows.append(dict(video_id=V,observation_id=idx,shot_id=shot,start_sec=t,end_sec=t,source_seek_sec=t,observation_type='POINT_SUPPLEMENT_NOT_A_SEGMENT',description=desc,asset_ids=assets,source_sha256=sha,frame_sha256=f['frame_sha256'],evidence_status='SCREEN_OBSERVED',interval_constancy='NOT_APPLICABLE'))
rows.sort(key=lambda r:r['source_seek_sec']);csvwrite('VISUAL_TIMELINE.csv',rows)
assetrows=[]
for a in sorted({x for r in rows for x in r['asset_ids'].split(';')}):
 rr=[r for r in rows if a in r['asset_ids'].split(';')];assetrows.append(dict(video_id=V,asset_id=a,category=a.split('_')[0],first_observed_sec=min(r['source_seek_sec'] for r in rr),last_observed_sec=max(r['source_seek_sec'] for r in rr),observation_ids=';'.join(r['observation_id'] for r in rr),observed_appearances=len(rr),reuse_status='VISIBLE_DESIGN_REUSE' if len(rr)>1 else 'SINGLE_REVIEWED_APPEARANCE',original_asset_file_identity='NOT_VERIFIED',source_sha256=sha,note='Category/design-family observations, not count of authored source files. Named character identity uses onscreen labels and caption context.'))
csvwrite('ASSET_OBSERVATIONS.csv',assetrows)
tracks=json.loads((R/'data/extracted/channel-data/DS-000036/caption-tracks.json').read_text());srt=tracks['tracks'][V]['srt'];caps=[]
def timecode(t):
 a,b,c=t.replace(',','.').split(':');return int(a)*3600+int(b)*60+float(c)
for block in re.split(r'\n\s*\n',srt.strip()):
 lines=block.splitlines()
 if len(lines)<3 or '-->' not in lines[1]:continue
 text=' '.join(lines[2:]).strip()
 if not text:continue
 a,b=lines[1].split('-->');caps.append(dict(cue_id=lines[0],start=timecode(a.strip()),end=timecode(b.strip()),text=text))
seq=json.loads((W/'TEMPORAL_MANIFEST.json').read_text());mn=parse_notes('motion_notes.txt');assert len(seq)==len(mn)==34
motions=[];av=[]
for s,n in zip(seq,mn):
 sid,tech,obs,direction,bounds,recipe,purpose,precision=n;assert sid==s['sequence_id'];a=s['start_sec'];b=s['end_sec'];overlap=[c for c in caps if c['start']<b and c['end']>a];states=[r['observation_id'] for r in rows if a<=r['source_seek_sec']<=b]
 motions.append(dict(video_id=V,motion_id=sid,start_sec=a,end_sec=b,review_window_sec=round(b-a,6),observation_ids=';'.join(states),source_sample_times_sec=';'.join(str(f['time_sec']) for f in s['frames']),sample_frame_sha256s=';'.join(f['sha256'] for f in s['frames']),visible_technique=tech.replace('CAMERA_PULL_BACK','SCALE'),observed_sequence=obs,direction_and_transform=direction,change_brackets=bounds,reported_change_bound_sec=float(precision),actual_sampling_step_sec=round((b-a)/6,6),reproduction_method_inferred=recipe,narrative_function_interpreted=purpose,caption_cue_ids=';'.join(c['cue_id'] for c in overlap),easing='NOT_MEASURED',actual_authoring_method='UNKNOWN',source_sha256=sha,evidence_status='SCREEN_OBSERVED_SEQUENCE;REPRODUCTION_METHOD_INFERRED',continuous_playback='NOT_PERFORMED'))
 av.append(dict(video_id=V,event_id='AV_'+sid,start_sec=a,end_sec=b,motion_id=sid,caption_cue_ids=';'.join(c['cue_id'] for c in overlap),caption_context=' '.join(c['text'] for c in overlap),visual_observation=obs,audio_evidence='ASR_INFERRED',visual_evidence='SCREEN_OBSERVED',direct_audio='NOT_VERIFIED',sync_status='CAPTION_DISPLAY_OVERLAP_ONLY;NOT_WORD_ALIGNED',source_sha256=sha,caption_sha256=hashlib.sha256(srt.encode()).hexdigest()))
csvwrite('MOTION_SEQUENCES.csv',motions);csvwrite('AUDIO_VISUAL_EVENTS.csv',av)
beats=[]
for i,(a,b,name,visual,purpose) in enumerate(parse_notes('beat_notes.txt')):
 a,b=float(a),float(b);rr=[r['observation_id'] for r in rows if a<=r['source_seek_sec']<b];cc=[c['cue_id'] for c in caps if c['start']<b and c['end']>a]
 beats.append(dict(video_id=V,beat_id=f'B{i:03d}',start_sec=a,end_sec=b,beat=name,visible_structure=visual,interpretation_and_caveat=purpose,observation_ids=';'.join(rr),caption_cue_ids=';'.join(cc),source_sha256=sha,evidence='SCREEN_OBSERVED_AND_AUTO_CAPTION_CONTEXT;NO_RETENTION_CLAIM'))
csvwrite('STORY_AND_EDITING_BEATS.csv',beats)
# Retain source-linked review metadata; no extracted frame library in Git.
save('REVIEW_EVIDENCE.json',{'reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'Single primary Codex agent; not independent human review','representative_manifest':[ {k:v for k,v in x.items() if k!='local_frame'} for x in frames],'supplement_manifest':[{k:v for k,v in x.items() if k!='local_frame'} for x in gaps],'temporal_manifest':[{**{k:v for k,v in s.items() if k!='frames'},'frames':[{k:v for k,v in f.items() if k!='local_frame'} for f in s['frames']]} for s in seq],'native_frames':[{'source_seek_sec':t,'sha256':hashlib.sha256((W/n).read_bytes()).hexdigest(),'resolution':'1920x1080'} for n,t in [('character_native.png',83.697),('dialogue_native.png',194.4),('asset_native.png',397.738),('last_frame.png',809.433333)]],'local_scratch':str(W),'source_sha256':sha,'no_bulk_frames_committed':True})
thumb=W/'thumbnail.jpg';(P/'evidence').mkdir(exist_ok=True);shutil.copyfile(thumb,P/'evidence/thumbnail.jpg');save('THUMBNAIL_PROVENANCE.json',{'video_id':V,'url':f'https://i.ytimg.com/vi/{V}/maxresdefault.jpg','retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(thumb.read_bytes()).hexdigest(),'bytes':thumb.stat().st_size,'historical_sha256':json.loads((O/'PREPARATION_CHECKPOINT.json').read_text())['scratch_files']['thumbnail.jpg']['sha256'],'pixel_review':'SCREEN_OBSERVED','source':'YouTube public thumbnail CDN; not MP4','historical_match':hashlib.sha256(thumb.read_bytes()).hexdigest()==json.loads((O/'PREPARATION_CHECKPOINT.json').read_text())['scratch_files']['thumbnail.jpg']['sha256']})
alltimes=sorted(set([r['source_seek_sec'] for r in rows]+[f['time_sec'] for s in seq for f in s['frames']]+[83.697,194.4,397.738,809.433333]));lens=[s['end']-s['start'] for s in va['shots']];gaps=[b-a for a,b in zip(alltimes,alltimes[1:])]
metrics={'video_id':V,'duration_sec':duration,'historical_candidate_shots':len(va['shots']),'historical_candidate_states':len(va['states']),'historical_change_episodes':len(va['episodes']),'candidate_mean_shot_duration_sec':statistics.mean(lens),'candidate_median_shot_duration_sec':statistics.median(lens),'candidate_shots_per_min':len(va['shots'])/duration*60,'candidate_states_per_min':len(va['states'])/duration*60,'reviewed_representatives':275,'reviewed_gap_samples':42,'reviewed_temporal_sequences':34,'reviewed_sequence_frames':sum(len(s['frames']) for s in seq),'reviewed_native_resolution_frames':4,'unique_reviewed_sample_times':len(alltimes),'maximum_between_sample_gap_sec':max(gaps),'first_reviewed_sec':min(alltimes),'last_reviewed_sec':max(alltimes),'container_tail_after_last_sample_sec':duration-max(alltimes),'nonblank_caption_cues':len(caps),'caption_word_count_regex':len(re.findall(r"\b[\w'-]+\b",' '.join(c['text'] for c in caps))),'metrics_warning':'Candidate segmentation undercounts some semantic changes and oversplits caption/UI changes; sample spacing does not certify absence of between-sample events. Caption words per container minute are not directly measured speech rate.'}
save('COVERAGE_MEASUREMENTS.json',metrics);print(json.dumps(metrics,indent=2))
# Pending validation is honest until dedicated validator runs.
save('QA.json',{'video_id':V,'status':'PENDING_VALIDATION','deep_forensic_status':'PARTIAL_TEMPORAL_MECHANISM_COVERAGE','independent_visual_review':'NOT_PERFORMED','direct_audio_listening':'NOT_PERFORMED','full_audiovisual_signoff':'NOT_COMPLETE','source_sha256':sha,'limitations':['All historical representative images and 42 supplemental stills reviewed; meaningful changes can still occur between samples.','34 selected temporal sequences reviewed; not all 625 automatic change episodes individually adjudicated.','Animation duration brackets are sampled bounds; easing and exact joint/transform trajectories not measured.','Historical shot boundaries remain candidates; discovered missed semantic scenes documented without pretending canonical segmentation was repaired.','Direct listening, exact narration timing, music/SFX identity and continuous playback not verified.','No channel-wide performance or blueprint inference is permitted from this single new package.','Representative thumbnail retrieved and visually reviewed; metrics remain historical.']})
