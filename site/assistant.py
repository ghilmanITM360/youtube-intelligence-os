"""Research assistant for the YIOS site: evidence tools + a model loop (stdlib only).

The model never sees the repository directly. It can only call the read-only tools below, which answer from the canonical catalogue,
the full-text search index and the inventoried files. Which model answers is configured with environment variables (nothing is stored in the repo):

  ANTHROPIC_API_KEY  [YIOS_MODEL, default claude-sonnet-5-5]        Anthropic Messages API
  YIOS_LLM_BASE_URL  [YIOS_LLM_MODEL, YIOS_LLM_KEY]                   any OpenAI-compatible server (Ollama http://localhost:11434/v1, LM Studio, OpenAI ...)

With neither set, the assistant still answers with search results only (no model, nothing leaves this machine).
When a model is configured, the question and the excerpts the tools return are sent to that provider."""
import html, gzip, json, os, re, sqlite3, time, urllib.error, urllib.request

R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SEARCH_DB = os.environ.get("YIOS_SEARCH_DB", f"{R}/data/catalog/yios_search.db")
RESEARCH_ROLES = ("research", "intelligence report", "playbook", "what-if study", "reanalysis", "report", "audit", "forensic analysis")
MAX_OUT = 12000   # characters one tool result may return to the model
MAX_ROUNDS = 8
API = {}          # filled by bind(): conn, channel, videos, video, channels (functions from server.py)


def bind(**fns):
    API.update(fns)


def sconn():
    if not os.path.exists(SEARCH_DB): raise ValueError("search index missing: run scripts/build_yios_search_index.py")
    c = sqlite3.connect(f"file:{SEARCH_DB}?mode=ro", uri=True); c.row_factory = sqlite3.Row
    return c


# filler words (English + Roman-Urdu/Hindi) that match nearly every document and drown the real topic words
STOP = set("""the an of to for in on is are was were be what if how why who which when where about tell me show give find and or with from this that it its my our you your i we they them
channel channels video videos please can could would should do does did has have had any some all most more into than then there here also not no yes
kaye kay ke ka ki ko baraye liye batao bata bataye batain do de dena hai hain tha thi mein me main par pe aur ya se say ye yeh wo woh kya kaun kitna kitne kitni karo kar kare karna
dikhao dikha mujhe humain hamain hum ek ik wala wali ab to bhi bi jo jis kis koi sab saray sare""".split())


def fts_query(q, mode="and"):
    """User text -> a safe FTS5 query (every word quoted, so punctuation or operators in the question can never break or alter the query).
    Filler words are dropped (unless that would leave nothing)."""
    w = re.findall(r"[\w'-]{2,}", q.lower())
    w = ([x for x in w if x not in STOP] or w)[:12]
    return (" OR " if mode == "or" else " ").join('"' + x.replace('"', "") + '"' for x in w)


def search(q, kind="any", role="", channel="", collection="", limit=10, offset=0):
    """Ranked full-text search over research documents and transcripts. Returns items with a snippet, the file/video it came from and the channels tied to it."""
    s = sconn()
    try:
        for mode in ("and", "or"):
            m = fts_query(q, mode)
            if not m: return {"total": 0, "items": []}
            where, args = ["fts match ?"], [m]
            if kind in ("doc", "transcript"): where.append("d.kind=?"); args.append(kind)
            if role: where.append("d.role=?"); args.append(role)
            if collection: where.append("d.ref like ?"); args.append(collection.rstrip("/") + "/%")
            if channel: where.append("exists(select 1 from doc_channels dc where dc.doc_id=d.id and dc.channel_id=?)"); args.append(channel)
            w = " and ".join(where); frm = "from fts join docs d on d.id=fts.rowid"
            total = s.execute(f"select count(*) {frm} where {w}", args).fetchone()[0]
            if total or mode == "or": break
        items = []
        for r in s.execute(f"select d.id, d.kind, d.ref, d.title, d.role, d.bytes, snippet(fts, 1, '«', '»', ' … ', 24) snip {frm} where {w} order by bm25(fts, 4, 1) limit ? offset ?", [*args, limit, offset]):
            ties = [{"channel_id": t["channel_id"], "via": t["via"]} for t in s.execute("select channel_id, via from doc_channels where doc_id=? order by via limit 6", (r["id"],))]
            items.append({"kind": r["kind"], "ref": r["ref"], "title": r["title"], "role": r["role"], "bytes": r["bytes"], "snippet": r["snip"], "channels": ties})
        return {"total": total, "mode": mode, "items": items}
    finally: s.close()


