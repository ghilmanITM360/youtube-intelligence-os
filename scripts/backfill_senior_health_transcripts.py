# usage: uv run --no-project --with yt-dlp python -I scripts/backfill_senior_health_transcripts.py [--limit N]
# Free caption backfill: per channel, latest 50 videos only (tiers 2,3,4; tier 1 already full). Creator caption (original lang) > auto <lang>-orig > auto <lang>. Never translations.
# Resumable (skips video_ids already in transcripts or in the coverage CSV). Stops on bot-check, never bypasses.
# Writes ONLY to data/catalog/senior_health_complete.db + research/senior-health-master/TRANSCRIPT_COVERAGE.csv.
import csv, hashlib, json, os, random, sqlite3, sys, time, urllib.request, datetime
import yt_dlp
R = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'
DB = f'{R}/data/catalog/senior_health_complete.db'; COV = f'{R}/research/senior-health-master/TRANSCRIPT_COVERAGE.csv'
GONE = ('Private video', 'unavailable', 'members', 'removed', 'terminated', 'confirm your age')  # age-gated = needs login, skipped as MISSING (not a bot-check)

def pick(info):
    lang = (info.get('language') or 'en').split('-')[0]
    man, auto = info.get('subtitles') or {}, info.get('automatic_captions') or {}
    for k in [lang] + sorted(x for x in man if x.split('-')[0] == lang and x != 'live_chat'):
        if k in man: return 'creator', k, man[k], lang
    for k in (f'{lang}-orig', lang):
        if k in auto: return 'auto', k, auto[k], lang
    return None, None, None, lang

def segs(j):
    out = []
    for e in j.get('events', []):
        if e.get('segs'):
            t = ''.join(s.get('utf8', '') for s in e['segs']).replace('\n', ' ').strip()
            if t: out.append((e['tStartMs'] / 1000, (e['tStartMs'] + e.get('dDurationMs', 0)) / 1000, t))
    return out

