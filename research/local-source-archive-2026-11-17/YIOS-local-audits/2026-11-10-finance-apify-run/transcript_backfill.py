# usage: uv run --no-project --with yt-dlp python -I transcript_backfill.py [--only VID,VID] [--limit N]
# Caption-first transcript backfill for every inventory video (master + PR #39 frozen packages), unauthenticated.
# Priority: creator caption in original language > YouTube auto-caption (<lang>-orig, then <lang>). Never translations.
# Resumable: videos already COMPLETE in TRANSCRIPT_COVERAGE.csv are skipped. Stops on bot-check (never bypassed).
import csv, io, json, os, random, subprocess, sys, time, hashlib, urllib.request, datetime
import yt_dlp

B = os.path.dirname(os.path.abspath(__file__)); REPO = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'
PR39 = '967ea707:research/youtube-12-channel-metadata/channels/{}/VIDEO_MASTER.csv'
PR39_SLUGS = {'logicalmoney72': 'logicalmoney', 'markbuildsus': 'markinvests', 'primateeconomics': 'primate',
              'unclefrankretirement16': 'unclefrank', 'unclejohnfinancial': 'unclejohn'}
COV = os.path.join(B, 'TRANSCRIPT_COVERAGE.csv')
FIELDS = ['video_id', 'channel_id', 'channel_slug', 'inventory_source', 'title', 'duration_s', 'language', 'source', 'track',
          'status', 'segments', 'words', 'first_start_s', 'last_end_s', 'coverage_ratio', 'transcript_path', 'raw_path',
          'raw_sha256', 'retrieved_utc', 'reason']


def inventory():
    slug = {r['channel_id']: r['label'].split('_', 1)[1] for r in csv.DictReader(open(os.path.join(B, 'CHANNEL_STATUS.csv')))}
    inv = {}
    for l in open(os.path.join(B, 'FINANCE_VIDEO_MASTER_ALL.jsonl')):
        r = json.loads(l)
        inv[r['video_id']] = dict(channel_id=r['channel_id'], channel_slug=slug[r['channel_id']], inventory_source='finance_master',
                                  title=r['title'], duration_s=r['duration_seconds'])
    for s, sl in PR39_SLUGS.items():
        t = subprocess.run(['git', '-C', REPO, 'show', PR39.format(s)], capture_output=True, text=True, check=True).stdout
        for r in csv.DictReader(io.StringIO(t)):
            inv.setdefault(r['video_id'], dict(channel_id=r['channel_id'], channel_slug=sl, inventory_source='pr39_frozen_package',
                                               title=r['title'], duration_s=r['duration_seconds']))
    return inv


def pick(info):
    lang = (info.get('language') or 'en').split('-')[0]
    man, auto = info.get('subtitles') or {}, info.get('automatic_captions') or {}
    for k in [lang] + sorted(x for x in man if x.split('-')[0] == lang and x != 'live_chat'):
        if k in man: return 'youtube_creator_caption', k, man[k], lang
    for k in (f'{lang}-orig', lang):
        if k in auto: return 'youtube_auto_caption', k, auto[k], lang
    return None, None, None, lang


def segs_from_json3(j):
    out = []
    for e in j.get('events', []):
        if not e.get('segs'): continue
        t = ''.join(s.get('utf8', '') for s in e['segs']).replace('\n', ' ').strip()
        if t: out.append((e['tStartMs'] / 1000, (e['tStartMs'] + e.get('dDurationMs', 0)) / 1000, t))
    return out


def validate(segs, dur):
    if not segs: return 'MISSING', 0, 'caption track empty'
    cov = segs[-1][1] / dur if dur else None
    words = sum(len(s[2].split()) for s in segs)
    if cov is not None and cov < 0.8: return 'PARTIAL', cov, f'timestamps cover {cov:.0%} of duration'
    if dur and words / max(dur, 1) < 0.3: return 'PARTIAL', cov, f'low word density {words}/{dur}s'
    return 'COMPLETE', cov, ''


def write_transcript(path, vid, meta, src, track, segs):
    with open(path, 'w') as f:
        f.write(f'# video_id={vid} channel_id={meta["channel_id"]} source={src} track={track}\n')
        for a, b, t in segs: f.write(f'[{a:09.3f} --> {b:09.3f}] {t}\n')