def channel_docs(cid, limit=200):
    """Research-type documents tied to a channel: those containing its ids first, then those that only mention its name."""
    s = sconn()
    try:
        q = ",".join("?" * len(RESEARCH_ROLES))
        return [dict(r) for r in s.execute(
            f"select d.ref, d.title, d.role, d.bytes, dc.via, (select count(*) from doc_channels x where x.doc_id=d.id) nch, substr(replace(f.text, char(10), ' '), 1, 320) preview from doc_channels dc join docs d on d.id=dc.doc_id join fts f on f.rowid=d.id "
            f"where dc.channel_id=? and d.kind='doc' and d.ref not like '%SHA256SUMS%' and d.role in ({q}) order by (dc.via='id') desc, (d.ref like '%.md') desc, nch, d.role, d.bytes desc limit ?", (cid, *RESEARCH_ROLES, limit))]
    finally: s.close()


def collections():
    s = sconn()
    try:
        out = {}
        for ref, role, n in s.execute("select ref, role, count(*) from docs where kind='doc' group by ref, role"):
            seg = ref.split("/"); key = "/".join(seg[:2]) if len(seg) > 2 and seg[0] in ("research", "data", "docs") else seg[0] if len(seg) > 1 else "(repo root)"
            d = out.setdefault(key, {"collection": key, "docs": 0, "roles": {}}); d["docs"] += n; d["roles"][role] = d["roles"].get(role, 0) + n
        return sorted(out.values(), key=lambda d: -d["docs"])
    finally: s.close()


# ---------------------------------------------------------------- tools
def _cap(o):
    t = json.dumps(o, ensure_ascii=False, default=str)
    return t if len(t) <= MAX_OUT else t[:MAX_OUT] + f'… [truncated, {len(t)} chars; narrow the request]'


def t_find_channels(a):
    c = API["conn"](); q = "%" + str(a.get("query", "")).replace("%", "").replace("_", "") + "%"
    try:
        return [dict(r) for r in c.execute("select c.channel_id, c.name, c.handle, c.subscribers, count(v.video_id) videos, sum(v.views) views from channels c left join videos v using(channel_id) "
                                           "where c.name like ? or c.handle like ? or c.channel_id=? group by 1 order by videos desc limit ?", (q, q, a.get("query", ""), min(int(a.get("limit", 10)), 30)))]
    finally: c.close()


def t_channel_overview(a):
    c = API["conn"]()
    try:
        ch = API["channel"](c, {}, a["channel_id"])
        if not ch: return {"error": "unknown channel_id"}
        st = ch["stats"]; top = sorted((v for v in st["all"] if v[5] is not None), key=lambda v: -v[5])[:10]
        return {"channel_id": ch["channel_id"], "name": ch["name"], "handle": ch["handle"], "subscribers": ch["subscribers"], "reported_total_videos": ch["channel_total_videos"],
                "videos_in_catalogue": st["n"], "views_total": st["views_total"], "views_median": st["views_median"], "views_max": st["views_max"], "first": st["first"], "last": st["last"],
                "median_gap_days": st["gap_days_median"], "likes_per_view_pct": st["engagement"], "by_year": [(y["l"], y["v"], y["views"]) for y in st["by_year"]], "types": ch["types"],
                "transcripts": sum(k["v"] for k in st["caption_kinds"]), "files_by_role": st["roles"], "specific_files": len(st["specific_files"]),
                "top_videos": [{"video_id": v[0], "title": v[1], "date": v[2], "views": v[5], "type": v[4]} for v in top],
                "note": "Counts come from the catalogue; a channel with 0 videos has only its record. Use search_research / list_videos for more."}
    finally: c.close()


def t_list_videos(a):
    c = API["conn"]()
    try:
        q = {k: [str(a[k])] for k in ("channel", "q", "tq", "year", "sort", "dir", "tx", "type") if a.get(k) not in (None, "")}
        if a.get("channel_id"): q["channel"] = [a["channel_id"]]
        d = API["videos"](c, q)
        return {"total": d["total"], "items": [{"video_id": v["video_id"], "title": v["title"], "channel": v["channel"], "date": v["published_date"], "views": v["views"], "likes": v["likes"], "type": v["video_type"], "has_transcript": bool(v["has_transcript"])} for v in d["items"][: min(int(a.get("limit", 15)), 30)]]}
    finally: c.close()


