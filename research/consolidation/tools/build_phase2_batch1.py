#!/usr/bin/env python3
"""Phase 2 batch 1: rebuild the consolidation maps. Read-only on every source.

Writes only into research/consolidation/ (next to this tools/ dir):
  VISUAL_EVIDENCE_MAP.csv, VISUAL_SEAL_VERIFICATION.csv,
  FINANCE_1612_RECONCILIATION.csv, PHASE2_BATCH1_FACTS.json

Inputs (all read-only): local MP4s (hashed again), local ledgers under ~/YIOS-local-audits,
the repo working tree, `git show` of pinned refs, and the registry DB opened mode=ro&immutable=1.
Run from the repo root:  python3 research/consolidation/tools/build_phase2_batch1.py
"""
import csv, glob, hashlib, io, json, os, re, sqlite3, subprocess, sys, collections

HOME = os.path.expanduser("~")
ROOT = os.getcwd()
OUT = os.path.join(ROOT, "research/consolidation")
MEDIA = f"{HOME}/Downloads/videos in mp3"
AUD = f"{HOME}/YIOS-local-audits"
XK = f"{AUD}/xkcd-whatif"
CT = f"{XK}/asset_library/_channel/ct_closure"
CF = f"{AUD}/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104"
FIN_REF = "origin/fix/finance-audit-validators"      # #45 tip
MB_REF = "origin/research/local-channel-media-library"  # #41 (Machine B media manifest)
FOLDERS = ["BarelyEvolved-MP4", "CasuallyFinance", "MonkeBiznis-MP4", "PrimateEconomics-MP4",
           "PrimitiveEducation-MP4", "casual_economics", "xkcd Channel"]


