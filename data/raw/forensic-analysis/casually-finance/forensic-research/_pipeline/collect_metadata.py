"""Phase A: public, unauthenticated, zero-spend metadata snapshot for @CasuallyFinance.

Mechanism (same public InnerTube family the YIOS repo scripts yt_tabs.py / yt_video_meta.py use; logic re-implemented here,
repo untouched): channel page -> Videos/Shorts/Streams tab continuation pagination + uploads-playlist (UU...) browse as an
independent completeness cross-check -> per-ID `player` (videoDetails + microformat) and `next` (likes/comments/chapters text).
Raw responses are kept under snapshots/<UTC stamp>/; nothing is overwritten. Bot-check => stop, never work around.
Usage: python3 -B collect_metadata.py <OUT_DIR>
"""
import json, re, sys, time, urllib.request, urllib.error
from pathlib import Path

CHANNEL_ID = "UCrNfRFWnLC3tCy1TnyhVQ7g"
HANDLE = "@CasuallyFinance"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9", "Cookie": "CONSENT=YES+1; SOCS=CAI"}
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20250925.01.00", "hl": "en", "gl": "US"}}


def http(url, body=None):
    h = dict(UA)
    if body is not None:
        h["Content-Type"] = "application/json"
        body = json.dumps(body).encode()
    for attempt in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, data=body, headers=h), timeout=40).read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(10 * (attempt + 1)); continue
            raise
        except (urllib.error.URLError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("RETRIES_EXHAUSTED " + url)


def ytext(o):
    if not o: return None
    return o.get("simpleText") or "".join(r.get("text", "") for r in o.get("runs", [])) or None


def texts(o):
    if isinstance(o, dict):
        if isinstance(o.get("content"), str): yield o["content"]
        for v in o.values(): yield from texts(v)
    elif isinstance(o, list):
        for v in o: yield from texts(v)


def walk(o, out, details, conts):
    """Collect (videoId -> title) plus the listing-card details YouTube rendered, and continuation tokens."""
    if isinstance(o, dict):
        if "videoId" in o and ("lengthText" in o or "viewCountText" in o):
            details.setdefault(o["videoId"], {"views_text": ytext(o.get("viewCountText")), "published_text": ytext(o.get("publishedTimeText")),
                                              "duration_text": ytext(o.get("lengthText"))})
        if "videoId" in o and ("title" in o or "headline" in o) and "thumbnail" in o:
            out.setdefault(o["videoId"], ytext(o.get("title") or o.get("headline")))
        if "shortsLockupViewModel" in o:
            v = o["shortsLockupViewModel"]
            vid = v.get("onTap", {}).get("innertubeCommand", {}).get("reelWatchEndpoint", {}).get("videoId")
            if vid:
                out.setdefault(vid, v.get("overlayMetadata", {}).get("primaryText", {}).get("content"))
                details.setdefault(vid, {"views_text": v.get("overlayMetadata", {}).get("secondaryText", {}).get("content"),
                                         "accessibility_text": v.get("accessibilityText")})
        if "lockupViewModel" in o and o["lockupViewModel"].get("contentType") in (None, "LOCKUP_CONTENT_TYPE_VIDEO"):
            v = o["lockupViewModel"]
            if v.get("contentId"):
                md = v.get("metadata", {}).get("lockupMetadataViewModel", {})
                out.setdefault(v["contentId"], md.get("title", {}).get("content"))
                badge = None
                for t in texts(v.get("contentImage", {})): badge = badge or t
                details.setdefault(v["contentId"], {"metadata_text": list(texts(md.get("metadata", {}))), "duration_text": badge})
        if isinstance(o.get("continuationCommand"), dict) and o["continuationCommand"].get("token"): conts.append(o["continuationCommand"]["token"])
        for v in o.values(): walk(v, out, details, conts)
    elif isinstance(o, list):
        for v in o: walk(v, out, details, conts)


def paginate(first_json, key, ctx, pages_log):
    out, details, conts = {}, {}, []
    walk(first_json, out, details, conts)
    seen, pages = set(), 1
    while conts:
        tok = conts.pop()
        if tok in seen: continue
        seen.add(tok); time.sleep(0.4)
        j = json.loads(http(f"https://www.youtube.com/youtubei/v1/browse?key={key}", {"context": ctx, "continuation": tok}))
        before = len(out)
        walk(j.get("onResponseReceivedActions", []), out, details, conts)
        pages += 1
        pages_log.append({"page": pages, "new_ids": len(out) - before})
    return out, details, pages


def tab(name, key, ctx):
    html = http(f"https://www.youtube.com/channel/{CHANNEL_ID}/{name}")
    data = json.loads(re.search(r"var ytInitialData = (\{.*?\});</script>", html).group(1))
    sel = [t["tabRenderer"]["title"] for t in data.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", [])
           if "tabRenderer" in t and t["tabRenderer"].get("selected")]
    want = {"videos": "videos", "shorts": "shorts", "streams": "live"}[name]
    if not sel or sel[0].lower() != want:
        return {"selected_tab": sel[0] if sel else None, "status": "TAB_ABSENT", "items": {}, "details": {}, "pages": 0, "page_log": []}
    log = []
    out, details, pages = paginate(data, key, ctx, log)
    return {"selected_tab": sel[0], "status": "OK", "items": out, "details": details, "pages": pages, "page_log": log}


def find_all(o, key, acc):
    if isinstance(o, dict):
        if key in o: acc.append(o[key])
        for v in o.values(): find_all(v, key, acc)
    elif isinstance(o, list):
        for v in o: find_all(v, key, acc)
    return acc


def next_extract(vid):
    j = json.loads(http("https://www.youtube.com/youtubei/v1/next?prettyPrint=false", {"context": CTX, "videoId": vid}))
    r = {}
    for f in find_all(j, "factoidRenderer", []):
        lab = ytext(f.get("label")); val = ytext(f.get("value"))
        if lab == "Likes": r["likes_text"] = val; r["likes_accessibility"] = f.get("accessibilityText")
        if lab == "Views": r["views_text_next"] = val
    for p in find_all(j, "engagementPanelSectionListRenderer", []):
        if p.get("panelIdentifier") == "engagement-panel-comments-section":
            ci = p.get("header", {}).get("engagementPanelTitleHeaderRenderer", {}).get("contextualInfo")
            r["comments_text"] = ytext(ci)
    ch = []
    for m in find_all(j, "macroMarkersListItemRenderer", []):
        ch.append({"title": ytext(m.get("title")), "time": ytext(m.get("timeDescription"))})
    r["chapters"] = ch
    vdh = find_all(j, "videoDescriptionHeaderRenderer", [])
    r["publish_date_text"] = ytext(vdh[0].get("publishDate")) if vdh else None
    r["has_comments_panel"] = any(p.get("panelIdentifier") == "engagement-panel-comments-section" for p in find_all(j, "engagementPanelSectionListRenderer", []))
    return r


def main(out_dir):
    out_dir = Path(out_dir)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    snap = out_dir / "01_CHANNEL_METADATA" / "snapshots" / stamp
    snap.mkdir(parents=True, exist_ok=True)
    html = http(f"https://www.youtube.com/{HANDLE}")
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    header = dict(canonical=canon and canon.group(1), og_title=(re.search(r'<meta property="og:title" content="([^"]*)"', html) or [None, None])[1],
                  handle_from_page=(re.search(r'"canonicalBaseUrl":"/(@[^"]+)"', html) or [None, None])[1],
                  header_videos_text=(re.search(r'"content":"([\d,.KM]+) videos?"', html) or [None, None])[1],
                  header_subscribers_text=(re.search(r'"content":"([\d,.KM]+) subscribers"', html) or [None, None])[1],
                  external_id=(re.search(r'"externalId":"(UC[\w-]{22})"', html) or [None, None])[1])
    key = re.search(r'"INNERTUBE_API_KEY":"([^"]+)"', html).group(1)
    ctx = json.loads(re.search(r'"INNERTUBE_CONTEXT":(\{.*?\}),"INNERTUBE_CONTEXT_CLIENT_NAME"', html).group(1))
    header["channel_id_verified"] = header["canonical"] == f"https://www.youtube.com/channel/{CHANNEL_ID}"
    uploads_pl = "UU" + CHANNEL_ID[2:]

    # 1) channel tabs (Videos / Shorts / Live) with continuation pagination
    tabs = {n: tab(n, key, ctx) for n in ("videos", "shorts", "streams")}
    # 2) uploads playlist browse as an independent enumeration
    pl_log = []
    first = json.loads(http(f"https://www.youtube.com/youtubei/v1/browse?key={key}", {"context": ctx, "browseId": "VL" + uploads_pl}))
    pl_items, pl_details, pl_pages = paginate(first, key, ctx, pl_log)
    (snap / "enumeration.json").write_text(json.dumps({"header": header, "uploads_playlist_id": uploads_pl, "tabs": tabs,
                                                       "uploads_playlist": {"items": pl_items, "details": pl_details, "pages": pl_pages, "page_log": pl_log}},
                                                      ensure_ascii=False, indent=1))
    ids = list(dict.fromkeys(list(tabs["videos"]["items"]) + list(tabs["shorts"]["items"]) + list(tabs["streams"]["items"]) + list(pl_items)))
    print("ids", len(ids), {k: len(v["items"]) for k, v in tabs.items()}, "playlist", len(pl_items), flush=True)

    # 3) per-video player + next
    praw, nraw = snap / "player_raw.jsonl", snap / "next_extract.jsonl"
    done_p = {json.loads(l)["video_id"] for l in praw.open()} if praw.exists() else set()
    done_n = {json.loads(l)["video_id"] for l in nraw.open()} if nraw.exists() else set()
    with praw.open("a") as fp, nraw.open("a") as fn:
        for vid in ids:
            if vid not in done_p:
                rec = {"video_id": vid, "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "source_method": "youtubei/v1/player (public, unauthenticated)"}
                try:
                    p = json.loads(http("https://www.youtube.com/youtubei/v1/player?prettyPrint=false", {"context": CTX, "videoId": vid}))
                    ps = p.get("playabilityStatus") or {}
                    if ps.get("status") == "LOGIN_REQUIRED" and not p.get("videoDetails") and "bot" in (ps.get("reason") or ""):
                        print("BOT_CHECK at", vid); sys.exit(3)
                    mf = dict((p.get("microformat") or {}).get("playerMicroformatRenderer") or {}); mf.pop("availableCountries", None)
                    caps = ((p.get("captions") or {}).get("playerCaptionsTracklistRenderer") or {}).get("captionTracks")
                    rec.update(playability_status=ps.get("status"), playability_reason=ps.get("reason"), video_details=p.get("videoDetails"),
                               microformat=mf or None, caption_tracks=[{"lang": c.get("languageCode"), "kind": c.get("kind"), "name": ytext(c.get("name"))} for c in caps] if caps else None,
                               captions_block_present="captions" in p)
                except Exception as e:
                    rec["error"] = repr(e)
                fp.write(json.dumps(rec, ensure_ascii=False) + "\n"); fp.flush(); time.sleep(0.3)
            if vid not in done_n:
                rec = {"video_id": vid, "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "source_method": "youtubei/v1/next (public, unauthenticated)"}
                try: rec.update(next_extract(vid))
                except Exception as e: rec["error"] = repr(e)
                fn.write(json.dumps(rec, ensure_ascii=False) + "\n"); fn.flush(); time.sleep(0.3)
    print("SNAPSHOT", snap)


if __name__ == "__main__":
    main(sys.argv[1])
