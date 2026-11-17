"""Fetch public watch-page player metadata for each listed video ID. Saves trimmed raw JSON per ID.
Usage: python3 -I census_watch.py <census_dir>"""
import json, re, sys, time, urllib.request, pathlib

D = pathlib.Path(sys.argv[1]); OUT = D / "raw" / "watch"; OUT.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
tabs = json.load(open(D / "tab_listings.json"))["tabs"]
ids = [i["video_id"] for t in tabs.values() for i in t["items"]]
for vid in dict.fromkeys(ids):
    f = OUT / f"{vid}.json"
    if f.exists(): continue
    body = json.dumps({"context": {"client": {"clientName": "WEB", "clientVersion": "2.20261030.02.00", "hl": "en", "gl": "US"}},
                       "videoId": vid}).encode()
    req = urllib.request.Request("https://www.youtube.com/youtubei/v1/player?prettyPrint=false", data=body,
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    pr = json.loads(urllib.request.urlopen(req, timeout=30).read())
    likes = comments = []; html = ""
    keep = dict(fetched_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), url=f"https://www.youtube.com/watch?v={vid}", method="youtubei/v1/player WEB (public, logged-out)",
                videoDetails=pr.get("videoDetails"), microformat=pr.get("microformat"),
                playabilityStatus=pr.get("playabilityStatus", {}).get("status"),
                captionTracks=[dict(lang=c.get("languageCode"), kind=c.get("kind"), name=(c.get("name") or {}).get("simpleText"))
                               for c in pr.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", [])],
                like_count_raw=likes[0] if likes else None, comment_count_raw=comments[0] if comments else None,
                canonical_shorts_link=None)
    f.write_text(json.dumps(keep, indent=1)); print(vid, keep["playabilityStatus"], (keep["microformat"] or {}).get("playerMicroformatRenderer", {}).get("publishDate"))
    time.sleep(1.2)
