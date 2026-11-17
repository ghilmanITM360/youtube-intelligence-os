"""Build Stage A workbook + CSVs from pinned, read-only sources. Writes only into this scratchpad folder."""
import csv, collections, glob, hashlib, json, math, re, sqlite3, pathlib
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

S = pathlib.Path(__file__).parent
REPO = pathlib.Path("/Users/ghilmankhan/workprojects/youtube-intelligence-os")
DBP = REPO / "data/catalog/youtube_channel_registry.db"
OBS = "2026-11-09T20:56Z..2026-11-09T21:40Z (UTC)"
PRICE = 0.004  # USD/video, Free plan, observed 2026-09-20 (DS-000027 preflight); ESTIMATE - recheck live
PRIORITY = {"FINANCE", "ECONOMICS", "SENIOR_HEALTH", "HISTORY"}
ns = {}; exec((S / "class_existing.py").read_text(), ns); C = ns["C"]
ns = {}; exec((S / "class_incoming.py").read_text(), ns); I = ns["I"]

db = sqlite3.connect(f"file:{DBP}?mode=ro", uri=True)
db.row_factory = sqlite3.Row
existing = {r["id"]: dict(r) for r in csv.DictReader(open(S / "existing_raw.csv"))}
samples_db = collections.defaultdict(list)
for r in db.execute("select canonical_channel_id c, youtube_video_id v from (select *, row_number() over (partition by canonical_channel_id order by views desc) rn from videos) where rn<=2"):
    samples_db[r["c"]].append("https://www.youtube.com/watch?v=" + r["v"])
max_pub = {r[0]: r[1] for r in db.execute("select canonical_channel_id, max(published_at) from videos group by 1")}

def load(pattern):
    return [json.loads(l) for f in sorted(glob.glob(str(S / pattern))) for l in open(f)]
pages_in = load("pages*.jsonl")
pages_ex = {r["channel_id"]: r for r in load("existing_pages.jsonl")}

def vids(r):
    vs = r.get("videos_sample", []); ids = {v["video_id"] for v in vs}
    return vs, [s for s in r.get("shorts_sample", []) if s["video_id"] not in ids]

def reported(r):
    for t in r.get("header_meta", []):
        m = re.match(r"([\d.,]+)(K?) videos?", t)
        if m:
            n = float(m.group(1).replace(",", "")); return int(n * 1000) if m.group(2) else int(n)
    return None

def subs(r):
    return next((t for t in r.get("header_meta", []) if "subscriber" in t), "")

# PR #39 / #38 / #43 / #37 / #46 known packages (by exact channel ID)
pr39 = {r["channel_id"]: r for r in csv.DictReader(open(S / "pr39_status.csv"))}
PKG = {cid: f"PR #39 research/youtube-12-channel-metadata @967ea707 ({r['public_captured']} public of {r['reported_videos']} reported; snapshot 2026-10-20; captions not captured)" for cid, r in pr39.items()}
PKG["UCiBGqUxeTe4AYQyRseSZaKw"] = "PR #38 research/monkey-explains-1999 @f176aa28 (76 public + 45 members-only evidence rows; 0 captions; snapshot 2026-10-20; $0.500)"
PKG["UCrNfRFWnLC3tCy1TnyhVQ7g"] = "PR #37 @1adfdeb9 inventory (210 videos) + PR #46 reviewed workbook @264e9ebf; CF hub research/casually-finance-consolidated @9a4023af; 206/206 Whisper-base ASR only"
PKG["UCPq6p8XwJcO5wY6BZiHab-A"] = "DS-000034 data/raw/competitors/DS-000034/UCPq6p8XwJcO5wY6BZiHab-A.jsonl.gz on main (26 per-video records, youtubei player, 2026-09-28; dataset present in registry but channel not registered; records mark playability UNPLAYABLE from that collection)"
# ID mentions on other refs (lead only; a mention is not a package)
hits = collections.defaultdict(set)
for l in open(S / "pkg_hits.tsv"):
    cid, ref, d = l.rstrip("\n").split("\t")
    hits[cid].add(f"{ref.replace('origin/','')}:{d}")
