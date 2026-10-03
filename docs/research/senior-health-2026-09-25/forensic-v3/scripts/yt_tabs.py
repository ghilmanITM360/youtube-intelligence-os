"""Enumerate public Videos/Shorts/Streams tab video IDs for a channel from youtube.com web pages."""
import json, re, sys, urllib.request, time

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9", "Cookie": "CONSENT=YES+1; SOCS=CAI"}

def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers={**UA, **({"Content-Type": "application/json"} if data else {})})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

DETAILS = {}  # videoId -> listing-card text exactly as YouTube rendered it (views/age/duration/thumbnail)


def _texts(o):
    """Every visible 'content' string inside a lockup metadata subtree, in order."""
    if isinstance(o, dict):
        if isinstance(o.get("content"), str):
            yield o["content"]
        for v in o.values():
            yield from _texts(v)
    elif isinstance(o, list):
        for v in o:
            yield from _texts(v)


def _badge(o):
    for t in _texts_key(o, "thumbnailBadgeViewModel"):
        return t.get("text")


def _texts_key(o, key):
    if isinstance(o, dict):
        if key in o:
            yield o[key]
        for v in o.values():
            yield from _texts_key(v, key)
    elif isinstance(o, list):
        for v in o:
            yield from _texts_key(v, key)


def walk(o, out, conts):
    if isinstance(o, dict):
        if "videoId" in o and "videoRenderer" not in o and ("lengthText" in o or "viewCountText" in o):
            g = lambda k: (o.get(k) or {}).get("simpleText") or "".join(r.get("text", "") for r in (o.get(k) or {}).get("runs", []))
            DETAILS.setdefault(o["videoId"], {"views_text": g("viewCountText"), "published_text": g("publishedTimeText"),
                                              "duration_text": g("lengthText"),
                                              "thumbnail_url": ((o.get("thumbnail") or {}).get("thumbnails") or [{}])[-1].get("url")})
        if "videoId" in o and ("title" in o or "headline" in o) and "thumbnail" in o:
            t = o.get("title") or o.get("headline") or {}
            txt = t.get("simpleText") or "".join(r.get("text", "") for r in t.get("runs", []))
            out.setdefault(o["videoId"], txt)
        if "shortsLockupViewModel" in o:
            v = o["shortsLockupViewModel"]
            vid = v.get("onTap", {}).get("innertubeCommand", {}).get("reelWatchEndpoint", {}).get("videoId")
            if vid:
                out.setdefault(vid, v.get("overlayMetadata", {}).get("primaryText", {}).get("content", ""))
                DETAILS.setdefault(vid, {"views_text": v.get("overlayMetadata", {}).get("secondaryText", {}).get("content"),
                                         "accessibility_text": v.get("accessibilityText"),
                                         "thumbnail_url": ((v.get("onTap", {}).get("innertubeCommand", {}).get("reelWatchEndpoint", {})
                                                            .get("thumbnail") or {}).get("thumbnails") or [{}])[-1].get("url")})
        if "lockupViewModel" in o and o["lockupViewModel"].get("contentType") in (None, "LOCKUP_CONTENT_TYPE_VIDEO"):
            v = o["lockupViewModel"]
            if v.get("contentId"):
                md = v.get("metadata", {}).get("lockupMetadataViewModel", {})
                out.setdefault(v["contentId"], md.get("title", {}).get("content", ""))
                srcs = (((v.get("contentImage") or {}).get("thumbnailViewModel") or {}).get("image") or {}).get("sources") or [{}]
                DETAILS.setdefault(v["contentId"], {"metadata_text": list(_texts(md.get("metadata", {}))),
                                                    "duration_text": _badge(v.get("contentImage")),
                                                    "thumbnail_url": srcs[-1].get("url")})
        if "continuationCommand" in o:
            conts.append(o["continuationCommand"]["token"])
        for v in o.values(): walk(v, out, conts)
    elif isinstance(o, list):
        for v in o: walk(v, out, conts)

def tab(cid, name):
    html = get(f"https://www.youtube.com/channel/{cid}/{name}")
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m: return None, "NO_INITIAL_DATA"
    data = json.loads(m.group(1))
    # confirm the selected tab is really the one requested (YouTube falls back to Home when a tab is absent)
    sel = [t["tabRenderer"]["title"] for t in data.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", [])
           if "tabRenderer" in t and t["tabRenderer"].get("selected")]
    key = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', html).group(1)
    ctx = json.loads(re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html).group(1))
    if not sel or sel[0].lower() != {"videos": "videos", "shorts": "shorts", "streams": "live"}[name]:
        return {}, "TAB_ABSENT(" + (sel[0] if sel else "NONE") + ")"
    out, conts = {}, []
    walk(data, out, conts)
    seen = set()
    while conts:
        tok = conts.pop()
        if tok in seen: continue
        seen.add(tok)
        time.sleep(0.4)
        j = json.loads(get(f"https://www.youtube.com/youtubei/v1/browse?key={key}", json.dumps({"context": ctx, "continuation": tok}).encode()))
        walk(j.get("onResponseReceivedActions", []), out, conts)
    return out, (sel[0] if sel else "NONE")


def details_for(ids):
    return {i: DETAILS[i] for i in ids if i in DETAILS}

def header(cid):
    html = get(f"https://www.youtube.com/channel/{cid}")
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    name = re.search(r'<meta property="og:title" content="([^"]*)"', html)
    vids = re.search(r'"content":"([\d,.KM]+) videos?"', html)
    subs = re.search(r'"content":"([\d,.KM]+) subscribers"', html)
    handle = re.search(r'"canonicalBaseUrl":"/(@[^"]+)"', html)
    removed = re.search(r'(This channel was removed[^"<]*|This account has been terminated[^"<]*|doesn\'t have any content)', html)
    return dict(canonical=canon and canon.group(1), name=name and name.group(1), handle=handle and handle.group(1),
                header_videos=vids and vids.group(1), subscribers=subs and subs.group(1), removed=removed and removed.group(1))

def resolve(ref):
    if ref.startswith("UC"): return ref, None
    html = get(f"https://www.youtube.com/{ref}")
    m = re.search(r'<link rel="canonical" href="https://www.youtube.com/channel/(UC[\w-]{22})"', html)
    return (m.group(1), None) if m else (None, "HANDLE_UNRESOLVED")

if __name__ == "__main__":
    ref = sys.argv[1]
    try: cid, err = resolve(ref)
    except Exception as e: cid, err = None, "HANDLE_UNRESOLVED:" + repr(e)
    if not cid:
        print(json.dumps({"ref": ref, "channel_id": None, "error": err})); sys.exit()
    res = {"ref": ref, "channel_id": cid, "observed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), **header(cid), "tabs": {}}
    # "doesn't have any content" is also YouTube's empty-Home-tab placeholder, so it is only final once every tab is empty
    home_only_empty = bool(res["removed"]) and "any content" in res["removed"]
    if not res["removed"] or home_only_empty:
        for name in ("videos", "shorts", "streams"):
            try:
                ids, sel = tab(cid, name)
                res["tabs"][name] = {"selected_tab": sel, "count": None if ids is None else len(ids), "items": ids,
                                     "details": details_for(ids or {})}
            except Exception as e:
                res["tabs"][name] = {"error": repr(e)}
        if home_only_empty and any((t.get("count") or 0) for t in res["tabs"].values()):
            res["removed"] = None
    print(json.dumps(res, ensure_ascii=False))
