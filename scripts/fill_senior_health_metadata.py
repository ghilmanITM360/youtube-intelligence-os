# usage: uv run --no-project --with yt-dlp python -I scripts/fill_senior_health_metadata.py
# Fills metadata for the 25 "new + good views" senior-health channels (REMAINING_CHANNELS_NEW_GOOD_VIEWS.csv) in the local working DB:
#  1) thumbnail_url for every video (deterministic i.ytimg.com/vi/<id>/hqdefault.jpg)  2) latest-100 video list + full metadata for channels that have 0 videos.
# No cookies, no bypass; stops on bot-check. Resumable (skips video_ids already in videos).
import csv, json, sqlite3, sys, time, random
import yt_dlp
R = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'
db = sqlite3.connect(f'{R}/data/catalog/senior_health_complete.db')
chs = [r['url'].rsplit('/', 1)[1] for r in csv.DictReader(open(f'{R}/research/senior-health-master/REMAINING_CHANNELS_NEW_GOOD_VIEWS.csv'))]
flat = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'extract_flat': 'in_playlist', 'playlistend': 100})
ydl = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True})
for ch in chs:
    if db.execute('select count(*) from videos where channel_id=?', (ch,)).fetchone()[0] == 0:
        try: ents = (flat.extract_info(f'https://www.youtube.com/channel/{ch}/videos', download=False) or {}).get('entries') or []
        except Exception as e: print('SKIP', ch, str(e).splitlines()[0][:160], flush=True); continue  # e.g. terminated channel
        ids = [e['id'] for e in ents if e and len(e.get('id', '')) == 11][:100]
        for i in ids:
            time.sleep(2 + random.random() * 2)
            try: x = ydl.extract_info(f'https://www.youtube.com/watch?v={i}', download=False)
            except Exception as e:
                m = str(e).lower()
                if 'not a bot' in m or 'confirm you' in m or 'rate' in m: print('BOT_CHECK — stopping', m[:150]); sys.exit(2)
                continue
            if x.get('channel_id') != ch: continue
            d = x.get('upload_date') or ''
            db.execute('insert or ignore into videos(video_id,channel_id,url,title,published,duration_seconds,video_type,views,likes,comments,description,hashtags,keywords,has_transcript,source) values(?,?,?,?,?,?,?,?,?,?,?,?,?,0,?)',
                (i, ch, f'https://www.youtube.com/watch?v={i}', x.get('title'), f'{d[:4]}-{d[4:6]}-{d[6:]}' if d else None, x.get('duration'), 'video', x.get('view_count'), x.get('like_count'), x.get('comment_count'),
                 x.get('description'), json.dumps(x.get('tags') or []), None, 'yt-dlp_full_latest100'))
            db.commit()
        print('LISTED', ch, len(ids), flush=True)
    db.execute("update videos set thumbnail_url='https://i.ytimg.com/vi/'||video_id||'/hqdefault.jpg' where channel_id=? and thumbnail_url is null", (ch,))
    n, t = db.execute('select count(*), sum(has_transcript) from videos where channel_id=?', (ch,)).fetchone()
    db.execute('update channels set videos_in_db=?, transcripts_in_db=? where channel_id=?', (n, t or 0, ch)); db.commit()
print('DONE')
