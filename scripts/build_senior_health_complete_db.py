#!/usr/bin/env python3
"""Build data/catalog/senior_health_complete.db: every senior-health channel, video, description,
transcript and raw record in the repo, in one SQLite file. Read-only on all sources; rebuildable."""
import glob, gzip, json, os, sqlite3
R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INV = f"{R}/docs/research/senior-health-2026-09-25/forensic-v3/SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.json"
REG = f"{R}/data/catalog/youtube_channel_registry.db"
NEW = f"{R}/research/senior-health-apify-2026-11-11/senior_health_apify.db"
OUT = f"{R}/data/catalog/senior_health_complete.db"

def secs(s):
    try:
        p = [int(x) for x in str(s).split(":")]; r = 0
        for x in p: r = r * 60 + x
        return r
    except Exception: return None

if os.path.exists(OUT): os.remove(OUT)
db = sqlite3.connect(OUT)
db.executescript("""
create table channels(channel_id text primary key, name text, handle text, url text, category text, tier text,
  subscribers text, channel_total_videos text, channel_total_views text, joined text, description text,
  live_total integer, videos_in_db integer, transcripts_in_db integer, sources text, raw_json text);
create table videos(video_id text primary key, channel_id text references channels(channel_id), url text, title text,
  published text, duration_seconds integer, video_type text, views integer, likes integer, comments integer,
  description text, hashtags text, keywords text, thumbnail_url text, has_transcript integer, source text, sources text, raw_json text);
create table transcripts(video_id text primary key references videos(video_id), text text, word_count integer,
  language text, caption_type text, sha256 text, source text);
create table ds34_records(video_id text, channel_id text, tab text, playability_status text, playability_reason text,
  collected_at text, raw_json text);
create index ix_v on videos(channel_id); create index ix_d on ds34_records(video_id);
""")
ch = {}
def C(cid):
    return ch.setdefault(cid, dict(channel_id=cid, url=f"https://www.youtube.com/channel/{cid}", sources=set()))
for c in json.load(open(INV))["channels"]:
    x = C(c["canonical_channel_id"]); x.update(name=c["verified_name"], handle=c.get("current_handle"),
        category=c["source_group"], subscribers=c.get("subscribers"), channel_total_videos=c.get("header_videos"),
        channel_total_views=c.get("channel_total_views"), joined=c.get("joined"),
        live_total=sum(int(c.get(k) or 0) for k in ("live_regular", "live_shorts", "live_streams")))
    x["sources"].add("inventory_2026-09-28")
vids = {}
def V(row):
    vid = row["video_id"]
    if vid in vids:
        for k, v in row.items():
            if v not in (None, "") and vids[vid].get(k) in (None, ""): vids[vid][k] = v
        vids[vid]["sources"].add(row["source"])
    else:
        row["sources"] = {row["source"]}; vids[vid] = row

reg = sqlite3.connect(f"file:{REG}?mode=ro", uri=True)
tr = []
for cid in list(ch):
    for v in reg.execute("select youtube_video_id,canonical_url,title,published_at,duration_seconds,video_type,views,likes,comments,description,thumbnail_url,raw_json from videos where canonical_channel_id=?", (cid,)):
        t = reg.execute("select transcript_text,word_count,language,caption_type,transcript_sha256 from transcripts where youtube_video_id=? and coalesce(is_placeholder,0)=0 and transcript_text is not null", (v[0],)).fetchone()
        C(cid)["sources"].add("registry")
        V(dict(video_id=v[0], channel_id=cid, url=v[1], title=v[2], published=v[3], duration_seconds=v[4], video_type=v[5],
               views=v[6], likes=v[7], comments=v[8], description=v[9], thumbnail_url=v[10], raw_json=v[11],
               has_transcript=1 if t else 0, source="registry"))
        if t: tr.append((v[0], *t, "registry"))

