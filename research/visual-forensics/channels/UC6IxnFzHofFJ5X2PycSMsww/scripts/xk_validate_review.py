"""Validate a reviewer's annotations + audit actual image reads in the subagent transcript.
Usage: python3 -I xk_validate_review.py <video_dir> <reviewer_id> <agent_id>
Writes review/<reviewer_id>/validation.json; exit 1 on any error."""
import csv, json, re, sys, hashlib, pathlib
V = pathlib.Path(sys.argv[1]).resolve(); RV = sys.argv[2]; AG = sys.argv[3]
R = V / "review" / RV
T = pathlib.Path(f"/Users/ghilmankhan/.claude/projects/-Users-ghilmankhan-workprojects-youtube-intelligence-os/d2a98830-292c-4d67-85e5-ec71a232e398/subagents/agent-{AG}.jsonl")
errs = []; warn = []
segs = list(csv.DictReader(open(V / "tables/segments_v1.csv")))
sheets = sorted({r["sheet"] for r in csv.DictReader(open(V / "tables/sheet_index.csv"))})
try:
    ann = list(csv.DictReader(open(R / "annotations.csv")))
except Exception as e:
    ann = []; errs.append(f"annotations unreadable: {e}")
if ann:
    if list(ann[0].keys()) != ["seg", "event_class", "subtype", "description", "confidence"]: errs.append(f"bad header {list(ann[0].keys())}")
    if [a["seg"] for a in ann] != [s["seg"] for s in segs]: errs.append("seg list/order mismatch")
    ok_cls = {"STATIC_HOLD", "SHOT_CUT", "GRAPHIC/TEXT", "CAMERA", "CHARACTER", "LIGHT/COLOR/EFFECT", "FALSE_POSITIVE"}
    kind = {s["seg"]: s["kind"] for s in segs}
    for a in ann:
        parts = a.get("event_class", "").split("+")
        if not parts or any(p not in ok_cls for p in parts): errs.append(f"{a['seg']} bad class {a.get('event_class')}")
        if kind.get(a["seg"]) == "HOLD" and a["event_class"] != "STATIC_HOLD": warn.append(f"{a['seg']} HOLD classed {a['event_class']}")
        if kind.get(a["seg"]) == "ACTIVITY" and a["event_class"] == "STATIC_HOLD": errs.append(f"{a['seg']} ACTIVITY classed STATIC_HOLD")
        if a.get("confidence") not in ("HIGH", "MEDIUM", "LOW"): errs.append(f"{a['seg']} bad confidence")
        if len((a.get("description") or "").strip()) < 8: errs.append(f"{a['seg']} empty description")
obs = R / "observations.md"
if not obs.exists() or len(obs.read_text().split()) < 150: errs.append("observations.md missing/short")
prov = {}
if T.exists():
    txt = T.read_text()
    reads = re.findall(r'"name":"Read","input":\{"file_path":"([^"]+)"', txt)
    sheet_reads = [p for p in reads if "/frames/sheets/" in p and str(V) in p]
    opened = sorted({pathlib.Path(p).name for p in sheet_reads})
    imgs = txt.count('"type":"image"')
    missing = [s for s in sheets if s not in opened]
    if missing: errs.append(f"sheets never opened: {missing}")
    if imgs < len(sheets): errs.append(f"image results {imgs} < sheets {len(sheets)}")
    other_writes = [p for p in re.findall(r'"name":"(?:Write|Edit)","input":\{"file_path":"([^"]+)"', txt) if not p.startswith(str(R))]
    if other_writes: errs.append(f"writes outside review dir: {other_writes}")
    prov = dict(transcript=str(T), transcript_sha256=hashlib.sha256(T.read_bytes()).hexdigest(), sheet_read_calls=len(sheet_reads),
                unique_sheets_opened=len(opened), image_results=imgs, sheets_expected=len(sheets))
else:
    errs.append(f"transcript not found {T}")
out = dict(video_id=V.name, reviewer=RV, agent_id=AG, rows=len(ann), segments=len(segs), errors=errs, warnings=warn, provenance=prov,
           unresolved=[a["seg"] for a in ann if "UNRESOLVED" in a.get("description", "") or a.get("confidence") == "LOW"],
           model_note="Claude Code subagent (sonnet); same vendor/model family as orchestrator; not human; no audio")
R.mkdir(parents=True, exist_ok=True); (R / "validation.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ("rows", "segments", "errors", "warnings", "unresolved")})[:1500], prov)
sys.exit(1 if errs else 0)