def t_get_video(a):
    c = API["conn"]()
    try:
        v = API["video"](c, {}, a["video_id"])
        if not v: return {"error": "unknown video_id"}
        t = v.get("transcript"); off = int(a.get("transcript_offset", 0)); n = min(int(a.get("transcript_chars", 3000)), 9000)
        return {"video_id": v["video_id"], "title": v["title"], "channel": v["channel"], "channel_id": v["channel_id"], "published": v["published_date"], "duration_seconds": v["duration_seconds"], "type": v["video_type"],
                "views": v["views"], "likes": v["likes"], "comments": v["comments"], "rank_in_channel": v["rank"], "description": (v["description"] or "")[:1500],
                "transcript": {"caption_kind": t["caption_kind"], "language": t["language"], "words": t["word_count"], "total_chars": len(t["text"]), "offset": off, "text": t["text"][off: off + n]} if t else None,
                "files_naming_this_video": [{"path": x["path"], "role": x["role"], "videos_in_file": x["videos_mentioned"]} for x in v["artifacts"] if x["videos_mentioned"] <= 25][:15]}
    finally: c.close()


def t_search_research(a):
    d = search(a.get("query", ""), a.get("kind", "any"), a.get("role", ""), a.get("channel_id", ""), a.get("collection", ""), min(int(a.get("limit", 8)), 15))
    for it in d["items"]: it["snippet"] = it["snippet"][:500]
    return d


def t_read_document(a):
    c = API["conn"]()
    try:
        p = str(a.get("path", ""))
        if not c.execute("select 1 from artifacts where path=?", (p,)).fetchone(): return {"error": "not an inventoried file; use search_research to find paths"}
        f = os.path.join(R, p)
        if not os.path.isfile(f): return {"error": "file not present in this checkout"}
        raw = open(f, "rb").read(30_000_000)
        if p.endswith(".gz"): raw = gzip.decompress(raw)
        if b"\0" in raw[:2000]: return {"error": "binary file; no text to read"}
        t = raw.decode("utf-8", "replace"); off = int(a.get("offset", 0)); n = min(int(a.get("length", 8000)), 10000)
        return {"path": p, "total_chars": len(t), "offset": off, "next_offset": off + n if off + n < len(t) else None, "text": t[off: off + n]}
    finally: c.close()


def t_sql_query(a):
    sql = str(a.get("sql", "")).strip().rstrip(";")
    if not re.match(r"(?is)^\s*(select|with)\b", sql) or ";" in sql: return {"error": "one SELECT (or WITH ... SELECT) statement only"}
    c = API["conn"]()
    try:
        c.set_authorizer(lambda act, *x: sqlite3.SQLITE_DENY if act in (sqlite3.SQLITE_ATTACH, sqlite3.SQLITE_DETACH, sqlite3.SQLITE_PRAGMA) else sqlite3.SQLITE_OK)
        t0 = time.time(); c.set_progress_handler(lambda: 1 if time.time() - t0 > 6 else 0, 20000)
        try: cur = c.execute(sql); rows = cur.fetchmany(100)
        except sqlite3.Error as e: return {"error": str(e)}
        return {"columns": [d[0] for d in cur.description], "rows": [list(r) for r in rows], "truncated_at_100": len(rows) == 100}
    finally: c.close()


SCHEMA = ("Tables: channels(channel_id, name, handle, subscribers, channel_total_videos, channel_total_views); videos(video_id, channel_id, title, published_date 'YYYY-MM-DD', duration_seconds, video_type LONG|SHORT|STREAM|UNKNOWN, "
          "views, likes, comments, description, has_transcript, source_count); transcripts(video_id, caption_kind, language, word_count); artifacts(path, area, format, role, bytes, videos_mentioned, channels_mentioned); "
          "artifact_links(path, target_kind 'video'|'channel', target_id, via, mentions); conflicts(video_id, field, chosen_value, other_value); quality_issues(video_id, source_id, field, raw_value, issue).")
