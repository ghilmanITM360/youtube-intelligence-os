"""Capture a channel's public About panel (description, country, joined date, total views, links) verbatim.

Usage: python3 yt_channel_about.py <channel_id> [...]   -> one JSON line per channel on stdout
"""
import json, re, sys, time
from yt_tabs import get

KEY = '"aboutChannelViewModel":{'


def about(cid):
    html = get(f"https://www.youtube.com/channel/{cid}/about")
    rec = {"channel_id": cid, "observed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "source_reference": f"https://www.youtube.com/channel/{cid}/about"}
    i = html.find(KEY)
    if i < 0:
        return {**rec, "error": "NO_ABOUT_VIEW_MODEL"}
    vm, _ = json.JSONDecoder().raw_decode(html, i + len(KEY) - 1)
    return {**rec, "about": {k: vm.get(k) for k in ("description", "country", "joinedDateText", "viewCountText",
                                                    "subscriberCountText", "videoCountText", "canonicalChannelUrl",
                                                    "channelId", "links")}}


if __name__ == "__main__":
    for cid in sys.argv[1:]:
        try:
            print(json.dumps(about(cid), ensure_ascii=False), flush=True)
        except Exception as e:
            print(json.dumps({"channel_id": cid, "error": repr(e)}), flush=True)
        time.sleep(0.4)
