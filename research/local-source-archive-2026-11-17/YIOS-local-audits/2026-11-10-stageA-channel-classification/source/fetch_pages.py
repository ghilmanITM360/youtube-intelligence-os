"""Stage A identity/sample fetch: one public /videos and one /shorts page per normalized input.
No media, no auth, no pagination. Writes pages.jsonl (extracted fields + page SHA-256)."""
import hashlib, json, re, sys, time, urllib.request, datetime, pathlib

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
HDR = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9", "Cookie": "CONSENT=YES+1; SOCS=CAI"}
out = pathlib.Path(sys.argv[2])
done = set()
if out.exists():
    done = {json.loads(l)["input_url"] for l in out.read_text().splitlines()}


def get(url):
    req = urllib.request.Request(url, headers=HDR)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.geturl(), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:  # network error
        return -1, url, str(e)


def texts(o):
    """All 'content' strings under o (viewModel text)."""
    acc = []
    def w(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "content" and isinstance(v, str):
                    acc.append(v)
                else:
                    w(v)
        elif isinstance(x, list):
            for v in x:
                w(v)
    w(o)
    return acc


def lockups(d, limit):
    items = []
    def w(x):
        if len(items) >= limit:
            return
        if isinstance(x, dict):
            if "lockupViewModel" in x:
                lv = x["lockupViewModel"]
                md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
                items.append({"video_id": lv.get("contentId"),
                              "title": md.get("title", {}).get("content"),
                              "meta": [t for t in texts(md.get("metadata", {})) if t.strip()][:4],
                              "overlay": [t for t in texts(lv.get("contentImage", {})) if t.strip()][:2]})
                return
            if "shortsLockupViewModel" in x:
                sv = x["shortsLockupViewModel"]
                vid = sv.get("onTap", {}).get("innertubeCommand", {}).get("reelWatchEndpoint", {}).get("videoId")
                items.append({"video_id": vid,
                              "title": sv.get("overlayMetadata", {}).get("primaryText", {}).get("content"),
                              "meta": [sv.get("overlayMetadata", {}).get("secondaryText", {}).get("content")]})
                return
            for v in x.values():
                w(v)
        elif isinstance(x, list):
            for v in x:
                w(v)
    w(d)
    return items


def parse(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m:
        return None
    d = json.loads(m.group(1))
    cm = d.get("metadata", {}).get("channelMetadataRenderer", {})
    hdr = d.get("header", {}).get("pageHeaderRenderer", {})
    hdr_text = [t for t in texts(hdr.get("content", {}).get("pageHeaderViewModel", {}).get("metadata", {})) if t.strip()]
    alerts = [t for t in texts(d.get("alerts", [])) if t.strip()] + re.findall(r'"alertRenderer".{0,400}?"text":"([^"]+)"', html)[:2]
    return d, {"channel_id": cm.get("externalId"), "title": cm.get("title"), "description": (cm.get("description") or "")[:600],
               "vanity_url": cm.get("vanityChannelUrl"), "country": None, "header_meta": hdr_text[:6], "alerts": alerts[:3],
               "family_safe": cm.get("isFamilySafe")}


for url in pathlib.Path(sys.argv[1]).read_text().split():
    if url in done:
        continue
    rec = {"input_url": url, "observed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "access_path": "PUBLIC_HTTP_PAGE_FETCH (no login, no cookies beyond consent)"}
    for tab, limit in (("videos", 8), ("shorts", 4)):
        st, final, html = get(url.rstrip("/") + "/" + tab)
        rec[f"{tab}_http"] = st
        rec[f"{tab}_final_url"] = final
        rec[f"{tab}_page_sha256"] = hashlib.sha256(html.encode()).hexdigest() if html else None
        p = parse(html) if st == 200 else None
        if p:
            d, meta = p
            if tab == "videos" or not rec.get("channel_id"):
                rec.update(meta)
            elif meta["channel_id"] != rec.get("channel_id"):
                rec["shorts_channel_id_conflict"] = meta["channel_id"]
            rec[f"{tab}_sample"] = lockups(d, limit)
        time.sleep(1.2)
    with out.open("a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(url, rec.get("channel_id"), len(rec.get("videos_sample", [])), len(rec.get("shorts_sample", [])), flush=True)
