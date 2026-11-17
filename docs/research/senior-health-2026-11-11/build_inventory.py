"""Report 1 inventory builder: unify Senior Health competitor + Dr Rehan data (read-only on sources).
Run from repo root: python3 -I docs/research/senior-health-2026-11-11/build_inventory.py
"""
import csv, json, sqlite3, re, ast, statistics, collections, os, sys
csv.field_size_limit(10**9)
OUT = "docs/research/senior-health-2026-11-11"
E = "data/extracted/channel-data/senior-health-16-acquisition"
REG = "data/catalog/youtube_channel_registry.db"
REHAN = "UCQIzqH7QZ9viBYpOFqgSXMg"
REG_HEALTH = ["UCFpxvukIqCAUA7YizI-q9Dw", "UCFuGMi0idGeyXl6wYK9hg7Q", "UCXZi5JVeuTluazF-fYqQgNA",
              "UC356D-NzdnznBOftTpYoBLw", "UCQcBYZxFW7YwNMU8-DsT3Uw", "UCMJxAeBJ0d1JC937de1eZ0Q",
              "UCAYG0fzUyxv6OevH88qA45w"]

def secs(d):
    if d in (None, "", "None"): return None
    if str(d).isdigit(): return int(d)
    p = [int(x) for x in str(d).split(":")]
    return sum(v * 60 ** i for i, v in enumerate(reversed(p)))

def num(x):
    try: return int(float(x))
    except (TypeError, ValueError): return None

rows, chan = [], {}
# --- Batch A: Nov 2026 acquisition (15 channels)
tx = {}
for l in open(f"{E}/TRANSCRIPTS_ALL.jsonl"):
    r = json.loads(l); tx[r["video_id"]] = r
for c in csv.DictReader(open(f"{E}/CHANNEL_MASTER.csv")):
    chan[c["channel_id"]] = dict(name=c["channel_name"], handle=c["channel_handle"], subs=num(c["subscribers"]),
                                 joined=c["joined"], location=c["location"], batch="A_NOV_ACQ", snapshot="2026-11")
for v in csv.DictReader(open(f"{E}/VIDEO_MASTER.csv")):
    t = tx.get(v["video_id"])
    rows.append(dict(batch="A_NOV_ACQ", role="COMPETITOR", channel_id=v["channel_id"], video_id=v["video_id"],
        title=v["title"], published=v["published_date"][:10], duration_s=secs(v["duration"]), type=v["type"],
        views=num(v["view_count"]), likes=num(v["likes"]), comments=num(v["comment_count"]),
        thumb_url=bool(v["thumbnail_url"]), desc_chars=len(v["description"] or ""),
        tx_words=len(t["text"].split()) if t else 0, tx_source=t["source"] if t else "", tx_placeholder=0,
        tx_timestamps=0))
# --- Batch B: registry (Sept 2026) + Rehan DS-000032
db = sqlite3.connect(f"file:{REG}?mode=ro", uri=True)
for cid in REG_HEALTH + [REHAN]:
    n, h = db.execute("select channel_name,current_handle from channels where canonical_channel_id=?", (cid,)).fetchone()
    subs = None
    for (rj,) in db.execute("select raw_json from videos where canonical_channel_id=? and raw_json is not null limit 5", (cid,)):
        try: subs = num(json.loads(rj).get("numberOfSubscribers"))
        except Exception: pass
        if subs is not None: break
    chan[cid] = dict(name=n, handle=(h or "").lstrip("@"), subs=subs, joined="", location="",
                     batch="B_REGISTRY_SEP", snapshot="2026-09")
    for vid, title, pub, dur, typ, views, likes, com, desc, th in db.execute(
        "select youtube_video_id,title,published_at,duration_seconds,video_type,views,likes,comments,description,thumbnail_url from videos where canonical_channel_id=?", (cid,)):
        t = db.execute("select max(word_count), min(is_placeholder), max(caption_type) from transcripts where youtube_video_id=?", (vid,)).fetchone()
        rows.append(dict(batch="B_REGISTRY_SEP", role="OWN" if cid == REHAN else "COMPETITOR", channel_id=cid, video_id=vid,
            title=title, published=(pub or "")[:10], duration_s=dur, type=typ, views=views, likes=likes, comments=com,
            thumb_url=bool(th), desc_chars=len(desc or ""), tx_words=(t[0] or 0) if t[1] == 0 else 0,
            tx_source=t[2] or "", tx_placeholder=1 if t[1] == 1 else 0, tx_timestamps=0))
# --- Rehan Nov pilots: refresh metadata for all 66, add 10 new + SRT
P = "data/raw/channel-data/drrehanomar-acquisition-2026-11-11/apify/"
p2 = {r["id"]: r for r in json.load(open(P + "pilot2/dataset.json"))}
p3 = {r["id"]: r for r in json.load(open(P + "pilot3_subtitles/dataset.json"))}
byid = {r["video_id"]: r for r in rows if r["channel_id"] == REHAN}
rehan_sept_views = {k: v["views"] for k, v in byid.items()}
for vid, r in p2.items():
    base = byid.get(vid)
    upd = dict(views=num(r["viewCount"]), likes=num(r["likes"]), comments=num(r["commentsCount"]),
               type=r["type"], duration_s=secs(r["duration"]), batch="REHAN_NOV_PILOT")
    if base: base.update(upd)
    else:
        subs_raw = p3.get(vid, {}).get("subtitles")
        if isinstance(subs_raw, str) and subs_raw not in ("None", ""): subs_raw = ast.literal_eval(subs_raw)
        srt = (subs_raw or [{}])[0] if isinstance(subs_raw, list) else {}
        words = len(re.sub(r"\d+\n[\d:,]+ --> [\d:,]+\n", " ", srt.get("srt") or "").split())
        rows.append(dict(role="OWN", channel_id=REHAN, video_id=vid, title=r["title"], published=r["date"][:10],
            thumb_url=bool(r["thumbnailUrl"]), desc_chars=len(r["text"] or ""), tx_words=words,
            tx_source=srt.get("type", ""), tx_placeholder=0, tx_timestamps=1 if words else 0, **upd))
