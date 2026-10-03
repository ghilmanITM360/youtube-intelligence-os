"""Build the reconciled Senior Health master inventory and missing-data matrix.

Inputs (read-only):
  - <live-catalog>/candidates.tsv                  every recovered Senior Health lead
  - <live-catalog>/live/*.json                     public YouTube tab enumeration (yt_tabs.py)
  - data/catalog/youtube_channel_registry.db       canonical registry
  - data/catalog/youtube_inventory.db              Apify run provenance
  - [public-metadata-dir]/<channel_id>.jsonl       optional per-video public metadata (yt_video_meta.py)
Outputs:
  - SENIOR-HEALTH-MASTER-INVENTORY.json / .csv                 (default: the 2026-09-25 snapshot)
  - SENIOR-HEALTH-MASTER-INVENTORY-<date>.json / .csv          (when a later live-catalog-<date> is given)

Usage: build_master_inventory.py [live-catalog-dir] [public-metadata-dir]
"""
import csv, gzip, json, re, sqlite3, statistics, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parents[1]
DEFAULT_LIVE = "live-catalog-2026-09-25"
LIVE = HERE / (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_LIVE)
META = Path(sys.argv[2]) if len(sys.argv) > 2 else None

sys.path.insert(0, str(ROOT / "scripts"))
from video_type_classification import classify_video_type, REGULAR, SHORT, STREAM, UNKNOWN  # noqa: E402
PRICE = 0.004  # Free-plan $/video; re-verified live 2026-09-28 (Apify pricing page); must be re-verified before spend

REG = sqlite3.connect(ROOT / "data/catalog/youtube_channel_registry.db")
INV = sqlite3.connect(ROOT / "data/catalog/youtube_inventory.db")

# prior_class values that disqualify a lead from paid acquisition regardless of live state
NOT_ACQUIRABLE = {"removed", "terminated", "empty", "persona_clone", "persona_clone_breakout",
                  "dead_handle", "redirects_waterling", "thin"}
UNAVAILABLE = {"removed", "terminated", "empty", "dead_handle"}
DIRECT = {"direct", "direct_flagged", "small_direct"}

# Title-lexicon relevance screen over each channel's own enumerated public titles (a MEASURED share, not a
# quality or credential judgment). Thresholds are deliberately simple and reported alongside every row.
HEALTH_RE = re.compile(r"health|doctor|dr\.|heart|blood|pressure|diabet|sugar|vitamin|kidney|liver|brain|memory|dementia|"
                       r"sleep|pain|joint|bone|muscle|leg|walk|balance|fall|exercise|diet|food|eat|drink|nutri|protein|"
                       r"medic|pill|disease|cancer|stroke|cholesterol|inflamm|symptom|arthritis|mobility|strength|"
                       r"saúde|salud|स्वास्थ्य", re.I)
SENIOR_RE = re.compile(r"senior|elder|older|aging|ageing|over (5|6|7|8)0|after (5|6|7|8)0|(5|6|7|8)0\+|retire|"
                       r"grandparent|idoso|mayores|बुजुर्ग", re.I)
QUALIFY_HEALTH, QUALIFY_SENIOR, QUALIFY_MIN_TITLES = 0.6, 0.25, 5
# the 14 Group-C channels named in SENIOR-HEALTH-MASTER-INVENTORY-REPORT.md (2026-09-25)
QUALIFIED_PENDING_2026_09_25 = {
    "UCslmaJaMSw8F8BId4CxByJw", "UCC4TRhL4BiA7--jpxVVXcpQ", "UC2BaKQ5vqal9yaC-VbpD5ZQ", "UClzqmRzoC-7r8GiB_XQUn_A",
    "UCLxLjL1XVaKqZg-wZ2EBspA", "UCRxZVn1cDGyo_p7ZbxhkeUQ", "UCX_cW2SeHF1iBxbjx41vfrA", "UCPjG4ZRBkiO1y_vHlnj8jIg",
    "UCUUKjcYdqOHk2j-pbUnWDNw", "UC4oT7W2VOi-TJI3WWU51DHA", "UCHOrUqhgZmEwhmXqvLwghpg", "UCj-4CkWt2waFCjt5h7fZSiA",
    "UCxD2fste1dR0EUhj0gB8aOw", "UC6VFFdBkvTxy8VUO0d2h1Xg"}


