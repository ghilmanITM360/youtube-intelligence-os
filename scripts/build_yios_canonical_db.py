#!/usr/bin/env python3
"""Build data/catalog/yios_canonical.db: ONE row per channel and per video, merged from the five video stores.

  python3 scripts/build_yios_canonical_db.py build    # rebuild the DB + data/manifests/yios-canonical-sources.json
  python3 scripts/build_yios_canonical_db.py verify   # reconcile counts and integrity of the built DB

Derived and rebuildable (gitignored with the other data/catalog/*.db). Source DBs are opened read-only and never modified
(AGENTS.md rule 4). Nothing is dropped: every source row is kept in video_sources / channel_sources with its RAW values,
disagreements go to conflicts, unusable values to quality_issues. Scalar precedence (freshest first):
sh_apify > finance > sh_core > registry > inventory; the first valid value wins, a different valid value is a conflict.
Channel key = YouTube UC id; the inventory's CH-NNNNNN ids are mapped through inventory.channels.youtube_channel_id."""
import hashlib, json, os, re, sqlite3, sys

R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = f"{R}/data/catalog/yios_canonical.db"
MANIFEST = f"{R}/data/manifests/yios-canonical-sources.json"
SRC = {  # source_id -> repo-relative path (freshest first = precedence order)
    "sh_apify": "research/senior-health-apify-2026-11-11/senior_health_apify.db",
    "finance": "data/catalog/finance_economics_complete.db",
    "sh_core": "data/catalog/senior_health/senior_health_core.db",
    "registry": "data/catalog/youtube_channel_registry.db",
    "inventory": "data/catalog/youtube_inventory.db",
}
ORDER = list(SRC)
VTYPE = {  # raw spelling (lowercased) -> (normalized, basis)
    "video": ("LONG", "DECLARED"), "videos": ("LONG", "DECLARED"), "regular video": ("LONG", "DECLARED"),
    "regular": ("LONG", "DECLARED"), "long_form": ("LONG", "DECLARED"),
    "videos_tab": ("LONG", "INFERRED_FROM_VIDEOS_TAB"),  # a source tab label, not a declared type
    "short": ("SHORT", "DECLARED"), "shorts": ("SHORT", "DECLARED"), "streams": ("STREAM", "DECLARED"),
}
SCHEMA = """
CREATE TABLE source_dbs(source_id TEXT PRIMARY KEY, path TEXT, sha256 TEXT, bytes INTEGER, video_rows INTEGER, channel_rows INTEGER);
CREATE TABLE channels(channel_id TEXT PRIMARY KEY, inventory_id TEXT, name TEXT, handle TEXT, url TEXT, subscribers INTEGER,
  channel_total_videos INTEGER, channel_total_views INTEGER, source_count INTEGER);
CREATE TABLE channel_sources(channel_id TEXT, source_id TEXT, raw_name TEXT, raw_handle TEXT, raw_label TEXT, raw_subscribers TEXT,
  PRIMARY KEY(channel_id, source_id));
CREATE TABLE unresolved_channels(source_id TEXT, name TEXT, handle TEXT, url TEXT, reason TEXT);
CREATE TABLE video_type_map(raw TEXT PRIMARY KEY, normalized TEXT, basis TEXT, rows INTEGER);
CREATE TABLE videos(video_id TEXT PRIMARY KEY, channel_id TEXT NOT NULL REFERENCES channels(channel_id), url TEXT, title TEXT,
  published_date TEXT, published_at_utc TEXT, published_precision TEXT, duration_seconds INTEGER,
  video_type TEXT NOT NULL, video_type_basis TEXT NOT NULL, views INTEGER, likes INTEGER, comments INTEGER,
  description TEXT, thumbnail_url TEXT, has_transcript INTEGER NOT NULL, source_count INTEGER NOT NULL);
CREATE TABLE video_sources(video_id TEXT, source_id TEXT, raw_channel_id TEXT, raw_title TEXT, raw_published TEXT, raw_duration TEXT,
  raw_video_type TEXT, raw_views TEXT, raw_likes TEXT, raw_comments TEXT, PRIMARY KEY(video_id, source_id));
CREATE TABLE conflicts(video_id TEXT, field TEXT, chosen_source TEXT, chosen_value TEXT, other_source TEXT, other_value TEXT);
CREATE TABLE quality_issues(video_id TEXT, source_id TEXT, field TEXT, raw_value TEXT, issue TEXT);
CREATE INDEX idx_videos_channel ON videos(channel_id);
CREATE INDEX idx_videos_type ON videos(video_type);
"""


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()