def git(*a, raw=False):
    r = subprocess.run(["git", *a], capture_output=True, cwd=ROOT)
    return r.stdout if raw else r.stdout.decode()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def write_csv(name, rows, fields):
    with open(f"{OUT}/{name}", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


facts = {}

# ---------- 1. local MP4 inventory (fresh SHA-256) ----------
cf_manifest = {r["file"]: r for r in csv.DictReader(open(f"{AUD}/CF_TRANSCRIPTS_ASR_20261109/manifest.csv", encoding="utf-8"))}
mb_text = git("show", f"{MB_REF}:research/media-library/MEDIA_MASTER.csv")
machine_b_shas = {r["sha256"] for r in csv.DictReader(io.StringIO(mb_text)) if r["asset_type"] == "VIDEO"}
census = {r["video_id"]: r for r in csv.DictReader(open(f"{XK}/census/census.csv", encoding="utf-8"))}
xk_ledger = {r["video_id"]: r for r in csv.DictReader(open(f"{CT}/CLOSURE_LEDGER_v1.csv", encoding="utf-8"))}
cf_ledger = json.load(open(f"{CF}/visual_complete_ledger.json"))
cf_baseline = {r["video_id"]: r for r in json.load(open(f"{CF}/source_identity_baseline_v1.json"))["rows"]}
cf_closed = {e["video_id"] for e in cf_ledger["videos"]}
cf_index = {r["video_id"]: r for r in csv.DictReader(open("research/casually-finance/INDEX.csv", encoding="utf-8"))}

tree = git("ls-tree", "-r", "--name-only", "HEAD").split("\n")
def published_dir(vid):
    d = f"research/visual-forensics/channels/casual-finance/{vid}"
    return d if any(f.startswith(d + "/") for f in tree) else "LOCAL_ONLY"

rows, seen_local_ids = [], collections.defaultdict(set)
for folder in FOLDERS:
    for fn in sorted(os.listdir(f"{MEDIA}/{folder}")):
        if not fn.endswith(".mp4"):
            continue
        p = f"{MEDIA}/{folder}/{fn}"
        m = re.search(r"\[([A-Za-z0-9_-]{11})\]\.mp4$", fn)
        vid = m.group(1) if m else ""
        how = "ID_IN_NAME" if m else ""
        if folder == "CasuallyFinance" and fn in cf_manifest:
            mr = cf_manifest[fn]
            vid, how = mr["video_id"] or vid, mr["match"]
        sha = sha_file(p)
        row = dict(channel_folder=folder, video_id=vid, id_match=how or "UNMAPPED",
                   mp4_relpath=f"{folder}/{fn}", size_bytes=os.path.getsize(p), sha256=sha,
                   in_machine_b_manifest_41=sha in machine_b_shas,
                   visual_status="NOT_CLOSED", closure_source="", failing_gates="", closed_utc="",
                   ledger_sha_matches_file="", published_evidence="LOCAL_ONLY", av_status="BLOCKED")
        if folder == "CasuallyFinance" and vid in cf_closed:
            row.update(visual_status="VISUAL_ANALYSIS_COMPLETE", closure_source="CF visual_complete_ledger.json + count_complete.py",
                       ledger_sha_matches_file=str(cf_baseline[vid]["sha256"] == sha) if vid in cf_baseline else "NO_BASELINE",
                       failing_gates="none", published_evidence=published_dir(vid))
        if folder == "xkcd Channel" and vid in xk_ledger:
            L = xk_ledger[vid]
            row.update(visual_status=L["status"], closure_source=f"xkcd CLOSURE_LEDGER_v1.csv ({L['format']})",
                       failing_gates=L["failing_gates"], closed_utc=L["closed_utc"],
                       ledger_sha_matches_file=str(L["source_sha256"] == sha))
        if folder == "CasuallyFinance" and vid in cf_index:
            row["transcript_state"] = "ASR_UNCERTIFIED"
        rows.append(row)
        seen_local_ids[folder].add(vid)

# catalog IDs with no local file (xkcd census)
for vid, c in census.items():
    if vid not in seen_local_ids["xkcd Channel"]:
        rows.append(dict(channel_folder="xkcd Channel", video_id=vid, id_match="NO_LOCAL_FILE", mp4_relpath="",
                         size_bytes="", sha256="", in_machine_b_manifest_41="", visual_status="NO_SOURCE_MEDIA",
                         closure_source="census.csv", failing_gates="", closed_utc="", ledger_sha_matches_file="",
                         published_evidence="LOCAL_ONLY", av_status="BLOCKED"))
for vid in cf_index:
    if vid not in seen_local_ids["CasuallyFinance"]:
        rows.append(dict(channel_folder="CasuallyFinance", video_id=vid, id_match="NO_LOCAL_FILE", mp4_relpath="",
                         size_bytes="", sha256="", in_machine_b_manifest_41="", visual_status="NO_SOURCE_MEDIA",
                         closure_source="", failing_gates="", closed_utc="", ledger_sha_matches_file="",
                         published_evidence="LOCAL_ONLY", av_status="BLOCKED"))
for r in rows:
    r.setdefault("transcript_state", "")
fields = ["channel_folder", "video_id", "id_match", "mp4_relpath", "size_bytes", "sha256", "in_machine_b_manifest_41",
          "visual_status", "closure_source", "failing_gates", "closed_utc", "ledger_sha_matches_file",
          "published_evidence", "transcript_state", "av_status"]
write_csv("VISUAL_EVIDENCE_MAP.csv", rows, fields)
files = [r for r in rows if r["sha256"]]
facts["mp4"] = dict(files=len(files), distinct_sha=len({r["sha256"] for r in files}),
                    bytes=sum(int(r["size_bytes"]) for r in files),
                    unmapped_files=sum(1 for r in files if not r["video_id"]),
                    in_machine_b_manifest=sum(1 for r in files if r["in_machine_b_manifest_41"]),
                    by_folder=dict(collections.Counter(r["channel_folder"] for r in files)))
facts["cf_closed"] = dict(count=len(cf_closed),
                          sha_match=sum(1 for r in rows if r["channel_folder"] == "CasuallyFinance" and r["visual_status"] == "VISUAL_ANALYSIS_COMPLETE" and r["ledger_sha_matches_file"] == "True"),
                          published=sorted(r["video_id"] for r in rows if r["visual_status"] == "VISUAL_ANALYSIS_COMPLETE" and r["channel_folder"] == "CasuallyFinance" and r["published_evidence"] != "LOCAL_ONLY"),
                          local_only=sorted(r["video_id"] for r in rows if r["visual_status"] == "VISUAL_ANALYSIS_COMPLETE" and r["channel_folder"] == "CasuallyFinance" and r["published_evidence"] == "LOCAL_ONLY"))
xr = [r for r in rows if r["channel_folder"] == "xkcd Channel"]
facts["xkcd"] = dict(census=len(census), rows=len(xr), closed=sum(1 for r in xr if r["visual_status"] == "VISUAL_ANALYSIS_COMPLETE"),
                     closed_by_format=dict(collections.Counter(xk_ledger[r["video_id"]]["format"] for r in xr if r["visual_status"] == "VISUAL_ANALYSIS_COMPLETE")),
                     ledger_sha_mismatch=[r["video_id"] for r in xr if r["ledger_sha_matches_file"] == "False"],
                     no_local=[r["video_id"] for r in xr if r["id_match"] == "NO_LOCAL_FILE"])

# ---------- 2. seal verification ----------
LIVING = re.compile(r"(CLOSURE_LEDGER_v1\.csv|CT_CLOSURE_HANDOFF_v\d+\.md)$")

def verify_seal(seal, extra_bases=()):
    """Per entry: look in the seal's own base dir first, then in extra_bases (local workspace).
    ok_here = verified next to the seal; ok_extra = verified only in an extra base (heavy evidence kept local)."""
    ents = []
    for ln in open(seal, encoding="utf-8", errors="replace"):
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+?)\s*$", ln)
        if m:
            ents.append((m.group(1), m.group(2)))
    if not ents:
        return dict(entries=0, ok_here=0, ok_extra=0, differs=0, missing=0, base="", detail="NO_PARSEABLE_ENTRIES", living_only=False)
    d = os.path.dirname(os.path.abspath(seal))
    cands, cur = [], d
    for _ in range(6):
        cands.append(cur); cur = os.path.dirname(cur)
    base = max(cands, key=lambda b: sum(1 for _, p in ents[:40] if os.path.exists(os.path.join(b, p))))
    ok_here = ok_extra = differs = missing = 0
    bad, bad_paths = [], []
    for h, p in ents:
        hit = None
        for tag, b in [("here", base)] + [("extra", e) for e in extra_bases]:
            fp = os.path.join(b, p)
            if os.path.isfile(fp):
                hit = (tag, sha_file(fp) == h)
                if hit[1]:
                    break
        if hit is None:
            missing += 1; bad.append("MISSING " + p)
        elif hit[1]:
            ok_here += hit[0] == "here"; ok_extra += hit[0] == "extra"
        else:
            differs += 1; bad.append("DIFFERS " + p); bad_paths.append(p)
    return dict(entries=len(ents), ok_here=ok_here, ok_extra=ok_extra, differs=differs, missing=missing,
                base=base.replace(HOME, "~"), detail="; ".join(bad[:6]) + (" ..." if len(bad) > 6 else ""),
                living_only=bool(bad_paths) and all(LIVING.search(x) for x in bad_paths) and missing == 0)

