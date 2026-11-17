"""Enumerate @xkcd_whatif Videos/Shorts/Live tabs via public YouTube web pages + innertube continuations.
Raw responses saved under census/raw/. Usage: python3 -I census_tabs.py <census_dir>"""
import json, re, sys, time, urllib.request, pathlib

D = pathlib.Path(sys.argv[1]); RAW = D / "raw"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"

def initial(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    return json.loads(m.group(1))

def walk(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key: yield v
            yield from walk(v, key)
    elif isinstance(o, list):
        for v in o: yield from walk(v, key)

def txt(t):
    if not t: return None
    if "simpleText" in t: return t["simpleText"]
    if "runs" in t: return "".join(r.get("text", "") for r in t["runs"])
    if "content" in t: return t["content"]
    return None

def items(data, tab):
    out = []
    for v in walk(data, "videoRenderer"):
        out.append(dict(video_id=v["videoId"], title=txt(v.get("title")), length_text=txt(v.get("lengthText")),
                        view_text=txt(v.get("viewCountText")), published_text=txt(v.get("publishedTimeText")),
                        listing=tab))
    for v in walk(data, "lockupViewModel"):
        if v.get("contentType") not in (None, "LOCKUP_CONTENT_TYPE_VIDEO"): continue
        meta = v.get("metadata", {}).get("lockupMetadataViewModel", {})
        rows = [p.get("text", {}).get("content") for r in walk(meta, "metadataRows") for row in r
                for p in row.get("metadataParts", [])]
        badges = [b.get("text") for b in walk(v.get("contentImage", {}), "thumbnailBadgeViewModel") for b in [b]]
        out.append(dict(video_id=v.get("contentId"), title=(meta.get("title") or {}).get("content"),
                        length_text=badges[0] if badges else None, meta_parts=rows, listing=tab))
    for v in walk(data, "shortsLockupViewModel"):
        vid = v.get("onTap", {}).get("innertubeCommand", {}).get("reelWatchEndpoint", {}).get("videoId")
        if not vid:
            m = re.search(r"/shorts/([\w-]{11})", json.dumps(v)); vid = m and m.group(1)
        ov = v.get("overlayMetadata", {})
        out.append(dict(video_id=vid, title=(ov.get("primaryText") or {}).get("content"),
                        view_text=(ov.get("secondaryText") or {}).get("content"), listing=tab))
    return out

def cont_token(data):
    scope = list(walk(data, "richGridRenderer")) + list(walk(data, "appendContinuationItemsAction"))
    toks = [c.get("continuationEndpoint", {}).get("continuationCommand", {}).get("token")
            for sc in scope for c in walk(sc, "continuationItemRenderer")]
    toks = [t for t in toks if t]
    return toks[-1] if toks else None

def main():
    html0 = (RAW / "page_videos.html").read_text()
    key = re.search(r'INNERTUBE_API_KEY":"([^"]+)"', html0).group(1)
    ver = re.search(r'"clientVersion":"([^"]+)"', html0).group(1)
    res = {}
    for tab in ("videos", "shorts"):
        data = initial((RAW / f"page_{tab}.html").read_text())
        got = items(data, tab); tok = cont_token(data); n = 0
        while tok:
            n += 1
            body = json.dumps({"context": {"client": {"clientName": "WEB", "clientVersion": ver, "hl": "en", "gl": "US"}},
                               "continuation": tok}).encode()
            req = urllib.request.Request(f"https://www.youtube.com/youtubei/v1/browse?key={key}&prettyPrint=false",
                                         data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
            raw = urllib.request.urlopen(req, timeout=30).read()
            (RAW / f"cont_{tab}_{n:02d}.json").write_bytes(raw)
            d = json.loads(raw); new = items(d, tab)
            seen = {i["video_id"] for i in got}
            if not [i for i in new if i["video_id"] not in seen]:
                print(tab, "no new ids on page", n, "-> stop"); tok = "STALLED"; break
            got += new; tok = cont_token(d); time.sleep(1.0)
        res[tab] = dict(pages=1 + n, items=got, exhausted=tok is None, stop_reason=tok and "STALLED_OR_TOKEN_LEFT" or "NO_CONTINUATION")
        print(tab, "pages", 1 + n, "items", len(got), "unique", len({i["video_id"] for i in got}))
    (D / "tab_listings.json").write_text(json.dumps(dict(snapshot_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                                       method="public youtube.com channel tab HTML ytInitialData + youtubei/v1/browse continuations",
                                                       tabs=res), indent=1))

main()
