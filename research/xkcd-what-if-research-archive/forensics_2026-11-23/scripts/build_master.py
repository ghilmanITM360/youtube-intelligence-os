import csv,json,os,re,collections
R='/Users/ghilmanislam360/Documents/youtube-intelligence-os/'
V=R+'research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/'
cen={r['video_id']:r for r in csv.DictReader(open(V+'census/census.csv'))}
pr={r['video_id']:r for r in csv.DictReader(open('media_probe_88.csv'))}
inv={i['id']:i for i in json.load(open(R+'research/what-if-scripts/analysis/inventory.json'))}
mx={r['video_id']:r for r in csv.DictReader(open(V+'campaign/campaign_matrix.csv'))}
a=os.path.expanduser('~/Documents/YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU/')
rows=[]
for vid,c in cen.items():
    d=V+'videos/'+vid
    has_gate=os.path.exists(d+'/quality_gate.json'); has_tab=os.path.isdir(d+'/tables')
    asr=os.path.isdir(d+'/asr') and bool(os.listdir(d+'/asr'))
    shots=os.path.exists(d+'/shot_ledger.csv')
    p=pr.get(vid)
    media='FULL_MEDIA_AVAILABLE' if p else 'MISSING'
    tx=vid in inv
    if p and has_gate: tier='TARGETED_VISUAL'
    elif p and has_tab: tier='STRUCTURAL_ONLY'
    elif p and tx: tier='TRANSCRIPT_ONLY'
    elif p: tier='MEDIA_ONLY_NO_ANALYSIS'
    else: tier='UNAVAILABLE'
    if media=='FULL_MEDIA_AVAILABLE' and not tx and not asr: cls='FULL_MEDIA_AVAILABLE_NO_TRANSCRIPT'
    else: cls=media
    rows.append(dict(video_id=vid,url=c['canonical_url'],title=c['title'],publish_date=c['publish_datetime'][:10],duration_s_census=c['duration_s'],format=c['format_class'],views_2026_11_04=c['views_player'],
      local_media_status=cls,local_media_path=p['path'] if p else '',sha256=p['sha256'] if p else '',res=(p['width']+'x'+p['height']) if p else '',fps=p['fps'] if p else '',duration_s_ffprobe=round(float(p['duration']),3) if p else '',has_audio=p['has_audio'] if p else '',
      catalog_transcript=('V%s'%inv[vid]['vid'][1:] if tx else 'NONE'),caption_type=inv[vid]['caption_type'] if tx else '',words=inv[vid]['words'] if tx else '',local_asr_whisper=('YES_PROVISIONAL' if asr else 'NO'),
      script_audit=('V%s'%inv[vid]['vid'][1:]+' DONE' if tx else 'NONE'),visual_tier=tier,per_video_gate=('quality_gate.json (VISUAL_ANALYSIS_PARTIAL)' if has_gate else ''),shot_ledger='YES' if shots else 'NO',
      campaign_role=mx[vid]['role'] if vid in mx else '',live_rss_2026_11_23='LISTED' if vid in open('rss_2026-11-23.xml').read() else 'not in latest-15'))
rows.append(dict(video_id='Aony69nO5kI',url='https://www.youtube.com/watch?v=Aony69nO5kI',title='What if we tried to eat the sun?',publish_date='2026-11-17',format='UNCLASSIFIED',local_media_status='MISSING',visual_tier='UNAVAILABLE',catalog_transcript='NONE',live_rss_2026_11_23='LISTED',campaign_role='POST_CENSUS_UPLOAD'))
w=csv.DictWriter(open('03_CHANNEL_MASTER_INVENTORY.csv','w'),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows)); 
for k in ('local_media_status','visual_tier'): print(k,collections.Counter(r[k] for r in rows))
print(collections.Counter((r['format'],r['visual_tier']) for r in rows))
print('transcript',collections.Counter(r['catalog_transcript']!='NONE' for r in rows),'asr',collections.Counter(r['local_asr_whisper'] for r in rows if 'local_asr_whisper' in r))
xw=csv.DictWriter(open('03_VIDEO_IDENTITY_CROSSWALK.csv','w'),fieldnames=['video_id','script_vid','census_title','media_sha256','campaign_hash_match','census_hash_match','brain_srcid_note'])
xw.writeheader()
h=json.load(open(V+'campaign/source_hashes_all_2026-11-06.json'))
for vid,c in cen.items():
    p=pr.get(vid)
    xw.writerow(dict(video_id=vid,script_vid=inv[vid]['vid'] if vid in inv else '',census_title=c['title'],media_sha256=p['sha256'] if p else '',campaign_hash_match=('MATCH' if p and vid in h and h[vid]['sha256']==p['sha256'] else ('NOT_IN_CAMPAIGN_HASHES' if vid not in h else 'DIFF')),census_hash_match=('MATCH' if p and p['sha256'] in c['local_sha256'] else ''),brain_srcid_note=''))
