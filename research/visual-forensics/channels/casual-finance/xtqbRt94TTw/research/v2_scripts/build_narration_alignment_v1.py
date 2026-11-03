import pathlib,json,csv,math,hashlib
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');O=R/'production_v1';O.mkdir(exist_ok=True)
a=json.loads((R/'asr/asr_whisper_base_v1.json').read_text());partition=list(csv.DictReader((R/'integrated_v1/frame_partition_provisional.csv').open()));rows=[];segments=[]
for x in a['segments']:
 assert x['end']>=x['start']>=0
 matches=[]
 for p in partition:
  start=(int(p['start'])+1)/24;end=(int(p['end'])+2)/24;overlap=max(0,min(end,x['end'])-max(start,x['start']))
  if overlap>0:matches.append((p,overlap))
 for p,overlap in matches:
  rows.append(dict(video_id='xtqbRt94TTw',asr_id=x['id'],asr_start_s=x['start'],asr_end_s=x['end'],asr_text=x['text'],partition_id=p['partition_id'],partition_kind=p['kind'],source_start_pts=(int(p['start'])+1)/24,source_end_exclusive_pts=(int(p['end'])+2)/24,overlap_seconds=round(overlap,6),audio_method='WHISPER_BASE_ASR_UNCERTIFIED',actual_listening='NO',visual_relation='UNREVIEWED_NOT_INFERRED_FROM_TIME_OVERLAP',limitations='sentence timestamps; overlap is numerical only; no word timing, sound cues or semantic alignment certification'))
 segments.append((x['start'],x['end']))
with (O/'asr_visual_overlap_v1.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
union=0;right=0
for l,r in sorted(segments):union+=max(0,r-max(l,right));right=max(right,r)
stats={'segments':len(a['segments']),'alignment_overlap_rows':len(rows),'audio_duration_s':827.670522,'asr_segment_union_seconds':round(union,3),'asr_temporal_envelope':[min(x[0] for x in segments),max(x[1] for x in segments)],'actual_listening_seconds':0,'asr_label':'ASR_UNCERTIFIED_NOT_LISTENING','semantic_narration_visual_alignment':'PENDING_INDEPENDENT_REVIEW','video_first_pts':1/24,'video_last_frame_pts':19862/24,'video_end_exclusive_pts':19863/24,'audio_before_video_first_pts_seconds':1/24,'audio_after_video_end_exclusive_seconds':round(827.670522-19863/24,6),'time_mapping':'measured original video PTS=(frame+1)/24; audio ASR timestamps relative to source audio start0; frame end exclusive=(frame+2)/24','untranscribed_intervals':'ASR silence/unrecognized gaps not certified silence; final segment ends820.76s and audio lasts827.670522s'}
(O/'asr_alignment_stats_v1.json').write_text(json.dumps(stats,indent=2))
(O/'AUDIO_REVIEW_BLOCKER_v1.md').write_text('''# Actual listening remains unavailable
Current tool harness has image inspection and local ASR execution but no qualified source-audio listening/perception channel. No human listening receipt was found. Actual listening: 0 seconds. ASR processed the full decoded source audio into199 tentative sentence segments; transcription is not hearing.
Do not certify speech stress, music, SFX, BPM, silence, auditory synchronization or full AV sign-off. An actual qualified listener must play the source from audio0 through827.670522 seconds, log time spans, compare numeric words and on-screen values, and inspect claimed cuts/sound reveals together. The final untranscribed interval820.76–827.670522 especially needs hearing; do not label it silent.
Numerical overlap table is not semantic narration/visual alignment. All financial assertions remain unverified source claims; no external fact-checking was requested/performed.
''')
print(stats)
