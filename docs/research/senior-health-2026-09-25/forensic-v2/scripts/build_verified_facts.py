"""Re-derive verified per-video / per-channel facts for the Senior Health cohort
directly from the canonical registry DB (+ raw Apify channel metadata).

Read-only against canonical data. Output: forensic-v2/VERIFIED-FACTS.json
Every field carries its source; missing values are the literal string UNKNOWN.
"""
import json, sqlite3, statistics, re, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parents[1] / "VERIFIED-FACTS.json"
DB = ROOT / "data/catalog/youtube_channel_registry.db"
AS_OF = "2026-09-25"

CHANNELS = {
    "UCAYG0fzUyxv6OevH88qA45w": "Senior Health Hub",
    "UCMJxAeBJ0d1JC937de1eZ0Q": "Dr. Okoro",
    "UC356D-NzdnznBOftTpYoBLw": "Dr. Ares Senior",
    "UCXZi5JVeuTluazF-fYqQgNA": "Dr. Aliza Wright | Advice",
    "UCQcBYZxFW7YwNMU8-DsT3Uw": "Dr. Elias Senior Health",
    "UCFuGMi0idGeyXl6wYK9hg7Q": "Doctor Thomas",
}
RAW_CHANNEL_FILES = [
    "data/raw/channel-data/DS-000027/apify/dqMkTSwYwRir4QfUM/youtube_actor_raw.json",
    "data/raw/competitors/DS-000028/apify/uLT4StERHwuiLthti/raw/dataset.json",
    "data/raw/competitors/DS-000029/apify/WqJIbwUkgkHDHxdaI/raw/dataset.json",
    "data/raw/competitors/DS-000030/apify/ai1C2ifFj7SPFkINt/raw/dataset.json",
]
SNAPSHOT_MANIFESTS = glob.glob(str(ROOT / "data/manifests/DS-0000*-thumbnail-snapshot-*.json"))


def raw_channel_meta():
    meta, thumbs = {}, {}
    for f in RAW_CHANNEL_FILES:
        for r in json.load(open(ROOT / f)):
            cid = r.get("channelId")
            thumbs[r["id"]] = (r.get("thumbnailUrl"), f)
            meta.setdefault(cid, {
                "channel_joined_date": r.get("channelJoinedDate") or "UNKNOWN",
                "subscribers_at_scrape": r.get("numberOfSubscribers") or "UNKNOWN",
                "channel_total_videos_at_scrape": r.get("channelTotalVideos") or "UNKNOWN",
                "channel_total_views_at_scrape": r.get("channelTotalViews") or "UNKNOWN",
                "source": f,
            })
    return meta, thumbs


def snapshot_paths():
    out = {}
    for m in SNAPSHOT_MANIFESTS:
        d = json.load(open(m))
        for s in d.get("snapshots", []):
            vid = re.search(r"/vi/([^/]+)/", s.get("final_url") or s.get("original_registered_url") or "")
            if vid and s.get("local_path"):
                rel = s["local_path"].split("youtube-intelligence-os/")[-1]
                out[vid.group(1)] = {"local_path": rel, "manifest": str(Path(m).relative_to(ROOT)),
                                     "exists": (ROOT / rel).exists()}
    return out


def main():
    con = sqlite3.connect(DB)
    meta, raw_thumbs = raw_channel_meta()
    snaps = snapshot_paths()
    q = """select v.youtube_video_id, v.canonical_channel_id, v.title, v.published_at, v.duration_seconds,
                  v.video_type, v.views, v.likes, v.comments, v.thumbnail_url,
                  t.evidence_locator, t.word_count, t.is_placeholder, t.unavailable_reason, t.dataset_id
           from videos v left join transcripts t using(youtube_video_id)
           where v.canonical_channel_id in (%s)""" % ",".join("?" * len(CHANNELS))
    rows = con.execute(q, list(CHANNELS)).fetchall()
    videos, by_ch = [], {}
    for (vid, cid, title, pub, dur, vtype, views, likes, comments, thumb, loc, wc, ph, unav, ds) in rows:
        if thumb:
            tsrc, turl = "REGISTRY_DB.videos.thumbnail_url", thumb
        elif vid in raw_thumbs and raw_thumbs[vid][0]:
            tsrc, turl = "RAW_APIFY.thumbnailUrl:" + raw_thumbs[vid][1], raw_thumbs[vid][0]
        else:
            tsrc, turl = "UNKNOWN", "UNKNOWN"
        has_tx = bool(loc) and not ph and (wc or 0) > 0
        videos.append({
            "video_id": vid, "channel_id": cid, "channel": CHANNELS[cid], "title": title,
            "upload_date": (pub or "UNKNOWN")[:10], "published_at_raw": pub or "UNKNOWN",
            "duration_seconds": dur if dur is not None else "UNKNOWN",
            "video_type": vtype or "UNKNOWN", "views": views if views is not None else "UNKNOWN",
            "likes": likes, "comments": comments, "dataset_id": ds,
            "transcript_path": loc if has_tx else "UNKNOWN",
            "transcript_word_count": wc if has_tx else 0,
            "transcript_unavailable_reason": None if has_tx else (unav or "NO_TRANSCRIPT_ROW"),
            "thumbnail_url": turl, "thumbnail_url_source": tsrc,
            "thumbnail_repository_snapshot": snaps.get(vid, {}).get("local_path", "NONE"),
            "fact_source": "data/catalog/youtube_channel_registry.db (videos, transcripts)",
        })
        by_ch.setdefault(cid, []).append(videos[-1])

    channels = {}
    for cid, vs in by_ch.items():
        vs.sort(key=lambda v: v["published_at_raw"])
        views = [v["views"] for v in vs if isinstance(v["views"], int)]
        med = statistics.median(views)
        recent10 = statistics.median([v["views"] for v in vs[-10:] if isinstance(v["views"], int)])
        for v in vs:
            v["channel_median_views"] = med
            v["outlier_multiple_vs_channel_median"] = round(v["views"] / med, 3) if med else "UNKNOWN"
        top = max(vs, key=lambda v: v["views"])
        total = sum(views)
        channels[cid] = {
            "channel": CHANNELS[cid], "videos_in_repository": len(vs),
            "earliest_available_upload": vs[0]["upload_date"], "earliest_video_id": vs[0]["video_id"],
            "latest_available_upload": vs[-1]["upload_date"],
            "median_views_all": med, "median_views_recent10_by_upload": recent10,
            "total_views_in_repository": total,
            "top_video": {"video_id": top["video_id"], "title": top["title"], "views": top["views"],
                           "upload_date": top["upload_date"], "share_of_channel_views": round(top["views"] / total, 4)},
            "raw_channel_metadata": meta.get(cid, {"channel_joined_date": "UNKNOWN", "subscribers_at_scrape": "UNKNOWN",
                                                   "source": "no raw Apify channel record in repository"}),
            "transcripts_available": sum(1 for v in vs if v["transcript_path"] != "UNKNOWN"),
            "thumbnail_urls_known": sum(1 for v in vs if v["thumbnail_url"] != "UNKNOWN"),
            "thumbnail_repository_snapshots": sum(1 for v in vs if v["thumbnail_repository_snapshot"] != "NONE"),
        }
    json.dump({"as_of": AS_OF, "source_db": str(DB.relative_to(ROOT)), "channels": channels,
               "videos": sorted(videos, key=lambda v: (v["channel"], v["published_at_raw"]))},
              open(OUT, "w"), indent=1)
    print(f"{len(videos)} videos, {len(channels)} channels -> {OUT}")


if __name__ == "__main__":
    main()
