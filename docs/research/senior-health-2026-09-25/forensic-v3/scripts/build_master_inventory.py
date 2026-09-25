"""Build the reconciled Senior Health master inventory and missing-data matrix.

Inputs (read-only):
  - live-catalog-2026-09-25/candidates.tsv          every recovered Senior Health lead
  - live-catalog-2026-09-25/live/*.json            public YouTube tab enumeration (yt_tabs.py)
  - data/catalog/youtube_channel_registry.db       canonical registry
  - data/catalog/youtube_inventory.db              Apify run provenance
Outputs:
  - SENIOR-HEALTH-MASTER-INVENTORY.json / .csv
"""
import csv, json, sqlite3, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parents[1]
LIVE = HERE / "live-catalog-2026-09-25"
PRICE = 0.004  # last verified $/result (Free plan, 2026-09-25 DS-000033 run); must be re-verified live before spend

REG = sqlite3.connect(ROOT / "data/catalog/youtube_channel_registry.db")
INV = sqlite3.connect(ROOT / "data/catalog/youtube_inventory.db")

# prior_class values that disqualify a lead from paid acquisition regardless of live state
NOT_ACQUIRABLE = {"removed", "terminated", "empty", "persona_clone", "persona_clone_breakout",
                  "dead_handle", "redirects_waterling", "thin"}
DIRECT = {"direct", "direct_flagged", "small_direct"}


def live_record(ref):
    p = LIVE / "live" / (ref.replace("@", "_").replace("/", "_") + ".json")
    if not p.exists() or not p.stat().st_size:
        return None
    return json.loads(p.read_text())


def repo_videos(cid):
    return {r[0]: r[1] for r in REG.execute(
        "select youtube_video_id, video_type from videos where canonical_channel_id=?", (cid,))}


def main():
    rows = []
    for c in csv.DictReader(open(LIVE / "candidates.tsv"), delimiter="\t"):
        live = live_record(c["ref"]) or {}
        cid = live.get("channel_id") or (c["ref"] if c["ref"].startswith("UC") else None)
        reg = REG.execute("select channel_name,current_handle,status,package_status,transcript_status,"
                          "description_status from channels where canonical_channel_id=?", (cid,)).fetchone() if cid else None
        datasets = [r[0] for r in REG.execute("select dataset_id from dataset_channels where canonical_channel_id=?", (cid,))] if cid else []
        runs = [r[0] for r in INV.execute("select actor_run_id from apify_source_runs where dataset_id in (%s)"
                                          % ",".join("?" * len(datasets)), datasets)] if datasets else []
        repo = repo_videos(cid) if cid else {}
        tabs = live.get("tabs", {})

        def live_ids(name):
            t = tabs.get(name) or {}
            return None if "error" in t or t.get("count") is None else set((t.get("items") or {}).keys())

        lv, ls, lst = live_ids("videos"), live_ids("shorts"), live_ids("streams")
        n_real_tx = REG.execute("select count(*) from transcripts t join videos v using(youtube_video_id) "
                                "where v.canonical_channel_id=? and t.is_placeholder=0", (cid,)).fetchone()[0] if cid else 0
        n_desc = sum(1 for _ in REG.execute("select 1 from videos where canonical_channel_id=? and length(coalesce(description,''))>0", (cid,))) if cid else 0

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

        # A gap made only of the newest items of a newest-first tab is post-snapshot upload drift;
        # anything else (e.g. the oldest Shorts) is a historical extraction gap.
        def gap_kind(name, miss):
            if not miss:
                return None
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
            "repo_regular": sum(1 for t in repo.values() if t == "video"),
            "repo_shorts": sum(1 for t in repo.values() if t == "shorts"),
            "repo_other": sum(1 for t in repo.values() if t not in ("video", "shorts")),
            "repo_real_transcripts": n_real_tx, "repo_missing_transcripts": len(repo) - n_real_tx if repo else None,
            "repo_descriptions": n_desc,
            "missing_regular_ids": miss_v, "missing_shorts_ids": miss_s, "missing_stream_ids": miss_st,
            "repo_ids_not_currently_public": repo_not_live, "gap_kinds": gap_kinds,
            "required_new_results": need if cls in ("A", "B", "OWN") else (len(live_all) if cls == "E" else 0),
            "class": cls,
        })
        r = rows[-1]
        r["est_cost_usd"] = round(r["required_new_results"] * PRICE, 3)

    out = HERE / "SENIOR-HEALTH-MASTER-INVENTORY"
    json.dump({"generated_by": "forensic-v3/scripts/build_master_inventory.py", "price_per_result_usd_unverified": PRICE,
               "channels": rows}, open(f"{out}.json", "w"), indent=1, ensure_ascii=False)
    flat = [k for k in rows[0] if not k.endswith("_ids") and k not in ("repo_ids_not_currently_public",)]
    with open(f"{out}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=flat + ["missing_ids"], extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({**{k: (";".join(v) if isinstance(v, list) else v) for k, v in r.items()},
                        "missing_ids": ";".join((r["missing_regular_ids"] or []) + (r["missing_shorts_ids"] or []) + (r["missing_stream_ids"] or []))})
    from collections import Counter
    print(Counter(r["class"] for r in rows))


if __name__ == "__main__":
    sys.exit(main())
