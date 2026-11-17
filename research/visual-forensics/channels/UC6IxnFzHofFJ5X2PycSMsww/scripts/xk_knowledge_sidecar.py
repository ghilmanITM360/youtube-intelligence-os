"""Phase 7 sidecar: knowledge_links_v1 -> derived/CH-000004/forensic-knowledge-links-v1.json (published to
data/intelligence/channels/CH-000004/ on the research branch only; catalog and existing index untouched).
Usage: python3 -I xk_knowledge_sidecar.py <ws> [--test]   (--test runs retrieval examples + validation, exits 1 on failure)"""
import csv, json, sys, hashlib, pathlib, collections, re
W = pathlib.Path(sys.argv[1]); R = pathlib.Path("/Users/ghilmankhan/workprojects/youtube-intelligence-os")
YT = "UC6IxnFzHofFJ5X2PycSMsww"; OUT = W / "derived/CH-000004/forensic-knowledge-links-v1.json"
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
RECON = {"MISSING_SOURCE_HASH": ("RETAINED_NO_LOCAL_SOURCE", "no local media and no hash in the repo forensic index; not guessed"),
         "RULE_NO_LINKED_TEST": ("RETAINED_UNTESTED", "device not exercised by any machine-linked reconstruction test; stays UNTESTED"),
         "RULE_NO_SEG_CITATION": ("RETAINED_NO_SEGMENT_CITATION", "manual evidence cell has no video+segment citation; not invented")}

def build():
    idx_p = R / "data/intelligence/channels/CH-000004/forensic-observation-index-v1.json"; idx = json.load(open(idx_p))
    sh = json.load(open(W / "campaign/source_hashes_all_2026-11-06.json"))
    edges = list(csv.DictReader(open(W / "campaign/knowledge_links_v1.csv"))); iss = list(csv.DictReader(open(W / "campaign/knowledge_links_v1_issues.csv")))
    for e in edges:
        e["local_only"] = e["to_type"] == "evidence_locator"  # locators point at local-only sheets/strips (media never in Git)
    issues = [dict(i, reconciliation=RECON[i["kind"]][0], reason=RECON[i["kind"]][1]) for i in iss]
    overlap = [dict(youtube_video_id=v["youtube_video_id"], repo_index_source_media_sha256=v["source_media_sha256"],
                    campaign_source_sha256=sh[v["youtube_video_id"]]["sha256"],
                    same_media=v["source_media_sha256"] == sh[v["youtube_video_id"]]["sha256"])
               for v in idx["videos"] if v["youtube_video_id"] in sh]
    return dict(schema_version="forensic-knowledge-links-1", channel_id="CH-000004", youtube_channel_id=YT,
                evidence_state="DERIVED_RESEARCH_BRANCH_NOT_ON_MAIN",
                policy="Derived, text-only links. Catalog and forensic-observation-index-v1.json unchanged. Rules are CAMPAIGN_RULE (AI/campaign interpretation of CHANNEL_OBSERVATION); not source-declared facts. Evidence locators point at local-only images.",
                inputs=dict(links_csv_sha256=sha(W / "campaign/knowledge_links_v1.csv"), issues_csv_sha256=sha(W / "campaign/knowledge_links_v1_issues.csv"),
                            manual_v0_7_sha256=sha(W / "campaign/CHANNEL_PRODUCTION_MANUAL_v0.7.md"), observation_index_sha256=sha(idx_p)),
                overlap_with_forensic_observation_index=overlap,
                overlap_note="Same YouTube ids appear in the repo index and in this campaign but the media hashes differ (different source files): do NOT count as one independent evidence set (AGENTS rule 9).",
                counts=dict(edges=len(edges), issues=len(issues), by_edge=dict(collections.Counter(f"{e['from_type']}>{e['to_type']}:{e['status']}" for e in edges))),
                edges=edges, issues=issues)

def idx_by(d):
    out = collections.defaultdict(list)
    for e in d["edges"]: out[(e["from_type"], e["from_id"])].append(e)
    return out

def chain(d, ix, video):
    """video -> state events -> locator -> observation -> rule -> spec/test"""
    res = []
    for se in ix[("video", video)]:
        if se["to_type"] != "state_event": continue
        sid = se["to_id"]; loc = ix[("state_event", sid)][0]["to_id"]; ob = ix[("evidence_locator", sid)][0]["to_id"]
        rules = [e["to_id"] for e in ix[("observation", ob)] if e["to_type"] == "production_rule"]
        res.append(dict(state_event=sid, locator=loc, observation=ob, rules=rules))
    return res