def mention(cid):
    h = sorted(hits.get(cid, ()))
    return f"{len(h)} ref:dir hits, e.g. " + "; ".join(h[:3]) if h else ""

# ---------- Existing Registry ----------
ex_rows = []
for cid, e in sorted(existing.items(), key=lambda x: x[1]["channel_name"].lower()):
    n, sub, sec, ctype, conf, why = C[cid]
    p = pages_ex.get(cid)
    sample = samples_db.get(cid) or (["https://www.youtube.com/watch?v=" + v["video_id"] for v in vids(p)[0][:2]] if p else [])
    nv = int(e["n_videos"])
    gaps = []
    if nv == 0: gaps.append("no video metadata in registry")
    else:
        if int(e["n_thumb_url"]) < nv: gaps.append(f"thumbnail_url missing {nv-int(e['n_thumb_url'])}/{nv}")
        if int(e["n_thumb_bin"]) == 0: gaps.append("no thumbnail binaries")
        if int(e["n_tx_placeholder"]): gaps.append(f"placeholder transcripts {e['n_tx_placeholder']}")
        if int(e["n_tx_real"]) < nv: gaps.append(f"real text {e['n_tx_real']}/{nv}")
        if p is None and nv: gaps.append(f"registry snapshot ends {max_pub.get(cid,'')[:10]}")
    drift = ""
    if p and p.get("title") and p["title"].strip() != e["channel_name"].strip():
        drift = f"live title '{p['title'].strip()}' vs registry '{e['channel_name']}'"
    if p and (p.get("vanity_url") or "").lower().rstrip("/").split("/")[-1] != (e["current_handle"] or "").lower():
        drift += f"; live handle {(p.get('vanity_url') or '').split('/')[-1]} vs registry {e['current_handle']}"
    ex_rows.append({
        "canonical_channel_id": cid, "channel_name": e["channel_name"], "handle": e["current_handle"],
        "source_group": e["source_group"], "target_group": e["target_group"], "registry_status": e["status"],
        "primary_niche": n, "sub_niche": sub, "secondary_niche": sec, "channel_type": ctype, "confidence": conf,
        "classification_basis": ("registry titles (DB)" if nv else "") + (" + public page " + OBS if p else ""),
        "rationale": why, "sample_url_1": sample[0] if sample else "", "sample_url_2": sample[1] if len(sample) > 1 else "",
        "live_subscribers_obs": subs(p) if p else "", "live_reported_videos_obs": reported(p) if p else "",
        "reg_videos": nv, "reg_titles": e["n_title"], "reg_views": e["n_views"], "reg_dates": e["n_date"],
        "reg_date_range": e["date_range"], "reg_thumbnail_urls": e["n_thumb_url"], "reg_thumbnail_binaries": e["n_thumb_bin"],
        "reg_real_transcripts": e["n_tx_real"], "reg_placeholder_transcripts": e["n_tx_placeholder"],
        "reg_caption_types": e["caption_types"], "transcript_status": e["transcript_status"],
        "staged_package_outside_registry": PKG.get(cid, ""), "id_mentions_on_refs_lead": mention(cid),
        "identity_drift_flag": drift.strip("; "), "gaps": "; ".join(gaps),
        "in_incoming_list": "",
    })
ex_by_id = {r["canonical_channel_id"]: r for r in ex_rows}

# ---------- Incoming Review + Crosswalk ----------
REPEAT = {"@primateeconomics": 2, "@monkebiznis": 2, "@primitiveeducation": 2, "@logicalmoney72": 2, "@markbuildsus": 2,
          "@unknownfrequencies-tv": 2, "@unclefrankretirement16": 2, "@unclejohnfinancial": 2, "@chronofold-m8x": 2,
          "@thetimepiecehistory": 2, "@whatif4k": 2, "@serioushistory": 3, "@drdinnes-yt": 2, "@williamthorneuk01": 2,
          "@cronusmakescents": 2, "@wild_instinct-mvp": 2, "@forksofwar": 2, "@whythatyoutube": 2, "@galactichighway3000": 2}