new = sqlite3.connect(f"file:{NEW}?mode=ro", uri=True)
new.row_factory = sqlite3.Row
for r in new.execute("select * from channels"):
    x = C(r["channel_id"]); x["sources"].add("apify_2026-11-11")
    x.update(name=r["channel_name"], handle=r["handle"], url=r["url"] or x["url"], subscribers=r["subscribers"],
             channel_total_videos=r["channel_total_videos"], channel_total_views=r["channel_total_views"],
             joined=r["joined"], description=r["description"])
    x.setdefault("category", "NEW_APIFY_2026_11_11")
for r in new.execute("select * from videos"):
    V(dict(video_id=r["video_id"], channel_id=r["channel_id"], url=r["url"], title=r["title"], published=r["published_utc"],
           duration_seconds=secs(r["duration"]), video_type=r["type"], views=r["views"], likes=r["likes"], comments=r["comments"],
           description=r["description"], hashtags=r["hashtags"], thumbnail_url=r["thumbnail_url"], raw_json=r["raw_json"],
           has_transcript=0, source="apify_2026-11-11"))

for p in sorted(glob.glob(f"{R}/data/raw/competitors/DS-000034/*.jsonl.gz")):
    for l in gzip.open(p, "rt"):
        if not l.strip(): continue
        d = json.loads(l); vd = d.get("video_details") or {}; cid = d["enumerated_channel_id"]
        C(cid)["sources"].add("DS-000034")
        db.execute("insert into ds34_records values(?,?,?,?,?,?,?)", (d["video_id"], cid, d["enumerated_tab"],
                   d["playability_status"], d["playability_reason"], d["collected_at"], l.strip()))
        mf = d.get("microformat")
        pub = mf.get("playerMicroformatRenderer", {}).get("publishDate") if isinstance(mf, dict) else None
        V(dict(video_id=d["video_id"], channel_id=cid, url=f"https://www.youtube.com/watch?v={d['video_id']}", title=vd.get("title"),
               published=pub, duration_seconds=int(vd["lengthSeconds"]) if str(vd.get("lengthSeconds", "")).isdigit() else None,
               video_type=d["enumerated_tab"], views=vd.get("viewCount"), description=vd.get("shortDescription"),
               keywords=json.dumps(vd.get("keywords")) if vd.get("keywords") else None, has_transcript=0, source="DS-000034"))

def tier(x, n):
    return ("1_FULL_PACKAGE" if "registry" in x["sources"] and n else "2_APIFY_COMPLETE" if "apify_2026-11-11" in x["sources"]
            else "3_PUBLIC_PER_VIDEO_METADATA" if n else "4_IDENTITY_ONLY")
cnt, tc = {}, {}
for v in vids.values():
    cnt[v["channel_id"]] = cnt.get(v["channel_id"], 0) + 1; tc[v["channel_id"]] = tc.get(v["channel_id"], 0) + (v.get("has_transcript") or 0)
for cid, x in ch.items():
    n = cnt.get(cid, 0)
    db.execute("insert into channels values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (cid, x.get("name"), x.get("handle"), x["url"],
        x.get("category"), tier(x, n), x.get("subscribers"), x.get("channel_total_videos"), x.get("channel_total_views"),
        x.get("joined"), x.get("description"), x.get("live_total"), n, tc.get(cid, 0), ";".join(sorted(x["sources"])), None))
cols = ["video_id","channel_id","url","title","published","duration_seconds","video_type","views","likes","comments","description","hashtags","keywords","thumbnail_url","has_transcript","source","sources","raw_json"]
for v in vids.values():
    v["source"] = sorted(v["sources"])[0]; v["sources"] = ";".join(sorted(v["sources"]))
    db.execute(f"insert into videos values({','.join('?'*len(cols))})", [v.get(c) for c in cols])
db.executemany("insert into transcripts values(?,?,?,?,?,?,?)", tr)
db.commit()
for q in ["select tier,count(*),sum(videos_in_db),sum(transcripts_in_db) from channels group by tier",
          "select count(*) from videos", "select count(*) from transcripts", "select count(*) from ds34_records",
          "pragma foreign_key_check", "pragma integrity_check"]:
    print(q, db.execute(q).fetchall())