TOOLS = [
    ("find_channels", "Find channels by (part of) name, handle or id.", {"query": "string", "limit": "integer?"}, t_find_channels),
    ("channel_overview", "Numbers and top videos for one channel: views, median, upload years, types, transcripts and how many files exist about it.", {"channel_id": "string"}, t_channel_overview),
    ("list_videos", "List videos with filters. sort: views|likes|duration|date|title; dir: asc to reverse; q searches titles; tq searches inside transcripts; year like 2024; tx '1' = has transcript; type LONG|SHORT|STREAM.",
     {"channel_id": "string?", "q": "string?", "tq": "string?", "year": "string?", "sort": "string?", "dir": "string?", "tx": "string?", "type": "string?", "limit": "integer?"}, t_list_videos),
    ("get_video", "One video: metadata, rank in its channel, description, a slice of its transcript (use transcript_offset to read further) and the files that name it.", {"video_id": "string", "transcript_offset": "integer?", "transcript_chars": "integer?"}, t_get_video),
    ("search_research", "Full-text search over the repository's research documents (reports, audits, playbooks, forensic analyses, studies) and over transcripts. kind: doc|transcript|any. Results carry the file path or video id, a snippet and the channels tied to it "
     "(via 'id' = the text contains the channel's/video's id, 'name' = only the channel's name appears: a lead, not an analysis).", {"query": "string", "channel_id": "string?", "kind": "string?", "role": "string?", "collection": "string?", "limit": "integer?"}, t_search_research),
    ("read_document", "Read an inventoried text file (markdown, json, csv, txt) by path, in slices of up to 10000 characters (offset/length).", {"path": "string", "offset": "integer?", "length": "integer?"}, t_read_document),
    ("sql_query", "Read-only SQL (one SELECT, max 100 rows) over the catalogue for counts and comparisons. " + SCHEMA, {"sql": "string"}, t_sql_query),
]
TOOL_FN = {n: f for n, _, _, f in TOOLS}


def run_tool(name, args):
    if name not in TOOL_FN: return _cap({"error": "unknown tool " + name})
    try: return _cap(TOOL_FN[name](args or {}))
    except (KeyError, ValueError, TypeError, sqlite3.Error) as e: return _cap({"error": f"{type(e).__name__}: {e}"})


def schema_for(kind):
    def prop(t):
        base = t.rstrip("?"); return {"type": "integer" if base == "integer" else "string"}
    out = []
    for n, d, props, _ in TOOLS:
        sch = {"type": "object", "properties": {k: prop(v) for k, v in props.items()}, "required": [k for k, v in props.items() if not v.endswith("?")]}
        out.append({"name": n, "description": d, "input_schema": sch} if kind == "anthropic" else {"type": "function", "function": {"name": n, "description": d, "parameters": sch}})
    return out


# ---------------------------------------------------------------- models
SYSTEM = """You are the research assistant of the YouTube Intelligence OS (YIOS), a local evidence repository about YouTube channels, their videos, transcripts and the research documents written about them.

Rules you must follow:
1. Answer only from tool results. Use the tools before answering; never use memory as a source about a channel or video. If the tools return nothing relevant, say so plainly.
2. Cite every claim: a file as [file: path], a video as [video: VIDEO_ID], a channel as [channel: UC...]. Numbers come from tool output (say which tool or table).
3. Keep three things apart and label them: FACT (in the data), INTERPRETATION (your reading of it), HYPOTHESIS (a testable guess). Never present an inference as a fact.
4. A document 'mentioning' a channel or video is not an analysis of it. A pattern in views is a correlation: never claim a title, thumbnail or topic caused views.
5. Say when evidence is thin (few videos, no transcripts, 0 collected videos, missing likes/comments) and what data would settle it.
6. Prefer several focused tool calls over one broad one. Read the most relevant documents with read_document before summarising them.
7. You cannot change any data. Answer in the user's language (Hinglish is fine), concise, with short tables or lists when comparing."""


def provider():
    if os.environ.get("ANTHROPIC_API_KEY"): return "anthropic", os.environ.get("YIOS_MODEL", "claude-sonnet-5-5")
    if os.environ.get("YIOS_LLM_BASE_URL"): return "openai", os.environ.get("YIOS_LLM_MODEL", "llama3.1")
    return None, None