SUFFIX = {"@monkeyexplains1999": "/featured"} | {h: "/videos" for h in ["@thetimepiecehistory", "@drnimrahealth", "@thereptheory111",
          "@thefinance_pov", "@franksutherlandva", "@williamthorneuk01", "@frank_law_uk", "@nia.prescott", "@thewealthlogicaustralia",
          "@mark.calloway", "@goodenoughanimation", "@metabolicinsights-h1b", "@ethos-j7t", "@funnotsofun"]}
assert sum(REPEAT.get(k, 1) for k in I) == 144 and len(I) == 124
order = open(S / "inputs.txt").read().split()
pg = {r["input_url"]: r for r in pages_in}
in_rows, xw = [], []
for seq, url in enumerate(order, 1):
    key = url.split("youtube.com/")[1].replace("channel/", "").lower()
    r = pg[url]; cid = r.get("channel_id")
    occ = REPEAT.get(key, 1)
    cls = I[key]
    if cid in existing:
        dbm = "ALREADY_IN_DB"; e = ex_by_id[cid]; e["in_incoming_list"] = f"Incoming #{seq}"
        n, sub, sec, ctype, conf, why = C[cid]; cls_src = "Existing Registry row (shared classification)"
    elif cid:
        dbm = "NEW_TO_DB"; n, sub, sec, ctype, conf, why = cls; cls_src = "incoming public page sample"
    else:
        dbm = "IDENTITY_UNRESOLVED"; n, sub, sec, ctype, conf, why = ("UNCLEAR", "", "", "", "low", "HTTP 404 on /@handle, /videos and /about; web search found no identity lead"); cls_src = "none"
    vs, sh = vids(r)
    in_rows.append({
        "seq": seq, "normalized_input_url": url, "input_handle_as_supplied": url.split("youtube.com/")[1],
        "occurrence_count": occ, "original_suffix_removed": SUFFIX.get(key, ""),
        "canonical_channel_id": cid or "", "identity_status": "VERIFIED" if cid else "PAGE_UNAVAILABLE",
        "live_title": (r.get("title") or "").strip(), "live_handle": (r.get("vanity_url") or "").split("/")[-1],
        "subscribers_obs": subs(r), "reported_videos_obs": reported(r),
        "db_membership": dbm, "staged_package": PKG.get(cid, ""), "id_mentions_on_refs_lead": mention(cid) if cid else "",
        "primary_niche": n, "sub_niche": sub, "secondary_niche": sec, "channel_type": ctype, "confidence": conf,
        "classification_source": cls_src, "rationale": why,
        "sample_url_1": f"https://www.youtube.com/watch?v={vs[0]['video_id']}" if vs else (f"https://www.youtube.com/shorts/{sh[0]['video_id']}" if sh else ""),
        "sample_url_2": f"https://www.youtube.com/watch?v={vs[1]['video_id']}" if len(vs) > 1 else (f"https://www.youtube.com/shorts/{sh[0]['video_id']}" if sh and vs else ""),
        "sample_titles": " || ".join((v["title"] or "")[:70] for v in vs[:8]),
        "shorts_tab_titles": " || ".join((v["title"] or "")[:60] for v in sh[:4]),
        "access_path": r["access_path"], "observed_at_utc": r["observed_at_utc"],
        "videos_page_sha256": r.get("videos_page_sha256") or "", "http_videos/shorts": f"{r.get('videos_http')}/{r.get('shorts_http')}",
        "description_excerpt": (r.get("description") or "")[:200].replace("\n", " "),
    })
    xw.append({"seq": seq, "supplied_entries_represented": occ,
               "supplied_forms": url + (" (+" + SUFFIX[key] + " form)" if key in SUFFIX else "") + (f" x{occ}" if occ > 1 else ""),
               "normalized_url": url, "handle_compare_key_casefold": key, "resolved_channel_id": cid or "UNRESOLVED",
               "resolution_evidence": "ytInitialData channelMetadataRenderer.externalId + <link rel=canonical>" if cid else "HTTP 404",
               "registry_match": dbm, "registry_name": existing[cid]["channel_name"] if cid in existing else "",
               "conflict_or_note": ""})