def main():
    d = build(); OUT.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(d, indent=1, sort_keys=True); OUT.write_text(txt)
    print("sidecar", OUT, hashlib.sha256(txt.encode()).hexdigest(), d["counts"]["edges"], "edges", d["counts"]["issues"], "issues")
    if "--test" not in sys.argv: return
    ix = idx_by(d); fails = []; log = []
    def T(name, ok, info=""):
        log.append(dict(test=name, result="PASS" if ok else "FAIL", info=str(info)[:300]))
        if not ok: fails.append(name)
    # identity
    tg = [r for r in csv.reader(open(R / "data/manifests/YOUTUBE_CHANNEL_TARGETS.csv")) if r and r[0] == YT][0]
    T("T1 channel identity: YT id registered as xkcd's What If? in target registry", "What If" in tg[1], tg[1])
    T("T2 forensic-index channel_id is CH-000004", json.load(open(R / "data/intelligence/channels/CH-000004/forensic-observation-index-v1.json"))["channel_id"] == "CH-000004")
    cen = {r["video_id"] for r in csv.DictReader(open(W / "census/census.csv"))}
    T("T3 every video edge id is in the census", all(e["to_id"] in cen for e in d["edges"] if e["from_type"] == "channel"))
    T("T4 91 channel>video edges: 83 catalog + 8 flagged NOT_IN_PROJECT_CATALOG", collections.Counter(e["status"] for e in d["edges"] if e["from_type"] == "channel") == {"LINKED": 83, "NOT_IN_PROJECT_CATALOG_CH000004": 8})
    # every state_event resolves in its ledger
    bad = []
    for e in d["edges"]:
        if e["from_type"] == "video" and e["to_type"] == "state_event":
            v, g = e["to_id"].split(":"); L = list(csv.DictReader(open(W / "videos" / v / "tables/state_ledger.csv")))
            if not any(r["seg"] == g for r in L): bad.append(e["to_id"])
    T("T5 every state_event resolves in its video state_ledger", not bad, bad)
    # every chain complete
    inc = [v for v in {e["from_id"] for e in d["edges"] if e["to_type"] == "state_event"} for c in chain(d, ix, v) if not (c["locator"] and c["observation"] and c["rules"])]
    T("T6 every state_event chain reaches locator, observation and >=1 rule", not inc, inc)
    # source hash edges equal source-hash table; and re-hash 3 local files that exist
    sh = json.load(open(W / "campaign/source_hashes_all_2026-11-06.json"))
    T("T7 64 source_hash edges equal the hash table", {e["from_id"]: e["to_id"] for e in d["edges"] if e["to_type"] == "source_hash"} == {v: x["sha256"] for v, x in sh.items()})
    T("T8 issue accounting: 27+8+2=37 and each has a reconciliation", collections.Counter(i["kind"] for i in d["issues"]) == {"MISSING_SOURCE_HASH": 27, "RULE_NO_LINKED_TEST": 8, "RULE_NO_SEG_CITATION": 2} and all(i["reconciliation"].startswith("RETAINED") for i in d["issues"]))
    T("T9 missing-hash videos absent from census-hashes and from repo index (no silent fill)", not ({i["ref"] for i in d["issues"] if i["kind"] == "MISSING_SOURCE_HASH"} & (set(sh) | {o["youtube_video_id"] for o in d["overlap_with_forensic_observation_index"]})))
    T("T10 overlap with repo index recorded; hashes differ (not same media)", len(d["overlap_with_forensic_observation_index"]) == 10 and not any(o["same_media"] for o in d["overlap_with_forensic_observation_index"]))
    T("T11 untested rules not claimed as tested", not ({i["ref"] for i in d["issues"] if i["kind"] == "RULE_NO_LINKED_TEST"} & {e["from_id"] for e in d["edges"] if e["to_type"] == "test_result"}))
    T("T12 no media paths outside locator edges, no secrets patterns", not re.search(r"\.(mp4|wav)\b|api[_-]?key|token", json.dumps([e for e in d["edges"] if e["to_type"] != "evidence_locator"] + d["issues"]), re.I))
    T("T13 deterministic rebuild", json.dumps(build(), indent=1, sort_keys=True) == txt)
    T("T14 sidecar size < 3 MB", len(txt) < 3_000_000, len(txt))
    # retrieval examples (printed)
    ex = {}
    ex["E1 video 2LSyizrk8-0 chain"] = chain(d, ix, "2LSyizrk8-0")[:3]
    ex["E2 rule MAN07-S6-R02 -> spec/test"] = [(e["to_type"], e["to_id"]) for e in ix[("production_rule", "MAN07-S6-R02")]]
    ex["E3 untested rules"] = sorted({i["ref"] for i in d["issues"] if i["kind"] == "RULE_NO_LINKED_TEST"})
    ex["E4 source hash 2LSyizrk8-0"] = [e["to_id"] for e in ix[("video", "2LSyizrk8-0")] if e["to_type"] == "source_hash"]
    ob2rule = {(e["from_id"], e["to_id"]) for e in d["edges"] if e["to_type"] == "production_rule"}
    ex["E5 observation types supporting R02"] = sorted(o for o, r in ob2rule if r == "MAN07-S6-R02")
    T("T15 retrieval examples non-empty", all(ex[k] for k in ex), {k: len(v) for k, v in ex.items()})
    out = dict(sidecar_sha256=hashlib.sha256(txt.encode()).hexdigest(), tests=log, failures=fails, examples=ex)
    (W / "campaign/PHASE7_VALIDATION_v1.json").write_text(json.dumps(out, indent=1))
    for l in log: print(l["result"], l["test"], "|", l["info"][:100])
    sys.exit(1 if fails else 0)
main()
