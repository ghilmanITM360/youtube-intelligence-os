#!/usr/bin/env python3
"""Read-only local website over data/catalog/yios_canonical.db (stdlib only, no build step).

  python3 site/server.py [--port 8020]        then open http://127.0.0.1:8020

Build the DB first: scripts/build_yios_canonical_db.py build && scripts/build_yios_artifact_inventory.py
The DB is opened read-only; /raw serves only files that the artifact inventory lists (no path traversal)."""
import argparse, collections, datetime, gzip, html, json, mimetypes, os, re, sqlite3, subprocess, sys, threading, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB = os.environ.get("YIOS_CANONICAL_DB", f"{R}/data/catalog/yios_canonical.db")
INDEX = os.path.join(os.path.dirname(__file__), "index.html")
SORTS = {"views": "v.views DESC", "date": "v.published_date DESC", "duration": "v.duration_seconds DESC",
         "likes": "v.likes DESC", "title": "v.title COLLATE NOCASE"}
MAX_RAW = 20_000_000


def conn():
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    return c


def rows(c, sql, *a):
    return [fix(dict(r)) for r in c.execute(sql, a)]


def fix(r):
    """Some source channel names hold HTML entities ('&amp;'); show them decoded (the stored value is left untouched)."""
    for k in ("name", "channel", "raw_name"):
        if isinstance(r.get(k), str) and "&" in r[k]: r[k] = html.unescape(r[k])
    return r


def one(c, sql, *a):
    r = c.execute(sql, a).fetchone()
    return fix(dict(r)) if r else None


_LOCK, _MEM = threading.Lock(), {}


def memo(key, fn):
    """The DB is read-only while the server runs, so results are cached per DB file version (rebuilt DB => new keys)."""
    k = (key, os.stat(DB).st_mtime_ns)
    with _LOCK:
        if k in _MEM: return _MEM[k]
    v = fn()
    with _LOCK:
        if len(_MEM) > 800: _MEM.clear()
        _MEM[k] = v
    return v


def spec_index(c):
    """One pass over the links: which videos / which files are 'specific' (file names 25 videos or fewer), per channel."""
    def build():
        meta = {r["path"]: r for r in rows(c, "select path, role, format, videos_mentioned from artifacts where videos_mentioned<=25")}
        per, vids = {}, set()
        for cid, path, vid in c.execute("select v.channel_id, l.path, l.target_id from artifact_links l join videos v on v.video_id=l.target_id "
                                        "where l.target_kind='video'"):
            if path in meta:
                vids.add(vid); d = per.setdefault(cid, {"files": {}, "videos": set()}); d["files"].setdefault(path, set()).add(vid); d["videos"].add(vid)
        return {"vids": vids, "meta": meta, "per": per}
    return memo("spec", build)


def median(xs):
    xs = sorted(xs); n = len(xs)
    return None if not n else xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def like(s):
    return "%" + s.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"


def summary(c, q):
    n = lambda t: c.execute(f"select count(*) from {t}").fetchone()[0]
    return {"channels": n("channels"), "videos": n("videos"), "source_rows": n("video_sources"), "transcripts": n("transcripts"),
            "artifacts": n("artifacts"), "artifact_links": n("artifact_links"), "conflicts": n("conflicts"), "quality_issues": n("quality_issues"),
            "video_types": rows(c, "select video_type, count(*) n from videos group by 1 order by n desc"),
            "sources": rows(c, "select source_id, video_rows, channel_rows, sha256 from source_dbs order by video_rows desc"),
            "roles": rows(c, "select role, count(*) n from artifacts group by 1 order by n desc"),
            "by_year": rows(c, "select substr(published_date,1,4) y, count(*) n, sum(views) views from videos where published_date is not null group by 1 order by 1"),
            "caption_kinds": rows(c, "select caption_kind, count(*) n from transcripts group by 1 order by n desc"),
            "videos_with_specific_artifact": len(spec_index(c)["vids"]),
            "completeness": one(c, "select count(*) n, sum(views is not null) views, sum(published_date is not null) date, sum(duration_seconds is not null) duration, "
                                   "sum(likes is not null) likes, sum(comments is not null) comments, sum(thumbnail_url is not null) thumbnail, sum(has_transcript) transcript, "
                                   "sum(description is not null and description<>'') description from videos"),
            "top_channels": rows(c, "select c.channel_id, c.name, sum(v.views) views, count(*) videos from videos v join channels c using(channel_id) "
                                    "group by 1 order by views desc nulls last limit 15")}


