#!/usr/bin/env python3
"""Build the senior-health master index (all sources, zero-to-date) from repo files only.
Read-only on every source; writes only into this folder. Re-run to rebuild."""
import csv, glob, gzip, json, os, sqlite3, collections
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.dirname(os.path.abspath(__file__))
INV = f"{R}/docs/research/senior-health-2026-09-25/forensic-v3/SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.json"
REG = f"{R}/data/catalog/youtube_channel_registry.db"
DS34 = f"{R}/data/raw/competitors/DS-000034/*.jsonl.gz"
NEW = f"{R}/research/senior-health-apify-2026-11-11/senior_health_apify.db"

ch = {}  # channel_id -> dict
def C(cid):
    return ch.setdefault(cid, dict(channel_id=cid, name="", handle="", category="", subscribers="",
        live_total="", registry_videos=0, registry_transcripts=0, ds34_records=0, ds34_playable=0,
        apify_2026_11_11_videos=0, tier=""))
vids = {}  # video_id -> row (priority registry > apify > ds34)
def V(vid, row):
    if vid not in vids: vids[vid] = row; vids[vid]["sources"] = set()
    vids[vid]["sources"].add(row["_src"])
    for k, v in row.items():
        if k != "_src" and v not in (None, "") and vids[vid].get(k) in (None, ""): vids[vid][k] = v

for c in json.load(open(INV))["channels"]:
    x = C(c["canonical_channel_id"]); x["name"] = c["verified_name"]; x["handle"] = c.get("current_handle", "")
    x["category"] = c["source_group"] + "|" + c.get("senior_health_relevance", "")
    x["subscribers"] = c.get("subscribers", "")
    x["live_total"] = sum(int(c.get(k) or 0) for k in ("live_regular", "live_shorts", "live_streams"))

reg = sqlite3.connect(f"file:{REG}?mode=ro", uri=True)
for cid in list(ch):
    rows = reg.execute("select youtube_video_id,title,published_at,duration_seconds,views,likes,comments,thumbnail_url,video_type from videos where canonical_channel_id=?", (cid,)).fetchall()
    if not rows: continue
    for v in rows:
        t = reg.execute("select length(coalesce(transcript_text,'')) from transcripts where youtube_video_id=? and coalesce(is_placeholder,0)=0", (v[0],)).fetchone()
        has = 1 if t and t[0] else 0
        C(cid)["registry_videos"] += 1; C(cid)["registry_transcripts"] += has
        V(v[0], dict(_src="registry", channel_id=cid, title=v[1], published=v[2], duration_s=v[3], views=v[4],
                     likes=v[5], comments=v[6], thumbnail_url=v[7], video_type=v[8], has_transcript=has))

new = sqlite3.connect(f"file:{NEW}?mode=ro", uri=True)
for r in new.execute("select channel_id,channel_name,handle,subscribers from channels"):
    x = C(r[0]); x["name"] = x["name"] or r[1]; x["handle"] = x["handle"] or r[2]; x["subscribers"] = x["subscribers"] or r[3]
    x["category"] = x["category"] or "NEW_APIFY_2026_11_11"
for r in new.execute("select video_id,channel_id,title,published_utc,views,likes,comments,duration,thumbnail_url,type from videos"):
    C(r[1])["apify_2026_11_11_videos"] += 1
    V(r[0], dict(_src="apify_2026_11_11", channel_id=r[1], title=r[2], published=r[3], views=r[4], likes=r[5],
                 comments=r[6], duration_s=r[7], thumbnail_url=r[8], video_type=r[9], has_transcript=0))

for p in sorted(glob.glob(DS34)):
    for l in gzip.open(p, "rt"):
        if not l.strip(): continue
        d = json.loads(l); vd = d.get("video_details") or {}; cid = d["enumerated_channel_id"]
        x = C(cid); x["ds34_records"] += 1; x["ds34_playable"] += d["playability_status"] == "OK"
        mf = (d.get("microformat") or {}).get("playerMicroformatRenderer", {}) if isinstance(d.get("microformat"), dict) else {}
        V(d["video_id"], dict(_src="ds34_public_meta", channel_id=cid, title=vd.get("title"),
                              duration_s=vd.get("lengthSeconds"), views=vd.get("viewCount"),
                              published=mf.get("publishDate"), video_type=d.get("enumerated_tab")))

for x in ch.values():
    if x["registry_videos"]: x["tier"] = "1_FULL_PACKAGE_metadata+transcripts(registry)"
    elif x["apify_2026_11_11_videos"]: x["tier"] = "2_APIFY_METADATA_COMPLETE(2026-11-11)"
    elif x["ds34_records"]: x["tier"] = "3_PUBLIC_PER_VIDEO_METADATA_ONLY(DS-000034)"
    else: x["tier"] = "4_IDENTITY_ONLY"

F = ["channel_id", "name", "handle", "category", "tier", "subscribers", "live_total", "registry_videos",
     "registry_transcripts", "apify_2026_11_11_videos", "ds34_records", "ds34_playable"]
rows = sorted(ch.values(), key=lambda x: (x["tier"], x["name"].lower()))
with open(f"{OUT}/MASTER_CHANNELS.csv", "w", newline="") as f:
    w = csv.DictWriter(f, F); w.writeheader(); [w.writerow({k: x[k] for k in F}) for x in rows]

dbp = f"{OUT}/senior_health_master.db"
if os.path.exists(dbp): os.remove(dbp)
db = sqlite3.connect(dbp)
db.execute(f"create table channels({','.join(F)}, primary key(channel_id))")
db.executemany(f"insert into channels values({','.join('?'*len(F))})", [[x[k] for k in F] for x in rows])
VF = ["video_id", "channel_id", "title", "published", "duration_s", "views", "likes", "comments", "video_type", "thumbnail_url", "has_transcript", "sources"]
db.execute(f"create table videos({','.join(VF)}, primary key(video_id))")
db.executemany(f"insert into videos values({','.join('?'*len(VF))})",
    [[(";".join(sorted(v["sources"])) if k == "sources" else v.get(k)) for k in VF] for v in vids.values()])
db.commit()

T = collections.Counter(x["tier"] for x in ch.values())
tv = collections.defaultdict(int)
for x in ch.values(): tv[x["tier"]] += x["registry_videos"] or x["apify_2026_11_11_videos"] or x["ds34_records"]
print("channels", len(ch), dict(T)); print("unique video ids", len(vids))
print("transcripts", sum(x["registry_transcripts"] for x in ch.values()))
print("videos by tier", dict(tv))
print("ds34 records", sum(x["ds34_records"] for x in ch.values()), "playable", sum(x["ds34_playable"] for x in ch.values()))