for x in xw:
    r = next(i for i in in_rows if i["seq"] == x["seq"])
    if r["db_membership"] == "ALREADY_IN_DB" and r["live_title"].lower() != x["registry_name"].strip().lower():
        x["conflict_or_note"] = f"display name differs: live '{r['live_title']}' vs registry '{x['registry_name']}' (ID exact match)"
    elif r["live_handle"] and r["live_handle"].lower() != r["input_handle_as_supplied"].lower() and not r["input_handle_as_supplied"].startswith("channel/"):
        x["conflict_or_note"] = f"live handle {r['live_handle']} (case-insensitive compare)"
    elif r["input_handle_as_supplied"].startswith("channel/") and r["live_handle"]:
        x["conflict_or_note"] = f"UC input; live handle {r['live_handle']}"
ids = collections.Counter(r["canonical_channel_id"] for r in in_rows if r["canonical_channel_id"])
assert all(v == 1 for v in ids.values()), "distinct URLs resolved to same ID"

# ---------- Apify Queue ----------
B1 = {  # proposed first batch: new channels in the four priority niches, moderate size, clear niche
 "UCMl8WtFdqfnzzKcC2KWZZnQ", "UCj0uhARVVmROWv9TBpVIr9Q", "UCW_JmbBR0gsRGIUGRY3WA-Q", "UCAOeipQ5KGzZ2McMF1RNsrQ",
 "UCZXShYiBJlahi8mCNiU3XBg", "UCr1NnI7dwgIqeGJymhKL37A", "UC8p5EKG8jlsL2R2bvr2fZ3g",
 "UCvHD6lldf4L3XMAmGU44cYw", "UCLxJ_nQg42P-0XNRdGwA2gg", "UCsPba6Pqq_cp37zyU6MP82g", "UC1rXgYI3Eqsyyt06QEbGg3Q",
 "UCoZd78hRUdxxsuGiABuHF_A", "UC2YHYn047fkAob8Od3leQjw", "UCuyKlvQhPbPKdENL8y1lDrA", "UCSwjhnEm3TP94W_lvs9miIQ"}
q = []
def limit_for(n):
    return None if n is None else int(math.ceil(n * 1.10)) + 5
def add(cid, name, pop, niche, action, missing, pkg, rationale, n_rep, scope="regular videos + Shorts (streams 0 unless observed); restricted rows kept as evidence, excluded from public master", batch=""):
    lim = limit_for(n_rep) if action in ("NEW_FULL_SNAPSHOT",) else None
    q.append({"canonical_channel_id": cid, "channel_name": name, "population": pop, "primary_niche": niche,
              "proposed_action": action, "proposed_batch": batch, "exact_missing_fields": missing, "existing_package_ref": pkg,
              "public_format_scope": scope if action != "REUSE" else "n/a", "date_scope": "full channel history (no date filter: avoids $1.30/1k date-range event)" if action == "NEW_FULL_SNAPSHOT" else ("only videos missing the field" if action == "GAP_FILL" else "n/a"),
              "reported_videos_obs": n_rep if n_rep is not None else "UNKNOWN",
              "result_limit_total": lim if lim else "", "est_cost_usd": round(lim * PRICE, 3) if lim else ("UNKNOWN" if action == "GAP_FILL" else 0),
              "cost_basis": f"${PRICE}/video Free-plan rate observed 2026-09-20; ESTIMATE, recheck live" if lim else "",
              "rationale": rationale, "approval_status": "NOT_APPROVED"})
