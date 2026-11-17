"""Phase 7 (owner brief of 2026-11-04, session d2a98830 msg 9): structured links
channel -> video -> source hash -> state/event -> evidence locator -> observation -> production rule -> specification -> test result.
Deterministic; links ONLY what the manual v0.7 section-6 table explicitly cites; everything else is reported as issue. No new infrastructure, no catalog writes.
Outputs: campaign/knowledge_links_v1.csv (edges), knowledge_links_v1_issues.csv. Usage: python3 -I xk_knowledge_links.py <ws>"""
import csv, json, re, hashlib, pathlib, sys
W = pathlib.Path(sys.argv[1]); CH = "UC6IxnFzHofFJ5X2PycSMsww"; MAN = "campaign/CHANNEL_PRODUCTION_MANUAL_v0.7.md"
VER = dict(manual="v0.7", ledger="ledger_v1 (built videos)", spec="RT4_916/spec_s6.md")
edges, issues = [], []
def E(ft, fi, tt, ti, kc, loc, st="LINKED"): edges.append(dict(from_type=ft, from_id=fi, to_type=tt, to_id=ti, knowledge_class=kc, source_locator=loc, version=VER["manual"], status=st))
def I(kind, ref, why): issues.append(dict(kind=kind, ref=ref, detail=why))
cat = set(json.load(open(W / "census/catalog_ch000004_ids.json")))
census = {r["video_id"]: r for r in csv.DictReader(open(W / "census/census.csv"))} if (W / "census/census.csv").exists() else {}
sha = json.load(open(W / "campaign/source_hashes_all_2026-11-06.json"))
for v in sorted(census or cat):
    E("channel", CH, "video", v, "CHANNEL_OBSERVATION", "census/census.csv", "LINKED" if v in cat else "NOT_IN_PROJECT_CATALOG_CH000004")
    if v in sha: E("video", v, "source_hash", sha[v]["sha256"], "CHANNEL_OBSERVATION", "campaign/source_hashes_all_2026-11-06.json")
    else: I("MISSING_SOURCE_HASH", v, "no local source / not hashed")
text = (W / MAN).read_text(); sec = text.split("## 6.")[1].split("\n## 7.")[0]
rows = [l for l in sec.splitlines() if l.startswith("|") and not l.startswith("|---") and "Device" not in l.split("|")[1]]
spec_txt = (W / "reconstruction/RT4_916/spec_s6.md").read_text()
rt4 = {r["device"] for r in csv.DictReader(open(W / "reconstruction/RT4_916/attempt_2/RT1_intended_timeline.csv"))}
DEV = {"Pop-on": "pop", "Write-on type": "write", "Write-on stroke": "stroke", "Slide/pan": "slide", "State swap": "swap"}
cite = re.compile(r"([A-Za-z0-9_-]{11}) (G\d{4})((?:[–/]G?\d{4})*)")
def segs(a, tail):
    out = [a]; 
    for sep, b in re.findall(r"([–/])(G?\d{4})", tail):
        b = b if b.startswith("G") else "G" + b
        out.append((sep, b))
    return out
for n, l in enumerate(rows, 1):
    c = [x.strip() for x in l.strip("|").split("|")]; rid = f"MAN07-S6-R{n:02d}"; dev = c[0]
    E("production_rule", rid, "specification", MAN + " §6 + §9", "CAMPAIGN_RULE", f"{MAN} §6 row '{dev}'")
    if any(k in dev for k in DEV):
        k = next(DEV[x] for x in DEV if x in dev)
        (E("production_rule", rid, "test_result", "RT4_916/attempt_2 (26/26 events, portrait silent PASS)", "CAMPAIGN_RULE", "reconstruction/RT4_916/RT4_FULL_VISUAL_REVIEW.md") if k in rt4 else I("RULE_DEVICE_NOT_IN_RT4", rid, dev))
    else: I("RULE_NO_LINKED_TEST", rid, f"{dev}: no RT4 intended event uses this device; RT1–RT3 not machine-linked")
    found = 0
    for v, s, tail in cite.findall(c[3]):
        S = list(csv.DictReader(open(W / "videos" / v / "tables/state_ledger.csv"))) if (W / "videos" / v / "tables/state_ledger.csv").exists() else None
        if S is None: I("CITED_VIDEO_NO_LEDGER", rid, f"{v} {s}"); continue
        names = [s]
        for sep, b in re.findall(r"([–/])(G?\d{4})", tail):
            b = b if b.startswith("G") else "G" + b
            if sep == "–":
                ids = [r["seg"] for r in S]; 
                if s in ids and b in ids: names = ids[ids.index(s):ids.index(b) + 1]
                else: names.append(b)
            else: names.append(b)
        for g in names:
            r = next((x for x in S if x["seg"] == g), None)
            if not r: I("BROKEN_SEG_REF", rid, f"{v} {g} not in state_ledger"); continue
            found += 1; sid = f"{v}:{g}"
            E("video", v, "state_event", sid, "CHANNEL_OBSERVATION", f"videos/{v}/tables/state_ledger.csv frames {r['start_frame']}-{r['end_frame']}")
            sh = list(csv.DictReader(open(W / "videos" / v / "tables/sheet_index.csv"))); sheets = sorted({x["sheet"] for x in sh if x["seg"] == g})
            strip = list(csv.DictReader(open(W / "videos" / v / "tables/strip_index.csv"))) if (W / "videos" / v / "tables/strip_index.csv").exists() else []
            loc = ";".join(f"videos/{v}/frames/sheets/{x}" for x in sheets) + ("".join(f";videos/{v}/frames/strips/{x['strip']}" for x in strip if x["seg"] == g))
            E("state_event", sid, "evidence_locator", loc or "NONE", "CHANNEL_OBSERVATION", f"videos/{v}/tables/sheet_index.csv|strip_index.csv", "LINKED" if loc else "NO_LOCATOR")
            if not loc: I("NO_EVIDENCE_LOCATOR", sid, "segment absent from sheet_index/strip_index")
            E("evidence_locator", sid, "observation", f"{r['event_class']}:{r['subtype']}", "CHANNEL_OBSERVATION", f"videos/{v}/tables/state_ledger.csv#{g} (reviewer {r['reviewer']}, confidence {r['confidence']})")
            E("observation", f"{r['event_class']}:{r['subtype']}", "production_rule", rid, "CAMPAIGN_RULE", f"{MAN} §6 evidence cell cites {v} {g}")
            if f"{v} {g}" in spec_txt or f"{v} {g}".replace(" ", " ") in spec_txt: E("production_rule", rid, "specification", f"RT4_916/spec_s6.md cites {v} {g}", "CAMPAIGN_RULE", "reconstruction/RT4_916/spec_s6.md")
    if not found: I("RULE_NO_SEG_CITATION", rid, f"{dev}: evidence cell '{c[3][:60]}' has no video+segment citation")
for name, rs in (("knowledge_links_v1.csv", edges), ("knowledge_links_v1_issues.csv", issues)):
    w = csv.DictWriter(open(W / "campaign" / name, "w", newline=""), fieldnames=list(rs[0]) if rs else ["none"]); w.writeheader(); w.writerows(rs)
from collections import Counter
print(len(edges), "edges;", len(issues), "issues;", dict(Counter(e["to_type"] for e in edges)), dict(Counter(i["kind"] for i in issues)))
