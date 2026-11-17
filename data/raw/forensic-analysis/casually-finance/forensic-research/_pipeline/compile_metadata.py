"""Phase A/B (part 2): compile the dated metadata snapshot into catalog deliverables and reconcile local files to the 18 requested IDs.
Usage: python3 -B compile_metadata.py <OUT_DIR> [snapshot_stamp]
"""
import csv, glob, json, re, statistics, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

SELECTED = [  # (id, user_supplied_title, user_class)
    ("roe3SgezmmU", "The Stock Market Is Being Used as a Dumping Ground", "LONG"), ("Uumnx2Fo6cE", "The New American Housing Crisis Has Landed", "LONG"),
    ("xtqbRt94TTw", "To Save the Economy... We’re About to Break It", "LONG"), ("o3FQcd91MIs", "Why The Dumbest Investors Win (it's not why you think)", "LONG"),
    ("dlBhLhn8lL0", "MicroStrategy: The Crypto Scam Hiding in Plain Sight", "LONG"), ("kwMHrTFCWUE", "Every Type of Investor Explained in 6 Minutes", "LONG"),
    ("DgbHW0IqHrI", "America Is Walking Into Something It Can't Stop", "LONG"), ("5umJ63d3rzQ", "Brace For Impact.", "LONG"),
    ("0ll9rEtoRrs", "The World's Safest Market Is Breaking", "LONG"), ("-X6YzlY_8tM", "The SpaceX IPO... It's Worse Than You Think", "LONG"),
    ("2EZzwupIa80", "Nothing Forces the Government to Fix The $40 Trillion Debt", "SHORT"), ("YGC3ao005as", "We're Fighting A Battle Against the Market", "SHORT"),
    ("PxgCsLSf-w4", "Somebody Is Quietly Repricing America", "SHORT"), ("6S3PzAUFnXQ", "America's Debt Hasn't Broken... Yet", "SHORT"),
    ("turJ6VMfUjI", "Why You (Mathematically) Need Inflation", "SHORT"), ("Qof71Ef-3EU", "The Cheap Money Era Is Coming to an End", "SHORT"),
    ("rSa2aziEsAI", "Why Japan's Economy Is Awful", "SHORT"), ("JsK53moCyZA", "The SpaceX IPO Nobody Can (Actually) Explain...", "SHORT"),
]
TOPICS = [  # DERIVED_HEURISTIC keyword rules over title+tags+description (first match wins, ordered by specificity)
    ("SPACEX_IPO", r"spacex|ipo\b|going public|public offering"), ("CRYPTO", r"bitcoin|crypto|microstrategy|stablecoin|ethereum"),
    ("HOUSING_REAL_ESTATE", r"housing|mortgage|real estate|home price|rent\b"), ("NATIONAL_DEBT_FISCAL", r"national debt|\bdebt\b|deficit|treasur|bond market|fiscal"),
    ("INFLATION_RATES_FED", r"inflation|interest rate|the fed\b|federal reserve|cheap money|rate cut"), ("JAPAN_GLOBAL_MACRO", r"japan|china|europe|yen"),
    ("AI_TECH_BUBBLE", r"\bai\b|nvidia|openai|tech bubble|bubble"), ("INVESTING_EDUCATION", r"investor|investing|index fund|etf|retire|401k|dumbest"),
    ("STOCK_MARKET_STRUCTURE", r"stock market|market crash|sell.?off|vanguard|blackrock|passive"), ("ECONOMY_GENERAL", r"economy|recession|jobs|tariff"),
]
SPONSOR_STRONG_RX = re.compile(r"(sponsor|#ad\b|paid promotion|paid partnership|thank you to .{0,40} for|brought to you|#\w*partner\b)", re.I)
PROMO_RX = re.compile(r"(use code|promo code|code \"?\w+\"? |free for \d+ days|free trial|\d+% off|subscribe for|book a meeting|try \w+ (inside|for)|sign up|get \d+ month)", re.I)
AFFILIATE_RX = re.compile(r"affiliate", re.I)
TS_RX = re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+)$", re.M)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower().replace("’", "'"))


def dget(o, *ks):
    for k in ks:
        o = (o or {}).get(k) if isinstance(o, dict) else None
    return o


