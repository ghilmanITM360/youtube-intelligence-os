"""Validate committed research relationships without decoding or modifying source media."""
from pathlib import Path
import csv,json,hashlib,collections,re,datetime
R=Path(__file__).resolve().parents[3];D=R/'research/casual-economics-deep-dive-2026-10';V='Iwz0fhJWN9Q';P=D/'02_VIDEO_FORENSICS'/V
checks={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def read(n):return list(csv.DictReader((P/n).open()))
src=json.loads((D/'01_SOURCE_INVENTORY'/f'{V}.json').read_text());sha=src['actual_sha256'];dur=src['actual_duration_sec'];manifest=json.loads((R/'docs/research/finance/casual-economics/LOCAL_SOURCE_MANIFEST.json').read_text())['files']
for m in manifest:
 s=json.loads((D/'01_SOURCE_INVENTORY'/f'{m["video_id"]}.json').read_text());check('source_record_'+m['video_id'],s['actual_sha256']==m['sha256'] and s['expected_sha256']==m['sha256'] and s['actual_size_bytes']==m['size_bytes'] and s['status']=='PRESENT_HASH_VERIFIED' and bool(s['video_streams'] and s['audio_streams']))
check('eleven_unique_sources',len(manifest)==len({x['sha256'] for x in manifest})==11)
timeline=read('VISUAL_TIMELINE.csv');assets=read('ASSET_OBSERVATIONS.csv');motions=read('MOTION_SEQUENCES.csv');beats=read('STORY_AND_EDITING_BEATS.csv');av=read('AUDIO_VISUAL_EVENTS.csv');assetids={x['asset_id'] for x in assets};obsids={x['observation_id'] for x in timeline};motionids={x['motion_id'] for x in motions}
for name,rows,key in [('timeline',timeline,'observation_id'),('assets',assets,'asset_id'),('motions',motions,'motion_id'),('beats',beats,'beat_id'),('av',av,'event_id')]:
 check(name+'_unique',len({x[key] for x in rows})==len(rows));check(name+'_source',all(x['video_id']==V and x['source_sha256']==sha for x in rows))
 if name!='assets':check(name+'_bounds',all(0<=float(x['start_sec'])<=float(x['end_sec'])<=dur for x in rows))
check('275_representatives_42_supplements',len(timeline)==317 and sum(x['observation_type']=='REVIEWED_REPRESENTATIVE_OF_CANDIDATE_INTERVAL' for x in timeline)==275)
check('asset_links',all(set(x['asset_ids'].split(';'))<=assetids for x in timeline))
check('asset_occurrence_links',all(set(x['observation_ids'].split(';'))<=obsids for x in assets))
check('motion_observation_links',all(set(filter(None,x['observation_ids'].split(';')))<=obsids for x in motions))
check('av_motion_links',all(x['motion_id'] in motionids for x in av))
check('beats_full_duration',float(beats[0]['start_sec'])==0 and float(beats[-1]['end_sec'])==dur and all(float(a['end_sec'])==float(b['start_sec']) for a,b in zip(beats,beats[1:])))
check('audio_labels_honest',all(x['direct_audio']=='NOT_VERIFIED' and 'NOT_WORD_ALIGNED' in x['sync_status'] for x in av))
check('no_easing_claim',all(x['easing']=='NOT_MEASURED' and x['actual_authoring_method']=='UNKNOWN' for x in motions))
ev=json.loads((P/'REVIEW_EVIDENCE.json').read_text());check('evidence_counts',len(ev['representative_manifest'])==275 and len(ev['supplement_manifest'])==42 and len(ev['temporal_manifest'])==34 and len(ev['native_frames'])==4)
frames={x['state_id']:x for x in ev['representative_manifest']};frames.update({x['supplement_id']:x for x in ev['supplement_manifest']})
check('timeline_frame_hashes',all(x['frame_sha256']==frames[x['observation_id']]['frame_sha256'] for x in timeline))
check('sequence_frame_hashes',all(m['sample_frame_sha256s'].split(';')==[f['sha256'] for f in s['frames']] for m,s in zip(motions,ev['temporal_manifest'])))
thumb=json.loads((P/'THUMBNAIL_PROVENANCE.json').read_text());check('thumbnail_bytes',hashlib.sha256((P/'evidence/thumbnail.jpg').read_bytes()).hexdigest()==thumb['sha256'])
check('audio_signal_decode',json.loads((P/'AUDIO_SIGNAL_MEASUREMENTS.json').read_text())['decode_exit_code']==0)
cap=json.loads((R/'data/extracted/channel-data/DS-000036/caption-tracks.json').read_text())['tracks'][V]['srt'];capids={b.splitlines()[0] for b in re.split(r'\n\s*\n',cap.strip()) if b};check('caption_provenance',all(x['caption_sha256']==hashlib.sha256(cap.encode()).hexdigest() for x in av));check('caption_ids',all(set(filter(None,x['caption_cue_ids'].split(';')))<=capids for x in av+motions+beats))
check('required_reports',all((P/n).is_file() for n in ['VIDEO_REPORT.md','PACKAGING_AND_CLAIMS.md','VISUAL_TIMELINE.csv','ASSET_OBSERVATIONS.csv','MOTION_SEQUENCES.csv','STORY_AND_EDITING_BEATS.csv','AUDIO_VISUAL_EVENTS.csv']))
check('no_source_media',not any(p.suffix.lower() in {'.mp4','.mkv','.mov','.wav','.mp3','.npz'} for p in D.rglob('*') if p.is_file()))
check('compact_files',all(p.stat().st_size<1000000 for p in D.rglob('*') if p.is_file()))
# Historical tables are reused, not rebuilt. Compare complete row multisets.
old=R/'data/extracted/forensic-analysis/casual-economics/2026-10-12';counts={};done=[p.parent for p in (old/'02_VIDEO_FORENSICS').glob('*/QA.json')]
for master in (old/'03_MASTER_DATA').glob('*.csv'):
 with master.open() as f:reader=csv.DictReader(f);fields=reader.fieldnames;master_rows=list(reader)
 combined=[]
 for p in done:
  table=p/master.name.replace('MASTER_','',1)
  if table.exists():combined+=list(csv.DictReader(table.open()))
 canonical=lambda rr:collections.Counter(tuple(x.get(k,'') for k in fields) for x in rr)
 check('historical_master_'+master.stem,canonical(master_rows)==canonical(combined));counts[master.stem]=len(master_rows)
check('historical_master_total',len(counts)==10 and sum(counts.values())==18091)
for file in D.rglob('*.py'):compile(file.read_text(),str(file),'exec')
qa=json.loads((P/'QA.json').read_text());qa.update(status='PASS_STRUCTURAL',checks=checks,validation_count=len(checks),validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),historical_master_counts=counts,files={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in P.glob('*.csv')});(P/'QA.json').write_text(json.dumps(qa,indent=2)+'\n');print('PASS_STRUCTURAL',len(checks),'checks;',len(timeline),'observations;',len(motions),'sequences;',len(beats),'beats; historical master rows',sum(counts.values()));print('Deep mechanism coverage PARTIAL; full AV NOT_COMPLETE')