def count(x):  # 5000 / "14400" / "116K" / "17,215,098 views" / "1.2M" -> int, else None
    if x is None or x == "": return None
    if isinstance(x, (int, float)): return int(x)
    m = re.match(r"^([\d.,]+)\s*([KMB]?)", str(x).strip(), re.I)
    if not m: return None
    try: return int(round(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2).upper()]))
    except ValueError: return None


def hms(s):  # "01:02:03" / "12:34" -> seconds
    if isinstance(s, int): return s
    if s is None or s == "": return None
    try:
        r = 0
        for x in str(s).split(":"): r = r * 60 + int(x)
        return r
    except ValueError: return None


def handle(h):
    h = (h or "").strip()
    return "@" + h.lstrip("@") if h.lstrip("@") else None


def pdate(raw):  # -> (date, utc_or_None, precision) or None when unusable
    s = (raw or "").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z", s): return s[:10], s[:19] + "Z", "SECOND_UTC"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", s): return s[:10], None, "DATETIME_TZ_UNKNOWN"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s): return s, None, "DATE"
    return None


def ro(path):
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def read_sources():
    """-> channels{src: [dict]}, videos{src: [dict]} with uniform keys; raw values kept as read."""
    ch, vd = {}, {}
    q = lambda c, s: [dict(zip([d[0] for d in cur.description], r)) for cur in [c.execute(s)] for r in cur]
    for sid in ORDER:
        c = ro(f"{R}/{SRC[sid]}")
        if sid == "sh_apify":
            ch[sid] = [dict(id=r["channel_id"], name=r["channel_name"], handle=r["handle"], url=r["url"], label=r["coverage"],
                            subs=r["subscribers"], tv=r["channel_total_videos"], tw=r["channel_total_views"])
                       for r in q(c, "select * from channels")]
            vd[sid] = [dict(id=r["video_id"], ch=r["channel_id"], url=r["url"], title=r["title"], pub=r["published_utc"], dur=r["duration"],
                            vt=r["type"], views=r["views"], likes=r["likes"], comments=r["comments"], desc=r["description"],
                            thumb=r["thumbnail_url"], tx=0) for r in q(c, "select * from videos")]
        elif sid in ("finance", "sh_core"):
            lab = "niche" if sid == "finance" else "category"
            ch[sid] = [dict(id=r["channel_id"], name=r["name"], handle=r["handle"], url=r["url"], label=r[lab], subs=r["subscribers"],
                            tv=r["channel_total_videos"], tw=r["channel_total_views"]) for r in q(c, "select * from channels")]
            vd[sid] = [dict(id=r["video_id"], ch=r["channel_id"], url=r["url"], title=r["title"], pub=r["published"], dur=r["duration_seconds"],
                            vt=r["video_type"], views=r["views"], likes=r["likes"], comments=r["comments"], desc=r["description"],
                            thumb=r["thumbnail_url"], tx=r["has_transcript"] or 0) for r in q(c, "select * from videos")]
        elif sid == "registry":
            ch[sid] = [dict(id=r["canonical_channel_id"], name=r["channel_name"], handle=r["current_handle"], url=r["canonical_url"],
                            label=r["source_group"], subs=None, tv=None, tw=None) for r in q(c, "select * from channels")]
            tx = {r[0] for r in c.execute("select youtube_video_id from transcripts where is_placeholder=0 and length(coalesce(transcript_text,''))>0")}
            vd[sid] = [dict(id=r["youtube_video_id"], ch=r["canonical_channel_id"], url=r["canonical_url"], title=r["title"], pub=r["published_at"],
                            dur=r["duration_seconds"], vt=r["video_type"], views=r["views"], likes=r["likes"], comments=r["comments"],
                            desc=r["description"], thumb=r["thumbnail_url"], tx=int(r["youtube_video_id"] in tx)) for r in q(c, "select * from videos")]
        else:  # inventory: CH-NNNNNN ids; mapped to UC via youtube_channel_id
            rows = q(c, "select * from channels")
            ch[sid] = [dict(id=r["youtube_channel_id"], inv=r["channel_id"], name=r["display_name"], handle=r["handle"], url=r["channel_url"],
                            label=None, subs=None, tv=None, tw=None) for r in rows]
            m = {r["channel_id"]: r["youtube_channel_id"] for r in rows}
            vd[sid] = [dict(id=r["youtube_video_id"], ch=m[r["channel_id"]], url=r["canonical_url"], title=None, pub=None, dur=None, vt=None,
                            views=None, likes=None, comments=None, desc=None, thumb=None, tx=0) for r in q(c, "select * from videos")]
    return ch, vd


