import importlib.util, json, sqlite3, threading, urllib.error, urllib.parse, urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def get(base, path):
    try:
        with urllib.request.urlopen(base + path) as r: return r.status, r.read()
    except urllib.error.HTTPError as e: return e.code, e.read()


def test_every_endpoint_answers_and_raw_is_whitelisted(tmp_path, monkeypatch):
    canon, inv, site = load("canon", "scripts/build_yios_canonical_db.py"), load("inv", "scripts/build_yios_artifact_inventory.py"), load("site", "site/server.py")
    db = str(tmp_path / "c.db")
    monkeypatch.setattr(canon, "OUT", db); monkeypatch.setattr(canon, "MANIFEST", str(tmp_path / "m.json"))
    canon.build()
    monkeypatch.setattr(inv, "DB", db); inv.main()
    monkeypatch.setattr(site, "DB", db)
    srv = ThreadingHTTPServer(("127.0.0.1", 0), site.H); threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    try:
        c = sqlite3.connect(db)
        vid, cid = c.execute("select video_id, channel_id from videos where has_transcript=1 limit 1").fetchone()
        path = c.execute("select path from artifacts where format='markdown' limit 1").fetchone()[0]
        for p in ["/", "/api/summary", "/api/channels", f"/api/channel/{cid}", "/api/videos?sort=views&tx=1&page=2", f"/api/video/{vid}",
                  "/api/artifacts?specific=1", f"/api/artifact?path={path}", "/api/quality", "/api/videos?q=100%25"]:
            assert get(base, p)[0] == 200, p
        assert json.loads(get(base, f"/api/video/{vid}")[1])["transcript"]["text"]
        st = json.loads(get(base, f"/api/channel/{cid}")[1])["stats"]  # per-channel report aggregates reconcile with the catalogue
        assert st["n"] == c.execute("select count(*) from videos where channel_id=?", (cid,)).fetchone()[0] and sum(x["v"] for x in st["by_year"]) <= st["n"]
        assert json.loads(get(base, "/api/summary")[1])["by_year"]
        gz = c.execute("select path from artifacts where path like '%.gz' limit 1").fetchone()
        if gz: assert get(base, f"/raw?path={gz[0]}")[0] in (200, 404)  # .gz is shown decompressed (404 only if the file is absent in this checkout)
        assert len(st["all"]) == st["n"] and sum(t["v"] for t in st["by_type"]) == st["n"]  # the all-videos table and per-type split cover every video
        ch = json.loads(get(base, "/api/channels")[1]); assert ch and "median" in ch[0] and "spark" in ch[0]
        for p in ["/api/videos?year=2024&dir=asc&sort=views", "/api/videos?art=1&tx=1", "/api/videos?tq=the", "/api/summary"]: assert get(base, p)[0] == 200, p
        assert json.loads(get(base, f"/api/video/{vid}")[1])["rank"]["of"] >= 1
        req = urllib.request.Request(base + "/api/channels", headers={"Accept-Encoding": "gzip"})
        with urllib.request.urlopen(req) as r: assert r.headers["Content-Encoding"] == "gzip"  # big JSON is compressed
        for sec in ("transcripts", "files", "quality", "transcripts?q=the"): assert get(base, f"/api/channel/{cid}/{sec}")[0] == 200, sec  # per-channel tabs
        assert json.loads(get(base, f"/api/channel/{cid}/transcripts")[1])["count"] >= 1
        for ext in ("xlsx", "docx", "zip"):  # structured previews, when such a file is inventoried and present in this checkout
            r = c.execute("select path from artifacts where path like ? limit 1", ("%." + ext,)).fetchone()
            if r and (ROOT / r[0]).exists(): assert get(base, "/api/peek?path=" + urllib.parse.quote(r[0]))[0] == 200, ext
        assert get(base, "/api/peek?path=../../etc/passwd")[0] == 404  # not inventoried -> never opened
        assert get(base, "/api/video/nope000000x")[0] == 404
        assert get(base, "/raw?path=../../../../etc/passwd")[0] == 404  # not in the inventory -> never read
        assert get(base, "/api/videos?sort=views%3Bdrop%20table%20videos")[0] == 200  # unknown sort falls back, never reaches SQL
    finally:
        srv.shutdown()
