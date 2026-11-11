# usage: uv run --no-project --with yt-dlp python -I extract.py   (resumable; stops on bot-check, never bypasses)
# Newest-100 uploads for 5 channels that Apify capped at 40: yt-dlp metadata + creator/auto caption in ONE paced request per video.
import json, os, sys, time, random, sqlite3, datetime, urllib.request, hashlib
import yt_dlp
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, '/Users/ghilmankhan/YIOS-local-audits/2026-11-11-finance-economics-db-merge/pipeline')
import transcript_backfill as tb
DB = '/Users/ghilmankhan/workprojects/yios-audit-fixes/data/catalog/finance_economics_complete.db'
CH = {'UCFPfloFwa6X2UddqRH83rAA': 'aliciainvests', 'UCDokTQePVxNZUqmzevDM7NQ': 'ivaninvests', 'UCegPlgZVNg0g1pAzZtGH4dw': 'markretiredat55',
      'UCHKwo7_qXD8ixLZmpPlIb_w': 'tomlazyinvestor', 'UCKqgbX0MOmE5ZzyFpTP524g': 'tomtalksmoney'}
META = os.path.join(B, 'metadata.jsonl'); os.makedirs(os.path.join(B, 'transcripts'), exist_ok=True)
have = {r[0] for r in sqlite3.connect(DB).execute('select video_id from videos')}
done = {json.loads(l)['id'] for l in open(META)} if os.path.exists(META) else set()
lst = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'extract_flat': True, 'playlistend': 100})
ydl = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True})
ids = []
for cid in CH:
    es = lst.extract_info(f'https://www.youtube.com/channel/{cid}/videos', download=False)['entries'][:100]
    new = [e['id'] for e in es if e['id'] not in have]; print(cid, CH[cid], 'listed', len(es), 'new', len(new), flush=True)
    ids += [(cid, i) for i in new]
n = 0
for cid, vid in ids:
    if vid in done: continue
    if n: time.sleep(6 + random.random() * 4)
    n += 1; info = None
    for a in range(3):
        try: info = ydl.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False); break
        except Exception as e:
            err = str(e).splitlines()[0][:300]
            if any(k in err.lower() for k in ('confirm you', 'not a bot', 'rate-limited')): print('BOT_CHECK — stop', err); sys.exit(2)
            time.sleep(5 * (a + 1))
    if not info: print('FAIL', vid, err, flush=True); continue
    keep = {k: info.get(k) for k in ('id', 'title', 'description', 'upload_date', 'timestamp', 'duration', 'view_count', 'like_count', 'comment_count',
            'tags', 'categories', 'thumbnail', 'channel_id', 'channel', 'uploader_id', 'webpage_url', 'language', 'live_status', 'availability')}
    keep['retrieved_utc'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    src, track, fmts, lang = tb.pick(info); keep['caption'] = None
    if src:
        url = next((f['url'] for f in fmts if f.get('ext') == 'json3'), None); raw = None
        for a in range(3):
            try: raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read(); break
            except Exception: time.sleep(5 * (a + 1))
        if raw:
            segs = tb.segs_from_json3(json.loads(raw)); st, cov, why = tb.validate(segs, info.get('duration') or 0)
            tp = os.path.join(B, 'transcripts', f'{vid}.transcript.txt'); tb.write_transcript(tp, vid, {'channel_id': cid}, src, track, segs)
            open(os.path.join(B, 'transcripts', f'{vid}.{track}.json3'), 'wb').write(raw)
            keep['caption'] = dict(source=src, track=track, language=lang, status=st, coverage=cov, reason=why, words=sum(len(s[2].split()) for s in segs))
    with open(META, 'a') as f: f.write(json.dumps(keep, ensure_ascii=False) + '\n')
    print(n, len(ids), vid, (keep['caption'] or {}).get('status'), flush=True)
print('DONE')