def live_record(ref):
    p = LIVE / "live" / (ref.replace("@", "_").replace("/", "_") + ".json")
    if not p.exists() or not p.stat().st_size:
        return None
    return json.loads(p.read_text())


def repo_videos(cid):
    return {r[0]: r[1] for r in REG.execute(
        "select youtube_video_id, video_type from videos where canonical_channel_id=?", (cid,))}


SUBNICHE = {  # title keyword families -> sub-niche label (MEASURED keyword counts; top two reported)
    "cardiovascular": r"heart|cardio|blood pressure|hypertens|stroke|artery|arteries|cholesterol|circulation|amlodipine|losartan|lisinopril",
    "metabolic_diabetes": r"diabet|blood sugar|insulin|glucose|a1c|metabolic|belly fat|weight",
    "kidney": r"kidney|creatinine|renal",
    "brain_cognition": r"brain|memory|dementia|alzheimer|cognit|neuro",
    "mobility_fitness_falls": r"exercise|walk|balance|fall|leg strength|muscle|mobility|stretch|workout|squat|knee|joint",
    "nutrition": r"food|eat|fruit|vegetable|protein|vitamin|supplement|drink|diet|breakfast|snack|nuts|seed",
    "medication_safety": r"medication|pill|drug|amlodipine|metformin|statin|prescription|side effect",
    "sleep": r"sleep|bed|insomnia|night",
}
SUBNICHE_RE = {k: re.compile(v, re.I) for k, v in SUBNICHE.items()}


def channel_titles(tabs):
    return [t for tab in tabs.values() for t in ((tab or {}).get("items") or {}).values() if t]


def subniche(tabs):
    titles = channel_titles(tabs)
    counts = sorted(((sum(bool(rx.search(t)) for t in titles), k) for k, rx in SUBNICHE_RE.items()), reverse=True)
    return ";".join(k for n, k in counts[:2] if n) or None


def title_shares(tabs):
    titles = [t for tab in tabs.values() for t in ((tab or {}).get("items") or {}).values() if t]
    if not titles:
        return None, None, 0
    return (round(sum(bool(HEALTH_RE.search(t)) for t in titles) / len(titles), 3),
            round(sum(bool(SENIOR_RE.search(t)) for t in titles) / len(titles), 3), len(titles))


def metadata_coverage(cid):
    """Per-channel summary of yt_video_meta.py records; None when none were collected."""
    p = next((q for q in (META / f"{cid}.jsonl", META / f"{cid}.jsonl.gz") if q.exists()), None) if META and cid else None
    if not p:
        return None
    recs = [json.loads(l) for l in (gzip.open(p, "rt") if p.suffix == ".gz" else p.open())]
    if not recs:
        return None
    ok = [r for r in recs if r.get("video_details")]
    mf = lambda r: r.get("microformat") or {}
    views = [int(r["video_details"]["viewCount"]) for r in ok if str(r["video_details"].get("viewCount", "")).isdigit()]
    pub = sorted(mf(r)["publishDate"] for r in ok if mf(r).get("publishDate"))
    return {
        "meta_enumerated": len(recs), "meta_ok": len(ok), "meta_errors": sum("error" in r for r in recs),
        "meta_unavailable": sum(1 for r in recs if "error" not in r and not r.get("video_details")),
        "meta_channel_id_mismatch_ids": sorted(r["video_id"] for r in ok if r["video_details"].get("channelId") != cid),
        "meta_descriptions": sum(1 for r in ok if (r["video_details"].get("shortDescription") or "").strip()),
        "meta_likes": sum(1 for r in ok if mf(r).get("likeCount")),
        "meta_thumbnails": sum(1 for r in ok if (r["video_details"].get("thumbnail") or {}).get("thumbnails")),
        "meta_tags": sum(1 for r in ok if r["video_details"].get("keywords")),
        "meta_live_content": sum(1 for r in ok if r["video_details"].get("isLiveContent") or mf(r).get("liveBroadcastDetails")),
        "meta_earliest_publish": pub[0] if pub else None, "meta_latest_publish": pub[-1] if pub else None,
        "meta_views_median": int(statistics.median(views)) if views else None,
        "meta_views_max": max(views) if views else None,
        "meta_collected_at": max(r["collected_at"] for r in recs),
        "_publish_by_id": {r["video_id"]: mf(r).get("publishDate") for r in ok},
    }