def channels(c, q):
    out = rows(c, "select c.channel_id, c.name, c.handle, c.subscribers, c.channel_total_videos total, count(v.video_id) videos, sum(v.views) views, max(v.views) best, sum(v.likes) likes, "
                  "sum(v.has_transcript) transcripts, min(v.published_date) first_date, max(v.published_date) last_date, c.source_count "
                  "from channels c left join videos v using(channel_id) group by c.channel_id order by videos desc")
    vw, spark = {}, {}
    for cid, x in c.execute("select channel_id, views from videos where views is not null"): vw.setdefault(cid, []).append(x)
    for cid, y, n in c.execute("select channel_id, substr(published_date,1,4), count(*) from videos where published_date is not null group by 1,2"): spark.setdefault(cid, {})[y] = n
    for r in out: r["median"] = median(vw.get(r["channel_id"], [])); r["spark"] = spark.get(r["channel_id"], {})
    return out


def stats(c, cid):
    """Aggregates for one channel's report page (computed on demand, cached per DB version)."""
    vs = rows(c, "select video_id, title, published_date, duration_seconds d, video_type, views, likes, comments, has_transcript from videos where channel_id=?", cid)
    vw = sorted(v["views"] for v in vs if v["views"] is not None)
    med = median(vw)
    bucket = lambda x, edges, labels: labels[next((i for i, e in enumerate(edges) if x < e), len(edges))]
    dur = {}; vb = {}; bt = {}
    for v in vs:
        k = "unknown" if v["d"] is None else bucket(v["d"], [60, 300, 600, 1200, 2400, 3600], ["<1 min", "1-5 min", "5-10 min", "10-20 min", "20-40 min", "40-60 min", ">60 min"])
        dur[k] = dur.get(k, 0) + 1
        t = bt.setdefault(v["video_type"], {"l": v["video_type"], "v": 0, "views": 0, "all": []}); t["v"] += 1
        if v["views"] is not None:
            k = bucket(v["views"], [1e3, 1e4, 1e5, 1e6], ["<1K", "1K-10K", "10K-100K", "100K-1M", ">1M"]); vb[k] = vb.get(k, 0) + 1
            t["views"] += v["views"]; t["all"].append(v["views"])
    for t in bt.values(): t["median"] = median(t.pop("all"))
    order = lambda d, labels: [{"l": l, "v": d[l]} for l in labels if l in d]
    dated = [v for v in vs if v["published_date"]]
    days = []
    for v in sorted(dated, key=lambda v: v["published_date"]):
        try: days.append(datetime.date.fromisoformat(v["published_date"][:10]).toordinal())
        except ValueError: pass
    gaps = [b - a for a, b in zip(days, days[1:])]
    lv = [(v["likes"], v["views"]) for v in vs if v["likes"] is not None and v["views"]]
    sp = spec_index(c)["per"].get(cid, {"files": {}, "videos": set()})
    meta = spec_index(c)["meta"]
    spec_files = sorted(({"path": p, "role": meta[p]["role"], "format": meta[p]["format"], "videos_mentioned": meta[p]["videos_mentioned"], "n": len(x)} for p, x in sp["files"].items()),
                        key=lambda f: (-f["n"], f["path"]))[:100]
    return {"n": len(vs), "views_total": sum(vw), "views_median": med, "views_max": vw[-1] if vw else None, "likes_total": sum(v["likes"] or 0 for v in vs),
            "comments_total": sum(v["comments"] or 0 for v in vs),
            "engagement": round(sum(a for a, _ in lv) / sum(b for _, b in lv) * 100, 2) if lv else None,
            "gap_days_median": median(gaps), "span_days": (days[-1] - days[0]) if len(days) > 1 else 0,
            "avg_minutes": round(sum(v["d"] for v in vs if v["d"]) / max(1, sum(1 for v in vs if v["d"])) / 60, 1),
            "first": min((v["published_date"] for v in dated), default=None), "last": max((v["published_date"] for v in dated), default=None),
            "durations": order(dur, ["<1 min", "1-5 min", "5-10 min", "10-20 min", "20-40 min", "40-60 min", ">60 min", "unknown"]),
            "view_buckets": order(vb, ["<1K", "1K-10K", "10K-100K", "100K-1M", ">1M"]),
            "by_type": sorted(bt.values(), key=lambda t: -t["v"]),
            "by_month": rows(c, "select substr(published_date,1,7) l, count(*) v, sum(views) views from videos where channel_id=? and published_date is not null group by 1 order by 1", cid),
            "by_year": rows(c, "select substr(published_date,1,4) l, count(*) v, sum(views) views from videos where channel_id=? and published_date is not null group by 1 order by 1", cid),
            "weekday": rows(c, "select cast(strftime('%w', published_date) as int) l, count(*) v from videos where channel_id=? and published_date is not null group by 1 order by 1", cid),
            "all": [[v["video_id"], v["title"], v["published_date"], v["d"], v["video_type"], v["views"], v["likes"], v["comments"], v["has_transcript"]] for v in vs],
            "caption_kinds": rows(c, "select t.caption_kind l, count(*) v from transcripts t join videos v using(video_id) where v.channel_id=? group by 1 order by v desc", cid),
            "roles": rows(c, "select a.role l, count(distinct a.path) v from artifact_links l join artifacts a using(path) where (l.target_kind='channel' and l.target_id=?) "
                             "or (l.target_kind='video' and l.target_id in (select video_id from videos where channel_id=?)) group by 1 order by v desc", cid, cid),
            "specific_files": spec_files, "videos_with_specific_file": len(sp["videos"])}