def main():
    args = sys.argv[1:]; only = set(args[args.index('--only') + 1].split(',')) if '--only' in args else None
    limit = int(args[args.index('--limit') + 1]) if '--limit' in args else None
    inv = inventory()
    done = {r['video_id']: r for r in csv.DictReader(open(COV))} if os.path.exists(COV) else {}
    ydl = yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True})
    n = 0
    for vid, meta in inv.items():
        if only and vid not in only: continue
        if vid in done and done[vid]['status'] == 'COMPLETE': continue
        if limit is not None and n >= limit: break
        n += 1
        if n > 1: time.sleep(6 + random.random() * 4)  # pace every video, including failures
        row = dict(video_id=vid, **meta, retrieved_utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
        info, err = None, ''
        for attempt in range(3):
            try: info = ydl.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False); break
            except Exception as e:
                err = str(e).splitlines()[0][:300]
                if any(k in err.lower() for k in ('confirm you', 'not a bot', 'rate-limited')):
                    print('BOT_CHECK/RATE_LIMIT — stopping, not bypassing:', err, flush=True); done[vid] = {**row, 'status': 'RETRYABLE', 'reason': 'bot-check/rate-limit: ' + err}
                    save(done, inv); sys.exit(2)
                if any(k in err for k in ('Private video', 'unavailable', 'members', 'removed')): break
                time.sleep(5 * (attempt + 1))
        if info is None:
            gone = any(k in err for k in ('Private video', 'unavailable', 'members', 'removed'))  # confirmed gap vs transient (network/DNS)
            done[vid] = {**row, 'status': 'MISSING' if gone else 'RETRYABLE', 'reason': 'metadata fetch failed: ' + err}; print('FAIL', vid, err); save(done, inv); continue
        if info.get('id') != vid or info.get('channel_id') != meta['channel_id']:
            done[vid] = {**row, 'status': 'MISSING', 'reason': f'identity mismatch id={info.get("id")} ch={info.get("channel_id")}'}; save(done, inv); continue
        dur = info.get('duration') or float(meta['duration_s'] or 0)
        src, track, fmts, lang = pick(info)
        row.update(duration_s=dur, language=lang)
        if not src:
            done[vid] = {**row, 'status': 'MISSING', 'reason': 'no creator or auto caption track in original language'}; print('NOCAP', vid); save(done, inv); continue
        url = next((f['url'] for f in fmts if f.get('ext') == 'json3'), None)
        raw = None
        for attempt in range(3):
            try: raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read(); break
            except Exception as e: err = str(e)[:200]; time.sleep(5 * (attempt + 1))
        if not raw:
            done[vid] = {**row, 'source': src, 'track': track, 'status': 'RETRYABLE', 'reason': 'caption download failed/empty: ' + err}; print('EMPTY', vid); save(done, inv); continue
        d = os.path.join(B, 'transcripts', meta['channel_slug']); os.makedirs(os.path.join(d, 'raw'), exist_ok=True)
        rp = os.path.join(d, 'raw', f'{vid}.{track}.json3'); open(rp, 'wb').write(raw)
        segs = segs_from_json3(json.loads(raw)); status, cov, reason = validate(segs, dur)
        tp = os.path.join(d, f'{vid}.transcript.txt'); write_transcript(tp, vid, meta, src, track, segs)
        done[vid] = {**row, 'source': src, 'track': track, 'status': status, 'segments': len(segs), 'words': sum(len(s[2].split()) for s in segs),
                     'first_start_s': segs[0][0] if segs else '', 'last_end_s': segs[-1][1] if segs else '',
                     'coverage_ratio': round(cov, 3) if cov is not None else '', 'transcript_path': os.path.relpath(tp, B),
                     'raw_path': os.path.relpath(rp, B), 'raw_sha256': hashlib.sha256(raw).hexdigest(), 'reason': reason}
        print(status, vid, src, track, len(segs), flush=True); save(done, inv)
    save(done, inv)


def save(done, inv):
    tmp = COV + '.tmp'
    with open(tmp, 'w', newline='') as f:
        w = csv.DictWriter(f, FIELDS, extrasaction='ignore'); w.writeheader()
        for vid in inv:
            w.writerow(done.get(vid) or {'video_id': vid, **inv[vid], 'status': 'QUEUED'})
    os.replace(tmp, COV)


if __name__ == '__main__':
    main()
