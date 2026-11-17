"""Public tab-presence probe (no auth, no pagination, no media): which of Videos/Shorts/Live tabs each channel exposes."""
import sys, json, re, hashlib, datetime, concurrent.futures as cf
import urllib.request
class F:
    HDR = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36", "Accept-Language": "en-US,en;q=0.9", "Cookie": "CONSENT=YES+1; SOCS=CAI"}
    @staticmethod
    def get(url):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=F.HDR), timeout=30) as r:
                return r.status, r.geturl(), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e: return e.code, url, ""
        except Exception as e: return -1, url, str(e)
    @staticmethod
    def lockups(tr, n): return [0] * json.dumps(tr).count('"lockupViewModel"')
def probe(cid):
    st, fu, html = F.get(f"https://www.youtube.com/channel/{cid}/streams")
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    tabs, live_items = [], 0
    if m:
        d = json.loads(m.group(1))
        for t in d.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", []):
            tr = t.get("tabRenderer")
            if tr: tabs.append(tr.get("title"))
            if tr and tr.get("selected") and tr.get("title") == "Live":
                live_items = len(F.lockups(tr, 60))
    return dict(channel_id=cid, http=st, final_url=fu, tabs=tabs, live_items_first_page=live_items,
                page_sha256=hashlib.sha256(html.encode()).hexdigest(),
                observed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"))
ids = [l.strip() for l in open(sys.argv[2]) if l.strip()]
with cf.ThreadPoolExecutor(4) as ex, open(sys.argv[3], "w") as o:
    for r in ex.map(probe, ids): o.write(json.dumps(r) + "\n"); print(r["channel_id"], r["http"], r["tabs"], r["live_items_first_page"])
