#!/usr/bin/env python3
"""Full-text search index over the repo's research documents and the transcripts (stdlib, SQLite FTS5).

  python3 scripts/build_yios_search_index.py          -> data/catalog/yios_search.db  (gitignored, rebuildable)

Reads data/catalog/yios_canonical.db and the inventoried files; never writes to them. Used by the website's Research page and the Ask assistant.
Every hit keeps its provenance: kind ('doc' = an inventoried file, 'transcript' = a stored transcript), ref (file path or video id) and
how it was tied to a channel ('id' = the file/transcript contains that channel's or video's id, 'name' = the channel's name appears in the text).
A 'name' tie is a lead only: a mention is not an analysis."""
import html, json, os, re, sqlite3, sys, time

R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CAN = os.environ.get("YIOS_CANONICAL_DB", f"{R}/data/catalog/yios_canonical.db")
OUT = os.environ.get("YIOS_SEARCH_DB", f"{R}/data/catalog/yios_search.db")
TEXT_FORMATS = ("markdown", "text", "html", "json", "jsonl")
MAX_CHARS = 400_000      # per file
MAX_JSON_BYTES = 400_000  # bigger JSON is data, not prose


def title_of(path, text):
    m = re.search(r"^#{1,3}\s+(.+)$", text, re.M) or re.search(r'"title"\s*:\s*"([^"]{4,160})"', text[:4000])
    return (m.group(1).strip() if m else os.path.basename(path))[:200]


def strings(o, out, n=0):
    """Leaf strings of a JSON value (the prose inside analysis files), capped."""
    if n > 60_000: return
    if isinstance(o, str):
        if len(o) > 3: out.append(o)
    elif isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str) and len(v) > 3: out.append(f"{k}: {v}")
            else: strings(v, out, n + len(out))
    elif isinstance(o, list):
        for v in o: strings(v, out, n + len(out))


def read(path, fmt, nbytes):
    f = os.path.join(R, path)
    if not os.path.isfile(f): return None
    if fmt in ("json", "jsonl") and nbytes and nbytes > MAX_JSON_BYTES: return None
    raw = open(f, "rb").read(MAX_CHARS * 2).decode("utf-8", "replace")
    if fmt == "html": raw = html.unescape(re.sub(r"<(script|style)\b.*?</\1>|<[^>]+>", " ", raw, flags=re.S | re.I))
    if fmt == "json":
        try: parts = []; strings(json.loads(raw), parts); raw = "\n".join(parts)
        except ValueError: pass
    if fmt == "jsonl":
        parts = []
        for line in raw.splitlines()[:2000]:
            try: strings(json.loads(line), parts)
            except ValueError: pass
        raw = "\n".join(parts)
    return raw[:MAX_CHARS]


def main():
    t0 = time.time()
    if not os.path.exists(CAN): sys.exit(f"missing {CAN}: build the canonical DB first")
    c = sqlite3.connect(f"file:{CAN}?mode=ro", uri=True)
    if os.path.exists(OUT): os.remove(OUT)
    o = sqlite3.connect(OUT)
    o.executescript("""
      create table docs(id integer primary key, kind text, ref text, title text, role text, bytes integer);
      create table doc_channels(doc_id integer, channel_id text, via text);
      create index idx_dc_doc on doc_channels(doc_id); create index idx_dc_ch on doc_channels(channel_id);
      create index idx_docs_ref on docs(kind, ref);
      create virtual table fts using fts5(title, text, tokenize='porter unicode61');""")
    # channel ties through ids (links table) and names
    by_path = {}
    for p, kind, tid in c.execute("select l.path, l.target_kind, l.target_id from artifact_links l"):
        by_path.setdefault(p, set()).add(tid if kind == "channel" else (kind, tid))
    vid_ch = dict(c.execute("select video_id, channel_id from videos"))
    names = [(cid, n.lower()) for cid, n in c.execute("select channel_id, name from channels") if n and (len(n) >= 8 or " " in n.strip())]
    handles = [(cid, h.lower().lstrip("@")) for cid, h in c.execute("select channel_id, handle from channels") if h and len(h.lstrip("@")) >= 6]
    n_docs = 0
    for path, role, fmt, nbytes in c.execute(f"select path, role, format, bytes from artifacts where format in ({','.join('?' * len(TEXT_FORMATS))}) order by path", TEXT_FORMATS):
        text = read(path, fmt, nbytes)
        if not text or len(text) < 40: continue
        cur = o.execute("insert into docs(kind, ref, title, role, bytes) values('doc', ?, ?, ?, ?)", (path, title_of(path, text), role, nbytes))
        did = cur.lastrowid; o.execute("insert into fts(rowid, title, text) values(?, ?, ?)", (did, title_of(path, text), text))
        ties = {}
        for t in by_path.get(path, ()):
            if isinstance(t, tuple):
                ch = vid_ch.get(t[1]) if t[0] == "video" else None
            else: ch = t
            if ch: ties[ch] = "id"
        if role in ("research", "intelligence report", "playbook", "what-if study", "reanalysis", "report", "audit", "forensic analysis") and fmt in ("markdown", "text"):
            low = text.lower()
            for cid, n in names:
                if cid not in ties and n in low: ties[cid] = "name"
            for cid, hnd in handles:
                if cid not in ties and hnd in low: ties[cid] = "name"
        o.executemany("insert into doc_channels values(?,?,?)", [(did, ch, via) for ch, via in ties.items()])
        n_docs += 1
        if n_docs % 500 == 0: print(f"  {n_docs} documents...", flush=True)
    n_tx = 0
    for vid, title, cid, text in c.execute("select v.video_id, v.title, v.channel_id, x.text from transcripts t join videos v using(video_id) join transcript_texts x on x.sha256=t.text_sha256"):
        cur = o.execute("insert into docs(kind, ref, title, role, bytes) values('transcript', ?, ?, 'transcript', ?)", (vid, title or vid, len(text)))
        o.execute("insert into fts(rowid, title, text) values(?, ?, ?)", (cur.lastrowid, title or vid, text))
        o.execute("insert into doc_channels values(?,?, 'id')", (cur.lastrowid, cid)); n_tx += 1
    o.execute("insert into fts(fts) values('optimize')"); o.commit(); o.close()
    print(f"search index: {n_docs} documents + {n_tx} transcripts -> {OUT} ({os.path.getsize(OUT) / 1e6:.0f} MB, {time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