seals = sorted(glob.glob(f"{CT}/SHA256SUMS*")) + sorted(glob.glob(f"{CF}/SHA256SUMS*"))
seals += sorted(glob.glob(f"{ROOT}/research/visual-forensics/channels/casual-finance/*/**/EVIDENCE_SHA256SUMS", recursive=True))
seal_rows = []
for s in seals:
    extra = ()
    m = re.search(r"casual-finance/([^/]+)/", s)
    if m:
        extra = (f"{AUD}/2026-11-08-{m.group(1)}-deep-ct-scan", f"{AUD}/2026-10-24-{m.group(1)}-deep-ct-scan")
    v = verify_seal(s, extra)
    scope = "xkcd ct_closure" if s.startswith(CT) else ("CF target (local)" if s.startswith(CF) else "CF published (repo tree)")
    if not v["entries"]:
        status = "EMPTY"
    elif not v["differs"] and not v["missing"]:
        status = "PASS" if not v["ok_extra"] else "PASS_HEAVY_FILES_LOCAL_ONLY"
    elif v["living_only"]:
        status = "SUPERSEDED_LIVING_FILE"
    else:
        status = "FAIL"
    seal_rows.append(dict(scope=scope, seal_file=s.replace(HOME, "~").replace(ROOT + "/", ""), status=status, **v))
