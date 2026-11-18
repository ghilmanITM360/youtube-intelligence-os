#!/usr/bin/env python3
"""Merge Apify refresh R1+R2+R3 (2026-11-18) into data/catalog/finance_economics_complete.db.
Rules: no duplicates (key video_id); existing rows are UPDATED, not replaced: published fills if empty, views/likes/comments/thumbnail refreshed,
the previous values kept in video_snapshots (batch PRE) next to the new ones (batch FRESH); existing transcripts are kept; new videos inserted with
transcript when present; new channels inserted. Run from repo root: python3 -I <this file>. Idempotent."""
import json, re, sqlite3, hashlib, glob, os
ROOT = os.getcwd()
DB = ROOT + '/data/catalog/finance_economics_complete.db'
RAW = ROOT + '/research/new-finance-channel/05_FRESH_COMPETITOR_DATA/raw/'
BATCH = 'apify_2026-11-18_R123'; SNAP = '2026-11-18'
def dur(s):
    t = 0
    for x in [int(x) for x in (s or '0').split(':')]: t = t * 60 + x
    return t
def srt_text(srt):
    return re.sub(r'\s+', ' ', ' '.join(l.strip() for l in srt.splitlines() if l.strip() and not l.strip().isdigit() and '-->' not in l)).strip()
c = sqlite3.connect(DB)
c.execute("create table if not exists video_snapshots(video_id text, snapshot_date text, views integer, likes integer, comments integer, subscribers_channel integer, batch text, primary key(video_id, snapshot_date, batch))")
c.execute("create table if not exists channel_snapshots(channel_id text, snapshot_date text, subscribers integer, channel_total_videos integer, batch text, primary key(channel_id, snapshot_date, batch))")
stats = dict(new_videos=0, updated=0, dated=0, new_tx=0, new_channels=0)
for f in sorted(glob.glob(RAW + 'R*.json')):
    for r in json.load(open(f)):
        if not r.get('id') or r.get('type') not in ('video', 'shorts'): continue
        vid, cid = r['id'], r['channelId']
        ch = c.execute("select subscribers,channel_total_videos from channels where channel_id=?", (cid,)).fetchone()
        if ch is None:
            c.execute("insert into channels(channel_id,name,handle,url,niche,sub_niche,availability,subscribers,channel_total_videos,channel_total_views,joined,description,data_category,sources) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (cid, r['channelName'], '@' + r['channelUsername'], r['channelUrl'], 'FINANCE', 'see research/new-finance-channel inventory', 'AVAILABLE', r.get('numberOfSubscribers'), r.get('channelTotalVideos'), r.get('channelTotalViews'), r.get('channelJoinedDate'), r.get('channelDescription'), 'PARTIAL', BATCH)); stats['new_channels'] += 1
        else:
            c.execute("insert or ignore into channel_snapshots values(?,?,?,?,?)", (cid, 'PRE', ch[0], ch[1], 'PRE_' + BATCH))
            c.execute("update channels set subscribers=?, channel_total_videos=coalesce(?,channel_total_videos) where channel_id=?", (r.get('numberOfSubscribers'), r.get('channelTotalVideos'), cid))
        c.execute("insert or ignore into channel_snapshots values(?,?,?,?,?)", (cid, SNAP, r.get('numberOfSubscribers'), r.get('channelTotalVideos'), BATCH))
        old = c.execute("select published,views,likes,comments,sources,has_transcript from videos where video_id=?", (vid,)).fetchone()
        sub_ = (r.get('subtitles') or [None])[0]
        txt = srt_text(sub_['srt']) if sub_ and sub_.get('srt') else None
        if old is None:
            c.execute("insert into videos(video_id,channel_id,url,title,published,duration_seconds,video_type,views,likes,comments,description,hashtags,keywords,thumbnail_url,thumbnail_source,metadata_level,has_transcript,sources) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (vid, cid, r['url'], r['title'], r['date'], dur(r.get('duration')), {'video': 'REGULAR', 'shorts': 'SHORT'}[r['type']], r.get('viewCount'), r.get('likes'), r.get('commentsCount'), r.get('text'), json.dumps(r.get('hashtags') or []), '', r.get('thumbnailUrl'), 'captured', 'FULL', 1 if txt else 0, BATCH)); stats['new_videos'] += 1
        else:
            c.execute("insert or ignore into video_snapshots values(?,?,?,?,?,?,?)", (vid, 'PRE', old[1], old[2], old[3], None, 'PRE_' + BATCH))
            if not old[0]: stats['dated'] += 1
            c.execute("update videos set published=coalesce(nullif(published,''),?), views=coalesce(?,views), likes=coalesce(?,likes), comments=coalesce(?,comments), thumbnail_url=coalesce(?,thumbnail_url), thumbnail_source=case when ?>'' then 'captured' else thumbnail_source end, metadata_level='FULL', sources=case when sources like ? then sources else coalesce(sources,'')||';'||? end where video_id=?",
                      (r['date'], r.get('viewCount'), r.get('likes'), r.get('commentsCount'), r.get('thumbnailUrl'), r.get('thumbnailUrl') or '', '%' + BATCH + '%', BATCH, vid)); stats['updated'] += 1
        c.execute("insert or ignore into video_snapshots values(?,?,?,?,?,?,?)", (vid, SNAP, r.get('viewCount'), r.get('likes'), r.get('commentsCount'), r.get('numberOfSubscribers'), BATCH))
        if txt and not c.execute("select 1 from transcripts where video_id=?", (vid,)).fetchone():
            c.execute("insert into transcripts values(?,?,?,?,?,?,?,?,?)", (vid, 'youtube_auto_caption' if sub_.get('type') == 'auto_generated' else 'youtube_creator_caption', 'en-orig' if sub_.get('type') == 'auto_generated' else 'en', sub_.get('language', 'en'), 'COMPLETE', txt, len(txt.split()), hashlib.sha256(txt.encode()).hexdigest(), BATCH))
            c.execute("update videos set has_transcript=1 where video_id=?", (vid,)); stats['new_tx'] += 1
        c.execute("delete from apify_rows where video_id=? and batch=?", (vid, BATCH))
        c.execute("insert into apify_rows values(?,?,?,?)", (vid, cid, BATCH, json.dumps(r, ensure_ascii=False)))
c.execute("update channels set videos_in_db=(select count(*) from videos v where v.channel_id=channels.channel_id), transcripts_in_db=(select count(*) from transcripts t join videos v using(video_id) where v.channel_id=channels.channel_id), thumbnails_in_db=(select count(*) from videos v where v.channel_id=channels.channel_id and thumbnail_url is not null and thumbnail_url<>'') where channel_id in (select distinct channel_id from videos where sources like ?)", ('%' + BATCH + '%',))
c.execute("update channels set availability_note=coalesce(availability_note||'; ','')||'name on YouTube 2026-11-18: The Wealth Cortex' where name='Nostalgic Wheels' and coalesce(availability_note,'') not like '%Wealth Cortex%'")
c.commit(); print(stats); print(c.execute("pragma integrity_check").fetchone(), c.execute("select count(*),count(distinct video_id) from videos").fetchone())