def first(vals):  # vals: [(source, value)] in precedence order, None = unusable
    return next(((s, v) for s, v in vals if v not in (None, "")), (None, None))


def build():
    ch_src, vd_src = read_sources()
    if os.path.exists(OUT): os.remove(OUT)
    db = sqlite3.connect(OUT)
    db.executescript(SCHEMA)
    for sid in ORDER:
        p = f"{R}/{SRC[sid]}"
        db.execute("insert into source_dbs values(?,?,?,?,?,?)", (sid, SRC[sid], sha_file(p), os.path.getsize(p), len(vd_src[sid]), len(ch_src[sid])))
    # ---- channels
    chans = {}
    for sid in ORDER:
        for r in ch_src[sid]:
            if not r["id"]:
                db.execute("insert into unresolved_channels values(?,?,?,?,?)", (sid, r["name"], r["handle"], r["url"], "NO_CHANNEL_ID_IN_SOURCE"))
                continue
            chans.setdefault(r["id"], []).append((sid, r))
    for cid in sorted(chans):
        rows = chans[cid]
        pick = lambda k, f=lambda x: x: first([(s, f(r[k])) for s, r in rows])[1]
        inv = next((r["inv"] for s, r in rows if r.get("inv")), None)
        db.execute("insert into channels values(?,?,?,?,?,?,?,?,?)", (cid, inv, pick("name"), pick("handle", handle), pick("url"),
                   pick("subs", count), pick("tv", count), pick("tw", count), len(rows)))
        for s, r in rows:
            db.execute("insert into channel_sources values(?,?,?,?,?,?)", (cid, s, r["name"], r["handle"], r["label"], None if r["subs"] is None else str(r["subs"])))
    # ---- videos
    by = {}
    for sid in ORDER:
        for r in vd_src[sid]: by.setdefault(r["id"], []).append((sid, r))
    tcount = {}
    for vid in sorted(by):
        rows = by[vid]
        for s, r in rows:
            db.execute("insert into video_sources values(?,?,?,?,?,?,?,?,?,?)",
                       (vid, s, r["ch"], r["title"], r["pub"], None if r["dur"] is None else str(r["dur"]), r["vt"],
                        None if r["views"] is None else str(r["views"]), None if r["likes"] is None else str(r["likes"]),
                        None if r["comments"] is None else str(r["comments"])))
        cand = {
            "channel_id": [(s, r["ch"]) for s, r in rows], "url": [(s, r["url"]) for s, r in rows],
            "title": [(s, r["title"]) for s, r in rows], "duration_seconds": [(s, hms(r["dur"])) for s, r in rows],
            "views": [(s, count(r["views"])) for s, r in rows], "likes": [(s, count(r["likes"])) for s, r in rows],
            "comments": [(s, count(r["comments"])) for s, r in rows],
            "description": [(s, r["desc"]) for s, r in rows], "thumbnail_url": [(s, r["thumb"]) for s, r in rows],
        }
        pd = []
        for s, r in rows:
            d = pdate(r["pub"])
            if r["pub"] not in (None, "") and d is None:
                db.execute("insert into quality_issues values(?,?,?,?,?)", (vid, s, "published", r["pub"], "UNPARSEABLE_DATE_PLACEHOLDER"))
            pd.append((s, d))
        vt = []
        for s, r in rows:
            raw = (r["vt"] or "").strip().lower()
            if not raw: continue
            if raw not in VTYPE: raise SystemExit(f"unknown video_type spelling {r['vt']!r} in {s} ({vid}); add it to VTYPE")
            vt.append((s, VTYPE[raw]))
        declared = [(s, v) for s, v in vt if v[1] == "DECLARED"]
        _, vtype = first(declared or vt) if (declared or vt) else (None, ("UNKNOWN", "UNKNOWN"))
        # ---- conflicts: another source holds a different valid value than the chosen one
        def conflict(field, vals):
            vals = [(s, v) for s, v in vals if v not in (None, "")]
            for s, v in vals[1:]:
                if v != vals[0][1]: db.execute("insert into conflicts values(?,?,?,?,?,?)", (vid, field, vals[0][0], str(vals[0][1]), s, str(v)))
        for f in ("channel_id", "title", "duration_seconds", "views", "likes", "comments"): conflict(f, cand[f])
        conflict("published_date", [(s, d[0] if d else None) for s, d in pd])
        conflict("video_type", [(s, v[0]) for s, v in vt])
        _, d = first(pd)
        cid = first(cand["channel_id"])[1]
        if cid not in chans: raise SystemExit(f"{vid}: channel {cid!r} has no channel row")
        db.execute("insert into videos values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            vid, cid, first(cand["url"])[1], first(cand["title"])[1], d[0] if d else None, d[1] if d else None,
            d[2] if d else None, first(cand["duration_seconds"])[1], vtype[0], vtype[1], first(cand["views"])[1],
            first(cand["likes"])[1], first(cand["comments"])[1], first(cand["description"])[1], first(cand["thumbnail_url"])[1],
            int(any(r["tx"] for _, r in rows)), len(rows)))
        for s, r in rows:
            if s == "inventory": continue  # inventory has no video_type column; its None is not a data gap
            k = (r["vt"] or "").strip().lower()
            tcount[k] = tcount.get(k, 0) + 1
    for raw, n in sorted(tcount.items()):
        norm = VTYPE.get(raw, ("UNKNOWN", "UNKNOWN"))
        db.execute("insert into video_type_map values(?,?,?,?)", (raw or "(null)", norm[0], norm[1], n))
    db.commit()
    h = logical_hash(db)
    n = {t: db.execute(f"select count(*) from {t}").fetchone()[0] for t in ("channels", "videos", "video_sources", "conflicts", "quality_issues", "unresolved_channels")}
    db.close()
    srcs = {s: dict(zip(("path", "sha256", "bytes", "video_rows", "channel_rows"), r)) for s, *r in
            sqlite3.connect(OUT).execute("select source_id,path,sha256,bytes,video_rows,channel_rows from source_dbs")}
    with open(MANIFEST, "w") as f:
        json.dump({"builder": "scripts/build_yios_canonical_db.py", "sources": srcs, "counts": n, "logical_sha256": h}, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(n), "logical_sha256", h[:16])