write_csv("VISUAL_SEAL_VERIFICATION.csv", seal_rows,
          ["scope", "seal_file", "status", "entries", "ok_here", "ok_extra", "differs", "missing", "base", "detail"])
# frozen contract hash
contract_ok = open(f"{CT}/VISUAL_CLOSURE_CONTRACT_v1.sha256").read().split()
facts["contract_sha_ok"] = sha_file(f"{CT}/VISUAL_CLOSURE_CONTRACT_v1.md") in contract_ok
facts["seals"] = dict(files=len(seal_rows), by_scope_status={f"{k[0]}|{k[1]}": v for k, v in collections.Counter((r["scope"], r["status"]) for r in seal_rows).items()},
                      not_pass=[(r["seal_file"].split("/")[-1] if r["scope"]!="CF published (repo tree)" else r["seal_file"].split("/")[-3], r["status"], r["entries"], r["differs"], r["missing"]) for r in seal_rows if not r["status"].startswith("PASS")])

# ---------- 3. Finance 1,612 reconciliation ----------
P = "research/finance-economics-intelligence"
qtext = git("show", f"{FIN_REF}:{P}/FINANCE_CONTINUATION_QUEUE.csv", raw=True)
queue = list(csv.DictReader(io.StringIO(qtext.decode())))
master_bytes = git("show", f"{FIN_REF}:{P}/VIDEO_MASTER.csv", raw=True)
man = json.loads(git("show", f"{FIN_REF}:{P}/audit-baseline/MANIFEST.json"))
frozen_ids = {r["Video_ID"] for r in csv.DictReader(io.StringIO(git("show", f"{FIN_REF}:{P}/audit-baseline/VIDEO_IDS.csv")))}
db = sqlite3.connect("file:data/catalog/youtube_channel_registry.db?mode=ro&immutable=1", uri=True)
reg = {v: (c) for v, c in db.execute("select youtube_video_id, canonical_channel_id from videos")}
tr = {}
for v, ph in db.execute("select youtube_video_id, is_placeholder from transcripts"):
    tr[v] = "PLACEHOLDER" if ph else "REAL_TEXT"
DIMS = ["thumbnail_status", "topic_status", "title_status", "script_status", "performance_status", "virality_status"]
qblob = git("rev-parse", f"{FIN_REF}:{P}/FINANCE_CONTINUATION_QUEUE.csv").strip()
frows = []
for q in queue:
    v = q["video_id"]
    done = sum(1 for d in DIMS if q[d].startswith("COMPLETE"))
    frows.append(dict(
        video_id=v, population=q["population"], population_layer=q["population_layer"],
        channel_id=q["channel_id"], channel_name=q["channel_name"],
        in_frozen_966_ids=v in frozen_ids,
        in_registry_db=v in reg,
        registry_channel_matches_queue=(reg[v] == q["channel_id"]) if v in reg else "",
        registry_transcript=tr.get(v, "ABSENT_FROM_REGISTRY"),
        queue_transcript_completeness=q["transcript_completeness"],
        queue_eligibility=q["eligibility"], accepted_batch_id=q["accepted_batch_id"],
        accepted_commit=q["accepted_commit"], dims_complete_of_6=done))
write_csv("FINANCE_1612_RECONCILIATION.csv", frows,
          ["video_id", "population", "population_layer", "channel_id", "channel_name", "in_frozen_966_ids", "in_registry_db",
           "registry_channel_matches_queue", "registry_transcript", "queue_transcript_completeness", "queue_eligibility",
           "accepted_batch_id", "accepted_commit", "dims_complete_of_6"])