def main(out, stamp=None):
    out = Path(out)
    snaps = sorted(glob.glob(str(out / "01_CHANNEL_METADATA/snapshots/*/player_raw.jsonl")))
    snapdir = Path(snaps[-1]).parent if not stamp else out / "01_CHANNEL_METADATA/snapshots" / stamp
    enum = json.load(open(snapdir / "enumeration.json"))
    player = {r["video_id"]: r for r in map(json.loads, open(snapdir / "player_raw.jsonl"))}
    nxt = {r["video_id"]: r for r in map(json.loads, open(snapdir / "next_extract.jsonl"))}
    tab_of = {}
    for t in ("videos", "shorts", "streams"):
        for vid in enum["tabs"][t]["items"]: tab_of.setdefault(vid, t)
    rows = []
    for vid, p in player.items():
        vd, mf, n = p.get("video_details") or {}, p.get("microformat") or {}, nxt.get(vid, {})
        collected = datetime.strptime(p["collected_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        pub = mf.get("publishDate") or mf.get("uploadDate")
        pub_dt = datetime.fromisoformat(pub) if pub else None
        age = (collected - pub_dt).total_seconds() / 86400 if pub_dt else None
        views = int(vd.get("viewCount") or mf.get("viewCount") or 0) if (vd.get("viewCount") or mf.get("viewCount")) else None
        desc = vd.get("shortDescription") or ""
        dur = int(vd.get("lengthSeconds") or mf.get("lengthSeconds") or 0) or None
        tab = tab_of.get(vid)
        cls = {"videos": "LONG_FORM", "shorts": "SHORT", "streams": "LIVE"}.get(tab, "UNKNOWN")
        ev = [f"channel_tab={tab}", f"isShortsEligible={mf.get('isShortsEligible')}", f"isLiveContent={vd.get('isLiveContent')}", f"duration={dur}s"]
        if cls == "SHORT" and mf.get("isShortsEligible") is False: ev.append("CONFLICT:tab=shorts_but_isShortsEligible=false")
        if cls == "LONG_FORM" and mf.get("isShortsEligible") is True: ev.append("CONFLICT:tab=videos_but_isShortsEligible=true")
        chapters = n.get("chapters") or [{"title": m.group(2).strip(), "time": m.group(1)} for m in TS_RX.finditer(desc)]
        head = "\n".join(desc.split("\n")[:4])  # sponsor/promo text sits in the first lines of the description
        sp = [m.group(0) for m in SPONSOR_STRONG_RX.finditer(desc)]
        promo = [m.group(0) for m in PROMO_RX.finditer(head)] if re.search(r"https?://", head) else []
        sponsor_signal = "STRONG_SPONSOR_TEXT" if sp else "PROMO_LINK_IN_DESCRIPTION_HEAD" if promo else "NONE"
        doms = sorted({urlparse(u).netloc for u in re.findall(r"https?://[^\s)]+", desc)})
        hay = (vd.get("title") or "").lower()  # title only: the 8 tags are channel-wide boilerplate and descriptions carry sponsor copy
        topic = next((t for t, rx in TOPICS if re.search(rx, hay)), "UNCLASSIFIED")
        thumbs = [t["url"] for t in (dget(vd, "thumbnail", "thumbnails") or [])] + [t["url"] for t in (dget(mf, "thumbnail", "thumbnails") or [])]
        likes_exact = mf.get("likeCount")
        rows.append(dict(
            video_id=vid, watch_url=f"https://www.youtube.com/watch?v={vid}" if cls != "SHORT" else f"https://www.youtube.com/shorts/{vid}",
            channel_id=vd.get("channelId"), channel_name=vd.get("author"), channel_handle="@CasuallyFinance", title=vd.get("title"), description=desc,
            published_at=pub, upload_date=mf.get("uploadDate"), duration_sec=dur, width_height="NOT_EXPOSED_BY_PUBLIC_ENDPOINT(player status UNPLAYABLE; no streamingData)",
            format_class=cls, format_classification_evidence="; ".join(ev), views=views, likes=int(likes_exact) if likes_exact else None,
            likes_text_rounded=n.get("likes_text"), comments_text_rounded=n.get("comments_text"),
            comments_availability=("COUNT_PRESENT" if n.get("comments_text") else "PANEL_PRESENT_NO_COUNT" if n.get("has_comments_panel") else "NO_PANEL_(DISABLED_OR_UNKNOWN)"),
            thumbnail_urls=" | ".join(dict.fromkeys(thumbs)), tags=" | ".join(vd.get("keywords") or []), category=mf.get("category"), language="NOT_EXPOSED_BY_PUBLIC_ENDPOINT",
            caption_availability="NOT_EXPOSED(no caption tracklist returned; player UNPLAYABLE)" if not p.get("captions_block_present") else json.dumps(p.get("caption_tracks")),
            sponsor_signal_in_description=sponsor_signal, sponsor_match_text=" | ".join((sp + promo)[:3]), affiliate_boilerplate_mentioned=bool(AFFILIATE_RX.search(desc)), description_link_domains=" | ".join(doms),
            chapters_count=len(chapters), chapters=json.dumps(chapters, ensure_ascii=False) if chapters else "", topic_derived_heuristic=topic,
            is_live_content=vd.get("isLiveContent"), is_family_safe=mf.get("isFamilySafe"), is_unlisted=mf.get("isUnlisted"),
            age_days_at_collection=round(age, 3) if age is not None else None, views_per_day=round(views / max(age, 1.0), 1) if views is not None and age is not None else None,
            collected_at=p["collected_at"], metadata_source="youtubei/v1/player+next (public, unauthenticated) via collect_metadata.py", snapshot=snapdir.name))
    # within-format percentiles (views and views/day) -- descriptive only
    for cls in ("LONG_FORM", "SHORT", "LIVE"):
        g = [r for r in rows if r["format_class"] == cls and r["views"] is not None]
        if not g: continue
        vs = sorted(r["views"] for r in g); vpd = sorted(r["views_per_day"] for r in g)
        for r in g:
            r["views_percentile_in_format"] = round(100 * sum(v <= r["views"] for v in vs) / len(vs), 1)
            r["vpd_percentile_in_format"] = round(100 * sum(v <= r["views_per_day"] for v in vpd) / len(vpd), 1)
    rows.sort(key=lambda r: r["published_at"] or "", reverse=True)
    cols = list(rows[0].keys())
    for r in rows:
        for k in r:
            if k not in cols: cols.append(k)
    with open(out / "01_CHANNEL_METADATA/all-videos-metadata.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    by = {r["video_id"]: r for r in rows}

    # selected manifest (metadata only)
    sel_rows = []
    for vid, ut, uc in SELECTED:
        r = by.get(vid)
        sel_rows.append(dict(video_id=vid, user_supplied_title=ut, user_supplied_class=uc, in_public_catalog=bool(r), public_title=r and r["title"],
                             title_match_exact_normalized=bool(r) and norm(r["title"]) == norm(ut), format_class_public=r and r["format_class"],
                             class_agrees_with_user=bool(r) and ((uc == "LONG" and r["format_class"] == "LONG_FORM") or (uc == "SHORT" and r["format_class"] == "SHORT")),
                             published_at=r and r["published_at"], duration_sec_public=r and r["duration_sec"], views=r and r["views"], likes=r and r["likes"],
                             views_per_day=r and r["views_per_day"], views_percentile_in_format=r and r.get("views_percentile_in_format"),
                             vpd_percentile_in_format=r and r.get("vpd_percentile_in_format"), topic_derived_heuristic=r and r["topic_derived_heuristic"],
                             sponsor_signal=r and r["sponsor_signal_in_description"], collected_at=r and r["collected_at"]))
    with open(out / "01_CHANNEL_METADATA/selected-18-video-manifest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sel_rows[0].keys())); w.writeheader(); w.writerows(sel_rows)

    # coverage / completeness
    tabs_union = set().union(*[set(enum["tabs"][t]["items"]) for t in enum["tabs"]])
    pl = set(enum["uploads_playlist"]["items"])
    cnt = lambda c: sum(r["format_class"] == c for r in rows)
    pub_dates = [r["published_at"] for r in rows if r["published_at"]]
    cov = dict(
        generated_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), snapshot=snapdir.name, channel_id=CHANNEL if (CHANNEL := "UCrNfRFWnLC3tCy1TnyhVQ7g") else None,
        channel_id_verified_against_live_canonical_link=enum["header"]["channel_id_verified"], handle="@CasuallyFinance",
        enumeration=dict(videos_tab=len(enum["tabs"]["videos"]["items"]), shorts_tab=len(enum["tabs"]["shorts"]["items"]), live_tab=len(enum["tabs"]["streams"]["items"]),
                         tabs_union=len(tabs_union), uploads_playlist_UU=len(pl), in_tabs_not_playlist=sorted(tabs_union - pl), in_playlist_not_tabs=sorted(pl - tabs_union),
                         tab_pages={t: enum["tabs"][t]["pages"] for t in enum["tabs"]}, playlist_pages=enum["uploads_playlist"]["pages"]),
        unique_video_ids=len(rows), duplicates_removed=len(set(tabs_union | pl)) - len(rows), by_format=dict(LONG_FORM=cnt("LONG_FORM"), SHORT=cnt("SHORT"), LIVE=cnt("LIVE"), UNKNOWN=cnt("UNKNOWN")),
        player_records=len(player), player_errors=sum("error" in p for p in player.values()), next_records=len(nxt), next_errors=sum("error" in n for n in nxt.values()),
        field_coverage={k: sum(1 for r in rows if r.get(k) not in (None, "")) for k in ("title", "description", "published_at", "duration_sec", "views", "likes", "likes_text_rounded", "comments_text_rounded", "thumbnail_urls", "tags", "category", "chapters")},
        oldest_published=min(pub_dates) if pub_dates else None, newest_published=max(pub_dates) if pub_dates else None,
        classification_conflicts=[r["video_id"] for r in rows if "CONFLICT" in r["format_classification_evidence"]],
        header_reported_video_count_text=enum["header"].get("header_videos_text"), header_reported_subscribers_text=enum["header"].get("header_subscribers_text"),
        not_exposed_by_public_mechanism=["impressions", "CTR", "retention", "revenue", "traffic sources", "video width/height (no streamingData; player UNPLAYABLE)", "caption tracks", "language", "exact comment count (rounded text only)"],
        unresolved_gaps=["Third-party 'video_count=67' in Aug-2026 summary is NOT used; completeness is measured from accessible IDs only.",
                         "Videos not listed publicly (unlisted/private/members) are by definition not enumerable here.",
                         "An empty snapshots/20261011T182635Z folder is a crashed first run (continuation-token bug fixed); it contains no data."],
        note="Public metrics are a point-in-time snapshot; compare future snapshots rather than overwriting.")
    (out / "01_CHANNEL_METADATA/metadata-coverage.json").write_text(json.dumps(cov, indent=1, ensure_ascii=False))
    # channel metadata
    chmeta = dict(channel_id=cov["channel_id"], handle="@CasuallyFinance", channel_url="https://www.youtube.com/@CasuallyFinance", verification=enum["header"], uploads_playlist_id=enum["uploads_playlist_id"],
                  channel_name=rows[0]["channel_name"], snapshot=snapdir.name, collected_at=cov["generated_at"], format_counts=cov["by_format"],
                  catalog_stats={c: dict(n=cnt(c), views_median=statistics.median([r["views"] for r in rows if r["format_class"] == c and r["views"] is not None] or [0]),
                                         views_mean=round(statistics.mean([r["views"] for r in rows if r["format_class"] == c and r["views"] is not None] or [0])),
                                         views_max=max([r["views"] for r in rows if r["format_class"] == c and r["views"] is not None] or [0])) for c in ("LONG_FORM", "SHORT")},
                  third_party_claims_not_used_as_fact={"source": "~/Downloads/files (6)/05_CasualFinance_Summary.md + 07_CasualFinance_Metadata.json (2026-08-23, third-party/partial)", "claims": "subs 307K, 67+ videos, median 311K views, 'stock footage + motion graphics' style"})
    (out / "01_CHANNEL_METADATA/channel-metadata.json").write_text(json.dumps(chmeta, indent=1, ensure_ascii=False))
    print(json.dumps({k: cov[k] for k in ("unique_video_ids", "by_format", "enumeration", "classification_conflicts", "channel_id_verified_against_live_canonical_link")}, indent=1)[:1500])
    print(json.dumps(chmeta["catalog_stats"]))


if __name__ == "__main__":
    main(*sys.argv[1:3])