seen = set()
for r in in_rows:
    cid = r["canonical_channel_id"]
    if not cid:
        add("", r["input_handle_as_supplied"], "INCOMING", "UNCLEAR", "HOLD", "identity", "", "IDENTITY_UNRESOLVED: HTTP 404; owner to supply current URL or UC ID", None); continue
    seen.add(cid); n = r["primary_niche"]; pop = "BOTH" if r["db_membership"] == "ALREADY_IN_DB" else "INCOMING"
    if cid in PKG:
        add(cid, r["live_title"], pop, n, "REUSE", "caption track existence + caption text (not captured); thumbnail binaries (not approved)", PKG[cid],
            "Staged package exists outside the canonical registry; do not rerun metadata. Caption gap-fill is a separate optional batch.", r["reported_videos_obs"])
    elif pop == "BOTH":
        e = ex_by_id[cid]
        if e["source_group"] == "IDENTITY_ONLY":
            add(cid, r["live_title"], pop, n, "NEW_FULL_SNAPSHOT", "all video metadata; caption existence", "", "In registry as identity only; HISTORY niche", r["reported_videos_obs"], batch="B2")
        else:
            add(cid, r["live_title"], pop, n, "GAP_FILL", f"videos published after {max_pub.get(cid,'')[:10]} (registry {e['reg_videos']} vs live {r['reported_videos_obs']})", e["source_group"],
                "Registry package is complete for its snapshot; only newer uploads are missing", r["reported_videos_obs"], batch="B3")
    elif n in PRIORITY:
        add(cid, r["live_title"], pop, n, "NEW_FULL_SNAPSHOT", "all: identity, video IDs/URLs, titles, descriptions, publish timestamps, duration, format, views/likes/comments, thumbnail URLs, caption existence",
            "", f"Verified new channel in priority niche {n} ({r['confidence']} confidence)", r["reported_videos_obs"], batch="B1" if cid in B1 else "B2")
    else:
        add(cid, r["live_title"], pop, n, "HOLD", "all", "", f"Niche {n} is not one of the three fixed priority groups; awaiting owner choice of fourth group", r["reported_videos_obs"])
for e in ex_rows:
    cid = e["canonical_channel_id"]
    if cid in seen: continue
    n = e["primary_niche"]; nv = e["reg_videos"]
    if "IDENTITY DRIFT" in e["rationale"] or (e["identity_drift_flag"] and nv == 0 and "Overhead" in e["channel_name"]):
        add(cid, e["channel_name"], "EXISTING", n, "HOLD", "identity re-verification", "", "Identity drift: channel renamed/rebranded since registration; owner check before spend", e["live_reported_videos_obs"] or None); continue
    if cid in PKG:
        add(cid, e["channel_name"], "EXISTING", n, "REUSE", "official caption tracks (only ASR exists)", PKG[cid], "Staged package outside registry; do not re-acquire metadata", e["live_reported_videos_obs"] or None); continue
    if nv == 0:
        if n in PRIORITY:
            add(cid, e["channel_name"], "EXISTING", n, "NEW_FULL_SNAPSHOT", "all video metadata; caption existence", "", f"Registry identity only; priority niche {n}", e["live_reported_videos_obs"] or None, batch="B2")
        else:
            add(cid, e["channel_name"], "EXISTING", n, "HOLD", "all video metadata", "", f"Identity only; niche {n} not in fixed priority groups", e["live_reported_videos_obs"] or None)
        continue
    miss = []
    if int(e["reg_placeholder_transcripts"]): miss.append(f"caption/transcript text for {e['reg_placeholder_transcripts']} placeholder videos")
    thumb = f"thumbnail_url empty for {nv-int(e['reg_thumbnail_urls'])} videos (derivable from video ID pattern; no Apify spend; label DERIVED if filled)" if int(e["reg_thumbnail_urls"]) < nv else ""
    if miss:
        if thumb: miss.append(thumb)
        add(cid, e["channel_name"], "EXISTING", n, "GAP_FILL", "; ".join(miss), e["source_group"], "Package exists; fill named fields only", None, batch="B3")
    else:
        add(cid, e["channel_name"], "EXISTING", n, "REUSE", thumb or "thumbnail binaries only (not approved; not an Apify metadata gap)", e["source_group"], "Registry package complete for its snapshot", None)

