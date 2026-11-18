#!/usr/bin/env python3
"""Add the 4 Apify datasets (2026-11-18) to niche DBs. Monkey Economics -> finance DB; Primate Science -> science DB.
Schema = finance_economics_complete.db. Run from repo root: python3 -I <this file>. Idempotent (INSERT OR REPLACE by key)."""
import json, re, sqlite3, hashlib, os, sys
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(H)
FIN = os.path.join(C, 'finance_economics_complete.db'); SCI = os.path.join(C, 'science_complete.db')
BATCH = 'apify_2026-11-18'
FILES = [('monkeyeconomics_videos_fcONxAeiuoalTdytW.json', FIN, 'FINANCE', 'finance/economics explained with a monkey (animation)'),
         ('monkeyeconomics_shorts_mKe8JMN7uKclbmCNz.json', FIN, 'FINANCE', 'finance/economics explained with a monkey (animation)'),
         ('primatescience_videos_3WH1iLiSqSfDcB66b.json', SCI, 'SCIENCE', 'science concepts explained with a monkey (animation)'),
         ('primatescience_shorts_SzXTtdClCedfGZpmv.json', SCI, 'SCIENCE', 'science concepts explained with a monkey (animation)')]
SCHEMA = [r for r in sqlite3.connect(FIN).execute("select sql from sqlite_master where sql is not null")]
def dur(s):
    p = [int(x) for x in (s or '0').split(':')]; t = 0
    for x in p: t = t * 60 + x
    return t
def srt_text(srt):
    out = []
    for l in srt.splitlines():
        l = l.strip()
        if not l or l.isdigit() or '-->' in l: continue
        out.append(l)
    return re.sub(r'\s+', ' ', ' '.join(out)).strip()
VT = {'video': 'REGULAR', 'shorts': 'SHORT'}
for fn, db, niche, sub in FILES:
    rows = json.load(open(os.path.join(H, fn)))
    if not os.path.exists(db):
        c = sqlite3.connect(db)
        for (s,) in SCHEMA:
            if not s.startswith('CREATE') or 'sqlite_autoindex' in s: continue
            c.execute(s)
        c.commit(); c.close()
    c = sqlite3.connect(db)
    for r in rows:
        cid = r['channelId']; vid = r['id']
        c.execute("insert or ignore into channels(channel_id,name,handle,url,niche,sub_niche,availability,subscribers,channel_total_videos,channel_total_views,joined,description,data_category,sources) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (cid, r['channelName'], '@' + r['channelUsername'], r['channelUrl'], niche, sub, 'AVAILABLE', r.get('numberOfSubscribers'), r.get('channelTotalVideos'), r.get('channelTotalViews'), r.get('channelJoinedDate'), r.get('channelDescription'), 'COMPLETE', BATCH))
        sub_ = (r.get('subtitles') or [None])[0]
        txt = srt_text(sub_['srt']) if sub_ and sub_.get('srt') else None
        c.execute("insert or replace into videos(video_id,channel_id,url,title,published,duration_seconds,video_type,views,likes,comments,description,hashtags,keywords,thumbnail_url,thumbnail_source,metadata_level,has_transcript,sources) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (vid, cid, r['url'], r['title'], r['date'], dur(r.get('duration')), VT[r['type']], r.get('viewCount'), r.get('likes'), r.get('commentsCount'), r.get('text'), json.dumps(r.get('hashtags') or []), '', r.get('thumbnailUrl'), 'captured', 'FULL', 1 if txt else 0, BATCH))
        if txt:
            c.execute("insert or replace into transcripts values(?,?,?,?,?,?,?,?,?)",
                      (vid, 'youtube_auto_caption' if sub_.get('type') == 'auto_generated' else 'youtube_creator_caption', 'en-orig' if sub_.get('type') == 'auto_generated' else 'en', sub_.get('language', 'en'), 'COMPLETE', txt, len(txt.split()), hashlib.sha256(txt.encode()).hexdigest(), BATCH))
        c.execute("delete from apify_rows where video_id=? and batch=?", (vid, BATCH))
        c.execute("insert into apify_rows values(?,?,?,?)", (vid, cid, BATCH, json.dumps(r, ensure_ascii=False)))
    for cid, in c.execute("select distinct channel_id from videos where sources=?", (BATCH,)).fetchall():
        c.execute("update channels set reported_videos=channel_total_videos, videos_in_db=(select count(*) from videos where channel_id=?), transcripts_in_db=(select count(*) from transcripts t join videos v using(video_id) where v.channel_id=?), thumbnails_in_db=(select count(*) from videos where channel_id=? and thumbnail_url is not null) where channel_id=?", (cid, cid, cid, cid))
    c.commit(); c.close()
for db in (FIN, SCI):
    c = sqlite3.connect(db); print(os.path.basename(db), c.execute("select name,videos_in_db,transcripts_in_db,reported_videos from channels where data_category='COMPLETE' and sources like ?", ('%' + BATCH + '%',)).fetchall(), c.execute("pragma integrity_check").fetchone())