chan[REHAN].update(subs=num(next(iter(p2.values()))["numberOfSubscribers"]), joined="Feb 3, 2026",
                   location="United States", batch="B_REGISTRY_SEP+REHAN_NOV_PILOT", snapshot="2026-11")

# --- checks
ids = collections.Counter(r["video_id"] for r in rows)
dups = [k for k, v in ids.items() if v > 1]
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()
tmap = collections.defaultdict(set)
for r in rows: tmap[norm(r["title"])].add(r["channel_id"])
cross_title = {t: c for t, c in tmap.items() if len(c) > 1}
within = collections.Counter((r["channel_id"], norm(r["title"])) for r in rows)
within_dup = sum(1 for v in within.values() if v > 1)
for r in rows:
    r["is_short"] = int("short" in (r["type"] or "").lower() or (r["duration_s"] or 999) <= 60)
    r["channel"] = chan[r["channel_id"]]["name"]

cols = ["role", "batch", "channel", "channel_id", "video_id", "title", "published", "duration_s", "type", "is_short",
        "views", "likes", "comments", "thumb_url", "desc_chars", "tx_words", "tx_source", "tx_placeholder", "tx_timestamps"]
with open(f"{OUT}/01-unified-video-table.csv", "w", newline="") as f:
    w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(sorted(rows, key=lambda r: (r["role"], r["channel"], r["published"])))

cov = []
for cid, c in chan.items():
    vs = [r for r in rows if r["channel_id"] == cid]
    views = [r["views"] for r in vs if r["views"] is not None]
    cov.append(dict(role="OWN" if cid == REHAN else "COMPETITOR", channel=c["name"], handle=c["handle"], channel_id=cid,
        batch=c["batch"], snapshot=c["snapshot"], subscribers=c["subs"], joined=c["joined"], videos=len(vs),
        long_form=sum(1 - r["is_short"] for r in vs), shorts=sum(r["is_short"] for r in vs),
        first_upload=min(r["published"] for r in vs), last_upload=max(r["published"] for r in vs),
        total_views=sum(views), median_views=int(statistics.median(views)) if views else None,
        tx_real=sum(1 for r in vs if r["tx_words"] > 0), tx_placeholder=sum(r["tx_placeholder"] for r in vs),
        tx_missing=sum(1 for r in vs if r["tx_words"] == 0 and not r["tx_placeholder"]),
        tx_short_lt100w=sum(1 for r in vs if 0 < r["tx_words"] < 100 and not r["is_short"]),
        tx_timestamped=sum(r["tx_timestamps"] for r in vs),
        thumb_urls=sum(r["thumb_url"] for r in vs), no_desc=sum(1 for r in vs if r["desc_chars"] == 0),
        no_views=sum(1 for r in vs if r["views"] is None), no_date=sum(1 for r in vs if not re.match(r"\d{4}-\d\d-\d\d", r["published"] or "")),
        no_duration=sum(1 for r in vs if not r["duration_s"]), no_likes=sum(1 for r in vs if r["likes"] is None)))
cov.sort(key=lambda r: (r["role"], r["batch"], r["channel"]))
with open(f"{OUT}/01-channel-coverage.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(cov[0])); w.writeheader(); w.writerows(cov)

comp = [r for r in rows if r["role"] == "COMPETITOR"]
print("channels", len(chan), "competitor", len(chan) - 1, "| rows", len(rows), "competitor videos", len(comp), "rehan", len(rows) - len(comp))
print("dup video ids across sources:", len(dups), "| cross-channel identical titles:", len(cross_title), "| within-channel dup titles:", within_dup)
for t, c in list(cross_title.items())[:8]: print("  X-TITLE:", t[:90], [chan[x]["name"] for x in c])
for r in cov: print(" | ".join(str(r[k]) for k in ["role", "channel", "snapshot", "subscribers", "videos", "long_form", "shorts", "first_upload", "last_upload", "total_views", "median_views", "tx_real", "tx_placeholder", "tx_missing", "tx_short_lt100w", "thumb_urls", "no_desc", "no_views", "no_date", "no_duration", "no_likes"]))
ch = [(k, rehan_sept_views[k], byid[k]["views"]) for k in rehan_sept_views if k in p2]
print("rehan Sept->Nov total views (56 common):", sum(a for _, a, _ in ch), "->", sum(b for *_, b in ch))
missing = [(r["channel"], r["video_id"], r["title"][:60]) for r in rows if r["tx_words"] == 0]
print("no usable transcript:", len(missing)); [print("  ", m) for m in missing[:40]]
