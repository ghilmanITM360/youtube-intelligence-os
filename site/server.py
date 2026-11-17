#!/usr/bin/env python3
"""Read-only local website over data/catalog/yios_canonical.db (stdlib only, no build step).

  python3 site/server.py [--port 8020]        then open http://127.0.0.1:8020

Build the DB first: scripts/build_yios_canonical_db.py build && scripts/build_yios_artifact_inventory.py
The DB is opened read-only; /raw serves only files that the artifact inventory lists (no path traversal)."""
import argparse, gzip, json, mimetypes, os, sqlite3, subprocess, sys
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
    return [dict(r) for r in c.execute(sql, a)]


def one(c, sql, *a):
    r = c.execute(sql, a).fetchone()
    return dict(r) if r else None


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
            "videos_with_specific_artifact": c.execute("select count(distinct target_id) from artifact_links l join artifacts a using(path) "
                                                       "where l.target_kind='video' and a.videos_mentioned<=25").fetchone()[0]}


def channels(c, q):
    return rows(c, "select c.channel_id, c.name, c.handle, c.subscribers, count(v.video_id) videos, sum(v.views) views, "
                   "sum(v.has_transcript) transcripts, min(v.published_date) first_date, max(v.published_date) last_date, c.source_count "
                   "from channels c left join videos v using(channel_id) group by c.channel_id order by videos desc")


