#!/usr/bin/env python3
"""Sample top-sorted top-level public comments (max 150, no replies) via yt-dlp android_vr client. Stores NO author names/ids/urls. Resumable."""
import json,subprocess,os,time,datetime,sys
A=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Y='/private/tmp/claude-501/venv/bin/yt-dlp'
ids=[l.split('\t') for l in open(A+'/raw/comment_sample_ids.tsv').read().splitlines() if l and not l.startswith('tGzCouGAu08')]
out=A+'/raw/comments_sample.jsonl'
done={json.loads(l)['video_id'] for l in open(out)} if os.path.exists(out) else set()
for v,role,title,ch,views in ids:
    if v in done: continue
    tmp=f'{A}/raw/comments_tmp/{v}'
    p=subprocess.run([Y,'--skip-download','--write-comments','--write-info-json','--extractor-args','youtube:player_client=android_vr;max_comments=150,150,0,0;comment_sort=top','-o',tmp,v],capture_output=True,text=True)
    f=tmp+'.info.json'
    if not os.path.exists(f): print(v,'FAILED',p.stderr[-150:].replace('\n',' '),flush=True); continue
    d=json.load(open(f)); cs=[dict(likes=c.get('like_count'),ts=c.get('timestamp'),text=c.get('text'),pinned=c.get('is_pinned'),by_uploader=c.get('author_is_uploader')) for c in (d.get('comments') or []) if not c.get('parent') or c.get('parent')=='root']
    open(out,'a').write(json.dumps(dict(video_id=v,role=role,title=title,channel=ch,views_at_sample=d.get('view_count'),comment_count_reported=d.get('comment_count'),n_sampled=len(cs),sort='top',sampled_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),comments=cs))+'\n')
    os.remove(f); print(v,len(cs),flush=True); time.sleep(4)
