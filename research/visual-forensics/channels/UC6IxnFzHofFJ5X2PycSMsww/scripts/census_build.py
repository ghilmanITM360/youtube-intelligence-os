"""Join tab listings + player metadata + catalog + local files into census.csv/json. python3 -I census_build.py <ws>"""
import json, re, sys, csv, hashlib, pathlib, collections

W = pathlib.Path(sys.argv[1]); C = W / "census"
LOCAL_DIRS = [pathlib.Path("/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel"),
              pathlib.Path("/Users/ghilmankhan/workprojects/video data of what if/videos")]
tabs = json.load(open(C / "tab_listings.json"))
cat_ids = set(json.load(open(C / "catalog_ch000004_ids.json")))
cat = json.load(open(C / "catalog_ch000004_snapshots.json"))

# local files: hash once, cache
hcache = C / "local_hashes.json"
hashes = json.load(open(hcache)) if hcache.exists() else {}
local = collections.defaultdict(list)
for d in LOCAL_DIRS:
    for f in sorted(d.glob("*.mp4")):
        m = re.search(r"\[([\w-]{11})\]\.mp4$", f.name) or re.search(r"_Media_([\w-]{11})_\d{3}_", f.name)
        if str(f) not in hashes:
            h = hashlib.sha256()
            with open(f, "rb") as fh:
                for b in iter(lambda: fh.read(1 << 20), b""): h.update(b)
            hashes[str(f)] = dict(sha256=h.hexdigest(), size=f.stat().st_size)
        local[m.group(1) if m else "UNRESOLVED:" + f.name].append(dict(path=str(f), **hashes[str(f)]))
hcache.write_text(json.dumps(hashes, indent=1))

rows = []
listed = {}
for tab, t in tabs["tabs"].items():
    for i in t["items"]: listed.setdefault(i["video_id"], (tab, i))
for vid, (tab, it) in listed.items():
    w = json.load(open(C / "raw" / "watch" / f"{vid}.json"))
    vd = w.get("videoDetails") or {}; mf = (w.get("microformat") or {}).get("playerMicroformatRenderer", {})
    snaps = cat["snapshots"].get(vid, [])
    rows.append(dict(
        video_id=vid, canonical_url=f"https://www.youtube.com/watch?v={vid}" if tab == "videos" else f"https://www.youtube.com/shorts/{vid}",
        title=vd.get("title") or it.get("title"), publish_datetime=mf.get("publishDate"), upload_datetime=mf.get("uploadDate"),
        duration_s=int(vd["lengthSeconds"]) if vd.get("lengthSeconds") else None,
        format_class="SHORT" if tab == "shorts" else "LONG_FORM",
        format_evidence=f"listed on channel /{tab} tab (snapshot {tabs['snapshot_utc']})",
        is_live_content=vd.get("isLiveContent"), category=mf.get("category"),
        views_player=int(vd["viewCount"]) if vd.get("viewCount") else None,
        views_listing_text=it.get("view_text") or ((it.get("meta_parts") or [None])[0]),
        likes="UNAVAILABLE_LOGGED_OUT_PLAYER", comments="UNAVAILABLE_LOGGED_OUT_PLAYER",
        thumbnail_ref=f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        caption_tracks=";".join(f"{c['lang']}:{c['kind'] or 'manual'}" for c in w["captionTracks"]) or "NONE_RETURNED_UNPLAYABLE_PLAYER",
        catalog_registered=vid in cat_ids, catalog_type=snaps[-1]["video_type"] if snaps else None,
        catalog_transcript_rows=cat["transcripts"].get(vid, 0),
        local_files=len(local.get(vid, [])), local_paths=" | ".join(x["path"] for x in local.get(vid, [])),
        local_sha256=" | ".join(x["sha256"] for x in local.get(vid, [])),
        snapshot_utc=w["fetched_utc"], playability=w["playabilityStatus"]))
rows.sort(key=lambda r: r["publish_datetime"] or "")
with open(C / "census.csv", "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
ls = set(listed)
summary = dict(
    snapshot_utc=tabs["snapshot_utc"], channel_id="UC6IxnFzHofFJ5X2PycSMsww", handle="@xkcd_whatif",
    method=tabs["method"] + "; per-video metadata via youtubei/v1/player (logged-out); watch HTML returned HTTP 429",
    long_form=sum(r["format_class"] == "LONG_FORM" for r in rows), shorts=sum(r["format_class"] == "SHORT" for r in rows),
    livestreams=0, livestreams_evidence="/@xkcd_whatif/streams redirected to Home tab (no Live tab rendered); isLiveContent true count=%d" % sum(bool(r["is_live_content"]) for r in rows),
    other_uncertain=0, unique_total=len(rows),
    tabs_exhausted={k: v["exhausted"] for k, v in tabs["tabs"].items()},
    catalog_ids=len(cat_ids), catalog_not_listed_now=sorted(cat_ids - ls), listed_not_in_catalog=sorted(ls - cat_ids),
    catalog_type_disagreements=[r["video_id"] for r in rows if r["catalog_type"] and (r["catalog_type"] == "shorts") != (r["format_class"] == "SHORT")],
    local_ids=sorted(k for k in local if not k.startswith("UNRESOLVED")), local_unresolved=sorted(k for k in local if k.startswith("UNRESOLVED")),
    local_ids_not_listed=sorted(k for k in local if not k.startswith("UNRESOLVED") and k not in ls),
    listed_without_local=sorted(r["video_id"] for r in rows if not r["local_files"]),
    duplicate_local_copies={k: len(v) for k, v in local.items() if len(v) > 1},
    limitations=["likes/comments not returned by logged-out player endpoint", "captions not returned (player UNPLAYABLE bot gate); transcript availability unknown from YouTube",
                 "listing is public-visible uploads at snapshot only; private/unlisted/removed items invisible"])
(C / "census_summary.json").write_text(json.dumps(summary, indent=1))
print(json.dumps({k: (v if not isinstance(v, list) or len(v) < 15 else f"{len(v)} items") for k, v in summary.items()}, indent=1))
