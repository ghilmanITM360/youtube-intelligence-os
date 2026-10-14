"""Validate sampled research provenance and referential integrity without source decode."""
import collections,csv,datetime,hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=R/'research/casual-economics-deep-dive-2026-10';V=sys.argv[1];P=D/'02_VIDEO_FORENSICS'/V;checks={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def read(n):return list(csv.DictReader((P/n).open()))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((D/'01_SOURCE_INVENTORY'/f'{V}.json').read_text());dur=s['actual_duration_sec'];sha=s['actual_sha256'];m=next(x for x in json.loads((R/'docs/research/finance/casual-economics/LOCAL_SOURCE_MANIFEST.json').read_text())['files'] if x['video_id']==V)
check('manifest_source_identity',sha==s['expected_sha256']==m['sha256'] and s['actual_size_bytes']==m['size_bytes'])
check('source_stream_records',bool(s['video_streams'] and s['audio_streams']))
t=read('VISUAL_TIMELINE.csv');a=read('ASSET_OBSERVATIONS.csv');mo=read('MOTION_SEQUENCES.csv');b=read('STORY_AND_EDITING_BEATS.csv');av=read('AUDIO_VISUAL_EVENTS.csv')
for name,rows,key in [('timeline',t,'observation_id'),('assets',a,'asset_id'),('motions',mo,'motion_id'),('beats',b,'beat_id'),('av',av,'event_id')]:
 check(name+'_nonempty',bool(rows));check(name+'_unique',len({x[key] for x in rows})==len(rows));check(name+'_source',all(x['video_id']==V and x['source_sha256']==sha for x in rows))
 if name!='assets':check(name+'_bounds',all(0<=float(x['start_sec'])<=float(x['end_sec'])<=dur for x in rows))
obs={x['observation_id'] for x in t};assets={x['asset_id'] for x in a};motions={x['motion_id'] for x in mo}
check('point_samples_not_fake_segments',all(x['start_sec']==x['end_sec'] and x['shot_id']=='NOT_SEGMENTED' and x['observation_type']=='REVIEWED_POINT_SAMPLE_NOT_SHOT' for x in t))
check('timeline_asset_links',all(set(x['asset_ids'].split(';'))<=assets for x in t))
check('asset_observation_links',all(set(x['observation_ids'].split(';'))<=obs for x in a))
check('asset_occurrence_counts',all(int(x['observed_appearances'])==sum(x['asset_id'] in z['asset_ids'].split(';') for z in t) for x in a))
check('motion_observation_links',all(set(filter(None,x['observation_ids'].split(';')))<=obs for x in mo))
check('beat_observation_links',all(set(filter(None,x['observation_ids'].split(';')))<=obs for x in b))
check('av_motion_links',all(x['motion_id'] in motions for x in av))
check('beats_partition_duration',float(b[0]['start_sec'])==0 and float(b[-1]['end_sec'])==dur and all(float(x['end_sec'])==float(y['start_sec']) for x,y in zip(b,b[1:])))
e=json.loads((P/'REVIEW_EVIDENCE.json').read_text());fm={f['observation_id']:f for f in e['representative_manifest']};sm={z['sequence_id']:z for z in e['temporal_manifest']}
check('evidence_identity',e['video_id']==V and e['source_sha256']==sha)
check('all_stills_evidence_linked',set(fm)==obs and all(x['frame_sha256']==fm[x['observation_id']]['frame_sha256'] and float(x['source_seek_sec'])==fm[x['observation_id']]['source_seek_sec'] for x in t))
check('all_sequences_evidence_linked',set(sm)==motions and all(x['sample_frame_sha256s'].split(';')==[f['sha256'] for f in sm[x['motion_id']]['frames']] for x in mo))
check('sequence_timestamps_match',all([float(z) for z in x['source_sample_times_sec'].split(';')]==[f['time_sec'] for f in sm[x['motion_id']]['frames']] for x in mo))
check('sequence_bounds',all(z['start_sec']==z['frames'][0]['time_sec'] and z['end_sec']==z['frames'][-1]['time_sec'] for z in sm.values()))
check('sequence_monotonic',all(all(x['time_sec']<y['time_sec'] for x,y in zip(z['frames'],z['frames'][1:])) for z in sm.values()))
check('no_unverified_workflow_claim',all(x['actual_authoring_method']=='UNKNOWN' and x['easing']=='NOT_MEASURED' for x in mo))
check('audio_labels_honest',all(x['direct_audio']=='NOT_VERIFIED' and 'NOT_WORD_ALIGNED' in x['sync_status'] for x in av))
srt=json.loads((R/'data/extracted/channel-data/DS-000036/caption-tracks.json').read_text())['tracks'][V]['srt'];csha=hashlib.sha256(srt.encode()).hexdigest();ids={z.splitlines()[0] for z in re.split(r'\n\s*\n',srt.strip()) if z}
check('caption_hashes',all(x['caption_sha256']==csha for x in av));check('caption_cue_links',all(set(filter(None,x['caption_cue_ids'].split(';')))<=ids for x in mo+b+av))
check('thumbnail_hash',digest(P/'evidence/thumbnail.jpg')==json.loads((P/'THUMBNAIL_PROVENANCE.json').read_text())['sha256'])
check('audio_signal_decode',json.loads((P/'AUDIO_SIGNAL_MEASUREMENTS.json').read_text())['decode_exit_code']==0)
c=json.loads((P/'COVERAGE_MEASUREMENTS.json').read_text());times=sorted({float(x['source_seek_sec']) for x in t}|{f['time_sec'] for z in sm.values() for f in z['frames']})
check('coverage_counts',c['reviewed_point_samples']==len(t) and c['reviewed_temporal_sequences']==len(mo) and c['reviewed_sequence_frame_entries']==sum(len(z['frames']) for z in sm.values()) and c['unique_reviewed_sample_times']==len(times))
check('coverage_gap',c['maximum_between_sample_gap_sec']==max(y-x for x,y in zip(times,times[1:]))<=4.001)
check('coverage_endpoints',times[0]==0 and 0<=dur-times[-1]<.25)
check('no_false_exhaustiveness',c['shot_count']=='NOT_CERTIFIED' and c['all_visual_states_reviewed'] is False)
check('review_notes_complete',len((P/'review_inputs/review_notes.txt').read_text().splitlines())==len(t) and len((P/'review_inputs/motion_notes.txt').read_text().splitlines())==len(mo))
check('reports_present',all((P/n).is_file() for n in ['VIDEO_REPORT.md','PACKAGING_AND_CLAIMS.md']))
check('compact_no_source_media',all(f.stat().st_size<1000000 and f.suffix.lower() not in {'.mp4','.wav','.mp3','.npz','.mov'} for f in P.rglob('*') if f.is_file()))
q=json.loads((P/'QA.json').read_text());check('qa_limitations_present',len(q['limitations'])>=6 and q['full_audiovisual_signoff']=='NOT_COMPLETE' and q['direct_audio_listening']=='NOT_PERFORMED' and q['independent_visual_review']=='NOT_PERFORMED')
q.update(status='PASS_STRUCTURAL',validation_count=len(checks),checks=checks,validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),validation_scope='Sampled point/temporal package integrity; not exhaustive scene census or AV signoff',files={f.name:{'bytes':f.stat().st_size,'sha256':digest(f)} for f in P.glob('*.csv')});(P/'QA.json').write_text(json.dumps(q,indent=2)+'\n');print(V,'PASS_STRUCTURAL',len(checks),'checks',len(t),'points',len(mo),'sequences',len(b),'beats; FULL_AV_NOT_COMPLETE')