def channel(c, q, cid):
    ch = one(c, "select * from channels where channel_id=?", cid)
    if not ch: return None
    ch["sources"] = rows(c, "select * from channel_sources where channel_id=?", cid)
    ch["types"] = rows(c, "select video_type, count(*) n from videos where channel_id=? group by 1 order by n desc", cid)
    ch["artifacts"] = rows(c, "select a.path, a.role, a.format, a.videos_mentioned, l.via, l.mentions from artifact_links l join artifacts a using(path) "
                              "where l.target_kind='channel' and l.target_id=? order by a.videos_mentioned, a.path limit 300", cid)
    ch["stats"] = memo(("stats", cid), lambda: stats(c, cid))
    ch["video_artifact_count"] = c.execute("select count(distinct l.path) from artifact_links l join videos v on v.video_id=l.target_id "
                                           "where l.target_kind='video' and v.channel_id=?", (cid,)).fetchone()[0]
    return ch


STOP = set("""the and for that this with you your are was were have has had not but from they them their what when how why who which will would can could should about into out over than then there these those just like more most some any all one two our its his her she him also been being because very much many get got make made does did doing done than too only own same such here where while after before again up down off now new""".split())


def words(text):
    return [w for w in re.findall(r"[a-z][a-z']{2,}", text.lower())]


def ch_transcripts(c, q, cid):
    """Readable-transcript index for one channel + what its transcripts talk about (word and phrase counts)."""
    t = q.get("q", [""])[0].strip()
    base = ("from transcripts t join videos v using(video_id) join transcript_texts x on x.sha256=t.text_sha256 where v.channel_id=?")
    items = []
    for r in c.execute(f"select v.video_id, v.title, v.published_date, v.views, t.word_count, t.caption_kind, t.language, x.text {base} "
                       + ("and x.text like ? escape '\\' " if t else "") + "order by v.views desc nulls last limit 200", (cid, like(t)) if t else (cid,)):
        o = {"video_id": r[0], "title": r[1], "date": r[2], "views": r[3], "words": r[4], "kind": r[5], "lang": r[6]}
        if t:
            i = r[7].lower().find(t.lower()); o["hits"] = r[7].lower().count(t.lower()); o["snip"] = r[7][max(0, i - 90): i + len(t) + 90].replace("\n", " ")
        items.append(o)
    def top():
        cw, cb = collections.Counter(), collections.Counter()
        for (x,) in c.execute(f"select x.text {base}", (cid,)):
            w = words(x); cw.update(a for a in w if a not in STOP and len(a) > 3)
            cb.update(f"{a} {b}" for a, b in zip(w, w[1:]) if a not in STOP and b not in STOP and len(a) > 2 and len(b) > 2)
        return {"words": cw.most_common(40), "phrases": [p for p in cb.most_common(40) if p[1] > 2][:30]}
    tot = c.execute(f"select count(*), coalesce(sum(t.word_count),0) {base}", (cid,)).fetchone()
    return {"count": tot[0], "words_total": tot[1], "items": items, "query": t, **(memo(("tw", cid), top) if tot[0] and not t else {"words": [], "phrases": []})}