def inventory_category(r):
    """Explicit taxonomy. Qualification, acquisition and research completeness are kept as separate fields."""
    if r["class"] == "OWN":
        return "OWN_CHANNEL"
    if r["prior_class"] in UNAVAILABLE or (r["class"] == "F" and r["live_status"] != "LIVE"):
        return "REMOVED_OR_UNAVAILABLE"
    if r["class"] == "F":
        return "EXCLUDED_BY_REVIEW"  # live but previously excluded (persona clone / thin) — see prior_class
    if r["repo_videos"]:
        live_total = sum(x or 0 for x in (r["live_regular"], r["live_shorts"], r["live_streams"]))
        if live_total and r["repo_videos"] < 0.5 * live_total:
            return "PARTIALLY_ACQUIRED"
        kinds = set(r["gap_kinds"].values())
        if "HISTORICAL_GAP" in kinds:
            return "ACQUIRED_WITH_HISTORICAL_GAPS"
        return "ACQUIRED_WITH_NEW_PUBLIC_UPLOADS" if kinds else "ACQUIRED_COMPLETE_AT_SNAPSHOT"
    if not r["canonical_channel_id"] or r["live_status"] != "LIVE":
        return "UNVERIFIED_IDENTITY"
    if r["canonical_channel_id"] in QUALIFIED_PENDING_2026_09_25:
        return "QUALIFIED_PENDING"
    h, s, n = r["health_title_share"], r["senior_title_share"], r["titles_screened"]
    if r["prior_class"] != "international_reference" and h is not None and \
            h >= QUALIFY_HEALTH and s >= QUALIFY_SENIOR and n >= QUALIFY_MIN_TITLES:
        return "HEALTH_RELEVANT_IDENTITY_ONLY"
    return "ADJACENT_HEALTH_REFERENCE"


def load_about():
    p = LIVE / "channel_about.jsonl"
    return {r["channel_id"]: r for r in map(json.loads, p.open())} if p.exists() else {}


def shared_titles():
    """Exact (case/space-normalized) title reuse across different channels in this snapshot (duplicate-network check)."""
    owners = {}
    for f in (LIVE / "live").glob("*.json"):
        if not f.stat().st_size:
            continue
        d = json.loads(f.read_text())
        for t in channel_titles(d.get("tabs") or {}):
            owners.setdefault(" ".join(t.lower().split()), set()).add(d.get("channel_id"))
    return {k: v for k, v in owners.items() if len(v) > 1}