def logical_hash(db):
    h = hashlib.sha256()
    for (t,) in db.execute("select name from sqlite_master where type='table' order by 1").fetchall():
        h.update(t.encode())
        for row in db.execute(f"select * from {t} order by 1,2,3,4"): h.update(repr(row).encode())
    return h.hexdigest()


def verify():
    db = ro(OUT)
    one = lambda s: db.execute(s).fetchone()[0]
    src_rows = one("select sum(video_rows) from source_dbs")
    checks = {
        "video_sources rows == sum of source video rows": one("select count(*) from video_sources") == src_rows,
        "videos + duplicate source rows == source rows": one("select count(*) from videos") + one("select sum(source_count-1) from videos") == src_rows,
        "no orphan video->channel": one("select count(*) from videos v left join channels c using(channel_id) where c.channel_id is null") == 0,
        "no orphan video_sources->videos": one("select count(*) from video_sources s left join videos v using(video_id) where v.video_id is null") == 0,
        "video_type in {LONG,SHORT,STREAM,UNKNOWN}": one("select count(*) from videos where video_type not in ('LONG','SHORT','STREAM','UNKNOWN')") == 0,
        "every channel has >=1 source row": one("select count(*) from channels c where not exists (select 1 from channel_sources s where s.channel_id=c.channel_id)") == 0,
        "video_id is 11 chars": one("select count(*) from videos where length(video_id)<>11") == 0,
    }
    for k, ok in checks.items(): print("PASS" if ok else "FAIL", k)
    print("videos", one("select count(*) from videos"), "channels", one("select count(*) from channels"), "source rows", src_rows)
    return all(checks.values())


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "build": build()
    elif cmd == "verify": sys.exit(0 if verify() else 1)
    else: sys.exit(__doc__)