def main():
    # Per channel: latest 50 videos (yt-dlp flat list of the channel Videos tab), metadata rows added if missing, then captions. 5-minute break after every 5 channels.
    only = sys.argv[sys.argv.index('--channel') + 1] if '--channel' in sys.argv else None
    db = sqlite3.connect(DB)
    cov = {r['video_id']: r for r in csv.DictReader(open(COV))} if os.path.exists(COV) else {}
    chans = db.execute("select channel_id, name, tier from channels where tier != '1_FULL_PACKAGE' order by tier, name").fetchall()
    ydl = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True})
    flat = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'extract_flat': 'in_playlist', 'playlistend': 100})
    skip = int(sys.argv[sys.argv.index('--skip') + 1]) if '--skip' in sys.argv else 0  # first N channels were done under the old latest-50 plan
    def log(vid, st, why=''):
        cov[vid] = dict(video_id=vid, status=st, reason=why, retrieved_utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
        with open(COV + '.tmp', 'w', newline='') as f:
            w = csv.DictWriter(f, ['video_id', 'status', 'reason', 'retrieved_utc']); w.writeheader(); w.writerows(cov.values())
        os.replace(COV + '.tmp', COV)
    done = 0
    for ci, (ch, name, tier) in enumerate(chans, 1):
        if only and ch != only: continue
        if ci <= skip: continue
        ids, ferr = [], ''
        for a in range(3):
            try:
                ents = (flat.extract_info(f'https://www.youtube.com/channel/{ch}/videos', download=False) or {}).get('entries') or []
                ids = [e for e in ents if e and e.get('id') and len(e['id']) == 11][:100]; break
            except Exception as e:
                ferr = str(e).splitlines()[0][:200]
                if any(k in ferr.lower() for k in ('confirm you', 'not a bot', 'rate-limited')): print('BOT_CHECK — stopping:', ferr, flush=True); sys.exit(2)
                time.sleep(5 * (a + 1))
        st = dict(COMPLETE=0, PARTIAL=0, MISSING=0, RETRYABLE=0, SKIPPED_HAVE=0, TOO_NEW=0)
        # metadata for latest 100 (cheap); transcripts for 60: 30 newest + 20 most viewed + 10 least viewed (>=90 days old); gaps filled by recency
        for e in ids:
            db.execute('insert or ignore into videos(video_id,channel_id,url,title,duration_seconds,video_type,views,has_transcript,source) values(?,?,?,?,?,?,?,0,?)',
                       (e['id'], ch, f"https://www.youtube.com/watch?v={e['id']}", e.get('title'), int(e['duration']) if e.get('duration') else None, 'video', e.get('view_count'), 'yt-dlp_flat_latest100'))
            db.execute('update videos set views=? where video_id=? and views is null', (e.get('view_count'), e['id']))
        db.commit()
        seen = {r[0] for r in db.execute('select video_id from transcripts')}
        def run(e, min_age=None):
            vid = e['id']
            if vid in seen: st['SKIPPED_HAVE'] += 1; return 'SKIPPED_HAVE'
            if vid in cov and cov[vid]['status'] != 'RETRYABLE': st[cov[vid]['status']] += 1; return cov[vid]['status']
            time.sleep(6 + random.random() * 4)
            r = fetch_one(db, ydl, vid, ch, e.get('duration'), log, min_age); st[r] += 1; return r
        V = lambda e: e.get('view_count') or 0
        rest = ids[30:]
        chosen = {e['id'] for e in ids[:30]} | {e['id'] for e in sorted(rest, key=V, reverse=True)[:20]}
        for e in ids:
            if e['id'] in chosen: run(e)
        got = 0
        for e in sorted((e for e in rest if e['id'] not in chosen), key=V):
            if got >= 10: break
            if run(e, 90) != 'TOO_NEW': got += 1; chosen.add(e['id'])
        for e in ids:
            if len(chosen) >= 60: break
            if e['id'] not in chosen: chosen.add(e['id']); run(e)
        n = db.execute('select count(*) from videos where channel_id=?', (ch,)).fetchone()[0]
        t = db.execute('select count(*) from transcripts where video_id in (select video_id from videos where channel_id=?)', (ch,)).fetchone()[0]
        db.execute('update channels set videos_in_db=?, transcripts_in_db=? where channel_id=?', (n, t, ch)); db.commit()
        done += 1
        print(f'CHANNEL {ci}/{len(chans)} {name} | listed {len(ids)}{" ERR "+ferr if not ids else ""} | ' + ' '.join(f'{k}={v}' for k, v in st.items() if v) + f' | transcripts_total={t}', flush=True)
        if done % 5 == 0 and not only: print('BREAK 5 min after 5 channels', flush=True); time.sleep(300)

def fetch_one(db, ydl, vid, ch, dur, log, min_age=None):
    info, err = None, ''
    for a in range(3):
        try: info = ydl.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False); break
        except Exception as e:
            err = str(e).splitlines()[0][:300]
            if 'confirm your age' not in err.lower() and any(k in err.lower() for k in ('confirm you', 'not a bot', 'rate-limited')):
                log(vid, 'RETRYABLE', err); print('BOT_CHECK — stopping:', err, flush=True); sys.exit(2)
            if any(k in err for k in GONE): break
            time.sleep(5 * (a + 1))
    if info is None:
        gone = any(k in err for k in GONE); log(vid, 'MISSING' if gone else 'RETRYABLE', 'metadata: ' + err); return 'MISSING' if gone else 'RETRYABLE'
    if info.get('id') != vid or info.get('channel_id') != ch: log(vid, 'MISSING', f'identity mismatch ch={info.get("channel_id")}'); return 'MISSING'
    ud = info.get('upload_date')
    if min_age and ud and (datetime.datetime.now() - datetime.datetime.strptime(ud, '%Y%m%d')).days < min_age: return 'TOO_NEW'
    d = info.get('duration') or dur or 0
    src, track, fmts, lang = pick(info)
    if not src: log(vid, 'MISSING', 'no original-language caption track'); return 'MISSING'
    url = next((f['url'] for f in fmts if f.get('ext') == 'json3'), None); raw = None
    for a in range(3):
        try: raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read(); break
        except Exception as e:
            err = str(e)[:200]
            if '429' in err: print('RATE_LIMIT 429 on caption download — cooling down 15 min (no bypass)', flush=True); time.sleep(900)
            else: time.sleep(5 * (a + 1))
    s = segs(json.loads(raw)) if raw else []
    if not s: log(vid, 'RETRYABLE', 'caption empty/failed ' + err); return 'RETRYABLE'
    text = '\n'.join(f'[{a:09.3f}] {t}' for a, b, t in s)
    wc = sum(len(t.split()) for _, _, t in s); ratio = s[-1][1] / d if d else 1
    db.execute('insert or replace into transcripts values(?,?,?,?,?,?,?)', (vid, text, wc, lang, track + ('_creator' if src == 'creator' else '_auto'), hashlib.sha256(raw).hexdigest(), 'yt-dlp_caption'))
    db.execute('update videos set has_transcript=1 where video_id=?', (vid,)); db.commit()
    k = 'COMPLETE' if ratio >= 0.8 else 'PARTIAL'; log(vid, k, f'coverage {ratio:.0%}'); return k

if __name__ == '__main__': main()