def main():
    rows = []
    abouts = load_about()
    shared = shared_titles() if LIVE.name != DEFAULT_LIVE else {}
    for c in csv.DictReader(open(LIVE / "candidates.tsv"), delimiter="\t"):
        live = live_record(c["ref"]) or {}
        cid = live.get("channel_id") or (c["ref"] if c["ref"].startswith("UC") else None)
        reg = REG.execute("select channel_name,current_handle,status,package_status,transcript_status,"
                          "description_status,forensic_video_status,visual_asset_status from channels "
                          "where canonical_channel_id=?", (cid,)).fetchone() if cid else None
        datasets = [r[0] for r in REG.execute("select dataset_id from dataset_channels where canonical_channel_id=?", (cid,))] if cid else []
        runs = [r[0] for r in INV.execute("select actor_run_id from apify_source_runs where dataset_id in (%s)"
                                          % ",".join("?" * len(datasets)), datasets)] if datasets else []
        repo = repo_videos(cid) if cid else {}
        tabs = live.get("tabs", {})
        meta = metadata_coverage(cid) if META else None

        def live_ids(name):
            t = tabs.get(name) or {}
            return None if "error" in t or t.get("count") is None else set((t.get("items") or {}).keys())

        lv, ls, lst = live_ids("videos"), live_ids("shorts"), live_ids("streams")
        n_real_tx = REG.execute("select count(*) from transcripts t join videos v using(youtube_video_id) "
                                "where v.canonical_channel_id=? and t.is_placeholder=0", (cid,)).fetchone()[0] if cid else 0
        n_desc = sum(1 for _ in REG.execute("select 1 from videos where canonical_channel_id=? and length(coalesce(description,''))>0", (cid,))) if cid else 0
        n_thumb = sum(1 for _ in REG.execute("select 1 from videos where canonical_channel_id=? and length(coalesce(thumbnail_url,''))>0", (cid,))) if cid else 0
        repo_latest = REG.execute("select max(published_at) from videos where canonical_channel_id=?", (cid,)).fetchone()[0] if cid else None

        def missing(ids):
            return None if ids is None else sorted(ids - set(repo))

        miss_v, miss_s, miss_st = missing(lv), missing(ls), missing(lst)
        live_all = (lv or set()) | (ls or set()) | (lst or set())
        repo_not_live = sorted(set(repo) - live_all) if (lv is not None and ls is not None) else None
        removed = live.get("removed") or (live.get("error") if not cid else None)

        # --- classification A-F (Phase 2) ---
        if c["source_group"] == "OWN_CHANNEL":
            cls = "OWN"
        elif removed or c["prior_class"] in NOT_ACQUIRABLE or (lv is not None and not live_all):
            cls = "F"
        elif repo:
            gaps = [m for m in (miss_v, miss_s, miss_st) if m]
            unknown = any(m is None for m in (miss_v, miss_s, miss_st))
            cls = "B" if gaps else ("A" if not unknown else "B")
        elif reg:
            cls = "C" if reg[3] != "NO_PACKAGE" else "D"
        else:
            cls = "E"

        # Post-snapshot upload drift vs historical extraction gap. With per-video publish dates, a missing ID
        # published after the newest acquired video is a NEW upload; otherwise fall back to newest-first tab order.
        def gap_kind(name, miss):
            if not miss:
                return None
            pub = (meta or {}).get("_publish_by_id") or {}
            if repo_latest and all(pub.get(m) for m in miss):
                return "NEW_UPLOADS_SINCE_SNAPSHOT" if all(pub[m][:10] > repo_latest[:10] for m in miss) else "HISTORICAL_GAP"
            order = list((tabs.get(name) or {}).get("items") or {})
            return "NEW_UPLOADS_SINCE_SNAPSHOT" if all(order.index(m) < len(miss) for m in miss) else "HISTORICAL_GAP"

        gap_kinds = {n: k for n, m in (("videos", miss_v), ("shorts", miss_s), ("streams", miss_st))
                     if repo and (k := gap_kind(n, m))}
        if cls == "B" and set(gap_kinds.values()) == {"NEW_UPLOADS_SINCE_SNAPSHOT"}:
            cls = "A"  # complete as of its acquisition snapshot; refresh is optional
        need = sum(len(m) for m in (miss_v, miss_s, miss_st) if m)
        rows.append({
            "ref": c["ref"], "canonical_channel_id": cid,
            "verified_name": live.get("name") or (reg[0] if reg else None) or c["name"],
            "recorded_name": c["name"], "current_handle": live.get("handle") or (reg[1] if reg else None),
            "canonical_url": f"https://www.youtube.com/channel/{cid}" if cid else None,
            "source_group": c["source_group"], "prior_class": c["prior_class"],
            "senior_health_relevance": "DIRECT" if c["prior_class"] in DIRECT or c["prior_class"] == "registered" else
                                       ("OWN" if c["source_group"] == "OWN_CHANNEL" else "ADJACENT_OR_REFERENCE"),
            "live_observed_at": live.get("observed_at"), "live_status": removed or ("LIVE" if cid and live else "NOT_OBSERVED"),
            "header_videos": live.get("header_videos"), "subscribers": live.get("subscribers"),
            "live_regular": None if lv is None else len(lv), "live_shorts": None if ls is None else len(ls),
            "live_streams": None if lst is None else len(lst),
            "streams_tab": (tabs.get("streams") or {}).get("selected_tab"),
            "registry_status": reg[2] if reg else None, "package_status": reg[3] if reg else None,
            "dataset_ids": datasets, "apify_runs": runs,
            "repo_regular": sum(1 for t in repo.values() if classify_video_type(t) == REGULAR),
            "repo_shorts": sum(1 for t in repo.values() if classify_video_type(t) == SHORT),
            "repo_streams": sum(1 for t in repo.values() if classify_video_type(t) == STREAM),
            "repo_other": sum(1 for t in repo.values() if classify_video_type(t) == UNKNOWN),
            "repo_real_transcripts": n_real_tx, "repo_missing_transcripts": len(repo) - n_real_tx if repo else None,
            "repo_descriptions": n_desc,
            "missing_regular_ids": miss_v, "missing_shorts_ids": miss_s, "missing_stream_ids": miss_st,
            "repo_ids_not_currently_public": repo_not_live, "gap_kinds": gap_kinds,
            "required_new_results": need if cls in ("A", "B", "OWN") else (len(live_all) if cls == "E" else 0),
            "class": cls,
        })
        r = rows[-1]
        r["est_cost_usd"] = round(r["required_new_results"] * PRICE, 3)
        if LIVE.name != DEFAULT_LIVE:  # extended fields; the 2026-09-25 snapshot schema stays unchanged
            h, s, n = title_shares(tabs)
            mine = {" ".join(t.lower().split()) for t in channel_titles(tabs)}
            dup = {t: shared[t] - {cid} for t in mine if t in shared}
            r.update(sub_niche=subniche(tabs), shared_title_count=len(dup),
                     shared_title_channel_ids=sorted(set().union(*dup.values())) if dup else [])
            r.update(repo_videos=len(repo), repo_thumbnail_urls=n_thumb, repo_latest_publish=repo_latest,
                     health_title_share=h, senior_title_share=s, titles_screened=n,
                     credential_status="NOT_VERIFIED")
            ab = (abouts.get(cid) or {}).get("about") or {}
            r.update(country=ab.get("country") or ("NOT_PUBLICLY_STATED" if ab else "NOT_COLLECTED"),
                     joined=((ab.get("joinedDateText") or {}).get("content") or "").removeprefix("Joined ") or None,
                     channel_total_views=ab.get("viewCountText"),
                     channel_description=ab.get("description"))
            r["inventory_category"] = inventory_category(r)
            if meta:
                meta.pop("_publish_by_id")
                r.update(meta)
            live_total = len(live_all)
            ok = (meta or {}).get("meta_ok", 0)
            r["listing_detail_count"] = sum(len((t or {}).get("details") or {}) for t in tabs.values())
            r["metadata_completeness"] = ("NOT_APPLICABLE" if not live_total else
                                          "PER_VIDEO_COMPLETE" if ok >= live_total else
                                          "PER_VIDEO_PARTIAL" if ok else
                                          "LISTING_LEVEL_ONLY" if r["listing_detail_count"] >= live_total else "NONE")
            r["acquisition_completeness"] = ("NONE" if not repo else "COMPLETE_AT_SNAPSHOT" if not gap_kinds or
                                             set(gap_kinds.values()) == {"NEW_UPLOADS_SINCE_SNAPSHOT"} else "HISTORICAL_GAPS")
            r["transcript_status"] = reg[4] if reg else "NONE"
            r["forensic_research_status"] = (f"{reg[6]}; visual={reg[7]}" if reg else "NOT_STARTED")

    suffix = "" if LIVE.name == DEFAULT_LIVE else "-" + LIVE.name.removeprefix("live-catalog-")
    out = HERE / f"SENIOR-HEALTH-MASTER-INVENTORY{suffix}"
    json.dump({"generated_by": "forensic-v3/scripts/build_master_inventory.py", "live_catalog": LIVE.name,
               "price_per_result_usd_unverified": PRICE, "channels": rows} if suffix else
              {"generated_by": "forensic-v3/scripts/build_master_inventory.py", "price_per_result_usd_unverified": PRICE,
               "channels": rows}, open(f"{out}.json", "w"), indent=1, ensure_ascii=False)
    flat = [k for k in dict.fromkeys(k for r in rows for k in r)
            if not k.endswith("_ids") and k not in ("repo_ids_not_currently_public",)]
    with open(f"{out}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=flat + ["missing_ids"], extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({**{k: (";".join(v) if isinstance(v, list) else v) for k, v in r.items()},
                        "missing_ids": ";".join((r["missing_regular_ids"] or []) + (r["missing_shorts_ids"] or []) + (r["missing_stream_ids"] or []))})
    print(Counter(r["class"] for r in rows))
    if suffix:
        print(Counter(r["inventory_category"] for r in rows))
        render_report(rows, HERE / f"SENIOR-HEALTH-MASTER-INVENTORY-REPORT{suffix}.md")


