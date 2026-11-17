"""Build closure_v1/reconstruction_blueprint_v2.md from the rv1 state ledger + viewed corrections.
usage: blueprint_v2.py <id> <corrections.json>  (json: {"global": str, "states": {"VSxxx": "corrected prompt"}, "motion": str, "continuity": str})"""
import csv, json, sys, pathlib
v = sys.argv[1]; C = json.load(open(sys.argv[2]))
b = pathlib.Path.home() / f"YIOS-local-audits/xkcd-whatif/videos/{v}"
rows = list(csv.DictReader(open(b / "tables/state_ledger.csv"))); man = json.load(open(b / "source_manifest.json"))["source"]
L = [f"# Reconstruction blueprint v2 — {v} (closure v1; rv1 blueprint unchanged)",
     "Use A = internal evidence-matched test only (source art, script, voice, names and branding are not reusable). Use B = ORIGINAL transfer: new subject and drawings, PROMPT_PACK_v2 locks and original branding; never the source logo, title lockup, creator name or recurring characters.",
     f"Global: {man['resolution']}, 24 fps CFR, {man['decoded_frames']} f. {C['global']}", "",
     "| State | Frames | Enter (event @frame, length) | Image prompt (rv1 description verified on native/half-scale view; corrections applied) |", "|---|---|---|---|"]
prev = None
for r in rows:
    if r["kind"] == "ACTIVITY": prev = r; continue
    vs = r["visual_state_id"]; ent = "first frame" if prev is None else f"{prev['subtype']} @f{prev['start_frame']}, {prev['frames']} f"
    desc = C["states"].get(vs, r["description"]).replace("|", "/")
    L.append(f"| {vs} | {r['start_frame']}–{r['end_frame']} | {ent} | {desc} |"); prev = None
L += ["", f"Motion: {C['motion']}", f"Continuity: {C['continuity']}",
      "QA: (1) use A frame compare per state at native res; (2) every onset within ±1 frame of the ledger; (3) pops change on exactly 1 frame, multi-frame events match the measured curve (activity_curves.csv); (4) holds still (<0.1% changed px excluding grain); (5) all text exactly as transcribed in CLOSURE.md and legible at 320 px width; (6) use B originality check.",
      "Not done: per-video render test (not required by contract v1)."]
(b / "closure_v1/reconstruction_blueprint_v2.md").write_text("\n".join(L) + "\n"); print(len(L), "lines")