# ---------- Niche Summary ----------
ex_n = collections.Counter(r["primary_niche"] for r in ex_rows)
in_n = collections.Counter(r["primary_niche"] for r in in_rows if r["canonical_channel_id"])
comb = {r["canonical_channel_id"]: r["primary_niche"] for r in ex_rows}
for r in in_rows:
    if r["canonical_channel_id"]: comb.setdefault(r["canonical_channel_id"], r["primary_niche"])
cb = collections.Counter(comb.values())
niches = sorted(set(ex_n) | set(in_n), key=lambda k: (k not in PRIORITY, -cb[k], k))
summ = [{"primary_niche": k, "priority_group": "FIXED_PRIORITY" if k in PRIORITY else ("FOURTH_GROUP_CANDIDATE" if cb[k] >= 5 and k != "UNCLEAR" else ""),
         "existing_registry": ex_n[k], "incoming_verified": in_n[k], "combined_dedup_by_id": cb[k],
         "incoming_new_to_db": sum(1 for r in in_rows if r["primary_niche"] == k and r["db_membership"] == "NEW_TO_DB")} for k in niches]
summ.append({"primary_niche": "IDENTITY_UNRESOLVED (incoming, not counted above)", "priority_group": "", "existing_registry": 0,
             "incoming_verified": 0, "combined_dedup_by_id": 0, "incoming_new_to_db": 0, "unresolved_rows": sum(1 for r in in_rows if not r["canonical_channel_id"])})
summ.append({"primary_niche": "TOTAL", "existing_registry": len(ex_rows), "incoming_verified": len(ids), "combined_dedup_by_id": len(comb),
             "incoming_new_to_db": sum(1 for r in in_rows if r["db_membership"] == "NEW_TO_DB")})

pins = [
 ("generated_at_utc", "2026-11-09/10"), ("repo_commit_HEAD", "efd3dc0a18bc50e95ae6a6c1e1b9931b2d0abbf6 (docs/yios-consolidation-index, clean)"),
 ("registry_db_path", "data/catalog/youtube_channel_registry.db (Git LFS, materialized, opened mode=ro)"),
 ("registry_db_sha256", hashlib.sha256(DBP.read_bytes()).hexdigest()),
 ("registry_schema_version", "PRAGMA user_version=0 (no numbered schema version); registry_metadata.generated_at=2026-09-28T13:21:20Z"),
 ("registry_source_payload_sha256", "b8f72bfee5d3c8edc206dd4a28d4f31470b9f24a1305044548a1dc78ebd90296"),
 ("canonical_channel_count", "75 (STANDARD_PACKAGE 40, HISTORICAL_CATALOG 6, IDENTITY_ONLY 29); 2,303 videos"),
 ("count_vs_owner_expectation", "Owner expected ~73. docs/YOUTUBE_CHANNEL_REGISTRY.md (verified 2026-09-23) says 71; the DB was rebuilt 2026-09-28 after PR #6 added DS-000029/30/32/33 (Doctor Thomas, Senior Health Hub, Decode Your Heart, Better Health While Aging) = 75. No evidence supports 73."),
 ("incoming_reconciliation", "144 supplied entries -> 124 normalized URLs (20 repeats; 15 suffixes removed) -> 120 verified UC IDs (0 shared IDs) + 4 IDENTITY_UNRESOLVED"),
 ("incoming_raw_list_note", "Only the 124-URL list and the Appendix repeat/suffix summary were supplied; occurrence counts are reconstructed from that summary, not from a raw 144-line file."),
 ("access_path", "Public HTTP fetch of each channel /videos and /shorts page (no login; consent cookie only); no media downloaded; Firefox/browser session NOT used (cost/scale); 4 x 404 checked by web search"),
 ("classification_nature", "AI interpretation of titles/descriptions; not factual observation. channel_type is UNOBSERVED unless the description or title format states it; thumbnails were not viewed."),
 ("package_presence_method", "Known packages matched by exact UC ID (PR #38, #39, #37/#46, DS-000034 on main). id_mentions_on_refs_lead = git grep of the 120 IDs over remote refs: 52 of 56 refs scanned; NOT scanned: origin/ui/v1 and 3 origin/yios-test/* claim refs. Local worktrees and ~/YIOS-local-audits were not ID-scanned beyond the known CF/xkcd/BE/PE folders. A mention is a lead, not a package."),
 ("pricing_basis", "$4.00/1,000 videos Free plan (data/raw/channel-data/DS-000027/preflight/authenticated_apify_pricing_evidence.json, 2026-09-20). Historical: PR #38 $0.500 total; PR #39 $2.012 total. Must be rechecked live before any run."),
]