def ch_files(c, q, cid):
    """Every file that is specifically about this channel (channel-level, or naming 25 videos or fewer), with the numbers to group them."""
    sp = spec_index(c); out = {}
    for path, vids in sp["per"].get(cid, {"files": {}})["files"].items():
        m = sp["meta"][path]; out[path] = {"path": path, "role": m["role"], "format": m["format"], "videos_mentioned": m["videos_mentioned"], "n": len(vids), "kind": "video"}
    for r in rows(c, "select a.path, a.role, a.format, a.videos_mentioned, a.bytes from artifact_links l join artifacts a using(path) where l.target_kind='channel' and l.target_id=? and a.videos_mentioned<=25", cid):
        out.setdefault(r["path"], {**r, "n": 0})["kind"] = "channel"
    sizes = {r[0]: r[1] for r in c.execute("select path, bytes from artifacts where path in (%s)" % ",".join("?" * len(out)), list(out))} if out else {}
    for f in out.values(): f["bytes"] = sizes.get(f["path"])
    bulk = c.execute("select count(distinct l.path) from artifact_links l join videos v on v.video_id=l.target_id join artifacts a using(path) where l.target_kind='video' and v.channel_id=? and a.videos_mentioned>25", (cid,)).fetchone()[0]
    return {"files": sorted(out.values(), key=lambda f: (f["role"], -f["n"], f["path"])), "bulk_files": bulk}


def ch_quality(c, q, cid):
    ids = "select video_id from videos where channel_id=?"
    return {"conflicts": rows(c, f"select cf.*, v.title from conflicts cf join videos v using(video_id) where cf.video_id in ({ids}) order by field, cf.video_id", cid),
            "issues": rows(c, f"select qi.*, v.title from quality_issues qi join videos v using(video_id) where qi.video_id in ({ids}) order by issue, qi.video_id", cid),
            "sources_per_video": rows(c, "select source_count l, count(*) v from videos where channel_id=? group by 1 order by 1", cid),
            "mismatch": c.execute(f"select count(*) from transcript_candidates where sha_matches_source=0 and video_id in ({ids})", (cid,)).fetchone()[0]}


CH_SECTIONS = {"transcripts": ch_transcripts, "files": ch_files, "quality": ch_quality}


def videos(c, q):
    g = lambda k: q.get(k, [""])[0]
    where, args = [], []
    if g("q"): where.append("v.title like ? escape '\\'"); args.append(like(g("q")))
    if g("channel"): where.append("v.channel_id=?"); args.append(g("channel"))
    if g("type"): where.append("v.video_type=?"); args.append(g("type"))
    if g("tx") == "1": where.append("v.has_transcript=1")
    if g("year"): where.append("substr(v.published_date,1,4)=?"); args.append(g("year"))
    if g("tq"): where.append("v.video_id in (select t.video_id from transcripts t join transcript_texts x on x.sha256=t.text_sha256 where x.text like ? escape '\\')"); args.append(like(g("tq")))
    if g("art") == "1":
        sv = spec_index(c)["vids"]; c.create_function("is_spec", 1, lambda x: x in sv, deterministic=True); where.append("is_spec(v.video_id)")
    w = ("where " + " and ".join(where)) if where else ""
    page = max(int(g("page") or 1), 1); size = 50
    total = c.execute(f"select count(*) from videos v {w}", args).fetchone()[0]
    order = SORTS.get(g("sort"), SORTS["date"])
    if g("dir") == "asc": order = order.replace(" DESC", "") if " DESC" in order else order + " DESC"
    items = rows(c, f"select v.video_id, v.title, v.channel_id, c.name channel, v.published_date, v.duration_seconds, v.video_type, v.views, v.likes, "
                    f"v.has_transcript, v.source_count from videos v join channels c using(channel_id) {w} "
                    f"order by {order} nulls last, v.video_id limit ? offset ?", *args, size, (page - 1) * size)
    return {"total": total, "page": page, "size": size, "items": items}