def _post(url, headers, body):
    req = urllib.request.Request(url, json.dumps(body).encode(), {"content-type": "application/json", **headers}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as r: return json.load(r)
    except urllib.error.HTTPError as e: raise RuntimeError(f"model API error {e.code}: {e.read()[:400].decode('utf-8', 'replace')}")
    except (urllib.error.URLError, TimeoutError) as e: raise RuntimeError(f"could not reach the model API: {e}")


def call_model(messages, system):
    """One model turn. messages use Anthropic-style blocks; returns (content_blocks, usage)."""
    prov, model = provider()
    if prov == "anthropic":
        r = _post("https://api.anthropic.com/v1/messages", {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"},
                  {"model": model, "max_tokens": 4096, "system": system, "tools": schema_for("anthropic"), "messages": messages})
        return r["content"], r.get("usage", {})
    base = os.environ["YIOS_LLM_BASE_URL"].rstrip("/"); msgs = [{"role": "system", "content": system}]
    for m in messages:
        if isinstance(m["content"], str): msgs.append(m); continue
        if m["role"] == "assistant":
            calls = [{"id": b["id"], "type": "function", "function": {"name": b["name"], "arguments": json.dumps(b["input"])}} for b in m["content"] if b["type"] == "tool_use"]
            msgs.append({"role": "assistant", "content": "".join(b.get("text", "") for b in m["content"] if b["type"] == "text") or None, **({"tool_calls": calls} if calls else {})})
        else:
            for b in m["content"]: msgs.append({"role": "tool", "tool_call_id": b["tool_use_id"], "content": b["content"]})
    hdr = {"authorization": "Bearer " + os.environ["YIOS_LLM_KEY"]} if os.environ.get("YIOS_LLM_KEY") else {}
    r = _post(base + "/chat/completions", hdr, {"model": model, "messages": msgs, "tools": schema_for("openai")})
    m = r["choices"][0]["message"]; blocks = [{"type": "text", "text": m["content"]}] if m.get("content") else []
    for c in m.get("tool_calls") or []:
        try: inp = json.loads(c["function"]["arguments"] or "{}")
        except ValueError: inp = {}
        blocks.append({"type": "tool_use", "id": c["id"], "name": c["function"]["name"], "input": inp})
    return blocks, r.get("usage", {})


def chat(history, emit, channel_id=None, model_fn=None):
    """Run one assistant turn. history = [{role, content: str}], emit(event dict). model_fn is injectable for tests."""
    call = model_fn or call_model
    system = SYSTEM + (f"\n\nThe user is looking at channel {channel_id}; unless they say otherwise, questions are about it." if channel_id else "")
    msgs = [{"role": m["role"], "content": str(m["content"])[:20000]} for m in history[-20:] if m.get("role") in ("user", "assistant")]
    used = {"input_tokens": 0, "output_tokens": 0}
    for _ in range(MAX_ROUNDS):
        blocks, usage = call(msgs, system)
        used["input_tokens"] += usage.get("input_tokens", usage.get("prompt_tokens", 0)) or 0; used["output_tokens"] += usage.get("output_tokens", usage.get("completion_tokens", 0)) or 0
        for b in blocks:
            if b["type"] == "text" and b["text"].strip(): emit({"type": "text", "text": b["text"]})
        uses = [b for b in blocks if b["type"] == "tool_use"]
        if not uses: break
        msgs.append({"role": "assistant", "content": [{k: b[k] for k in ("type", "text", "id", "name", "input") if k in b} for b in blocks]}); results = []
        for b in uses:
            emit({"type": "tool", "name": b["name"], "input": b["input"]}); out = run_tool(b["name"], b["input"])
            emit({"type": "tool_result", "name": b["name"], "chars": len(out)}); results.append({"type": "tool_result", "tool_use_id": b["id"], "content": out})
        msgs.append({"role": "user", "content": results})
    else: emit({"type": "text", "text": "\n\n(Stopped after " + str(MAX_ROUNDS) + " rounds of tool calls; ask a narrower follow-up to continue.)"})
    emit({"type": "done", "usage": used})


def clean(snip):
    """Snippet for display: drop transcript timestamps, turn the « » hit markers into bold."""
    return re.sub(r"\s+", " ", re.sub(r"\[\d+\.\d+\]\s*", "", snip)).replace("«", "**").replace("»", "**").strip()


def norm(s):
    return " ".join(re.sub(r"[^\w\s]", " ", re.sub(r"['\u2019]s\b", "", s.lower())).split())


def match_channels(question, limit=5):
    """Channels the question refers to: the longest run of question words found inside a channel name (a single word needs 5+ letters and must not be filler)."""
    qw = norm(question).split()
    grams = {" ".join(qw[i:i + n]) for n in (3, 2, 1) for i in range(len(qw) - n + 1)}
    grams = [g for g in grams if " " in g or (len(g) >= 5 and g not in STOP)]
    if not grams: return []
    c = API["conn"]()
    try: rows = c.execute("select c.channel_id, c.name, c.handle, count(v.video_id) videos from channels c left join videos v using(channel_id) group by 1").fetchall()
    finally: c.close()
    out = []
    for r in rows:
        hay = " " + norm((r["name"] or "") + " " + (r["handle"] or "").lstrip("@")) + " "
        hit = [g for g in grams if f" {g} " in hay and any(w not in STOP for w in g.split())] or [g for g in grams if " " in g and f" {g} " in hay]
        if hit: out.append((max(len(g.split()) for g in hit), max(len(g) for g in hit), r["videos"], dict(r)))
    out.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    return [((o[0], o[1]), o[3]) for o in out[:limit]]


def retrieval_only(question, channel_id, emit):
    """No model configured: answer with the evidence itself (the channel the question names, its research documents, ranked search hits)."""
    emit({"type": "text", "text": "No AI model is configured, so this is search only (nothing left this machine). Set `ANTHROPIC_API_KEY` (or `YIOS_LLM_BASE_URL`) and restart the site to get written answers.\n"})
    found = match_channels(question)
    scope = channel_id or ""
    # the question names one channel when its best match is unique (ties like "blood pressure" are a topic, not a channel)
    if found and not scope and found[0][1]["videos"] and (len(found) == 1 or found[0][0] != found[1][0]): scope = found[0][1]["channel_id"]
    if found and not channel_id:
        emit({"type": "text", "text": "\n**Channels matching your words**\n" + "\n".join(f"- [channel: {c['channel_id']}] {html.unescape(c['name'] or '')} ({c['videos']} videos)" for _, c in found) + "\n"})
    if scope:
        ov = json.loads(run_tool("channel_overview", {"channel_id": scope}))
        if "error" not in ov:
            emit({"type": "tool", "name": "channel_overview", "input": {"channel_id": scope}})
            top = "\n".join(f"  - [video: {v['video_id']}] {v['title']} ({v['views']:,} views)" for v in ov["top_videos"][:5] if v["views"] is not None)
            emit({"type": "text", "text": f"\n**{html.unescape(ov['name'] or '')}** [channel: {scope}]: {ov['videos_in_catalogue']} videos, {ov['views_total'] or 0:,} views in total (median {ov['views_median'] or 0:,}), {ov['first']} to {ov['last']}, {ov['transcripts']} transcripts, {ov['specific_files']} channel-specific files.\n"
                                      + ("Most viewed:\n" + top + "\n" if top else "")})
    for kind, label in (("doc", "Research documents"), ("transcript", "Transcripts")):
        emit({"type": "tool", "name": "search_research", "input": {"query": question, "kind": kind}})
        topic = [x for x in re.findall(r"[\w'-]{2,}", question.lower()) if x not in STOP]
        if scope and not topic and kind == "transcript": continue  # the question only named the channel: its overview and files above are the answer
        d = search(question, kind, channel=scope, limit=6) if topic or not scope else {"total": 0, "items": []}
        if not d["items"] and scope and kind == "doc":  # the question only named the channel: list what has been written about it
            docs = channel_docs(scope, 8)
            emit({"type": "text", "text": f"\n**{label}** (research tied to this channel: {len(docs)} shown, ids first)\n" + ("\n".join(f"- [file: {x['ref']}] {x['title']}" + (" (name only)" if x["via"] == "name" else "") for x in docs) or "- nothing found") + "\n"})
            continue
        emit({"type": "text", "text": f"\n**{label}** ({d['total']} hits)\n" + ("\n".join(f"- [{'file' if kind == 'doc' else 'video'}: {i['ref']}] {i['title']} — {clean(i['snippet'])}" for i in d["items"]) or "- nothing found") + "\n"})
    emit({"type": "done", "usage": {}})
