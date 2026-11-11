#!/usr/bin/env python3
"""Build data/catalog/finance_economics_complete.db: every Finance / investing / economics channel, video,
description, thumbnail URL and transcript the repo holds, in one rebuildable SQLite file.

  python3 scripts/build_finance_economics_complete_db.py stage-transcripts   # tar timestamped .txt from the local audit dirs (re-run as backfill grows)
  python3 scripts/build_finance_economics_complete_db.py build               # rebuild the DB from repo files only

Read-only on the frozen registry DB and on research/finance-economics-master/sources. Precedence for scalar video
fields: apify 2026-11-11 > apify 2026-11-10 > machine_a expansion > registry > machine_a universe/landscape/queue >
casual_finance index; first non-empty value wins, every contributing source is recorded."""
import csv, datetime, glob, gzip, hashlib, io, json, os, re, sqlite3, sys, tarfile

R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
M = f"{R}/research/finance-economics-master"
S = f"{M}/sources"
REG = f"{R}/data/catalog/youtube_channel_registry.db"
OUT = f"{R}/data/catalog/finance_economics_complete.db"
AUD = os.path.expanduser("~/YIOS-local-audits")
TX = {"apify_2026-11-10": f"{AUD}/2026-11-10-finance-apify-run/transcripts",
      "apify_2026-11-11": f"{AUD}/2026-11-11-finance-economics-db-merge/pipeline/transcripts"}
csv.field_size_limit(1 << 30)


def sha(b): return hashlib.sha256(b).hexdigest()
def rcsv(p): return list(csv.DictReader(open(p, newline="", encoding="utf-8")))
def rjsonl_gz(p): return [json.loads(l) for l in gzip.open(p, "rt", encoding="utf-8") if l.strip()]
def num(x):
    try: return int(float(x))
    except Exception: return None
def abbrev(s):  # "272K" / "1.2M" / "3,400"
    m = re.match(r"^([\d.,]+)\s*([KMB]?)", str(s or "").strip(), re.I)
    return int(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2).upper()]) if m else None
def hms(s):
    try:
        r = 0
        for x in str(s).split(":"): r = r * 60 + int(x)
        return r
    except Exception: return None


def stage_transcripts():
    for tag, d in TX.items():
        out = f"{S}/transcripts_{tag}.tar.gz"
        with tarfile.open(out, "w:gz", compresslevel=9) as t:
            for p in sorted(glob.glob(f"{d}/*/*.transcript.txt") + glob.glob(f"{d}/*/*.whisper_*.transcript.txt")):
                t.add(p, arcname=os.path.relpath(p, d))
        print(out, os.path.getsize(out))
        import shutil; shutil.copy(f"{os.path.dirname(d)}/TRANSCRIPT_COVERAGE.csv" if tag.endswith("10") else f"{os.path.dirname(d)}/TRANSCRIPT_COVERAGE.csv", f"{S}/{tag}/TRANSCRIPT_COVERAGE.csv")


def plain(txt):  # timestamped transcript -> plain text
    return " ".join(re.sub(r"^\[[\d.]+ --> [\d.]+\] ", "", l) for l in txt.splitlines() if l and not l.startswith("#"))


def read_tar(tag):
    p = f"{S}/transcripts_{tag}.tar.gz"
    out = {}
    if os.path.exists(p):
        with tarfile.open(p) as t:
            for m in t.getmembers():
                if m.isfile(): out[m.name] = t.extractfile(m).read().decode("utf-8")
    return out