# ---------- write ----------
def sheet(wb, name, rows, first=False):
    ws = wb.active if first else wb.create_sheet(name); ws.title = name
    if not rows: return
    cols = list(dict.fromkeys(k for r in rows for k in r))
    ws.append(cols)
    for r in rows: ws.append([r.get(c, "") for c in cols])
    for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496")
    ws.freeze_panes = "B2"; ws.auto_filter.ref = ws.dimensions
    for i, c in enumerate(cols, 1): ws.column_dimensions[get_column_letter(i)].width = min(60, max(12, len(c) + 2))
    with open(S / "out" / f"{name.replace(' ', '_')}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(rows)
(S / "out").mkdir(exist_ok=True)
wb = Workbook()
sheet(wb, "Pins and Method", [{"key": k, "value": v} for k, v in pins], first=True)
sheet(wb, "Existing Registry", ex_rows)
sheet(wb, "Incoming Review", in_rows)
sheet(wb, "Identity Crosswalk", xw)
sheet(wb, "Niche Summary", summ)
qo = sorted(q, key=lambda r: ({"B1": 0, "B2": 1, "B3": 2, "": 3}[r["proposed_batch"]], {"NEW_FULL_SNAPSHOT": 0, "GAP_FILL": 1, "REUSE": 2, "HOLD": 3}[r["proposed_action"]], r["primary_niche"]))
sheet(wb, "Apify Queue", qo)
for nm in ["FINANCE", "ECONOMICS", "SENIOR_HEALTH", "HISTORY"]:
    rows = [dict(population="EXISTING", **{k: r[k] for k in ("canonical_channel_id", "channel_name", "sub_niche", "confidence")}) for r in ex_rows if r["primary_niche"] == nm]
    rows += [dict(population="INCOMING", canonical_channel_id=r["canonical_channel_id"], channel_name=r["live_title"], sub_niche=r["sub_niche"], confidence=r["confidence"], db_membership=r["db_membership"]) for r in in_rows if r["primary_niche"] == nm and r["db_membership"] == "NEW_TO_DB"]
    sheet(wb, f"Filter {nm.title().replace('_',' ')}", rows)
wb.save(S / "out" / "YIOS_STAGE_A_CHANNEL_CLASSIFICATION_2026-11-10.xlsx")
b1 = [r for r in qo if r["proposed_batch"] == "B1"]
print("B1", len(b1), sum(r["result_limit_total"] for r in b1), round(sum(r["est_cost_usd"] for r in b1), 3))
for a in ("NEW_FULL_SNAPSHOT", "GAP_FILL", "REUSE", "HOLD"):
    print(a, collections.Counter((r["proposed_batch"]) for r in q if r["proposed_action"] == a))
print(json.dumps(summ, indent=0)[:3000])
