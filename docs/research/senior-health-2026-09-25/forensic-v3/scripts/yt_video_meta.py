"""Collect public per-video metadata (zero spend) for every Video ID a yt_tabs.py snapshot enumerated.

Usage: python3 yt_video_meta.py <live-snapshot.json> <out.jsonl> [delay-seconds]

Source: YouTube's public InnerTube `player` endpoint (the same JSON the watch page embeds as
ytInitialPlayerResponse). `videoDetails` and `microformat.playerMicroformatRenderer` are kept verbatim
(minus the per-country availability list) so derived fields can be recomputed later. No stream,
caption or login-gated data is requested. Resumable: IDs already present in <out.jsonl> are skipped.
If YouTube answers with its "confirm you're not a bot" check, the script records nothing for that ID and exits
with status 3 so the caller backs off — the check is respected, never worked around.
"""
import json, sys, time, urllib.request, urllib.error
from pathlib import Path

HDR = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
       "Accept-Language": "en-US,en;q=0.9", "Content-Type": "application/json"}
CTX = {"client": {"clientName": "WEB", "clientVersion": "2.20250925.01.00", "hl": "en", "gl": "US"}}
URL = "https://www.youtube.com/youtubei/v1/player?prettyPrint=false"


def fetch(vid):
    body = json.dumps({"context": CTX, "videoId": vid}).encode()
    for attempt in range(4):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(URL, data=body, headers=HDR), timeout=30).read())
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(10 * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("RETRIES_EXHAUSTED")


BOT_CHECK = 3


def main(snapshot, out, delay="0.25"):
    snap = json.loads(Path(snapshot).read_text())
    tab_of = {}
    for name, t in (snap.get("tabs") or {}).items():
        for vid in (t.get("items") or {}):
            tab_of.setdefault(vid, name)
    out = Path(out)
    done = {json.loads(l)["video_id"] for l in out.open()} if out.exists() else set()
    with out.open("a") as f:
        for vid, tab in tab_of.items():
            if vid in done:
                continue
            rec = {"video_id": vid, "enumerated_channel_id": snap["channel_id"], "enumerated_tab": tab,
                   "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "source_method": "youtubei/v1/player (public, unauthenticated)", "source_reference": URL}
            try:
                p = fetch(vid)
                ps = p.get("playabilityStatus") or {}
                if ps.get("status") == "LOGIN_REQUIRED" and not p.get("videoDetails") and "bot" in (ps.get("reason") or ""):
                    sys.exit(BOT_CHECK)
                mf = dict((p.get("microformat") or {}).get("playerMicroformatRenderer") or {})
                mf.pop("availableCountries", None)
                rec.update(playability_status=(p.get("playabilityStatus") or {}).get("status"),
                           playability_reason=(p.get("playabilityStatus") or {}).get("reason"),
                           video_details=p.get("videoDetails"), microformat=mf or None)
            except Exception as e:  # recorded, never silently dropped
                rec["error"] = repr(e)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            time.sleep(float(delay))


if __name__ == "__main__":
    main(*sys.argv[1:4])
