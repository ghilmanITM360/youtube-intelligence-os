"""Assemble explicitly reviewed point/temporal evidence; never label samples as shots."""
import csv, datetime, hashlib, json, re, shutil, sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=R/'research/casual-economics-deep-dive-2026-10'
V=sys.argv[1];W=Path(sys.argv[2]);P=D/'02_VIDEO_FORENSICS'/V
assert V=='nr5dcBPACH0', 'Greece assembler: native-review inputs are video-specific; do not apply blindly to another video'
P.mkdir(parents=True,exist_ok=True);(P/'review_inputs').mkdir(exist_ok=True);(P/'evidence').mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
def write(n,rows):
 with (P/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def notes(n):return [x.split('|') for x in (W/n).read_text().splitlines() if x]
s=json.loads((D/'01_SOURCE_INVENTORY'/f'{V}.json').read_text());source=s['actual_sha256'];dur=s['actual_duration_sec']
fm=json.loads((W/'FRAME_MANIFEST.json').read_text());assert fm['video_id']==V and fm['source_sha256']==source
rn=notes('review_notes.txt');assert len(rn)==len(fm['frames'])
timeline=[]
for f,(idx,desc,assets) in zip(fm['frames'],rn):
 assert f['observation_id']==f'G{int(idx):03d}' and sha(Path(f['local_frame']))==f['frame_sha256']
 t=f['source_seek_sec'];timeline.append(dict(video_id=V,observation_id=f['observation_id'],shot_id='NOT_SEGMENTED',start_sec=t,end_sec=t,source_seek_sec=t,observation_type='REVIEWED_POINT_SAMPLE_NOT_SHOT',description=desc,asset_ids=assets,source_sha256=source,frame_sha256=f['frame_sha256'],evidence_status='SCREEN_OBSERVED',interval_constancy='NOT_APPLICABLE'))
write('VISUAL_TIMELINE.csv',timeline)
assets=[]
for a in sorted({a for x in timeline for a in x['asset_ids'].split(';')}):
 rr=[x for x in timeline if a in x['asset_ids'].split(';')];assets.append(dict(video_id=V,asset_id=a,category=a.split('_')[0],first_observed_sec=min(x['source_seek_sec'] for x in rr),last_observed_sec=max(x['source_seek_sec'] for x in rr),observation_ids=';'.join(x['observation_id'] for x in rr),observed_appearances=len(rr),reuse_status='VISIBLE_DESIGN_FAMILY' if len(rr)>1 else 'SINGLE_REVIEWED_APPEARANCE',original_asset_file_identity='NOT_VERIFIED',source_sha256=source,note='Observed categories, not authored-file counts; identity names use caption/label context.'))
write('ASSET_OBSERVATIONS.csv',assets)
srt=json.loads((R/'data/extracted/channel-data/DS-000036/caption-tracks.json').read_text())['tracks'][V]['srt'];csha=hashlib.sha256(srt.encode()).hexdigest();caps=[]
def tc(t):
 h,m,z=t.strip().replace(',','.').split(':');return int(h)*3600+int(m)*60+float(z)
for b in re.split(r'\n\s*\n',srt.strip()):
 l=b.splitlines()
 if len(l)<3 or '-->' not in l[1] or not ' '.join(l[2:]).strip():continue
 a,z=l[1].split('-->');caps.append(dict(cue_id=l[0],start=tc(a),end=tc(z),text=' '.join(l[2:])))
def overlap(a,b):return [c for c in caps if c['start']<b and c['end']>a]
def obs(a,b):return ';'.join(x['observation_id'] for x in timeline if a<=x['source_seek_sec']<=b)
seq=json.loads((W/'TEMPORAL_MANIFEST.json').read_text());mn=notes('motion_notes.txt');assert len(seq)==len(mn)
motions=[];av=[]
for z,(sid,tech,description,recipe,purpose) in zip(seq,mn):
 assert z['sequence_id']==sid
 for f in z['frames']:assert sha(Path(f['local_frame']))==f['sha256']
 a,b=z['start_sec'],z['end_sec'];cc=overlap(a,b);times=[f['time_sec'] for f in z['frames']];step=max(y-x for x,y in zip(times,times[1:]))
 motions.append(dict(video_id=V,motion_id=sid,start_sec=a,end_sec=b,review_window_sec=b-a,observation_ids=obs(a,b),source_sample_times_sec=';'.join(str(t) for t in times),sample_frame_sha256s=';'.join(f['sha256'] for f in z['frames']),visible_technique=tech,observed_sequence=description,direction_and_transform='See observed_sequence; sampled transforms only',change_brackets='Sample bounds in source_sample_times_sec; not exact onset/duration',reported_change_bound_sec=round(step,6),actual_sampling_step_sec=round(step,6),reproduction_method_inferred=recipe,narrative_function_interpreted=purpose,caption_cue_ids=';'.join(c['cue_id'] for c in cc),easing='NOT_MEASURED',actual_authoring_method='UNKNOWN',source_sha256=source,evidence_status='SCREEN_OBSERVED_SEQUENCE;REPRODUCTION_METHOD_INFERRED',continuous_playback='NOT_PERFORMED'))
 av.append(dict(video_id=V,event_id='AV_'+sid,start_sec=a,end_sec=b,motion_id=sid,caption_cue_ids=';'.join(c['cue_id'] for c in cc),caption_context=' '.join(c['text'] for c in cc),visual_observation=description,audio_evidence='ASR_INFERRED',visual_evidence='SCREEN_OBSERVED',direct_audio='NOT_VERIFIED',sync_status='CAPTION_DISPLAY_OVERLAP_ONLY;NOT_WORD_ALIGNED',source_sha256=source,caption_sha256=csha))
write('MOTION_SEQUENCES.csv',motions);write('AUDIO_VISUAL_EVENTS.csv',av)
beats=[]
for i,(a,b,name,visual,purpose) in enumerate(notes('beat_notes.txt')):
 a,b=float(a),float(b);beats.append(dict(video_id=V,beat_id=f'B{i:03d}',start_sec=a,end_sec=b,beat=name,visible_structure=visual,interpretation_and_caveat=purpose,observation_ids=obs(a,b),caption_cue_ids=';'.join(c['cue_id'] for c in overlap(a,b)),source_sha256=source,evidence='SCREEN_OBSERVED_AND_AUTO_CAPTION_CONTEXT;NO_RETENTION_CLAIM'))
write('STORY_AND_EDITING_BEATS.csv',beats)
for n in ['review_notes.txt','motion_notes.txt','beat_notes.txt']:shutil.copyfile(W/n,P/'review_inputs'/n)
for n in ['thumbnail.jpg']:shutil.copyfile(W/n,P/'evidence'/n)
shutil.copyfile(W/'THUMBNAIL_PROVENANCE.json',P/'THUMBNAIL_PROVENANCE.json')
native=[dict(source_seek_sec=t,sha256=sha(W/n),resolution='1280x720') for n,t in [('character_native.png',144),('metaphor_native.png',780)]]
save('REVIEW_EVIDENCE.json',dict(video_id=V,source_sha256=source,reviewer='Single primary Codex agent; not independent reviewer',local_scratch=str(W),representative_manifest=[{k:v for k,v in f.items() if k!='local_frame'} for f in fm['frames']],temporal_manifest=[{**{k:v for k,v in z.items() if k!='frames'},'frames':[{k:v for k,v in f.items() if k!='local_frame'} for f in z['frames']]} for z in seq],native_frames=native,sampling='4-second point sampling plus selected temporal review; no complete shot census',decoder_warning='Two mmco: unref short failure warnings during initial point-seeking pass; exact seek not logged. Reviewed frames show no obvious corruption at contact-sheet scale. Full decode integrity NOT_CERTIFIED.'))
times=sorted({x['source_seek_sec'] for x in timeline}|{f['time_sec'] for z in seq for f in z['frames']});save('COVERAGE_MEASUREMENTS.json',dict(video_id=V,duration_sec=dur,reviewed_point_samples=len(timeline),reviewed_temporal_sequences=len(seq),reviewed_sequence_frame_entries=sum(len(z['frames']) for z in seq),unique_reviewed_sample_times=len(times),maximum_between_sample_gap_sec=max(b-a for a,b in zip(times,times[1:])),first_reviewed_sec=times[0],last_reviewed_sec=times[-1],container_tail_after_last_sample_sec=dur-times[-1],shot_count='NOT_CERTIFIED',all_visual_states_reviewed=False,nonblank_caption_cues=len(caps),caption_word_count_regex=len(re.findall(r"\b[\w'-]+\b",' '.join(c['text'] for c in caps))),metrics_warning='Fixed samples can miss short scenes; no measured edit cadence or exhaustive motion coverage.'))
log=(W/'audio_signal.log').read_text();overall=log.split('Overall')[-1];save('AUDIO_SIGNAL_MEASUREMENTS.json',dict(video_id=V,source_sha256=source,decode_exit_code=int((W/'audio_exit.txt').read_text()),log_sha256=sha(W/'audio_signal.log'),overall_statistics=overall.strip(),interpretation='Aggregate decoded signal only; not listening, voice/music/SFX classification or speech-only rate.'))
save('QA.json',dict(video_id=V,status='PENDING_VALIDATION',source_sha256=source,deep_forensic_status='PARTIAL_SAMPLED_VISUAL_AND_TEMPORAL_COVERAGE',independent_visual_review='NOT_PERFORMED',direct_audio_listening='NOT_PERFORMED',full_audiovisual_signoff='NOT_COMPLETE',limitations=['4-second samples are point observations, not an exhaustive shot/state segmentation.','27 targeted sequences do not certify all intervening motion or frame-exact timing/easing.','Initial seeking emitted two H.264 reference warnings; source hash reused, not rehashed; full video decode integrity unverified.','Audio decoded for signal measurements only; direct listening and exact narration/music/SFX sync unverified.','Charts, dramatized dialogue and economic claims remain source-video claims until external fact checks.','Current CDN thumbnail cannot certify upload-time packaging.','Native details reviewed by same primary agent, not independent QA.']))
print('Assembled',V,len(timeline),'stills',len(motions),'sequences',len(beats),'beats; QA pending')