TABLES = [
    ("1. Acquired Senior Health competitors", lambda r: r["inventory_category"].startswith(("ACQUIRED", "PARTIALLY"))),
    ("2. Qualified pending competitors (2026-09-25 Group C)", lambda r: r["inventory_category"] == "QUALIFIED_PENDING"),
    ("3. Identity-only leads that pass the relevance screen (pre-2026-09-28 leads)",
     lambda r: r["inventory_category"] == "HEALTH_RELEVANT_IDENTITY_ONLY" and not r["source_group"].startswith("DISCOVERY_2026_09_28")),
    ("4. Newly discovered relevant channels (2026-09-28 discovery)",
     lambda r: r["inventory_category"] == "HEALTH_RELEVANT_IDENTITY_ONLY" and r["source_group"].startswith("DISCOVERY_2026_09_28")),
    ("5. Adjacent / reference channels", lambda r: r["inventory_category"] == "ADJACENT_HEALTH_REFERENCE"),
    ("6. Own channel (never counted as a competitor)", lambda r: r["inventory_category"] == "OWN_CHANNEL"),
    ("7. Removed, excluded or unverified", lambda r: r["inventory_category"] in
     ("REMOVED_OR_UNAVAILABLE", "EXCLUDED_BY_REVIEW", "UNVERIFIED_IDENTITY")),
]