def stats(c, cid):
    """Aggregates for one channel's report page (computed on demand, nothing stored)."""
    vs = rows(c, "select video_id, title, published_date, duration_seconds d, video_type, views, likes, comments, has_transcript from videos where channel_id=?", cid)
    vw = sorted(v["views"] for v in vs if v["views"] is not None)
    med = (vw[len(vw) // 2] if len(vw) % 2 else (vw[len(vw) // 2 - 1] + vw[len(vw) // 2]) / 2) if vw else None
    bucket = lambda x, edges, labels: labels[next((i for i, e in enumerate(edges) if x < e), len(edges))]
    dur = {}; vb = {}
    for v in vs:
        k = "unknown" if v["d"] is None else bucket(v["d"], [60, 300, 600, 1200, 2400, 3600], ["<1 min", "1-5 min", "5-10 min", "10-20 min", "20-40 min", "40-60 min", ">60 min"])
        dur[k] = dur.get(k, 0) + 1
        if v["views"] is not None:
            k = bucket(v["views"], [1e3, 1e4, 1e5, 1e6], ["<1K", "1K-10K", "10K-100K", "100K-1M", ">1M"]); vb[k] = vb.get(k, 0) + 1
    order = lambda d, labels: [{"l": l, "v": d[l]} for l in labels if l in d]
    dated = [v for v in vs if v["published_date"]]
    return {"n": len(vs), "views_total": sum(vw), "views_median": med, "views_max": vw[-1] if vw else None, "likes_total": sum(v["likes"] or 0 for v in vs),
            "avg_minutes": round(sum(v["d"] for v in vs if v["d"]) / max(1, sum(1 for v in vs if v["d"])) / 60, 1),
            "first": min((v["published_date"] for v in dated), default=None), "last": max((v["published_date"] for v in dated), default=None),
            "durations": order(dur, ["<1 min", "1-5 min", "5-10 min", "10-20 min", "20-40 min", "40-60 min", ">60 min", "unknown"]),
            "view_buckets": order(vb, ["<1K", "1K-10K", "10K-100K", "100K-1M", ">1M"]),
            "by_month": rows(c, "select substr(published_date,1,7) l, count(*) v, sum(views) views from videos where channel_id=? and published_date is not null group by 1 order by 1", cid),
            "by_year": rows(c, "select substr(published_date,1,4) l, count(*) v, sum(views) views from videos where channel_id=? and published_date is not null group by 1 order by 1", cid),
            "weekday": rows(c, "select cast(strftime('%w', published_date) as int) l, count(*) v from videos where channel_id=? and published_date is not null group by 1 order by 1", cid),
            "top": sorted((v for v in vs if v["views"] is not None), key=lambda v: -v["views"])[:10],
            "latest": sorted(dated, key=lambda v: v["published_date"], reverse=True)[:10],
            "caption_kinds": rows(c, "select t.caption_kind l, count(*) v from transcripts t join videos v using(video_id) where v.channel_id=? group by 1 order by v desc", cid),
            "roles": rows(c, "select a.role l, count(distinct a.path) v from artifact_links l join artifacts a using(path) where (l.target_kind='channel' and l.target_id=?) "
                             "or (l.target_kind='video' and l.target_id in (select video_id from videos where channel_id=?)) group by 1 order by v desc", cid, cid),
            "specific_files": rows(c, "select a.path, a.role, a.format, a.videos_mentioned, count(distinct l.target_id) n from artifact_links l join artifacts a using(path) "
                                      "join videos v on v.video_id=l.target_id where l.target_kind='video' and v.channel_id=? and a.videos_mentioned<=25 "
                                      "group by a.path order by n desc, a.path limit 100", cid),
            "videos_with_specific_file": c.execute("select count(distinct l.target_id) from artifact_links l join artifacts a using(path) join videos v on v.video_id=l.target_id "
                                                   "where l.target_kind='video' and v.channel_id=? and a.videos_mentioned<=25", (cid,)).fetchone()[0]}


def channel(c, q, cid):
    ch = one(c, "select * from channels where channel_id=?", cid)
    if not ch: return None
    ch["sources"] = rows(c, "select * from channel_sources where channel_id=?", cid)
    ch["types"] = rows(c, "select video_type, count(*) n from videos where channel_id=? group by 1 order by n desc", cid)
    ch["artifacts"] = rows(c, "select a.path, a.role, a.format, a.videos_mentioned, l.via, l.mentions from artifact_links l join artifacts a using(path) "
                              "where l.target_kind='channel' and l.target_id=? order by a.videos_mentioned, a.path limit 300", cid)
    ch["stats"] = stats(c, cid)
    ch["video_artifact_count"] = c.execute("select count(distinct l.path) from artifact_links l join videos v on v.video_id=l.target_id "
                                           "where l.target_kind='video' and v.channel_id=?", (cid,)).fetchone()[0]
    return ch


def videos(c, q):
    g = lambda k: q.get(k, [""])[0]
    where, args = [], []
    if g("q"): where.append("v.title like ? escape '\\'"); args.append(like(g("q")))
    if g("channel"): where.append("v.channel_id=?"); args.append(g("channel"))
    if g("type"): where.append("v.video_type=?"); args.append(g("type"))
    if g("tx") == "1": where.append("v.has_transcript=1")
    if g("art") == "1": where.append("exists(select 1 from artifact_links l join artifacts a using(path) where l.target_kind='video' "
                                     "and l.target_id=v.video_id and a.videos_mentioned<=25)")
    w = ("where " + " and ".join(where)) if where else ""
    page = max(int(g("page") or 1), 1); size = 50
    total = c.execute(f"select count(*) from videos v {w}", args).fetchone()[0]
    order = SORTS.get(g("sort"), SORTS["date"])
    items = rows(c, f"select v.video_id, v.title, v.channel_id, c.name channel, v.published_date, v.duration_seconds, v.video_type, v.views, v.likes, "
                    f"v.has_transcript, v.source_count from videos v join channels c using(channel_id) {w} "
                    f"order by {order} nulls last, v.video_id limit ? offset ?", *args, size, (page - 1) * size)
    return {"total": total, "page": page, "size": size, "items": items}


def video(c, q, vid):
    v = one(c, "select v.*, c.name channel from videos v join channels c using(channel_id) where video_id=?", vid)
    if not v: return None
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


ROUTES = {"/api/summary": summary, "/api/channels": channels, "/api/videos": videos, "/api/artifacts": artifacts,
          "/api/artifact": artifact, "/api/quality": quality}


class H(BaseHTTPRequestHandler):
    def send(self, code, body, ctype, extra=()):
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
            c = conn()
            try:
                if p == "/raw": return self.raw(c, q)
                if p in ROUTES:
                    out = ROUTES[p](c, q)
                elif p.startswith("/api/channel/"): out = channel(c, q, p.rsplit("/", 1)[1])
                elif p.startswith("/api/video/"): out = video(c, q, p.rsplit("/", 1)[1])
                else: return self.js({"error": "not found"}, 404)
            finally:
                c.close()
            self.js(out) if out is not None else self.js({"error": "not found"}, 404)
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
        self.send(200, data, ct, (("Content-Security-Policy", "sandbox"), ("X-Content-Type-Options", "nosniff")))

    def log_message(self, *a): pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--port", type=int, default=8020); a = ap.parse_args()
    if not os.path.exists(DB) and DB == f"{R}/data/catalog/yios_canonical.db":  # fresh checkout (e.g. 2nd Mac): build from the tracked source DBs
        print("canonical DB missing, building it from the tracked source databases (~1 min)...")
        for sc in (["build_yios_canonical_db.py", "build"], ["build_yios_artifact_inventory.py"]):
            subprocess.run([sys.executable, f"{R}/scripts/{sc[0]}", *sc[1:]], cwd=R, check=False)
    if not os.path.exists(DB): sys.exit(f"missing {DB}: run scripts/build_yios_canonical_db.py build, then scripts/build_yios_artifact_inventory.py")
    print(f"YIOS site on http://127.0.0.1:{a.port}  (db {DB}, read-only)")
    ThreadingHTTPServer(("127.0.0.1", a.port), H).serve_forever()