def video(c, q, vid):
    v = one(c, "select v.*, c.name channel from videos v join channels c using(channel_id) where video_id=?", vid)
    if not v: return None
    vw = [r[0] for r in c.execute("select views from videos where channel_id=? and views is not null", (v["channel_id"],))]
    v["rank"] = {"of": len(vw), "pos": (sum(1 for x in vw if x > v["views"]) + 1) if v["views"] is not None else None, "median": median(vw)}
    v["sources"] = rows(c, "select * from video_sources where video_id=? order by source_id", vid)
    v["conflicts"] = rows(c, "select * from conflicts where video_id=?", vid)
    v["quality_issues"] = rows(c, "select * from quality_issues where video_id=?", vid)
    v["transcript"] = one(c, "select t.*, x.text from transcripts t join transcript_texts x on x.sha256=t.text_sha256 where t.video_id=?", vid)
    v["transcript_candidates"] = rows(c, "select * from transcript_candidates where video_id=? order by source_id", vid)
    v["artifacts"] = rows(c, "select a.path, a.role, a.format, a.area, a.videos_mentioned, l.via, l.mentions from artifact_links l join artifacts a using(path) "
                             "where l.target_kind='video' and l.target_id=? order by a.videos_mentioned, a.role, a.path", vid)
    return v


def artifacts(c, q):
    g = lambda k: q.get(k, [""])[0]
    where, args = [], []
    if g("q"): where.append("path like ? escape '\\'"); args.append(like(g("q")))
    for k in ("role", "area", "format"):
        if g(k): where.append(f"{k}=?"); args.append(g(k))
    if g("specific") == "1": where.append("videos_mentioned between 1 and 25")
    w = ("where " + " and ".join(where)) if where else ""
    page = max(int(g("page") or 1), 1); size = 50
    total = c.execute(f"select count(*) from artifacts {w}", args).fetchone()[0]
    items = rows(c, f"select * from artifacts {w} order by videos_mentioned desc, path limit ? offset ?", *args, size, (page - 1) * size)
    return {"total": total, "page": page, "size": size, "items": items,
            "roles": [r["role"] for r in rows(c, "select distinct role from artifacts order by 1")],
            "areas": [r["area"] for r in rows(c, "select distinct area from artifacts order by 1")]}


def artifact(c, q):
    p = q.get("path", [""])[0]
    a = one(c, "select * from artifacts where path=?", p)
    if not a: return None
    a["links"] = rows(c, "select l.target_kind, l.target_id, l.via, l.mentions, coalesce(v.title, ch.name) label from artifact_links l "
                         "left join videos v on l.target_kind='video' and v.video_id=l.target_id "
                         "left join channels ch on l.target_kind='channel' and ch.channel_id=l.target_id "
                         "where l.path=? order by l.target_kind, l.mentions desc limit 300", p)
    return a


def quality(c, q):
    return {"conflicts": rows(c, "select cf.*, v.title from conflicts cf join videos v using(video_id) order by field, video_id"),
            "issues": rows(c, "select qi.*, v.title from quality_issues qi left join videos v using(video_id) order by issue, video_id"),
            "unresolved_channels": rows(c, "select * from unresolved_channels"),
            "sha_mismatch": c.execute("select count(*) from transcript_candidates where sha_matches_source=0").fetchone()[0]}


PFX = r"(?:\w+:)?"  # some writers prefix every OOXML tag (<x:row>), most do not