def render_report(rows, path):
    """Channel-by-channel markdown tables; every total is summed from the rows rendered beneath it."""
    n = lambda v: 0 if v is None else v
    fmt = lambda v: "—" if v is None else str(v)
    head = ("| Channel | Channel ID | Handle | Category | Sub-niche | Country | Subs | Live R/S/L | Repo R/S/L | "
            "Repo desc/tx/thumb | Per-video metadata ok/enumerated | Listing cards | Missing vs repo | Shared titles | Results if acquired | Est. $ |")
    out = [f"# Senior Health master inventory — {LIVE.name.removeprefix('live-catalog-')}", "",
           f"Generated by `forensic-v3/scripts/build_master_inventory.py {LIVE.name} <public-metadata>` from the live "
           "snapshot, the canonical registry and DS-000034 public metadata. Do not hand-edit; rebuild instead.", "",
           "Category counts: " + ", ".join(f"{k} {v}" for k, v in sorted(Counter(r['inventory_category'] for r in rows).items())), ""]
    for title, pred in TABLES:
        sel = [r for r in rows if pred(r)]
        out += [f"## {title} — {len(sel)} channels", "", head, "|" + "---|" * 16]
        for r in sel:
            miss = sum(len(r[k] or []) for k in ("missing_regular_ids", "missing_shorts_ids", "missing_stream_ids")) if r["repo_videos"] else "—"
            out.append("| " + " | ".join(map(str, [
                r["verified_name"].replace("|", "/"), f"`{r['canonical_channel_id']}`" if r["canonical_channel_id"] else "—",
                fmt(r["current_handle"]), r["inventory_category"], fmt(r.get("sub_niche")), fmt(r.get("country")),
                fmt(r["subscribers"]), f"{fmt(r['live_regular'])}/{fmt(r['live_shorts'])}/{fmt(r['live_streams'])}",
                f"{r['repo_regular']}/{r['repo_shorts']}/{r['repo_streams']}",
                f"{r['repo_descriptions']}/{r['repo_real_transcripts']}/{r['repo_thumbnail_urls']}",
                f"{fmt(r.get('meta_ok'))}/{fmt(r.get('meta_enumerated'))}", r["listing_detail_count"], miss, r.get("shared_title_count", 0),
                r["required_new_results"], f"{r['est_cost_usd']:.3f}"])) + " |")
        out += ["", f"Totals: live videos {sum(n(r['live_regular']) + n(r['live_shorts']) + n(r['live_streams']) for r in sel)}, "
                f"repo videos {sum(r['repo_videos'] for r in sel)}, per-video metadata records {sum(n(r.get('meta_ok')) for r in sel)}, "
                f"listing cards {sum(r['listing_detail_count'] for r in sel)}, "
                f"results if acquired {sum(r['required_new_results'] for r in sel)}, est. ${sum(r['est_cost_usd'] for r in sel):.3f}", ""]
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