orig = [r for r in frows if r["population"] == "ORIGINAL"]
exp = [r for r in frows if r["population"] == "EXPANSION"]
acc = [r for r in frows if r["queue_eligibility"] == "ACCEPTED"]
facts["finance"] = dict(
    queue_rows=len(queue), distinct_ids=len({r["video_id"] for r in frows}),
    original=len(orig), expansion=len(exp), channels=len({r["channel_id"] for r in frows}),
    original_in_frozen_ids=sum(r["in_frozen_966_ids"] for r in orig), frozen_ids=len(frozen_ids),
    frozen_ids_missing_from_queue=len(frozen_ids - {r["video_id"] for r in frows}),
    original_in_registry=sum(r["in_registry_db"] for r in orig), expansion_in_registry=sum(r["in_registry_db"] for r in exp),
    expansion_in_frozen_ids=sum(r["in_frozen_966_ids"] for r in exp),
    registry_channel_mismatch=sum(1 for r in frows if r["registry_channel_matches_queue"] is False),
    registry_placeholder_in_queue=sum(1 for r in frows if r["registry_transcript"] == "PLACEHOLDER"),
    queue_placeholder=sum(1 for r in frows if r["queue_transcript_completeness"] == "PLACEHOLDER"),
    accepted=len(acc), accepted_by_population=dict(collections.Counter(r["population"] for r in acc)),
    dims_complete_distribution=dict(sorted(collections.Counter(r["dims_complete_of_6"] for r in frows).items())),
    all6_not_accepted=sum(1 for r in frows if r["dims_complete_of_6"] == 6 and r["queue_eligibility"] != "ACCEPTED"),
    accepted_not_all6=sum(1 for r in acc if r["dims_complete_of_6"] != 6),
    eligibility=dict(collections.Counter(r["queue_eligibility"] for r in frows)),
    pins=dict(queue_ref=FIN_REF, queue_ref_sha=git("rev-parse", FIN_REF).strip(), queue_blob=qblob,
              queue_file_sha256=hashlib.sha256(qtext).hexdigest(),
              video_master_sha256=hashlib.sha256(master_bytes).hexdigest(), frozen_master_sha256_in_manifest=man["frozen_master_sha256"],
              manifest_registry_sha256=man["source_hashes"]["data/catalog/youtube_channel_registry.db"],
              live_registry_sha256=sha_file("data/catalog/youtube_channel_registry.db")))
# per-channel original/expansion table
chan = collections.defaultdict(lambda: collections.Counter())
for r in frows:
    chan[r["channel_name"]][r["population"]] += 1
    chan[r["channel_name"]]["in_registry"] += r["in_registry_db"]
    chan[r["channel_name"]]["accepted"] += r["queue_eligibility"] == "ACCEPTED"
facts["finance_channels"] = {k: dict(v) for k, v in sorted(chan.items(), key=lambda kv: -sum(kv[1][p] for p in ("ORIGINAL", "EXPANSION")))}


# ---------- 4. pins of the local ledgers (new file; existing seals are not touched) ----------
pin_files = [f"{CT}/CLOSURE_LEDGER_v1.csv", f"{CT}/VISUAL_CLOSURE_CONTRACT_v1.md", f"{CT}/CT_CLOSURE_HANDOFF_v10.md",
             f"{XK}/census/census.csv", f"{XK}/census/census_summary.json", f"{XK}/asset_library/library_manifest.csv",
             f"{CF}/visual_complete_ledger.json", f"{CF}/source_identity_baseline_v1.json", f"{CF}/target_roster_v1.csv",
             f"{CF}/count_complete.py", f"{AUD}/CF_TRANSCRIPTS_ASR_20261109/manifest.csv",
             f"{ROOT}/data/catalog/youtube_channel_registry.db", f"{ROOT}/data/catalog/youtube_inventory.db"]
with open(f"{OUT}/LOCAL_EVIDENCE_PINS.sha256", "w") as f:
    for q in pin_files:
        f.write(f"{sha_file(q)}  {q.replace(HOME, '~')}\n")

json.dump(facts, open(f"{OUT}/PHASE2_BATCH1_FACTS.json", "w"), indent=1, sort_keys=True)
print(json.dumps(facts, indent=1, sort_keys=True)[:6000])