def col(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(): n = n * 26 + ord(ch) - 64
    return n - 1


def attr(tag, name):
    m = re.search(r'(?:^|[\s<])' + re.escape(name) + r'="([^"]*)"', tag)
    return html.unescape(m.group(1)) if m else None


def texts(xml, tag="t"):
    """Concatenated text of every <t>/<w:t> element (OOXML text is plain XML; regex keeps this free of the XML parser, which some Pythons lack)."""
    return html.unescape("".join(re.findall(r"<" + PFX + tag + r"\b[^>]*>(.*?)</" + PFX + tag + ">", xml, re.S)))


def read_xlsx(f, maxrows=2000):
    """Sheets of an .xlsx as plain rows (stdlib only: an xlsx is a zip of XML). Values are the stored cell values, formulas are not evaluated."""
    z = zipfile.ZipFile(f)
    if any(i.file_size > 80_000_000 for i in z.infolist()): raise ValueError("workbook too large to preview")
    rd = lambda n: z.read(n).decode("utf-8", "replace")
    ss = [texts(re.sub(r"<" + PFX + r"rPh\b.*?</" + PFX + "rPh>", "", si, flags=re.S)) for si in re.findall(r"<" + PFX + r"si\b[^>]*>(.*?)</" + PFX + "si>", rd("xl/sharedStrings.xml"), re.S)] if "xl/sharedStrings.xml" in z.namelist() else []
    rels = {attr(t, "Id"): attr(t, "Target") for t in re.findall(r"<Relationship\b[^>]*>", rd("xl/_rels/workbook.xml.rels"))}
    out = []
    for t in re.findall(r"<" + PFX + r"sheet\b[^>]*>", rd("xl/workbook.xml")):
        rid = re.search(r'\b\w+:id="([^"]*)"', t); tgt = rels.get(rid.group(1) if rid else None, ""); tgt = tgt.lstrip("/") if tgt.startswith("/") else "xl/" + tgt
        rws, total = [], 0
        for rm in re.finditer(r"<" + PFX + r"row\b[^>]*?(?:/>|>(.*?)</" + PFX + "row>)", rd(tgt), re.S):
            total += 1
            if len(rws) >= maxrows: continue
            row = []
            for cm in re.finditer(r"<" + PFX + r"c\b([^>]*?)(?:/>|>(.*?)</" + PFX + "c>)", rm.group(1) or "", re.S):
                a, body = cm.group(1), cm.group(2) or ""; i = col(attr(a, "r")); row += [""] * (i + 1 - len(row)); v = re.search(r"<" + PFX + "v>(.*?)</" + PFX + "v>", body, re.S); ty = attr(a, "t")
                row[i] = ss[int(v.group(1))] if ty == "s" and v else texts(body) if ty == "inlineStr" else html.unescape(v.group(1)) if v else ""
            rws.append(row)
        out.append({"name": attr(t, "name"), "rows": rws, "total_rows": total})
    return {"kind": "sheets", "sheets": out}


def read_docx(f):
    xml = zipfile.ZipFile(f).read("word/document.xml").decode("utf-8", "replace")
    paras = [texts(re.sub(r"<w:(?:tab|br)\b[^>]*/>", "<w:t> </w:t>", p), "w:t") for p in re.findall(r"<w:p\b[^>]*>(.*?)</w:p>", xml, re.S)]
    return {"kind": "text", "paragraphs": [x for x in paras if x.strip()][:5000]}


def read_db(f):
    d = sqlite3.connect(f"file:{f}?mode=ro", uri=True); out = []
    try:
        for (name,) in d.execute("select name from sqlite_master where type='table' and name not like 'sqlite_%' order by name"):
            cur = d.execute(f'select * from "{name}" limit 50')
            out.append({"name": name, "cols": [x[0] for x in cur.description], "rows": [[v if isinstance(v, (int, float, str, type(None))) else f"<{len(v)} bytes>" for v in r] for r in cur],
                        "total_rows": d.execute(f'select count(*) from "{name}"').fetchone()[0]})
    finally: d.close()
    return {"kind": "db", "tables": out}


def read_zip(f):
    return {"kind": "zip", "entries": [[i.filename, i.file_size] for i in zipfile.ZipFile(f).infolist()][:2000]}


PEEK = {"xlsx": read_xlsx, "docx": read_docx, "db": read_db, "zip": read_zip}


def peek(c, q):
    p = q.get("path", [""])[0]
    if not c.execute("select 1 from artifacts where path=?", (p,)).fetchone(): return None  # whitelist: inventoried files only
    f, ext = os.path.join(R, p), p.rsplit(".", 1)[-1].lower()
    if ext not in PEEK: raise ValueError("no structured preview for ." + ext)
    if not os.path.isfile(f): raise ValueError("file not present in this checkout (LFS or other branch)")
    if ext != "db" and os.path.getsize(f) > MAX_RAW: raise ValueError("file too large to preview")
    try: return PEEK[ext](f)
    except (zipfile.BadZipFile, KeyError, AttributeError, TypeError, sqlite3.Error) as e: raise ValueError("could not read this file: " + str(e)[:100])


ROUTES = {"/api/peek": peek, "/api/summary": summary, "/api/channels": channels, "/api/videos": videos, "/api/artifacts": artifacts,
          "/api/artifact": artifact, "/api/quality": quality}


class H(BaseHTTPRequestHandler):
    def send(self, code, body, ctype, extra=(), gz=None):
        if gz is not None and "gzip" in self.headers.get("Accept-Encoding", ""): body, extra = gz, (*extra, ("Content-Encoding", "gzip"), ("Vary", "Accept-Encoding"))
        self.send_response(code)
        self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body)))
        for k, v in extra: self.send_header(k, v)
        self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(body)

    def js(self, obj, code=200):
        self.send(code, json.dumps(obj, ensure_ascii=False).encode(), "application/json; charset=utf-8")

    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query); p = u.path
        try:
            if p in ("/", "/index.html"):
                return self.send(200, open(INDEX, "rb").read(), "text/html; charset=utf-8")
            if p == "/raw":
                c = conn()
                try: return self.raw(c, q)
                finally: c.close()
            if p in ROUTES: fn = lambda c: ROUTES[p](c, q)
            elif p.startswith("/api/channel/") and p.count("/") == 4 and p.rsplit("/", 1)[1] in CH_SECTIONS:
                fn = lambda c: CH_SECTIONS[p.rsplit("/", 1)[1]](c, q, p.split("/")[3])
            elif p.startswith("/api/channel/"): fn = lambda c: channel(c, q, p.rsplit("/", 1)[1])
            elif p.startswith("/api/video/"): fn = lambda c: video(c, q, p.rsplit("/", 1)[1])
            else: return self.js({"error": "not found"}, 404)

            def build():  # json + gzip once per (url, DB version)
                c = conn()
                try: out = fn(c)
                finally: c.close()
                if out is None: return None
                b = json.dumps(out, ensure_ascii=False).encode()
                return b, (gzip.compress(b, 5) if len(b) > 1024 else None)
            r = memo(("http", self.path), build)
            if r is None: return self.js({"error": "not found"}, 404)
            self.send(200, r[0], "application/json; charset=utf-8", gz=r[1])
        except (ValueError, sqlite3.Error) as e:
            self.js({"error": str(e)}, 400)

    def raw(self, c, q):
        p = q.get("path", [""])[0]
        if not c.execute("select 1 from artifacts where path=?", (p,)).fetchone():  # whitelist: only inventoried files
            return self.js({"error": "not an inventoried artifact"}, 404)
        f = os.path.join(R, p)
        if not os.path.isfile(f): return self.js({"error": "file not present in this checkout (LFS or other branch)"}, 404)
        if os.path.getsize(f) > MAX_RAW: return self.js({"error": "file too large to preview"}, 413)
        data, name = open(f, "rb").read(), p
        if p.endswith(".gz"):  # show .json.gz / .jsonl.gz as their plain content
            try: data = gzip.decompress(data)
            except OSError: return self.js({"error": "not a valid gzip file"}, 415)
            if len(data) > MAX_RAW: return self.js({"error": "file too large to preview"}, 413)
            name = p[:-3]
        ct = mimetypes.guess_type(name)[0] or "text/plain"
        if ct.startswith("text/") or ct in ("application/json", "application/javascript"): ct += "; charset=utf-8"
        # sandbox: an inventoried .svg/.html opened directly can never run scripts on this origin
        pdf = ct == "application/pdf"  # a PDF cannot run page scripts, and the browser's viewer needs an un-sandboxed frame to show it inline
        self.send(200, data, ct, (("X-Content-Type-Options", "nosniff"),) if pdf else (("Content-Security-Policy", "sandbox"), ("X-Content-Type-Options", "nosniff")))

    def log_message(self, *a): pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--port", type=int, default=8020); a = ap.parse_args()
    if not os.path.exists(DB) and DB == f"{R}/data/catalog/yios_canonical.db":  # fresh checkout (e.g. 2nd Mac): build from the tracked source DBs
        print("canonical DB missing, building it from the tracked source databases (~1 min)...")
        for sc in (["build_yios_canonical_db.py", "build"], ["build_yios_artifact_inventory.py"]):
            subprocess.run([sys.executable, f"{R}/scripts/{sc[0]}", *sc[1:]], cwd=R, check=False)
    if not os.path.exists(DB): sys.exit(f"missing {DB}: run scripts/build_yios_canonical_db.py build, then scripts/build_yios_artifact_inventory.py")
    print(f"YIOS site on http://127.0.0.1:{a.port}  (db {DB}, read-only)")
    threading.Thread(target=lambda: spec_index(conn()), daemon=True).start()  # warm the one slow aggregate so the first page load is instant
    ThreadingHTTPServer(("127.0.0.1", a.port), H).serve_forever()
