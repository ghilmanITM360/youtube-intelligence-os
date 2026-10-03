"""Harvest channel candidates from public YouTube search (channel-filtered and video results).

Usage: python3 yt_search_discover.py <queries.txt> <out.jsonl>
Each output row: query, result_kind (channel|video), channel_id, channel_name, plus the visible
subscriber/video-count or video title/view text exactly as YouTube rendered it. Discovery only —
relevance and identity are verified afterwards with yt_tabs.py and manual review.
"""
import json, re, sys, time, urllib.parse
from yt_tabs import get

FILTERS = {"channel": "EgIQAg%3D%3D", "video": "EgIQAQ%3D%3D"}


def text(o):
    return (o or {}).get("simpleText") or "".join(r.get("text", "") for r in (o or {}).get("runs", []))


def walk(o, hits):
    if isinstance(o, dict):
        if "channelRenderer" in o:
            c = o["channelRenderer"]
            hits.append({"result_kind": "channel", "channel_id": c.get("channelId"), "channel_name": text(c.get("title")),
                         "visible_subscribers": text(c.get("videoCountText")) or text(c.get("subscriberCountText")),
                         "visible_handle_or_count": text(c.get("subscriberCountText"))})
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            owner = (v.get("ownerText") or {}).get("runs", [{}])[0]
            hits.append({"result_kind": "video", "channel_id": owner.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId"),
                         "channel_name": owner.get("text"), "video_id": v.get("videoId"), "video_title": text(v.get("title")),
                         "visible_views": text(v.get("viewCountText")), "visible_published": text(v.get("publishedTimeText"))})
        for x in o.values():
            walk(x, hits)
    elif isinstance(o, list):
        for x in o:
            walk(x, hits)


def main(qfile, out):
    with open(out, "a") as f:
        for q in [l.strip() for l in open(qfile) if l.strip() and not l.startswith("#")]:
            for kind, sp in FILTERS.items():
                html = get(f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}&sp={sp}")
                m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
                hits = []
                if m:
                    walk(json.loads(m.group(1)), hits)
                for h in hits:
                    f.write(json.dumps({"query": q, "search_filter": kind, "observed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), **h}, ensure_ascii=False) + "\n")
                time.sleep(0.6)


if __name__ == "__main__":
    main(*sys.argv[1:3])