def build():
    if os.path.exists(OUT): os.remove(OUT)
    db = sqlite3.connect(OUT)
    db.executescript("""
create table channels(channel_id text primary key, name text, handle text, url text, niche text, sub_niche text,
  availability text, availability_note text, subscribers integer, channel_total_videos integer, channel_total_views integer,
  joined text, description text, reported_videos integer, videos_in_db integer, transcripts_in_db integer, thumbnails_in_db integer,
  data_category text, sources text);
create table videos(video_id text primary key, channel_id text references channels(channel_id), url text, title text,
  published text, duration_seconds integer, video_type text, views integer, likes integer, comments integer,
  description text, hashtags text, keywords text, thumbnail_url text, thumbnail_source text, metadata_level text,
  has_transcript integer, sources text);
create table transcripts(video_id text references videos(video_id), source text, caption_type text, language text,
  status text, text text, word_count integer, sha256 text, origin text, primary key(video_id, source));
create table apify_rows(video_id text, channel_id text, batch text, raw_json text);
create index ix_v on videos(channel_id); create index ix_t on transcripts(video_id);
create table meta(k text primary key, v text);
""")
    # ---- channel universe
    ch = {}
    for r in rcsv(f"{M}/CHANNEL_DATA_SORT_initial.csv"):
        ch[r["channel_id"]] = dict(channel_id=r["channel_id"], name=r["channel"], niche=r["niche"], reported=num(r["reported_videos"]),
                                   sources=set(), availability="AVAILABLE")
    sub = {}
    for f in ("Filter_Finance", "Filter_Economics"):
        for r in rcsv(f"{S}/stage_a/{f}.csv"): sub[r["canonical_channel_id"]] = r["sub_niche"]
    vids, trs = {}, {}
    def C(cid, name=None):
        x = ch.setdefault(cid, dict(channel_id=cid, name=name, niche="FINANCE", sources=set(), availability="AVAILABLE"))
        return x
    def V(src, level, **row):
        vid = row["video_id"]
        v = vids.setdefault(vid, dict(video_id=vid, sources=[], metadata_level=level))
        for k, x in row.items():
            if x not in (None, "") and v.get(k) in (None, ""): v[k] = x
        if src not in v["sources"]: v["sources"].append(src)
        if level == "FULL": v["metadata_level"] = "FULL"
        elif v["metadata_level"] != "FULL" and level == "PARTIAL": v["metadata_level"] = "PARTIAL"
        if v.get("channel_id"): C(v["channel_id"])["sources"].add(src)
    def T(vid, src, cap, lang, status, text, origin):
        if not text: return
        trs[(vid, src)] = (vid, src, cap, lang, status, text, len(text.split()), sha(text.encode()), origin)

    # ---- apify batches (newest first for precedence); also channel-level info from raw datasets
    for tag in ("apify_2026-11-11", "apify_2026-11-10"):
        for r in rjsonl_gz(f"{S}/{tag}/VIDEO_MASTER_ALL.jsonl.gz"):
            C(r["channel_id"], r["channel_name"]).update(handle=r.get("channel_handle"), url=r.get("channel_url"))
            V(tag, "FULL", video_id=r["video_id"], channel_id=r["channel_id"], url=r["watch_url"], title=r["title"],
              published=r["publication_timestamp_utc"], duration_seconds=r["duration_seconds"], video_type=r["video_type"],
              views=r["view_count"], likes=r["like_count"], comments=r["comment_count"], description=r["description"],
              hashtags=json.dumps(r["hashtags"]) if r.get("hashtags") else None,
              keywords=json.dumps(r["keywords"]) if r.get("keywords") else None, thumbnail_url=r["thumbnail_url"])
        for p in sorted(glob.glob(f"{S}/{tag}/raw/*_dataset.json.gz")):
            for row in json.load(gzip.open(p, "rt", encoding="utf-8")):
                a = row.get("aboutChannelInfo") or {}
                cid = row.get("channelId") or a.get("channelId")
                if row.get("id"): db.execute("insert into apify_rows values(?,?,?,?)", (row["id"], cid, tag, json.dumps(row, ensure_ascii=False)))
                if cid and a:
                    x = C(cid, a.get("channelName"))
                    for k, f in (("subscribers", "numberOfSubscribers"), ("channel_total_videos", "channelTotalVideos"),
                                 ("channel_total_views", "channelTotalViews")): x.setdefault(k, num(a.get(f)))
                    x.setdefault("joined", a.get("channelJoinedDate")); x.setdefault("description", a.get("channelDescription"))
    # apify transcripts
    for tag in ("apify_2026-11-10", "apify_2026-11-11"):
        tar = read_tar(tag)
        for r in rcsv(f"{S}/{tag}/TRANSCRIPT_COVERAGE.csv"):
            k = r["transcript_path"].split("/", 1)[-1]
            if r["status"] in ("COMPLETE", "PARTIAL") and k in tar:
                T(r["video_id"], r["source"], r["track"], r["language"], r["status"], plain(tar[k]), tag)
        if tag == "apify_2026-11-10":
            for r in rcsv(f"{S}/{tag}/WHISPER_SUPPLEMENT.csv"):
                k = r["transcript_path"].split("/", 1)[-1]
                if k in tar:
                    T(r["video_id"], r["source"], r["model"], "en", "COMPLETE_ASR", plain(tar[k]), tag)
    # unavailable channels
    for u in json.load(open(f"{S}/apify_2026-11-11/UNAVAILABLE_CHANNELS.json")):
        x = C(u["channel_id"]); x.update(availability="UNAVAILABLE_OR_DELETED", availability_note=json.dumps(u["row"].get("additionalData") or "removed"))
        x["sources"].add("apify_2026-11-11")

    # ---- machine A expansion masters (rich metadata) + landscape + universe + queue
    for f in ("EXPANSION_12_CHANNEL_MASTER.csv", "EXPANSION_MONKEY_MASTER.csv"):
        for r in rcsv(f"{S}/machine_a/{f}"):
            C(r["channel_id"], r["channel_name"]).setdefault("url", r["channel_url"])
            V("machine_a_expansion", "FULL", video_id=r["video_id"], channel_id=r["channel_id"], url=r["watch_url"], title=r["title"],
              published=r["publication_timestamp_utc"], duration_seconds=num(r["duration_seconds"]), video_type=r["video_type"],
              views=num(r["view_count"]), likes=num(r["like_count"]), comments=num(r["comment_count"]), description=r["description"],
              hashtags=r["hashtags"], keywords=r["keywords"], thumbnail_url=r["thumbnail_url"])
    # ---- registry slice
    reg = sqlite3.connect(f"file:{REG}?mode=ro", uri=True)
    for cid in list(ch):
        for v in reg.execute("select youtube_video_id,canonical_url,title,published_at,duration_seconds,video_type,views,likes,comments,description,thumbnail_url "
                             "from videos where canonical_channel_id=?", (cid,)):
            V("registry", "FULL", video_id=v[0], channel_id=cid, url=v[1], title=v[2], published=v[3], duration_seconds=v[4], video_type=v[5],
              views=v[6], likes=v[7], comments=v[8], description=v[9], thumbnail_url=v[10])
            for t in reg.execute("select transcript_text,language,caption_type,dataset_id from transcripts where youtube_video_id=? "
                                 "and coalesce(is_placeholder,0)=0 and transcript_text is not null and transcript_text<>''", (v[0],)):
                T(v[0], "registry:" + t[3], t[2], t[1], "COMPLETE", t[0], "registry")
    # machine A universe / landscape / queue (title-level where nothing richer exists)
    for r in rcsv(f"{S}/machine_a/FINANCE_UNIVERSE.csv"):
        if r["inclusion_decision"] != "INCLUDE" and r["channel_id"] not in ch: continue
        C(r["channel_id"], r["channel_name"])
        V("machine_a_universe", "TITLE_ONLY", video_id=r["video_id"], channel_id=r["channel_id"], url=r["video_url"], title=r["title"])
    for r in rcsv(f"{S}/machine_a/LANDSCAPE_VIDEOS.csv"):
        C(r["Channel_ID"], r["Channel"])
        V("machine_a_landscape", "PARTIAL", video_id=r["Video_ID"], channel_id=r["Channel_ID"], title=r["Title"],
          views=abbrev(r["Views_display"]), duration_seconds=hms(r["Duration_display"]), video_type=r["Format_basis"])
    for r in rcsv(f"{S}/machine_a/FINANCE_CONTINUATION_QUEUE.csv"):
        if r["video_id"] in vids: V("machine_a_queue", "PARTIAL", video_id=r["video_id"], views=num(r["views"]))
        else:
            C(r["channel_id"], r["channel_name"]); V("machine_a_queue", "PARTIAL", video_id=r["video_id"], channel_id=r["channel_id"], views=num(r["views"]))
    # ---- casual finance (catalog + Whisper ASR transcripts, kept as source casual_finance:whisper_base)
    cf = None
    for r in rcsv(f"{S}/casual_finance/INDEX.csv"):
        cf = cf or "UCrNfRFWnLC3tCy1TnyhVQ7g"
        V("casual_finance_index", "PARTIAL", video_id=r["video_id"], channel_id=cf, url=f"https://www.youtube.com/watch?v={r['video_id']}",
          title=r["title"], published=r["published_at"], duration_seconds=num(r["duration_sec"]), video_type=r["format"], views=num(r["views"]))
    for p in glob.glob(f"{S}/casual_finance/transcripts_asr_base_20261109/*.json"):
        d = json.load(open(p))
        T(d["video_id"], "casual_finance:whisper_base", "whisper-base", d.get("language"), d.get("status", "ASR_UNCERTIFIED"),
          (d.get("text") or "").strip(), "casual_finance_asr_20261109")

    # ---- thumbnails: actor URL where captured, else the standard YouTube pattern (labelled)
    for v in vids.values():
        if v.get("thumbnail_url"): v["thumbnail_source"] = "captured"
        else: v["thumbnail_url"] = f"https://i.ytimg.com/vi/{v['video_id']}/hqdefault.jpg"; v["thumbnail_source"] = "derived_standard_pattern"
        v.setdefault("url", f"https://www.youtube.com/watch?v={v['video_id']}")
    vids = {k: v for k, v in vids.items() if v.get("channel_id") in ch}
    # ---- per-channel cap (owner decision 2026-11-11): metadata <=100/channel = newest 50 + top-viewed 30 + low-viewed (>=90d old) 20,
    # topped up by next-newest. Transcript targets (for backfill) = newest 30 + top 20 + low 10 within the kept set. Casual Finance exempt.
    CF = "UCrNfRFWnLC3tCy1TnyhVQ7g"; cutoff = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=90)).strftime("%Y-%m-%d")
    def pick(vs, n_new, n_top, n_low, total):
        vs = sorted(vs, key=lambda v: v.get("published") or "", reverse=True); keep = {v["video_id"] for v in vs[:n_new]}
        rest = [v for v in vs if v["video_id"] not in keep]
        keep |= {v["video_id"] for v in sorted(rest, key=lambda v: -(v.get("views") or 0))[:n_top]}
        rest = [v for v in vs if v["video_id"] not in keep and (not v.get("published") or v["published"][:10] <= cutoff)]
        keep |= {v["video_id"] for v in sorted(rest, key=lambda v: v.get("views") or 0)[:n_low]}
        for v in vs:
            if len(keep) >= total: break
            keep.add(v["video_id"])
        return keep
    bych = {}
    for v in vids.values(): bych.setdefault(v["channel_id"], []).append(v)
    kept, targets, dropped = {}, set(), 0
    for cid, vs in bych.items():
        if cid == CF: k = {v["video_id"] for v in vs}; targets |= k
        else:
            k = pick(vs, 50, 30, 20, 100) if len(vs) > 100 else {v["video_id"] for v in vs}
            kv = [v for v in vs if v["video_id"] in k]; targets |= pick(kv, 30, 20, 10, 60) if len(kv) > 60 else k
        dropped += len(vs) - len(k); kept.update({i: vids[i] for i in k})
    vids = kept; print("cap: dropped", dropped, "videos; kept", len(vids))
    with open(f"{M}/TRANSCRIPT_TARGETS.txt", "w") as f: f.write("\n".join(sorted(targets)))
    have_t = {vid for (vid, _s) in trs}
    for v in vids.values(): v["has_transcript"] = 1 if v["video_id"] in have_t else 0

    # ---- channel stats + category
    st = {}
    for v in vids.values():
        s = st.setdefault(v["channel_id"], [0, 0, 0]); s[0] += 1; s[1] += v["has_transcript"]; s[2] += v["thumbnail_source"] == "captured"
    for cid, x in ch.items():
        n, t, th = st.get(cid, [0, 0, 0]); rep = x.get("reported"); capd = min(rep, 100) if rep and cid != CF else rep
        if x["availability"] != "AVAILABLE" and not n: cat = "UNAVAILABLE_OR_DELETED"
        elif not n: cat = "NONE"
        elif t >= 0.95 * n and (not capd or n >= 0.95 * capd) and th >= 0.95 * n: cat = "COMPLETE"
        elif t == 0: cat = "METADATA_ONLY"
        elif capd and n < 0.95 * capd: cat = "PARTIAL_VIDEOS"
        else: cat = "PARTIAL_TRANSCRIPTS"
        x.update(n=n, t=t, th=th, cat=cat)
        db.execute("insert into channels values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (cid, x.get("name"), x.get("handle"), x.get("url") or f"https://www.youtube.com/channel/{cid}", x.get("niche"), sub.get(cid),
                    x["availability"], x.get("availability_note"), x.get("subscribers"), x.get("channel_total_videos"), x.get("channel_total_views"),
                    x.get("joined"), x.get("description"), rep, n, t, th, cat, ";".join(sorted(x["sources"]))))
    cols = ["video_id", "channel_id", "url", "title", "published", "duration_seconds", "video_type", "views", "likes", "comments",
            "description", "hashtags", "keywords", "thumbnail_url", "thumbnail_source", "metadata_level", "has_transcript"]
    for v in vids.values():
        db.execute(f"insert into videos values({','.join('?' * 18)})", [v.get(c) for c in cols] + [";".join(v["sources"])])
    db.executemany("insert into transcripts values(?,?,?,?,?,?,?,?,?)", [t for k, t in trs.items() if k[0] in vids])
    db.execute("delete from apify_rows where video_id not in (select video_id from videos)")
    db.execute("insert into meta values('built_from_registry_sha256',?)", (sha(open(REG, "rb").read()),))
    db.commit()
    for q in ["select niche,data_category,count(*),sum(videos_in_db),sum(transcripts_in_db) from channels group by 1,2",
              "select count(*) from videos", "select count(*) from transcripts", "select count(*) from videos where has_transcript=1",
              "select count(*) from videos where thumbnail_source='captured'", "pragma foreign_key_check", "pragma integrity_check"]:
        print(q, db.execute(q).fetchall())
    db.execute("vacuum"); db.close()
    with open(f"{M}/CHANNEL_DATA_FINAL.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["niche", "channel", "channel_id", "reported_videos", "videos", "transcripts", "captured_thumbnails", "category", "availability", "sources"])
        for cid, x in sorted(ch.items(), key=lambda kv: (kv[1]["niche"], kv[1]["name"] or "")):
            w.writerow([x["niche"], x.get("name"), cid, x.get("reported"), x["n"], x["t"], x["th"], x["cat"], x["availability"], ";".join(sorted(x["sources"]))])


if __name__ == "__main__":
    {"stage-transcripts": stage_transcripts, "build": build}[sys.argv[1]]()
